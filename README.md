# Content Machine 1.0

A drop-in content department for coaches, consultants and service businesses. Buyers load it into ChatGPT or Claude. From there it researches, finds their one message, plans series and writes scripts, and it checks every piece before handing it over. It ships as two editions built from one source: English (EN) and Vietnamese (VN).

This README is for maintainers. Buyers never see this repository.

## Where things are

| Path | What |
|---|---|
| `docs/PLAN.md` | The implementation plan: phases, gates and what the founder does |
| `docs/DECISIONS.md` | Founder decisions. These win over every other document |
| `docs/research/` | The research corpus and final specs (start with its README) |
| `docs/founder/phase0-checks.md` | Real-account checks that unlock the release |
| `platform/targets.toml` | Every platform limit, with its source and verification date, plus the budgets derived from them |
| `docs/BUILD.md` | The build, the lint codes, the runtime lint and graders, verdict files and packaging |
| `core/`, `modules/`, `strings/`, `editions/`, `plugin/` | The kit's sources (instruction blocks, method sections, strings, editions, the plugin's skills and agents) |
| `evals/` | Personas, cases, the run packets (`run.py`), the transcript graders (`graders.py`) and their thresholds (`acceptance.toml`); see `evals/README.md` |
| `qa/standards/` | The build-only judge rubrics; `qa/runs/` the review rounds; `qa/releases/` the release verdicts |
| `docs/founder/real-account-test.md` | The founder's real-account checklist (Claude and ChatGPT, about 100 minutes) |
| `CHANGELOG.md` | What changed per version; `[buyer]` lines become the buyers' "What's new" page |

Build and check (from the repository root):

```
python3 tools/build.py --edition all      # renders dist/en, dist/vn, the plugin zip and dist/maintainer/manifest.json
python3 tools/lint.py                     # 0 errors expected (warnings are budget notes)
python3 -m unittest discover -s tools/tests
python3 tools/package.py                  # the edition zips; --release needs qa/releases/v<VERSION>/ with a PASS verdict
```

## Status

Version: see `VERSION` (1.3.10, build v13.10, 11 Oct 2026). Every phase's sources are built; the release verdict for this version (`qa/releases/v1.3.10/`) is not written yet, so `package.py --release` refuses it.
