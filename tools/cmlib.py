"""Shared library for the Content Machine build tools (standard library only).

Loads editions, strings, prose sections and method maps, and implements the
small template language described in docs/BUILD.md §4.
"""
from __future__ import annotations

import hashlib
import os
import re
import tomllib
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(os.environ.get("CM_ROOT", Path(__file__).resolve().parent.parent))

EDITIONS = ("en", "vn")
TARGET_FLAGS = ("kit", "phone", "method", "grow", "skill", "task", "help", "site")
EXTRA_FLAGS = ("connected", "standalone")

SECTION_RE = re.compile(r"^<!--\s*@section\s+([a-z0-9][a-z0-9._-]*)((?:\s+[a-z_]+=[^\s>]+)*)\s*-->\s*$", re.M)
ATTR_RE = re.compile(r"([a-z_]+)=([^\s>]+)")
TAG_RE = re.compile(r"\{\{(.*?)\}\}", re.S)
NAME_RE = re.compile(r"^[a-z_][a-z0-9_]*$")
KEY_RE = re.compile(r"^[a-z0-9_.-]+$")


class CMError(Exception):
    """A build error with a lint code (docs/BUILD.md §7)."""

    def __init__(self, code: str, message: str, path: str | None = None):
        super().__init__(f"{code} {path + ': ' if path else ''}{message}")
        self.code = code
        self.path = path
        self.message = message


# ---------------------------------------------------------------- text helpers

def nfc(text: str) -> str:
    return unicodedata.normalize("NFC", text)


def nfc_len(text: str) -> int:
    return len(nfc(text))


def sha10(text: str) -> str:
    return hashlib.sha256(nfc(text).encode("utf-8")).hexdigest()[:10]


def finish(text: str) -> str:
    """NFC-normalise and end with exactly one newline."""
    return nfc(text).rstrip() + "\n"


def load_toml(path: Path) -> dict:
    try:
        with open(path, "rb") as fh:
            return tomllib.load(fh)
    except FileNotFoundError:
        raise CMError("E161", "file not found", str(path))
    except tomllib.TOMLDecodeError as exc:
        raise CMError("E161", f"bad TOML: {exc}", str(path))


def rel(path: Path, root: Path | None = None) -> str:
    root = root or ROOT
    try:
        return str(Path(path).resolve().relative_to(root.resolve()))
    except ValueError:
        return str(path)


# ---------------------------------------------------------------- editions + strings

@dataclass
class Edition:
    id: str
    lang: str
    cfg: dict
    params: dict
    pending: dict
    strings: dict[str, str]
    string_src: dict[str, str] = field(default_factory=dict)

    @property
    def name(self) -> str:
        return self.cfg.get("name", "Content Machine")

    @property
    def skill_name(self) -> str:
        return self.cfg["skill_name"]

    @property
    def file_suffix(self) -> str:
        return self.cfg["file_suffix"]

    @property
    def zip_name(self) -> str:
        return self.cfg["zip_name"]

    def lookup(self, name: str):
        if name in self.params:
            return self.params[name]
        if name in self.cfg:
            return self.cfg[name]
        raise KeyError(name)


def load_strings(edition_id: str, root: Path | None = None) -> tuple[dict[str, str], dict[str, str]]:
    root = root or ROOT
    path = root / "strings" / f"{edition_id}.toml"
    if not path.exists():
        return {}, {}
    data = load_toml(path).get("strings", {})
    texts: dict[str, str] = {}
    srcs: dict[str, str] = {}
    for key, value in data.items():
        if isinstance(value, dict):
            texts[key] = value.get("text", "")
            if "src" in value:
                srcs[key] = value["src"]
        else:
            texts[key] = value
    return texts, srcs


def load_edition(edition_id: str, root: Path | None = None) -> Edition:
    root = root or ROOT
    data = load_toml(root / "editions" / f"{edition_id}.toml")
    cfg = data.get("edition", {})
    for key in ("id", "lang", "skill_name", "file_suffix", "zip_name"):
        if key not in cfg:
            raise CMError("E161", f"[edition] missing key '{key}'", f"editions/{edition_id}.toml")
    texts, srcs = load_strings(edition_id, root)
    return Edition(
        id=cfg["id"],
        lang=cfg["lang"],
        cfg=cfg,
        params=data.get("params", {}),
        pending=data.get("pending", {}),
        strings=texts,
        string_src=srcs,
    )


# ---------------------------------------------------------------- sections

@dataclass
class Section:
    id: str
    file: str
    body: str
    attrs: dict[str, str]
    order: int

    @property
    def module(self) -> str:
        return self.id.split(".", 1)[0]


def parse_sections(text: str, file: str = "") -> tuple[str, list[Section]]:
    """Split a prose file into (preamble, sections)."""
    matches = list(SECTION_RE.finditer(text))
    if not matches:
        return text, []
    preamble = text[: matches[0].start()]
    sections: list[Section] = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[m.end():end].strip("\n")
        attrs = dict(ATTR_RE.findall(m.group(2) or ""))
        sections.append(Section(id=m.group(1), file=file, body=body.strip(), attrs=attrs, order=i))
    return preamble, sections


def prose_files(lang: str, root: Path | None = None) -> list[Path]:
    root = root or ROOT
    files: list[Path] = []
    for folder in ("core", "modules"):
        d = root / folder / lang
        if d.is_dir():
            files.extend(sorted(d.glob("*.md")))
    return files


def load_sections(lang: str, root: Path | None = None) -> tuple[dict[str, Section], list[str]]:
    """Return (sections by id, duplicate ids)."""
    root = root or ROOT
    out: dict[str, Section] = {}
    dupes: list[str] = []
    seq = 0
    for path in prose_files(lang, root):
        _, secs = parse_sections(path.read_text(encoding="utf-8"), rel(path, root))
        for s in secs:
            s.order = seq
            seq += 1
            if s.id in out:
                dupes.append(s.id)
                continue
            out[s.id] = s
    return out, dupes


def select_sections(selectors: list[str], sections: dict[str, Section], where: str = "") -> list[Section]:
    picked: list[Section] = []
    seen: set[str] = set()
    ordered = sorted(sections.values(), key=lambda s: s.order)
    for sel in selectors:
        if sel.endswith(".*"):
            prefix = sel[:-1]
            hits = [s for s in ordered if s.id.startswith(prefix)]
        else:
            hits = [sections[sel]] if sel in sections else []
        if not hits:
            raise CMError("E130", f"selector '{sel}' matches no section", where or None)
        for s in hits:
            if s.id not in seen:
                picked.append(s)
                seen.add(s.id)
    return picked


LINT_OK_RE = re.compile(r"[ \t]*<!--\s*lint-ok:[A-Z0-9,]+\s*-->")


def strip_markers(text: str) -> str:
    """Remove section markers and inline `<!-- lint-ok:E143 -->` waivers."""
    return LINT_OK_RE.sub("", SECTION_RE.sub("", text))


# ---------------------------------------------------------------- template language

@dataclass
class Ctx:
    edition: Edition
    flags: frozenset[str]
    path: str = ""
    depth: int = 0


def _tokenize(text: str):
    pos = 0
    for m in TAG_RE.finditer(text):
        if m.start() > pos:
            yield ("text", text[pos:m.start()])
        yield ("tag", m.group(1).strip())
        pos = m.end()
    if pos < len(text):
        yield ("text", text[pos:])


def _parse(tokens: list, i: int, path: str, closing: str | None):
    """Parse tokens into a node list until the matching close tag."""
    nodes: list = []
    while i < len(tokens):
        kind, val = tokens[i]
        if kind == "text":
            nodes.append(("text", val))
            i += 1
            continue
        if val.startswith("#if ") or val.startswith("#unless "):
            op, _, cond = val.partition(" ")
            then, i, stop = _parse(tokens, i + 1, path, op[1:])
            other: list = []
            if stop == "else":
                other, i, stop = _parse(tokens, i, path, op[1:])
            if stop != "/" + op[1:]:
                raise CMError("E170", f"unclosed {{{{{val}}}}}", path)
            nodes.append((op[1:], cond.strip(), then, other))
            continue
        if val == "else":
            if closing is None:
                raise CMError("E170", "{{else}} outside a block", path)
            return nodes, i + 1, "else"
        if val.startswith("/"):
            if closing is None or val != "/" + closing:
                raise CMError("E170", f"unexpected {{{{{val}}}}}", path)
            return nodes, i + 1, val
        nodes.append(("var", val))
        i += 1
    if closing is not None:
        raise CMError("E170", f"unclosed {{{{#{closing}}}}}", path)
    return nodes, i, None


def _flag_true(cond: str, ctx: Ctx) -> bool:
    names = [c.strip() for c in cond.split(",") if c.strip()]
    if not names:
        raise CMError("E170", "empty condition", ctx.path)
    known = set(EDITIONS) | set(TARGET_FLAGS) | set(EXTRA_FLAGS)
    for n in names:
        if n not in known:
            raise CMError("E170", f"unknown flag '{n}'", ctx.path)
    return any(n in ctx.flags for n in names)


def _eval(nodes: list, ctx: Ctx) -> str:
    out: list[str] = []
    for node in nodes:
        kind = node[0]
        if kind == "text":
            out.append(node[1])
        elif kind in ("if", "unless"):
            truth = _flag_true(node[1], ctx)
            if kind == "unless":
                truth = not truth
            out.append(_eval(node[2] if truth else node[3], ctx))
        elif kind == "var":
            out.append(_var(node[1], ctx))
    return "".join(out)


def _var(name: str, ctx: Ctx) -> str:
    if name.startswith("t:"):
        key = name[2:].strip()
        if not KEY_RE.match(key):
            raise CMError("E170", f"bad string key '{key}'", ctx.path)
        if key not in ctx.edition.strings:
            raise CMError("E170", f"unknown string key '{key}'", ctx.path)
        if ctx.depth > 4:
            raise CMError("E170", f"string nesting too deep at '{key}'", ctx.path)
        inner = Ctx(ctx.edition, ctx.flags, ctx.path, ctx.depth + 1)
        return render_text(ctx.edition.strings[key], inner)
    if not NAME_RE.match(name):
        raise CMError("E170", f"bad tag '{{{{{name}}}}}'", ctx.path)
    try:
        value = ctx.edition.lookup(name)
    except KeyError:
        raise CMError("E170", f"unknown param '{name}'", ctx.path)
    if isinstance(value, (dict, list)):
        raise CMError("E170", f"param '{name}' is not a scalar", ctx.path)
    return str(value)


def render_text(text: str, ctx: Ctx) -> str:
    tokens = list(_tokenize(text))
    nodes, _, _ = _parse(tokens, 0, ctx.path, None)
    return _eval(nodes, ctx)


def make_ctx(edition: Edition, target: str, extra: tuple[str, ...] = (), path: str = "") -> Ctx:
    if target not in TARGET_FLAGS:
        raise CMError("E170", f"unknown target '{target}'", path)
    return Ctx(edition=edition, flags=frozenset({edition.id, target, *extra}), path=path)


def render(text: str, edition: Edition, target: str, extra: tuple[str, ...] = (), path: str = "") -> str:
    """Render prose or a template for one edition and target; strip section markers; NFC."""
    out = render_text(text, make_ctx(edition, target, extra, path))
    out = strip_markers(out)
    out = re.sub(r"\n{3,}", "\n\n", out)
    return finish(out)


def runtime_slots(text: str) -> set[str]:
    """Single-brace {slot} names (runtime placeholders the model fills)."""
    no_tags = TAG_RE.sub("", text)
    return set(re.findall(r"(?<!\{)\{([a-z_][a-z0-9_]*)\}(?!\})", no_tags))
