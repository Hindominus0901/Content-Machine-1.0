# Changelog

Lines tagged `[buyer]` become the localised "What's new" page shipped to buyers. All other lines are for maintainers.

## [Unreleased]

### Added
- Research corpus, plan and founder decisions (`docs/`).
- Platform limits with sources and verification dates (`platform/targets.toml`).
- Phase-0 real-account checklist for the founder (`docs/founder/phase0-checks.md`).
- Level-up files: one per area per edition (`Level-ups/RESEARCH`, `LAUNCH`, `BOARD`, `STRATEGY` `-EN|VN.md`, each within 30,720 B since 7 Oct 2026, was 24,576 B), replacing the one GROW file; the board's five CSVs in `Level-ups/Board/`.
- Plugin: companion skills `cm-research`, `cm-launch`, `cm-board`, `cm-strategy` (`-en`, `-vn`) and four agents (`cm-researcher`, `cm-listener`, `cm-writer`, `cm-reviewer`) in `dist/content-machine-plugin.zip`; sources in `plugin/`.
- Two more level-up files and their companion skills: `Level-ups/HOOKS-EN|VN.md` (the hook library: over 100 hook shapes in 20 mechanisms, by surface; skill `cm-hooks`) and `Level-ups/CAMPAIGNS-EN|VN.md` (six launch campaigns with day cards and checkpoints, checklist, objections, FAQ, sales page, sequences, the live, live selling, timing, after; skill `cm-campaigns`). Sources `modules/{en,vn}/hook-library.md` and `launch-campaigns.md`; build-only rubrics `qa/standards/hook-library.md` and `launch-campaign.md`. The kit's LEVEL-UPS line routes hooks and titles to HOOKS and a launch to LAUNCH + CAMPAIGNS; the plugin now holds 16 skills.
- Nudge texts (`automation/tasks.toml`, `task-nudge*.tmpl`) are built and linted against the 900-character budget.
- Strategy depth from the Soo Wei Goh and Matt Gray audits (18 + 11 changes, merged where they overlap): buyer stages and plain names for steps, the self-check gift, a "before our call" message, title and hook shapes, form ranking, series, long-video section closers, self-test and description order, competitor standouts, pain and after lines (`modules/{en,vn}/strategy|ideas|packaging|fmt-long|character|research.md`). Coverage: `docs/research/strategy-coverage.md`. The kit (instruction blocks, method files) does not grow.

### Changed
- ChatGPT agent was removed in August 2026: the research access question, the helpers line, the companion skills and `cm-researcher` now name ChatGPT Work and its browser (`platform/targets.toml` `chatgpt_agent_mode_available`, checked 2026-10-07).
