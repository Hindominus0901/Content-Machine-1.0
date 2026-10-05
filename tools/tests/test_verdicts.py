"""Tests for tools/verdict_check.py and tools/preflight.py on temporary repos."""
from __future__ import annotations

import contextlib
import datetime as dt
import io
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))

import preflight  # noqa: E402
import verdict_check  # noqa: E402


def verdict(result: str = "PASS", score: str = "18/20", critical: str = "none", not_run: str = "none",
            producer: str = "claude-opus-5-5 · high", reviewer: str = "claude-sonnet-5 · high",
            body: str = "", scorecard: str = '{"result": "PASS", "score": "18/20"}') -> str:
    return textwrap.dedent(f"""\
        Result: {result}
        Score: {score}
        Critical items failed: {critical}
        Not run: {not_run}

        | Field | Value |
        |---|---|
        | Subject at commit | modules/en/setup.md @ e70891d |
        | Build sha | 3f9a1c2b7d4e5f60718293a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4 |
        | Edition and lane | en · S1 |
        | Producer | {producer} |
        | Reviewer | {reviewer} |
        | Inputs | evals/cases/setup.en.toml |

        ## Deterministic results
        lint: 0 errors.
        {body}

        Would a coach post this? Yes, the film-today script reads like the coach.
        <!-- scorecard {scorecard} -->
        """)


class TempDir(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel: str, text: str) -> Path:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(text), encoding="utf-8")
        return path

    def quiet(self, fn, *args) -> tuple[int, str]:
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            code = fn(list(args))
        return code, out.getvalue()


class VerdictCheckTests(TempDir):
    def pair(self, name: str = "setup-verdict.md", **kw) -> Path:
        path = self.write(f"qa/verdicts/p2-setup/{name}", verdict(**kw))
        self.write(f"qa/verdicts/p2-setup/{name[:-3]}.second-read.md",
                   verdict(reviewer="claude-opus-5-5 · max", scorecard='{"result": "PASS"}'))
        return path

    def errors(self, path: Path) -> list[str]:
        return verdict_check.check_file(path).errors

    def test_good_pass_with_second_read(self):
        path = self.pair()
        self.assertEqual(self.errors(path), [])
        code, out = self.quiet(verdict_check.main, str(self.root / "qa" / "verdicts"))
        self.assertEqual(code, 0, out)
        self.assertEqual(out.count("OK"), 2)

    def test_good_fail_needs_no_second_read(self):
        path = self.write("qa/verdicts/x/area-verdict.md",
                          verdict(result="FAIL", score="15/20", critical="2 (template-fill ask, setup run 2 turn 6)",
                                  scorecard='{"result": "FAIL"}'))
        self.assertEqual(self.errors(path), [])

    def test_first_lines_are_fixed(self):
        path = self.write("qa/verdicts/x/a-verdict.md", "# Verdict\n" + verdict(result="FAIL", scorecard="{}"))
        errs = self.errors(path)
        self.assertTrue(any("line 1" in e for e in errs), errs)
        path = self.write("qa/verdicts/x/b-verdict.md", verdict(result="PASS*", scorecard="{}"))
        self.assertTrue(any("line 1" in e for e in self.errors(path)))
        path = self.write("qa/verdicts/x/c-verdict.md", verdict(result="FAIL", score="21/20", scorecard="{}"))
        self.assertTrue(any("impossible" in e for e in self.errors(path)))

    def test_pass_with_critical_or_not_run_is_invalid(self):
        errs = self.errors(self.pair(critical="1 (fake testimonial)"))
        self.assertTrue(any("PASS with 1 critical" in e for e in errs), errs)
        errs = self.errors(self.pair(name="b-verdict.md", not_run="G4 blind tests"))
        self.assertTrue(any("not run counts as FAIL" in e for e in errs), errs)

    def test_producer_and_reviewer_must_differ(self):
        errs = self.errors(self.pair(reviewer="Claude-Opus-5-5 ·  high"))
        self.assertIn("header: producer and reviewer are the same", errs)

    def test_header_rows_required(self):
        text = verdict(result="FAIL", scorecard="{}").replace("| Build sha |", "| Notes |").replace(" @ e70891d", "")
        errs = self.errors(self.write("qa/verdicts/x/h-verdict.md", text))
        self.assertIn("header: Build sha row missing or without a hash", errs)
        self.assertIn("header: no commit hash on the Subject (or Commit) row", errs)

    def test_conditional_and_praise_wording(self):
        errs = self.errors(self.pair(body="Would pass after edits to beat 2. Great work overall."))
        self.assertTrue(any("conditional-pass wording" in e for e in errs), errs)
        self.assertTrue(any("praise words: great" in e for e in errs), errs)
        quoted = self.pair(name="q-verdict.md", body='Offending line quoted: "This is an amazing offer" (SG2).')
        self.assertEqual(self.errors(quoted), [])

    def test_pass_needs_passing_second_read(self):
        lone = self.write("qa/verdicts/y/lone-verdict.md", verdict())
        self.assertIn("PASS without a second read (lone-verdict.second-read.md)", self.errors(lone))
        path = self.write("qa/verdicts/y/two-verdict.md", verdict())
        self.write("qa/verdicts/y/two-verdict.second-read.md",
                   verdict(result="FAIL", score="14/20", critical="1 (number not in P-row)", scorecard="{}"))
        self.assertTrue(any("lower result stands" in e for e in self.errors(path)))

    def test_scorecard_must_parse_and_agree(self):
        errs = self.errors(self.pair(scorecard="{not json}"))
        self.assertTrue(any("scorecard is not valid JSON" in e for e in errs), errs)
        errs = self.errors(self.pair(name="d-verdict.md", scorecard='{"result": "FAIL"}'))
        self.assertTrue(any("scorecard result FAIL differs" in e for e in errs), errs)
        no_card = verdict(result="FAIL", scorecard="").replace("<!-- scorecard  -->", "")
        errs = self.errors(self.write("qa/verdicts/x/n-verdict.md", no_card))
        self.assertTrue(any("scorecard comment missing" in e for e in errs), errs)

    def test_cli_on_bad_folder_exits_1_and_missing_path_2(self):
        self.write("qa/verdicts/z/bad-verdict.md", "Result: maybe\n")
        code, out = self.quiet(verdict_check.main, str(self.root / "qa" / "verdicts"))
        self.assertEqual(code, 1)
        self.assertIn("FAIL", out)
        code, _ = self.quiet(verdict_check.main, str(self.root / "nowhere"))
        self.assertEqual(code, 2)


# ---------------------------------------------------------------- preflight: run contract

PREFLIGHT_MD = """\
# Preflight: p2-setup

Round: {round}

## Goal
Write modules/en/setup.md so Day 0 reaches the Map in 8 coach turns.

## Inputs
- `evals/cases/setup.en.toml`
- `evals/personas/en/*/persona.toml`

## Upstream
{upstream}

## Critical items
- SG1 trace: every number from `evals/personas/en/proof-coach/persona.toml`
{critical_extra}

## May write
- `modules/en/setup.md`

## Stop conditions
- A critical item is capped by a missing input.

## Never
- Real names, Matt Gray framework names, unverified platform facts.

## Prior verdicts
{priors}
"""


class RunContractTests(TempDir):
    def setUp(self):
        super().setUp()
        self.write("evals/cases/setup.en.toml", "[[case]]\nid = 'setup.en.001'\n")
        self.write("evals/personas/en/proof-coach/persona.toml", "id = 'proof-coach'\n")

    def contract(self, round: int = 1, upstream: str = "none", critical_extra: str = "", priors: str = "none") -> None:
        self.write("qa/runs/p2-setup/preflight.md",
                   PREFLIGHT_MD.format(round=round, upstream=upstream, critical_extra=critical_extra, priors=priors))

    def checks(self) -> dict[str, tuple[bool, str]]:
        rep = preflight.run_contract(self.root, "p2-setup")
        return {check: (ok, detail) for ok, check, detail in rep.lines}

    def test_good_contract(self):
        self.contract()
        checks = self.checks()
        self.assertTrue(all(ok for ok, _ in checks.values()), checks)
        code, out = self.quiet(preflight.main, "--run", "p2-setup", "--root", str(self.root))
        self.assertEqual(code, 0, out)

    def test_missing_and_empty_headings(self):
        text = PREFLIGHT_MD.format(round=1, upstream="none", critical_extra="", priors="none")
        text = text.replace("## Never\n- Real names, Matt Gray framework names, unverified platform facts.\n", "")
        text = text.replace("- `modules/en/setup.md`\n", "")
        self.write("qa/runs/p2-setup/preflight.md", text)
        ok, detail = self.checks()["run.headings"]
        self.assertFalse(ok)
        self.assertIn("missing: Never", detail)
        self.assertIn("empty: May write", detail)

    def test_missing_input_and_capped_item_stop(self):
        self.contract(critical_extra="- CC8 verbatim voice: MISSING `evals/personas/en/proof-coach/voice-samples.md`")
        checks = self.checks()
        self.assertFalse(checks["run.inputs"][0])
        self.assertIn("voice-samples.md", checks["run.inputs"][1])
        self.assertFalse(checks["run.critical"][0])
        self.assertIn("STOP", checks["run.critical"][1])

    def test_upstream_must_pass_with_second_read(self):
        self.write("qa/verdicts/p1-build/build-verdict.md", verdict())
        self.contract(upstream="- `qa/verdicts/p1-build/build-verdict.md`")
        ok, detail = self.checks()["run.upstream"]
        self.assertFalse(ok)
        self.assertIn("no PASS second read", detail)
        self.write("qa/verdicts/p1-build/build-verdict.second-read.md", verdict(reviewer="x · max"))
        self.assertTrue(self.checks()["run.upstream"][0])

    def test_round_counts_failed_priors(self):
        fail = verdict(result="FAIL", score="12/20", critical="1 (x)", scorecard="{}")
        self.write("qa/verdicts/p2-setup/setup-verdict.md", fail)
        self.contract(round=1, priors="none")
        ok, detail = self.checks()["run.round"]
        self.assertFalse(ok)
        self.assertIn("failed priors + 1 = 2", detail)
        self.contract(round=2, priors="none")
        ok, detail = self.checks()["run.round"]
        self.assertFalse(ok)
        self.assertIn("not listed: setup-verdict.md", detail)
        self.contract(round=2, priors="- qa/verdicts/p2-setup/setup-verdict.md (FAIL)")
        self.assertTrue(self.checks()["run.round"][0])

    def test_round_3_needs_founder_yes(self):
        fail = verdict(result="FAIL", score="12/20", critical="1 (x)", scorecard="{}")
        self.write("qa/verdicts/p2-setup/setup-verdict.md", fail)
        self.write("qa/verdicts/p2-setup/setup-r2-verdict.md", fail)
        self.contract(round=3, priors="- setup-verdict.md\n- setup-r2-verdict.md")
        ok, detail = self.checks()["run.round"]
        self.assertFalse(ok)
        self.assertIn("founder-yes.md", detail)
        self.write("qa/runs/p2-setup/founder-yes.md", "Yes, one more round. Founder, 2026-10-05.\n")
        self.assertTrue(self.checks()["run.round"][0])

    def test_missing_preflight_fails(self):
        code, out = self.quiet(preflight.main, "--run", "nope", "--root", str(self.root))
        self.assertEqual(code, 1)
        self.assertIn("FAIL run.preflight", out)


# ---------------------------------------------------------------- preflight: G0 release

class ReleaseTests(TempDir):
    TODAY = dt.date(2026, 10, 5)

    def setUp(self):
        super().setUp()
        self.write("VERSION", "1.1.0\n")
        self.write("CHANGELOG.md", "# Changelog\n\n## [1.1.0]\n- [buyer] Faster Day 0.\n\n## [1.0.0]\n- First.\n")
        (self.root / "qa" / "releases" / "v1.0.0").mkdir(parents=True)
        self.write("platform/targets.toml", """
            [meta]
            max_age_days = 90
            [limits.a]
            value = 1
            verified_on = "2026-09-01"
            [limits.b]
            value = ""
            evidence = "VERIFY"
            verified_on = ""
            [budgets.x]
            limit = "a"
            en = 1
            """)
        self.write("editions/en.toml", "[edition]\nid = 'en'\n")
        self.write("editions/vn.toml", "[edition]\nid = 'vn'\n[pending]\nword_rate = { default = 3.5, reason = 'x' }\n")
        self.write("editions/vn.acceptance.toml",
                   "[accepted.word_rate]\ndefault = 3.5\nsigned_by = 'founder'\ndate = '2026-10-01'\n")
        self.write("evals/acceptance.toml", "[cases]\nper_module_min = 2\nguardrails_min = 3\n")
        self.write("evals/registry.toml", """
            [modules.setup]
            status = "active"
            baseline = "evals/baselines/setup.toml"
            [modules.guardrails]
            status = "planned"
            baseline = ""
            """)
        self.write("evals/baselines/setup.toml", "edge = 8.1\n")
        for ed in ("en", "vn"):
            self.write(f"evals/cases/setup.{ed}.toml", "[[case]]\nid = 'a'\n[[case]]\nid = 'b'\n")
        self.write("qa/CALIBRATION.md", "# Calibration\n\njudge_validated: yes (v1.1.0)\n")

    def results(self) -> dict[str, tuple[bool, str]]:
        rep = preflight.release(self.root, self.TODAY)
        return {check: (ok, detail) for ok, check, detail in rep.lines}

    def test_all_green(self):
        res = self.results()
        self.assertTrue(all(ok for ok, _ in res.values()), res)
        code, out = self.quiet(preflight.main, "--release", "--root", str(self.root), "--today", "2026-10-05")
        self.assertEqual(code, 0, out)

    def test_version_and_changelog_bump(self):
        self.write("VERSION", "1.0.0\n")
        (self.root / "qa" / "releases" / "v1.0.1").mkdir()
        self.assertIn("not above the last release 1.0.1", self.results()["G0.version"][1])
        self.write("VERSION", "1.2.0\n")
        self.assertIn("no '## [1.2.0]' section", self.results()["G0.version"][1])

    def test_no_prior_release_passes(self):
        (self.root / "qa" / "releases" / "v1.0.0").rmdir()
        self.assertTrue(self.results()["G0.version"][0])

    def test_stale_or_missing_verified_on(self):
        self.write("platform/targets.toml", """
            [meta]
            max_age_days = 90
            [limits.a]
            verified_on = "2026-01-01"
            [limits.b]
            verified_on = ""
            release_blocking = true
            """)
        ok, detail = self.results()["G0.freshness"]
        self.assertFalse(ok)
        self.assertIn("a verified 277 days ago (max 90)", detail)
        self.assertIn("b has no verified_on", detail)

    def test_unsigned_pending_key(self):
        self.write("editions/vn.acceptance.toml", "[accepted.word_rate]\ndefault = 3.5\nsigned_by = ''\n")
        ok, detail = self.results()["G0.pending"]
        self.assertFalse(ok)
        self.assertIn("vn.word_rate", detail)

    def test_active_module_needs_cases_and_baseline(self):
        self.write("evals/cases/setup.vn.toml", "[[case]]\nid = 'a'\n")
        (self.root / "evals" / "baselines" / "setup.toml").unlink()
        ok, detail = self.results()["G0.modules"]
        self.assertFalse(ok)
        self.assertIn("setup.vn has 1 cases (min 2)", detail)
        self.assertIn("setup has no recorded baseline", detail)

    def test_shipped_module_must_be_active(self):
        self.write("modules/en/guardrails.md", "<!-- @section guardrails.core -->\nx\n")
        ok, detail = self.results()["G0.modules"]
        self.assertFalse(ok)
        self.assertIn("guardrails ships but is 'planned'", detail)

    def test_judge_must_be_validated_for_this_release(self):
        self.write("qa/CALIBRATION.md", "judge_validated: yes (v1.0.0)\n")
        self.assertFalse(self.results()["G0.judge"][0])
        self.write("qa/CALIBRATION.md", "## v1.1.0\njudge_validated: yes\n")
        self.assertTrue(self.results()["G0.judge"][0])
        self.write("qa/CALIBRATION.md", "judge_validated: no\n")
        self.assertFalse(self.results()["G0.judge"][0])

    def test_release_round(self):
        fail = verdict(result="FAIL", score="1/2", critical="1 (x)", scorecard="{}")
        self.write("qa/releases/v1.1.0/RELEASE-VERDICT.md", fail)
        self.write("qa/releases/v1.1.0/RELEASE-VERDICT-r2.md", fail)
        ok, detail = self.results()["G0.round"]
        self.assertFalse(ok)
        self.assertIn("round 3 needs the founder's written yes", detail)
        self.write("qa/releases/v1.1.0/founder-yes.md", "Yes.\n")
        ok, detail = self.results()["G0.round"]
        self.assertTrue(ok)
        self.assertIn("RELEASE-VERDICT.md (FAIL)", detail)

    def test_fails_closed_when_a_file_is_missing(self):
        (self.root / "evals" / "registry.toml").unlink()
        ok, detail = self.results()["G0.modules"]
        self.assertFalse(ok)
        self.assertIn("could not run", detail)

    def test_usage_error(self):
        code, _ = self.quiet(preflight.main)
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
