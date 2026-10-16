#!/usr/bin/env python3
"""Render the Notion build prompt and the Sheets Lite template from schemas/hub.toml.

    python3 tools/hub_build_prompt.py --edition en|vn|all [--root PATH]

Per edition (docs/BUILD.md §6):
    dist/maintainer/notion-build-prompt-<edition>.md   the prompt Claude runs with the Notion connector
    dist/maintainer/sheets-<edition>/<Tab>.csv          one header row per tab; Start holds the steps
    dist/maintainer/sheets-<edition>/BUILD-NOTES.md     dropdowns, formats and Scoreboard formulas

Property names and option values are printed exactly as the schema has them
(English in both editions). Descriptions, view names and page text come from
strings/<edition>.toml: a description key with no string yet prints as the key
itself, a view or page label as its neutral English name, and every such key is
reported, so nothing goes silently blank. Output is deterministic.
"""
from __future__ import annotations

import argparse
import csv
import io
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cmlib  # noqa: E402
import cmschema  # noqa: E402
from cmlib import CMError  # noqa: E402

DB_ORDER = ("content", "series", "bank", "runs")
TYPE_LABEL = {
    "title": "Title", "rich_text": "Text", "select": "Select", "multi_select": "Multi-select",
    "status": "Status", "number": "Number", "date": "Date", "relation": "Relation", "url": "URL",
    "checkbox": "Checkbox",
}
WITHIN_TEXT = {"this_week": "this week", "next_30_days": "the next 30 days", "past_7_days": "the past 7 days"}
SHEET_KIND = {
    "title": "text", "rich_text": "text", "select": "dropdown", "multi_select": "dropdown (multiple)",
    "status": "dropdown", "number": "number", "date": "date (YYYY-MM-DD)", "relation": "text",
    "url": "link", "checkbox": "checkbox",
}
FIELD_GUIDE_KEY = "hub.page.start_here.field_guide"
SCOREBOARD_ROWS = 1000


@dataclass
class Result:
    edition: str
    paths: list[Path] = field(default_factory=list)
    missing: list[str] = field(default_factory=list)   # strings keys with no text yet


class Texts:
    """Edition strings for the hub, rendered with the template engine."""

    def __init__(self, ed: cmlib.Edition):
        self.ed = ed
        self.ctx = cmlib.make_ctx(ed, "help", path=f"strings/{ed.id}.toml")
        self.missing: list[str] = []

    def get(self, key: str, fallback: str | None = None) -> str:
        if key in self.ed.strings:
            return cmlib.nfc(cmlib.render_text(self.ed.strings[key], self.ctx)).strip()
        if key not in self.missing:
            self.missing.append(key)
        return key if fallback is None else fallback

    def render(self, text: str) -> str:
        return cmlib.nfc(cmlib.render_text(text, self.ctx))


# ---------------------------------------------------------------- small formatting helpers

def code(name: str) -> str:
    return f"`{name}`"


def codes(names) -> str:
    return ", ".join(code(n) for n in names)


def quoted(text: str) -> str:
    return '"' + " ".join(text.split()) + '"'


def cell(text: str) -> str:
    return " ".join(text.split()).replace("|", "\\|")


def sentence(text: str) -> str:
    text = text.strip()
    return text[:1].upper() + text[1:] + ("" if text.endswith((".", "!", "?")) else ".")


def page_name(hub: dict, pid: str, t: Texts) -> str:
    return t.render(hub["pages"][pid]["name"])


def ordered_dbs(hub: dict) -> list[str]:
    dbs = cmschema.databases(hub)
    return [d for d in DB_ORDER if d in dbs] + sorted(d for d in dbs if d not in DB_ORDER)


def number_setting(p: dict) -> str:
    parts = []
    lo, hi = (p.get("range") or [None, None])
    if lo is not None:
        parts.append(f"{lo} or more" if hi >= 1_000_000 else f"{lo}-{hi}")
    if p.get("number_format") == "number_with_commas":
        parts.append("number with commas")
    return " · ".join(parts)


def settings(hub: dict, p: dict) -> str:
    """The Options / settings cell for one property."""
    ptype = p["type"]
    if ptype in cmschema.OPTION_TYPES:
        text = codes(p["options"])
        if ptype == "status" and p.get("status_groups"):
            groups = "; ".join(f"{g}: {codes(v)}" for g, v in p["status_groups"].items())
            text += f" · groups: {groups}"
        if p.get("ai_may_set") and p.get("ai_may_set") != p["options"]:
            text += f" · the machine may set only {codes(p['ai_may_set'])}"
        return text
    if ptype == "relation":
        target = cmschema.databases(hub)[p["relation_to"]]["name"]
        if p.get("two_way"):
            return f"to {code(target)}, two-way (shows there as {code(p['synced_property'])})"
        return f"to {code(target)}, one-way (no property on the other side)"
    if ptype == "number":
        return number_setting(p)
    if ptype == "date":
        return "date only, no time"
    return ""


def filter_text(f: dict) -> str:
    prop, op, value = code(f["property"]), f["op"], f.get("value")
    if op == "is":
        return f"{prop} is {code(value)}"
    if op == "is_not":
        return f"{prop} is not {code(value)}"
    if op == "is_any_of":
        return f"{prop} is any of {codes(value)}"
    if op == "within":
        return f"{prop} is within {WITHIN_TEXT[value]}"
    return f"{prop} {op.replace('_', ' ')}"


# ---------------------------------------------------------------- the Notion prompt

def notion_prompt(hub: dict, t: Texts) -> str:
    ed = t.ed
    root = page_name(hub, "root", t)
    pages = hub["pages"]
    dbs = cmschema.databases(hub)
    field_guide = t.get(FIELD_GUIDE_KEY, "Field guide")
    out: list[str] = []
    add = out.append

    add(f"# Build the {root} board in Notion · {ed.file_suffix} edition")
    add("")
    add(f"> Maintainer note: generated by tools/hub_build_prompt.py from schemas/hub.toml "
        f"(schema v{hub.get('schema_version')}); rebuild it, never edit it by hand. Share one empty Notion "
        f"page named \"{root}\" with the Notion connector, open a new Claude chat with the connector on, "
        "and paste everything below the line.")
    add("")
    add("---")
    add("")
    add(f"You are building the {root} board template in Notion with the Notion connector. Follow the steps "
        "in order, exactly as written, then report back as step 6 says.")
    add("")
    add("## Ground rules")
    add("")
    rules = [
        "Every name in backticks is exact: page, database, property and option names keep the same "
        "spelling and letter case. They are English in every edition. Never translate, rename, reorder, "
        "merge or add any.",
        "Text in quotation marks (page text, view names, descriptions) is this edition's own wording. "
        "Copy it exactly, without the quotation marks.",
        f"Build everything inside the shared page {code(root)}. Delete nothing. If something with the right "
        "name already exists, keep it and add only what is missing.",
        "Set each property's description from the tables. If the connector cannot set property "
        f"descriptions, list them instead on the {code(pages['start_here']['name'])} page under a toggle named "
        f"{quoted(field_guide)}, one line per property: `Property`: description.",
        "If the connector cannot create a `status` property, create a `select` with the same options in "
        "the same order, and say so in your report.",
        f"Create the {len(dbs)} databases first, then the relations (step 3), then the views (step 4).",
        "Leave every database empty: no sample rows, no template rows.",
        "Items listed under \"Page body\" are not properties. The machine writes them into each row's "
        "page later; create nothing for them.",
    ]
    if ed.id != cmlib.EDITIONS[0]:
        rules.insert(2, "This is the Vietnamese edition: the quoted text is Vietnamese, while every name "
                        "in backticks stays English.")
    for i, rule in enumerate(rules, 1):
        add(f"{i}. {rule}")
    add("")

    # -- step 1: pages
    add("## Step 1 · Pages")
    add("")
    add(f"1. {code(root)} is the shared page. Its first paragraph: "
        + "; ".join(quoted(t.get(k)) for k in pages["root"].get("body_keys", [])) + ".")
    n = 2
    for pid in pages["root"].get("children", []):
        page = pages[pid]
        add(f"{n}. {code(page_name(hub, pid, t))}, a child page of {code(root)}.")
        n += 1
        if page.get("first_block_key"):
            add(f"   - First block: a callout with {quoted(t.get(page['first_block_key']))}. The machine "
                "replaces it with the newest Brand Card at Level 2; Notion's page history keeps old versions.")
        for key in page.get("body_keys", []):
            add(f"   - Paragraph: {quoted(t.get(key))}")
        if page.get("bank_heading_key"):
            add(f"   - Heading: {quoted(t.get(page['bank_heading_key']))}, with the "
                f"{code(dbs['bank']['name'])} database inline under it (step 2).")
        for child in page.get("children", []):
            sub = pages[child]
            add(f"   - Child page {code(page_name(hub, child, t))}: "
                + "; ".join(quoted(t.get(k)) for k in sub.get("body_keys", [])) + ".")
            if sub.get("sections"):
                add(f"     Leave the rest empty; the machine writes these parts later: "
                    f"{', '.join(sub['sections'])}.")
            if sub.get("brief_fields"):
                add(f"     Add a table with the columns `Field` and `Answer`, one row per field: "
                    f"{codes(sub['brief_fields'])}. Launch types: {codes(sub.get('launch_types', []))}.")
            ledger = sub.get("ledger")
            if ledger:
                checks = [t.get(k, en) for k, en in zip(ledger.get("check_keys", []), ledger.get("checks", []))]
                add(f"     Then a heading {quoted(t.get(ledger['heading_key']))} with a table whose columns "
                    f"are {codes(ledger['columns'])} and no rows, then these to-do items, unticked: "
                    + "; ".join(quoted(c) for c in checks) + ".")
    add("")

    # -- step 2: databases
    add("## Step 2 · Databases")
    add("")
    add(f"Create {len(dbs)} databases. " + " ".join(
        f"{code(dbs[d]['name'])} goes {'inline on' if dbs[d]['parent'] != 'root' else 'inside'} "
        f"{code(page_name(hub, dbs[d]['parent'], t))}." for d in ordered_dbs(hub)))
    add("")
    upsert_keys = hub.get("rules", {}).get("upsert_keys", {})
    for i, db_id in enumerate(ordered_dbs(hub), 1):
        db = dbs[db_id]
        add(f"### 2.{i} {code(db['name'])} · one row = {db.get('row', '')}")
        add("")
        add(f"Description: {quoted(t.get(db['description_key']))}")
        if upsert_keys.get(db_id):
            add(f"Key: {code(upsert_keys[db_id])}. It is unique: every write finds the row by it.")
        add("")
        add("| # | Property | Type | Options / settings | Description |")
        add("|---|---|---|---|---|")
        k = 0
        for p in cmschema.notion_properties(hub, db_id):
            k += 1
            add(f"| {k} | {code(p['name'])} | {TYPE_LABEL[p['type']]} (`{p['type']}`) | "
                f"{cell(settings(hub, p))} | {cell(quoted(t.get(p['description_key'])))} |")
        body = [p for p in cmschema.properties(hub, db_id) if p.get("page_body")]
        if body:
            add("")
            add("Page body, not properties: " + "; ".join(
                f"{code(p['name'])} ({quoted(t.get(p['description_key']))})" for p in body) + ".")
        add("")

    # -- step 3: relations
    add("## Step 3 · Relations")
    add("")
    done: set[tuple[str, str]] = set()
    for db_id in ordered_dbs(hub):
        for p in cmschema.properties(hub, db_id):
            if p["type"] != "relation" or (db_id, p["name"]) in done:
                continue
            target = p["relation_to"]
            if p.get("two_way"):
                done.add((target, p["synced_property"]))
                add(f"- {code(dbs[db_id]['name'])} {code(p['name'])} ↔ {code(dbs[target]['name'])} "
                    f"{code(p['synced_property'])}: one two-way relation, a property on each side.")
            else:
                same = " (the same database)" if target == db_id else ""
                add(f"- {code(dbs[db_id]['name'])} {code(p['name'])} → {code(dbs[target]['name'])}{same}: "
                    "one-way, no property on the other side.")
    add("")

    # -- step 4: views
    add("## Step 4 · Views")
    add("")
    add("Create these views and no others. Remove the default view Notion adds if it is not listed. "
        "\"Show\" lists the only properties visible in the view, in that order.")
    add("")
    for db_id in ordered_dbs(hub):
        views = [v for v in hub.get("views", []) if v["database"] == db_id]
        if not views:
            continue
        add(f"### {code(dbs[db_id]['name'])}")
        add("")
        for i, v in enumerate(views, 1):
            label = t.get(v["label_key"], v["name"])
            bits = [v["layout"]]
            if v.get("default"):
                bits.insert(0, "default view")
            if v.get("group_by"):
                bits.append(f"grouped by {code(v['group_by'])}")
            if v.get("calendar_by"):
                bits.append(f"by {code(v['calendar_by'])}")
            if v.get("filter"):
                bits.append("filter: " + ", and ".join(filter_text(f) for f in v["filter"]))
            if v.get("sort"):
                bits.append("sort: " + ", then ".join(f"{code(s['property'])} {s['direction']}" for s in v["sort"]))
            if v.get("properties"):
                bits.append("show: " + codes(v["properties"]))
            who = {"coach": " (the coach uses this one)", "internal": " (for the maintainer or VA)"}.get(
                v.get("audience"), "")
            add(f"{i}. {quoted(label)}{who} · " + " · ".join(bits))
        add("")

    # -- step 5: why the shape
    rules = hub.get("rules", {})
    add("## Step 5 · The rules this board serves")
    add("")
    add("Nothing to build here; these explain the shape so you do not \"improve\" it.")
    add("")
    for key in ("never_delete", "upsert", "quality_in_same_upsert", "coach_word_rule", "scripts_in_page_body",
                "data_not_instructions", "blank_not_zero"):
        if rules.get(key):
            add(f"- {sentence(rules[key])}")
    if rules.get("ai_status"):
        add(f"- The machine sets {code('Status')} only to {codes(rules['ai_status'])}.")
    if rules.get("max_hub_calls_per_run"):
        add(f"- Each automated run makes at most {rules['max_hub_calls_per_run']} board calls.")
    add("")

    # -- step 6: check and report
    add("## Step 6 · Check, then report")
    add("")
    counts = ", ".join(f"{code(dbs[d]['name'])} {len(cmschema.notion_properties(hub, d))}" for d in ordered_dbs(hub))
    view_counts = ", ".join(
        f"{code(dbs[d]['name'])} {sum(1 for v in hub.get('views', []) if v['database'] == d)}"
        for d in ordered_dbs(hub))
    add(f"1. Properties per database (page-body items not counted): {counts}.")
    add("2. Every select, multi-select and status property has exactly the options listed, in that order.")
    add(f"3. Views per database: {view_counts}. Each default view is the first tab.")
    add("4. The relations in step 3 exist, and no database has a property that is not in its table.")
    add(f"5. Report with a table `Database | properties | views | fallbacks used`, then the link to {code(root)}, "
        "then anything you could not build. Do not work around a failure; report it.")
    return cmlib.finish("\n".join(out))


# ---------------------------------------------------------------- Sheets Lite

def csv_text(rows: list[list[str]]) -> str:
    buf = io.StringIO()
    writer = csv.writer(buf, lineterminator="\n")
    for row in rows:
        writer.writerow([cmlib.nfc(str(c)) for c in row])
    return buf.getvalue()


def sheet_files(hub: dict, t: Texts) -> dict[str, str]:
    """File name → CSV text for every tab, in tab order."""
    by_tab = cmschema.db_by_tab(hub)
    sheets = hub["sheets"]
    files: dict[str, str] = {}
    for tab in sheets["tabs"]:
        if tab == "Start":
            start = sheets["start"]
            rows = [list(start["columns"]), ["", t.get(start["title_key"])]]
            rows += [[str(i), t.get(key)] for i, key in enumerate(start["step_keys"], 1)]
        elif tab == "Scoreboard":
            rows = [[c["name"] for c in sheets["scoreboard"]]]
        else:
            rows = [[p["name"] for p in cmschema.sheet_columns(hub, by_tab[tab])]]
        files[f"{tab}.csv"] = csv_text(rows)
    return files


def sheet_notes(hub: dict, t: Texts) -> str:
    ed = t.ed
    root = page_name(hub, "root", t)
    sheets = hub["sheets"]
    by_tab = cmschema.db_by_tab(hub)
    out: list[str] = []
    add = out.append
    add(f"# Sheets Lite template: {root} · {ed.file_suffix} edition")
    add("")
    add("Generated by tools/hub_build_prompt.py from schemas/hub.toml; rebuild it, never edit it by hand.")
    add("")
    add("## Every tab")
    add("")
    add(f"- Import each CSV in this folder as its own tab, in this order: {', '.join(sheets['tabs'])}.")
    add(f"- Locale: {sheets.get('locale', '')}.")
    add(f"- Header: {sheets.get('header', '')}. Protect row 1 with a warning.")
    add("- Nothing runs on this sheet automatically; rows are pasted as tab-separated text at the first empty row.")
    add("- Dropdown options are the exact values below (English in every edition).")
    add("")
    for tab in sheets["tabs"]:
        if tab in cmschema.FIXED_TABS:
            continue
        db_id = by_tab[tab]
        cols = cmschema.sheet_columns(hub, db_id)
        add(f"## {tab}")
        add("")
        add("| Column | Header | Kind | Dropdown values |")
        add("|---|---|---|---|")
        for i, p in enumerate(cols):
            kind = SHEET_KIND[p["type"]]
            if p["type"] == "relation":
                target = cmschema.databases(hub)[p["relation_to"]]
                key = hub.get("rules", {}).get("upsert_keys", {}).get(p["relation_to"], "")
                kind = f"text: the {target['name']} row's {key}"
            elif p.get("page_body"):
                kind = "text (long; wrap)"
            add(f"| {cmschema.column_letter(i)} | {p['name']} | {cell(kind)} | {cell(', '.join(p.get('options', [])))} |")
        add("")
        key_col = cmschema.column_letter(0)
        add(f"Conditional format: highlight duplicate keys in column {key_col}, range {key_col}2:{key_col}, "
            f"custom formula `=AND(${key_col}2<>\"\",COUNTIF(${key_col}:${key_col},${key_col}2)>1)`.")
        add("")
    add("## Scoreboard")
    add("")
    add(f"Row n mirrors Content row n. Put these formulas in row 2, then copy them down to row {SCOREBOARD_ROWS}. "
        "Check them once in the template before publishing it.")
    add("")
    add("| Column | Header | Row 2 formula | Note |")
    add("|---|---|---|---|")
    for i, c in enumerate(sheets["scoreboard"]):
        formula = cmschema.scoreboard_formula(hub, c["formula"], 2)
        add(f"| {cmschema.column_letter(i)} | {c['name']} | `{formula}` | {cell(c.get('note', ''))} |")
    return cmlib.finish("\n".join(out))


# ---------------------------------------------------------------- build

def load_schemas(root: Path) -> dict[str, dict]:
    """Every schema file present, validated together; CMError E161 on the first problems."""
    data = {name: cmschema.load(name, root) for name in cmschema.SCHEMAS
            if cmschema.schema_path(name, root).exists()}
    findings = cmschema.check(root, data)
    if findings:
        shown = "; ".join(f"{where}: {msg}" for _, where, msg in findings[:5])
        more = f" (+{len(findings) - 5} more)" if len(findings) > 5 else ""
        raise CMError("E161", f"{len(findings)} schema problem(s): {shown}{more}", "schemas")
    return data


def write(path: Path, text: str) -> Path:
    if not path.name.isascii():
        raise CMError("E150", "non-ASCII file name", str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.encode("utf-8"))
    return path


def build_edition(root: Path, hub: dict, edition_id: str) -> Result:
    ed = cmlib.load_edition(edition_id, root)
    t = Texts(ed)
    result = Result(edition=edition_id)
    out = root / "dist" / "maintainer"
    result.paths.append(write(out / f"notion-build-prompt-{edition_id}.md", notion_prompt(hub, t)))
    sheets_dir = out / f"sheets-{edition_id}"
    if sheets_dir.exists():
        shutil.rmtree(sheets_dir)
    for name, text in sheet_files(hub, t).items():
        result.paths.append(write(sheets_dir / name, text))
    result.paths.append(write(sheets_dir / "BUILD-NOTES.md", sheet_notes(hub, t)))
    result.missing = list(t.missing)
    return result


def build(root: Path, editions: list[str]) -> list[Result]:
    """Write the hub outputs for the given editions; [] when schemas/hub.toml does not exist yet."""
    root = Path(root).resolve()
    if not cmschema.schema_path("hub", root).exists():
        return []
    hub = load_schemas(root)["hub"]
    return [build_edition(root, hub, e) for e in editions]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Render the Notion build prompt and Sheets Lite CSVs.")
    ap.add_argument("--edition", required=True, choices=[*cmlib.EDITIONS, "all"])
    ap.add_argument("--root", type=Path, default=None, help="repo root (default: CM_ROOT or this repo)")
    args = ap.parse_args(argv)
    root = (args.root or cmlib.ROOT).resolve()
    editions = list(cmlib.EDITIONS) if args.edition == "all" else [args.edition]
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    try:
        results = build(root, editions)
    except CMError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    if not results:
        print("note: schemas/hub.toml not present; nothing to render")
        return 0
    for r in results:
        for p in r.paths:
            print(f"wrote {cmlib.rel(p, root)}")
        if r.missing:
            print(f"note: {r.edition}: {len(r.missing)} strings key(s) not in strings/{r.edition}.toml yet; "
                  "printed as the key (descriptions) or the English name (labels)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
