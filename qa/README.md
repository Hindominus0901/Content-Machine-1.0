# QA

Build-time quality assurance for Content Machine. **Nothing here ships.** Lint asserts that the zips exclude `qa/` and `evals/`.

The full system is specified in `docs/research/wf12-qa-spec.md`. This page is the working summary.

## Doctrine (ported from the founder's agency QA)

1. **One question.** Would this embarrass the coach, or cost a buyer's trust, if it were posted as it is?
2. **Nothing invented.** A missing fact becomes a visible `[NEEDS: …]` / `[CẦN BẠN: …]`, never a guess. Blank is not zero.
3. **Cheapest first.** Deterministic checks, then the rubric, then lenses, then a human. Never spend judgment on a piece that failed a lint.
4. **Never claim a check that didn't run.** "Not run" is not "clean"; at build it counts as FAIL.
5. **Uncertain means fail.** At build, uncertain = FAIL. At runtime, uncertain = cut the line or downgrade the piece.
6. **No conditional pass, no praise.** The first line is `Result: PASS` or `Result: FAIL`. "Pass after edits" is a FAIL that names the edits.
7. **Honesty over targets.** A shortfall reported as a shortfall passes. A shortfall dressed up fails.
8. **The reviewer is never the writer.** Producer and reviewer differ (model or effort, and always the context). The judge never sees module prose, self-scores or the lane.
9. **Two rounds, then the founder.** Round 2 fixes only the named items. If round 2 fails, the work stops and the founder gets a 1-page escalation.
10. **Rigor at build, quiet at runtime.** When the machine is wrong, fix the rubric or the module, never the verdict.

## Layout

| Path | What |
|---|---|
| `standards/` | One build-only rubric per artifact (G3 judge rubric and the source of eval cases) |
| `verdicts/<id>/` | Verdict files: `<area>-verdict.md` plus `.second-read.md`. Never edited; a new verdict supersedes |
| `runs/<id>/` | Build run contract: `preflight.md`, `self-audit.md`, frozen `self-score.md` |
| `releases/vX.Y.Z/` | `gates/G0…G9-verdict.md`, `smoke/`, `walkthrough/`, `blind/`, `RELEASE-VERDICT.md`, `SIGNOFF.md` |
| `LEDGER.md` | One row per verdict; honesty and score gaps |
| `CALIBRATION.md` | G3b runtime-vs-judge data per release; judge validation status |
| `rubric-proposals.md` | Proposed rubric changes from labels and misses |
| `incidents.md` | Real-world misses reported by coaches or testers |
| `inbox/` | Raw "send feedback" pastes and ad-hoc rejections, waiting to become labelled cases |

## Gates (release)

G0 preflight → G1 deterministic → G2 golden runs → G3 judge (+ G3b calibration) → G4 3× blind generative tests → G5 second read → G6 simulated walkthroughs → G7 platform smoke (human) → G8 human testers → G9 rounds and sign-off.

Pass rules: `wf12-qa-spec.md` §5.1, `wf11-ux-spec.md` §6, and `evals/acceptance.toml`. Every gate that is "not run" counts as FAIL.

## Recorded ceilings

Limits that are accepted on purpose and never waived silently.

- **Same-context runtime checker.** In a chat the checker is the writer. It is trusted only as far as G3b calibration proves.
- **ChatGPT has no code execution in the kit.** Counts are writing targets there, not checks (`lint: manual`).
- **Simulated golden runs are approximate.** One simulator plays both sides under leakage rules. G7/G8 real-account runs are the true test.
