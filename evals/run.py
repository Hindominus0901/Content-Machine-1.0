#!/usr/bin/env python3
"""Simulated runs: build run packets, then grade the transcripts (docs/PLAN.md "How simulated runs work";
evals/README.md "Lanes and simulated runs").

    python3 evals/run.py packet --suite day0 --edition en --lane S1 [--persona ID ...] [--repeat 3] [--tag p2]
    python3 evals/run.py packet --suite cases --edition en --lane S1 --module setup [--case setup.en.004 ...]
    python3 evals/run.py grade evals/runs/<run-id> [...]
    python3 evals/run.py summary evals/runs/<run-id> [...]

No API keys are needed: `packet` writes everything a simulator agent needs into evals/runs/<run-id>/,
the agent writes transcript.jsonl and notes.md there, and `grade` checks the transcript.

Run folder (graders.py reads transcript.jsonl and meta.json; keep both formats):

    meta.json          persona, edition, lane, build_sha, suite, repeat (+ case for the cases suite); "edits":
                       the simulator's log of leak removals after the first grade (turn, field, before, after, reason)
    packet/README.md   the protocol: who plays which side, the leakage rule, what to write back
    packet/MACHINE.md  the machine side: the lane, and the kit files it runs on (in packet/kit/)
    packet/COACH.md    the coach side: the persona files it may use and the suite's script
    packet/kit/        1-INSTRUCTIONS.txt (+ CONTENT-MACHINE-<ED>.md in S1 and floor), as built
    transcript.jsonl   written by the simulator
    transcript.raw.jsonl  the transcript as first graded (written by `grade`; later edits are checked against it)
    notes.md           written by the simulator
    grades.json        written by `grade` (with "edited": the rows changed since the first grade)

Lanes: S0 compact mode (instruction block only, no method file); S1 the Project kit (instruction block +
method file); floor S1 played by a smaller model (the weaker free-tier model); S3 the L3 skill with a fake
hub (needs the skill build, P4).

`grade` runs graders.py (I1-I23 and the other checks) on each run. A cases-suite run also checks its
case's D assertions (contains, regex, not_*, verdict, max_*, invariants) on the reply to the last coach
turn, or on the scope named at the start of the case's notes ("scope: transcript | pieces | visible |
each reply"). A run passes when graders.py passes and, for a case, every assertion holds.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import shutil
import sys
import tomllib
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_ROOT = Path(os.environ.get("CM_ROOT", HERE.parent))
sys.path.insert(0, str(HERE.parent / "tools"))
import cmlib  # noqa: E402
from cmcore import checks as ck  # noqa: E402

_spec = importlib.util.spec_from_file_location("graders", HERE / "graders.py")
graders = importlib.util.module_from_spec(_spec)
sys.modules.setdefault("graders", graders)          # dataclasses resolve annotations through sys.modules
_spec.loader.exec_module(graders)

SUITES = ("day0", "cases")
LANES = {
    "S0": {"method": False, "model": "the session's model",
           "about": "Compact mode: the project holds the instruction block only. The method file is missing, so "
                    "the setup check shows ✗ method file and Day 0 runs from the instruction block alone."},
    "S1": {"method": True, "model": "the session's model",
           "about": "The Project kit: the instruction block is the project's instructions and the method file is "
                    "a project file. Read a §CM- section of the method file only when the instructions say so."},
    "floor": {"method": True, "model": "a smaller model (haiku), standing in for the weaker free-tier model",
              "about": "Same kit as S1, played by a smaller model. Follow the instructions as written; do not "
                       "compensate for what a weaker model would miss."},
    "S3": {"method": False, "model": "the session's model",
           "about": "The L3 skill with a fake hub (P4)."},
}
SCOPES = ("transcript", "pieces", "visible", "each reply", "each")
SCOPE_RE = re.compile(r"^\s*scope:\s*(transcript|pieces|visible|each reply|each)\b", re.I)
TURN_SPLIT_RE = re.compile(r"^\[turn \d+\]\s*", re.M)
CASE_RUN_CHECKS = {"deny_list"}
APP_NAMES = {"chatgpt": "ChatGPT", "claude": "Claude"}
VERDICT_KINDS = {
    "hard stop": {"hardstop"},
    "needs you": {"needs"},
    "draft": {"draft_queued", "draft_fixable"},
    "override": {"override"},
}


class RunError(Exception):
    """A packet cannot be built or a run cannot be graded."""


# ---------------------------------------------------------------- helpers

def nfc(text: str) -> str:
    return unicodedata.normalize("NFC", text)


def rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return str(path)


def load_toml(path: Path) -> dict:
    with open(path, "rb") as fh:
        return tomllib.load(fh)


def persona_app(pdir: Path) -> tuple[str, str]:
    """(app, plan) from persona.toml: the machine side is told its app, never the plan."""
    path = pdir / "persona.toml"
    if not path.exists():
        return "", ""
    data = load_toml(path)
    return str(data.get("app", "")).lower(), str(data.get("plan", ""))


def persona_day0(pdir: Path) -> str:
    """persona.toml day0 ("2026-10-11 20:45"): the persona's story is set on that date, so it wins over --today."""
    path = pdir / "persona.toml"
    return str(load_toml(path).get("day0", "")).strip() if path.exists() else ""


def personas(root: Path, edition: str) -> list[str]:
    base = root / "evals" / "personas" / edition
    return sorted(p.name for p in base.iterdir() if (p / "persona.toml").exists()) if base.is_dir() else []


def load_cases(root: Path, module: str, edition: str) -> list[dict]:
    path = root / "evals" / "cases" / f"{module}.{edition}.toml"
    if not path.exists():
        raise RunError(f"{rel(path, root)} not found")
    return load_toml(path).get("case", [])


def find_case(root: Path, case_id: str) -> dict:
    parts = case_id.split(".")
    if len(parts) < 3:
        raise RunError(f"case id '{case_id}' is not <module>.<edition>.<nnn>")
    for case in load_cases(root, parts[0], parts[1]):
        if case.get("id") == case_id:
            return case
    raise RunError(f"case {case_id} not found in evals/cases/{parts[0]}.{parts[1]}.toml")


def coach_turns(case: dict) -> list[str]:
    """The coach turns in a case's input: "[turn n]" lines separate several turns."""
    text = nfc(str(case.get("input", ""))).strip()
    turns = [t.strip() for t in TURN_SPLIT_RE.split(text)]
    return [t for t in turns if t]


# ---------------------------------------------------------------- packets

def build_kit(root: Path, edition: str) -> tuple[dict[str, Path], str]:
    """Build the edition (tools/build.py) and return its kit files and the build sha."""
    import build as cm_build                         # tools/build.py, on sys.path above
    try:
        manifest = cm_build.build(root, [edition])
    except cmlib.CMError as exc:
        raise RunError(f"build failed: {exc}")
    ed = cmlib.load_edition(edition, root)
    out = root / "dist" / edition
    files = {"instructions": out / "1-INSTRUCTIONS.txt", "method": out / f"CONTENT-MACHINE-{ed.file_suffix}.md",
             "phone": out / "PHONE-STARTER.txt"}
    if not files["instructions"].exists():
        raise RunError(f"the {edition} build has no 1-INSTRUCTIONS.txt (core/{ed.lang}/start-block.md missing?)")
    return files, str(manifest.get("build_sha256", ""))[:12]


def run_id(suite: str, edition: str, persona: str, lane: str, repeat: int, tag: str = "",
           case: str = "") -> str:
    parts = [tag] if tag else []
    parts += [case.replace(".", "_")] if case else [suite, edition, persona]
    return "-".join(parts + [lane, f"r{repeat}"])


PROTOCOL = """# Run packet: {run_id}

One simulator agent plays both sides, turn by turn, from the files in this folder. No API keys, no real account.

- **Machine side:** `MACHINE.md`. It runs on the kit files in `kit/` exactly as written. It may not use any
  persona fact before the coach has said it in the transcript, and it never reads the persona folder,
  `expected.toml`, the eval cases or `qa/`.
- **Coach side:** `COACH.md`. Only facts from the persona files it names, in the persona's style and order.
- Keep the two apart: write each machine reply from the transcript so far and the kit only. `grade` scans
  every machine turn for persona wording the coach never said (the leak check): a leak makes the run invalid.
  Never write "no leaks" in notes.md without a passing leak check.
- Machine turns are frozen after the first grade: it keeps the transcript as `transcript.raw.jsonl`. After that,
  change only the leaked words of a machine turn, and log each change in `meta.json` under `"edits"`:
  `{{"turn": 7, "field": "openers_closers", "before": "…", "after": "…", "reason": "leak: …"}}`. Any other change
  (a coach turn, a time, a rewrite that is not a leak removal) makes the run invalid; `grade` prints "edited: n".

## Write back into this run folder ({run_dir})

1. `transcript.jsonl`: one JSON object per turn, in order:
   `{{"turn": 1, "role": "coach" | "machine", "text": "...", "t_min": 0.5}}`. A coach turn and the machine
   reply to it share the same `turn` number. `t_min` is the modelled minute the turn ends (dictation, typing
   and reading speed plus time away). Optional keys on a coach row: `"away_min": 40` for time away
   before it (a site visit, a plan limit; it does not count as active time), `"quit": true` on the coach's
   quit line (the run then ends on that coach turn), `"third_party": true` when the whole turn is someone
   else's post. Turns alternate coach, machine; every coach turn but a quit gets a reply.
2. `notes.md`: outcome; the step reached and the minute; coach turns; where the machine broke the kit or a
   rule; any persona fact the machine used before the coach said it (a leak), and what you did about it;
   whether this coach comes back tomorrow, and why.
3. Then run: `python3 evals/run.py grade {run_dir}`.

Do not edit the files in `packet/`, or `meta.json` beyond its `"edits"` log.
"""

MACHINE = """# Machine side ({lane})

{about}

- **Model:** {model}.
- **Edition:** {edition}. The app is {app}.
- **Your instructions:** `kit/1-INSTRUCTIONS.txt`, verbatim, as the project's instructions.
{method_line}
- Reply only from these files and the transcript so far. Never use a fact the coach has not said.
- Searching the web is not possible in this run: where the kit says "search if you can", you can't.
- A link the coach sends is never opened here (unopened = unread).
- Today's date: {today}.
- You know which app you run in; you do not know the coach's plan or device until they say it.
"""

COACH_DAY0 = """# Coach side: {persona} ({edition}), Day 0

Persona folder: `{pdir}`. Read `persona.toml` (identity, app, plan and device, behaviour traits, quit
triggers), `answers.md` and `written-posts.md`. Never read `expected.toml` or `voice-samples.md` (they are
answer keys for the graders) and never let them shape a turn.

## Script

1. Open the project chat with exactly: `{start}`.
2. Dictate the three `## Dump chunk` sections of `answers.md` verbatim, in order, one coach turn each, when
   the machine asks for the dump. When the dump prompt invites posts you've written, paste the body of
   `written-posts.md` `## W1` and `## W2` (verbatim, without their headings) as one more turn, after chunk 1
   or 2, the way this coach would. Then say you are done in your own words ("done", "ok that's it"). If the
   machine says the dump is enough, or asks you to wrap up, say done there and skip the chunks not yet
   dictated (the machine then asks only what it is missing).
3. After the dump, answer only what the machine asks, one answer per question, from `## Answer bank`, in
   the persona's style. Say "skip" when the answer bank has nothing and the behaviour fits.
4. Follow `## Behaviour`: impatience, pushback lines word for word when their trigger happens, and quit
   the moment a quit trigger in `persona.toml` or `## Behaviour` happens: write the quit line as the last
   coach turn with `"quit": true`, and stop.
5. Accept the Map with a short OK unless something on it is wrong for this coach, then fix only that line.
6. Stop when the machine has delivered Week 1 and the Brand Card with the save line and NEXT, or when the
   coach quits, or after {max_turns} coach turns.

Time: model `t_min` from dictation (about 130 words a minute), typing (about 30 words a minute on a phone,
40 on a laptop), reading (about 200 words a minute) and the persona's time away (`away_min`). A pasted post
takes about half a minute. Plan limits: if this persona's plan ({plan} on {app}) would hit a message limit
during the run, model it (`away_min` on the coach's next turn) and say so in notes.md.
"""

COACH_CASE = """# Coach side: case {case_id} ({edition})

Persona: {persona_line}

**Title:** {title}

**Context** (the state before the case's input; build it as earlier turns of the transcript, briefly, using
only persona facts and the context's own words, so the machine reaches this state honestly):

{context}

**Input:** the coach's turn(s) for this case, verbatim and in order (a `<<paste: file …>>` marker means: paste
that part of the persona file, verbatim):

{inputs}

Stop after the machine's reply to the last input turn. Never read the case file or its assertions.
"""


def write_packet(root: Path, out_root: Path, rid: str, meta: dict, kit: dict[str, Path], lane: str,
                 coach_md: str, today: str) -> Path:
    run_dir = out_root / rid
    if run_dir.exists():
        raise RunError(f"{rel(run_dir, root)} exists; pass another --tag or remove it")
    (run_dir / "packet" / "kit").mkdir(parents=True)
    spec = LANES[lane]
    shutil.copy2(kit["instructions"], run_dir / "packet" / "kit" / kit["instructions"].name)
    method_line = "- **Method file:** none in this lane (compact mode)."
    if spec["method"]:
        if not kit["method"].exists():
            raise RunError(f"lane {lane} needs {kit['method'].name}, which the build did not produce")
        shutil.copy2(kit["method"], run_dir / "packet" / "kit" / kit["method"].name)
        method_line = f"- **Method file:** `kit/{kit['method'].name}`, a project file."
    ed = cmlib.load_edition(meta["edition"], root)
    app = APP_NAMES.get(meta.get("app", ""), "ChatGPT or Claude") + " (a Project)"
    files = {
        "README.md": PROTOCOL.format(run_id=rid, run_dir=rel(run_dir, root)),
        "MACHINE.md": MACHINE.format(lane=lane, about=spec["about"], model=spec["model"], edition=ed.id, app=app,
                                     method_line=method_line, today=today),
        "COACH.md": coach_md,
    }
    for name, text in files.items():
        (run_dir / "packet" / name).write_text(nfc(text), encoding="utf-8")
    (run_dir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return run_dir


def make_packets(root: Path, suite: str, edition: str, lane: str, persona_ids: list[str], repeat: int = 1,
                 tag: str = "", module: str = "", case_ids: list[str] | None = None,
                 out_root: Path | None = None, today: str = "",
                 kit: tuple[dict[str, Path], str] | None = None) -> list[Path]:
    """Write one packet per persona (day0) or per D case (cases), times `repeat`. `kit` is (files, sha) from
    build_kit; tests pass prebuilt files."""
    if suite not in SUITES:
        raise RunError(f"unknown suite '{suite}' ({', '.join(SUITES)})")
    if lane not in LANES:
        raise RunError(f"unknown lane '{lane}' ({', '.join(LANES)})")
    if lane == "S3":
        raise RunError("lane S3 needs the L3 skill build and the fake hub (P4); not available yet")
    out_root = out_root or root / "evals" / "runs"
    kit, sha = kit or build_kit(root, edition)
    strings = graders.load_strings(root, edition)[0]
    known = personas(root, edition)
    made = []
    if suite == "day0":
        chosen = known if persona_ids in ([], ["all"]) else persona_ids
        for pid in chosen:
            if pid not in known:
                raise RunError(f"persona '{pid}' not found under evals/personas/{edition}/")
            pdir = root / "evals" / "personas" / edition / pid
            accept = load_toml(root / "evals" / "acceptance.toml").get("day0", {})
            app, plan = persona_app(pdir)
            coach = COACH_DAY0.format(persona=pid, edition=edition, pdir=rel(pdir, root),
                                      start=strings.get("cmd.start", "Start"),
                                      max_turns=int(accept.get("session_max_turns", 10)) + 4,
                                      app=APP_NAMES.get(app, app or "the app"), plan=plan or "unknown plan")
            for n in range(1, repeat + 1):
                rid = run_id(suite, edition, pid, lane, n, tag)
                meta = {"persona": f"{edition}/{pid}", "edition": edition, "lane": lane, "build_sha": sha,
                        "suite": suite, "repeat": n, **({"app": app} if app else {})}
                made.append(write_packet(root, out_root, rid, meta, kit, lane, coach, persona_day0(pdir) or today))
        return made
    if not module:
        raise RunError("the cases suite needs --module")
    cases = load_cases(root, module, edition)
    if case_ids:
        missing = set(case_ids) - {c.get("id") for c in cases}
        if missing:
            raise RunError("case(s) not found: " + ", ".join(sorted(missing)))
        cases = [c for c in cases if c.get("id") in case_ids]
    for case in cases:
        if case.get("kind", "D") != "D" or (case.get("lanes") and lane not in case.get("lanes", [])):
            continue
        pid = case.get("persona", "")
        if pid and pid not in known:
            raise RunError(f"{case['id']}: persona '{pid}' not found under evals/personas/{edition}/")
        persona_line = (f"`{rel(root / 'evals' / 'personas' / edition / pid, root)}` (persona.toml, answers.md, "
                        f"written-posts.md and the paste files; never expected.toml or voice-samples.md)"
                        if pid else "none (a standalone case)")
        app = persona_app(root / "evals" / "personas" / edition / pid)[0] if pid else ""
        inputs = "\n\n".join(f"Turn {i}:\n\n```text\n{t}\n```" for i, t in enumerate(coach_turns(case), 1))
        coach = COACH_CASE.format(case_id=case["id"], edition=edition, persona_line=persona_line,
                                  title=case.get("title", ""), context=case.get("context", "") or "none",
                                  inputs=inputs or "(none)")
        for n in range(1, repeat + 1):
            rid = run_id(suite, edition, pid, lane, n, tag, case=case["id"])
            meta = {"persona": f"{edition}/{pid}" if pid else "", "edition": edition, "lane": lane,
                    "build_sha": sha, "suite": suite, "repeat": n, "case": case["id"], **({"app": app} if app else {})}
            made.append(write_packet(root, out_root, rid, meta, kit, lane, coach, today))
    if not made:
        raise RunError(f"no D cases of {module}.{edition} run on lane {lane}")
    return made


# ---------------------------------------------------------------- case assertions

def case_scope(case: dict) -> str:
    m = SCOPE_RE.match(str(case.get("notes", "")))
    if not m:
        return "reply"
    scope = m.group(1).lower()
    return "each" if scope.startswith("each") else scope


def _texts(run, scope: str) -> list[str]:
    replies = run.replies
    if not replies:
        return []
    last = replies[-1]
    if scope == "transcript":
        return ["\n\n".join(r.text for r in replies)]
    if scope == "each":
        return [r.text for r in replies]
    if scope == "pieces":
        return ["\n\n".join(p.body for p in last.pieces)]
    if scope == "visible":
        return [last.visible()]
    return [last.text]


def _status_kinds(run, reply) -> set[str]:
    return {k for i in range(len(reply.lines)) for k in [graders._status_kind(reply, i, run.matcher)] if k}


def check_verdict(run, want: str) -> tuple[bool | None, str]:
    """The case's verdict field against the last reply's status lines (wf15 §2: Ready prints nothing)."""
    w = want.strip().lower()
    if not w or not run.replies:
        return None, ""
    r = run.replies[-1]
    kinds = _status_kinds(run, r)
    if w in ("ready", "ready-downgraded"):
        if r.after_check or r.after_why:
            ok = bool(kinds & graders.STATUS_READY)
            return ok, "" if ok else f"no Ready line after the coach's check (found {sorted(kinds) or 'none'})"
        bad = kinds & (graders.STATUS_READY | graders.STATUS_DRAFT | {"why"})
        return not bad, "" if not bad else f"a Ready piece printed {sorted(bad)}"
    if w == "override":
        cmd = run.strings.get("cmd.post_anyway", "post anyway").casefold()
        last_coach = next((t.text for t in reversed(run.turns) if t.role == "coach"), "")
        if cmd and cmd in nfc(last_coach).casefold():
            ok = "override" in kinds
            return ok, "" if ok else "no override line after 'post anyway'"
        return None, "hidden state (an F1 request logs the Override; its one note is asserted by the case)"
    wanted = VERDICT_KINDS.get(w)
    if wanted is None:
        return None, f"unknown verdict '{want}'"
    ok = bool(kinds & wanted)
    return ok, "" if ok else f"no {want} line (found {sorted(kinds) or 'none'})"


def check_case(case: dict, run, report: dict | None = None) -> dict:
    """Every D assertion of the case on the run's transcript. Returns {"pass", "failures", "skipped"}."""
    failures, skipped = [], []
    if case.get("kind", "D") != "D":
        return {"id": case.get("id"), "pass": None, "failures": [], "skipped": ["P case: scored by the judge"]}
    if not run.replies:
        return {"id": case.get("id"), "pass": False, "failures": ["no machine reply"], "skipped": []}
    scope = case_scope(case)
    texts = [nfc(t) for t in _texts(run, scope)]
    every = scope == "each"

    def some(pred) -> bool:
        return any(pred(t) for t in texts)

    def all_(pred) -> bool:
        return all(pred(t) for t in texts)

    for item in case.get("contains", []):
        needle = nfc(item).casefold()
        if not some(lambda t: needle in t.casefold()):
            failures.append(f'contains "{item}": missing')
    for item in case.get("not_contains", []):
        needle = nfc(item).casefold()
        if not all_(lambda t: needle not in t.casefold()):
            failures.append(f'not_contains "{item}": present')
    for pat in case.get("regex", []):
        try:
            rx = re.compile(pat)
        except re.error as exc:
            failures.append(f"regex /{pat}/ does not compile: {exc}")
            continue
        if not some(lambda t: rx.search(t) is not None):
            failures.append(f"regex /{pat}/: no match")
    for pat in case.get("not_regex", []):
        try:
            rx = re.compile(pat)
        except re.error as exc:
            failures.append(f"not_regex /{pat}/ does not compile: {exc}")
            continue
        hit = next((m for t in texts for m in [rx.search(t)] if m), None)
        if hit:
            failures.append(f'not_regex /{pat}/: matched "{hit.group(0)[:60]}"')

    replies = run.replies if every else run.replies[-1:]
    for r in replies:
        visible = r.visible()
        words = ck.count_words(visible, run.lang)
        if case.get("max_words") and words > int(case["max_words"]):
            failures.append(f"turn {r.turn}: {words} words (max {case['max_words']})")
        if case.get("max_chars") and len(visible) > int(case["max_chars"]):
            failures.append(f"turn {r.turn}: {len(visible)} characters (max {case['max_chars']})")
        q = len(graders.reply_questions(r))
        if case.get("max_questions") and q > int(case["max_questions"]):
            failures.append(f"turn {r.turn}: {q} questions (max {case['max_questions']})")

    ok, why = check_verdict(run, str(case.get("verdict", "")))
    if ok is False:
        failures.append(f"verdict {case['verdict']}: {why}")
    elif ok is None and why:
        skipped.append(f"verdict {case['verdict']}: {why}")

    if report is not None:
        by_id = {i["id"]: i for i in report.get("invariants", [])}
        for iid in case.get("invariants", []):
            inv = by_id.get(iid)
            if inv is None:
                skipped.append(f"{iid}: not a graders.py invariant")
            elif inv["pass"] is False:
                failures.append(f"{iid} failed: " + "; ".join(inv.get("evidence", [])[:3]))
            elif inv["pass"] is None:
                skipped.append(f"{iid}: {inv.get('status', 'not_run')}")
    return {"id": case.get("id"), "scope": scope, "pass": not failures, "failures": failures, "skipped": skipped}


# ---------------------------------------------------------------- run protocol (is the run itself valid?)

WORD_RE = re.compile(r"[^\W_]+(?:['’][^\W_]+)*")
DICTATION_MAX_WPM = 160          # 130 wpm modelled, with slack
LEAK_N = {"en": 6, "vn": 8}      # words / tiếng in a run shared with the persona files


NUMBER_WORDS = set("""zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen
sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred thousand million
k grand percent một hai ba bốn năm sáu bảy tám chín mười mươi trăm nghìn ngàn triệu tỷ tỉ""".split())


def _words(text: str) -> list[str]:
    return [w.casefold() for w in WORD_RE.findall(nfc(text))]


def _content_words(text: str) -> list[str]:
    """Words with numbers dropped: "63" and "sixty-three" are the same fact said two ways."""
    return [w for w in _words(text) if not w.isdigit() and w not in NUMBER_WORDS]


def _grams(words: list[str], n: int) -> set[str]:
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def _rows(run_dir: Path) -> list[dict]:
    path = run_dir / "transcript.jsonl"
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _protocol(cid: str, ev: list[str], **extra) -> dict:
    return {"id": cid, "pass": not ev, "status": "fail" if ev else "pass", "evidence": ev, **extra}


def check_turns(rows: list[dict]) -> dict:
    """Coach and machine alternate from a coach turn; every coach turn but a quit gets a reply."""
    ev = []
    if rows and rows[0].get("role") != "coach":
        ev.append("the transcript starts with a machine turn")
    for a, b in zip(rows, rows[1:]):
        if a.get("quit"):
            ev.append(f"turn {b.get('turn')}: a turn after the coach quit")
        elif a.get("role") == b.get("role"):
            ev.append(f"turn {b.get('turn')}: two {a.get('role')} turns in a row")
    if rows and rows[-1].get("role") == "coach" and not rows[-1].get("quit"):
        ev.append("the last coach turn has no reply and no \"quit\": true")
    return _protocol("turns", ev)


def _dump_runs(pdir: Path, n: int = 12) -> set[str]:
    path = pdir / "answers.md"
    if not path.exists():
        return set()
    text = path.read_text(encoding="utf-8")
    chunks = re.findall(r"^## Dump chunk[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return set().union(*(_grams(_words(c), n) for c in chunks)) if chunks else set()


def check_pace(rows: list[dict], pdir: Path) -> dict:
    """A dictated dump chunk takes at least words / 160 minutes of active time (t_min minus away_min)."""
    dump = _dump_runs(pdir)
    ev, prev = [], None
    for r in rows:
        t = r.get("t_min")
        if r.get("role") == "coach" and dump and t is not None and prev is not None:
            words = _words(r.get("text", ""))
            if _grams(words, 12) & dump:
                active = float(t) - float(prev) - float(r.get("away_min") or 0)
                need = len(words) / DICTATION_MAX_WPM
                if active < need:
                    ev.append(f"turn {r.get('turn')}: {len(words)} dictated words in {active:.1f} min "
                              f"(needs ≥{need:.1f} at {DICTATION_MAX_WPM} wpm)")
        if t is not None:
            prev = t
    return _protocol("pace", ev)


VOICE_FIELD_RE = re.compile(r"^\W*(?:tone|rhythm|phrases?|openers?(?:_closers)?|closers|never_say|do_say|passages|"
                            r"audience_address|address_1to1|connectors|written_vs_spoken|code_mix|humou?r|dialect)\b",
                            re.I)
# A machine field's label ("openers_closers: ", "plan_start=", "list_size: ") is the card's wording, never the
# persona's: it is cut before the leak scan, so "openers closers" never joins a value (review G18).
FIELD_LABEL_RE = re.compile(r"^[\W_]*[a-z][a-z0-9_]*\s*(?:=|:(?=\s|$))"            # "openers_closers: …" at the start
                            r"|(?:(?<=\s)|(?<=\|)|(?<=\[))[a-z][a-z0-9]*(?:_[a-z0-9]+)+\s*(?:=|:(?=\s|$))"   # "plan_start="
                            r"|(?:(?<=\s)|(?<=\|))[a-z][a-z0-9]*=")                    # "season=1"
LIST_SPLIT_RE = re.compile(r"\s+[|·]\s+")
# A machine line's list items: " | ", " · ", and a bracketed list's quoted items ('["Okay. Here's the math.", "…"]').
ITEM_SPLIT_RE = re.compile(r"\s+[|·]\s+|\"\s*,\s*\"|\[\s*\"|\"\s*\]")


def _toml_strings(value) -> list[str]:
    """Every string value in a parsed TOML document, one per string (keys and array brackets left out)."""
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        return [s for v in value.values() for s in _toml_strings(v)]
    if isinstance(value, list):
        return [s for v in value for s in _toml_strings(v)]
    return []


# A whole persona phrase this long (EN words / VN tiếng), copied as a list item, is a leak however short; a form of
# address ("audience_address: chị – các em") is an inference from a closed set, never counted this way.
LEAK_ITEM_MIN = {"en": 3, "vn": 5}
ADDRESS_FIELD_RE = re.compile(r"^\W*(?:audience_address|address_1to1|pronouns|xung_ho)\b", re.I)
MD_ITEM_RE = re.compile(r"^\s*(?:[-*•]|\d{1,2}[.)])\s+(.+)$", re.M)


def _persona_values(pdir: Path) -> list[str]:
    """The persona's phrases as written: every TOML string value, each list item (" | ", " · ") apart."""
    out = []
    for f in sorted(pdir.glob("*.toml")):
        text = f.read_text(encoding="utf-8")
        try:
            values = _toml_strings(tomllib.loads(text))
        except tomllib.TOMLDecodeError:
            values = text.splitlines()
        out += [item for value in values for item in LIST_SPLIT_RE.split(value)]
    return out


def leak_corpus(pdir: Path, n: int) -> set[str]:
    """The persona's wording as n-grams: Markdown files whole, TOML files one string value at a time and each list item
    (" | ", " · ") apart, so a key never joins its value and two values never join (review G18)."""
    corpus: set[str] = set()
    for f in sorted(pdir.glob("*.md")):
        corpus |= _grams(_content_words(f.read_text(encoding="utf-8")), n)
    for item in _persona_values(pdir):
        corpus |= _grams(_content_words(item), n)
    return corpus


def leak_items(pdir: Path, lang: str = "en") -> set[str]:
    """Whole persona phrases of LEAK_ITEM_MIN+ words (a TOML value or list item, a Markdown bullet): a machine list item
    that is one of them word for word copied it, even when it is shorter than a leak n-gram ("Okay. Here's the
    math.")."""
    items = _persona_values(pdir)
    for f in sorted(pdir.glob("*.md")):
        items += [m.group(1) for m in MD_ITEM_RE.finditer(f.read_text(encoding="utf-8"))]
    least = LEAK_ITEM_MIN.get(lang, 3)
    return {" ".join(w) for w in (_content_words(i) for i in items) if len(w) >= least}


# The visible voice lines (strings): the card top's HOW YOU SAY IT and the Map's YOUR VOICE are Voice Card lines too.
VOICE_LINE_KEYS = ("card.visible.how", "map.voice")


def voice_labels(root: Path, edition: str) -> tuple[str, ...]:
    """The rendered labels of the visible voice lines (VOICE_LINE_KEYS), folded for a prefix match."""
    try:
        strings, _ = graders.load_strings(root, edition)
    except Exception:                                  # a repo without strings: field lines only
        return ()
    out = []
    for key in VOICE_LINE_KEYS:
        label = nfc(str(strings.get(key, ""))).strip().rstrip(":").strip().casefold()
        if label:
            out.append(label)
    return tuple(out)


def _visible_voice_line(line: str, labels: tuple[str, ...]) -> bool:
    """A visible voice line (voice_labels): 'GIỌNG: thẳng · kể dài · hay nói "…"', 'HOW YOU SAY IT: …'."""
    head = re.sub(r"^[\s#>*_`-]+", "", nfc(line)).casefold()
    return any(head.startswith(label) for label in labels)


def check_leaks(rows: list[dict], pdir: Path, kit_dir: Path | None, lang: str,
                labels: tuple[str, ...] = ()) -> dict:
    """Persona wording in a machine turn that the coach never said before it and the kit does not hold:
    the simulator's machine side read the persona files (README "Keep the two apart"). A hit in a Voice
    Card line (a voice field, or the visible HOW YOU SAY IT / YOUR VOICE line, read one quote apart from its label) fails the run (it inflates I23 and the voice judging); other hits are listed for a
    human read ("warn"), since a model can rebuild a coach's phrase from what they said. A machine line is read
    without its field labels and one list item at a time (leak_corpus reads the persona's TOML the same way); a list
    item that is a whole persona phrase the coach never said leaks however short it is (leak_items)."""
    n = LEAK_N.get(lang, 6)
    corpus, whole = leak_corpus(pdir, n), leak_items(pdir, lang)
    # a run whose first or last n-1 words the coach said, or the kit holds, is a restatement, not a leak
    known: set[str] = set()
    said = " "                                    # the coach's words so far, for whole-item matches
    if kit_dir and kit_dir.is_dir():
        for f in sorted(kit_dir.glob("*")):
            known |= _grams(_content_words(f.read_text(encoding="utf-8")), n - 1)
            said += " ".join(_content_words(f.read_text(encoding="utf-8"))) + " | "
    fails, warns = [], []
    for r in rows:
        if r.get("role") == "coach":
            known |= _grams(_content_words(r.get("text", "")), n - 1)
            said += " ".join(_content_words(r.get("text", ""))) + " | "
            continue
        for line in r.get("text", "").splitlines():
            visible = _visible_voice_line(line, labels)
            voice = visible or bool(VOICE_FIELD_RE.match(line))
            items = ITEM_SPLIT_RE.split(FIELD_LABEL_RE.sub(" ", line))
            if visible:                              # the kit's 'hay nói "{câu}"' never joins the coach's quote
                items = [part for item in items for part in re.split(r"[\"“”]", item)]
            for item in items:
                words = _content_words(item)
                phrase = " ".join(words)
                if len(words) < n and phrase in whole and f" {phrase} " not in said and not ADDRESS_FIELD_RE.match(line) \
                        and not visible:                 # a visible line's short parts (an address form): n-grams only
                    (fails if voice else warns).append(f'turn {r.get("turn")}: "{phrase}"')
                    continue

                def leaked(i: int) -> bool:
                    g = words[i:i + n]
                    return (" ".join(g) in corpus and " ".join(g[:-1]) not in known
                            and " ".join(g[1:]) not in known)

                hit = [i for i in range(len(words) - n + 1) if leaked(i)]
                spans, start, end = [], None, -1
                for i in hit:                          # merge overlapping n-gram hits into spans
                    if start is None or i > end:
                        if start is not None:
                            spans.append((start, end))
                        start = i
                    end = i + n
                if start is not None:
                    spans.append((start, end))
                for a, b in spans:
                    entry = f'turn {r.get("turn")}: "{" ".join(words[a:b])}"'
                    (fails if voice else warns).append(entry)
    out = _protocol("leaks", fails, n=n, warnings=warns)
    if not fails and warns:
        out["status"] = "warn"
    return out


RAW_TRANSCRIPT = "transcript.raw.jsonl"
EDIT_KEYS = ("turn", "field", "before", "after", "reason")


def freeze_transcript(run_dir: Path) -> bool:
    """The first grade keeps the transcript as written (transcript.raw.jsonl); later grades compare against it (review
    P8). True when this call froze it."""
    raw = run_dir / RAW_TRANSCRIPT
    if raw.exists() or not (run_dir / "transcript.jsonl").exists():
        return False
    shutil.copy2(run_dir / "transcript.jsonl", raw)
    return True


def check_edits(run_dir: Path, meta: dict) -> dict:
    """Machine turns are frozen after the first grade (review P8): every row that differs from transcript.raw.jsonl
    is an edit. Only a machine turn's text may change, only to remove a leak, and each change needs an entry in
    meta.json "edits" ({"turn", "field", "before", "after", "reason": "leak: …"}) whose "before" is in the frozen
    text and whose "after" is in the edited text, and the logged changes are the whole change: replaying them on the
    frozen text (each "before" → "after", in log order) gives the edited text. Rows added after the last frozen row
    are new turns, not edits. details: edited (rows changed), appended (rows added)."""
    raw_path = run_dir / RAW_TRANSCRIPT
    if not raw_path.exists():
        return _protocol("edits", [], edited=0, appended=0)
    raw = [json.loads(line) for line in raw_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    cur = _rows(run_dir)
    log = [e for e in meta.get("edits", []) if isinstance(e, dict)]
    ev, edited = [], 0
    for i, old in enumerate(raw):
        new = cur[i] if i < len(cur) else None
        if new == old:
            continue
        edited += 1
        turn = old.get("turn")
        if new is None:
            ev.append(f"turn {turn}: a {old.get('role')} row was removed after the first grade")
            continue
        if old.get("role") != "machine" or {k: v for k, v in old.items() if k != "text"} \
                != {k: v for k, v in new.items() if k != "text"}:
            ev.append(f"turn {turn}: a {old.get('role')} row changed after the first grade (only a machine turn's "
                      "text may change, to remove a leak)")
            continue
        entries = [e for e in log if e.get("turn") == turn]
        if not entries:
            ev.append(f'turn {turn}: machine turn edited after the first grade with no entry in meta.json "edits"')
            continue
        replay, logged_ok = old.get("text", ""), True
        for e in entries:
            missing = [k for k in EDIT_KEYS if k not in e]
            if missing:
                ev.append(f"turn {turn}: the edit log entry lacks {', '.join(missing)}")
            elif not str(e["reason"]).strip().casefold().startswith("leak"):
                ev.append(f'turn {turn}: an edit that is not a leak removal ("{e["reason"]}")')
            elif str(e["before"]) not in old.get("text", "") or str(e["after"]) not in new.get("text", ""):
                ev.append(f"turn {turn}: the edit log's before/after does not match the frozen and edited text")
            else:
                replay = replay.replace(str(e["before"]), str(e["after"]), 1)
                continue
            logged_ok = False
        if logged_ok and replay != new.get("text", ""):
            ev.append(f"turn {turn}: the machine turn changed beyond its logged edits (replaying \"before\" → "
                      "\"after\" on the frozen text does not give the edited text)")
    for e in log:
        if e.get("turn") not in {r.get("turn") for r, c in zip(raw, cur) if r != c}:
            ev.append(f"turn {e.get('turn')}: an edit log entry for a turn that did not change")
    return _protocol("edits", list(dict.fromkeys(ev)), edited=edited, appended=max(0, len(cur) - len(raw)))


def protocol_checks(run_dir: Path, root: Path, meta: dict) -> list[dict]:
    rows = _rows(run_dir)
    lang = "vn" if meta.get("edition") == "vn" else "en"
    pdir = root / "evals" / "personas" / meta["persona"]
    labels = voice_labels(root, meta.get("edition", lang))
    return [check_turns(rows), check_pace(rows, pdir),
            check_leaks(rows, pdir, run_dir / "packet" / "kit", lang, labels), check_edits(run_dir, meta)]


# ---------------------------------------------------------------- grading

def grade_run(run_dir: Path, root: Path) -> dict:
    run_dir = Path(run_dir)
    meta_path = run_dir / "meta.json"
    if not meta_path.exists():
        raise RunError(f"{run_dir}: meta.json missing")
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    if not meta.get("persona") and meta.get("case"):
        raise RunError(f"{run_dir.name}: standalone cases (no persona) cannot be graded by graders.py yet")
    report = graders.grade(run_dir, root)
    out = dict(report)
    freeze_transcript(run_dir)
    out["protocol"] = protocol_checks(run_dir, root, meta) if meta.get("persona") else []
    edits = next((p for p in out["protocol"] if p["id"] == "edits"), None)
    out["edited"] = edits["edited"] if edits else 0
    out["valid"] = all(p["pass"] for p in out["protocol"])
    out["pass"] = bool(report["pass"]) and out["valid"]
    if meta.get("case"):
        # a case run is a slice of a session: the session checks (day0_timing, quit_triggers) are reported,
        # not counted; every invariant and the deny list still count
        run = graders.load_run(run_dir, root)
        out["case"] = check_case(find_case(root, meta["case"]), run, report)
        counted = report["invariants"] + [c for c in report["checks"] if c["id"] in CASE_RUN_CHECKS]
        out["failed"] = [x["id"] for x in counted if x["pass"] is False]
        out["info_failed"] = [c["id"] for c in report["checks"]
                              if c["id"] not in CASE_RUN_CHECKS and c["pass"] is False]
        out["pass"] = not out["failed"] and out["case"]["pass"] is not False and out["valid"]
    (run_dir / "grades.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return out


def film_cell(d: dict) -> str:
    """Film-ready minutes for the summary: active minutes (the budget's unit), the clock in brackets when the coach
    was away ("16.1 (56.1)"; review G16, VG-16)."""
    active, clock = d.get("film_ready_active_minutes"), d.get("film_ready_minutes")
    if active is None:
        return "–" if clock is None else f"{clock:g}"
    return f"{active:g}" if clock is None or abs(clock - active) < 0.05 else f"{active:g} ({clock:g})"


def summary_rows(results: list[dict]) -> str:
    head = ("| Run | Persona | Lane | Valid | Pass | Failed | Coach turns | Map turns | Film-ready min (clock) | "
            "Case |")
    rows = [head, "|" + "---|" * 10]
    for g in results:
        day0 = next((c for c in g.get("checks", []) if c["id"] == "day0_timing"), {})
        d = day0.get("details", {})
        case = g.get("case", {})
        case_cell = ""
        if case:
            case_cell = "pass" if case.get("pass") else ("P" if case.get("pass") is None else
                                                          "fail: " + "; ".join(case.get("failures", [])[:2]))
        bad = [p["id"] for p in g.get("protocol", []) if not p["pass"]]
        valid = "no: " + ", ".join(bad) if bad else "yes"
        if g.get("edited"):
            valid += f" (edited: {g['edited']})"
        rows.append("| {run} | {persona} | {lane} | {valid} | {ok} | {failed} | {turns} | {map} | {film} | {case} |".format(
            run=g.get("run", ""), persona=g.get("persona", ""), lane=g.get("lane", ""), valid=valid,
            ok="yes" if g.get("pass") else "no", failed=", ".join(g.get("failed", [])) or "–",
            turns=g.get("summary", {}).get("coach_turns", ""), map=d.get("map_coach_turns", "–"),
            film=film_cell(d), case=case_cell.replace("|", "/")))
    return "\n".join(rows)


# ---------------------------------------------------------------- CLI

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Build simulated-run packets and grade transcripts.")
    ap.add_argument("--root", type=Path, default=None, help="repository root (default: CM_ROOT or this repo)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("packet", help="write run packets under evals/runs/")
    p.add_argument("--suite", required=True, choices=SUITES)
    p.add_argument("--edition", required=True, choices=list(cmlib.EDITIONS))
    p.add_argument("--lane", required=True, choices=list(LANES))
    p.add_argument("--persona", action="append", default=[], help="persona id; repeatable; default all (day0)")
    p.add_argument("--module", default="", help="cases suite: the module whose D cases to run")
    p.add_argument("--case", action="append", default=[], help="cases suite: only these case ids; repeatable")
    p.add_argument("--repeat", type=int, default=1, help="runs per persona or case (G2 uses 3)")
    p.add_argument("--tag", default="", help="prefix for the run ids (e.g. a round name)")
    p.add_argument("--out", type=Path, default=None, help="folder for the runs (default evals/runs)")
    p.add_argument("--today", default="", help="the date the machine side is told (YYYY-MM-DD)")
    g = sub.add_parser("grade", help="grade run folders; writes grades.json in each")
    g.add_argument("runs", nargs="+", type=Path)
    s = sub.add_parser("summary", help="a markdown table of graded runs (grades them first if needed)")
    s.add_argument("runs", nargs="+", type=Path)
    args = ap.parse_args(argv)
    root = (args.root or DEFAULT_ROOT).resolve()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    try:
        if args.cmd == "packet":
            if args.repeat < 1:
                raise RunError("--repeat must be at least 1")
            made = make_packets(root, args.suite, args.edition, args.lane, args.persona, args.repeat, args.tag,
                                args.module, args.case, args.out, args.today or "the date in the transcript")
            for d in made:
                print(rel(d, root))
            return 0
        results = []
        for d in args.runs:
            if args.cmd == "summary" and (d / "grades.json").exists():
                results.append(json.loads((d / "grades.json").read_text(encoding="utf-8")))
            else:
                results.append(grade_run(d, root))
        if args.cmd == "summary":
            print(summary_rows(results))
        else:
            for r in results:
                case = r.get("case")
                extra = ""
                if case and case.get("pass") is False:
                    extra = " · case: " + "; ".join(case["failures"][:3])
                bad = [p["id"] for p in r.get("protocol", []) if not p["pass"]]
                status = "pass" if r["pass"] else "FAIL " + (", ".join(r["failed"] + [f"invalid run: {b}" for b in bad])
                                                             or "case")
                print(f"{r['run']}: {status}{extra} · edited: {r.get('edited', 0)}")
        return 0 if all(r.get("pass") for r in results) else 1
    except (RunError, graders.GraderError, cmlib.CMError, OSError, tomllib.TOMLDecodeError,
            json.JSONDecodeError) as exc:
        print(f"run: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
