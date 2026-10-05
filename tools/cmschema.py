"""Load and validate schemas/*.toml; parse Slot and Run keys (standard library only).

    findings = check(root)              # [] when every schema is sound; else (code, where, message)
    kinds = key_kinds("2026-W41-N1")    # ["slot.weekly"]

The schema files and their shapes are documented in their own headers:
schemas/hub.toml, schemas/keys.toml, schemas/banks.toml, schemas/brand-card.toml.
Every finding uses lint code E161 (bad schema, docs/BUILD.md §7).
"""
from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cmlib  # noqa: E402
from cmlib import CMError  # noqa: E402

SCHEMAS = ("hub", "keys", "banks", "brand-card")

PROPERTY_TYPES = ("title", "rich_text", "select", "multi_select", "status", "number", "date",
                  "relation", "url", "checkbox")
OPTION_TYPES = ("select", "multi_select", "status")
GROUPS = ("Pipeline", "Plan", "Script", "Quality", "Repurpose", "Human", "Stats", "AI", "Run", "Item", "Proof")
STATUS_GROUPS = ("To-do", "In progress", "Complete")
LAYOUTS = ("table", "board", "list", "calendar", "gallery")
AUDIENCES = ("coach", "more", "internal")
FILTER_OPS = ("is", "is_not", "is_any_of", "is_empty", "is_not_empty", "is_checked", "is_not_checked", "within")
WITHIN = ("this_week", "next_30_days", "past_7_days")
VALUE_OPS = ("is", "is_not", "is_any_of")
CARD_TYPES = ("text", "int", "date", "enum", "list", "rows")
SIZED_CARD_TYPES = ("text", "list", "rows")
PAGE_BODY = "page body"
FIXED_TABS = ("Start", "Scoreboard")
# Words the coach never sees (wf11-ux-spec §4); Brand Card field names must avoid them.
FRAMEWORK_WORDS = ("pillar", "rung", "domino", "edge", "admirable", "likable", "credible", "trustable",
                   "spcl", "signal", "filter", "mirror", "bomb", "lock", "rubric", "score", "ship_check")
PLACEHOLDER_RE = re.compile(r"\{([A-Za-z][A-Za-z0-9 -]*)\}")
FIELD_NAME_RE = re.compile(r"^[a-z][a-z0-9_]*$")


def schema_path(name: str, root: Path | None = None) -> Path:
    return (root or cmlib.ROOT) / "schemas" / f"{name}.toml"


def load(name: str, root: Path | None = None) -> dict:
    """One schema file as a dict; CMError E161 when missing or not valid TOML."""
    return cmlib.load_toml(schema_path(name, root))


def load_all(root: Path | None = None) -> dict[str, dict]:
    return {name: load(name, root) for name in SCHEMAS}


# ---------------------------------------------------------------- hub helpers

def databases(hub: dict) -> dict[str, dict]:
    dbs = hub.get("databases", {})
    return dbs if isinstance(dbs, dict) else {}


def properties(hub: dict, db_id: str) -> list[dict]:
    props = databases(hub).get(db_id, {}).get("property", [])
    return [p for p in props if isinstance(p, dict)] if isinstance(props, list) else []


def prop(hub: dict, db_id: str, name: str) -> dict | None:
    return next((p for p in properties(hub, db_id) if p.get("name") == name), None)


def notion_properties(hub: dict, db_id: str) -> list[dict]:
    """Properties Notion creates (page-body items excluded)."""
    return [p for p in properties(hub, db_id) if not p.get("page_body")]


def sheet_columns(hub: dict, db_id: str) -> list[dict]:
    """The database's Sheets Lite columns, in column order."""
    return [p for p in properties(hub, db_id) if p.get("sheet_column") is True]


def db_by_tab(hub: dict) -> dict[str, str]:
    return {db.get("sheet_tab"): db_id for db_id, db in databases(hub).items() if db.get("sheet_tab")}


def column_letter(index: int) -> str:
    """0 -> A, 25 -> Z, 26 -> AA."""
    letters = ""
    index += 1
    while index:
        index, rem = divmod(index - 1, 26)
        letters = chr(65 + rem) + letters
    return letters


def scoreboard_formula(hub: dict, formula: str, row: int) -> str:
    """Resolve {Prop} to the Content tab column letter, {row} and {prev} to row numbers."""
    cols = {p["name"]: column_letter(i) for i, p in enumerate(sheet_columns(hub, "content"))}

    def sub(m: re.Match) -> str:
        name = m.group(1)
        if name == "row":
            return str(row)
        if name == "prev":
            return str(row - 1)
        if name not in cols:
            raise CMError("E161", f"scoreboard formula names '{name}', which is not a Content sheet column",
                          "schemas/hub.toml")
        return cols[name]

    return PLACEHOLDER_RE.sub(sub, formula)


# ---------------------------------------------------------------- keys

def key_grammars(keys: dict) -> list[tuple[str, dict]]:
    """(kind, spec) for every grammar: slot.weekly, slot.launch, slot.drop, run.<TYPE>."""
    out: list[tuple[str, dict]] = []
    slot = keys.get("slot", {})
    for name in ("weekly", "launch", "drop"):
        if isinstance(slot.get(name), dict):
            out.append((f"slot.{name}", slot[name]))
    for entry in keys.get("run", {}).get("key", []):
        if isinstance(entry, dict) and entry.get("type"):
            out.append((f"run.{entry['type']}", entry))
    return out


def calendar_ok(groups: dict) -> bool:
    """True when the ISO week or the calendar date named by the match groups exists."""
    try:
        if groups.get("week"):
            dt.date.fromisocalendar(int(groups["year"]), int(groups["week"]), 1)
        if groups.get("month") and groups.get("day"):
            dt.date(int(groups["year"]), int(groups["month"]), int(groups["day"]))
    except ValueError:
        return False
    return True


def match_key(text: str, spec: dict) -> dict | None:
    """The match groups when text fits the grammar and names a real week or day."""
    m = re.fullmatch(spec["pattern"], text)
    if not m or not calendar_ok(m.groupdict()):
        return None
    return {k: v for k, v in m.groupdict().items() if v is not None}


def key_kinds(text: str, keys: dict | None = None, root: Path | None = None) -> list[str]:
    """Every grammar that accepts text ("DROP-2026-10-07" is both a slot and a run key)."""
    keys = keys if keys is not None else load("keys", root)
    return [kind for kind, spec in key_grammars(keys) if match_key(text, spec) is not None]


def is_slot_key(text: str, keys: dict | None = None, root: Path | None = None) -> bool:
    return any(k.startswith("slot.") for k in key_kinds(text, keys, root))


def is_run_key(text: str, keys: dict | None = None, root: Path | None = None) -> bool:
    return any(k.startswith("run.") for k in key_kinds(text, keys, root))


# ---------------------------------------------------------------- validation

class _Findings(list):
    def add(self, where: str, message: str) -> None:
        self.append(("E161", where, message))


def _is_str_list(value) -> bool:
    return isinstance(value, list) and all(isinstance(v, str) for v in value)


def _options(p: dict) -> list[str]:
    opts = p.get("options", [])
    return opts if _is_str_list(opts) else []


def check(root: Path | None = None, data: dict[str, dict] | None = None) -> list[tuple[str, str, str]]:
    """Validate the four schema files together; returns (code, where, message) findings."""
    root = root or cmlib.ROOT
    out = _Findings()
    if data is None:
        data = {}
        for name in SCHEMAS:
            try:
                data[name] = load(name, root)
            except CMError as exc:
                out.add(f"schemas/{name}.toml", exc.message)
    for name, d in data.items():
        if d.get("schema_version") != 1:
            out.add(f"schemas/{name}.toml", "schema_version must be 1")
    if "hub" in data:
        _check_hub(data["hub"], out)
    if "keys" in data:
        _check_keys(data["keys"], data.get("hub"), out)
    if "banks" in data:
        _check_banks(data["banks"], data.get("hub"), out)
    if "brand-card" in data:
        _check_card(data["brand-card"], data.get("banks"), root, out)
    return list(out)


def _check_key(value, where: str, out: _Findings, seen: set[str] | None = None) -> None:
    if not isinstance(value, str) or not cmlib.KEY_RE.match(value):
        out.add(where, f"'{value}' is not a valid strings key ([a-z0-9_.-])")
    elif seen is not None:
        if value in seen:
            out.add(where, f"strings key '{value}' is used twice")
        seen.add(value)


def _check_hub(hub: dict, out: _Findings) -> None:
    where = "schemas/hub.toml"
    dbs = databases(hub)
    if not dbs:
        out.add(where, "no [databases.<id>] tables")
        return
    desc_keys: set[str] = set()
    for db_id, db in dbs.items():
        w = f"{where} [databases.{db_id}]"
        for k in ("name", "sheet_tab", "parent", "description_key"):
            if not isinstance(db.get(k), str) or not db.get(k):
                out.add(w, f"missing '{k}'")
        _check_key(db.get("description_key"), w, out, desc_keys)
        props = properties(hub, db_id)
        if not props:
            out.add(w, "no [[property]] tables")
            continue
        names = [p.get("name") for p in props]
        for dup in sorted({n for n in names if isinstance(n, str) and names.count(n) > 1}):
            out.add(w, f"property '{dup}' is listed twice")
        if sum(1 for p in props if p.get("type") == "title") != 1:
            out.add(w, "needs exactly one property of type 'title'")
        for p in props:
            _check_property(hub, db_id, p, f"{w} property '{p.get('name')}'", out, desc_keys)
    _check_rules(hub, out)
    _check_views(hub, out)
    _check_pages(hub, out)
    _check_sheets(hub, out)


def _check_property(hub: dict, db_id: str, p: dict, w: str, out: _Findings, desc_keys: set[str]) -> None:
    name, ptype = p.get("name"), p.get("type")
    if not isinstance(name, str) or not name.strip() or name != name.strip():
        out.add(w, "needs a name")
    elif not name.isascii() or "," in name:
        out.add(w, "names are ASCII with no commas")
    if ptype not in PROPERTY_TYPES:
        out.add(w, f"type must be one of {', '.join(PROPERTY_TYPES)}")
    if p.get("group") not in GROUPS:
        out.add(w, f"group must be one of {', '.join(GROUPS)}")
    if not isinstance(p.get("sheet_column"), bool):
        out.add(w, "sheet_column must be true or false")
    _check_key(p.get("description_key"), w, out, desc_keys)
    if p.get("page_body") and ptype != "rich_text":
        out.add(w, "page_body items are rich_text")
    if p.get("page_body") and ptype == "title":
        out.add(w, "the title cannot live in the page body")
    opts = p.get("options")
    if ptype in OPTION_TYPES:
        if not _is_str_list(opts) or not opts:
            out.add(w, "needs a non-empty options list")
        else:
            if len(set(opts)) != len(opts):
                out.add(w, "options repeat")
            for o in opts:
                if "," in o or not o.strip():
                    out.add(w, f"option '{o}' is empty or has a comma (Notion rejects it)")
    elif opts is not None:
        out.add(w, f"a {ptype} property takes no options")
    for key in ("ai_may_set", "on_coach_word"):
        if key not in p:
            continue
        if ptype != "status":
            out.add(w, f"{key} belongs on status properties only")
        elif not _is_str_list(p[key]) or not set(p[key]) <= set(_options(p)):
            out.add(w, f"{key} must be a subset of options")
    if ptype == "status":
        if set(p.get("ai_may_set", [])) & set(p.get("on_coach_word", [])):
            out.add(w, "a value cannot be both ai_may_set and on_coach_word")
        groups = p.get("status_groups")
        if not isinstance(groups, dict) or set(groups) - set(STATUS_GROUPS):
            out.add(w, f"status_groups must use {', '.join(STATUS_GROUPS)}")
        else:
            placed = [v for vals in groups.values() for v in (vals if _is_str_list(vals) else [])]
            if sorted(placed) != sorted(_options(p)):
                out.add(w, "status_groups must place every option exactly once")
    if ptype == "relation":
        target = p.get("relation_to")
        if target not in databases(hub):
            out.add(w, f"relation_to '{target}' is not a database id")
        elif p.get("two_way"):
            back = prop(hub, target, p.get("synced_property", ""))
            if not back or back.get("type") != "relation" or back.get("relation_to") != db_id \
                    or back.get("synced_property") != p.get("name"):
                out.add(w, f"two_way needs a synced_property in '{target}' that relates back")
        elif not isinstance(p.get("two_way"), bool):
            out.add(w, "relation needs two_way = true or false")
    rng = p.get("range")
    if rng is not None and (ptype != "number" or not (isinstance(rng, list) and len(rng) == 2
                                                      and all(isinstance(x, int) for x in rng)
                                                      and rng[0] <= rng[1])):
        out.add(w, "range is [min, max] on number properties only")


def _check_rules(hub: dict, out: _Findings) -> None:
    w = "schemas/hub.toml [rules]"
    rules = hub.get("rules")
    if not isinstance(rules, dict):
        out.add(w, "missing [rules]")
        return
    for k in ("never_delete", "upsert", "upsert_keys", "quality_in_same_upsert", "max_hub_calls_per_run",
              "ai_status", "coach_word_status"):
        if k not in rules:
            out.add(w, f"missing '{k}'")
    if rules.get("max_hub_calls_per_run") != 30:
        out.add(w, "max_hub_calls_per_run must be 30 (QA spec §2.7)")
    status = prop(hub, "content", "Status")
    if not status:
        out.add(w, "Content needs a Status property")
    else:
        if status.get("ai_may_set") != rules.get("ai_status"):
            out.add(w, "ai_status must equal Content Status ai_may_set")
        if status.get("on_coach_word") != rules.get("coach_word_status"):
            out.add(w, "coach_word_status must equal Content Status on_coach_word")
        if set(status.get("ai_may_set", [])) | set(status.get("on_coach_word", [])) != set(_options(status)):
            out.add(w, "every Content Status value is either ai_may_set or on_coach_word")
    archive = rules.get("archive_property")
    if archive and not prop(hub, "content", archive):
        out.add(w, f"archive_property '{archive}' is not a Content property")
    keys = rules.get("upsert_keys", {})
    for db_id in databases(hub):
        key = keys.get(db_id) if isinstance(keys, dict) else None
        if not key or not prop(hub, db_id, key):
            out.add(w, f"upsert_keys needs an existing property for '{db_id}'")
            continue
        cols = sheet_columns(hub, db_id)
        if hub.get("paste", {}).get("key_first") and (not cols or cols[0]["name"] != key):
            out.add(w, f"the first {db_id} sheet column must be its upsert key '{key}'")


def _check_views(hub: dict, out: _Findings) -> None:
    views = hub.get("views", [])
    if not isinstance(views, list) or not views:
        out.add("schemas/hub.toml", "no [[views]]")
        return
    defaults: dict[str, int] = {}
    seen: set[tuple[str, str]] = set()
    label_keys: set[str] = set()
    for v in views:
        w = f"schemas/hub.toml view '{v.get('name')}'"
        db_id = v.get("database")
        if db_id not in databases(hub):
            out.add(w, f"database '{db_id}' is not a database id")
            continue
        if (db_id, v.get("name")) in seen:
            out.add(w, "view name repeats in its database")
        seen.add((db_id, v.get("name")))
        _check_key(v.get("label_key"), w, out, label_keys)
        if v.get("layout") not in LAYOUTS:
            out.add(w, f"layout must be one of {', '.join(LAYOUTS)}")
        if v.get("audience") not in AUDIENCES:
            out.add(w, f"audience must be one of {', '.join(AUDIENCES)}")
        if v.get("default"):
            defaults[db_id] = defaults.get(db_id, 0) + 1
        if v.get("layout") == "calendar" and not prop(hub, db_id, v.get("calendar_by", "")):
            out.add(w, "a calendar needs calendar_by naming a date property")
        if v.get("layout") == "board" and not v.get("group_by"):
            out.add(w, "a board needs group_by")
        for name in [v.get("group_by"), v.get("calendar_by")]:
            if name and not prop(hub, db_id, name):
                out.add(w, f"'{name}' is not a property of {db_id}")
        for name in v.get("properties", []):
            p = prop(hub, db_id, name)
            if not p:
                out.add(w, f"shows unknown property '{name}'")
            elif p.get("page_body"):
                out.add(w, f"'{name}' lives in the page body and cannot be shown")
            elif v.get("audience") == "coach" and p.get("internal"):
                out.add(w, f"coach view shows internal property '{name}'")
        for s in v.get("sort", []):
            if not prop(hub, db_id, s.get("property", "")) or s.get("direction") not in ("ascending", "descending"):
                out.add(w, f"bad sort {s}")
        for f in v.get("filter", []):
            _check_filter(hub, db_id, f, w, out)
    for db_id, n in defaults.items():
        if n > 1:
            out.add("schemas/hub.toml", f"database '{db_id}' has {n} default views")


def _check_filter(hub: dict, db_id: str, f: dict, w: str, out: _Findings) -> None:
    p = prop(hub, db_id, f.get("property", ""))
    op = f.get("op")
    if not p:
        out.add(w, f"filter on unknown property '{f.get('property')}'")
        return
    if op not in FILTER_OPS:
        out.add(w, f"filter op must be one of {', '.join(FILTER_OPS)}")
        return
    value = f.get("value")
    if op in VALUE_OPS:
        values = value if op == "is_any_of" else [value]
        if not _is_str_list(values) or not values:
            out.add(w, f"filter '{op}' on '{p['name']}' needs a value")
        elif p.get("type") in OPTION_TYPES and not set(values) <= set(_options(p)):
            out.add(w, f"filter value {value} is not an option of '{p['name']}'")
    elif op == "within":
        if p.get("type") != "date" or value not in WITHIN:
            out.add(w, f"'within' needs a date property and one of {', '.join(WITHIN)}")
    elif op in ("is_checked", "is_not_checked") and p.get("type") != "checkbox":
        out.add(w, f"'{op}' needs a checkbox property")


def _check_pages(hub: dict, out: _Findings) -> None:
    pages = hub.get("pages", {})
    w = "schemas/hub.toml [pages]"
    if not isinstance(pages, dict) or "root" not in pages:
        out.add(w, "needs [pages.root]")
        return
    for pid, page in pages.items():
        if not isinstance(page.get("name"), str) or not page.get("name"):
            out.add(f"{w}.{pid}", "missing name")
        parent = page.get("parent", "")
        if pid != "root" and parent not in pages:
            out.add(f"{w}.{pid}", f"parent '{parent}' is not a page id")
        for child in page.get("children", []):
            if child not in pages or pages[child].get("parent") != pid:
                out.add(f"{w}.{pid}", f"child '{child}' must be a page whose parent is '{pid}'")
        for key in page.get("body_keys", []):
            _check_key(key, f"{w}.{pid}", out)
    for db_id, db in databases(hub).items():
        parent = db.get("parent")
        if parent not in pages or db_id not in pages[parent].get("databases", []):
            out.add(f"schemas/hub.toml [databases.{db_id}]",
                    f"parent '{parent}' must be a page that lists it under databases")


def _check_sheets(hub: dict, out: _Findings) -> None:
    w = "schemas/hub.toml [sheets]"
    sheets = hub.get("sheets", {})
    tabs = sheets.get("tabs", [])
    if not _is_str_list(tabs) or len(set(tabs)) != len(tabs):
        out.add(w, "tabs must be a list of unique names")
        return
    wanted = set(FIXED_TABS) | set(db_by_tab(hub))
    if set(tabs) != wanted:
        out.add(w, f"tabs must be exactly {', '.join(sorted(wanted))}")
    for tab in tabs:
        if not re.fullmatch(r"[A-Za-z0-9-]+", tab):
            out.add(w, f"tab '{tab}' must be an ASCII file-safe name")
    start = sheets.get("start", {})
    _check_key(start.get("title_key"), f"{w}.start", out)
    for key in start.get("step_keys", []):
        _check_key(key, f"{w}.start", out)
    board = sheets.get("scoreboard", [])
    if not isinstance(board, list) or not board:
        out.add(w, "needs [[sheets.scoreboard]] columns")
    for col in board if isinstance(board, list) else []:
        try:
            scoreboard_formula(hub, col.get("formula", ""), 2)
        except CMError as exc:
            out.add(f"{w}.scoreboard '{col.get('name')}'", exc.message)


def _check_examples(kind: str, spec: dict, out: _Findings, where: str) -> None:
    try:
        re.compile(spec.get("pattern", ""))
    except re.error as exc:
        out.add(where, f"{kind}: bad regex: {exc}")
        return
    if not spec.get("examples"):
        out.add(where, f"{kind}: needs examples")
    for ex in spec.get("examples", []):
        if match_key(ex, spec) is None:
            out.add(where, f"{kind}: example '{ex}' does not match")
    for bad in spec.get("near_misses", []):
        if re.fullmatch(spec["pattern"], bad):
            out.add(where, f"{kind}: near-miss '{bad}' matches")
    for bad in spec.get("invalid", []):
        if not re.fullmatch(spec["pattern"], bad) or match_key(bad, spec) is not None:
            out.add(where, f"{kind}: invalid '{bad}' must fit the regex but name no real day or week")


def _check_keys(keys: dict, hub: dict | None, out: _Findings) -> None:
    where = "schemas/keys.toml"
    grammars = dict(key_grammars(keys))
    for kind in ("slot.weekly", "slot.launch", "slot.drop"):
        if kind not in grammars:
            out.add(where, f"missing [{kind}]")
    for kind, spec in grammars.items():
        _check_examples(kind, spec, out, where)
    formats = set(_options(prop(hub, "content", "Format") or {})) if hub else None
    weekly = grammars.get("slot.weekly", {})
    for s in weekly.get("suffix", []):
        if match_key(f"2026-W41-{s.get('code')}", weekly) is None:
            out.add(where, f"weekly suffix '{s.get('code')}' is not accepted by the pattern")
        if formats is not None and s.get("format") not in formats:
            out.add(where, f"weekly suffix '{s.get('code')}' format '{s.get('format')}' is not a Content Format")
    drop = grammars.get("slot.drop", {})
    if formats is not None and drop.get("format") not in formats:
        out.add(where, f"drop slot format '{drop.get('format')}' is not a Content Format")
    launch = grammars.get("slot.launch", {})
    for f in launch.get("fmt", []):
        if match_key(f"LCH-TEST-D01-{f.get('code')}", launch) is None:
            out.add(where, f"launch fmt '{f.get('code')}' is not accepted by the pattern")
        if formats is not None and f.get("format") not in formats:
            out.add(where, f"launch fmt '{f.get('code')}' format '{f.get('format')}' is not a Content Format")
    if hub:
        types = [k.split(".", 1)[1] for k in grammars if k.startswith("run.")]
        hub_types = _options(prop(hub, "runs", "Type") or {})
        if sorted(types) != sorted(hub_types):
            out.add(where, f"run key types {types} must equal the Runs Type options {hub_types}")
        states = [s.get("name") for s in keys.get("run", {}).get("state", [])]
        hub_states = _options(prop(hub, "runs", "Run State") or {})
        if states != hub_states:
            out.add(where, f"run states {states} must equal the Runs Run State options {hub_states}")


def _check_banks(banks: dict, hub: dict | None, out: _Findings) -> None:
    where = "schemas/banks.toml"
    ids = banks.get("ids", {})
    try:
        id_re = re.compile(ids.get("pattern", ""))
    except re.error as exc:
        out.add(where, f"[ids] bad regex: {exc}")
        return
    for ex in ids.get("examples", []):
        if not id_re.fullmatch(ex):
            out.add(where, f"[ids] example '{ex}' does not match")
    for bad in ids.get("near_misses", []):
        if id_re.fullmatch(bad):
            out.add(where, f"[ids] near-miss '{bad}' matches")
    bank_props = {p["name"]: p for p in properties(hub, "bank")} if hub else None
    hub_targets = None if bank_props is None else set(bank_props) | {PAGE_BODY}
    for f in banks.get("shared", []):
        if hub_targets is not None and f.get("hub") not in hub_targets:
            out.add(where, f"shared field '{f.get('name')}' maps to unknown Bank property '{f.get('hub')}'")
    types = banks.get("types", {})
    if not types:
        out.add(where, "no [types.<prefix>] tables")
    kinds_all: list[str] = []
    states_all: list[str] = []
    options: list[str] = []
    for key, t in types.items():
        w = f"{where} [types.{key}]"
        prefix = t.get("prefix")
        if prefix != key or not re.fullmatch(r"[A-Z]", str(prefix)) or not id_re.fullmatch(f"{prefix}-1"):
            out.add(w, "prefix must equal the table key, be one capital letter and fit [ids] pattern")
        options.append(t.get("hub_option"))
        _check_key(t.get("label_key"), w, out)
        fields = t.get("fields", [])
        if not fields or not any(f.get("required") is True for f in fields):
            out.add(w, "needs fields with at least one required field")
        names = [f.get("name") for f in fields]
        if len(set(names)) != len(names):
            out.add(w, "field names repeat")
        for f in fields:
            if not isinstance(f.get("required"), bool):
                out.add(w, f"field '{f.get('name')}' needs required = true/false")
            if hub_targets is not None and f.get("hub") not in hub_targets:
                out.add(w, f"field '{f.get('name')}' maps to unknown Bank property '{f.get('hub')}'")
            _check_bank_field_limits(f, w, out)
        if not any(f.get("hub") == "Text" and f.get("required") for f in fields):
            out.add(w, "a required field must map to Text (the row title)")
        kinds = t.get("kinds", [])
        if kinds and not any(f.get("hub") == "Kind" for f in fields):
            out.add(w, "kinds listed but no field maps to Kind")
        kinds_all += [k for k in kinds if k not in kinds_all]
        states = t.get("states", [])
        if not _is_str_list(states) or not states:
            out.add(w, "needs states")
        states_all += [s for s in states if s not in states_all]
    if bank_props is not None:
        for name, values in (("Type", options), ("Kind", kinds_all), ("State", states_all)):
            hub_opts = _options(bank_props.get(name, {}))
            if sorted(map(str, values)) != sorted(hub_opts):
                out.add(where, f"Bank {name} options in hub.toml must equal the types' values {values}")
    caps = banks.get("card_caps", {})
    for prefix in ("V", "S", "P"):
        if not isinstance(caps.get(prefix), int) or caps[prefix] < 1:
            out.add(f"{where} [card_caps]", f"{prefix} needs a positive cap")


def _positive_int(value) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def _check_bank_field_limits(f: dict, w: str, out: _Findings) -> None:
    """Optional field attributes: options (closed list), max_chars (int), max_words ({en, vn})."""
    name = f.get("name")
    if "options" in f:
        opts = f["options"]
        if not _is_str_list(opts) or not opts or len(set(opts)) != len(opts):
            out.add(w, f"field '{name}' options must be a non-empty list of unique strings")
    if "max_chars" in f and not _positive_int(f["max_chars"]):
        out.add(w, f"field '{name}' max_chars must be a positive integer")
    if "max_words" in f:
        mw = f["max_words"]
        if not isinstance(mw, dict) or not all(_positive_int(mw.get(e)) for e in cmlib.EDITIONS):
            out.add(w, f"field '{name}' max_words needs positive en and vn integers")


def _card_fields(card: dict) -> list[tuple[str, dict]]:
    out = []
    for part in ("visible", "machine"):
        for f in card.get(part, {}).get("field", []):
            out.append((part, f))
    return out


def _check_card(card: dict, banks: dict | None, root: Path, out: _Findings) -> None:
    where = "schemas/brand-card.toml"
    budgets = card.get("budgets", {})
    sources = card.get("sources", {})
    for k in ("whole_chars", "visible_chars"):
        if not all(isinstance(budgets.get(k, {}).get(e), int) for e in cmlib.EDITIONS):
            out.add(f"{where} [budgets]", f"{k} needs en and vn integers")
    for e in cmlib.EDITIONS:
        whole, visible = budgets.get("whole_chars", {}).get(e), budgets.get("visible_chars", {}).get(e)
        if isinstance(whole, int) and isinstance(visible, int) and whole < visible:
            out.add(f"{where} [budgets]", f"whole_chars.{e} is smaller than visible_chars.{e}")
    targets_path = root / "platform" / "targets.toml"
    if targets_path.exists():
        targets = cmlib.load_toml(targets_path).get("budgets", {})
        for k, ref in (("whole_chars", budgets.get("whole")), ("visible_chars", budgets.get("visible"))):
            spec = targets.get(ref)
            if spec is None:
                continue
            for e in cmlib.EDITIONS:
                if spec.get(e) != budgets.get(k, {}).get(e):
                    out.add(f"{where} [budgets]", f"{k}.{e} disagrees with targets.toml [budgets.{ref}]")
    fields = _card_fields(card)
    if not any(p == "visible" for p, _ in fields) or not any(p == "machine" for p, _ in fields):
        out.add(where, "needs [[visible.field]] and [[machine.field]] tables")
    names: set[str] = set()
    labels: set[str] = set()
    caps = (banks or {}).get("card_caps", {})
    bank_types = (banks or {}).get("types", {})
    for part, f in fields:
        name = f.get("name", "")
        w = f"{where} {part} field '{name}'"
        if not FIELD_NAME_RE.match(str(name)):
            out.add(w, "names are plain lower_snake_case")
        if name in names:
            out.add(w, "name repeats")
        names.add(name)
        if any(word in str(name) for word in FRAMEWORK_WORDS):
            out.add(w, "field names use plain words, never framework words")
        ftype = f.get("type")
        if ftype not in CARD_TYPES:
            out.add(w, f"type must be one of {', '.join(CARD_TYPES)}")
        if f.get("source") not in sources:
            out.add(w, f"source '{f.get('source')}' is not in [sources]")
        req = f.get("required")
        if not (isinstance(req, bool) or (_is_str_list(req) and set(req) <= set(cmlib.EDITIONS))):
            out.add(w, "required is true, false or a list of editions")
        _check_key(f.get("label_key"), w, out, labels)
        if ftype in SIZED_CARD_TYPES:
            mc = f.get("max_chars", {})
            if not all(isinstance(mc.get(e), int) and mc[e] > 0 for e in cmlib.EDITIONS):
                out.add(w, "max_chars needs positive en and vn integers")
        if ftype in ("list", "rows"):
            mi = f.get("max_items")
            if not isinstance(mi, int) or mi < 1 or f.get("min_items", 0) > mi:
                out.add(w, "max_items must be a positive integer ≥ min_items")
        if ftype == "enum" and not (_is_str_list(f.get("options")) and f.get("options")):
            out.add(w, "enum needs options")
        if ftype == "rows":
            bt = f.get("bank_type")
            if banks is not None and bt not in bank_types:
                out.add(w, f"bank_type '{bt}' is not a Bank type")
            elif banks is not None and f.get("max_items") != caps.get(bt):
                out.add(w, f"max_items must equal banks.toml card_caps.{bt} ({caps.get(bt)})")
    for name in budgets.get("trim_order", []):
        if name not in names:
            out.add(f"{where} [budgets]", f"trim_order names unknown field '{name}'")
    for e in cmlib.EDITIONS:
        total = visible_max(card, e)
        limit = budgets.get("visible_chars", {}).get(e)
        if isinstance(limit, int) and total > limit:
            out.add(f"{where} [visible]", f"{e}: fields can reach {total} characters, over the {limit} budget")


def _field_max(f: dict, edition: str) -> int:
    per = f.get("max_chars", {}).get(edition, 0) if isinstance(f.get("max_chars"), dict) else 0
    return per * (f.get("max_items", 1) if f.get("type") in ("list", "rows") else 1)


def visible_max(card: dict, edition: str) -> int:
    """Longest the visible part can be by construction (fields at max + label allowance)."""
    allowance = card.get("budgets", {}).get("label_allowance", 0)
    return sum(_field_max(f, edition) + allowance for p, f in _card_fields(card) if p == "visible")
