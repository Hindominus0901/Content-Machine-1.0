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

The build system, modules, evals and QA arrive phase by phase (see `docs/PLAN.md`). This README gains build, lint, eval and release instructions as they land.

## Status

Phase 0 (foundations) is in progress.
