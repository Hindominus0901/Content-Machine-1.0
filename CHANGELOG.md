# Changelog

Lines tagged `[buyer]` become the localised "What's new" page shipped to buyers. All other lines are for maintainers.

## [Unreleased]

### Added
- Research corpus, plan and founder decisions (`docs/`).
- Platform limits with sources and verification dates (`platform/targets.toml`).
- Phase-0 real-account checklist for the founder (`docs/founder/phase0-checks.md`).
- Level-up files: one per area per edition (`Level-ups/RESEARCH`, `LAUNCH`, `BOARD`, `STRATEGY` `-EN|VN.md`, each within 24,576 B), replacing the one GROW file; the board's five CSVs in `Level-ups/Board/`.
- Plugin: companion skills `cm-research`, `cm-launch`, `cm-board`, `cm-strategy` (`-en`, `-vn`) and four agents (`cm-researcher`, `cm-listener`, `cm-writer`, `cm-reviewer`) in `dist/content-machine-plugin.zip`; sources in `plugin/`.
- Nudge texts (`automation/tasks.toml`, `task-nudge*.tmpl`) are built and linted against the 900-character budget.
