# Changelog

Lines tagged `[buyer]` become the localised "What's new" page shipped to buyers. All other lines are for maintainers.

## [1.3.9] - 2026-10-11

Build v13.9: the readiness gaps from the founder's own app test (outside assessment of v13.8, 11 Oct 2026). VERSION now follows the build (13.9 → 1.3.9); it stayed 1.0.0 through v13.8.

### Changed
- One level-up rule per route. Plugin: each level-up is a companion skill that loads when its job comes up, nothing to upload (the main SKILL.md pointer and every companion body say so, and say that the method's "add the file" step is the Project route's). Project or folder: add the one Level-ups file the job needs. The board's setup (§CM-BOARD 2) names both routes: the download's Level-ups/Board folder, or the files handed over in the plugin.
- `plugin.json` version comes from VERSION (1.3.9, was 1.0.0 while the content was v13.8); its description names all nine companions (banks and copywriting were missing).
- No offer before week 2 outside a launch, written where the asks are chosen: Week 1's CONVERT piece asks for a reply, never a price (§CM-CTA-BANK 1, §CM-HOOK-CTA 1, §CM-COPY 2).
- One ask per piece in the examples: the email P.S. with "3 ways I can help" is now one call ask; the myth carousel asks for the keyword only; cart emails ask "join" (or, to EARLY replies, for the one question in the way), never "join or reply"; the belief-shift step asks for the story only.
- Launch and campaign pieces carry the added-details list under each piece ("Máy tự thêm: …", §CM-HUMANIZE) next to the voice pass; a coach who doesn't film gets a video's beats as a post (§CM-CAMPAIGNS 2, §CM-LAUNCH-POSTS).
- Kit: source check before print (every concrete detail traces to the coach's words, the Brand Card or a kept research line; facts never added; illustrative lines listed under the piece as "Máy tự thêm" / "Added by me").
- Kit: silent week cross-read (one scene/story per piece, belief line at most twice a week, `used` stories on the card); thin dump keeps the founder's lengths with the list and one story-first question.
- Kit: style (pet phrase once a piece, one particle a sentence, no em dash in VN pieces, one ask per piece, one-question "Cần" line); Week-1 convert slot asks for replies only; platform-neutral inbox replies; honest tier hours; §CM-TODAY plugin level-ups load on their own.

## [Before 1.3.9]

Everything from v1 to v13.8, built under VERSION 1.0.0 and never released on its own.


### Added
- Research corpus, plan and founder decisions (`docs/`).
- Platform limits with sources and verification dates (`platform/targets.toml`).
- Phase-0 real-account checklist for the founder (`docs/founder/phase0-checks.md`).
- Level-up files: one per area per edition (`Level-ups/RESEARCH`, `LAUNCH`, `BOARD`, `STRATEGY` `-EN|VN.md`, each within 30,720 B since 7 Oct 2026, was 24,576 B), replacing the one GROW file; the board's five CSVs in `Level-ups/Board/`.
- Plugin: companion skills `cm-research`, `cm-launch`, `cm-board`, `cm-strategy` (`-en`, `-vn`) and four agents (`cm-researcher`, `cm-listener`, `cm-writer`, `cm-reviewer`) in `dist/content-machine-plugin.zip`; sources in `plugin/`.
- Two more level-up files and their companion skills: `Level-ups/HOOKS-EN|VN.md` (the hook library: over 100 hook shapes in 20 mechanisms, by surface; skill `cm-hooks`) and `Level-ups/CAMPAIGNS-EN|VN.md` (six launch campaigns with day cards and checkpoints, checklist, objections, FAQ, sales page, sequences, the live, live selling, timing, after; skill `cm-campaigns`). Sources `modules/{en,vn}/hook-library.md` and `launch-campaigns.md`; build-only rubrics `qa/standards/hook-library.md` and `launch-campaign.md`. The kit's LEVEL-UPS line routes hooks and titles to HOOKS and a launch to LAUNCH + CAMPAIGNS; the plugin now holds 16 skills.
- Nudge texts (`automation/tasks.toml`, `task-nudge*.tmpl`) are built and linted against the 900-character budget.
- Strategy depth from the Soo Wei Goh and Matt Gray audits (18 + 11 changes, merged where they overlap): buyer stages and plain names for steps, the self-check gift, a "before our call" message, title and hook shapes, form ranking, series, long-video section closers, self-test and description order, competitor standouts, pain and after lines (`modules/{en,vn}/strategy|ideas|packaging|fmt-long|character|research.md`). Coverage: `docs/research/strategy-coverage.md`. The kit (instruction blocks, method files) does not grow.
- v13, "a content department in a box" (founder, 9 Oct 2026; `docs/DECISIONS.md`): the machine now offers choices step by step (§CM-OPTIONS: A/B/C, one recommended, in order, no vague endings), restores its state at chat start from memory, past chats, HUB.md and NICHE.md (§CM-MEMORY), researches the channels the coach likes, the competitors, their viewers and the niche before the strategy (§CM-CHANNELS, §CM-AUDIENCE, §CM-NICHE), builds the strategy in 8 steps (§CM-STRATEGY-ENGINE) with content lines, the three content types in depth and a 4-week calendar (§CM-CONTENT-LINES, §CM-TIERS, §CM-CALENDAR), keeps banks of asks, gifts, buyer words, stories and proof (§CM-BANKS and its parts), picks one writing framework per piece with storytelling and persuasion (§CM-COPY and its parts), and keeps a hub: a Notion workspace it builds plus HUB.md in the project, the Google Sheet as the fallback, and 4 scheduled tasks that read and write it (§CM-HUB-NOTION, §CM-HUB-MD, §CM-HUB-TASKS).
- Two more level-up files and companion skills: `Level-ups/BANKS-EN|VN.md` (skill `cm-banks`) and `Level-ups/COPY-EN|VN.md` (skill `cm-copy`); nine level-ups and 20 plugin skills in all. New modules `options`, `content-banks`, `copywriting`, `channel-research`; new standards `calendar`, `banks`, `copy-frameworks`, `channel-teardown`, `hub` (`qa/standards/`); the Notion hub spec `templates/notion/workspace.toml`; a monthly task text (`automation/task-nudge-monthly.tmpl`).
- Budgets: RESEARCH 41,984 / 54,272 B, BOARD 35,840 / 47,104, PLAYBOOK 34,816 / 45,056, BANKS 32,768 / 40,960, COPY 40,960 / 53,248 (EN / VN); the strategy document grew from 7 to 9 parts (evals `STRATEGY_PARTS`).

### Changed
- The comment keyword is a buyer phrase of 2 or more words (VN: 2 tiếng or more), in the hook library's CTA part too; the strategy document's offer and the level-up offers are A/B/C lines, not "Want …? Say 'yes'"; the Day-0 strategy may come in up to 3 steps (`evals/acceptance.toml [day0] strategy_max_steps`); Day 0's last reply offers the hub, the reminders offer moved to Day 1; `schemas/hub.toml` names the Notion workspace the default hub.
- ChatGPT agent was removed in August 2026: the research access question, the helpers line, the companion skills and `cm-researcher` now name ChatGPT Work and its browser (`platform/targets.toml` `chatgpt_agent_mode_available`, checked 2026-10-07).
