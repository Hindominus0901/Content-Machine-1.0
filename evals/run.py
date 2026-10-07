#!/usr/bin/env python3
"""Simulated runs: build run packets, then grade the transcripts (docs/PLAN.md "How simulated runs work";
evals/README.md "Lanes and simulated runs").

    python3 evals/run.py packet --suite day0 --edition en --lane S1 [--persona ID ...] [--repeat 3] [--tag p2] [--web] [--plugin]
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

Lane options (flags of `packet`, kept in meta.json and shown as "S1+web" in the summary; review retest-ft1 fix 5):
  --web     the machine side may use web search and page fetch for the background research pass (§CM-LISTEN).
            Without it MACHINE.md says searching is not possible, as before. With it MACHINE.md names the pass,
            the read-only rules (open a page before quoting it; roles, never names; never log in, post, react,
            follow, DM or join; never the coach's computer) and asks for a "## Research log" in notes.md
            (every query, every page opened, what was kept) for the reviewer to re-fetch. A link the coach sends is
            still never opened here (I20). The run id gets "-web" (…-S1-web-r1). Stands in for the coach's own
            browser or search tool (Claude in Chrome, ChatGPT Work); without it a run ends with 0 KEEP lines. The pass is
            run as if by a separate agent that sees only the transcript up to the turn it runs after (never the persona
            files), and each query is logged with the turn it really ran after ("Q6 · after turn 3 · …"); `grade` adds
            the protocol check research_leaks (a run of 2+ content words in a query that only the persona's answer bank
            holds invalidates the run; retest-ft2 fix 4) and graders.py checks the log itself (research_log).
  --plugin  the coach installed the plugin form: packet/kit/plugin/ holds the edition's skills (the main skill and
            its companion skills, one per level-up area: SKILL.md) and the plugin's agents, read from
            dist/content-machine-plugin.zip. The run id gets "-plugin".
Every lane with a method file (S1, floor) also ships the edition's Level-ups/*.md in packet/kit/Level-ups/, as the
coach's Project or Cowork folder holds them (the method file and the instructions point to them: RESEARCH-<ED>.md,
STRATEGY-<ED>.md, LAUNCH-<ED>.md, BOARD-<ED>.md); S0 (instruction block only) ships none.

`grade` runs graders.py (I1-I23 and the other checks) on each run. A cases-suite run also checks its
case's D assertions (contains, regex, not_*, verdict, max_*, invariants) on the reply to the last coach
turn, or on the scope named at the start of the case's notes ("scope: transcript | pieces | visible |
each reply"). A run passes when graders.py passes and, for a case, every assertion holds.
"""
from __future__ import annotations

import argparse
import datetime
import importlib.util
import json
import os
import re
import shutil
import sys
import tomllib
import unicodedata
import zipfile
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


WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December")


def run_date(value: str = "") -> str:
    """The date MACHINE.md gives the machine side: "Tuesday 6 October 2026" from "2026-10-06" (a persona day0 time stays:
    "2026-10-12 06:45" → "Monday 12 October 2026, 06:45"); no value is the day the packet is made. Always a real date,
    never "the date in the transcript" (no transcript row carries one, so each simulator invented its own; review
    retest-vg6-g7 P18). A value that is not YYYY-MM-DD[ HH:MM] is passed through as given."""
    text = value.strip()
    m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})(?:[ T](\d{1,2}:\d{2}))?", text)
    day = None
    if not text:
        day = datetime.date.today()
    elif m:
        try:
            day = datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            pass
    if day is None:
        return text
    stamp = f"{WEEKDAYS[day.weekday()]} {day.day} {MONTHS[day.month - 1]} {day.year}"
    return f"{stamp}, {m.group(4)}" if m and m.group(4) else stamp


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
    levelups = sorted((out / "Level-ups").glob("*.md")) if (out / "Level-ups").is_dir() else []
    files["levelups"] = levelups                          # the folder the coach's Project or Cowork folder holds
    files["plugin_zip"] = root / "dist" / PLUGIN_ZIP      # the plugin form, when built (both editions on disk)
    return files, str(manifest.get("build_sha256", ""))[:12]


PLUGIN_ZIP = "content-machine-plugin.zip"
PLUGIN_NAME = "content-machine"


def plugin_files(zip_path: Path, edition: str) -> dict[str, bytes]:
    """The plugin's files for one edition, as {path under kit/plugin/: bytes}: skills/<skill>/SKILL.md of the main skill
    (content-machine-<ed>) and of each companion skill (cm-<area>-<ed>), and agents/*.md. The method file and the
    level-up files are in the kit already (kit/ and kit/Level-ups/), so they are not repeated."""
    if not Path(zip_path).exists():
        raise RunError(f"{zip_path.name} not found: build both editions first (python3 tools/build.py --edition all)")
    out = {}
    with zipfile.ZipFile(zip_path) as zf:
        for name in sorted(zf.namelist()):
            parts = name.split("/")
            if len(parts) == 4 and parts[0] == PLUGIN_NAME and parts[1] == "skills" and parts[2].endswith(f"-{edition}") \
                    and parts[3] == "SKILL.md":
                out[f"skills/{parts[2]}/SKILL.md"] = zf.read(name)
            elif len(parts) == 3 and parts[0] == PLUGIN_NAME and parts[1] == "agents" and parts[2].endswith(".md"):
                out[f"agents/{parts[2]}"] = zf.read(name)
    if not out:
        raise RunError(f"{zip_path.name} holds no {edition} skills")
    return out


def run_id(suite: str, edition: str, persona: str, lane: str, repeat: int, tag: str = "",
           case: str = "", web: bool = False, plugin: bool = False) -> str:
    parts = [tag] if tag else []
    parts += [case.replace(".", "_")] if case else [suite, edition, persona]
    return "-".join(parts + [lane] + (["web"] if web else []) + (["plugin"] if plugin else []) + [f"r{repeat}"])


def lane_label(meta: dict) -> str:
    """"S1", "S1+web", "S1+web+plugin": the lane and its options, as the summary shows them."""
    return str(meta.get("lane", "")) + ("+web" if meta.get("web") else "") + ("+plugin" if meta.get("plugin") else "")


PROTOCOL = """# Run packet: {run_id}

One simulator agent plays both sides, turn by turn, from the files in this folder. No API keys, no real account.

- **Machine side:** `MACHINE.md`. It runs on the kit files in `kit/` exactly as written. It may not use any
  persona fact before the coach has said it in the transcript, and it never reads the persona folder,
  `expected.toml`, the eval cases or `qa/`.
- **Coach side:** `COACH.md`. Only facts from the persona files it names, in the persona's style and order.
- Keep the two apart: write each machine reply from the transcript so far and the kit only. `grade` scans
  every machine turn for persona wording the coach never said (the leak check): a leak makes the run invalid.
  Never write "no leaks" in notes.md without a passing leak check.
- Write each machine turn once; never run `grade` or a leak scan on a draft. A draft that used a persona fact
  stays as written and fails the run (P13).
- Machine turns are frozen after the first grade: it keeps the transcript as `transcript.raw.jsonl`. After that,
  change only the leaked words of a machine turn, and log each change in `meta.json` under `"edits"`:
  `{{"turn": 7, "field": "openers_closers", "before": "…", "after": "…", "reason": "leak: …"}}`. Any other change
  (a coach turn, a time, a rewrite that is not a leak removal) makes the run invalid; `grade` prints "edited: n".

## Write back into this run folder ({run_dir})

1. `transcript.jsonl`: one JSON object per turn, in order:
   `{{"turn": 1, "role": "coach" | "machine", "text": "...", "t_min": 0.5}}`. A coach turn and the machine
   reply to it share the same `turn` number. `t_min` is the modelled minute the turn ends, on one convention
   (P12): a machine turn's `t_min` is when the reply arrives, the coach's turn + about 0.3 min; the coach's
   reading time goes on their next turn, with their dictation or typing. Optional keys on a coach row:
   `"away_min": 40` for time away before it (a site visit, a plan limit; it does not count as active time),
   `"quit": true` on the coach's quit line (the run then ends on that coach turn), `"third_party": true` when
   the whole turn is someone else's post. Turns alternate coach, machine; every coach turn but a quit gets a
   reply.
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
{level_line}{plugin_line}{web_line}- A link the coach sends is never opened here (unopened = unread).
- Today's date: {today}.
- You know which app you run in; you do not know the coach's plan or device until they say it.
"""

WEB_OFF = ("- Searching the web is not possible in this run: where the kit says \"search if you can\", you can't. The "
           "background research pass has no tool: the Map comes first, then the exact paste steps.\n")
WEB_ON = (
    "- **Web search and page fetch are on in this run** (lane option `web`), for the background research pass only (Day 0, "
    "§CM-LISTEN: the kit's own searches in the buyer's words). Use them as a session with its own search tool does, "
    "read-only: open a page before you quote it (unopened = unread); a line you did not see on a page is \"(unverified)\" "
    "and never goes in a piece; people by role, never by name or handle; never log in, post, react, follow, DM or join; "
    "never touch the coach's computer or apps. A page that will not open is \"unread\" on the Map, not guessed. Keep "
    "a log as you go and put it in notes.md under \"## Research log\": each query, each page opened (URL, place, "
    "month, role) and the lines kept, so the reviewer can re-fetch them. Do not search before the kit says to. "
    "**Run the research pass as if by a separate agent that sees only the transcript so far** (the coach's turns and "
    "your replies up to the turn it runs after) and the kit, never the persona files, `answers.md`, `expected.toml` or "
    "anything about the coach that is not in the transcript at that turn: a query holds only words the coach has said by "
    "then, and the buyer's, never the persona's, wording. **Log the real turn of each query**, one line each, "
    "`Q<n> · after turn <N> · <query>`, N being the last coach turn the pass could see, the turn it really ran after "
    "(not a turn it is modelled in later or earlier). `grade` reads the log: a query that holds a run of two or more "
    "content words that only the persona's answer bank holds (a phrase the coach never said, such as "
    "\"which clients\") is a leak and makes the run invalid.\n")
LEVELUPS_LINE = (
    "- **Level-ups:** {names} are project files in `kit/Level-ups/`, next to the method file, as in the coach's Project or "
    "folder. Open one only when the instructions name it for the job (research and listening: RESEARCH; strategy, hooks, "
    "titles and long video: STRATEGY; launch: LAUNCH; the board: BOARD), and read the §CM- part the job needs, never the "
    "whole file.\n")
PLUGIN_LINE = (
    "- **Plugin form:** the coach installed the plugin. `kit/plugin/skills/` holds its skills (the main skill and one "
    "companion skill per level-up area; each SKILL.md) and `kit/plugin/agents/` its agents; the method file and the "
    "Level-ups are the kit's own (above). A companion skill carries its level-up file: when the job is theirs, read "
    "that skill's SKILL.md and its level-up file, and never ask the coach to upload a Level-ups file.\n")

COACH_DAY0 = """# Coach side: {persona} ({edition}), Day 0

Persona folder: `{pdir}`. Read `persona.toml` (identity, app, plan and device, behaviour traits, quit
triggers), `answers.md` and `written-posts.md`. Never read `expected.toml` or `voice-samples.md` (they are
answer keys for the graders) and never let them shape a turn.

## Script

1. Open the project chat with exactly: `{start}`.
2. Dictate the three `## Dump chunk` sections of `answers.md` verbatim, in order, one coach turn per send, when
   the machine asks for the dump. A chunk over about 400 words (VN tiếng) goes in two sends, split at a
   paragraph, as the dump prompt asks. Chunk 1's first send ends by about 300 words (VN tiếng), about 3 minutes
   of talk, at a paragraph or sentence end, as the dump prompt says "every 2–3 minutes"; the rest of chunk 1 is
   the next send (P16). When the dump prompt invites posts you've written, paste the body of
   `written-posts.md` `## W1` and `## W2` (verbatim, without their headings) as one more turn, after chunk 1
   or 2, the way this coach would. If the dump prompt asks where you post and about your list, and the
   persona's answer is in a later chunk, add it as one sentence at the end of chunk 1 (VP-2). Then say you are
   done in your own words ("done", "ok that's it"). The kit cuts the dump softly past about {cut} of your
   talk, your pasted posts not counted (acceptance.toml [day0]). If the machine says the dump is enough, or asks
   you to wrap up, say done there and skip what is not yet dictated (the machine then asks only what it is
   missing).
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
takes about half a minute. A machine turn's `t_min` is when the reply arrives (the coach's turn + about 0.3 min);
the coach's reading time goes on their next turn (P12). Plan limits: if this persona's plan ({plan} on {app})
would hit a message limit during the run, model it (`away_min` on the coach's next turn) and say so in notes.md.
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


WEB_PROTOCOL = """
## Web lane

This run has the `web` option: the machine side may search and fetch pages for the background research pass
(`MACHINE.md`). Add `## Research log` to `notes.md`: every query, every page opened (URL, place, month, role), the
lines kept and the lines dropped, and what the research changed on the Map (line 1, the keyword, big idea 1: before →
after), or "nothing". The reviewer re-fetches the kept lines. A line that was not seen on an opened page is never
quoted in a piece.

Run the research pass as if by a separate agent: it sees only the transcript up to the turn it runs after and the kit,
never the persona files. Log each query as it really ran, one line each under "### Queries":
`Q6 · after turn 3 · "which clients" agency owner`, where 3 is the last coach turn the pass could see. A modelled turn
("ran after turn 3" when the words came at turn 8) is a false log. Under "### Pages opened" number the pages (`1. <URL> ·
place · month · role · result`); under "### Lines kept" number the lines (`1. "the line" · role · place · month`, with
`(page 9)` when the page is not the group's); name the lines behind each pattern (`KEEP: <pattern> (lines 1, 2, 3)`).
`grade` checks the queries against the persona's answer bank (research_leaks: two or more content words in a row that
answers.md holds and nobody had said by that turn make the run invalid) and each KEEP against its pages
(research_log: lines from 2 or more distinct pages on 2 or more distinct hosts).
"""


def write_packet(root: Path, out_root: Path, rid: str, meta: dict, kit: dict[str, Path], lane: str,
                 coach_md: str, today: str) -> Path:
    """One packet folder. meta["web"] / meta["plugin"] are the lane options (module docstring): the machine side's
    web line, and the plugin's skills in kit/plugin/. A lane with a method file also gets the edition's Level-ups."""
    run_dir = out_root / rid
    if run_dir.exists():
        raise RunError(f"{rel(run_dir, root)} exists; pass another --tag or remove it")
    spec = LANES[lane]
    web, plugin = bool(meta.get("web")), bool(meta.get("plugin"))
    if plugin and not spec["method"]:
        raise RunError(f"--plugin needs a lane with the method file (S1 or floor), not {lane}")
    plugin_kit = plugin_files(Path(kit.get("plugin_zip") or root / "dist" / PLUGIN_ZIP), meta["edition"]) if plugin else {}
    (run_dir / "packet" / "kit").mkdir(parents=True)
    shutil.copy2(kit["instructions"], run_dir / "packet" / "kit" / kit["instructions"].name)
    method_line = "- **Method file:** none in this lane (compact mode)."
    level_line = ""
    if spec["method"]:
        if not kit["method"].exists():
            raise RunError(f"lane {lane} needs {kit['method'].name}, which the build did not produce")
        shutil.copy2(kit["method"], run_dir / "packet" / "kit" / kit["method"].name)
        method_line = f"- **Method file:** `kit/{kit['method'].name}`, a project file."
        levelups = [Path(f) for f in kit.get("levelups") or []]
        if levelups:
            (run_dir / "packet" / "kit" / "Level-ups").mkdir()
            for f in levelups:
                shutil.copy2(f, run_dir / "packet" / "kit" / "Level-ups" / f.name)
            level_line = LEVELUPS_LINE.format(names=", ".join(f"`{f.name}`" for f in levelups))
    for sub, data in plugin_kit.items():
        out = run_dir / "packet" / "kit" / "plugin" / sub
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
    ed = cmlib.load_edition(meta["edition"], root)
    app = APP_NAMES.get(meta.get("app", ""), "ChatGPT or Claude") + " (a Project)"
    files = {
        "README.md": PROTOCOL.format(run_id=rid, run_dir=rel(run_dir, root)) + (WEB_PROTOCOL if web else ""),
        "MACHINE.md": MACHINE.format(lane=lane + ("+web" if web else "") + ("+plugin" if plugin else ""),
                                     about=spec["about"], model=spec["model"], edition=ed.id, app=app,
                                     method_line=method_line, level_line=level_line,
                                     plugin_line=PLUGIN_LINE if plugin else "", web_line=WEB_ON if web else WEB_OFF,
                                     today=run_date(today)),
        "COACH.md": coach_md,
    }
    for name, text in files.items():
        (run_dir / "packet" / name).write_text(nfc(text), encoding="utf-8")
    (run_dir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return run_dir


def make_packets(root: Path, suite: str, edition: str, lane: str, persona_ids: list[str], repeat: int = 1,
                 tag: str = "", module: str = "", case_ids: list[str] | None = None,
                 out_root: Path | None = None, today: str = "",
                 kit: tuple[dict[str, Path], str] | None = None, web: bool = False, plugin: bool = False) -> list[Path]:
    """Write one packet per persona (day0) or per D case (cases), times `repeat`. `kit` is (files, sha) from
    build_kit; tests pass prebuilt files. `web` and `plugin` are the lane options (module docstring)."""
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
            cut = int(accept.get(f"dump_cut_words_{edition}", graders.DUMP_CUT_WORDS))     # review retest-vg4-g5 P15
            turns = int(accept.get(f"session_max_turns_{edition}", accept.get("session_max_turns", 10)))   # vg5-g6 G43
            coach = COACH_DAY0.format(persona=pid, edition=edition, pdir=rel(pdir, root),
                                      start=strings.get("cmd.start", "Start"),
                                      cut=f"{cut:,} {'tiếng' if edition == 'vn' else 'words'}",
                                      max_turns=turns + 4,
                                      app=APP_NAMES.get(app, app or "the app"), plan=plan or "unknown plan")
            for n in range(1, repeat + 1):
                rid = run_id(suite, edition, pid, lane, n, tag, web=web, plugin=plugin)
                meta = {"persona": f"{edition}/{pid}", "edition": edition, "lane": lane, "build_sha": sha,
                        "suite": suite, "repeat": n, **({"app": app} if app else {}),
                        **({"web": True} if web else {}), **({"plugin": True} if plugin else {})}
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
            rid = run_id(suite, edition, pid, lane, n, tag, case=case["id"], web=web, plugin=plugin)
            meta = {"persona": f"{edition}/{pid}" if pid else "", "edition": edition, "lane": lane,
                    "build_sha": sha, "suite": suite, "repeat": n, "case": case["id"], **({"app": app} if app else {}),
                    **({"web": True} if web else {}), **({"plugin": True} if plugin else {})}
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
        # `invariants` also names a check of graders.py (hook_lab, day0_shape, vn_messages …) the case depends on
        by_id = {i["id"]: i for i in report.get("checks", []) + report.get("invariants", [])}
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
PASTE_MIN_PER_POST = 0.5         # minutes per pasted written post (COACH.md "a pasted post takes about half a minute")
LEAK_N = {"en": 6, "vn": 8}      # words / tiếng in a run shared with the persona files
# A shorter run from an answers.md paragraph no coach turn covered (the POST_RUN test): a short lift of a fact the coach
# never dictated ("rồi mới đi coi nhà", "ngồi tính trước rồi mới dẫn đi"). A warning, never a failure: P9, a machine
# side that never sees the persona, stays the real fix (review retest-vg5-g6 P17).
LEAK_SHORT_N = {"en": 5, "vn": 5}


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


def _written_posts(pdir: Path) -> list[tuple[str, str]]:
    """(id, body) of the persona's written-posts.md sections ("W1", …)."""
    path = pdir / "written-posts.md"
    return graders.written_post_sections(path.read_text(encoding="utf-8")) if path.exists() else []


def _split_pasted(text: str, posts: list[tuple[str, set]]) -> tuple[list[str], set[str]]:
    """(the turn's other paragraphs, the ids of the written posts it pastes): a paragraph mostly made of a written
    post's runs is that post pasted (graders.is_pasted_post, the POST_RUN test dump_cut uses); a post that runs over
    several paragraphs counts once."""
    every = set().union(*(runs for _, runs in posts)) if posts else set()
    talk, pasted = [], set()
    for para in graders._paragraphs(nfc(text)):
        if every and graders.is_pasted_post(para, every):
            pasted.add(max(posts, key=lambda p: graders.run_coverage(para, p[1])[0])[0])
        else:
            talk.append(para)
    return talk, pasted


def check_pace(rows: list[dict], pdir: Path) -> dict:
    """A dictated dump chunk takes at least words / 160 minutes of active time (t_min minus away_min). The coach's
    pasted written posts (written-posts.md) are not dictated words: their paragraphs are left out of the words and of
    the dictation test, and each pasted post takes at least PASTE_MIN_PER_POST minutes instead (COACH.md: "a pasted post
    takes about half a minute"; review retest-vg4-g5 P14: one line of a pasted post shared with the dump made a whole
    paste turn read as dictation)."""
    dump = _dump_runs(pdir)
    posts = [(sid, graders.post_runs([body])) for sid, body in _written_posts(pdir)]
    ev, prev = [], None
    for r in rows:
        t = r.get("t_min")
        if r.get("role") == "coach" and t is not None and prev is not None:
            talk, pasted = _split_pasted(r.get("text", ""), posts)
            words = _words("\n\n".join(talk))
            dictated = bool(dump) and bool(_grams(words, 12) & dump)
            if dictated or pasted:
                active = float(t) - float(prev) - float(r.get("away_min") or 0)
                need = (len(words) / DICTATION_MAX_WPM if dictated else 0.0) + PASTE_MIN_PER_POST * len(pasted)
                if round(active, 2) < round(need, 2):
                    what = " and ".join(([f"{len(words)} dictated words"] if dictated else [])
                                        + ([f"{len(pasted)} pasted post{'s' if len(pasted) > 1 else ''}"]
                                           if pasted else []))
                    rate = ", ".join(([f"{DICTATION_MAX_WPM} wpm"] if dictated else [])
                                     + ([f"{PASTE_MIN_PER_POST:g} min a post"] if pasted else []))
                    ev.append(f"turn {r.get('turn')}: {what} in {active:.1f} min (needs ≥{need:.1f} at {rate})")
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


MD_HEADING_RE = re.compile(r"^\s*#{1,6}\s.*$", re.M)


def answer_paragraphs(pdir: Path) -> list[str]:
    """answers.md in paragraphs (blank-line apart, headings left out), each list item of a paragraph apart: one
    answer-bank line ("- **Gói dịch vụ + giá:** …") is one paragraph."""
    path = pdir / "answers.md"
    if not path.exists():
        return []
    text = MD_HEADING_RE.sub("", nfc(path.read_text(encoding="utf-8")))
    out = []
    for para in graders._paragraphs(text):
        items = re.split(r"\n(?=\s*(?:[-*•]|\d{1,2}[.)])\s)", para)
        out += [item.strip() for item in items if item.strip()]
    return out


def undictated_corpus(rows: list[dict], pdir: Path, n: int) -> set[str]:
    """The n-grams (_content_words) of the answers.md paragraphs no coach turn covered: fewer than half their tokens in
    POST_RUN-token runs of the coach's turns (graders.is_pasted_post, the coverage test _split_pasted uses; review
    retest-vg5-g6 P17)."""
    said = graders.post_runs([r.get("text", "") for r in rows if r.get("role") == "coach"])
    return set().union(*(_grams(_content_words(p), n) for p in answer_paragraphs(pdir)
                         if not graders.is_pasted_post(p, said)), set())


def _spans(hit: list[int], n: int) -> list[tuple[int, int]]:
    """Overlapping n-gram hits (start indexes, ascending) merged into (start, end) spans."""
    spans: list[tuple[int, int]] = []
    for i in hit:
        if spans and i <= spans[-1][1]:
            spans[-1] = (spans[-1][0], i + n)
        else:
            spans.append((i, i + n))
    return spans


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
    Card line (a voice field, or the visible HOW YOU SAY IT / YOUR VOICE line, read one quote apart from its label)
    fails the run (it inflates I23 and the voice judging); other hits are listed for a human read ("warn"), since a
    model can rebuild a coach's phrase from what they said. A machine line is read without its field labels and one
    list item at a time (leak_corpus reads the persona's TOML the same way); a list item that is a whole persona phrase
    the coach never said leaks however short it is (leak_items). A shorter run, LEAK_SHORT_N words / tiếng, of an
    answers.md paragraph no coach turn covered (undictated_corpus) is a warning, never a failure, in any line: a short
    lift of a fact the coach never dictated (review retest-vg5-g6 P17)."""
    n, short_n = LEAK_N.get(lang, 6), LEAK_SHORT_N.get(lang, 5)
    corpus, whole = leak_corpus(pdir, n), leak_items(pdir, lang)
    undictated = undictated_corpus(rows, pdir, short_n) if short_n < n else set()
    unit = "tiếng" if lang == "vn" else "words"
    # a run whose first or last n-1 words the coach said, or the kit holds, is a restatement, not a leak (the short
    # tier the same, with its own n-1)
    known: set[str] = set()
    known_short: set[str] = set()
    said = " "                                    # the coach's words so far, for whole-item matches

    def learn(text: str) -> None:
        nonlocal said
        words = _content_words(text)
        known.update(_grams(words, n - 1))
        known_short.update(_grams(words, short_n - 1))
        said += " ".join(words) + " | "

    if kit_dir and kit_dir.is_dir():
        for f in sorted(kit_dir.rglob("*")):                 # kit/, kit/Level-ups/, kit/plugin/: all the kit's wording
            if f.is_file() and f.suffix.lower() in (".txt", ".md"):
                learn(f.read_text(encoding="utf-8"))
    fails, warns = [], []
    for r in rows:
        if r.get("role") == "coach":
            learn(r.get("text", ""))
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

                def leaked(i: int, size: int, grams: set[str], seen: set[str]) -> bool:
                    g = words[i:i + size]
                    return (" ".join(g) in grams and " ".join(g[:-1]) not in seen
                            and " ".join(g[1:]) not in seen)

                spans = _spans([i for i in range(len(words) - n + 1) if leaked(i, n, corpus, known)], n)
                for a, b in spans:
                    entry = f'turn {r.get("turn")}: "{" ".join(words[a:b])}"'
                    (fails if voice else warns).append(entry)
                # the short tier (P17): a warning only, and only outside the spans already listed
                short = [i for i in range(len(words) - short_n + 1) if leaked(i, short_n, undictated, known_short)]
                for a, b in _spans(short, short_n):
                    if not any(a < y and x < b for x, y in spans):
                        warns.append(f'turn {r.get("turn")}: "{" ".join(words[a:b])}" (undictated answers.md, '
                                     f"{short_n}+ {unit})")
    out = _protocol("leaks", fails, n=n, short_n=short_n, warnings=warns)
    if not fails and warns:
        out["status"] = "warn"
    return out


# ---- the research log's queries (web lane; review retest-ft2 §8 fix 4)
# The research pass is the one place where the machine side reaches outside the transcript, and it did so with the persona
# files at hand: EN's topic 1 changed because "which clients" (a phrase of the persona's answer bank, never dictated) was
# in queries 6, 10 and 11, and a 5-word window cannot see a 2-word echo. check_research_leaks reads each logged query
# ("Q6 · after turn 3 · …"; graders.research_queries) for a run of RESEARCH_LEAK_N content words, none a function word,
# that the persona's answer bank (answers.md) holds and that neither the coach (turns up to the one it ran after) nor the machine (its replies
# before) nor the kit ever said, and fails the run on it. Words the coach said only LATER are a warning: the query claims
# a turn it could not have run in (the log's turn is modelled, not real).
RESEARCH_LEAK_N = {"en": 2, "vn": 4}          # content words / tiếng in a row (a VN word is 1-2 tiếng: 2 words ≈ 4 tiếng)
_QUERY_SPLIT_RE = re.compile(r"[\"“”()\[\]·|;:,.!?…\n/]+|\s[-–—]\s|\b(?:OR|AND)\b")
RESEARCH_STOP_EN = set("""a an the and or but so if then i you your we our us it its is are was were be been am to of in on at
for with from by as this that these those there here my me he she they them do does did not no just very can will would
should could have has had all any some than too also now up out off per into over about each own""".split())
RESEARCH_STOP_VN = {graders.ck.fold(w) for w in (
    "thì là mà và của cái những các một này đó ấy kia ạ nhé nha à ơi với cho để khi nếu vì nên có được đã đang sẽ rồi cũng "
    "thế vậy đi lại ra vào lên xuống mình bạn em anh chị tôi mấy hả hở đấy nhỉ luôn không chưa phải rất cứ nữa hay hoặc "
    "chỉ còn đều bị nhưng cần muốn tui cô chú").split()}


def _research_stem(word: str, lang: str) -> str:
    word = word.split("'")[0] if "'" in word else word
    if lang == "vn":
        return graders.ck.fold(word)
    if len(word) > 4 and word.endswith("ies"):
        return word[:-3] + "y"
    return word[:-1] if len(word) > 3 and word.endswith("s") and not word.endswith("ss") else word


def _research_windows(text: str, n: int, lang: str, raw: dict[str, str] | None = None) -> set[str]:
    """The runs of n content words in a row of a text, per clause (a quote, a comma, a sentence ends a run), none of them
    a function word; stemmed ("clients" → "client"). `raw`, when given, gets each run as written (the first time)."""
    stop = RESEARCH_STOP_VN if lang == "vn" else RESEARCH_STOP_EN
    out: set[str] = set()
    for seg in _QUERY_SPLIT_RE.split(nfc(text)):
        written = _content_words(seg)
        words = [_research_stem(w, lang) for w in written]
        for i in range(len(words) - n + 1):
            win = words[i:i + n]
            if not any(w in stop or len(w) < 2 for w in win):
                out.add(" ".join(win))
                if raw is not None:
                    raw.setdefault(" ".join(win), " ".join(written[i:i + n]))
    return out


def _answer_bank_windows(pdir: Path, n: int, lang: str) -> set[str]:
    """The runs of n content words in the persona's answer bank (answers.md: the dump and the Q&A the coach draws from).
    Not the persona's other files (the pastes it offers later, expected.toml): those share generic search words
    ("forum thread", "agency founder") with any query."""
    path = pdir / "answers.md"
    return _research_windows(path.read_text(encoding="utf-8"), n, lang) if path.exists() else set()


def _kit_text(kit_dir: Path | None) -> str:
    if not kit_dir or not kit_dir.is_dir():
        return ""
    return "\n".join(f.read_text(encoding="utf-8") for f in sorted(kit_dir.rglob("*"))
                     if f.is_file() and f.suffix.lower() in (".txt", ".md"))


def check_research_leaks(run_dir: Path, rows: list[dict], pdir: Path, kit_dir: Path | None, lang: str,
                         web: bool = True) -> dict | None:
    """Protocol check for the web lane's Research log (notes.md "## Research log", queries as "Q6 · after turn 3 · …"):
    - every query names the turn it really ran after, a turn the run has;
    - no query holds a run of RESEARCH_LEAK_N content words (no function word among them) that the persona's answer
      bank (answers.md) holds and no one had said at the turn it ran after: the coach's turns up to it, the machine's replies before it, the
      kit's own wording (a phrase the coach said only later is a warning: "ran after turn 3" cannot be true).
    A web run without a Research log fails (nothing to audit); a run that is not a web run and has no log returns None."""
    log = graders.research_log_text(run_dir)
    if not log.strip():
        return _protocol("research_leaks", ["a web-lane run needs its Research log in notes.md (\"## Research log\" with "
                                            "its queries)"]) if web else None
    n = RESEARCH_LEAK_N.get(lang, 2)
    queries = graders.research_queries(log)
    last_coach = max((r.get("turn", 0) for r in rows if r.get("role") == "coach"), default=0)
    persona = _answer_bank_windows(pdir, n, lang)
    kit = _research_windows(_kit_text(kit_dir), n, lang)
    when: dict[str, int] = {}                  # the first turn a window is available: a coach turn's own, a reply's + 1
    said_at: dict[str, int] = {}               # the first coach turn that says it
    for r in rows:
        k = r.get("turn", 0)
        for win in _research_windows(r.get("text", ""), n, lang):
            if r.get("role") == "coach":
                said_at.setdefault(win, k)
            when[win] = min(when.get(win, 10 ** 6), k if r.get("role") == "coach" else k + 1)
    fails, warns, no_turn = [], [], []
    unit = "tiếng" if lang == "vn" else "words"
    for q in queries:
        label = f'query {q["n"]} "{_short_q(q["text"])}"'
        turn = q["turn"]
        if turn is None:
            no_turn.append(q["n"])
            continue
        if turn > last_coach or turn < 1:
            fails.append(f"{label}: logged after turn {turn}, a turn this run does not have ({last_coach} coach turns)")
            continue
        leaked, ahead, written = [], [], {}
        for win in sorted(_research_windows(q["text"], n, lang, written)):
            if when.get(win, 10 ** 6) <= turn or win in kit:
                continue
            if win in said_at:
                ahead.append((written[win], said_at[win]))
            elif win in persona:
                leaked.append(written[win])
        if leaked:
            fails.append(f'{label} (after turn {turn}): "{"; ".join(leaked[:4])}" is in the persona\'s answer bank and was '
                         f"never said ({n}+ {unit} in a row)")
        if ahead:
            warns.append(f'{label} (after turn {turn}): "{"; ".join(w for w, _ in ahead[:3])}" first said at turn '
                         f'{max(t for _, t in ahead)}, after the turn the log gives')
    if no_turn:
        fails.append(f"queries {', '.join(map(str, no_turn[:8]))}{'…' if len(no_turn) > 8 else ''} name no turn: log each "
                     'as "Q<n> · after turn <N> · <query>"')
    out = _protocol("research_leaks", fails, n=n, queries=len(queries), warnings=warns)
    if not fails and warns:
        out["status"] = "warn"
    return out


def _short_q(text: str, limit: int = 60) -> str:
    return text if len(text) <= limit else text[:limit - 1].rstrip() + "…"


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
    checks = [check_turns(rows), check_pace(rows, pdir),
              check_leaks(rows, pdir, run_dir / "packet" / "kit", lang, labels), check_edits(run_dir, meta)]
    research = check_research_leaks(run_dir, rows, pdir, run_dir / "packet" / "kit", lang, web=bool(meta.get("web")))
    return checks + [research] if research else checks


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
    out["web"], out["plugin"] = bool(meta.get("web")), bool(meta.get("plugin"))      # the lane options (docstring)
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
            run=g.get("run", ""), persona=g.get("persona", ""), valid=valid,
            lane=lane_label({"lane": g.get("lane", ""), "web": g.get("web"), "plugin": g.get("plugin")}),
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
    p.add_argument("--today", default="", help="the date the machine side is told (YYYY-MM-DD; default: the day the "
                   "packet is made; a persona's day0 wins in a day0 suite)")
    p.add_argument("--web", action="store_true", help="lane option: the machine side may use web search and page fetch "
                   "for the background research pass (read-only; a Research log in notes.md); run ids get -web")
    p.add_argument("--plugin", action="store_true", help="lane option: the plugin form; the edition's skills and the "
                   "plugin's agents go in packet/kit/plugin/ (from dist/content-machine-plugin.zip); run ids get -plugin")
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
                                args.module, args.case, args.out, args.today, web=args.web, plugin=args.plugin)
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
