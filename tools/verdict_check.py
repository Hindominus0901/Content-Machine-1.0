#!/usr/bin/env python3
"""Validate verdict files (docs/BUILD.md §9; QA spec §5.5).

    python3 tools/verdict_check.py                    every verdict under qa/verdicts/
    python3 tools/verdict_check.py PATH [PATH ...]    files, or folders searched recursively

A verdict file is `<area>-verdict.md` (also RELEASE-VERDICT.md and gate files
like G3-verdict.md); its second read is `<name>.second-read.md` next to it.

Rules:
- The first four lines are exactly:
      Result: PASS | Result: FAIL
      Score: n/m                      (numbers, n <= m, m > 0)
      Critical items failed: 0 | none | <count> (<items>)
      Not run: none | <items>
  A PASS has 0 critical items failed and "Not run: none" ("not run" counts as FAIL).
- A header table (`| Field | Value |` rows) names: Subject (with the commit hash, or a
  Commit row), Build sha, Edition and Lane (one row or two), Producer and Reviewer.
  Producer and reviewer must differ.
- No conditional-pass wording ("pass after", "conditional", "pass with", "PASS*") and no
  praise words, outside quotes and inline code (quoted evidence may hold anything).
- A PASS needs `<name>.second-read.md` beside it whose Result is PASS (the lower result
  stands). Second reads are validated like any verdict but need no second read of their own.
- Every `<!-- scorecard {...} -->` line holds a JSON object, and there is at least one.
  A scorecard "result" or "score" key must agree with the first lines.

Exit 0 when every file is valid, 1 when any is not, 2 on a usage error.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cmcore import checks as ck  # noqa: E402

ROOT = Path(os.environ.get("CM_ROOT", Path(__file__).resolve().parent.parent))

RESULT_RE = re.compile(r"^Result: (PASS|FAIL)$")
SCORE_RE = re.compile(r"^Score: (\d+(?:\.\d+)?)/(\d+(?:\.\d+)?)$")
CRITICAL_RE = re.compile(r"^Critical items failed: (.+)$")
NOT_RUN_RE = re.compile(r"^Not run: (.+)$")
SCORECARD_RE = re.compile(r"<!--\s*scorecard\s+(.*?)\s*-->", re.S)
CONDITIONAL_RE = re.compile(r"\bpass(?:es|ed)?\s+after\b|\bconditional(?:ly)?\b|\bpass(?:es|ed)?\s+with\b|\bPASS\*",
                            re.I)
HASH_RE = re.compile(r"\b[0-9a-f]{7,64}\b")
PLACEHOLDER_RE = re.compile(r"^(?:|-|—|\?|tbd|todo|n/?a|none|<.*>)$", re.I)
SECOND_READ_SUFFIX = ".second-read.md"


@dataclass
class Verdict:
    path: Path
    result: str | None = None
    score: tuple[float, float] | None = None
    critical: int | None = None
    not_run: str | None = None
    header: dict[str, str] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)

    @property
    def is_second_read(self) -> bool:
        return self.path.name.endswith(SECOND_READ_SUFFIX)


def is_verdict_file(path: Path) -> bool:
    name = path.name.lower()
    return name.endswith(".md") and ("verdict" in name or name.endswith(SECOND_READ_SUFFIX))


def second_read_path(path: Path) -> Path:
    return path.with_name(path.name[:-3] + SECOND_READ_SUFFIX)


def _header_table(lines: list[str]) -> dict[str, str]:
    """The first markdown table after the fixed lines, as {normalised field: value}."""
    rows: dict[str, str] = {}
    started = False
    for line in lines:
        s = line.strip()
        if s.startswith("|"):
            started = True
            cells = [c.strip() for c in s.strip("|").split("|")]
            if len(cells) < 2 or all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            key = re.sub(r"[^a-z0-9 ]", " ", cells[0].casefold())
            key = " ".join(key.split())
            if key in ("field", "item", "key"):
                continue
            rows[key] = " | ".join(cells[1:]).strip()
        elif started:
            break
    return rows


def _find(rows: dict[str, str], *prefixes: str) -> tuple[str, str] | None:
    for key, value in rows.items():
        if any(key.startswith(p) for p in prefixes):
            return key, value
    return None


def _scan_text(text: str) -> str:
    """Text the wording rules apply to: no quotes, inline code or scorecard comments."""
    text = SCORECARD_RE.sub(" ", text)
    text = re.sub(r"`[^`\n]*`", " ", text)
    text = ck.straight_quotes(text)
    return re.sub(r'"[^"\n]*"', " ", text)


def parse(path: Path) -> Verdict:
    v = Verdict(path=path)
    try:
        text = path.read_text(encoding="utf-8").lstrip("﻿")
    except (OSError, UnicodeDecodeError) as exc:
        v.errors.append(f"cannot read: {exc}")
        return v
    lines = text.splitlines()
    head = (lines + [""] * 4)[:4]

    m = RESULT_RE.match(head[0])
    if m:
        v.result = m.group(1)
    else:
        v.errors.append('line 1 must be exactly "Result: PASS" or "Result: FAIL"')
    m = SCORE_RE.match(head[1])
    if m:
        n, total = float(m.group(1)), float(m.group(2))
        v.score = (n, total)
        if total <= 0 or n > total:
            v.errors.append(f"line 2 score {m.group(1)}/{m.group(2)} is impossible")
    else:
        v.errors.append('line 2 must be "Score: n/m"')
    m = CRITICAL_RE.match(head[2])
    if m:
        value = m.group(1).strip()
        count = re.match(r"(\d+)\b", value)
        if value.casefold() == "none":
            v.critical = 0
        elif count:
            v.critical = int(count.group(1))
        else:
            v.errors.append('line 3 must be "Critical items failed: none" or start with a count')
    else:
        v.errors.append('line 3 must be "Critical items failed: ..."')
    m = NOT_RUN_RE.match(head[3])
    if m:
        v.not_run = m.group(1).strip()
    else:
        v.errors.append('line 4 must be "Not run: ..."')

    if v.result == "PASS":
        if v.critical:
            v.errors.append(f"PASS with {v.critical} critical item(s) failed")
        if v.not_run is not None and v.not_run.casefold() != "none":
            v.errors.append(f'PASS with checks not run ("{v.not_run}"); not run counts as FAIL')

    rows = _header_table(lines[4:])
    v.header = rows
    if not rows:
        v.errors.append("header table missing")
    else:
        subject = _find(rows, "subject")
        commit = _find(rows, "commit")
        if not subject:
            v.errors.append("header: Subject row missing")
        if not any(r and HASH_RE.search(r[1]) for r in (subject, commit)):
            v.errors.append("header: no commit hash on the Subject (or Commit) row")
        build = _find(rows, "build sha", "build")
        if not build or not HASH_RE.search(build[1]):
            v.errors.append("header: Build sha row missing or without a hash")
        both = _find(rows, "edition and lane", "edition lane")
        if both:
            if PLACEHOLDER_RE.match(both[1]):
                v.errors.append("header: Edition and lane is empty")
        else:
            for name in ("edition", "lane"):
                row = _find(rows, name)
                if not row or PLACEHOLDER_RE.match(row[1]):
                    v.errors.append(f"header: {name.capitalize()} row missing or empty")
        producer, reviewer = _find(rows, "producer"), _find(rows, "reviewer")
        for label, row in (("Producer", producer), ("Reviewer", reviewer)):
            if not row or PLACEHOLDER_RE.match(row[1]):
                v.errors.append(f"header: {label} row missing or empty")
        if producer and reviewer and " ".join(producer[1].casefold().split()) == " ".join(
                reviewer[1].casefold().split()):
            v.errors.append("header: producer and reviewer are the same")

    scan = _scan_text(text)
    for m in CONDITIONAL_RE.finditer(scan):
        v.errors.append(f'conditional-pass wording "{m.group(0)}"')
    praise = ck.praise_words(scan, None)
    if praise:
        v.errors.append("praise words: " + ", ".join(praise))

    cards = SCORECARD_RE.findall(text)
    if not cards:
        v.errors.append("scorecard comment missing (<!-- scorecard {...} -->)")
    for raw in cards:
        try:
            card = json.loads(raw)
        except json.JSONDecodeError as exc:
            v.errors.append(f"scorecard is not valid JSON: {exc.msg}")
            continue
        if not isinstance(card, dict):
            v.errors.append("scorecard must be a JSON object")
            continue
        res = card.get("result")
        if isinstance(res, str) and v.result and res.upper() != v.result:
            v.errors.append(f"scorecard result {res} differs from Result: {v.result}")
        sc = card.get("score")
        if isinstance(sc, str) and v.score and sc.replace(" ", "") != head[1][len("Score: "):].replace(" ", ""):
            v.errors.append(f"scorecard score {sc} differs from line 2")
    return v


def check_file(path: Path) -> Verdict:
    """Parse one verdict and apply the second-read rule to it."""
    v = parse(path)
    if v.result == "PASS" and not v.is_second_read:
        sr_path = second_read_path(path)
        if not sr_path.exists():
            v.errors.append(f"PASS without a second read ({sr_path.name})")
        else:
            sr = parse(sr_path)
            if sr.result != "PASS":
                v.errors.append(f"second read {sr_path.name} is not PASS; the lower result stands")
    return v


def collect(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for p in paths:
        if p.is_dir():
            files.extend(sorted(f for f in p.rglob("*.md") if is_verdict_file(f)))
        else:
            files.append(p)
    return files


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate QA verdict files (QA spec §5.5).")
    parser.add_argument("paths", nargs="*", help="verdict files or folders (default: qa/verdicts/)")
    args = parser.parse_args(argv)
    paths = [Path(p) for p in args.paths] or [ROOT / "qa" / "verdicts"]
    missing = [p for p in paths if not p.exists()]
    if missing:
        print("verdict_check: not found: " + ", ".join(map(str, missing)), file=sys.stderr)
        return 2
    files = collect(paths)
    if not files:
        print("verdict_check: no verdict files")
        return 0
    bad = 0
    for f in files:
        v = check_file(f)
        if v.errors:
            bad += 1
            print(f"FAIL {f}: " + "; ".join(v.errors))
        else:
            print(f"OK   {f}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
