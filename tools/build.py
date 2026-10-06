#!/usr/bin/env python3
"""Assemble dist/<edition>/ and dist/maintainer/ (docs/BUILD.md §1, §6).

    python3 tools/build.py --edition en|vn|all [--root PATH]

Per edition:
    1-INSTRUCTIONS.txt                 kit    core/<lang>/start-block.md
    PHONE-STARTER.txt                  phone  core/<lang>/phone-starter.md, else start-block.md
    CONTENT-MACHINE-<SUFFIX>.md        method core/method.toml [method] anchors
    CONTENT-MACHINE-<SUFFIX>-1-FILE.md onefile the kit + the method file, as one file for ChatGPT
    Level-ups/GROW-<SUFFIX>.md         grow   core/method.toml [grow] anchors
    Level-ups/autopilot/<skill>.zip    skill  core/SKILL.md.tmpl + [skill] references + tools/shiplint.py
    START-HERE.html                    help   strings starthere.title / starthere.body
    Help/<name>.html                   help   guides/<name>.tmpl
    dist/site/<edition>/index.html     site   guides/setup-page.tmpl
    dist/content-machine-plugin.zip    plugin both editions' kit + method file, one plugin for Claude and ChatGPT
    dist/maintainer/tasks/<edition>/   task   automation/*.tmpl (samples for lint budgets)

A source that a later phase writes is skipped with a note in
dist/maintainer/manifest.json, never an error; `lint --release` turns every
skip into an error. Any CMError stops the build: "CODE path: message", exit 1.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import html
import io
import json
import shutil
import sys
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cmlib  # noqa: E402
from cmlib import CMError  # noqa: E402
from package import FILE_MODE, ZIP_DATE, check_ascii, compute_build_sha256, make_zip, read_version  # noqa: E402
from render import CONTRACT_KEY, render_file, render_reference, render_string  # noqa: E402

# Budgets in platform/targets.toml that apply to each top-level artifact.
FILE_BUDGETS = {
    "kit": ["instructions_block"],
    "phone": ["phone_starter"],
    "method": ["method_file"],
    "grow": ["grow_file"],
    "skill": ["skill_zip"],
}
SKILL_MD_BUDGETS = ["skill_md_lines", "skill_md_bytes"]
REFERENCE_BUDGETS = ["reference_lines", "reference_bytes"]
SITE_TEMPLATE = "setup-page.tmpl"

# Portable kits (docs/BUILD.md §6): the one plugin (Claude and ChatGPT, both editions) and the per-edition one-file
# kit. Most of their text lives here and not in strings/<ed>.toml: strings are coach-visible and lint E140 bars "§CM"
# from them, but this text addresses the model (the pointer and the file header name the method file's §CM- parts).
# Tags are filled per edition: {{name}} and {{file_suffix}} as in any string; {{cmd_start}} and {{cmd_next}} from
# strings cmd.start and cmd.next (what the coach types); {{h_instructions}} and {{h_method}} from this table.
#   description  the skill's description (SKILL.md): at most PLUGIN_DESCRIPTION_MAX characters, no '<' or '>'
#   pointer      one line under the front matter that points SKILL.md to the method file next to it
#   intro        the one-file kit's opening, then the headings h_instructions and h_method
#   readme       this edition's half of the plugin's README.md: what to do in Claude and in ChatGPT, then what to type
#   save_from    the kit's own save line, exactly as core/<lang>/start-block.md prints it in 1-INSTRUCTIONS.txt. The
#                outputs carry strings key portable.save instead (a chat is not a project, so "Save to project" and
#                "Add text content" do not apply). If the kit stops printing save_from exactly once, the build
#                stops (portable_instructions). Without portable.save the outputs are skipped, like any target
#                whose source a later phase writes.
PORTABLE = {
    "en": {
        "description": 'Content Machine for coaches: from a voice dump to one message, a video to film today and a '
                       'week plan. Use when the user says "{{cmd_start}}", "{{cmd_next}}", or asks for content.',
        "pointer": "The method file CONTENT-MACHINE-{{file_suffix}}.md sits next to this file. Each part starts with "
                   "§CM-…: read that part before the job it covers.",
        "save_from": "Save: ChatGPT: ⋯ under the card → Save to project. Claude: copy it, + by the project files → "
                     "Add text content. Backup: email it to yourself.",
        "h_instructions": "INSTRUCTIONS",
        "h_method": "METHOD",
        "intro": "# {{name}} — a file for the AI\n\nYou are the AI receiving this file. Read all of it. "
                 "{{h_instructions}} is how you work for this whole chat; {{h_method}} is the "
                 "CONTENT-MACHINE-{{file_suffix}}.md file {{h_instructions}} mentions, with the §CM- parts to read "
                 'before each job. When the user says "{{cmd_start}}" (or "{{cmd_next}}"), follow '
                 "{{h_instructions}}. Don't summarise the file or mention it.",
        "readme": "## English\n\n"
                  "One file, `content-machine-plugin.zip`, for both Claude and ChatGPT, with the English and the "
                  "Vietnamese edition in it. Keep it zipped; do not unzip it.\n\n"
                  "**Claude (Pro)**\n"
                  "1. claude.ai on a computer → Customize → Plugins → Add → Upload plugin → choose the zip.\n"
                  "2. If Claude says it needs Code execution: Settings → Capabilities → turn it on.\n"
                  "3. Open a new chat (web, desktop or phone) and type `{{cmd_start}}`.\n\n"
                  "**ChatGPT (Plus/Pro)**\n"
                  "1. Settings → Security and login → turn on Developer mode.\n"
                  "2. Plugins → upload the zip.\n"
                  "3. Open a new chat and type `{{cmd_start}}`.\n\n"
                  "Next day: say `{{cmd_next}}` in the same chat. In a new chat, paste the Brand Card first.",
    },
    "vn": {
        "description": 'Content Machine cho coach: từ lời kể ra thông điệp, video quay hôm nay, kế hoạch tuần. '
                       'Dùng khi người dùng gõ "{{cmd_start}}", "{{cmd_next}}", hay nhờ làm content, video, bài đăng.',
        "pointer": "File phương pháp CONTENT-MACHINE-{{file_suffix}}.md nằm cạnh file này. Mỗi phần bắt đầu bằng "
                   "§CM-…: đọc đúng phần đó trước khi làm việc nó nói tới.",
        "save_from": "Lưu: ChatGPT: ⋯ dưới card → Lưu vào dự án. Claude: chép card, + cạnh file của project → "
                     'Add text content. Dự phòng: gửi vào Zalo "Cloud của tôi".',
        "h_instructions": "HƯỚNG DẪN",
        "h_method": "PHƯƠNG PHÁP",
        "intro": "# {{name}} — file cho AI đọc\n\nBạn là AI đang nhận file này. Đọc hết file. Phần "
                 "{{h_instructions}} là cách bạn làm việc suốt cuộc trò chuyện này; phần {{h_method}} chính là file "
                 "CONTENT-MACHINE-{{file_suffix}}.md mà {{h_instructions}} nhắc tới, với các mục §CM- để tra trước "
                 'mỗi việc. Khi người dùng gõ "{{cmd_start}}" (hay "{{cmd_next}}"), làm theo '
                 "{{h_instructions}}. Không tóm tắt file, không nhắc tới file.",
        "readme": "## Tiếng Việt\n\n"
                  "Một file `content-machine-plugin.zip` dùng cho cả Claude và ChatGPT, có cả tiếng Việt lẫn tiếng "
                  "Anh. Để nguyên file zip, không giải nén.\n\n"
                  "**Claude (Pro)**\n"
                  "1. claude.ai trên máy tính → Customize → Plugins → Add → Upload plugin → chọn file zip.\n"
                  "2. Nếu Claude báo cần Code execution: Settings → Capabilities → bật lên.\n"
                  "3. Mở chat mới (web, máy tính hay điện thoại), gõ `{{cmd_start}}`.\n\n"
                  "**ChatGPT (Plus/Pro)**\n"
                  "1. Settings → Security and login → bật Developer mode.\n"
                  "2. Mục Plugins → tải file zip lên.\n"
                  "3. Mở chat mới, gõ `{{cmd_start}}`.\n\n"
                  "Hôm sau: nhắn `{{cmd_next}}` ngay trong đoạn chat cũ. Mở chat mới thì dán Brand Card vào trước.",
    },
}
SAVE_KEY = "portable.save"
PLUGIN_DESCRIPTION_MAX = 200     # claude.ai skill description limit (lint E102 holds the same line)
# The one plugin at dist/content-machine-plugin.zip. Claude takes it as is; OpenAI's plugin portal accepts a Claude
# plugin archive and converts it, so one package serves both apps. Skills go in this order.
PLUGIN_ZIP = "content-machine-plugin.zip"
PLUGIN_NAME = "content-machine"
PLUGIN_EDITIONS = ("vn", "en")
PLUGIN_DESCRIPTION = ("Content Machine for coaches (Tiếng Việt + English): a voice dump becomes one message, "
                      "a video to film today and a week plan.")
PLUGIN_KEYWORDS = ["content", "coach", "vn", "en"]
PLUGIN_README_HEAD = "# Content Machine — plugin\n\nTiếng Việt: gõ `{vn}` · English: type `{en}`"


def _matches(selector: str, sections: dict) -> bool:
    """True when a method.toml selector (exact id or prefix*) matches any section."""
    if selector.endswith("*"):
        return any(sid.startswith(selector[:-1]) for sid in sections)
    return selector in sections


# ---------------------------------------------------------------- report

@dataclass
class Report:
    targets: dict
    artifacts: dict = field(default_factory=dict)
    skipped: list = field(default_factory=list)
    notes: list = field(default_factory=list)

    def skip(self, edition: str, target: str, reason: str, item: str | None = None) -> None:
        entry = {"edition": edition, "target": target, "reason": reason}
        if item:
            entry["item"] = item
        self.skipped.append(entry)

    def note(self, edition: str, text: str) -> None:
        self.notes.append({"edition": edition, "note": text})

    def budget(self, name: str, edition: str, used: int) -> dict | None:
        spec = self.targets.get("budgets", {}).get(name)
        if not spec or edition not in spec:
            return None
        limit = spec[edition]
        return {
            "unit": spec.get("unit", ""),
            "budget": limit,
            "used": used,
            "percent": round(used * 100 / limit, 1) if limit else None,
        }


def text_stats(data: bytes) -> dict:
    stats = {"bytes": len(data), "nfc_chars": None, "lines": None, "sha256": hashlib.sha256(data).hexdigest()}
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return stats
    stats["nfc_chars"] = cmlib.nfc_len(text)
    stats["lines"] = text.count("\n") + (1 if text and not text.endswith("\n") else 0)
    return stats


def measure(stats: dict, unit: str, override: int | None = None) -> int | None:
    if override is not None:
        return override
    return {"chars_nfc": stats["nfc_chars"], "bytes": stats["bytes"], "lines": stats["lines"]}.get(unit)


def skill_description(skill_md: str) -> str | None:
    """The `description:` value from SKILL.md front matter (plain, quoted or folded)."""
    lines = skill_md.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return None
        if line.startswith("description:"):
            value = line[len("description:"):].strip()
            if value in (">", "|", ">-", "|-", ""):
                parts = []
                for cont in lines[i + 1:]:
                    if cont.strip() == "---" or (cont and not cont[0].isspace()):
                        break
                    parts.append(cont.strip())
                return " ".join(p for p in parts if p)
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            return value
    return None


# ---------------------------------------------------------------- ship_lint bundling

MODREF = '__import__("sys").modules[__name__]'
STDLIB = set(sys.stdlib_module_names) | {"__future__"}


def _cmcore_kind(name: str | None) -> str | None:
    if not name:
        return None
    if name == "cmcore.checks" or name.endswith(".cmcore.checks"):
        return "checks"
    if name == "cmcore" or name.endswith(".cmcore"):
        return "package"
    return None


def _is_cmcore_import(node) -> bool:
    if isinstance(node, ast.ImportFrom):
        return _cmcore_kind(node.module) is not None
    if isinstance(node, ast.Import):
        return any(_cmcore_kind(a.name) for a in node.names)
    return False


def _namespace(dotted: str) -> str:
    """`a.b.checks` -> a SimpleNamespace chain ending at this module (bound to `a`)."""
    expr = MODREF
    for part in reversed(dotted.split(".")[1:]):
        expr = f'__import__("types").SimpleNamespace({part}={expr})'
    return expr


def _bindings(node, where: str) -> list[str]:
    """Statements that replace a cmcore import once checks.py is inlined."""
    out: list[str] = []
    if isinstance(node, ast.ImportFrom):
        kind = _cmcore_kind(node.module)
        for a in node.names:
            if kind == "checks":
                if a.name != "*" and a.asname and a.asname != a.name:
                    out.append(f"{a.asname} = {a.name}")
            elif a.name == "checks":
                out.append(f"{a.asname or 'checks'} = {MODREF}")
            else:
                raise CMError("E170", f"ship_lint: cannot inline 'from {node.module} import {a.name}'", where)
        return out
    for a in node.names:
        kind = _cmcore_kind(a.name)
        if kind is None:
            out.append(f"import {a.name}" + (f" as {a.asname}" if a.asname else ""))
        elif a.asname:
            if kind != "checks":
                raise CMError("E170", f"ship_lint: cannot inline 'import {a.name} as {a.asname}'", where)
            out.append(f"{a.asname} = {MODREF}")
        else:
            dotted = a.name if kind == "checks" else a.name + ".checks"
            out.append(f"{dotted.split('.')[0]} = {_namespace(dotted)}")
    return out


def _check_imports(tree, where: str, allow_cmcore: bool) -> None:
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if node.level:
                raise CMError("E170", "ship_lint: relative import is not self-contained", where)
            names = [node.module or ""]
        elif isinstance(node, ast.Import):
            names = [a.name for a in node.names]
        else:
            continue
        for name in names:
            if _cmcore_kind(name):
                if allow_cmcore:
                    continue
                raise CMError("E170", f"ship_lint: import of '{name}' left after inlining", where)
            if name.split(".")[0] not in STDLIB:
                raise CMError("E170", f"ship_lint: imports non-standard module '{name}'", where)


def _strip_for_inline(src: str, where: str) -> tuple[list[str], set[str]]:
    """checks.py lines minus `from __future__` imports and `if __name__ == "__main__"` blocks."""
    tree = ast.parse(src, where)
    _check_imports(tree, where, allow_cmcore=False)
    futures: set[str] = set()
    drop: set[int] = set()
    for stmt in tree.body:
        is_future = isinstance(stmt, ast.ImportFrom) and stmt.module == "__future__"
        is_main = (isinstance(stmt, ast.If) and isinstance(stmt.test, ast.Compare)
                   and isinstance(stmt.test.left, ast.Name) and stmt.test.left.id == "__name__")
        if is_future:
            futures.update(a.name for a in stmt.names)
        if is_future or is_main:
            drop.update(range(stmt.lineno, stmt.end_lineno + 1))
    lines = src.splitlines(keepends=True)
    return [ln for i, ln in enumerate(lines, start=1) if i not in drop], futures


def _start_line(stmt) -> int:
    """First line of a statement, decorators included."""
    return min([stmt.lineno] + [d.lineno for d in getattr(stmt, "decorator_list", [])])


def bundle_shiplint(root: Path) -> str | None:
    """tools/shiplint.py as one self-contained file, with cmcore/checks.py inlined.

    Returns None when tools/shiplint.py does not exist yet.
    """
    src_path = root / "tools" / "shiplint.py"
    if not src_path.exists():
        return None
    where = "tools/shiplint.py"
    src = src_path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(src, where)
    except SyntaxError as exc:
        raise CMError("E170", f"ship_lint: {exc}", where)
    imports = sorted((n for n in ast.walk(tree) if _is_cmcore_import(n)), key=lambda n: n.lineno)
    if imports:
        checks_rel = "tools/cmcore/checks.py"
        try:
            checks_src = (root / checks_rel).read_text(encoding="utf-8")
        except FileNotFoundError:
            raise CMError("E161", "shiplint imports cmcore.checks but the file is missing", checks_rel)
        inline, futures = _strip_for_inline(checks_src, checks_rel)
        lines = src.splitlines(keepends=True)
        if lines and not lines[-1].endswith("\n"):
            lines[-1] += "\n"
        if inline and not inline[-1].endswith("\n"):
            inline[-1] += "\n"
        # Inline once at top level, before the statement holding the first cmcore import.
        first = imports[0]
        holder = next(s for s in tree.body if s.lineno <= first.lineno <= s.end_lineno)
        insert_at = _start_line(holder) - 1
        for node in reversed(imports):
            indent = " " * node.col_offset
            new = [indent + b + "\n" for b in _bindings(node, where)] or [indent + "pass\n"]
            lines[node.lineno - 1:node.end_lineno] = new
        block = ([f"# ---- inlined from {checks_rel} by tools/build.py; edit that file, not this copy ----\n"]
                 + inline + [f"# ---- end of {checks_rel} ----\n"])
        lines[insert_at:insert_at] = block
        have = {a.name for s in tree.body if isinstance(s, ast.ImportFrom) and s.module == "__future__"
                for a in s.names}
        missing = sorted(futures - have)
        if missing:
            doc = tree.body[0] if tree.body and isinstance(tree.body[0], ast.Expr) \
                and isinstance(getattr(tree.body[0], "value", None), ast.Constant) \
                and isinstance(tree.body[0].value.value, str) else None
            at = doc.end_lineno if doc else (_start_line(tree.body[0]) - 1 if tree.body else 0)
            lines[at:at] = [f"from __future__ import {', '.join(missing)}\n"]
        src = "".join(lines)
    try:
        out_tree = ast.parse(src, "ship_lint.py")
        compile(src, "ship_lint.py", "exec")
    except SyntaxError as exc:
        raise CMError("E170", f"ship_lint: bundled file does not compile: {exc}", where)
    _check_imports(out_tree, where, allow_cmcore=False)
    return src


def portable_zip(files: dict[str, bytes], where: str) -> bytes:
    """A plugin zip in memory, written like package.make_zip (sorted, fixed date and mode, level 9).

    make_zip leaves dotfiles out and a Claude plugin must hold .claude-plugin/plugin.json, so it cannot write it.
    """
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        for name in sorted(files):
            check_ascii(name, where)
            info = zipfile.ZipInfo(name, date_time=ZIP_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = FILE_MODE << 16
            zf.writestr(info, files[name], compresslevel=9)
    return buf.getvalue()


# ---------------------------------------------------------------- one edition

class EditionBuild:
    def __init__(self, root: Path, edition_id: str, report: Report):
        self.root = root
        self.report = report
        self.ed = cmlib.load_edition(edition_id, root)
        self.id = edition_id
        self.dist = root / "dist"
        self.out = self.dist / edition_id
        prose = self.ed.cfg.get("method_prose", self.ed.lang)
        self.sections, dupes = cmlib.load_sections(prose, root)
        if dupes:
            raise CMError("E114", "duplicate section id(s): " + ", ".join(sorted(set(dupes))), f"{prose} prose")
        method_path = root / "core" / "method.toml"
        self.method = cmlib.load_toml(method_path) if method_path.exists() else None

    # -- helpers

    def src(self, *parts: str) -> Path:
        return self.root.joinpath(*parts)

    def write(self, path: Path, text: str | bytes) -> Path:
        relp = cmlib.rel(path, self.dist)
        check_ascii(relp, "dist")
        path.parent.mkdir(parents=True, exist_ok=True)
        data = text.encode("utf-8") if isinstance(text, str) else text
        path.write_bytes(data)
        return path

    def record(self, path: Path, target: str, budgets: list[str] = (), overrides: dict | None = None,
               **extra) -> dict:
        stats = text_stats(path.read_bytes())
        entry = {"edition": self.id, "target": target, **stats}
        found = {}
        for name in budgets:
            spec = self.report.targets.get("budgets", {}).get(name, {})
            used = measure(stats, spec.get("unit", ""), (overrides or {}).get(name))
            b = self.report.budget(name, self.id, used) if used is not None else None
            if b:
                found[name] = b
        if found:
            entry["budgets"] = found
        entry.update(extra)
        key = Path(path).resolve().relative_to(self.dist.resolve()).as_posix()
        self.report.artifacts[key] = entry
        return entry

    def clean(self) -> None:
        for d in (self.out, self.dist / "maintainer" / "tasks" / self.id,
                  self.dist / "maintainer" / "skill" / self.id, self.dist / "site" / self.id):
            if d.exists():
                shutil.rmtree(d)
        self.out.mkdir(parents=True)

    # -- targets

    def build(self) -> None:
        self.clean()
        self.build_kit()
        self.build_phone()
        self.build_anchor_file("method", f"CONTENT-MACHINE-{self.ed.file_suffix}.md")
        self.build_anchor_file("grow", f"Level-ups/GROW-{self.ed.file_suffix}.md")
        self.build_skill()
        self.build_portable()
        self.build_start_here()
        self.build_guides()
        self.build_tasks()

    def build_kit(self) -> None:
        src = self.src("core", self.ed.lang, "start-block.md")
        if not src.exists():
            self.report.skip(self.id, "kit", f"{cmlib.rel(src, self.root)} not present yet")
            return
        out = self.write(self.out / "1-INSTRUCTIONS.txt", render_file(src, self.ed, "kit", root=self.root))
        self.record(out, "kit", FILE_BUDGETS["kit"], source=cmlib.rel(src, self.root))

    def build_phone(self) -> None:
        src = self.src("core", self.ed.lang, "phone-starter.md")
        if not src.exists():
            src = self.src("core", self.ed.lang, "start-block.md")
        if not src.exists():
            self.report.skip(self.id, "phone", f"core/{self.ed.lang}/start-block.md not present yet")
            return
        out = self.write(self.out / "PHONE-STARTER.txt", render_file(src, self.ed, "phone", root=self.root))
        self.record(out, "phone", FILE_BUDGETS["phone"], source=cmlib.rel(src, self.root))

    def title_for(self, table: str, cfg: dict, target: str) -> str:
        key = cfg.get("title_key")
        if key is None:
            key = f"{table}.title" if f"{table}.title" in self.ed.strings else None
        return render_string(key, self.ed, target) if key else self.ed.name

    def anchor_title(self, anchor_id: str, target: str) -> str:
        key = f"anchor.{anchor_id.lower()}"
        return render_string(key, self.ed, target) if key in self.ed.strings else anchor_id

    def build_anchor_file(self, table: str, relpath: str) -> None:
        """CONTENT-MACHINE-*.md from [method], GROW-*.md from [grow]."""
        target = table
        if self.method is None:
            self.report.skip(self.id, target, "core/method.toml not present yet")
            return
        cfg = self.method.get(table) or {}
        anchors = cfg.get("anchor", [])
        if not anchors:
            self.report.skip(self.id, target, f"core/method.toml [{table}] has no anchors yet")
            return
        seen: set[str] = set()
        blocks: list[tuple[str, str]] = []
        for anchor in anchors:
            aid = anchor.get("id")
            where = f"core/method.toml [{table}] anchor {aid}"
            if not aid:
                raise CMError("E161", f"[[{table}.anchor]] without an id", "core/method.toml")
            if aid in seen:
                raise CMError("E161", f"duplicate anchor id '{aid}'", "core/method.toml")
            seen.add(aid)
            selectors = anchor.get("sections") or []
            if not selectors:
                self.report.skip(self.id, target, "anchor has no sections yet", item=f"§CM-{aid}")
                continue
            if not any(_matches(sel, self.sections) for sel in selectors):
                # Not one selector matches yet: the module is written in a later step.
                self.report.skip(self.id, target, "anchor's modules not written yet", item=f"§CM-{aid}")
                continue
            picked = cmlib.select_sections(selectors, self.sections, where)
            body = "\n".join(cmlib.render(s.body, self.ed, target, path=f"{s.file}#{s.id}") for s in picked)
            blocks.append((aid, f"## §CM-{aid} · {self.anchor_title(aid, target)}\n\n{body.strip()}\n"))
        if not blocks:
            self.report.skip(self.id, target, f"no [{table}] anchor has sections yet")
            return
        head = [f"# {self.title_for(table, cfg, target)}\n"]
        contract = []
        if CONTRACT_KEY in self.ed.strings:
            contract = [render_string(CONTRACT_KEY, self.ed, target) + "\n"]
        text = cmlib.finish("\n".join(head + contract + [b for _, b in blocks] + contract))
        out = self.write(self.out / relpath, text)
        anchor_sizes = {}
        for aid, block in blocks:
            size = len(cmlib.nfc(block).encode("utf-8"))
            entry = {"bytes": size}
            b = self.report.budget("method_section", self.id, size) if table == "method" else None
            if b:
                entry["budgets"] = {"method_section": b}
            anchor_sizes[f"§CM-{aid}"] = entry
        self.record(out, target, FILE_BUDGETS[target], anchors=anchor_sizes)

    def build_skill(self) -> None:
        tmpl = self.src("core", "SKILL.md.tmpl")
        if not tmpl.exists():
            self.report.skip(self.id, "skill", "core/SKILL.md.tmpl not present yet")
            return
        name = self.ed.skill_name
        stage = self.dist / "maintainer" / "skill" / self.id / name
        skill_md = self.write(stage / "SKILL.md", render_file(tmpl, self.ed, "skill", root=self.root))
        skill_text = skill_md.read_text(encoding="utf-8")
        desc = skill_description(skill_text)
        overrides = {}
        md_budgets = list(SKILL_MD_BUDGETS)
        if desc is not None:
            overrides["skill_description"] = cmlib.nfc_len(desc)
            md_budgets.append("skill_description")
        else:
            self.report.note(self.id, "SKILL.md has no front-matter description")
        zip_rel = f"{self.id}/Level-ups/autopilot/{name}.zip"
        self.record(skill_md, "skill", md_budgets, overrides, in_zip=zip_rel)

        refs = (self.method or {}).get("skill", {}).get("reference", [])
        router = self.load_core("router.toml") if refs else {}
        checks = self.load_core("format-checks.toml") if refs else {}
        total = 0
        for ref in refs:
            file = ref.get("file", "")
            if not file.endswith(".md") or "/" in file or "\\" in file:
                raise CMError("E161", f"bad skill reference file name '{file}'", "core/method.toml [skill]")
            if not ref.get("sections"):
                self.report.skip(self.id, "skill", "reference has no sections yet", item=f"references/{file}")
                continue
            text = render_reference(self.ed, ref, self.sections, router, checks,
                                    path=f"core/method.toml [skill] {file}")
            path = self.write(stage / "references" / file, text)
            total += path.stat().st_size
            self.record(path, "skill", REFERENCE_BUDGETS, in_zip=zip_rel)
        if not refs:
            self.report.note(self.id, "skill has no [skill] references yet (empty skill)")

        script = bundle_shiplint(self.root)
        if script is None:
            self.report.skip(self.id, "skill", "tools/shiplint.py not present yet", item="scripts/ship_lint.py")
        else:
            path = self.write(stage / "scripts" / "ship_lint.py", script)
            self.record(path, "skill", in_zip=zip_rel)

        out = self.out / "Level-ups" / "autopilot" / f"{name}.zip"
        entries = make_zip(stage, out, prefix=name)
        self.record(out, "skill", FILE_BUDGETS["skill"] + ["references_total_bytes"],
                    {"references_total_bytes": total}, entries=entries)

    def load_core(self, name: str) -> dict:
        path = self.src("core", name)
        if not path.exists():
            self.report.note(self.id, f"core/{name} not present; skill headers/footers cannot resolve")
            return {}
        return cmlib.load_toml(path)

    def portable_text(self, key: str) -> str:
        """One PORTABLE text for this edition, its {{tags}} filled."""
        table = PORTABLE[self.ed.lang]
        text = table[key]
        local = {"h_instructions": table["h_instructions"], "h_method": table["h_method"],
                 "cmd_start": render_string("cmd.start", self.ed, "kit"),
                 "cmd_next": render_string("cmd.next", self.ed, "kit")}
        for tag, value in local.items():
            text = text.replace("{{%s}}" % tag, value)
        return cmlib.render(text, self.ed, "kit", path=f"tools/build.py PORTABLE['{self.ed.lang}']['{key}']").strip()

    def portable_instructions(self, kit: Path) -> str:
        """The kit text with its save line swapped for the portable one; the build stops unless it is there once."""
        text = kit.read_text(encoding="utf-8")
        old = PORTABLE[self.ed.lang]["save_from"]
        found = text.count(old)
        if found != 1:
            raise CMError("E170", f"the kit's save line must appear exactly once to be swapped for the plugin and "
                                  f"the one-file kit, found {found}; update PORTABLE['{self.ed.lang}']['save_from'] "
                                  f"in tools/build.py to match core/{self.ed.lang}/start-block.md",
                          cmlib.rel(kit, self.root))
        return text.replace(old, render_string("portable.save", self.ed, "kit"))

    def portable_blocker(self) -> str | None:
        """Why the portable outputs cannot be built for this edition yet, or None."""
        if SAVE_KEY not in self.ed.strings:
            return f"strings key {SAVE_KEY} not present yet"
        if not (self.out / "1-INSTRUCTIONS.txt").exists() or not self.method_path().exists():
            return "needs 1-INSTRUCTIONS.txt and the method file, which are not built yet"
        if self.ed.lang not in PORTABLE:
            return f"no PORTABLE texts for language '{self.ed.lang}' in tools/build.py"
        return None

    def method_path(self) -> Path:
        return self.out / f"CONTENT-MACHINE-{self.ed.file_suffix}.md"

    def portable_parts(self) -> dict:
        """What the plugin and the one-file kit are made of, from the kit and method file built in dist/<ed>/."""
        instructions = self.portable_instructions(self.out / "1-INSTRUCTIONS.txt")
        method = self.method_path()
        name = f"content-machine-{self.id}"
        description = self.portable_text("description")
        n = cmlib.nfc_len(description)
        if n > PLUGIN_DESCRIPTION_MAX or "<" in description or ">" in description:
            raise CMError("E102", f"skill description is {n} characters (max {PLUGIN_DESCRIPTION_MAX}) "
                                  "and must not contain '<' or '>'", f"tools/build.py PORTABLE['{self.ed.lang}']")
        # description as a double-quoted YAML scalar (JSON quoting is valid YAML): it holds ': ' and quotes
        front = f"---\nname: {name}\ndescription: {json.dumps(description, ensure_ascii=False)}\n---\n\n"
        heading = PORTABLE[self.ed.lang]
        one = (self.portable_text("intro") + f"\n\n## {heading['h_instructions']}\n\n" + instructions.rstrip()
               + f"\n\n## {heading['h_method']}\n\n" + method.read_text(encoding="utf-8"))
        return {
            "name": name,
            "brand": self.ed.name,
            "skill_md": cmlib.nfc(front + f"{self.portable_text('pointer')}\n\n{instructions}").encode("utf-8"),
            "method_name": method.name,
            "method": method.read_bytes(),
            "one_file": cmlib.finish(one),
            "readme": self.portable_text("readme"),
            "cmd_start": render_string("cmd.start", self.ed, "kit"),
        }

    def build_portable(self) -> None:
        """CONTENT-MACHINE-<SUFFIX>-1-FILE.md from the built kit and method file."""
        reason = self.portable_blocker()
        if reason:
            self.report.skip(self.id, "onefile", reason)
            return
        out = self.write(self.out / f"CONTENT-MACHINE-{self.ed.file_suffix}-1-FILE.md",
                         self.portable_parts()["one_file"])
        self.record(out, "onefile")

    def build_start_here(self) -> None:
        keys = ("starthere.title", "starthere.body")
        if not all(k in self.ed.strings for k in keys):
            self.report.skip(self.id, "help", "strings starthere.title / starthere.body missing",
                             item="START-HERE.html")
            return
        title = render_string("starthere.title", self.ed, "help")
        body = render_string("starthere.body", self.ed, "help")
        url = str(self.ed.cfg.get("setup_url") or self.ed.params.get("setup_url") or "")
        if not url:
            if not (self.out / "1-INSTRUCTIONS.txt").exists():
                self.report.skip(self.id, "help", "no [edition] setup_url and no 1-INSTRUCTIONS.txt to link to",
                                 item="START-HERE.html")
                return
            url = "1-INSTRUCTIONS.txt"
            self.report.note(self.id, "START-HERE.html links to 1-INSTRUCTIONS.txt until [edition] setup_url is set")
        lang = "vi" if self.ed.lang == "vn" else self.ed.lang
        page = (
            "<!doctype html>\n"
            f'<html lang="{lang}">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f"<title>{html.escape(title)}</title>\n"
            "<style>body{font-family:system-ui,sans-serif;max-width:36rem;margin:2rem auto;"
            "padding:0 1rem;line-height:1.5}a{font-size:1.25rem}</style>\n"
            "</head>\n<body>\n"
            f"<h1>{html.escape(title)}</h1>\n"
            + "".join(f"<p>{html.escape(p)}</p>\n" for p in body.split("\n\n") if p.strip())
            + f'<p><a href="{html.escape(url, quote=True)}">{html.escape(url)}</a></p>\n'
            "</body>\n</html>\n"
        )
        out = self.write(self.out / "START-HERE.html", cmlib.nfc(page))
        self.record(out, "help")

    def build_guides(self) -> None:
        guides = self.src("guides")
        tmpls = sorted(guides.glob("*.tmpl")) if guides.is_dir() else []
        help_tmpls = [t for t in tmpls if t.name != SITE_TEMPLATE]
        if not help_tmpls:
            self.report.skip(self.id, "help", "guides/*.tmpl not present yet", item="Help/")
        for t in help_tmpls:
            out = self.write(self.out / "Help" / f"{t.stem}.html", render_file(t, self.ed, "help", root=self.root))
            self.record(out, "help", source=cmlib.rel(t, self.root))
        site = guides / SITE_TEMPLATE
        if not site.exists():
            self.report.skip(self.id, "site", f"guides/{SITE_TEMPLATE} not present yet")
            return
        out = self.write(self.dist / "site" / self.id / "index.html", render_file(site, self.ed, "site", root=self.root))
        self.record(out, "site", source=cmlib.rel(site, self.root))

    def build_tasks(self) -> None:
        auto = self.src("automation")
        tmpls = sorted(auto.glob("*.tmpl")) if auto.is_dir() else []
        if not tmpls:
            self.report.skip(self.id, "task", "automation/*.tmpl not present yet")
            return
        budgets = self.report.targets.get("budgets", {})
        for t in tmpls:
            extra = tuple(f for f in cmlib.EXTRA_FLAGS if f in t.stem)
            text = render_file(t, self.ed, "task", extra, root=self.root)
            out = self.write(self.dist / "maintainer" / "tasks" / self.id / f"{t.stem}.txt", text)
            names = [n for n, spec in budgets.items()
                     if str(spec.get("artifact", "")).startswith(f"automation/{t.name}")]
            self.record(out, "task", names, source=cmlib.rel(t, self.root))


def build_plugin(root: Path, report: Report, builds: dict[str, EditionBuild]) -> None:
    """dist/content-machine-plugin.zip: both editions' skills in one Claude-format plugin.

    Read from dist/<edition>/ on disk, so a one-edition build still gets both skills if the other is built. A zip
    from an earlier build is removed when this one cannot make a new one.
    """
    out = root / "dist" / PLUGIN_ZIP
    parts: dict[str, dict] = {}
    for ed in PLUGIN_EDITIONS:
        edition = builds.get(ed) or EditionBuild(root, ed, report)
        reason = edition.portable_blocker()
        if reason:
            report.skip("all", "plugin", f"{ed}: {reason}")
            out.unlink(missing_ok=True)
            return
        parts[ed] = edition.portable_parts()
    readme = "\n\n".join([PLUGIN_README_HEAD.format(**{ed: parts[ed]["cmd_start"] for ed in PLUGIN_EDITIONS}),
                          *(parts[ed]["readme"] for ed in PLUGIN_EDITIONS)]) + "\n"
    manifest = {"name": PLUGIN_NAME, "version": read_version(root), "description": PLUGIN_DESCRIPTION,
                "author": {"name": parts[PLUGIN_EDITIONS[0]]["brand"]}, "keywords": PLUGIN_KEYWORDS}
    files = {f"{PLUGIN_NAME}/.claude-plugin/plugin.json":
             (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
             f"{PLUGIN_NAME}/README.md": cmlib.nfc(readme).encode("utf-8")}
    for ed in PLUGIN_EDITIONS:
        part = parts[ed]
        files[f"{PLUGIN_NAME}/skills/{part['name']}/SKILL.md"] = part["skill_md"]
        files[f"{PLUGIN_NAME}/skills/{part['name']}/{part['method_name']}"] = part["method"]
    data = portable_zip(files, cmlib.rel(out, root))
    out.write_bytes(data)
    report.artifacts[PLUGIN_ZIP] = {"edition": "all", "target": "plugin", **text_stats(data),
                                    "entries": sorted(files)}


# ---------------------------------------------------------------- whole build

def build(root: Path, editions: list[str]) -> dict:
    """Build the given editions under root; write and return the manifest."""
    root = Path(root).resolve()
    targets_path = root / "platform" / "targets.toml"
    targets = cmlib.load_toml(targets_path) if targets_path.exists() else {}
    report = Report(targets=targets)
    if not targets:
        report.note("all", "platform/targets.toml not present; no budgets in this manifest")
    version = read_version(root)
    builds: dict[str, EditionBuild] = {}
    for ed in editions:
        builds[ed] = EditionBuild(root, ed, report)
        builds[ed].build()
    build_plugin(root, report, builds)
    manifest = {
        "schema": 1,
        "version": version,
        "editions": sorted(editions),
        "build_sha256": compute_build_sha256(root / "dist", editions),
        "artifacts": dict(sorted(report.artifacts.items())),
        "skipped": report.skipped,
        "notes": report.notes,
    }
    out = root / "dist" / "maintainer" / "manifest.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=False) + "\n", encoding="utf-8")
    return manifest


def summary(manifest: dict) -> str:
    rows = []
    for path, a in manifest["artifacts"].items():
        worst = max((b["percent"] for b in a.get("budgets", {}).values() if b.get("percent") is not None),
                    default=None)
        pct = f"{worst:5.1f}%" if worst is not None else "      "
        rows.append(f"  {pct}  {a['bytes']:>8} B  {path}")
    lines = [f"build {manifest['version']}  sha256 {manifest['build_sha256']}"] + rows
    if manifest["skipped"]:
        lines.append(f"  skipped: {len(manifest['skipped'])} (see dist/maintainer/manifest.json)")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Assemble dist/<edition>/ and dist/maintainer/.")
    ap.add_argument("--edition", required=True, choices=[*cmlib.EDITIONS, "all"])
    ap.add_argument("--root", type=Path, default=None, help="repo root (default: CM_ROOT or this repo)")
    args = ap.parse_args(argv)
    root = (args.root or cmlib.ROOT).resolve()
    editions = list(cmlib.EDITIONS) if args.edition == "all" else [args.edition]
    try:
        manifest = build(root, editions)
    except CMError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    print(summary(manifest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
