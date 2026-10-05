#!/usr/bin/env python3
"""Gate G0 preflight and the build run contract (QA spec §5.1 G0, §5.6). Fails closed.

    python3 tools/preflight.py --release [--today YYYY-MM-DD] [--root PATH]
    python3 tools/preflight.py --run <id> [--root PATH]

--release (G0), every check must pass:
  version     VERSION is higher than the newest qa/releases/v*/ folder other than its own,
              and CHANGELOG.md has a "## [<VERSION>]" section. No earlier release: pass.
  freshness   every platform/targets.toml limit with a verified_on date is at most
              meta.max_age_days old; a release_blocking or budget-referenced limit must have a date.
  pending     every editions/<id>.toml [pending] key has an [accepted.<key>] row with signed_by
              and date in editions/<id>.acceptance.toml.
  modules     every evals/registry.toml module with status "active" has, per edition, at least its
              minimum [[case]] count in evals/cases/<name>.<edition>.toml (evals/acceptance.toml
              [cases]: "<name>_min" with "-" read as "_", else per_module_min) and an existing
              baseline file; a module that ships (modules/<lang>/<name>.md) must be active.
  judge       qa/CALIBRATION.md has a line "judge_validated: yes" naming the current release
              (on the line, e.g. "judge_validated: yes (v1.0.0)", or in the heading above it).
  round       prior release verdicts (qa/releases/v<VERSION>/RELEASE-VERDICT*.md) are listed;
              round = failed priors + 1; round 3 or later needs qa/releases/v<VERSION>/founder-yes.md.

--run <id> checks qa/runs/<id>/preflight.md, which the lead writes (never the producer):
  - headings (any level) Goal, Inputs, Upstream, Critical items, May write, Stop conditions,
    Never, each with content;
  - every `backticked/path` under Inputs and Critical items exists (globs must match);
  - every verdict path under Upstream is PASS with a PASS second read ("none" is allowed);
  - no critical item is marked MISSING or capped (that is a STOP);
  - a "Round: N" line; N = failed prior verdicts in qa/verdicts/<id>/ + 1, and every prior
    verdict is named in the file; round 3 or later needs qa/runs/<id>/founder-yes.md.

Prints one "PASS|FAIL <check>: <detail>" line per check. Exit 0 when all pass,
1 when any fails, 2 on a usage error.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import verdict_check  # noqa: E402

ROOT = Path(os.environ.get("CM_ROOT", Path(__file__).resolve().parent.parent))
RUN_HEADINGS = ("Goal", "Inputs", "Upstream", "Critical items", "May write", "Stop conditions", "Never")
SEMVER_RE = re.compile(r"^v?(\d+)\.(\d+)\.(\d+)$")


class Report:
    def __init__(self) -> None:
        self.lines: list[tuple[bool, str, str]] = []

    def add(self, ok: bool, check: str, detail: str) -> None:
        self.lines.append((ok, check, detail))

    @property
    def ok(self) -> bool:
        return all(ok for ok, _, _ in self.lines)

    def print(self) -> None:
        for ok, check, detail in self.lines:
            print(f"{'PASS' if ok else 'FAIL'} {check}: {detail}")


def _toml(path: Path) -> dict:
    with open(path, "rb") as fh:
        return tomllib.load(fh)


def _semver(text: str) -> tuple[int, int, int] | None:
    m = SEMVER_RE.match(text.strip())
    return tuple(int(g) for g in m.groups()) if m else None


def read_version(root: Path) -> str:
    return (root / "VERSION").read_text(encoding="utf-8").strip()


# ---------------------------------------------------------------- release checks

def check_version(root: Path, rep: Report) -> None:
    version = read_version(root)
    current = _semver(version)
    if not current:
        rep.add(False, "G0.version", f"VERSION '{version}' is not X.Y.Z")
        return
    releases = root / "qa" / "releases"
    prior = []
    if releases.is_dir():
        for d in releases.iterdir():
            v = _semver(d.name) if d.is_dir() else None
            if v and v != current:
                prior.append(v)
    if not prior:
        rep.add(True, "G0.version", f"{version}: no earlier release folder")
        return
    last = max(prior)
    last_s = ".".join(map(str, last))
    if current <= last:
        rep.add(False, "G0.version", f"VERSION {version} is not above the last release {last_s}")
        return
    changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
    m = re.search(rf"^##\s*\[v?{re.escape(version)}\][^\n]*\n(.*?)(?=^##\s|\Z)", changelog, re.M | re.S)
    if not m:
        rep.add(False, "G0.version", f"CHANGELOG.md has no '## [{version}]' section")
    elif not re.search(r"\S", re.sub(r"^#+.*$", "", m.group(1), flags=re.M)):
        rep.add(False, "G0.version", f"CHANGELOG.md section [{version}] is empty")
    else:
        rep.add(True, "G0.version", f"{version} > {last_s}; CHANGELOG has [{version}]")


def check_freshness(root: Path, rep: Report, today: dt.date) -> None:
    targets = _toml(root / "platform" / "targets.toml")
    max_age = int(targets.get("meta", {}).get("max_age_days", 90))
    budget_limits = {b.get("limit") for b in targets.get("budgets", {}).values() if b.get("limit")}
    problems = []
    for name, limit in sorted(targets.get("limits", {}).items()):
        stamp = str(limit.get("verified_on", "")).strip()
        needed = bool(limit.get("release_blocking")) or name in budget_limits
        if not stamp:
            if needed:
                problems.append(f"{name} has no verified_on (release-blocking or budget limit)")
            continue
        try:
            age = (today - dt.date.fromisoformat(stamp)).days
        except ValueError:
            problems.append(f"{name} verified_on '{stamp}' is not a date")
            continue
        if age > max_age:
            problems.append(f"{name} verified {age} days ago (max {max_age})")
        elif age < 0:
            problems.append(f"{name} verified_on {stamp} is in the future")
    if problems:
        rep.add(False, "G0.freshness", "; ".join(problems))
    else:
        rep.add(True, "G0.freshness", f"every verified_on within {max_age} days")


def check_pending(root: Path, rep: Report) -> None:
    problems = []
    for ed_file in sorted((root / "editions").glob("*.toml")):
        if ed_file.name.endswith(".acceptance.toml"):
            continue
        pending = _toml(ed_file).get("pending", {})
        if not pending:
            continue
        acc_file = ed_file.with_name(ed_file.stem + ".acceptance.toml")
        accepted = _toml(acc_file).get("accepted", {}) if acc_file.exists() else {}
        for key in sorted(pending):
            row = accepted.get(key, {})
            if not (str(row.get("signed_by", "")).strip() and str(row.get("date", "")).strip()):
                problems.append(f"{ed_file.stem}.{key}")
    if problems:
        rep.add(False, "G0.pending", "not accepted: " + ", ".join(problems))
    else:
        rep.add(True, "G0.pending", "every PENDING key signed")


def count_cases(path: Path) -> int:
    if not path.exists():
        return 0
    return len(_toml(path).get("case", []))


def min_cases(name: str, cases_cfg: dict, row: dict) -> int:
    if "min_cases" in row:
        return int(row["min_cases"])
    return int(cases_cfg.get(name.replace("-", "_") + "_min", cases_cfg.get("per_module_min", 20)))


def check_modules(root: Path, rep: Report) -> None:
    registry = _toml(root / "evals" / "registry.toml").get("modules", {})
    cases_cfg = _toml(root / "evals" / "acceptance.toml").get("cases", {})
    editions = sorted(p.stem for p in (root / "editions").glob("*.toml") if ".acceptance" not in p.name)
    problems, active = [], 0
    for name, row in sorted(registry.items()):
        status = row.get("status", "planned")
        ships = any((root / "modules" / ed / f"{name}.md").exists() for ed in editions)
        if status != "active":
            if ships:
                problems.append(f"{name} ships but is '{status}'")
            continue
        active += 1
        need = min_cases(name, cases_cfg, row)
        for ed in editions:
            have = count_cases(root / "evals" / "cases" / f"{name}.{ed}.toml")
            if have < need:
                problems.append(f"{name}.{ed} has {have} cases (min {need})")
        baseline = str(row.get("baseline", "")).strip()
        if not baseline or not (root / baseline).exists():
            problems.append(f"{name} has no recorded baseline")
    if problems:
        rep.add(False, "G0.modules", "; ".join(problems))
    else:
        rep.add(True, "G0.modules", f"{active} active module(s) meet their case minimums")


def check_judge(root: Path, rep: Report) -> None:
    version = read_version(root)
    path = root / "qa" / "CALIBRATION.md"
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    want = re.compile(rf"(?<![\d.])v?{re.escape(version)}(?![\d.])")
    heading = ""
    for line in text.splitlines():
        if line.startswith("#"):
            heading = line
        m = re.match(r"^\s*judge_validated:\s*yes\b(.*)$", line, re.I)
        if m and (want.search(m.group(1)) or want.search(heading)):
            rep.add(True, "G0.judge", f"judge validated for {version}")
            return
    rep.add(False, "G0.judge", f"qa/CALIBRATION.md has no 'judge_validated: yes ({version})' line")


def verdict_result(path: Path) -> str | None:
    return verdict_check.parse(path).result


def round_from(priors: list[Path]) -> int:
    return sum(1 for p in priors if verdict_result(p) != "PASS") + 1


def check_release_round(root: Path, rep: Report) -> None:
    version = read_version(root)
    folder = root / "qa" / "releases" / f"v{version}"
    priors = sorted(p for p in folder.glob("RELEASE-VERDICT*.md")
                    if not p.name.endswith(verdict_check.SECOND_READ_SUFFIX)) if folder.is_dir() else []
    listing = ", ".join(f"{p.name} ({verdict_result(p) or 'unreadable'})" for p in priors) or "none"
    rnd = round_from(priors)
    if rnd >= 3 and not (folder / "founder-yes.md").exists():
        rep.add(False, "G0.round", f"round {rnd} needs the founder's written yes "
                                   f"(qa/releases/v{version}/founder-yes.md); priors: {listing}")
    else:
        rep.add(True, "G0.round", f"round {rnd}; prior verdicts: {listing}")


def release(root: Path, today: dt.date) -> Report:
    rep = Report()
    for name, fn in (("G0.version", lambda: check_version(root, rep)),
                     ("G0.freshness", lambda: check_freshness(root, rep, today)),
                     ("G0.pending", lambda: check_pending(root, rep)),
                     ("G0.modules", lambda: check_modules(root, rep)),
                     ("G0.judge", lambda: check_judge(root, rep)),
                     ("G0.round", lambda: check_release_round(root, rep))):
        try:
            fn()
        except Exception as exc:  # fail closed: a check that cannot run is a FAIL
            rep.add(False, name, f"could not run: {type(exc).__name__}: {exc}")
    return rep


# ---------------------------------------------------------------- run contract

def split_sections(text: str) -> dict[str, str]:
    """{heading text (casefolded): body} for every markdown heading."""
    out: dict[str, str] = {}
    current = None
    for line in text.splitlines():
        m = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if m:
            current = m.group(1).strip().rstrip(":").casefold()
            out.setdefault(current, "")
        elif current is not None:
            out[current] += line + "\n"
    return out


def _paths(body: str) -> list[str]:
    return [p for p in re.findall(r"`([^`\n]+)`", body) if "/" in p or re.search(r"\.\w{1,5}$", p)]


def _exists(root: Path, pattern: str) -> bool:
    if any(ch in pattern for ch in "*?["):
        return any(root.glob(pattern))
    return (root / pattern).exists()


def run_contract(root: Path, run_id: str) -> Report:
    rep = Report()
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", run_id):
        rep.add(False, "run.id", f"bad run id '{run_id}'")
        return rep
    run_dir = root / "qa" / "runs" / run_id
    path = run_dir / "preflight.md"
    if not path.exists():
        rep.add(False, "run.preflight", f"qa/runs/{run_id}/preflight.md missing")
        return rep
    text = path.read_text(encoding="utf-8")
    sections = split_sections(text)

    missing = [h for h in RUN_HEADINGS if h.casefold() not in sections]
    empty = [h for h in RUN_HEADINGS if h.casefold() in sections and not sections[h.casefold()].strip()]
    if missing or empty:
        detail = "; ".join(filter(None, ["missing: " + ", ".join(missing) if missing else "",
                                         "empty: " + ", ".join(empty) if empty else ""]))
        rep.add(False, "run.headings", detail)
    else:
        rep.add(True, "run.headings", "all 7 sections present")

    gone = [p for h in ("inputs", "critical items") for p in _paths(sections.get(h, ""))
            if not _exists(root, p)]
    rep.add(not gone, "run.inputs", "missing: " + ", ".join(gone) if gone else "every named input exists")

    capped = [ln.strip() for ln in sections.get("critical items", "").splitlines()
              if re.search(r"\bmissing\b|\bcapped\b", ln, re.I)]
    rep.add(not capped, "run.critical", "STOP: critical item capped by a missing input: " + "; ".join(capped)
            if capped else "no critical item capped by a missing input")

    upstream = sections.get("upstream", "")
    problems = []
    for p in _paths(upstream):
        vp = root / p
        if not vp.exists():
            problems.append(f"{p} missing")
            continue
        if verdict_result(vp) != "PASS":
            problems.append(f"{p} is not PASS")
        sr = verdict_check.second_read_path(vp)
        if not sr.exists() or verdict_result(sr) != "PASS":
            problems.append(f"{p} has no PASS second read")
    if not _paths(upstream) and upstream.strip() and not re.search(r"\bnone\b", upstream, re.I):
        problems.append("Upstream names no verdict path and does not say 'none'")
    rep.add(not problems, "run.upstream", "; ".join(problems) if problems else "upstream verdicts PASS with second reads")

    priors = sorted(p for p in (root / "qa" / "verdicts" / run_id).glob("*.md")
                    if verdict_check.is_verdict_file(p) and not p.name.endswith(verdict_check.SECOND_READ_SUFFIX))
    unlisted = [p.name for p in priors if p.name not in text]
    expected = round_from(priors)
    m = re.search(r"^\s*(?:[-*]\s*)?\**Round\**:?\**\s*(\d+)", text, re.M | re.I)
    if not m:
        rep.add(False, "run.round", f"no 'Round: N' line (expected round {expected})")
    elif int(m.group(1)) != expected:
        rep.add(False, "run.round", f"Round {m.group(1)} but failed priors + 1 = {expected}")
    elif unlisted:
        rep.add(False, "run.round", "prior verdicts not listed: " + ", ".join(unlisted))
    elif expected >= 3 and not (run_dir / "founder-yes.md").exists():
        rep.add(False, "run.round", f"round {expected} needs qa/runs/{run_id}/founder-yes.md")
    else:
        rep.add(True, "run.round", f"round {expected}; {len(priors)} prior verdict(s) listed")
    return rep


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="G0 preflight and the run contract (fails closed).")
    parser.add_argument("--release", action="store_true", help="run the G0 release checks")
    parser.add_argument("--run", metavar="ID", help="check qa/runs/<ID>/preflight.md")
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root")
    parser.add_argument("--today", help="date for the freshness rule (YYYY-MM-DD; default: today)")
    args = parser.parse_args(argv)
    if not args.release and not args.run:
        parser.print_usage(sys.stderr)
        print("preflight: give --release and/or --run <id>", file=sys.stderr)
        return 2
    try:
        today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    except ValueError:
        print(f"preflight: bad --today '{args.today}'", file=sys.stderr)
        return 2
    root = args.root.resolve()
    rep = Report()
    if args.release:
        rep.lines += release(root, today).lines
    if args.run:
        try:
            rep.lines += run_contract(root, args.run).lines
        except Exception as exc:  # fail closed
            rep.add(False, "run", f"could not run: {type(exc).__name__}: {exc}")
    rep.print()
    return 0 if rep.ok else 1


if __name__ == "__main__":
    sys.exit(main())
