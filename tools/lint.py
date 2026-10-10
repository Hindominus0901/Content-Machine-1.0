#!/usr/bin/env python3
"""G1 deterministic lint (docs/BUILD.md §7).

    python3 tools/lint.py [--release] [--root PATH] [--json] [--today YYYY-MM-DD]

Source checks always run. Checks on built output read dist/ (written by
tools/build.py and tools/package.py); without dist/ they are skipped and a note
says which. Output is one line per finding ("E110 strings/vn.toml: key 'x'
missing") and a summary; --json prints a list of {code, path, message, level}
instead. Exit status is 1 when any E finding exists.

Warnings:
  W201  an artifact above 90% of its budget
  W202  a strings key that no template, prose file, config or tool uses
  W203  a module section that no target in core/method.toml selects
  W204  a release-only rule that will fail on --release (a stale verified_on)

Where docs/BUILD.md leaves a choice, this file decides:
  * The skill description is checked at source as strings key
    "skill.description" (rendered, per edition) and in dist/ as the SKILL.md
    front-matter description. Both are E102.
  * A strings value that is not NFC (NFD Vietnamese, say) is E111: src hashes
    and budgets are defined on NFC text, so such a value counts as stale. A
    prose section that is not NFC is E113.
  * E152: every zip in dist/ is extracted and re-zipped with package.make_zip
    (the build's own writer) in a temp folder; a different sha256 fails. A zip
    that breaks the contract outright (timestamps other than 1980-01-01 00:00,
    unsorted entries, machine-dependent permissions, timestamp extra fields)
    fails with that reason instead.
  * A source line ending in <!-- lint-ok:CODE[,CODE] --> is exempt from those
    codes, and so is its rendered copy in dist/. tools/lint_allow.toml lists
    accepted literals, paths and strings keys per code.
  * E132 does not apply to task-nudge* and task-connected* texts: they are short
    pointers that hand over to the project or the skill, where the card lives.
  * A missing dist/ or dist/<edition>/, and every target the build skipped, is
    E170 on --release and a note otherwise.
  * E161 also covers schemas/*.toml as a set: tools/cmschema.py checks their
    required keys and cross-references (a missing schema file is E161 too).
  * E110 also covers router and format-check text: a route or format used by a
    skill reference needs trigger_<id> / rules_<id> / checks_<id> for every
    non-EN edition, or render.py would fall back to the EN text there.
  * E152 fails closed: if tools/package.py cannot be imported, every zip is
    reported, because its determinism cannot be shown.
  * E148: a term from evals/personas/leak-terms.toml (a test persona's names,
    offer, coined phrases or story numbers) in a shipped kit source: a module or
    core section body, a strings value, or a file under plugin/. Without that
    file the check is skipped.
"""
from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import hashlib
import io
import json
import re
import struct
import sys
import tempfile
import tomllib
import zipfile
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cmlib  # noqa: E402
import cmschema  # noqa: E402
from cmlib import CMError, nfc, nfc_len, sha10  # noqa: E402

try:  # the build's deterministic zip writer, used to re-zip for E152
    import package as zip_writer  # noqa: E402
    ZIP_WRITER_ERROR = ""
except ImportError as exc:  # pragma: no cover - lint still runs, but E152 then fails closed
    zip_writer = None
    ZIP_WRITER_ERROR = repr(exc)

SOURCE_EDITION = "en"
SHIPPED_DIRS = ("core", "modules", "locales", "strings", "guides", "automation", "plugin")
TOML_DIRS = ("editions", "strings", "core", "schemas", "automation", "locales", "platform", "plugin")
TEXT_SUFFIXES = {".md", ".txt", ".toml", ".tmpl", ".html", ".htm", ".csv", ".json", ".ics",
                 ".css", ".js", ".svg", ".xml"}
LIST_FILES = ("deny-list.txt", "banned-tells.txt")
REQUIRED_EDITION_KEYS = ("id", "lang", "skill_name", "file_suffix", "zip_name")
EVIDENCE = ("DATA", "PRAC", "VERIFY")

CONTRACT_KEY = "contract.output"
DESCRIPTION_KEY = "skill.description"
CARD_MARKER = "SHIP CHECK"
CARDLESS_TASKS = ("task-nudge", "task-connected")
TASK_BUDGETS = (("task-nudge", "task_nudge"), ("task-standalone", "task_standalone"),
                ("task-connected", "task_connected"))

# Used when platform/targets.toml has no row (numbers from docs/BUILD.md §7 and PLAN P4).
DEFAULT_BUDGETS = {
    "skill_description": 190,
    "reference_lines": 150,
    "reference_bytes": 9216,
    "references_total_bytes": 204800,
    "references_per_job": 4,
}
SKILL_NAME_MAX = 64
SKILL_DESCRIPTION_HARD_MAX = 200
RESERVED_SKILL_WORDS = ("claude", "anthropic")
MAX_TRIGGER_CHARS = 200
MAX_RULES = 3
MAX_FORMAT_CHECKS = 5
HEAD_LINES = 10      # the output contract must sit within this many lines of the top...
TAIL_LINES = 4       # ...and of the bottom (non-blank lines, plus the contract's own)

MATT_GRAY_NAMES = ("Content Waterfall", "Content GPS", "4-3-2-1", "Authenticity Machine", "Founder OS")
FILL_WORDING = ("fill in", "fill out", "fill this", "fill-in", "điền vào", "điền thông tin")

DOS_EPOCH = (1980, 1, 1, 0, 0, 0)
FIXED_MODES = {0, 0o644, 0o755}
OS_LITTER = {"__MACOSX", ".DS_Store", "Thumbs.db", "desktop.ini"}
KEPT_DOT_NAMES = {".claude-plugin"}   # the manifest folder of a Claude plugin zip (tools/package.py)
FORBIDDEN_ZIP_DIRS = {"qa", "evals"}
TIME_EXTRA_FIELDS = {0x5455: "extended-timestamp", 0x000A: "NTFS-timestamp", 0x5855: "Info-ZIP Unix"}

WAIVER_RE = re.compile(r"[ \t]*<!--\s*lint-ok:\s*([A-Z0-9,\s]+?)\s*-->")
TAG_SPLIT_RE = re.compile(r"\{\{.*?\}\}")
VERDICT_RE = re.compile(r"\{\{\s*t:verdict\.")
STRING_TAG_RE = re.compile(r"\{\{\s*t:([a-z0-9_.-]+)\s*\}\}")
KEY_LITERAL_RE = re.compile(r"[\"']([a-z0-9_]+(?:\.[a-z0-9_-]+)+)[\"']")
HUB_REF_RE = re.compile(r"`hub:([^`\n]+)`")
CM_HEADING_RE = re.compile(r"^#{1,6}\s.*§CM-([A-Za-z0-9][A-Za-z0-9-]*)", re.M)
CM_REF_RE = re.compile(r"§CM-([A-Z0-9][A-Z0-9]*(?:-[A-Z0-9]+)*)")

# E147: a bare "bạn" in a VN coach-facing line. The coach picks a pair in reply 1 (anh/chị/bạn); fixed lines carry
# {xưng hô}/{tự xưng} slots, filled at run time. Scope: every strings/vn.toml value (minus buyer-facing keys, below)
# and every line of the instruction block and Ship Check (core/vn/*.md sections), quoted text, {…} slots and the
# pair notation ("mình–bạn", "bạn →") set aside; plus, anywhere in VN prose, the printed markers that leaked to
# coaches in the v13.4 demo: "[CẦN BẠN: …]", a raw "[anh/chị]" slot and the label "Bài bạn thích".
# "bạn bè", "kết bạn" are the word "friend", never flagged; "Bạn là {{name}}" speaks to the model.
# The leak markers are also checked (v13.7) in every strings/vn.toml value (buyer keys too: a missing fact in a CTA
# still prints to the coach) and in the surfaces outside the sections: plugin/agents/*.md, plugin/companions.toml
# and automation/* (scheduled-task prompts); an agent line that names the marker as a "never" example is waived.
VN_MARKER_SURFACES = ("plugin/agents/*.md", "plugin/companions.toml", "automation/*")
VN_ADDRESS_LANG = "vn"
VN_BUYER_KEYS = ("ask3.", "research.ask3", "cta.", "dm.", "series.", "talk.question")   # lines the coach sends to buyers
BARE_BAN_RE = re.compile(r"(?<!\w)bạn(?!\w)(?!\s*bè)", re.IGNORECASE)
BAN_PAIR_RE = re.compile(r"(?:mình|em|tôi|tớ)\s*[–—-]\s*bạn|bạn\s*[–—-]\s*(?:mình|em)|bạn\s*→|kết\s+bạn"
                         r"|bạn\s+là\s+\{\{\s*name\s*\}\}", re.IGNORECASE)
QUOTED_RE = re.compile(r'"[^"\n]*"|“[^”\n]*”|«[^»\n]*»|\{\{.*?\}\}|\{[^{}\n]*\}')
VN_LEAK_MARKERS = (
    ("needs tag", re.compile(r"\[\s*CẦN\s+BẠN\b", re.IGNORECASE)),
    ("raw slot", re.compile(r"\[(?:anh|chị)\s*/\s*(?:anh|chị|em|bạn)(?:\s*/\s*\w+)?\]", re.IGNORECASE)),
    ("label", re.compile(r"Bài\s+bạn\s+thích", re.IGNORECASE)),
)


def bare_ban(line: str) -> list[str]:
    """Bare "bạn" left in a VN coach-facing line once quotes, slots and pair notation are set aside."""
    body = QUOTED_RE.sub(" ", BAN_PAIR_RE.sub(" ", nfc(line)))
    return [m.group(0) for m in BARE_BAN_RE.finditer(body)]


# E148: kit examples must not be built from a test persona's own facts (COMPARE v13.7, new defect 1): the demo can no
# longer tell thinking from copying. The curated list lives with the fixtures; see its header.
LEAK_TERMS_FILE = "evals/personas/leak-terms.toml"


def leak_term_re(term: str) -> re.Pattern:
    term = nfc(term).strip()
    head = r"(?<!\w)" if term[:1].isalnum() else ""
    tail = r"(?!\w)" if term[-1:].isalnum() else ""
    return re.compile(head + re.escape(term) + tail, re.IGNORECASE)


def load_leak_terms(root: Path) -> list[tuple[str, str, re.Pattern]]:
    """(persona, term, regex) for every term in evals/personas/leak-terms.toml; [] when the file is absent."""
    path = Path(root) / LEAK_TERMS_FILE
    if not path.is_file():
        return []
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    return [(persona, term, leak_term_re(term)) for persona, block in sorted(data.items())
            for term in [*block.get("terms", []), *block.get("echoes", [])]]


PII_RULES = (
    ("email", re.compile(r"(?<![\w.%+-])[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}\b")),
    ("phone number", re.compile(r"(?<![\w+])(?:\+|00)84[\s.-]?\(?\d\)?(?:[\s.-]?\d){7,9}(?!\d)")),
    ("phone number", re.compile(r"(?<![\w+.,/])0[1-9](?:[\s.-]?\d){8,9}(?!\d)")),
    ("phone number", re.compile(r"(?<![\w+])\+\d{1,3}[\s.-]?\(?\d{1,4}\)?(?:[\s.-]?\d{2,4}){2,4}(?!\d)")),
    ("phone number", re.compile(r"(?<![\w+])\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}(?!\d)")),
    ("@handle", re.compile(r"(?<![\w@./])@([A-Za-z0-9_](?:[A-Za-z0-9_.]*[A-Za-z0-9_])?)")),
)
# CSS at-rules and our own section markers look like handles.
NOT_HANDLES = {"section", "media", "import", "keyframes", "font", "page", "supports", "charset",
               "namespace", "layer", "container", "property", "counter"}
EXAMPLE_EMAIL_RE = re.compile(r"@(?:[\w-]+\.)*(?:example\.(?:com|org|net)|[\w-]+\.(?:example|test|invalid))$", re.I)

MONTHS = (r"(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?"
          r"|sep(?:t(?:ember)?)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)")
UNIT_AFTER_YEAR = (r"(?:chars?|characters?|bytes?|words?|ký tự|từ|chữ|đồng|vnđ|vnd|usd|views?|followers?"
                   r"|người|lượt)\b|[₫$%đ]")
DATE_RULES = (
    ("ISO date", re.compile(r"(?<!\d)(?:19|20)\d{2}[-/.](?:0?[1-9]|1[0-2])[-/.](?:0?[1-9]|[12]\d|3[01])(?!\d)")),
    ("date", re.compile(r"(?<![\d/])(?:0?[1-9]|[12]\d|3[01])/(?:0?[1-9]|1[0-2])/(?:19|20)\d{2}(?!\d)")),
    ("date", re.compile(rf"\b{MONTHS}\.?\s+(?:\d{{1,2}}(?:st|nd|rd|th)?,?\s+)?(?:19|20)\d{{2}}\b", re.I)),
    ("date", re.compile(rf"\b\d{{1,2}}(?:st|nd|rd|th)?\s+{MONTHS}\.?,?\s+(?:19|20)\d{{2}}\b", re.I)),
    ("date", re.compile(r"(?<!\w)tháng\s+\d{1,2}\s*(?:/|năm)\s*(?:19|20)\d{2}(?!\d)", re.I)),
    ("date", re.compile(r"(?<!\w)ngày\s+\d{1,2}\s*(?:/|tháng)\s*\d{1,2}(?!\d)", re.I)),
    ("year", re.compile(rf"(?<![\w.,:/+-])20\d{{2}}(?![\w%]|[.,:/]\d)(?!\s*(?:{UNIT_AFTER_YEAR}))", re.I)),
    ("time word", re.compile(r"(?<!\w)(?:currently|as of|hiện nay|hiện tại)(?!\w)", re.I)),
)

DESCRIBE = {
    "E140": lambda label, hit: f"coach-visible jargon '{hit}' (deny-list)",
    "E141": lambda label, hit: f"AI tell or calque '{hit}'",
    "E142": lambda label, hit: f"Matt Gray framework name '{hit}'",
    "E143": lambda label, hit: f"template-fill wording '{hit}'",
    "E144": lambda label, hit: f"possible PII ({label}) '{hit}'",
    "E145": lambda label, hit: f"{label} '{hit}' outside locales/<lang>/platform-notes.md",
}


# ---------------------------------------------------------------- findings

@dataclass(frozen=True)
class Finding:
    code: str
    path: str
    message: str
    level: str = "error"

    def __str__(self) -> str:
        return f"{self.code} {self.path}: {self.message}"

    def as_dict(self) -> dict:
        return {"code": self.code, "path": self.path, "message": self.message, "level": self.level}


@dataclass
class Report:
    findings: list[Finding]
    notes: list[str]
    release: bool = False

    @property
    def errors(self) -> list[Finding]:
        return [f for f in self.findings if f.level == "error"]

    @property
    def warnings(self) -> list[Finding]:
        return [f for f in self.findings if f.level == "warning"]

    def codes(self, level: str = "error") -> set[str]:
        return {f.code for f in self.findings if f.level == level}

    def summary(self) -> str:
        def part(items: list[Finding], noun: str) -> str:
            counts = Counter(f.code for f in items)
            detail = ", ".join(f"{c} ×{n}" for c, n in sorted(counts.items()))
            plural = noun if len(items) == 1 else noun + "s"
            return f"{len(items)} {plural}" + (f" ({detail})" if detail else "")
        mode = "release" if self.release else "dev"
        return f"lint ({mode}): {part(self.errors, 'error')}, {part(self.warnings, 'warning')}"


# ---------------------------------------------------------------- small helpers

def front_matter_fields(text: str) -> dict[str, str]:
    """name, description and any other `key: value` line of a SKILL.md or agent front matter (a quoted JSON value is
    unquoted)."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    out: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return out
        key, sep, value = line.partition(":")
        if sep:
            value = value.strip()
            if value.startswith('"'):
                try:
                    value = json.loads(value)
                except json.JSONDecodeError:
                    pass
            out[key.strip()] = value
    return {}


def method_table(method: dict, table: str):
    """core/method.toml table by dotted name: "method", "skill", "levelup.research". {} when missing."""
    cur: object = method
    for part in table.split("."):
        cur = cur.get(part, {}) if isinstance(cur, dict) else {}
    return cur


def norm(text: str) -> str:
    return " ".join(nfc(text).split())


def count_lines(text: str) -> int:
    """Lines as build.py counts them (a final line without a newline still counts)."""
    return text.count("\n") + (1 if text and not text.endswith("\n") else 0)


def parse_date(value) -> dt.date | None:
    if isinstance(value, dt.datetime):
        return value.date()
    if isinstance(value, dt.date):
        return value
    if isinstance(value, str):
        try:
            return dt.date.fromisoformat(value.strip())
        except ValueError:
            return None
    return None


def phrase_regex(phrase: str, flags: int = re.IGNORECASE) -> re.Pattern:
    """A whole-word, whitespace-tolerant regex for a literal phrase ('…' ≡ '…')."""
    words = nfc(phrase).split()
    body = r"\s+".join("".join("['’]" if c in "'’" else re.escape(c) for c in w) for w in words)
    left = r"(?<!\w)" if (words[0][0].isalnum() or words[0][0] == "_") else ""
    right = r"(?!\w)" if (words[-1][-1].isalnum() or words[-1][-1] == "_") else ""
    return re.compile(left + body + right, flags)


def waived(line: str, code: str) -> bool:
    return any(code in m.group(1).replace(" ", "").split(",") for m in WAIVER_RE.finditer(line))


def line_pattern(line: str) -> re.Pattern | None:
    """A regex for how a source line renders: template tags become wildcards."""
    line = cmlib.SECTION_RE.sub("", WAIVER_RE.sub("", line))
    pieces = [p.split() for p in TAG_SPLIT_RE.split(line)]
    if sum(len("".join(p)) for p in pieces) < 8:
        return None
    return re.compile(".*?".join(r"\s+".join(map(re.escape, p)) for p in pieces))


def frontmatter(text: str) -> dict[str, str] | None:
    """`key: value` pairs between the leading '---' lines (quoted and folded values too)."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    out: dict[str, str] = {}
    key = None
    for line in lines[1:]:
        if line.strip() == "---":
            return out
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m and not line[:1].isspace():
            key, value = m.group(1), m.group(2).strip()
            if value in (">", "|", ">-", "|-"):
                value = ""
            elif len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            out[key] = value
        elif key and line[:1].isspace():
            out[key] = (out[key] + " " + line.strip()).strip()
    return None


def extra_field_ids(extra: bytes) -> list[int]:
    ids, i = [], 0
    while i + 4 <= len(extra):
        header_id, size = struct.unpack("<HH", extra[i:i + 4])
        ids.append(header_id)
        i += 4 + size
    return ids


def iter_strings(node):
    """Every string value in a parsed TOML tree."""
    if isinstance(node, str):
        yield node
    elif isinstance(node, dict):
        for v in node.values():
            yield from iter_strings(v)
    elif isinstance(node, list):
        for v in node:
            yield from iter_strings(v)


def _selector_matches(selector: str, sections: dict) -> bool:
    """True when a method.toml selector (exact id or prefix*) matches a section."""
    if selector.endswith("*"):
        return any(sid.startswith(selector[:-1]) for sid in sections)
    return selector in sections


def natural_key(text: str):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", text)]


def template_problems(text: str, edition: cmlib.Edition) -> list[tuple[str, str | None]]:
    """Every render error in text for this edition, on both sides of each {{#if}}.

    render() only evaluates the branch it takes, so this walks the parse tree
    instead. Returns (message, needle) pairs; needle locates the line.
    """
    try:
        nodes, _, _ = cmlib._parse(list(cmlib._tokenize(text)), 0, "", None)
    except CMError as exc:
        return [(exc.message, None)]
    known = set(cmlib.EDITIONS) | set(cmlib.TARGET_FLAGS) | set(cmlib.EXTRA_FLAGS)
    out: list[tuple[str, str | None]] = []

    def walk(nodes: list) -> None:
        for node in nodes:
            if node[0] == "var":
                name = node[1]
                if name.startswith(">"):
                    sid = name[1:].strip()
                    try:
                        known_ids = edition.sections()
                    except CMError as exc:
                        out.append((exc.message, sid))
                        continue
                    if sid not in known_ids:
                        out.append((f"unknown section '{sid}' in include", sid))
                elif name.startswith("t:"):
                    key = name[2:].strip()
                    if not cmlib.KEY_RE.match(key):
                        out.append((f"bad string key '{key}'", key))
                    elif key not in edition.strings:
                        out.append((f"unknown string key '{key}'", key))
                elif not cmlib.NAME_RE.match(name):
                    out.append((f"bad tag '{{{{{name}}}}}'", name))
                else:
                    try:
                        value = edition.lookup(name)
                    except KeyError:
                        out.append((f"unknown param '{name}'", name))
                        continue
                    if isinstance(value, (dict, list)):
                        out.append((f"param '{name}' is not a scalar", name))
            elif node[0] in ("if", "unless"):
                names = [c.strip() for c in node[1].split(",") if c.strip()]
                if not names:
                    out.append(("empty {{#if}} condition", None))
                out.extend((f"unknown flag '{n}'", n) for n in names if n not in known)
                walk(node[2])
                walk(node[3])

    walk(nodes)
    return out


# ---------------------------------------------------------------- the linter

class Linter:
    def __init__(self, root: Path, release: bool = False, today: dt.date | None = None):
        self.root = Path(root).resolve()
        self.release = release
        self.today = today or dt.date.today()
        self.notes: list[str] = []
        self._found: dict[tuple[str, str, str], Finding] = {}
        self._text: dict[Path, str] = {}
        self.toml: dict[str, dict | None] = {}
        self.editions: dict[str, cmlib.Edition] = {}
        self.strings: dict[str, tuple[dict[str, str], dict[str, str]]] = {}
        self.sections: dict[str, dict[str, cmlib.Section]] = {}
        self.section_where: dict[tuple[str, str], str] = {}
        self.targets: dict = {}
        self.allow: dict[str, dict] = {}
        self.terms: dict[tuple[str, str], list[tuple[str, re.Pattern]]] = {}
        self.seen_lines: dict[str, list[re.Pattern]] = defaultdict(list)
        self._cards: dict[tuple[str, bool], list[str]] = {}

    # -- plumbing

    @property
    def findings(self) -> list[Finding]:
        return list(self._found.values())

    def add(self, code: str, path: str, message: str, level: str | None = None) -> None:
        level = level or ("warning" if code.startswith("W") else "error")
        self._found.setdefault((code, str(path), message), Finding(code, str(path), message, level))

    def note(self, text: str) -> None:
        if text not in self.notes:
            self.notes.append(text)

    def rel(self, path: Path) -> str:
        try:
            return Path(path).resolve().relative_to(self.root).as_posix()
        except ValueError:
            return str(path)

    def text(self, path: Path) -> str:
        path = Path(path)
        if path not in self._text:
            data = path.read_bytes()
            try:
                self._text[path] = data.decode("utf-8")
            except UnicodeDecodeError:
                self.add("E170", self.rel(path), "not valid UTF-8")
                self._text[path] = data.decode("utf-8", errors="replace")
        return self._text[path]

    def files_under(self, *dirs: str, suffixes=TEXT_SUFFIXES) -> list[Path]:
        out: list[Path] = []
        for d in dirs:
            base = self.root / d
            if not base.is_dir():
                continue
            for p in sorted(base.rglob("*")):
                parts = p.relative_to(self.root).parts
                if p.is_file() and p.suffix.lower() in suffixes and not any(x.startswith(".") for x in parts):
                    out.append(p)
        return out

    def source_files(self) -> list[Path]:
        """Shipped source text, minus the lint word lists themselves."""
        return [p for p in self.files_under(*SHIPPED_DIRS)
                if not (p.name in LIST_FILES and self.rel(p).startswith("locales/"))]

    def shipped(self, path: Path) -> tuple[str, int]:
        """The part of a source file that ships and the line it starts on.

        render.render_file drops the maintainer preamble before the first
        @section marker, so word rules and template checks skip it too.
        """
        text = self.text(path)
        preamble, secs = cmlib.parse_sections(text)
        if secs:
            return text[len(preamble):], preamble.count("\n") + 1
        return text, 1

    def parse_toml(self, path: Path) -> dict | None:
        try:
            return tomllib.loads(path.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            self.add("E161", self.rel(path), "not valid UTF-8")
        except tomllib.TOMLDecodeError as exc:
            self.add("E161", self.rel(path), f"bad TOML: {exc}")
        return None

    def target_row(self, table: str, name: str) -> dict:
        rows = self.targets.get(table)
        row = rows.get(name) if isinstance(rows, dict) else None
        return row if isinstance(row, dict) else {}

    def budget(self, name: str, edition_id: str) -> int | None:
        value = self.target_row("budgets", name).get(edition_id)
        if isinstance(value, int) and not isinstance(value, bool) and value > 0:
            return value
        return DEFAULT_BUDGETS.get(name)

    def limit_value(self, name: str, default: int) -> int:
        value = self.target_row("limits", name).get("value")
        return value if isinstance(value, int) and not isinstance(value, bool) and value > 0 else default

    def check_budget(self, name: str, edition_id: str, used: int, where: str, what: str, unit: str,
                     code: str = "E101") -> None:
        limit = self.budget(name, edition_id)
        if not limit:
            return
        pct = round(used * 100 / limit, 1)
        if used > limit:
            self.add(code, where, f"{what} is {used:,} {unit}, over the {limit:,} budget ({pct}%, {name})")
        elif used * 10 > limit * 9:
            self.add("W201", where, f"{what} is {used:,} {unit}, {pct}% of the {limit:,} budget ({name})")

    def allowed(self, code: str, path: str, hit: str, key: str | None = None) -> bool:
        if code == "E144" and EXAMPLE_EMAIL_RE.search(hit):
            return True
        entry = self.allow.get(code)
        if not entry:
            return False
        if nfc(hit).casefold() in entry["allow"]:
            return True
        if key is not None and key in entry["keys"]:
            return True
        return any(fnmatch.fnmatch(path, pat) for pat in entry["paths"])

    def source_lang(self) -> str:
        ed = self.editions.get(SOURCE_EDITION)
        return ed.cfg.get("method_prose", ed.lang) if ed else SOURCE_EDITION

    def prose_langs(self) -> list[str]:
        langs = [self.source_lang()]
        for ed in self.editions.values():
            for lang in (ed.cfg.get("method_prose", ed.lang), ed.lang):
                if lang not in langs:
                    langs.append(lang)
        if not self.editions:
            langs += [e for e in cmlib.EDITIONS if e not in langs]
        return langs

    def lang_of(self, edition_id: str) -> str:
        ed = self.editions.get(edition_id)
        return ed.lang if ed else edition_id

    def render_prose(self, path: Path, edition: cmlib.Edition, target: str) -> str:
        """The file as it ships (preamble dropped, markers stripped); raw text on render errors."""
        text = self.text(path)
        preamble, secs = cmlib.parse_sections(text)
        if secs:
            text = text[len(preamble):]
        try:
            return cmlib.render(text, edition, target)
        except CMError:
            return cmlib.strip_markers(text)

    def contract(self, edition: cmlib.Edition, target: str) -> str | None:
        raw = edition.strings.get(CONTRACT_KEY)
        if raw is None:
            return None
        try:
            return cmlib.render(raw, edition, target).strip()
        except CMError:
            return nfc(raw).strip()

    # -- run

    def run(self) -> Report:
        steps = [
            self.load_allowlist, self.load_toml_files, self.load_editions, self.load_strings,
            self.load_terms, self.check_strings, self.check_sections, self.check_pending,
            self.check_targets, self.check_schemas, self.check_router, self.check_templates, self.check_hub_refs,
            self.check_source_text, self.check_vn_address, self.check_leak_terms, self.check_cards, self.check_tasks_data, self.check_levelup_sections,
            self.check_dist, self.check_unused,
        ]
        for step in steps:
            try:
                step()
            except Exception as exc:  # keep the gate running; report the crash as a finding
                self.add("E170", "tools/lint.py", f"lint step {step.__name__} failed: {exc!r}")
        findings = sorted(self._found.values(), key=lambda f: (f.code, natural_key(f.path), f.message))
        return Report(findings, self.notes, self.release)

    # -- loading

    def load_allowlist(self) -> None:
        path = self.root / "tools" / "lint_allow.toml"
        if not path.exists():
            return
        data = self.parse_toml(path) or {}
        where = self.rel(path)
        for code, table in data.items():
            if not isinstance(table, dict):
                self.add("E161", where, f"[{code}] must be a table with allow/paths/keys lists")
                continue
            entry = {}
            for k in ("allow", "paths", "keys"):
                value = table.get(k, [])
                if not isinstance(value, list) or not all(isinstance(x, str) for x in value):
                    self.add("E161", where, f"[{code}] {k} must be a list of strings")
                    value = []
                entry[k] = value
            entry["allow"] = {nfc(x).casefold() for x in entry["allow"]}
            self.allow[code] = entry

    def load_toml_files(self) -> None:
        for p in self.files_under(*TOML_DIRS, suffixes={".toml"}):
            self.toml[self.rel(p)] = self.parse_toml(p)
        self.targets = self.toml.get("platform/targets.toml") or {}

    def load_editions(self) -> None:
        ids = sorted(k[len("editions/"):-len(".toml")] for k in self.toml
                     if k.startswith("editions/") and k.count("/") == 1 and k.count(".") == 1)
        if not ids:
            self.add("E161", "editions", "no editions/<id>.toml found")
        for ed_id in ids:
            path = f"editions/{ed_id}.toml"
            data = self.toml[path]
            if data is None:
                continue
            cfg = data.get("edition")
            if not isinstance(cfg, dict):
                self.add("E161", path, "missing [edition] table")
                continue
            missing = [k for k in REQUIRED_EDITION_KEYS if not isinstance(cfg.get(k), str) or not cfg[k]]
            if missing:
                self.add("E161", path, f"[edition] missing {', '.join(missing)}")
                continue
            if cfg["id"] != ed_id:
                self.add("E161", path, f"[edition] id '{cfg['id']}' does not match the file name")
            if ed_id not in cmlib.EDITIONS:
                self.add("E161", path, f"unknown edition id '{ed_id}' (expected {', '.join(cmlib.EDITIONS)})")
            for table in ("params", "pending"):
                if not isinstance(data.get(table, {}), dict):
                    self.add("E161", path, f"[{table}] must be a table")
            for key, spec in (data.get("pending") or {}).items():
                if not isinstance(spec, dict) or "default" not in spec:
                    self.add("E161", path, f"[pending] {key} needs {{ default = ..., reason = \"...\" }}")
            self.check_skill_name(cfg["skill_name"], path, "skill_name")
            params = data.get("params") if isinstance(data.get("params"), dict) else {}
            pending = data.get("pending") if isinstance(data.get("pending"), dict) else {}
            self.editions[ed_id] = cmlib.Edition(id=ed_id, lang=cfg["lang"], cfg=cfg, params=params,
                                                 pending=pending, strings={}, string_src={})

    def load_strings(self) -> None:
        files = {k[len("strings/"):-len(".toml")] for k in self.toml
                 if k.startswith("strings/") and k.count("/") == 1}
        for sid in sorted(files):
            path = f"strings/{sid}.toml"
            data = self.toml[path]
            if data is None:
                continue
            table = data.get("strings")
            if not isinstance(table, dict):
                self.add("E161", path, "missing [strings] table")
                continue
            for key, value in table.items():
                if not cmlib.KEY_RE.match(key):
                    self.add("E161", path, f"key '{key}' is not a valid strings key ([a-z0-9_.-])")
                text = value.get("text") if isinstance(value, dict) else value
                if not isinstance(text, str):
                    self.add("E161", path, f"key '{key}' needs a text string")
            texts, srcs = cmlib.load_strings(sid, self.root)
            texts = {k: v for k, v in texts.items() if isinstance(v, str)}
            self.strings[sid] = (texts, srcs)
            if sid in self.editions:
                self.editions[sid].strings = texts
                self.editions[sid].string_src = srcs

    def load_terms(self) -> None:
        base = self.root / "locales"
        langs = {ed.lang for ed in self.editions.values()} | {self.lang_of(s) for s in self.strings}
        dirs = {p.name for p in base.iterdir() if p.is_dir()} if base.is_dir() else set()
        for lang in sorted(langs | dirs):
            for kind, name, code in (("deny", "deny-list.txt", "E140"), ("tells", "banned-tells.txt", "E141")):
                path = base / lang / name
                if path.exists():
                    self.terms[(kind, lang)] = self.parse_terms(path)
                elif lang in langs:
                    self.note(f"locales/{lang}/{name} missing; {code} not checked for {lang}")

    def parse_terms(self, path: Path) -> list[tuple[str, re.Pattern]]:
        """One entry per line; '#' comments; 're:' entries are case-sensitive regexes."""
        terms: list[tuple[str, re.Pattern]] = []
        for lineno, raw in enumerate(self.text(path).splitlines(), 1):
            entry = raw.strip()
            if not entry or entry.startswith("#"):
                continue
            if entry.startswith("re:"):
                try:
                    rx = re.compile(nfc(entry[3:].strip()))
                except re.error as exc:
                    self.add("E161", f"{self.rel(path)}:{lineno}", f"bad regex: {exc}")
                    continue
            else:
                rx = phrase_regex(entry)
            terms.append((entry, rx))
        return terms

    def terms_for(self, kind: str, lang: str | None) -> list[tuple[str, re.Pattern]]:
        if lang is not None:
            return self.terms.get((kind, lang), [])
        return [t for (k, _), items in sorted(self.terms.items()) if k == kind for t in items]

    # -- strings (E110-E112, E102 description)

    def check_strings(self) -> None:
        src_texts = self.strings.get(SOURCE_EDITION, ({}, {}))[0]
        for sid, (texts, srcs) in sorted(self.strings.items()):
            path = f"strings/{sid}.toml"
            for key, text in texts.items():
                if text != nfc(text):
                    self.add("E111", path, f"key '{key}': text is not NFC (e.g. NFD Vietnamese); "
                                           "src hashes and budgets use NFC, so it counts as stale")
            if sid == SOURCE_EDITION:
                continue
            for key in sorted(src_texts.keys() - texts.keys()):
                self.add("E110", path, f"key '{key}' missing")
            for key in sorted(texts.keys() - src_texts.keys()):
                self.add("E110", path, f"key '{key}' has no EN source")
            for key in sorted(src_texts.keys() & texts.keys()):
                want, got = sha10(src_texts[key]), srcs.get(key)
                if got is None:
                    self.add("E111", path, f"key '{key}' has no src hash (EN text hashes to {want})")
                elif got != want:
                    self.add("E111", path, f"key '{key}' is stale: src {got}, EN text now hashes to {want}")
                a, b = cmlib.runtime_slots(src_texts[key]), cmlib.runtime_slots(texts[key])
                if a != b:
                    self.add("E112", path, f"key '{key}': placeholders differ "
                                           f"(EN {sorted(a)}, {sid.upper()} {sorted(b)})")
        for ed_id, ed in sorted(self.editions.items()):
            if src_texts and ed_id != SOURCE_EDITION and f"strings/{ed_id}.toml" not in self.toml:
                self.add("E110", f"strings/{ed_id}.toml", f"file missing; {len(src_texts)} EN keys have no text")
            raw = ed.strings.get(DESCRIPTION_KEY)
            if raw is not None:
                try:
                    desc = cmlib.render(raw, ed, "skill").strip()
                except CMError:
                    desc = nfc(raw).strip()
                self.check_description(desc, ed_id, f"strings/{ed_id}.toml", f"key '{DESCRIPTION_KEY}'")

    def check_skill_name(self, name: str, where: str, label: str = "skill name") -> None:
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            self.add("E102", where, f"{label} '{name}' must be lowercase letters, digits and single hyphens")
        limit = self.limit_value("claude_skill_name_max", SKILL_NAME_MAX)
        if len(name) > limit:
            self.add("E102", where, f"{label} '{name}' is {len(name)} characters (max {limit})")
        for word in RESERVED_SKILL_WORDS:
            if word in name.lower():
                self.add("E102", where, f"{label} '{name}' contains the reserved word '{word}'")

    def check_description(self, desc: str, edition_id: str, where: str, label: str) -> None:
        if not desc:
            self.add("E102", where, f"{label} is empty")
            return
        hard = self.limit_value("claude_skill_description_max", SKILL_DESCRIPTION_HARD_MAX)
        limit = self.budget("skill_description", edition_id)
        n = nfc_len(desc)
        if n > limit:
            self.add("E102", where, f"{label} is {n} characters, over the {limit} budget "
                                    f"(claude.ai rejects over {hard})")
        elif n * 10 > limit * 9:
            self.add("W201", where, f"{label} is {n} characters, {round(n * 100 / limit, 1)}% of the {limit} budget")
        if "<" in desc or ">" in desc:
            self.add("E102", where, f"{label} contains '<' or '>'")

    # -- sections (E113, E114, E146)

    def check_sections(self) -> None:
        for lang in self.prose_langs():
            found: dict[str, cmlib.Section] = {}
            for path in cmlib.prose_files(lang, self.root):
                relp, text = self.rel(path), self.text(path)
                for lineno, line in enumerate(text.splitlines(), 1):
                    if "@section" in line and not cmlib.SECTION_RE.match(line):
                        self.add("E170", f"{relp}:{lineno}", "malformed @section marker (it would ship as text)")
                markers = list(cmlib.SECTION_RE.finditer(text))
                _, secs = cmlib.parse_sections(text, relp)
                for m, sec in zip(markers, secs):
                    where = f"{relp}:{text.count(chr(10), 0, m.start()) + 1}"
                    if sec.id in found:
                        self.add("E114", where, f"duplicate section id '{sec.id}' (first in {found[sec.id].file})")
                        continue
                    found[sec.id] = sec
                    self.section_where[(lang, sec.id)] = where
                    if sec.attrs.get("kind") == "script" and not VERDICT_RE.search(sec.body):
                        self.add("E146", where,
                                 f"script section '{sec.id}' prints no verdict line ({{{{t:verdict.…}}}})")
                    if sec.body != nfc(sec.body):
                        self.add("E113", where, f"section '{sec.id}' is not NFC")
            self.sections[lang] = found

        src_lang = self.source_lang()
        source = self.sections.get(src_lang, {})
        for lang, secs in self.sections.items():
            if lang == src_lang:
                continue
            for sid, sec in source.items():
                twin = secs.get(sid)
                if twin is None:
                    guess = sec.file.replace(f"/{src_lang}/", f"/{lang}/", 1)
                    if not self.release and not (self.root / guess).exists():
                        # The whole file is not ported yet: a note in dev, an error with --release.
                        # A twin file that exists but lacks a section is always an error.
                        self.note(f"{guess} not written yet ({lang.upper()} port of {sec.file})")
                        continue
                    self.add("E113", guess, f"section '{sid}' has no {lang.upper()} twin (EN: {sec.file})")
                    continue
                want, got = sha10(sec.body), twin.attrs.get("src")
                where = self.section_where[(lang, sid)]
                if got is None:
                    self.add("E113", where, f"section '{sid}' has no src (EN body hashes to {want})")
                elif got != want:
                    self.add("E113", where, f"section '{sid}' is stale: src {got}, EN body now hashes to {want}")
            for sid in sorted(secs.keys() - source.keys()):
                self.add("E113", self.section_where[(lang, sid)], f"section '{sid}' has no EN source (orphan)")

    # -- PENDING_VN (E120)

    def check_pending(self) -> None:
        for ed_id, ed in sorted(self.editions.items()):
            if not ed.pending:
                continue
            acc_path = f"editions/{ed_id}.acceptance.toml"
            accepted = (self.toml.get(acc_path) or {}).get("accepted", {})
            if not isinstance(accepted, dict):
                self.add("E161", acc_path, "[accepted] must hold one table per key")
                accepted = {}
            unsigned: list[tuple[str, str]] = []
            for key, spec in ed.pending.items():
                row = accepted.get(key)
                if not isinstance(row, dict):
                    problem = f"has no signed row in {acc_path}"
                elif not str(row.get("signed_by", "")).strip():
                    problem = "has no signed_by"
                elif parse_date(row.get("date")) is None:
                    problem = "has no valid date (YYYY-MM-DD)"
                elif isinstance(spec, dict) and "default" in spec and row.get("default") != spec["default"]:
                    problem = "was signed for a different default; re-sign the current one"
                else:
                    continue
                unsigned.append((key, problem))
            if self.release:
                for key, problem in unsigned:
                    self.add("E120", acc_path, f"PENDING key '{key}' {problem}")
            elif unsigned:
                self.note(f"{len(unsigned)} PENDING key(s) in editions/{ed_id}.toml not signed yet "
                          f"(E120 on --release)")

    # -- platform/targets.toml (E121, E122, E161)

    def check_targets(self) -> None:
        path = "platform/targets.toml"
        if path not in self.toml:
            self.add("E161", path, "file not found")
            return
        data = self.toml[path]
        if data is None:
            return
        meta = data.get("meta")
        max_age = meta.get("max_age_days") if isinstance(meta, dict) else None
        if not isinstance(max_age, int) or isinstance(max_age, bool) or max_age <= 0:
            self.add("E161", path, "[meta] max_age_days must be a positive integer")
            max_age = None
        limits = data.get("limits", {})
        budgets = data.get("budgets", {})
        if not isinstance(limits, dict) or not isinstance(budgets, dict):
            self.add("E161", path, "[limits] and [budgets] must be tables")
            return
        used_by: dict[str, list[str]] = defaultdict(list)
        for bid, row in budgets.items():
            if not isinstance(row, dict):
                self.add("E161", path, f"[budgets.{bid}] must be a table")
                continue
            for k in ("artifact", "unit", "limit"):
                if k not in row:
                    self.add("E161", path, f"[budgets.{bid}] missing '{k}'")
            for ed_id in self.editions:
                value = row.get(ed_id)
                if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
                    self.add("E161", path, f"[budgets.{bid}] needs a positive integer '{ed_id}'")
            ref = row.get("limit")
            if ref:
                if ref not in limits:
                    self.add("E161", path, f"[budgets.{bid}] names unknown limit '{ref}'")
                used_by[ref].append(bid)

        verify_blocking = 0
        for name, row in limits.items():
            if not isinstance(row, dict):
                self.add("E161", path, f"[limits.{name}] must be a table")
                continue
            missing = [k for k in ("value", "unit", "evidence", "verified_on", "source") if k not in row]
            if missing:
                self.add("E161", path, f"[limits.{name}] missing {', '.join(missing)}")
            evidence = row.get("evidence")
            if evidence not in EVIDENCE:
                self.add("E161", path, f"[limits.{name}] evidence must be one of {', '.join(EVIDENCE)}")
                continue
            raw = row.get("verified_on", "")
            date = parse_date(raw)
            blank = raw in ("", None)
            if evidence == "VERIFY":
                if not blank:
                    self.add("E122", path, f"limit '{name}' is VERIFY but carries verified_on {raw}")
                reasons = (["release_blocking"] if row.get("release_blocking") else []) + \
                          [f"budget {b}" for b in used_by.get(name, [])]
                if reasons:
                    verify_blocking += 1
                    if self.release:
                        self.add("E121", path, f"limit '{name}' is still VERIFY ({', '.join(reasons)})")
                continue
            if blank:
                self.add("E122", path, f"limit '{name}' is {evidence} but has no verified_on date")
            elif date is None:
                self.add("E122", path, f"limit '{name}' verified_on '{raw}' is not a YYYY-MM-DD date")
            elif date > self.today:
                self.add("E122", path, f"limit '{name}' verified_on {date} is in the future")
            elif max_age and (self.today - date).days > max_age:
                age = (self.today - date).days
                msg = f"limit '{name}' verified_on {date} is {age} days old (max {max_age}); re-verify it"
                self.add("E121" if self.release else "W204", path, msg)
        if verify_blocking and not self.release:
            self.note(f"{verify_blocking} release-blocking limit(s) in {path} still VERIFY (E121 on --release)")

    # -- router and method map (E130, E103, E161, E170)

    def references_per_job(self) -> int:
        values = [v for v in (self.budget("references_per_job", e) for e in self.editions) if v]
        return min(values) if values else DEFAULT_BUDGETS["references_per_job"]

    def check_router(self) -> None:
        method = self.toml.get("core/method.toml")
        router = self.toml.get("core/router.toml")
        formats = self.toml.get("core/format-checks.toml")
        refs: list[dict] = []
        if method:
            self.check_method_table(method, "method", "anchor")
            self.check_levelup_tables(method)
            refs = self.check_method_table(method, "skill", "reference")

        fmt_table = (formats or {}).get("format", {})
        if not isinstance(fmt_table, dict):
            self.add("E161", "core/format-checks.toml", "[format.<id>] tables expected")
            fmt_table = {}
        for fid, row in fmt_table.items():
            for k, v in (row.items() if isinstance(row, dict) else []):
                if k == "checks" or k.startswith("checks_"):
                    if not isinstance(v, list) or len(v) > MAX_FORMAT_CHECKS:
                        self.add("E161", "core/format-checks.toml",
                                 f"[format.{fid}] {k} must be a list of at most {MAX_FORMAT_CHECKS} yes/no lines")

        routes: list[dict] = []
        if router is not None:
            routes = router.get("route", [])
            if not isinstance(routes, list) or not all(isinstance(r, dict) for r in routes):
                self.add("E161", "core/router.toml", "routes must be [[route]] tables")
                routes = []
        ref_files = {r["file"] for r in refs}
        per_job = self.references_per_job()
        ids: set[str] = set()
        for r in routes:
            rid = r.get("id", "?")
            missing = [k for k in ("id", "module", "trigger", "loads") if k not in r]
            if missing:
                self.add("E161", "core/router.toml", f"route '{rid}' missing {', '.join(missing)}")
            if rid in ids:
                self.add("E130", "core/router.toml", f"duplicate route id '{rid}'")
            ids.add(rid)
            for k, v in r.items():
                if k.startswith("trigger") and isinstance(v, str) and nfc_len(v) > MAX_TRIGGER_CHARS:
                    self.add("E161", "core/router.toml",
                             f"route '{rid}' {k} is {nfc_len(v)} characters (max {MAX_TRIGGER_CHARS})")
                if k.startswith("rules"):
                    lines = v.splitlines() if isinstance(v, str) else (v if isinstance(v, list) else [])
                    lines = [x for x in lines if str(x).strip()]
                    if len(lines) > MAX_RULES:
                        self.add("E161", "core/router.toml",
                                 f"route '{rid}' {k} has {len(lines)} lines (max {MAX_RULES})")
            loads = r.get("loads", [])
            if not isinstance(loads, list) or not all(isinstance(f, str) for f in loads):
                self.add("E161", "core/router.toml", f"route '{rid}' loads must be a list of file names")
                continue
            if len(loads) > per_job:
                self.add("E103", "core/router.toml", f"route '{rid}' loads {len(loads)} files (max {per_job})")
            if refs:
                for f in loads:
                    if f not in ref_files:
                        self.add("E130", "core/router.toml",
                                 f"route '{rid}' loads '{f}', which no [[skill.reference]] builds")
            elif loads:
                msg = f"route '{rid}' loads {len(loads)} file(s) but core/method.toml has no [[skill.reference]] yet"
                if self.release:
                    self.add("E130", "core/router.toml", msg)
                else:
                    self.note(msg)

        reached = {f for r in routes for f in (r.get("loads") or []) if isinstance(f, str)}
        modules = {r.get("module") for r in routes}
        for ref in refs:
            label = f"[[skill.reference]] '{ref['file']}'"
            if router is None:
                self.add("E130", "core/method.toml", f"{label}: core/router.toml missing, so no route loads it")
                continue
            if ref["file"] not in reached:
                self.add("E130", "core/method.toml", f"{label} is not loaded by any route")
            if "route" in ref and ref["route"] not in ids:
                self.add("E130", "core/method.toml", f"{label} names unknown route '{ref['route']}'")
            elif "route" not in ref and ref.get("module") not in modules:
                self.add("E130", "core/method.toml", f"{label}: no route has module '{ref.get('module')}'")
            for fid in ref.get("formats") if isinstance(ref.get("formats"), list) else []:
                if fid not in fmt_table:
                    self.add("E130", "core/method.toml", f"{label} names format '{fid}', "
                                                         "not in core/format-checks.toml")
        self.check_reference_parity(refs, routes, fmt_table)
        if method:
            self.check_start_block_anchors(method)

    def check_reference_parity(self, refs: list[dict], routes: list[dict], fmt_table: dict) -> None:
        """E110: a non-EN skill reference must not fall back to the EN router or format-check text.

        render.render_reference uses trigger_<id> / rules_<id> / checks_<id> when present and
        the EN field otherwise, so a missing localized field would ship English text in the
        WHEN TO USE / RULES header or the CHECK BEFORE ANSWERING footer of that edition.
        """
        for ed_id, ed in sorted(self.editions.items()):
            if ed_id == SOURCE_EDITION:
                continue
            suffixes = (f"_{ed_id}", f"_{ed.lang}")
            reported: set[tuple[str, str]] = set()
            for ref in refs:
                if "route" in ref:
                    row = next((r for r in routes if r.get("id") == ref["route"]), None)
                else:
                    row = next((r for r in routes if r.get("module") == ref.get("module")), None)
                for field in ("trigger", "rules"):
                    if row is None or not row.get(field) or any(field + s in row for s in suffixes):
                        continue
                    rid = str(row.get("id", "?"))
                    if (rid, field) not in reported:
                        reported.add((rid, field))
                        self.add("E110", "core/router.toml",
                                 f"route '{rid}' has {field} but no {field}_{ed_id}; the {ed_id.upper()} "
                                 f"reference '{ref['file']}' would show the {SOURCE_EDITION.upper()} text")
                for fid in ref.get("formats") if isinstance(ref.get("formats"), list) else []:
                    row = fmt_table.get(fid)
                    if not isinstance(row, dict) or not row.get("checks") or any("checks" + s in row for s in suffixes):
                        continue
                    if (fid, "checks") not in reported:
                        reported.add((fid, "checks"))
                        self.add("E110", "core/format-checks.toml",
                                 f"[format.{fid}] has checks but no checks_{ed_id}; the {ed_id.upper()} "
                                 f"reference '{ref['file']}' would show the {SOURCE_EDITION.upper()} lines")

    def check_method_table(self, method: dict, table: str, kind: str) -> list[dict]:
        """Validate [[<table>.<kind>]] entries and their selectors; return the valid entries."""
        cfg = method_table(method, table)
        if not isinstance(cfg, dict):
            self.add("E161", "core/method.toml", f"[{table}] must be a table")
            return []
        entries = cfg.get(kind, [])
        if not isinstance(entries, list):
            self.add("E161", "core/method.toml", f"[[{table}.{kind}]] must be an array of tables")
            return []
        id_key = "id" if kind == "anchor" else "file"
        good, seen = [], set()
        for i, entry in enumerate(entries, 1):
            ident = entry.get(id_key) if isinstance(entry, dict) else None
            if not isinstance(ident, str) or not ident:
                self.add("E161", "core/method.toml", f"[[{table}.{kind}]] #{i} has no {id_key}")
                continue
            if ident in seen:
                self.add("E161", "core/method.toml", f"duplicate [[{table}.{kind}]] '{ident}'")
            seen.add(ident)
            selectors = entry.get("sections", [])
            if not isinstance(selectors, list) or not all(isinstance(s, str) for s in selectors):
                self.add("E161", "core/method.toml", f"[[{table}.{kind}]] '{ident}' sections must be a list")
                continue
            for lang in self.prose_langs():
                misses = []
                for sel in selectors:
                    try:
                        cmlib.select_sections([sel], self.sections.get(lang, {}))
                    except CMError:
                        misses.append(sel)
                if misses and len(misses) == len(selectors) and not self.release:
                    # Nothing written for this entry yet (build skips it too); an error on --release.
                    self.note(f"[[{table}.{kind}]] '{ident}' has no {lang.upper()} sections yet")
                    continue
                for sel in misses:
                    self.add("E130", "core/method.toml",
                             f"[[{table}.{kind}]] '{ident}': selector '{sel}' matches no {lang.upper()} section")
            if kind == "anchor" and selectors:
                # build.py titles the heading from this key and falls back to the bare id without it
                key = f"anchor.{ident.lower()}"
                for ed_id, ed in sorted(self.editions.items()):
                    if key not in ed.strings:
                        self.add("E170", "core/method.toml",
                                 f"[[{table}.anchor]] '{ident}' has no title string '{key}' in strings/{ed_id}.toml "
                                 f"(the built heading would read '§CM-{ident} · {ident}')")
            good.append(entry)
        title_key = cfg.get("title_key")
        if title_key is not None:
            for ed_id, ed in sorted(self.editions.items()):
                if title_key not in ed.strings:
                    self.add("E170", "core/method.toml",
                             f"[{table}] title_key '{title_key}' is not a strings key ({ed_id})")
        return good

    def check_levelup_tables(self, method: dict) -> None:
        """[levelup.<area>] tables: file, budget, anchors, and one §CM-id space with the method file (E161)."""
        raw = method.get("levelup")
        if raw is not None and not isinstance(raw, dict):
            self.add("E161", "core/method.toml", "[levelup] must hold [levelup.<area>] tables")
            return
        seen: dict[str, str] = {}
        base = method_table(method, "method")
        for entry in (base.get("anchor") or []) if isinstance(base, dict) else []:
            if isinstance(entry, dict) and isinstance(entry.get("id"), str):
                seen[entry["id"]] = "method"
        for area, cfg in cmlib.levelup_tables(method):
            table = f"levelup.{area}"
            name = cfg.get("file")
            if not isinstance(name, str) or not name.isascii() or not name.isalnum():
                self.add("E161", "core/method.toml", f"[{table}] needs file = an ASCII name such as \"RESEARCH\"")
            budget = cfg.get("budget")
            if budget is not None and not self.target_row("budgets", budget):
                self.add("E161", "core/method.toml", f"[{table}] budget '{budget}' is not in platform/targets.toml")
            for entry in self.check_method_table(method, table, "anchor"):
                aid = entry["id"]
                if aid in seen:
                    self.add("E161", "core/method.toml",
                             f"anchor id '{aid}' is in [{seen[aid]}] and [{table}]; §CM-ids are unique across files")
                seen[aid] = table

    def check_start_block_anchors(self, method: dict) -> None:
        cfg = method.get("method") if isinstance(method.get("method"), dict) else {}
        entries = cfg.get("anchor") if isinstance(cfg.get("anchor"), list) else []
        anchors = [a["id"] for a in entries if isinstance(a, dict) and isinstance(a.get("id"), str)]
        if not anchors:
            return
        for ed_id, ed in sorted(self.editions.items()):
            built = self.root / "dist" / ed_id / "1-INSTRUCTIONS.txt"
            source = self.root / "core" / ed.lang / "start-block.md"
            if built.exists():  # the rendered block is authoritative when it exists
                text, where = self.text(built), self.rel(built)
            elif source.exists():
                text, where = self.render_prose(source, ed, "kit"), self.rel(source)
            else:
                msg = (f"core/{ed.lang}/start-block.md not present; "
                       f"cannot check that it names the {len(anchors)} method anchors")
                if self.release:
                    self.add("E130", f"core/{ed.lang}/start-block.md", msg)
                else:
                    self.note(msg)
                continue
            for aid in anchors:
                if not re.search(rf"§CM-{re.escape(aid)}(?![A-Za-z0-9-])", text):
                    self.add("E130", where,
                             f"method anchor '{aid}' is not named in the start-block router (§CM-{aid})")

    # -- templates (E170)

    def check_templates(self) -> None:
        shared = self.files_under("automation", "guides", suffixes={".tmpl"})
        if (self.root / "core").is_dir():
            shared += sorted((self.root / "core").glob("*.tmpl"))
        for ed_id, ed in sorted(self.editions.items()):
            files: list[Path] = []
            for lang in dict.fromkeys((ed.lang, ed.cfg.get("method_prose", ed.lang))):
                files += cmlib.prose_files(lang, self.root)
                files += sorted((self.root / "locales" / lang).glob("*.md"))
            for path in list(dict.fromkeys(files + shared)):
                text, first = self.shipped(path)
                for message, needle in template_problems(text, ed):
                    where = self.rel(path)
                    pos = text.find(needle) if needle else -1
                    if pos >= 0:
                        where += f":{first + text.count(chr(10), 0, pos)}"
                    self.add("E170", where, f"{message} ({ed_id})")
            for key, value in sorted(ed.strings.items()):
                for message, _ in template_problems(value, ed):
                    self.add("E170", f"strings/{ed_id}.toml", f"key '{key}': {message}")

    # -- schemas/*.toml checked against each other (E161)

    def check_schemas(self) -> None:
        """tools/cmschema.py validates the four schema files together (required keys, options,
        views, key grammars, Bank types, Brand Card fields and budgets)."""
        present = {n: self.toml[f"schemas/{n}.toml"] for n in cmschema.SCHEMAS if f"schemas/{n}.toml" in self.toml}
        if not present:
            self.note("schemas/ not present; E161 schema checks skipped")
            return
        for name in cmschema.SCHEMAS:
            if name not in present:
                self.add("E161", f"schemas/{name}.toml", "file not found (the schemas are checked as a set)")
        data = {n: d for n, d in present.items() if d is not None}  # bad TOML is already E161
        for code, where, message in cmschema.check(self.root, data):
            self.add(code, where, message)

    # -- hub properties (E160)

    def hub_names(self) -> set[str] | None:
        data = self.toml.get("schemas/hub.toml")
        if data is None:
            return None
        props = {"properties", "property", "fields", "field", "columns", "column"}
        tables = {"databases", "database", "tables", "table"}
        names: set[str] = set()

        def walk(node, inside: bool) -> None:
            if isinstance(node, dict):
                for k, v in node.items():
                    if inside and (k == "name" or k.startswith("name_")) and isinstance(v, str):
                        names.add(v)
                    is_props = k in props or k.endswith(("_properties", "_property"))
                    if is_props and isinstance(v, dict):  # [properties.Status] style
                        names.update(pk for pk, pv in v.items() if isinstance(pv, dict))
                    walk(v, inside or is_props or k in tables)
            elif isinstance(node, list):
                for item in node:
                    walk(item, inside)

        walk(data, False)
        return names

    def check_hub_refs(self) -> None:
        names = self.hub_names()
        for path in self.source_files():
            text, first = self.shipped(path)
            for lineno, line in enumerate(text.splitlines(), first):
                for m in HUB_REF_RE.finditer(line):
                    name = m.group(1).strip()
                    where = f"{self.rel(path)}:{lineno}"
                    if names is None:
                        self.add("E160", where, f"`hub:{name}` used but schemas/hub.toml is missing")
                    elif name not in names:
                        self.add("E160", where, f"unknown hub property '{name}' (not in schemas/hub.toml)")

    # -- word rules (E140-E145)

    @staticmethod
    def match(line: str, rules, skip=None) -> list[tuple[str, str]]:
        """Non-overlapping (label, text) hits of every rule in one line, left to right."""
        hits = []
        for label, rx in rules:
            for m in rx.finditer(line):
                if m.group(0) and not (skip and skip(line, m, label)):
                    hits.append((m.start(), -m.end(), label, m.group(0)))
        out, end = [], -1
        for start, neg_end, label, hit in sorted(hits):
            if start >= end:
                out.append((label, hit))
                end = -neg_end
        return out

    def scan(self, code: str, where: str, text: str, rules, *, key: str | None = None,
             skip=None, rendered: bool = False, first: int = 1) -> None:
        """Report rule hits line by line, honouring lint-ok waivers and the allowlist.

        Source lines with a hit or a waiver are remembered so that their rendered
        copies in dist/ (rendered=True) are not reported a second time.
        """
        for lineno, line in enumerate(nfc(text).splitlines(), first):
            if rendered and any(p.search(line) for p in self.seen_lines[code]):
                continue
            is_waived = waived(line, code)
            body = WAIVER_RE.sub("", line)
            hits = self.match(body, rules, skip)
            if not hits and not is_waived:
                continue
            if not rendered:
                pattern = line_pattern(body)
                if pattern:
                    self.seen_lines[code].append(pattern)
            if is_waived:
                continue
            for label, hit in hits:
                if self.allowed(code, where, hit, key):
                    continue
                message = DESCRIBE[code](label, hit)
                if key is not None:
                    self.add(code, where, f"key '{key}': {message}")
                else:
                    self.add(code, f"{where}:{lineno}", message)

    @staticmethod
    def skip_pii(line: str, m: re.Match, label: str) -> bool:
        return label == "@handle" and m.group(1).lower() in NOT_HANDLES

    @staticmethod
    def skip_date(line: str, m: re.Match, label: str) -> bool:
        # "as of {date}" is a runtime slot the model fills, not a dated fact
        return label == "time word" and line[m.end():].lstrip().startswith("{")

    def check_source_text(self) -> None:
        mg = [(n, phrase_regex(n)) for n in MATT_GRAY_NAMES]
        fill = [(p, phrase_regex(p)) for p in FILL_WORDING]
        for sid, (texts, _) in sorted(self.strings.items()):
            path, lang = f"strings/{sid}.toml", self.lang_of(sid)
            for key, text in sorted(texts.items()):
                self.scan("E140", path, text, self.terms_for("deny", lang), key=key)
                self.scan("E141", path, text, self.terms_for("tells", lang), key=key)
                self.scan("E142", path, text, mg, key=key)
                self.scan("E143", path, text, fill, key=key)
                self.scan("E144", path, text, PII_RULES, key=key, skip=self.skip_pii)
        for path in self.source_files():
            relp = self.rel(path)
            top = relp.split("/", 1)[0]
            if top == "strings" and path.suffix == ".toml":
                continue  # scanned value by value above
            text, first = self.shipped(path)
            self.scan("E142", relp, text, mg, first=first)
            self.scan("E143", relp, text, fill, first=first)
            self.scan("E144", relp, text, PII_RULES, skip=self.skip_pii, first=first)
            if top in ("core", "modules", "locales") and not (top == "locales" and path.name == "platform-notes.md"):
                self.scan("E145", relp, text, DATE_RULES, skip=self.skip_date, first=first)
            lang = None if top == "guides" else path.parent.name
            if top == "guides" or (top == "locales" and path.name == "examples.md"):
                self.scan("E140", relp, text, self.terms_for("deny", lang), first=first)
                self.scan("E141", relp, text, self.terms_for("tells", lang), first=first)

    # -- VN address (E147)

    def check_vn_address(self) -> None:
        texts = self.strings.get(VN_ADDRESS_LANG, ({}, {}))[0]
        for key, text in sorted(texts.items()):
            for line in nfc(text).splitlines():
                if waived(line, "E147"):
                    continue
                for label, rx in VN_LEAK_MARKERS:
                    for m in rx.finditer(WAIVER_RE.sub("", line)):
                        self.add("E147", f"strings/{VN_ADDRESS_LANG}.toml",
                                 f"key '{key}': {label} '{m.group(0)}' prints to the coach (use {{XƯNG HÔ}})")
                if key.startswith(VN_BUYER_KEYS):
                    continue
                for hit in bare_ban(WAIVER_RE.sub("", line)):
                    self.add("E147", f"strings/{VN_ADDRESS_LANG}.toml",
                             f"key '{key}': bare '{hit}' in a coach-facing line (use {{xưng hô}})")
        for sid, sec in sorted(self.sections.get(VN_ADDRESS_LANG, {}).items()):
            where = self.section_where.get((VN_ADDRESS_LANG, sid), sec.file)
            relp, _, start = where.rpartition(":")
            first = int(start) + 1 if start.isdigit() else 1
            coach_facing = relp.startswith(f"core/{VN_ADDRESS_LANG}/")
            for lineno, line in enumerate(nfc(sec.body).splitlines(), first):
                if waived(line, "E147"):
                    continue
                body = WAIVER_RE.sub("", line)
                for label, rx in VN_LEAK_MARKERS:
                    for m in rx.finditer(body):
                        self.add("E147", f"{relp}:{lineno}", f"{label} '{m.group(0)}' prints to the coach "
                                 f"(use {{XƯNG HÔ}} / {{xưng hô}})")
                if coach_facing:
                    for hit in bare_ban(body):
                        self.add("E147", f"{relp}:{lineno}", f"bare '{hit}' in a coach-facing line (use {{xưng hô}})")
        for pattern in VN_MARKER_SURFACES:
            for path in sorted(self.root.glob(pattern)):
                if not path.is_file():
                    continue
                try:
                    text = path.read_text(encoding="utf-8")
                except (OSError, UnicodeDecodeError):
                    continue
                for lineno, line in enumerate(nfc(text).splitlines(), 1):
                    if waived(line, "E147"):
                        continue
                    for label, rx in VN_LEAK_MARKERS:
                        for m in rx.finditer(WAIVER_RE.sub("", line)):
                            self.add("E147", f"{self.rel(path)}:{lineno}", f"{label} '{m.group(0)}' prints to the "
                                     f"coach (use {{XƯNG HÔ}} / {{xưng hô}})")

    # -- persona fixture facts in kit sources (E148)

    def check_leak_terms(self) -> None:
        try:
            terms = load_leak_terms(self.root)
        except (OSError, tomllib.TOMLDecodeError) as exc:
            self.add("E161", LEAK_TERMS_FILE, f"cannot read: {exc}")
            return
        if not terms:
            return

        def scan(where: str, first: int, text: str) -> None:
            for lineno, line in enumerate(nfc(text).splitlines(), first):
                if waived(line, "E148"):
                    continue
                body = WAIVER_RE.sub("", line)
                for persona, term, rx in terms:
                    if rx.search(body):
                        self.add("E148", f"{where}:{lineno}" if first else where,
                                 f"'{term}' is a test persona's fact ({persona}); write the example for another niche")

        for lang, secs in sorted(self.sections.items()):
            for sid, sec in sorted(secs.items()):
                where = self.section_where.get((lang, sid), sec.file)
                relp, _, start = where.rpartition(":")
                if not start.isdigit():
                    relp, start = where, "0"
                scan(relp, int(start) + 1, sec.body)
        for lang, (texts, _) in sorted(self.strings.items()):
            for key, text in sorted(texts.items()):
                scan(f"strings/{lang}.toml key '{key}'", 0, text)
        for path in sorted((self.root / "plugin").rglob("*")):
            if path.is_file() and path.suffix in TEXT_SUFFIXES:
                try:
                    text = path.read_text(encoding="utf-8")
                except (OSError, UnicodeDecodeError):
                    continue
                scan(self.rel(path), 1, text)

    # -- Ship Check card budgets (E101)

    # ship-check.md may hold one card, or several sections included with {{>ship.…}}:
    # ship.kit and ship.card are budgeted as cards, ship.task as the task card.
    CARD_SECTIONS = (("ship.kit", "ship_check_card", "kit"), ("ship.card", "ship_check_card", "skill"),
                     ("ship.task", "ship_check_task", "task"))

    def check_cards(self) -> None:
        for ed_id, ed in sorted(self.editions.items()):
            path = self.root / "core" / ed.lang / "ship-check.md"
            sectioned = path.exists() and cmlib.parse_sections(self.text(path))[1]
            if sectioned:
                for sid, budget, target in self.CARD_SECTIONS:
                    if sid in ed.sections():
                        card = cmlib.render("{{>%s}}" % sid, ed, target, path=self.rel(path)).strip()
                        self.check_budget(budget, ed_id, nfc_len(card), f"{self.rel(path)}#{sid}",
                                          "Ship Check card", "characters")
                continue
            for name, budget in (("ship-check.md", "ship_check_card"), ("ship-check-task.md", "ship_check_task")):
                path = self.root / "core" / ed.lang / name
                if path.exists():
                    card = self.render_prose(path, ed, "kit").rstrip("\n")
                    self.check_budget(budget, ed_id, nfc_len(card), self.rel(path), "Ship Check card", "characters")

    def card_markers(self, ed: cmlib.Edition, task: bool) -> list[str]:
        """'SHIP CHECK' plus the first line of the edition's card (task variant first for tasks)."""
        if (ed.id, task) not in self._cards:
            markers = [CARD_MARKER]
            for sid in (("ship.task",) if task else ("ship.kit", "ship.card")):
                if sid in ed.sections():
                    card = cmlib.render("{{>%s}}" % sid, ed, "task" if task else "kit")
                    first = next((ln.strip() for ln in card.splitlines() if len(re.sub(r"\W", "", ln)) >= 8), None)
                    if first:
                        markers.append(first)
            for name in (("ship-check-task.md", "ship-check.md") if task else ("ship-check.md",)):
                path = self.root / "core" / ed.lang / name
                if path.exists():
                    card = self.render_prose(path, ed, "task" if task else "kit")
                    first = next((ln.strip() for ln in card.splitlines() if len(re.sub(r"\W", "", ln)) >= 8), None)
                    if first:
                        markers.append(first)
            self._cards[(ed.id, task)] = markers
        return self._cards[(ed.id, task)]

    # -- dist/ (E101-E103, E130-E132, E142-E143, E150-E153, E170)

    def check_dist(self) -> None:
        dist = self.root / "dist"
        if not dist.is_dir():
            if self.release:
                self.add("E170", "dist", "build output missing; run tools/build.py --edition all "
                                         "and tools/package.py before lint --release")
            else:
                self.note("dist/ not found, so these were skipped: E101/E103 budgets on built files, "
                          "E102 SKILL.md, E130 anchors in built files, E131, E132, E142/E143 on rendered "
                          "text, E150-E153. Run python3 tools/build.py --edition all first.")
            return
        self.check_manifest(dist)
        for path in sorted(dist.rglob("*")):
            if not path.name.isascii():
                self.add("E150", self.rel(path), "non-ASCII file name")
        for ed_id, ed in sorted(self.editions.items()):
            out = dist / ed_id
            if not out.is_dir():
                msg = f"dist/{ed_id}/ missing; run tools/build.py --edition {ed_id}"
                if self.release:
                    self.add("E170", f"dist/{ed_id}", msg)
                else:
                    self.note(msg)
                continue
            self.check_kit_files(ed, out)
            self.check_skill_zip(ed, out / "Level-ups" / "autopilot" / f"{ed.skill_name}.zip")
            self.check_tasks(ed, dist / "maintainer" / "tasks" / ed_id)
        self.check_zips(dist)
        self.check_plugin(dist)
        self.check_dist_text(dist)

    def check_manifest(self, dist: Path) -> None:
        path = dist / "maintainer" / "manifest.json"
        where = self.rel(path)
        if not path.exists():
            if self.release:
                self.add("E170", where, "manifest missing; run tools/build.py --edition all")
            return
        try:
            manifest = json.loads(self.text(path))
        except json.JSONDecodeError as exc:
            self.add("E161", where, f"bad JSON: {exc}")
            return
        skipped = manifest.get("skipped", []) if isinstance(manifest, dict) else []
        for item in skipped if isinstance(skipped, list) else []:
            if isinstance(item, dict):
                label = " ".join(str(item[k]) for k in ("edition", "target", "item") if item.get(k))
                reason = item.get("reason", "")
            else:
                label, reason = str(item), ""
            if self.release:
                self.add("E170", where, f"build skipped {label}" + (f": {reason}" if reason else ""))
        if skipped and not self.release:
            self.note(f"the build skipped {len(skipped)} target(s) whose sources a later phase writes "
                      f"(see {where}); each is an error on --release")

    def check_kit_files(self, ed: cmlib.Edition, out: Path) -> None:
        instructions = out / "1-INSTRUCTIONS.txt"
        if instructions.exists():
            text, where = self.text(instructions), self.rel(instructions)
            self.check_budget("instructions_block", ed.id, nfc_len(text), where, "instruction block", "characters")
            self.check_sandwich(ed, text, where, "kit")
            self.check_card(ed, text, where)
        phone = out / "PHONE-STARTER.txt"
        if phone.exists():
            self.check_budget("phone_starter", ed.id, nfc_len(self.text(phone)), self.rel(phone),
                              "phone starter", "characters")
        method = self.toml.get("core/method.toml") or {}
        # (core/method.toml table, target flag, built path, budget, label): the method file and one file per level-up
        files = [("method", "method", f"CONTENT-MACHINE-{ed.file_suffix}.md", "method_file", "method file")]
        for area, row in cmlib.levelup_tables(method):
            name = row.get("file")
            if isinstance(name, str) and name.isalnum() and isinstance(row.get("budget"), str):
                files.append((f"levelup.{area}", "grow", f"Level-ups/{name}-{ed.file_suffix}.md", row["budget"],
                              f"{area} level-up file"))
        secs = self.sections.get(ed.cfg.get("method_prose", ed.lang), {})
        defined = self.anchor_ids(method)
        for table, target, relpath, budget, label in files:
            path = out / relpath
            if not path.exists():
                continue
            text, where = self.text(path), self.rel(path)
            self.check_budget(budget, ed.id, len(text.encode("utf-8")), where, label, "bytes")
            blocks = self.anchor_blocks(text, self.contract(ed, target))
            cfg = method_table(method, table)
            entries = cfg.get("anchor") if isinstance(cfg.get("anchor"), list) else []
            for anchor in entries:
                if isinstance(anchor, dict) and anchor.get("sections") and anchor.get("id") not in blocks:
                    written = any(_selector_matches(sel, secs) for sel in anchor["sections"]
                                  if isinstance(sel, str))
                    if not written and not self.release:
                        continue  # build skipped it: its modules are not written yet (noted above)
                    self.add("E130", where,
                             f"anchor §CM-{anchor.get('id')} has sections but no heading in the built file")
            if table == "method":  # a level-up anchor may hold several sections: those are checked one by one
                for aid, block in blocks.items():
                    self.check_budget("method_section", ed.id, len(block.encode("utf-8")), where,
                                      f"section §CM-{aid}", "bytes")
            for ref in sorted(set(CM_REF_RE.findall(text)) - defined):
                self.add("E130", where, f"§CM-{ref} is named here but is no anchor of the method file or a level-up file")

    def check_tasks_data(self) -> None:
        """automation/tasks.toml: every [[task]] has a template file, a prose section and a name; the 900-character
        cap in [caps] is the task_nudge budget (E161)."""
        where = "automation/tasks.toml"
        data = self.toml.get(where)
        if not data:
            return
        auto = self.root / "automation"
        rows = data.get("task", [])
        if not isinstance(rows, list) or not rows:
            self.add("E161", where, "[[task]] entries expected")
            return
        ids: set[str] = set()
        for i, row in enumerate(rows, 1):
            if not isinstance(row, dict):
                self.add("E161", where, f"[[task]] #{i} must be a table")
                continue
            tid = row.get("id")
            if not isinstance(tid, str) or not tid or tid in ids:
                self.add("E161", where, f"[[task]] #{i} needs a unique id")
            ids.add(str(tid))
            template = row.get("template")
            if not isinstance(template, str) or not (auto / template).is_file():
                self.add("E161", where, f"[[task]] '{tid}': template '{template}' is not in automation/")
            elif f"{{{{>{row.get('section')}}}}}" not in (auto / template).read_text(encoding="utf-8"):
                self.add("E161", where, f"[[task]] '{tid}': {template} does not include its section '{row.get('section')}'")
            for lang in self.prose_langs():
                if row.get("section") not in self.sections.get(lang, {}):
                    self.add("E161", where, f"[[task]] '{tid}': section '{row.get('section')}' has no {lang.upper()} text")
            key = row.get("name_key")
            if key is not None:
                for ed_id, ed in sorted(self.editions.items()):
                    if key not in ed.strings:
                        self.add("E161", where, f"[[task]] '{tid}': name_key '{key}' is not a strings key ({ed_id})")
            elif not (isinstance(row.get("name"), dict) and all(e in row["name"] for e in self.editions)):
                self.add("E161", where, f"[[task]] '{tid}' needs name_key or name = {{ en = ..., vn = ... }}")
        cap = (data.get("caps") or {}).get("max_chars_filled")
        for ed_id in sorted(self.editions):
            want = self.budget("task_nudge", ed_id)
            if want and cap != want:
                self.add("E161", where, f"[caps] max_chars_filled is {cap}, the task_nudge budget is {want}")

    def check_levelup_sections(self) -> None:
        """Every section a level-up anchor pulls in, as rendered, stays within the method_section budget (E101).

        An anchor of a level-up file may hold two or three sections (research does); each section still has to fit
        one retrieval chunk, like each §CM anchor of the method file.
        """
        method = self.toml.get("core/method.toml") or {}
        tables = cmlib.levelup_tables(method)
        for ed_id, ed in sorted(self.editions.items()):
            lang = ed.cfg.get("method_prose", ed.lang)
            secs = self.sections.get(lang, {})
            seen: set[str] = set()
            for area, cfg in tables:
                for anchor in cfg.get("anchor", []) if isinstance(cfg.get("anchor"), list) else []:
                    selectors = anchor.get("sections") if isinstance(anchor, dict) else None
                    if not isinstance(selectors, list):
                        continue
                    try:
                        picked = cmlib.select_sections([s for s in selectors if isinstance(s, str)], secs)
                    except CMError:
                        continue  # reported as E130 by check_router
                    for sec in picked:
                        if sec.id in seen:
                            continue
                        seen.add(sec.id)
                        try:
                            body = cmlib.render(sec.body, ed, "grow", path=f"{sec.file}#{sec.id}")
                        except CMError:
                            continue  # reported as E170 by check_templates
                        self.check_budget("method_section", ed_id, len(nfc(body).encode("utf-8")),
                                          self.section_where.get((lang, sec.id), sec.file), f"section {sec.id}",
                                          "bytes")

    @staticmethod
    def anchor_ids(method: dict) -> set[str]:
        """Every anchor id in core/method.toml: the method file and all level-up files."""
        ids: set[str] = set()
        tables = ["method"] + [f"levelup.{area}" for area, _ in cmlib.levelup_tables(method)]
        for table in tables:
            cfg = method_table(method, table)
            for entry in (cfg.get("anchor") if isinstance(cfg, dict) and isinstance(cfg.get("anchor"), list) else []):
                if isinstance(entry, dict) and isinstance(entry.get("id"), str):
                    ids.add(entry["id"])
        return ids

    @staticmethod
    def anchor_blocks(text: str, contract: str | None) -> dict[str, str]:
        """Each '## §CM-<ID>' block of a method or level-up file, up to the next one."""
        heads = list(CM_HEADING_RE.finditer(text))
        blocks = {}
        for i, m in enumerate(heads):
            end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
            block = text[m.start():end]
            if i + 1 == len(heads) and contract and block.rstrip().endswith(contract):
                block = block.rstrip()[: -len(contract)]  # the closing contract line is not part of it
            blocks[m.group(1)] = block.rstrip("\n") + "\n"
        return blocks

    def check_sandwich(self, ed: cmlib.Edition, text: str, where: str, target: str) -> None:
        contract = self.contract(ed, target)
        if contract is None:
            self.add("E131", where, f"strings key '{CONTRACT_KEY}' missing ({ed.id}); no output contract to check")
            return
        c = norm(contract)
        lines = [ln for ln in text.splitlines() if ln.strip()]
        n = max(1, len([ln for ln in contract.splitlines() if ln.strip()]))
        top = c in norm(" ".join(lines[: n + HEAD_LINES]))
        bottom = c in norm(" ".join(lines[-(n + TAIL_LINES):]))
        if top and bottom and norm(text).count(c) < 2:  # short text: both windows see one copy
            self.add("E131", where, "output contract appears once; it must open and close the text")
            return
        if not top:
            self.add("E131", where, "output contract line missing at the top")
        if not bottom:
            self.add("E131", where, "output contract line missing at the bottom")

    def check_card(self, ed: cmlib.Edition, text: str, where: str, task: bool = False) -> None:
        markers = self.card_markers(ed, task)
        flat = norm(text)
        if not any(norm(m) in flat for m in markers):
            looked = " or ".join(repr(m) for m in markers)
            self.add("E132", where, f"Ship Check card missing (looked for {looked})")

    def check_skill_zip(self, ed: cmlib.Edition, path: Path) -> None:
        if not path.exists():
            return
        data, where = path.read_bytes(), self.rel(path)
        self.check_budget("skill_zip", ed.id, len(data), where, "skill zip", "bytes")
        try:
            zf = zipfile.ZipFile(io.BytesIO(data))
        except zipfile.BadZipFile:
            return  # check_zips reports it
        with zf:
            name = ed.skill_name
            files = [n for n in zf.namelist() if not n.endswith("/")]
            tops = sorted({n.split("/", 1)[0] for n in files})
            if tops != [name]:
                found = ", ".join(tops) or "nothing"
                self.add("E102", where, f"the zip must hold one folder named '{name}' (found {found})")
            skill_md = f"{name}/SKILL.md"
            if skill_md not in files:
                self.add("E102", where, f"{skill_md} missing")
            else:
                raw = zf.read(skill_md)
                text, inner = raw.decode("utf-8", errors="replace"), f"{where}!{skill_md}"
                fm = frontmatter(text)
                if fm is None:
                    self.add("E102", inner, "no front matter (--- name / description ---)")
                else:
                    if not fm.get("name"):
                        self.add("E102", inner, "front matter has no name")
                    else:
                        self.check_skill_name(fm["name"], inner, "name")
                        if fm["name"] != name:
                            self.add("E102", inner, f"name '{fm['name']}' does not match the folder '{name}'")
                    self.check_description(fm.get("description", ""), ed.id, inner, "description")
                self.check_budget("skill_md_lines", ed.id, count_lines(text), inner, "SKILL.md", "lines")
                self.check_budget("skill_md_bytes", ed.id, len(raw), inner, "SKILL.md", "bytes")
                self.check_card(ed, text, inner)
            total = 0
            for ref in sorted(n for n in files if n.startswith(f"{name}/references/") and n.endswith(".md")):
                raw = zf.read(ref)
                text, inner = raw.decode("utf-8", errors="replace"), f"{where}!{ref}"
                total += len(raw)
                self.check_budget("reference_lines", ed.id, count_lines(text), inner, "reference", "lines", "E103")
                self.check_budget("reference_bytes", ed.id, len(raw), inner, "reference", "bytes", "E103")
                self.check_sandwich(ed, text, inner, "skill")
            self.check_budget("references_total_bytes", ed.id, total, where, "all references", "bytes", "E103")

    def check_tasks(self, ed: cmlib.Edition, folder: Path) -> None:
        if not folder.is_dir():
            return
        for path in sorted(folder.glob("*.txt")):
            text, where = self.text(path), self.rel(path)
            budget = next((b for prefix, b in TASK_BUDGETS if path.stem.startswith(prefix)), None)
            if budget:
                self.check_budget(budget, ed.id, nfc_len(text), where, "task text", "characters")
            if not path.stem.startswith(CARDLESS_TASKS):
                self.check_card(ed, text, where, task=True)

    def check_plugin(self, dist: Path) -> None:
        """dist/content-machine-plugin.zip: the skills the sources promise, each with its front matter and files.

        Per edition: the main skill and one companion per [levelup.<area>] (name <skill>-<edition>, SKILL.md and the
        level-up file as built in dist/<edition>/Level-ups/); plugin/agents/*.md as agents. E102 front matter,
        E103 agent length, E130 a §CM- id the skill names that no file has, E170 a skill or file that is missing.
        """
        path = dist / "content-machine-plugin.zip"
        if not path.exists():
            return
        where = self.rel(path)
        try:
            zf = zipfile.ZipFile(io.BytesIO(path.read_bytes()))
        except zipfile.BadZipFile:
            return  # reported by check_zips
        with zf:
            names = set(zf.namelist())
            base = "content-machine"
            try:
                manifest = json.loads(zf.read(f"{base}/.claude-plugin/plugin.json"))
            except (KeyError, json.JSONDecodeError):
                self.add("E161", where, f"{base}/.claude-plugin/plugin.json is missing or not JSON")
                manifest = {}
            version = (self.root / "VERSION").read_text(encoding="utf-8").strip() if (self.root / "VERSION").exists() else None
            if manifest and version and manifest.get("version") != version:
                self.add("E170", where, f"plugin.json version {manifest.get('version')} is not VERSION {version}")
            method = self.toml.get("core/method.toml") or {}
            defined = self.anchor_ids(method)
            wanted: dict[str, tuple[str, dict | None]] = {}   # skill folder -> (edition id, [levelup] table or None)
            companions = (self.root / "plugin" / "companions.toml").exists()
            for ed_id, ed in sorted(self.editions.items()):
                wanted[f"content-machine-{ed_id}"] = (ed_id, None)
                if companions:
                    for area, cfg in cmlib.levelup_tables(method):
                        wanted[f"{cfg.get('skill')}-{ed_id}"] = (ed_id, cfg)
            for name, (ed_id, cfg) in sorted(wanted.items()):
                skill = f"{base}/skills/{name}/SKILL.md"
                if skill not in names:
                    self.add("E170", where, f"skill '{name}' is missing from the plugin")
                    continue
                text = zf.read(skill).decode("utf-8")
                fields = front_matter_fields(text)
                inner = f"{where}!{skill}"
                if fields.get("name") != name:
                    self.add("E102", inner, f"front matter name '{fields.get('name')}' must be the folder name '{name}'")
                desc = fields.get("description", "")
                if not desc or nfc_len(desc) > SKILL_DESCRIPTION_HARD_MAX or "<" in desc or ">" in desc:
                    self.add("E102", inner, f"description must be 1-{SKILL_DESCRIPTION_HARD_MAX} characters without "
                                            f"< or > (is {nfc_len(desc)})")
                if cfg is None:
                    continue
                ed = self.editions[ed_id]
                file = f"{cfg.get('file')}-{ed.file_suffix}.md"
                built = dist / ed_id / "Level-ups" / file
                inside = f"{base}/skills/{name}/{file}"
                if inside not in names:
                    self.add("E170", inner, f"{file} is not next to the skill")
                elif built.exists() and zf.read(inside) != built.read_bytes():
                    self.add("E170", inner, f"{file} differs from dist/{ed_id}/Level-ups/{file}")
                for ref in sorted(set(CM_REF_RE.findall(text)) - defined):
                    self.add("E130", inner, f"§CM-{ref} is named here but is no anchor of the method file or a level-up file")
            if companions:
                src = sorted((self.root / "plugin" / "agents").glob("*.md"))
                for f in src:
                    inner = f"{base}/agents/{f.name}"
                    if inner not in names:
                        self.add("E170", where, f"agent '{f.stem}' is missing from the plugin")
                        continue
                    agent = zf.read(inner).decode("utf-8")
                    fields = front_matter_fields(agent)
                    if fields.get("name") != f.stem or not fields.get("description"):
                        self.add("E102", f"{where}!{inner}", f"front matter needs name: {f.stem} and a description")
                    if count_lines(agent) > 60:
                        self.add("E103", f"{where}!{inner}", f"agent is {count_lines(agent)} lines, over 60")
                if not src:
                    self.add("E170", where, "plugin/companions.toml exists but plugin/agents/ holds no agent")

    def check_zips(self, dist: Path) -> None:
        for path in sorted(dist.rglob("*.zip")):
            data, where = path.read_bytes(), self.rel(path)
            if self.check_zip_bytes(data, where):
                self.check_zip_rebuild(data, where)

    def check_zip_bytes(self, data: bytes, where: str, depth: int = 0) -> bool:
        """Hygiene and the determinism contract for one zip (and zips inside it). True if clean."""
        try:
            zf = zipfile.ZipFile(io.BytesIO(data))
        except zipfile.BadZipFile:
            self.add("E152", where, "not a readable zip")
            return False
        clean = True
        with zf:
            infos = zf.infolist()
            names = [i.filename for i in infos]
            stamped, modes, extras = [], [], set()
            for info in infos:
                name = info.filename
                parts = [p for p in name.split("/") if p]
                folders = parts if info.is_dir() else parts[:-1]
                if not name.isascii():
                    self.add("E150", where, f"non-ASCII entry name '{name}'")
                    clean = False
                if any((p.startswith(".") and p not in KEPT_DOT_NAMES) or p in OS_LITTER for p in parts):
                    self.add("E151", where, f"'{name}' is a dotfile, __MACOSX or OS litter")
                    clean = False
                if any(p in FORBIDDEN_ZIP_DIRS for p in folders):
                    self.add("E153", where, f"'{name}' ships qa/ or evals/ content")
                    clean = False
                if info.date_time != DOS_EPOCH:
                    stamped.append(info)
                mode = (info.external_attr >> 16) & 0o777
                if mode not in FIXED_MODES:
                    modes.append(f"{name} {mode:o}")
                extras.update(TIME_EXTRA_FIELDS[h] for h in extra_field_ids(info.extra) if h in TIME_EXTRA_FIELDS)
                if name.lower().endswith(".zip") and depth < 2:
                    clean &= self.check_zip_bytes(zf.read(info), f"{where}!{name}", depth + 1)
            if stamped:
                first = stamped[0]
                stamp = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}".format(*first.date_time[:5])
                self.add("E152", where, f"{len(stamped)} entr{'y' if len(stamped) == 1 else 'ies'} carry a build-time "
                                        f"timestamp ('{first.filename}' {stamp}); the contract fixes 1980-01-01 00:00")
            if names != sorted(names):
                self.add("E152", where, "entries are not sorted by name")
            if len(set(names)) != len(names):
                self.add("E152", where, "duplicate entry names")
            if modes:
                self.add("E152", where, f"permissions depend on the machine ({modes[0]}); the contract fixes them")
            if extras:
                self.add("E152", where, f"entries carry {', '.join(sorted(extras))} extra fields")
            unsorted = names != sorted(names) or len(set(names)) != len(names)
            clean = clean and not (stamped or modes or extras or unsorted)
        return clean

    def check_zip_rebuild(self, data: bytes, where: str) -> None:
        """Re-zip the entries with package.make_zip in a temp folder; the sha256 must match."""
        if zip_writer is None:  # fail closed: determinism cannot be shown without the build's writer
            self.add("E152", where, f"cannot be re-zipped: tools/package.py not importable ({ZIP_WRITER_ERROR})")
            return
        with tempfile.TemporaryDirectory() as tmp:
            src, out = Path(tmp) / "src", Path(tmp) / "rebuilt.zip"
            src.mkdir()
            with zipfile.ZipFile(io.BytesIO(data)) as zf:
                for info in zf.infolist():
                    parts = PurePosixPath(info.filename).parts
                    if info.filename.startswith("/") or ".." in parts:
                        self.add("E151", where, f"unsafe entry name '{info.filename}'")
                        return
                    if info.is_dir():
                        continue
                    target = src.joinpath(*parts)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(zf.read(info))
            try:
                zip_writer.make_zip(src, out)
            except CMError as exc:
                self.add("E152", where, f"cannot be rebuilt: {exc.message}")
                return
            a = hashlib.sha256(data).hexdigest()
            b = hashlib.sha256(out.read_bytes()).hexdigest()
            if a != b:
                self.add("E152", where, f"rebuilding it gives a different sha256 ({a[:12]} vs {b[:12]}); "
                                        "zip it with package.make_zip")

    def check_dist_text(self, dist: Path) -> None:
        """E142 and E143 over rendered text: dist files first, then text inside zips."""
        mg = [(n, phrase_regex(n)) for n in MATT_GRAY_NAMES]
        fill = [(p, phrase_regex(p)) for p in FILL_WORDING]
        seen: set[str] = set()

        def scan(where: str, text: str) -> None:
            digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
            if digest in seen:
                return
            seen.add(digest)
            self.scan("E142", where, text, mg, rendered=True)
            self.scan("E143", where, text, fill, rendered=True)

        def text_entry(name: str) -> bool:
            suffix = PurePosixPath(name).suffix.lower()
            return suffix in TEXT_SUFFIXES and not name.endswith("maintainer/manifest.json")

        files = [p for p in sorted(dist.rglob("*")) if p.is_file()]
        for path in files:
            if text_entry(self.rel(path)):
                scan(self.rel(path), self.text(path))
        for path in files:
            if path.suffix.lower() == ".zip":
                self.scan_zip_text(path.read_bytes(), self.rel(path), scan, text_entry)

    def scan_zip_text(self, data: bytes, where: str, scan, text_entry, depth: int = 0) -> None:
        try:
            zf = zipfile.ZipFile(io.BytesIO(data))
        except zipfile.BadZipFile:
            return
        with zf:
            for info in zf.infolist():
                if info.is_dir():
                    continue
                if info.filename.lower().endswith(".zip") and depth < 2:
                    self.scan_zip_text(zf.read(info), f"{where}!{info.filename}", scan, text_entry, depth + 1)
                elif text_entry(info.filename):
                    scan(f"{where}!{info.filename}", zf.read(info).decode("utf-8", errors="replace"))

    # -- unused strings and sections (W202, W203)

    def check_unused(self) -> None:
        source = self.strings.get(SOURCE_EDITION, ({}, {}))[0]
        method = self.toml.get("core/method.toml") or {}
        if source:
            used: set[str] = set()
            for path in self.source_files() + self.files_under("schemas", "editions"):
                used.update(STRING_TAG_RE.findall(self.text(path)))
            for path in sorted((self.root / "tools").glob("*.py")) + sorted((self.root / "evals").glob("*.py")):
                used.update(KEY_LITERAL_RE.findall(self.text(path)))  # evals/graders.py reads next.prefix etc.
            for table in ["method"] + [f"levelup.{area}" for area, _ in cmlib.levelup_tables(method)]:
                cfg = method_table(method, table)
                cfg = cfg if isinstance(cfg, dict) else {}
                used.add(cfg.get("title_key") or f"{table}.title")
                for anchor in cfg.get("anchor", []) if isinstance(cfg.get("anchor"), list) else []:
                    if isinstance(anchor, dict):
                        used.add(f"anchor.{str(anchor.get('id', '')).lower()}")
            for relp, data in self.toml.items():
                if data and relp.startswith(("core/", "schemas/", "automation/")):
                    used.update(v for v in iter_strings(data) if v in source)
            for key in sorted(source.keys() - used):
                self.add("W202", f"strings/{SOURCE_EDITION}.toml",
                         f"key '{key}' is not used by any template, prose, config or tool")
        if method:
            lang = self.source_lang()
            sections = self.sections.get(lang, {})
            selected: set[str] = set()
            kinds = [("method", "anchor")] + [(f"levelup.{a}", "anchor") for a, _ in cmlib.levelup_tables(method)] \
                + [("skill", "reference")]
            for table, kind in kinds:
                cfg = method_table(method, table)
                cfg = cfg if isinstance(cfg, dict) else {}
                for entry in cfg.get(kind, []) if isinstance(cfg.get(kind), list) else []:
                    for sel in (entry.get("sections") or []) if isinstance(entry, dict) else []:
                        try:
                            selected.update(s.id for s in cmlib.select_sections([sel], sections))
                        except (CMError, TypeError):
                            pass  # reported as E130 / E161
            for sid, sec in sorted(sections.items()):
                if sec.file.startswith("modules/") and sid not in selected:
                    self.add("W203", self.section_where[(lang, sid)],
                             f"section '{sid}' is not selected by any target in core/method.toml")


# ---------------------------------------------------------------- entry points

def run_lint(root: Path | str | None = None, release: bool = False, today: dt.date | None = None) -> Report:
    """Lint the repo at root (default: CM_ROOT or this repo)."""
    return Linter(Path(root) if root else cmlib.ROOT, release=release, today=today).run()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="G1 deterministic lint (docs/BUILD.md §7).")
    ap.add_argument("--release", action="store_true", help="also apply the release-only rules")
    ap.add_argument("--root", type=Path, default=None, help="repo root (default: CM_ROOT or this repo)")
    ap.add_argument("--json", action="store_true", help="print findings as a JSON list")
    ap.add_argument("--today", type=dt.date.fromisoformat, default=None,
                    help="date for the freshness rules, YYYY-MM-DD (default: today)")
    args = ap.parse_args(argv)
    report = run_lint(args.root, release=args.release, today=args.today)
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    if args.json:
        print(json.dumps([f.as_dict() for f in report.findings], ensure_ascii=False, indent=2))
        for note in report.notes:
            print(f"note: {note}", file=sys.stderr)
    else:
        for finding in report.findings:
            print(finding)
        for note in report.notes:
            print(f"note: {note}")
        print(report.summary())
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
