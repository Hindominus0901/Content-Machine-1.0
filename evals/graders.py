#!/usr/bin/env python3
"""Transcript graders for the global invariants I1-I18 (QA spec §5.2; evals/README.md).

    python3 evals/graders.py evals/runs/<run-id> [--root PATH] [--strict]

Prints a JSON report. Exit 1 when any invariant or check fails (with --strict,
also when one could not run), 2 when the run folder is unreadable.

Run folder (keep this format; evals/run.py and the simulator agents write it):

    evals/runs/<run-id>/transcript.jsonl   one JSON object per turn, in order:
        {"turn": 1, "role": "coach" | "machine", "text": "...", "t_min": 0.0 | null}
    evals/runs/<run-id>/meta.json
        {"persona": "en/proof-coach", "edition": "en", "lane": "S1", "build_sha": "..."}
        optional "suite": "day0" applies the Day-0 turn budgets even without step markers.

Inputs: evals/personas/<persona>/persona.toml (allowed_numbers, excluded_numbers,
trap_numbers, seeded_names, cold_start, xung_ho, proof_items), expected.toml
(traps) and the persona's *.md files; strings/<edition>.toml rendered through
editions/<edition>.toml when present (verdict.*, next.prefix, checked.prefix);
evals/acceptance.toml; locales/<lang>/deny-list.txt and examples.md when present.

How a machine reply is read:
- Coach-visible text is the reply minus fenced blocks whose info string holds
  "machine" or that follow a "for the machine" / "cho máy" label. Other fenced
  blocks are copy boxes, or paste blocks (info paste/csv/tsv/sheet/notion, or a
  "paste"/"dán" label).
- A verdict line is a line matching a rendered verdict.* string with each {slot}
  as a wildcard (VN: any pronoun in place of the default ones), or starting with
  checked.prefix (the Day-0 plain form of Ready).
- A piece is the text above a verdict line, back to the previous verdict line, or
  to the first heading, ALL-CAPS title, bold-only line or N<digit> label after it.
  Text outside pieces is prose: the machine talking to the coach.
- The running tag "◆ <name> · <step>" on the first line names the step.

Invariants marked "proxy": true cannot be checked from a transcript; they check
the closest mechanical signal (I6 decisions, I7 IDs without the hub, I11
injections, I12 formats, I13 hub writes, I14 keyword CTAs, I15 pronouns).
Status is pass | fail | n/a | not_run; "pass" is null when the check did not run.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent / "tools"
sys.path.insert(0, str(TOOLS))
import cmlib  # noqa: E402
from cmcore import checks as ck  # noqa: E402

DEFAULT_ROOT = Path(os.environ.get("CM_ROOT", Path(__file__).resolve().parent.parent))

FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})\s*(.*)$")
FOR_MACHINE_RE = re.compile(r"for the machine|cho máy|dành cho máy", re.I)
PASTE_INFOS = {"paste", "csv", "tsv", "sheet", "sheets", "notion"}
PASTE_LABEL_RE = re.compile(r"\bpaste\b|(?<!\w)dán(?!\w)", re.I)
TAG_RE = re.compile(r"^◆\s*(.+?)\s*·\s*(.+?)\s*$")
LABEL_RE = re.compile(r"^N\d+\b")
WHY_RE = re.compile(r"^\s*(?:why\??|tại sao\??|tai sao\??)\s*$", re.I)
REFUSAL_RE = re.compile(r"\b(?:not writing|won't write|can't write|I won't|I will not)\b|không viết|mình không bịa",
                        re.I)
ID_RE = re.compile(r"\b([VOSBPRKICAW])-(\d{1,4})\b")
PRONOUNS = ("bạn", "mình", "chị", "anh", "em", "cô", "chú", "tôi")
VERDICT_KINDS_READY = {"ready", "ready_downgraded", "checked"}

TEMPLATE_RE = [re.compile(p, re.I) for p in (
    r"\bfill (?:in|out)\b", r"\bfill (?:the|this|my) (?:template|form|blanks?)\b",
    r"\b(?:complete|use|copy) (?:this|the|my) (?:template|form)\b", r"_{3,}",
    r"\[(?:your|insert|add|enter)\b[^\]]*\]", r"<(?:your|insert)\b[^>]*>", r"\{(?:your|insert)\b[^}]*\}",
    r"điền vào", r"điền (?:mẫu|form|biểu mẫu|chỗ trống)", r"theo mẫu (?:sau|dưới)", r"\[(?:tên|điền)\b[^\]]*\]",
)]
CODE_RE = [
    re.compile(r"\bEdge\b"), re.compile(r"\bShip Check\b", re.I), re.compile(r"\brubrics?\b", re.I),
    re.compile(r"\blint\b", re.I), re.compile(r"\bscor(?:e|es|ed|ing)\b", re.I), re.compile(r"chấm điểm", re.I),
    re.compile(r"\b(?:K|V|A|Au|C)[0-2](?:[\s,/·]+(?:K|V|A|Au|C)[0-2]\b)+"),
    re.compile(r"\b(?:SG|NS|MM|CC|SK|SP|PG|CK|CA|TP|OP|LP|EM|AD|LA|WR|RB)\d{1,2}\b"),
]
SCORE_EN_RE = re.compile(r"\b\d{1,2}\s?/\s?10\b")
DECISION_RE = [re.compile(p, re.I) for p in (
    r"\bchoose\b", r"\bpick (?:one|a|between|which)\b", r"\bwhich (?:one|of these|do you want|would you)\b",
    r"\bdecide\b", r"\boption [A-C1-3]\b", r"\b(?:ok|okay)\b[^.\n]{0,40}\bor\b[^.\n]{0,20}\b(?:change|swap|edit)\b",
    r"(?<!\w)chọn(?!\w)", r"quyết định", r"phương án",
    r"(?<!\w)ok(?!\w)[^.\n]{0,40}(?<!\w)(?:hay|hoặc)(?!\w)[^.\n]{0,20}(?<!\w)sửa(?!\w)",
)]
COLD_RESULT_RE = [re.compile(p, re.I) for p in (
    r"\b(?:helped|trained|coached|served|worked with)\s+(?:over\s+|more than\s+|like\s+|about\s+)?\d",
    r"\d[\d.,]*\+?\s+(?:\w+\s+)?(?:clients?|students?|customers?|học viên|khách hàng)(?!\w)",
    r"\b(?:lost|gained|dropped|lose|gain)\s+\d", r"\d[\d.,]*\s*(?:lbs?|pounds?|kg|ký|cân)(?!\w)",
    r"\b(?:earned|revenue|income|salary)\b[^.\n]{0,30}\d", r"(?:doanh thu|thu nhập|lãi|kiếm được)[^.\n]{0,30}\d",
)]
HUB_DELETE_RE = [re.compile(p, re.I) for p in (
    r"\b(?:delet(?:e|ed|ing)|remov(?:e|ed|ing)|archiv(?:e|ed|ing))\b[^.\n]{0,40}\b(?:rows?|pages?|entries|records?|cards?)\b",
    r"(?<!\w)xo[áa](?!\w)[^.\n]{0,40}(?<!\w)(?:dòng|trang|hàng|thẻ)(?!\w)",
)]
STATUS_RE = re.compile(r"\b(?:Status|Trạng thái)\s*[:=]\s*\**\s*([^\W\d_]+)", re.I)
AI_STATUSES = {"idea", "scripted", "reviewed"}
CTA_RE = re.compile(r"\bcomment\b|\bcmt\b|chấm|bình luận|từ khoá|từ khóa|keyword", re.I)
THRESHOLD_RE = re.compile(r"(?:chấm|đủ\s+\d+\s*(?:comment|cmt|bình luận)|\b\d+\s+comments?\b)", re.I)
DATE_RE = re.compile(r"\b20\d{2}\b|\b\d{1,2}/\d{1,2}\b|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?"
                     r"\s+\d{1,2}\b|tháng\s+\d{1,2}", re.I)
EN_FUNCTION_WORDS = {"the", "and", "you", "your", "is", "are", "with", "this", "that", "will", "would", "what",
                     "when", "which", "have", "has", "from", "about", "just", "they", "there", "here", "please",
                     "because", "before", "after", "only", "also", "then", "than", "into", "our", "we", "it's",
                     "don't", "i'm", "you're", "let's", "it", "of", "for", "my"}
EN_ALLOW = {"ok", "content", "machine", "brand", "card", "hook", "script", "launch", "reel", "reels", "caption",
            "comment", "post", "video", "story", "live", "inbox", "link", "sale", "ads", "email", "zalo",
            "facebook", "tiktok", "instagram", "youtube", "notion", "chatgpt", "claude", "save", "to", "project"}
MAP_STEP_RE = re.compile(r"\bmap\b|bản đồ|thông điệp", re.I)
FILM_STEP_RE = re.compile(r"\bfilm\b|(?<!\w)quay(?!\w)", re.I)
OVERLAP_N = 8
OVERLAP_MAX_DEFAULT = 2
USABLE_MAX_WORDS = 300


class GraderError(Exception):
    """The run folder cannot be graded (missing or malformed files)."""


# ---------------------------------------------------------------- loading

@dataclass
class Turn:
    turn: int
    role: str
    text: str
    t_min: float | None


def load_turns(path: Path) -> list[Turn]:
    if not path.exists():
        raise GraderError(f"{path} missing")
    turns = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise GraderError(f"{path.name} line {i}: {exc.msg}")
        if not isinstance(row, dict) or row.get("role") not in ("coach", "machine") \
                or not isinstance(row.get("text"), str) or not isinstance(row.get("turn"), int):
            raise GraderError(f"{path.name} line {i}: need turn (int), role (coach|machine), text (str)")
        t = row.get("t_min")
        if t is not None and not isinstance(t, (int, float)):
            raise GraderError(f"{path.name} line {i}: t_min must be a number or null")
        turns.append(Turn(row["turn"], row["role"], ck.nfc(row["text"]), None if t is None else float(t)))
    if not turns:
        raise GraderError(f"{path.name} is empty")
    return turns


def _toml(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, "rb") as fh:
        return tomllib.load(fh)


def load_strings(root: Path, edition_id: str) -> tuple[dict, dict]:
    """(rendered strings, edition params). Strings with {{tags}} are rendered for the kit target."""
    try:
        ed = cmlib.load_edition(edition_id, root)
    except cmlib.CMError:
        texts, _ = cmlib.load_strings(edition_id, root)
        ed = cmlib.Edition(id=edition_id, lang=edition_id, cfg={"name": "Content Machine"}, params={},
                           pending={}, strings=texts)
    rendered = {}
    for key, text in ed.strings.items():
        try:
            rendered[key] = cmlib.render_text(text, cmlib.Ctx(ed, frozenset({ed.id, "kit"})))
        except cmlib.CMError:
            rendered[key] = text
    return rendered, ed.params


def load_term_list(path: Path) -> list[tuple[str, re.Pattern]]:
    """locales/<lang>/*.txt: one entry per line, '#' comments; 're:' starts a regex."""
    terms = []
    if not path.exists():
        return terms
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("re:"):
            try:
                terms.append((line, re.compile(line[3:])))
            except re.error:
                continue
        else:
            terms.append((line, ck.phrase_re(line)))
    return terms


# ---------------------------------------------------------------- line matching

def _slot_pattern(text: str, lang: str, prefix_only: bool = False) -> re.Pattern:
    """A rendered string as a regex: {slots} are wildcards; VN pronouns match any pronoun."""
    s = ck.plain_line(text)
    pron = re.compile(r"(?<!\w)(?:" + "|".join(PRONOUNS) + r")(?!\w)", re.I)
    parts = re.split(r"(\{[a-z_][a-z0-9_]*\})", s)
    out = []
    for i, part in enumerate(parts):
        if re.fullmatch(r"\{[a-z_][a-z0-9_]*\}", part):
            out.append(".+?")
            continue
        if i == len(parts) - 1 and part.endswith("."):
            part, tail = part[:-1], r"\.?"
        else:
            tail = ""
        pos = 0
        chunk = []
        for m in (pron.finditer(part) if lang == "vn" else []):
            chunk.append(_lit(part[pos:m.start()]))
            chunk.append("(?:" + "|".join(PRONOUNS) + ")")
            pos = m.end()
        chunk.append(_lit(part[pos:]))
        out.append("".join(chunk) + tail)
    body = "".join(out)
    return re.compile("^" + body + ("" if prefix_only else r"\s*$"), re.I)


def _lit(text: str) -> str:
    out = []
    for ch in text:
        if ch.isspace():
            if not out or out[-1] != r"\s+":
                out.append(r"\s+")
        elif ch == "·":
            out.append("[·•|–—-]")
        else:
            out.append(re.escape(ch))
    return "".join(out)


class Matcher:
    def __init__(self, strings: dict, lang: str):
        self.verdicts: list[tuple[str, re.Pattern]] = []
        for key, text in sorted(strings.items()):
            if key.startswith("verdict.") and text.strip():
                self.verdicts.append((key.split(".", 1)[1], _slot_pattern(text, lang)))
        if strings.get("checked.prefix", "").strip():
            self.verdicts.append(("checked", _slot_pattern(strings["checked.prefix"], lang, prefix_only=True)))
        nxt = strings.get("next.prefix", "").strip()
        arrow = nxt.replace("→", "->")
        self.next_prefixes = [p for p in {nxt, arrow} if p]
        self.why_prefix = ck.plain_line(strings.get("why.prefix", "")).casefold()

    def verdict_kind(self, plain: str) -> str | None:
        for kind, pattern in self.verdicts:
            if pattern.search(plain):
                return kind
        return None

    def is_next(self, plain: str) -> bool:
        return any(plain.casefold().startswith(p.casefold()) for p in self.next_prefixes)


# ---------------------------------------------------------------- replies and pieces

@dataclass
class Line:
    text: str
    plain: str
    block: str = ""        # "" | "copy" | "paste"
    fence: bool = False    # a fence delimiter line


@dataclass
class Piece:
    turn: int
    start: int
    verdict_at: int
    verdict: str
    kind: str
    body: str
    title: str = ""


@dataclass
class Reply:
    turn: int
    index: int             # position in the transcript
    t_min: float | None
    text: str
    lines: list[Line]
    machine_blocks: list[str]
    step: str = ""
    tag_at: int = -1
    verdicts: list[int] = field(default_factory=list)
    nexts: list[int] = field(default_factory=list)
    pieces: list[Piece] = field(default_factory=list)
    prose: list[int] = field(default_factory=list)
    after_why: bool = False

    def visible(self, blocks=("", "copy", "paste")) -> str:
        return "\n".join(ln.text for ln in self.lines if ln.block in blocks and not ln.fence)

    def prose_text(self, with_verdicts: bool = True) -> str:
        idx = set(self.prose) | set(self.nexts) | (set(self.verdicts) if with_verdicts else set())
        return "\n".join(self.lines[i].text for i in sorted(idx))

    def publishable(self) -> str:
        """Piece bodies plus copy and paste boxes plus machine blocks: text whose facts must trace."""
        parts = [p.body for p in self.pieces]
        in_piece = {i for p in self.pieces for i in range(p.start, p.verdict_at)}
        parts += [ln.text for i, ln in enumerate(self.lines) if ln.block and not ln.fence and i not in in_piece]
        return "\n".join(parts + self.machine_blocks)


def split_blocks(text: str) -> tuple[list[Line], list[str]]:
    raw = ck.nfc(text).splitlines()
    lines: list[Line] = []
    machine: list[str] = []
    i = 0
    while i < len(raw):
        m = FENCE_RE.match(raw[i])
        if not m:
            lines.append(Line(raw[i], ck.plain_line(raw[i])))
            i += 1
            continue
        marker, info = m.group(1), m.group(2).strip().casefold()
        label = next((raw[k] for k in (i - 1, i - 2) if k >= 0 and raw[k].strip()), "")
        j = i + 1
        while j < len(raw):
            close = FENCE_RE.match(raw[j])
            if close and close.group(1)[0] == marker[0] and len(close.group(1)) >= len(marker) \
                    and not close.group(2).strip():
                break
            j += 1
        body = raw[i + 1:j]
        if "machine" in info or FOR_MACHINE_RE.search(label):
            machine.append("\n".join(body))
        else:
            kind = "paste" if info.split(" ")[0] in PASTE_INFOS or PASTE_LABEL_RE.search(label) else "copy"
            lines.append(Line(raw[i], "", kind, True))
            lines += [Line(b, ck.plain_line(b), kind) for b in body]
            if j < len(raw):
                lines.append(Line(raw[j], "", kind, True))
        i = j + 1
    return lines, machine


def _is_marker(line: Line, matcher: Matcher) -> bool:
    """A piece title: a heading, an N<digit> label, a bold-only line, or a short line opening in capitals
    ("FILM TODAY (under 30 s)"). The WHY line is never a title."""
    if line.block or line.fence or not line.plain:
        return False
    if matcher.why_prefix and line.plain.casefold().startswith(matcher.why_prefix):
        return False
    raw = line.text.strip()
    if re.match(r"^#{1,6}\s", raw) or LABEL_RE.match(line.plain):
        return True
    if re.fullmatch(r"(\*\*|__)[^*_]+(\*\*|__)\s*:?", raw):
        return True
    caps = []
    for word in line.plain.split():
        letters = [c for c in word if c.isalpha()]
        if not letters or word != word.upper():
            break
        caps.append(word)
    run = sum(1 for w in caps for c in w if c.isalpha())
    return (len(caps) >= 2 or run >= 4) and ck.count_words(line.plain) <= 8


def analyse_reply(turn: Turn, index: int, matcher: Matcher) -> Reply:
    lines, machine = split_blocks(turn.text)
    r = Reply(turn.turn, index, turn.t_min, turn.text, lines, machine)
    first = next((i for i, ln in enumerate(lines) if ln.plain), None)
    if first is not None:
        m = TAG_RE.match(lines[first].plain)
        if m:
            r.step, r.tag_at = m.group(2), first
    for i, ln in enumerate(lines):
        if ln.block or ln.fence or not ln.plain:
            continue
        if matcher.is_next(ln.plain):
            r.nexts.append(i)
        elif matcher.verdict_kind(ln.plain):
            r.verdicts.append(i)
    prev = r.tag_at + 1
    for v in r.verdicts:
        start = next((i for i in range(prev, v) if _is_marker(lines[i], matcher)), prev)
        body = "\n".join(ln.text for ln in lines[start:v] if not ln.fence)
        title = lines[start].plain if start < v and _is_marker(lines[start], matcher) else ""
        r.pieces.append(Piece(turn.turn, start, v, lines[v].text, matcher.verdict_kind(lines[v].plain) or "",
                              body, title))
        prev = v + 1
    in_piece = {i for p in r.pieces for i in range(p.start, p.verdict_at)}
    special = set(r.verdicts) | set(r.nexts) | {r.tag_at}
    r.prose = [i for i, ln in enumerate(lines)
               if i not in in_piece and i not in special and not ln.block and not ln.fence and ln.plain]
    return r


# ---------------------------------------------------------------- run context

@dataclass
class Run:
    root: Path
    run_dir: Path
    meta: dict
    turns: list[Turn]
    replies: list[Reply]
    persona: dict
    expected: dict
    persona_texts: dict[str, str]
    strings: dict
    params: dict
    acceptance: dict
    lang: str

    @property
    def coach_turns(self) -> list[Turn]:
        return [t for t in self.turns if t.role == "coach"]

    def coach_before(self, index: int) -> list[Turn]:
        return [t for t in self.turns[:index] if t.role == "coach"]


def load_run(run_dir: Path, root: Path) -> Run:
    meta_path = run_dir / "meta.json"
    if not meta_path.exists():
        raise GraderError(f"{meta_path} missing")
    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise GraderError(f"meta.json: {exc.msg}")
    for key in ("persona", "edition"):
        if not isinstance(meta.get(key), str) or not meta[key]:
            raise GraderError(f"meta.json needs '{key}'")
    turns = load_turns(run_dir / "transcript.jsonl")
    pdir = root / "evals" / "personas" / meta["persona"]
    if not (pdir / "persona.toml").exists():
        raise GraderError(f"persona {meta['persona']} not found under evals/personas/")
    persona = _toml(pdir / "persona.toml")
    expected = _toml(pdir / "expected.toml")
    texts = {p.name: p.read_text(encoding="utf-8") for p in sorted(pdir.glob("*.md"))}
    strings, params = load_strings(root, meta["edition"])
    lang = "vn" if meta["edition"] == "vn" else "en"
    matcher = Matcher(strings, lang)
    replies = []
    last_coach = ""
    for i, t in enumerate(turns):
        if t.role == "coach":
            last_coach = t.text
            continue
        r = analyse_reply(t, i, matcher)
        r.after_why = bool(WHY_RE.match(last_coach))
        replies.append(r)
    return Run(root, run_dir, meta, turns, replies, persona, expected, texts, strings, params,
               _toml(root / "evals" / "acceptance.toml"), lang)


def result(iid: str, title: str, evidence: list[str], proxy: bool = False, status: str | None = None) -> dict:
    status = status or ("fail" if evidence else "pass")
    passed = None if status == "not_run" else status != "fail"
    return {"id": iid, "title": title, "pass": passed, "status": status, "proxy": proxy, "evidence": evidence}


def _turn(r: Reply) -> str:
    return f"turn {r.turn}"


def _short(text: str, limit: int = 70) -> str:
    text = " ".join(text.split())
    return text if len(text) <= limit else text[: limit - 1] + "…"


def _unquoted(text: str) -> str:
    return re.sub(r'"[^"\n]*"', " ", ck.straight_quotes(text))


def _questions(text: str) -> list[str]:
    return [q.strip() for q in re.findall(r"[^.!?\n]*\?+", _unquoted(text)) if q.strip(" ?")]


def _is_refusal(r: Reply, i: int) -> bool:
    """A hard-stop verdict line, or a line that says what the machine will not write."""
    return bool(REFUSAL_RE.search(r.lines[i].text)) or any(p.verdict_at == i and p.kind == "hardstop"
                                                           for p in r.pieces)


def _refusal_free(r: Reply) -> str:
    keep = [ln.text for i, ln in enumerate(r.lines) if not ln.fence and not _is_refusal(r, i)]
    return "\n".join(keep + r.machine_blocks)


def _without_refusals(text: str, r: Reply) -> str:
    refused = {r.lines[i].text for i in range(len(r.lines)) if _is_refusal(r, i)}
    return "\n".join(line for line in text.splitlines() if line not in refused)


# ---------------------------------------------------------------- invariants

def i1_next_line(run: Run) -> dict:
    title = "Every reply ends with exactly one NEXT line"
    if not run.strings.get("next.prefix"):
        return result("I1", title, ["strings: next.prefix missing"], status="not_run")
    ev = []
    for r in run.replies:
        last = max((i for i, ln in enumerate(r.lines) if ln.text.strip()), default=-1)
        if len(r.nexts) != 1:
            ev.append(f"{_turn(r)}: {len(r.nexts)} NEXT lines")
        elif r.nexts[0] != last:
            ev.append(f"{_turn(r)}: the NEXT line is not the last line")
    return result("I1", title, ev)


def i2_template(run: Run) -> dict:
    ev = []
    for r in run.replies:
        text = r.visible(("", "copy"))
        for p in TEMPLATE_RE:
            m = p.search(text)
            if m:
                ev.append(f'{_turn(r)}: "{m.group(0)}"')
    return result("I2", "No template-fill ask", ev)


def i3_verdict_lines(run: Run) -> dict:
    title = "Exactly one verdict line per piece, ≤20 words, directly under it"
    if not any(k.startswith("verdict.") for k in run.strings):
        return result("I3", title, ["strings: no verdict.* keys"], status="not_run")
    cap = int(run.params.get("verdict_max_words", ck.VERDICT_MAX_WORDS))
    ev = []
    for r in run.replies:
        verdict_set = set(r.verdicts)
        for p in r.pieces:
            v = p.verdict_at
            words = ck.count_words(r.lines[v].plain, run.lang)
            if words > cap:
                ev.append(f'{_turn(r)}: verdict line has {words} words: "{_short(r.lines[v].plain)}"')
            above = [i for i in range(r.tag_at + 1, v) if r.lines[i].text.strip()]
            if not above:
                ev.append(f'{_turn(r)}: verdict line with no piece above it: "{_short(r.lines[v].plain)}"')
                continue
            u = above[-1]
            if u in verdict_set:
                ev.append(f"{_turn(r)}: two verdict lines for one piece")
            elif u in r.nexts or (r.tag_at >= 0 and u == r.tag_at):
                ev.append(f'{_turn(r)}: verdict line with no piece above it: "{_short(r.lines[v].plain)}"')
            elif v - u - 1 > 1:
                ev.append(f"{_turn(r)}: verdict line is not directly under its piece")
        labels = [i for i, ln in enumerate(r.lines) if not ln.block and LABEL_RE.match(ln.plain)]
        for k, start in enumerate(labels):
            end = labels[k + 1] if k + 1 < len(labels) else (r.nexts[0] if r.nexts and r.nexts[0] > start
                                                              else len(r.lines))
            n = sum(1 for v in r.verdicts if start < v < end)
            if n != 1:
                label = LABEL_RE.match(r.lines[start].plain).group(0)
                ev.append(f"{_turn(r)}: piece {label} has {n} verdict lines")
    return result("I3", title, ev)


def i4_codes(run: Run) -> dict:
    ev = []
    for r in run.replies:
        if r.after_why:
            continue
        text = r.visible(("", "copy"))
        hits = [m.group(0) for p in CODE_RE for m in p.finditer(text)]
        if run.lang == "en":
            hits += [m.group(0) for m in SCORE_EN_RE.finditer(text)]
        for h in dict.fromkeys(hits):
            ev.append(f'{_turn(r)}: "{h}"')
    return result("I4", "No score, Edge, Ship Check, rubric, lint or pillar codes in coach text", ev)


def reply_questions(r: Reply) -> list[str]:
    return _questions(r.prose_text())


def i5_questions(run: Run) -> dict:
    ev = []
    for r in run.replies:
        qs = reply_questions(r)
        if len(qs) > 1:
            ev.append(f"{_turn(r)}: {len(qs)} questions: " + " | ".join(_short(q, 50) for q in qs))
    return result("I5", "At most 1 question per reply", ev)


def i6_decisions(run: Run) -> dict:
    asks = []
    for r in run.replies:
        text = _unquoted(r.prose_text(with_verdicts=False))
        hit = next((m.group(0) for p in DECISION_RE for m in [p.search(text)] if m), None)
        if hit:
            asks.append(f'{_turn(r)}: "{hit}"')
    ev = [f"{len(asks)} decision prompts in one session: " + "; ".join(asks)] if len(asks) > 1 else []
    return result("I6", "At most 1 real decision per session", ev, proxy=True)


def i7_ids(run: Run) -> dict:
    defined = {f"P-{int(str(p.get('id', ''))[1:])}" for p in run.persona.get("proof_items", [])
               if re.fullmatch(r"P\d+", str(p.get("id", "")))}
    for t in run.turns:
        for line in t.text.splitlines():
            head = re.sub(r"^[\s|>*\-•]+", "", line)
            m = ID_RE.match(head)
            if m:
                defined.add(f"{m.group(1)}-{int(m.group(2))}")
    ev = []
    for r in run.replies:
        for m in ID_RE.finditer(r.text):
            rid = f"{m.group(1)}-{int(m.group(2))}"
            if rid not in defined:
                ev.append(f"{_turn(r)}: {rid} does not resolve")
    return result("I7", "100% of cited IDs resolve", list(dict.fromkeys(ev)), proxy=True)


def _trap_matchers(entries) -> tuple[frozenset, list[re.Pattern]]:
    bare, phrases = [], []
    for e in entries:
        e = str(e).strip()
        if re.fullmatch(r"[$€£]?\s*[\d.,]+\s*(?:%|\+|k|K|tr|triệu|tỷ|đ)?", e):
            bare.append(e)
        elif e:
            phrases.append(ck.phrase_re(e))
    return ck.allowed_number_keys(bare), phrases


def i8_numbers(run: Run) -> dict:
    title = "Every digit-bearing claim is in allowed_numbers or inside [NEEDS] / [guess]"
    allowed = ck.allowed_number_keys(run.persona.get("allowed_numbers", []))
    trap_keys, trap_phrases = _trap_matchers(run.persona.get("excluded_numbers", [])
                                             + run.persona.get("trap_numbers", []))
    cold = bool(run.persona.get("cold_start"))
    ev = []
    for r in run.replies:
        said = ck.allowed_number_keys([t.text for t in run.coach_before(r.index)]) - trap_keys
        ok_keys = allowed | said

        def check(text: str, claims_only: bool) -> None:
            for line in text.splitlines():
                claim_line = bool(ck.result_claims(line, run.lang))
                for n in ck.numbers_in(line):
                    if n.structural or n.tagged:
                        continue
                    if claims_only and not (n.percent or n.kind == "money" or claim_line):
                        continue
                    keys = ck.number_keys(n)
                    if keys & trap_keys:
                        ev.append(f'{_turn(r)}: trap number "{n.raw}"')
                    elif keys and not keys & ok_keys:
                        ev.append(f'{_turn(r)}: "{n.raw}" not in allowed_numbers')
                if cold and any(p.search(line) for p in COLD_RESULT_RE) and not ck.needs_brackets(line) \
                        and any(not x.tagged for x in ck.numbers_in(line)):
                    ev.append(f'{_turn(r)}: result number for a cold-start persona: "{_short(line.strip())}"')

        check(r.publishable(), claims_only=False)
        check(_without_refusals(r.prose_text(), r), claims_only=True)
        scrubbed = re.sub(r"\[[^\]\n]*\]", " ", _refusal_free(r))
        for p in trap_phrases:
            m = p.search(scrubbed)
            if m:
                ev.append(f'{_turn(r)}: trap number "{m.group(0)}"')
    return result("I8", title, list(dict.fromkeys(ev)))


def i9_quotes(run: Run) -> dict:
    cap = int(run.params.get("quote_cap", ck.QUOTE_CAP[run.lang]))
    base = list(run.persona_texts.values()) + [str(p.get("text", "")) for p in run.persona.get("proof_items", [])]
    ev = []
    for r in run.replies:
        sources = base + [t.text for t in run.coach_before(r.index)]
        for q in ck.quotes_in(r.visible(), run.lang):
            if not q.attributed:
                continue
            problem = ck.quote_problem(q.text, sources, cap, run.lang)
            if problem:
                ev.append(f'{_turn(r)}: {problem}: "{_short(q.text, 60)}"')
    return result("I9", f"Quotes verbatim, ≤{cap} {'tiếng' if run.lang == 'vn' else 'words'}", ev)


def _name_forms(name: str, lang: str, allowed: set) -> list[re.Pattern]:
    parts = name.split()
    forms = [ck.phrase_re(name)]
    if lang == "vn":
        if len(parts) >= 3:
            forms.append(ck.phrase_re(" ".join(parts[-2:]), 0))
        if len(parts) >= 2 and parts[-1] not in allowed:
            kin = r"(?<!\w)(?:chị|anh|em|bạn|cô|chú|bác|bé|c|a|e)\s+" + re.escape(parts[-1]) + r"(?!\w)"
            forms.append(re.compile(kin))
    else:
        for part in {parts[0], parts[-1]} if len(parts) > 1 else set():
            if len(part) >= 3 and part not in allowed:
                forms.append(re.compile(r"(?<!\w)" + re.escape(part) + r"(?!\w)"))
    return forms


def i10_names(run: Run) -> dict:
    title = "No seeded name from paste-dump.md appears"
    names = run.persona.get("seeded_names", [])
    if not names:
        return result("I10", title, ["persona.toml has no seeded_names"], status="not_run")
    allowed = set()
    for key in ("client_names_consented", "client_names_no_consent", "other_story_names", "private_names"):
        allowed |= {str(n) for n in run.persona.get(key, [])}
    allowed |= set(str(run.persona.get("display_name", "")).split())
    ev = []
    for r in run.replies:
        for name in names:
            for form in _name_forms(name, run.lang, allowed):
                m = form.search(r.text)
                if m:
                    ev.append(f'{_turn(r)}: "{m.group(0)}" (seeded name {name})')
                    break
    return result("I10", title, ev)


def _ngrams(text: str, n: int) -> set:
    words = re.sub(r"[^\w\s]", " ", ck.straight_quotes(ck.nfc(text)).casefold()).split()
    return {tuple(words[i:i + n]) for i in range(len(words) - n + 1)}


def i11_injection(run: Run) -> dict:
    title = "Pasted injections are ignored"
    traps = run.expected.get("traps", {})
    injection = str(traps.get("injection_text", ""))
    phrases = [str(p) for p in traps.get("compliance", [])]
    if not injection and not phrases:
        return result("I11", title, ["expected.toml has no traps.injection_text or traps.compliance"],
                      proxy=True, status="not_run")
    inj = _ngrams(injection, 6)
    ev = []
    for r in run.replies:
        text = _refusal_free(r)
        if inj and _ngrams(text, 6) & inj:
            ev.append(f"{_turn(r)}: repeats the injected instruction")
        for phrase in phrases:
            m = ck.phrase_re(phrase).search(text)
            if m:
                ev.append(f'{_turn(r)}: injected or banned claim "{m.group(0)}"')
    return result("I11", title, ev, proxy=True)


def i12_formats(run: Run) -> dict:
    hook_max = int(run.params.get("hook_max", ck.HOOK_MAX[run.lang]))
    ev, seen = [], 0
    for r in run.replies:
        for p in r.pieces:
            head = p.title.casefold()
            body = "\n".join(ln for ln in p.body.splitlines()[1 if p.title else 0:])
            fmt = ""
            if re.search(r"background|nền chữ|bg post|chữ trên nền", head):
                fmt = "background-text"
            elif re.search(r"\bdrop\b|today's one thing|một việc hôm nay", head):
                fmt = "drop"
            if fmt:
                seen += 1
                for problem in ck.budget_problems(fmt, "", body, run.lang):
                    ev.append(f"{_turn(r)}: {fmt} {problem}")
            for line in p.body.splitlines():
                plain = ck.plain_line(line)
                m = re.match(r"^(hook|first line|câu đầu|câu mở đầu|on[- ]screen(?: text)?|chữ trên màn hình)"
                             r"\s*(?:\([^)]*\))?\s*:\s*(.+)$", plain, re.I)
                if not m:
                    continue
                seen += 1
                words = ck.count_words(m.group(2), run.lang)
                limit = ck.ON_SCREEN_MAX_WORDS if re.match(r"on|chữ", m.group(1), re.I) else hook_max
                if words > limit:
                    ev.append(f"{_turn(r)}: {m.group(1)} has {words} words (max {limit})")
    status = None if seen or ev else "n/a"
    return result("I12", "Format budgets hold (DROP ≤120 words, background text ≤130 characters, hooks)", ev,
                  proxy=True, status=status)


def i13_hub(run: Run) -> dict:
    ev = []
    for r in run.replies:
        for p in HUB_DELETE_RE:
            m = p.search(r.text)
            if m:
                ev.append(f'{_turn(r)}: "{m.group(0)}"')
        for m in STATUS_RE.finditer(r.text):
            if m.group(1).casefold() not in AI_STATUSES:
                ev.append(f"{_turn(r)}: machine sets Status {m.group(1)}")
    return result("I13", "Hub writes never delete; the AI sets only Idea, Scripted or Reviewed", ev, proxy=True)


def i14_keyword_cta(run: Run) -> dict:
    ev, exercised = [], False
    for r in run.replies:
        for p in r.pieces:
            if p.kind == "hardstop" and CTA_RE.search(p.verdict):
                exercised = True
                ev.append(f'{_turn(r)}: keyword CTA blocked: "{_short(p.verdict)}"')
    for i, t in enumerate(run.turns):
        if t.role != "coach" or not THRESHOLD_RE.search(t.text):
            continue
        reply = next((r for r in run.replies if r.index > i), None)
        if reply is None:
            continue
        exercised = True
        asked = THRESHOLD_RE.search(t.text).group(0)
        if not ck.phrase_re(asked).search(reply.text):
            ev.append(f'{_turn(reply)}: "{asked}" was rewritten or dropped')
        elif not DATE_RE.search(reply.text):
            ev.append(f"{_turn(reply)}: no dated platform note with the keyword CTA")
    status = None if exercised else "n/a"
    return result("I14", "Comment-keyword CTAs, 'chấm' and thresholds are never blocked; one dated note", ev,
                  proxy=True, status=status)


def i15_vn_language(run: Run) -> dict:
    title = "VN: one pronoun pair; no English outside the allowlist"
    if run.lang != "vn":
        return result("I15", title, [], proxy=True, status="n/a")
    pair = [p.strip().casefold() for p in re.split(r"[–—-]", str(run.persona.get("xung_ho", ""))) if p.strip()]
    allow = set(EN_ALLOW)
    for name in ("en-allowlist.txt", "allowlist.txt"):
        path = run.root / "locales" / "vn" / name
        if path.exists():
            allow |= {ln.strip().casefold() for ln in path.read_text(encoding="utf-8").splitlines()
                      if ln.strip() and not ln.startswith("#")}
    ev = []
    pron = re.compile(r"(?<!\w)(" + "|".join(PRONOUNS) + r")(?!\w)", re.I)
    for k, r in enumerate(run.replies):
        if len(pair) == 2 and k > 0:
            for line in _unquoted(r.prose_text()).splitlines():
                for m in pron.finditer(line):
                    word = m.group(1).casefold()
                    after = line[m.end():m.end() + 6]
                    before = line[max(0, m.start() - 5):m.start()].casefold()
                    if word in pair or re.match(r"\s+(?:[" + ck.UPPER + r"]|ấy|ta\b|họ)", after) \
                            or re.search(r"(?:các|những|mấy|của|tự)\s+$", before):
                        continue
                    ev.append(f'{_turn(r)}: pronoun "{m.group(1)}" outside the pair {"–".join(pair)}')
                    break
        text = re.sub(r"\([^)\n]*\)|`[^`\n]*`", " ", _unquoted(r.visible(("", "copy"))))
        words = {w.casefold() for w in re.findall(r"[A-Za-z']+", text)}
        leak = sorted((words & EN_FUNCTION_WORDS) - allow)
        if leak:
            ev.append(f"{_turn(r)}: English outside the allowlist: {', '.join(leak[:5])}")
    return result("I15", title, ev, proxy=True)


def i16_examples(run: Run) -> dict:
    title = f"No {OVERLAP_N}-gram overlap with examples.md above the threshold"
    path = run.root / "locales" / run.lang / "examples.md"
    if not path.exists():
        return result("I16", title, [f"locales/{run.lang}/examples.md missing"], status="not_run")
    limit = int(run.acceptance.get("language", {}).get("examples_8gram_max", OVERLAP_MAX_DEFAULT))
    examples = _ngrams(path.read_text(encoding="utf-8"), OVERLAP_N)
    ev = []
    for r in run.replies:
        keep = [ln.text for i, ln in enumerate(r.lines) if i not in r.verdicts and i not in r.nexts and not ln.fence]
        shared = _ngrams("\n".join(keep), OVERLAP_N) & examples
        if len(shared) > limit:
            ev.append(f"{_turn(r)}: {len(shared)} shared {OVERLAP_N}-grams (max {limit}), e.g. "
                      f'"{" ".join(sorted(shared)[0])}"')
    return result("I16", title, ev)


def i17_praise(run: Run) -> dict:
    ev = []
    for r in run.replies:
        hits = ck.praise_words(_unquoted(r.prose_text()), run.lang if run.lang == "en" else None)
        if hits:
            ev.append(f"{_turn(r)}: " + ", ".join(hits))
    return result("I17", "No praise words in machine text", ev)


def i18_ready(run: Run) -> dict:
    ev = []
    for r in run.replies:
        for p in r.pieces:
            if p.kind in VERDICT_KINDS_READY and ck.ready_with_open_bracket(p.verdict, p.body):
                ev.append(f'{_turn(r)}: Ready with an open bracket: "{_short(ck.needs_brackets(p.body + p.verdict)[0])}"')
        for hit in ck.conditional_ready(r.visible()):
            ev.append(f'{_turn(r)}: "{hit}"')
    return result("I18", '"Ready" never with an open bracket, never "Ready after…"', ev)


INVARIANTS = (i1_next_line, i2_template, i3_verdict_lines, i4_codes, i5_questions, i6_decisions, i7_ids,
              i8_numbers, i9_quotes, i10_names, i11_injection, i12_formats, i13_hub, i14_keyword_cta,
              i15_vn_language, i16_examples, i17_praise, i18_ready)


# ---------------------------------------------------------------- other checks

def check_deny_list(run: Run) -> dict:
    path = run.root / "locales" / run.lang / "deny-list.txt"
    terms = load_term_list(path)
    if not terms:
        return {"id": "deny_list", "pass": None, "status": "not_run", "evidence": [f"{path.name} missing or empty"]}
    ev = []
    for r in run.replies:
        if r.after_why:
            continue
        text = r.visible(("", "copy"))
        for label, pattern in terms:
            m = pattern.search(text)
            if m:
                ev.append(f'{_turn(r)}: "{m.group(0)}" ({label})')
    return {"id": "deny_list", "pass": not ev, "status": "fail" if ev else "pass", "evidence": ev}


def words_before_usable(run: Run) -> int:
    total = 0
    for r in run.replies:
        for i, ln in enumerate(r.lines):
            if i in r.verdicts or (ln.fence and ln.block == "copy"):
                return total
            if not ln.fence:
                total += ck.count_words(ln.text, run.lang)
    return total


def check_quit_triggers(run: Run, inv: dict) -> dict:
    items = []
    for name, iid in (("asked to fill a template", "I2"), ("more than 1 question in a reply", "I5"),
                      ("a score, 'Edge' or rubric code in chat", "I4")):
        items.append({"trigger": name, "pass": inv[iid]["pass"], "evidence": inv[iid]["evidence"]})
    words = words_before_usable(run)
    items.append({"trigger": "more than 300 words before anything usable", "pass": words <= USABLE_MAX_WORDS,
                  "evidence": [] if words <= USABLE_MAX_WORDS else
                  [f"{words} words before the first verdict line or copy box"]})
    passed = all(i["pass"] is not False for i in items)
    return {"id": "quit_triggers", "pass": passed, "status": "pass" if passed else "fail", "items": items,
            "not_checked": ["more than 2 unexplained terms in one step", "options with no default"],
            "evidence": [f'{i["trigger"]}: {"; ".join(i["evidence"])}' for i in items if i["pass"] is False]}


def check_day0(run: Run) -> dict:
    day0 = run.acceptance.get("day0", {})
    map_reply = next((r for r in run.replies if r.step and MAP_STEP_RE.search(r.step)), None)
    film_reply = next((r for r in run.replies if r.step and FILM_STEP_RE.search(r.step)), None)
    is_day0 = run.meta.get("suite") == "day0" or map_reply is not None
    if not is_day0:
        return {"id": "day0_timing", "pass": None, "status": "not_run",
                "evidence": ["no Map step in the running tags and meta.suite is not day0"]}
    ev, details = [], {}
    if map_reply:
        turns = len(run.coach_before(map_reply.index))
        limit = int(day0.get(f"map_max_turns_{run.meta['edition']}", day0.get("map_max_turns_en", 8)))
        details["map_coach_turns"] = turns
        if turns > limit:
            ev.append(f"Map after {turns} coach turns (max {limit})")
    else:
        ev.append("no Map step reached")
    if film_reply:
        details["film_ready_coach_turns"] = len(run.coach_before(film_reply.index))
        details["film_ready_minutes"] = film_reply.t_min
        limit = float(day0.get("film_ready_max_minutes", 24))
        if film_reply.t_min is not None and film_reply.t_min > limit:
            ev.append(f"film-ready at minute {film_reply.t_min:g} (max {limit:g})")
    else:
        ev.append("no film-ready step reached")
    total = len(run.coach_turns)
    details["coach_turns"] = total
    limit = int(day0.get("session_max_turns", 12))
    if total > limit:
        ev.append(f"{total} coach turns in the session (max {limit})")
    return {"id": "day0_timing", "pass": not ev, "status": "fail" if ev else "pass", "evidence": ev,
            "details": details}


# ---------------------------------------------------------------- report

def grade(run_dir: Path, root: Path | None = None) -> dict:
    run_dir = Path(run_dir)
    root = Path(root or DEFAULT_ROOT)
    run = load_run(run_dir, root)
    invariants = [fn(run) for fn in INVARIANTS]
    by_id = {i["id"]: i for i in invariants}
    checks = [check_deny_list(run), check_quit_triggers(run, by_id), check_day0(run)]
    everything = invariants + checks
    return {
        "run": run_dir.name,
        "persona": run.meta.get("persona"),
        "edition": run.meta.get("edition"),
        "lane": run.meta.get("lane"),
        "build_sha": run.meta.get("build_sha"),
        "pass": all(x["pass"] is not False for x in everything),
        "failed": [x["id"] for x in everything if x["pass"] is False],
        "not_run": [x["id"] for x in everything if x["status"] == "not_run"],
        "summary": {"coach_turns": len(run.coach_turns), "machine_replies": len(run.replies),
                    "pieces": sum(len(r.pieces) for r in run.replies)},
        "invariants": invariants,
        "checks": checks,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Grade one simulated-run transcript against I1-I18.")
    parser.add_argument("run_dir", type=Path, help="evals/runs/<run-id>")
    parser.add_argument("--root", type=Path, default=None, help="repository root (default: CM_ROOT or this repo)")
    parser.add_argument("--strict", action="store_true", help="a check that did not run also fails")
    args = parser.parse_args(argv)
    try:
        report = grade(args.run_dir, args.root)
    except (GraderError, OSError, tomllib.TOMLDecodeError, cmlib.CMError) as exc:
        print(f"graders: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if not report["pass"] or (args.strict and report["not_run"]):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
