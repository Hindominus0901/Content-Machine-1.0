#!/usr/bin/env python3
"""Render one source file for an edition and target (docs/BUILD.md §4).

    python3 tools/render.py --edition vn --target kit core/vn/start-block.md
    python3 tools/render.py --edition en --reference setup.md

The template language itself lives in cmlib (render, render_text). This module
adds whole-file rendering and the skill-reference wrapper:

    <contract line>
    WHEN TO USE: <router trigger>
    RULES: <router rules>
    [CONTENTS: ...]            only when the reference runs over 100 lines
    <sections>
    CHECK BEFORE ANSWERING: <format checks, at most 5>
    <contract line>
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cmlib  # noqa: E402
from cmlib import CMError, Edition, Section  # noqa: E402

TOC_MIN_LINES = 100          # a reference longer than this gets a table of contents
MAX_FOOTER_CHECKS = 5
CONTRACT_KEY = "contract.output"
HEADING_RE = re.compile(r"^(#{1,3})\s+(.+?)\s*#*\s*$")
LEADING_BLANKS_RE = re.compile(r"\A(?:[ \t]*\n)+")


# ---------------------------------------------------------------- whole files

def render_file(path: Path, edition: Edition, target: str, extra: tuple[str, ...] = (),
                root: Path | None = None) -> str:
    """Render a prose file or template as it ships.

    A file with @section markers loses its preamble (maintainer notes before the
    first marker); render() strips the markers themselves. Leading blank lines
    go too, so SKILL.md front matter starts at the first byte.
    """
    path = Path(path)
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise CMError("E161", "file not found", cmlib.rel(path, root))
    preamble, sections = cmlib.parse_sections(text)
    if sections:
        text = text[len(preamble):]
    out = cmlib.render(text, edition, target, extra, path=cmlib.rel(path, root))
    return LEADING_BLANKS_RE.sub("", out) or "\n"


def render_string(key: str, edition: Edition, target: str) -> str:
    """One strings key rendered for a target, as a single stripped line or block."""
    return cmlib.render("{{t:%s}}" % key, edition, target, path=f"strings/{edition.id}.toml").strip()


# ---------------------------------------------------------------- skill references

def _localized(row: dict, key: str, edition: Edition):
    """row['<key>_<edition>'] when present (e.g. checks_vn), else row[key]."""
    for k in (f"{key}_{edition.id}", f"{key}_{edition.lang}"):
        if edition.id != "en" and k in row:
            return row[k]
    return row.get(key)


def _lines(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [ln.strip() for ln in value.splitlines() if ln.strip()]
    return [str(v).strip() for v in value if str(v).strip()]


def _routes(router) -> list[dict]:
    if isinstance(router, dict):
        return list(router.get("route", []))
    return list(router or [])


def _formats(format_checks) -> dict:
    if isinstance(format_checks, dict) and "format" in format_checks:
        return format_checks["format"]
    return format_checks or {}


def find_route(router, ref_entry: dict, where: str = "") -> dict:
    """The router row that gives a reference its WHEN TO USE / RULES header."""
    routes = _routes(router)
    if "route" in ref_entry:
        hits = [r for r in routes if r.get("id") == ref_entry["route"]]
        wanted = f"route '{ref_entry['route']}'"
    else:
        module = ref_entry.get("module")
        if not module:
            raise CMError("E161", "skill reference has no 'module' (or 'route')", where or None)
        hits = [r for r in routes if r.get("module") == module]
        wanted = f"module '{module}'"
    if not hits:
        raise CMError("E130", f"no router row for {wanted}", where or None)
    return hits[0]


def footer_checks(format_checks, formats: list[str], edition: Edition, where: str = "") -> list[str]:
    """The yes/no lines for a reference's formats, de-duplicated, at most 5."""
    table = _formats(format_checks)
    out: list[str] = []
    for fid in formats:
        if fid not in table:
            raise CMError("E161", f"unknown format '{fid}' (core/format-checks.toml)", where or None)
        for line in _lines(_localized(table[fid], "checks", edition)):
            if line not in out:
                out.append(line)
    if len(out) > MAX_FOOTER_CHECKS:
        raise CMError("E170", f"CHECK BEFORE ANSWERING would have {len(out)} lines (max {MAX_FOOTER_CHECKS})",
                      where or None)
    return out


def make_toc(body: str) -> list[str]:
    """Markdown headings (levels 1-3) outside code fences, as an indented list."""
    heads: list[tuple[int, str]] = []
    in_fence = False
    for line in body.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        m = None if in_fence else HEADING_RE.match(line)
        if m:
            heads.append((len(m.group(1)), m.group(2)))
    if not heads:
        return []
    top = min(level for level, _ in heads)
    return ["CONTENTS:"] + [f"{'  ' * (level - top)}- {title}" for level, title in heads]


def render_reference(edition: Edition, ref_entry: dict, sections: dict[str, Section], router,
                     format_checks, path: str = "") -> str:
    """Render one [[skill.reference]] entry with its header, footer and auto TOC."""
    where = path or f"core/method.toml [skill] {ref_entry.get('file', '?')}"
    selectors = ref_entry.get("sections") or []
    if not selectors:
        raise CMError("E161", "skill reference has no sections", where)
    picked = cmlib.select_sections(selectors, sections, where)
    ctx = cmlib.make_ctx(edition, "skill", path=where)

    def inline(text: str) -> str:
        return cmlib.nfc(cmlib.render_text(text, ctx)).strip()

    contract = render_string(CONTRACT_KEY, edition, "skill")
    route = find_route(router, ref_entry, where)
    trigger = inline(str(_localized(route, "trigger", edition) or ""))
    rules = [inline(r) for r in _lines(_localized(route, "rules", edition))]
    checks = [inline(c) for c in footer_checks(format_checks, list(ref_entry.get("formats", [])), edition, where)]

    header = [contract, "", f"WHEN TO USE: {trigger}".rstrip()]
    if rules:
        header += ["RULES:"] + [f"- {r}" for r in rules]
    body = "\n".join(cmlib.render(s.body, edition, "skill", path=f"{s.file}#{s.id}") for s in picked).strip()
    footer: list[str] = []
    if checks:
        footer += ["CHECK BEFORE ANSWERING:"] + [f"- {c}" for c in checks] + [""]
    footer.append(contract)

    def assemble(toc: list[str]) -> str:
        blocks = ["\n".join(header)]
        if toc:
            blocks.append("\n".join(toc))
        blocks += [body, "\n".join(footer)]
        return cmlib.finish("\n\n".join(blocks))

    text = assemble([])
    if text.count("\n") > TOC_MIN_LINES:
        text = assemble(make_toc(body))
    return text


# ---------------------------------------------------------------- CLI

def _resolve(path_arg: str, root: Path) -> Path:
    """An absolute path as given; a relative one under the repo root first, then the current folder."""
    p = Path(path_arg)
    if p.is_absolute():
        return p.resolve()
    under_root = root / p
    if under_root.exists() or not p.exists():
        return under_root.resolve()
    return p.resolve()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Render one file for an edition and target.")
    ap.add_argument("--edition", required=True, choices=list(cmlib.EDITIONS))
    ap.add_argument("--target", choices=list(cmlib.TARGET_FLAGS), help="target flag (required for a file)")
    ap.add_argument("--extra", action="append", default=[], choices=list(cmlib.EXTRA_FLAGS),
                    help="extra build flag; repeatable")
    ap.add_argument("--reference", help="render a [[skill.reference]] from core/method.toml by its file name")
    ap.add_argument("--root", type=Path, default=None, help="repo root (default: CM_ROOT or this repo)")
    ap.add_argument("file", nargs="?", help="source file (relative to the repo root or the current folder)")
    args = ap.parse_args(argv)
    root = (args.root or cmlib.ROOT).resolve()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    try:
        edition = cmlib.load_edition(args.edition, root)
        if args.reference:
            method = cmlib.load_toml(root / "core" / "method.toml")
            refs = [r for r in method.get("skill", {}).get("reference", []) if r.get("file") == args.reference]
            if not refs:
                raise CMError("E161", f"no [[skill.reference]] with file = '{args.reference}'", "core/method.toml")
            sections, _ = cmlib.load_sections(edition.cfg.get("method_prose", edition.lang), root)
            core = root / "core"
            router = cmlib.load_toml(core / "router.toml") if (core / "router.toml").exists() else {}
            checks = cmlib.load_toml(core / "format-checks.toml") if (core / "format-checks.toml").exists() else {}
            out = render_reference(edition, refs[0], sections, router, checks)
        else:
            if not args.file or not args.target:
                ap.error("give --target and a file, or --reference")
            out = render_file(_resolve(args.file, root), edition, args.target, tuple(args.extra), root)
    except CMError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
