# Build system contract

How the source tree compiles into two editions (EN and VN) and every target. Every tool is **standard-library Python 3.11+** (`tomllib`, `zipfile`, `hashlib`, `unicodedata`). There are no third-party dependencies, so the build runs anywhere, CI included.

```
python3 tools/build.py --edition all        # render + assemble dist/<edition>/ and dist/maintainer/
python3 tools/lint.py                       # G1 deterministic gate (dev mode)
python3 tools/lint.py --release             # G1 + release-only rules (PENDING_VN signed, no [VERIFY] limits, fresh dates)
python3 tools/package.py                    # deterministic zips from dist/<edition>/
python3 -m unittest discover -s tools/tests # tool tests + must-fail lint fixtures
```

## 1. Targets

A **target** is one shipped artifact family. Prose can switch on targets with flags (§4).

| Target flag | Output (per edition) | Source |
|---|---|---|
| `kit` | `1-INSTRUCTIONS.txt` (the Project instruction block) | `core/<lang>/start-block.md` |
| `phone` | `PHONE-STARTER.txt` | `core/<lang>/start-block.md` rendered with `phone` (or `core/<lang>/phone-starter.md` if present) |
| `method` | `CONTENT-MACHINE-<EN|VN>.md` | `core/method.toml` `[method]` anchors → module sections |
| `grow` | `Level-ups/<RESEARCH|LAUNCH|CAMPAIGNS|BOARD|STRATEGY|HOOKS|PLAYBOOK|BANKS|COPY>-<EN|VN>.md`, `Level-ups/Board/*.csv` | `core/method.toml` `[levelup.<area>]` anchors → module sections; `templates/sheets/<lang>/*.csv` |
| `skill` | `Level-ups/autopilot/<skill_name>.zip` → `<skill_name>/SKILL.md`, `references/*.md`, `scripts/ship_lint.py` | `core/SKILL.md.tmpl`, `core/method.toml` `[skill]` references, `tools/shiplint.py` |
| `task` | Task texts (nudge, standalone, connected, daily machine) printed by the machine in-session; samples rendered to `dist/maintainer/tasks/` for lint | `automation/*.tmpl`, listed in `automation/tasks.toml` |
| `help` | `Help/*.html`, `START-HERE.html` | `guides/*.tmpl` |
| `site` | `site/index.html` (hosted setup page) | `guides/setup-page.tmpl` |

`<lang>` is the edition's prose folder: `en` or `vn`. The edition's `method_prose` setting picks it; the VN edition is fully Vietnamese.

## 2. Editions and strings

**`editions/<id>.toml`:**

```toml
[edition]
id = "en"                    # en | vn
lang = "en"                  # prose folder under core/ and modules/
name = "Content Machine"     # the brand name lives in this one field
skill_name = "content-machine"
file_suffix = "EN"           # CONTENT-MACHINE-EN.md, RESEARCH-EN.md, LAUNCH-EN.md ...
zip_name = "Content-Machine-EN"

[params]                     # {{param}} values used in prose and templates
currency = "$"
# ...

[pending]                    # VN only: key = { default = <safe default>, reason = "..." }
```

**`editions/vn.acceptance.toml`.** The founder signs each PENDING key here before release:

```toml
[accepted.platform_priority]
default = "..."
signed_by = "founder"
date = "2026-..-.."
```

`lint --release` fails if any pending key lacks a signed row.

**`strings/en.toml`** holds every line the coach can read that is not method prose: verdict lines, checklists, commands, mic tips, setup-page copy, task text the coach reads. The keys are flat and dotted:

```toml
[strings]
"verdict.ready" = "Ready to {verb} · I'd post it: {evidence}"
```

**`strings/vn.toml`** has the same keys. Each value is an inline table that carries the hash of the EN text it was written from:

```toml
[strings]
"verdict.ready" = { text = "Sẵn sàng {verb} · Mình sẽ đăng: {evidence}", src = "3f9a1c2b7d" }
```

- `src` = the first 10 hex characters of the sha256 of the NFC-normalised EN text.
- Lint fails when a key is missing in VN (**parity**) or `src` no longer matches EN (**stale**).
- `{name}` placeholders are runtime slots that the model fills. Render leaves them untouched. Lint checks that EN and VN use the same placeholder set.

## 3. Prose files and sections

Model-facing prose lives in `core/<lang>/*.md` and `modules/<lang>/*.md`. A file is a sequence of **sections**. Each section opens with a marker comment:

```markdown
<!-- @section talk.core -->
## Weekly Talk
...
<!-- @section talk.mini -->
...
```

- Section IDs are `<module>.<name>` and are unique across the edition.
- The text before the first marker is the file preamble. It is ignored in assembly.
- VN sections carry their EN source hash: `<!-- @section talk.core src=3f9a1c2b7d -->`. The hash is the first 10 hex characters of the sha256 of the NFC EN section body, after its marker line and with leading and trailing whitespace stripped.
- Lint fails on:
  - an EN section with no VN twin, or a VN section with no EN twin;
  - a stale `src`;
  - duplicate IDs.
- Render strips every marker. Shipped files never contain `@section`.
- A section may carry `kind=script` (a script template). Every such section must print a verdict line (`{{t:verdict.` …) — lint E146.
- Prose names hub properties as `` `hub:Status` ``. Lint E160 checks each name against `schemas/hub.toml`.
- A line that must quote a banned phrase (e.g. a rule "never write 'fill in'") ends with `<!-- lint-ok:E143 -->`. Render strips the waiver.

**`core/method.toml`** assembles targets from sections. Selectors are exact IDs or `module.*`. Anchor ids are unique across the method file and all level-up files (E161), so prose can point at `§CM-<ID>` and the model finds it in whichever file holds it. A `[levelup.<area>]` table may also carry `assets` and `assets_from` (a folder under `Level-ups/` and the source folder, `{lang}` filled) for files the coach uses next to the level-up; the board table ships its five CSVs this way.

```toml
[method]                       # CONTENT-MACHINE-<SUFFIX>.md, the Day-0 kit method file
title_key = "method.title"     # strings key for the file title
[[method.anchor]]
id = "TALK"                    # rendered as a heading carrying "§CM-TALK"
sections = ["talk.core", "talk.mini"]

[levelup.launch]               # Level-ups/LAUNCH-<SUFFIX>.md: one table per area (research, launch, campaigns, board, strategy, hooks, playbook, banks, copy)
file = "LAUNCH"                # the file name stem
skill = "cm-launch"            # the plugin's companion skill: cm-launch-<edition>
title_key = "levelup.launch.title"
budget = "levelup_launch"      # platform/targets.toml budget for the file (E101)
[[levelup.launch.anchor]]      # same shape as [[method.anchor]]
id = "LAUNCH-BRIEF"
sections = ["launch-plan.grow-brief"]

[skill]                        # Level-3 skill references, one file per entry
[[skill.reference]]
file = "setup.md"
sections = ["setup.*", "message.*"]
module = "setup"               # router row providing the WHEN TO USE header
formats = ["native-short"]     # format-checks.toml entries for the CHECK BEFORE ANSWERING footer
```

## 4. Template language (`tools/render.py`)

Prose and templates use one small, deterministic syntax. No Jinja.

| Syntax | Meaning |
|---|---|
| `{{param}}` | Edition param from `[params]`, or `[edition]` fields (`{{name}}`, `{{skill_name}}`) |
| `{{t:key}}` | The edition's string for `key` (EN text, or VN `text`) |
| `{{#if flag}}…{{else}}…{{/if}}` | Keep a branch by flag. Flags are the edition id (`en`, `vn`), the target (`kit`, `phone`, `method`, `grow`, `skill`, `task`, `help`, `site`) and the extra build flags (`connected`, `standalone`). `{{#if a,b}}` means a OR b. Blocks may nest |
| `{{#unless flag}}…{{/unless}}` | The inverse |
| `{{>section.id}}` | Include another section of the same edition's prose folder, rendered with the same flags (≤4 levels). One source for text shared by several targets, e.g. the Ship Check card in the start-block, SKILL.md and task templates |
| `{name}` (single braces) | A runtime slot the model fills. Left as is |

Unknown params, unknown string keys and unbalanced blocks are **errors**, never silent blanks.

Every rendered text is NFC-normalised and ends with exactly one newline.

**Skill references.** `render.py` wraps each one:
- **Header:** the output-contract line (`{{t:contract.output}}`), then `WHEN TO USE:` (the router row's trigger text), then `RULES:` (the router row's rules).
- **Footer:** `CHECK BEFORE ANSWERING:` with the yes/no lines from `core/format-checks.toml` for the reference's `formats` (≤5 lines), then the output-contract line repeated (the "instruction sandwich").
- A reference over 100 lines gets an automatic table of contents.

## 5. Router, format checks, targets

- **`core/router.toml`.** One `[[route]]` per job:
  - `id`, `module`;
  - `trigger` (≤200 characters);
  - `rules` (≤3 short lines);
  - `loads` (≤4 reference files);
  - `writes`;
  - `phrases.en` / `phrases.vn` (command phrases and synonyms; VN accepts spellings without diacritics).

  Lint asserts:
  - every skill reference is reachable from a route;
  - every route loads ≤4 files that exist;
  - every method anchor is named by the kit's start-block router.
- **`core/format-checks.toml`:** `[format.<id>]` with `checks = ["…", …]`, at most 5 yes/no lines per format and per language (`checks_vn`).
- **`schemas/*.toml`:** the hub (Notion + Sheets), Slot and Run keys, Bank types and the Brand Card. `tools/cmschema.py` loads and validates them together; `tools/hub_build_prompt.py` renders the Notion build prompt and Sheets CSVs from them (`python3 tools/hub_build_prompt.py --edition all`).
- **`platform/targets.toml`:** limits and budgets (see its header). `build.py` writes the size of each built artifact and its % of budget into `dist/maintainer/manifest.json`.

## 6. Build outputs

```
dist/<edition>/                          → zipped by package.py as <zip_name>-v<VERSION>.zip
  START-HERE.html
  1-INSTRUCTIONS.txt
  CONTENT-MACHINE-<SUFFIX>.md
  CONTENT-MACHINE-<SUFFIX>-1-FILE.md     ChatGPT one-file kit (below)
  PHONE-STARTER.txt
  Help/…
  Level-ups/RESEARCH-<SUFFIX>.md         one level-up file per area, each within its own budget (below)
  Level-ups/LAUNCH-<SUFFIX>.md
  Level-ups/CAMPAIGNS-<SUFFIX>.md
  Level-ups/BOARD-<SUFFIX>.md
  Level-ups/STRATEGY-<SUFFIX>.md
  Level-ups/HOOKS-<SUFFIX>.md
  Level-ups/PLAYBOOK-<SUFFIX>.md
  Level-ups/BANKS-<SUFFIX>.md
  Level-ups/COPY-<SUFFIX>.md
  Level-ups/Board/*.csv                  the five header-row files the board setup imports
  Level-ups/autopilot/<skill_name>.zip
dist/content-machine-plugin.zip          one plugin for Claude and ChatGPT, both editions, with companion skills and agents (below)
dist/site/<edition>/index.html
dist/maintainer/manifest.json            sha256 + bytes + NFC chars + lines + % of budget per artifact
dist/maintainer/tasks/<edition>/*.txt    rendered task samples (lint budgets)
dist/maintainer/notion-build-prompt-<edition>.md, sheets-<edition>/*.csv
```

**Level-up files.** `build.py` writes one file per `[levelup.<area>]` table of `core/method.toml`: `Level-ups/<FILE>-<SUFFIX>.md` for RESEARCH, LAUNCH, CAMPAIGNS, BOARD, STRATEGY, HOOKS, PLAYBOOK, BANKS and COPY (nine files since v13, 9 Oct 2026), in each edition. A file opens with a title line (strings key `levelup.<area>.title`) and holds one `## §CM-<ID> · <title>` block per anchor, the title coming from `anchor.<id in lower case>`; unlike the method file it does not repeat the output contract line (the kit's instruction block in a Project, or the companion skill in the plugin, carries it). The `grow` target flag renders it. Each file has its own byte budget (`budgets.levelup_<area>`, EN / VN bytes: LAUNCH 30,720 / 30,720 (raised from 24,576 on 2026-10-07); STRATEGY 36,864 / 36,864; HOOKS 45,056 / 58,368 and CAMPAIGNS 53,248 / 72,704, each about 15% over its measured size; since v13 (9 Oct 2026) RESEARCH 41,984 / 54,272 (channels, audience, niche), BOARD 35,840 / 47,104 (the hub and its tasks), PLAYBOOK 34,816 / 45,056 (engine, tiers, lines, calendar, document), BANKS 32,768 / 40,960 and COPY 40,960 / 53,248; lint E101) and every section it pulls in stays within `budgets.method_section` (one retrieval chunk; an anchor may hold two or three sections, so the check is per section, E101). A coach adds only the files the job needs: in a Project, one upload each (the kit's LEVEL-UPS line names the file for each job, and its `levelup.offer_grow` line asks for it); in the plugin nothing, because each file also sits next to its companion skill. `Level-ups/Board/` holds the five header-row CSVs that `§CM-BOARD` step 2 tells the coach to import into one Google Sheet; their column order is checked against `schemas/hub.toml [campaign_board]`.

**Nudge texts.** `automation/tasks.toml` lists the scheduled nudges as data (`[[task]]`: id, template, section; `[caps]`, `[catch_up]`, `[launch_mode]`, `[apps.*]`). Each `automation/task-nudge*.tmpl` is `{{>automation.grow-task-<x>}}`; the `task` target renders it for both editions to `dist/maintainer/tasks/<edition>/<stem>.txt` with the `task_nudge` budget (900 characters, NFC; every stem that starts `task-nudge` shares it) and the task id in the manifest. A task that names a missing template or section stops the build (E161); lint checks `[caps] max_chars_filled` against the budget. Nudge texts are not exempt from the budget, only from the Ship Check card (they hand over to the project or the skill).

**The hub spec.** `templates/notion/workspace.toml` (v13, 9 Oct 2026) is the data behind §CM-HUB-NOTION: the root page 'Content Machine — {name}', its databases and properties (names in each edition's language: `name` / `name_vn`), views and the fence the machine builds inside. It is read by the hub prose and tooling, not rendered into a shipped file; `schemas/hub.toml [hub]` names it the default hub (the campaign-board Google Sheet is the fallback). Scheduled tasks since v13: `automation/tasks.toml` lists week, today, numbers, claude, monthly and launch; the monthly text is `automation/task-nudge-monthly.tmpl` (same 900-character budget).

**Zips are deterministic.** Entries are sorted, timestamps fixed at 1980-01-01 00:00, permissions fixed, and dotfiles, `__MACOSX` and `.DS_Store` are never included (the one exception is the plugin's `.claude-plugin/` folder, below). File names are ASCII only.

**Portable kits.** Two outputs carry the kit and the method file outside a Project, both built from `dist/<edition>/` by `tools/build.py`:

- **`dist/content-machine-plugin.zip`** is one plugin for both apps and both editions, in Claude's plugin format: `content-machine/.claude-plugin/plugin.json` (name, `version` from `VERSION`, a bilingual description), `README.md` (a bilingual install note) and one skill per edition, `skills/content-machine-vn/` and `skills/content-machine-en/`, each with a `SKILL.md` and its method file next to it. **Every skill works from its `SKILL.md` alone**: in claude.ai the files bundled next to a SKILL.md are not readable without code execution (founder test v10: the setup check printed "✗ file phương pháp (chế độ gọn)" and the run had no method). The main `SKILL.md` is a front matter (name, a description of at most 200 characters), a one-line pointer (the method file is inside this skill, under `METHOD` / `PHƯƠNG PHÁP` below, and counts as the method file for the setup check; with one sentence naming the companion skills), the edition's instruction block, then `## METHOD (CONTENT-MACHINE-EN.md)` / `## PHƯƠNG PHÁP (CONTENT-MACHINE-VN.md)` and the whole method file, `## §CM-` anchors untouched. The method file next to it stays, for apps that can read it. With `plugin/companions.toml` the plugin also holds, per edition and per `[levelup.<area>]`, a **companion skill** `skills/cm-<area>-<edition>/` (`cm-research-en`, `cm-launch-vn`, `cm-hooks-en`, `cm-campaigns-vn`, `cm-banks-en`, `cm-copy-vn` ... 18 in all, 20 skills with the two main ones): a `SKILL.md` whose front matter is `name` (= the folder) and a quoted `description` of at most 200 characters in the edition's language that names the plain trigger phrases, then a body (the output contract line; speak as the main skill does, with the same Brand Card, address, voice and house rules and one NEXT line; a job-to-`§CM-` list so the model reads only the part it needs; the house rules; the harness: with subagents or parallel tasks split research by source and the week's pieces by piece and have a separate reviewer read before printing, browse only with the coach's own Claude in Chrome or ChatGPT Work and its browser after asking once), then `## FILE (<FILE>-<SUFFIX>.md)` and the area's level-up file in full as built in `dist/<edition>/Level-ups/`, and for the board skill `## FILES IN Board/` (`## FILE TRONG Board/`) with the five header rows, one ` ```csv ` block each; the level-up file and the `Board/*.csv` also sit next to `SKILL.md`. The words around the files are in `plugin/companions.toml` (model-facing text, so not in `strings/`). `plugin/agents/*.md` are copied to `content-machine/agents/` (Claude Code and Cowork load them; claude.ai chat loads skills only): `cm-researcher` (one source per run, read-only, people by role, returns verbatim buyer lines and where), `cm-listener` (KEEP needs 2+ people in 2+ places, else WATCH), `cm-writer` (one piece per run in the coach's voice) and `cm-reviewer` (an independent second read that flags and never rewrites). Each agent has a front matter `name` (= the file name) and `description` and at most 60 lines (E161). The manifest records every plugin `SKILL.md`'s size (`skill_md_bytes`); one over 120 KB adds a manifest note and a build warning on stderr, and stops nothing. `lint` reads the built zip: every skill the sources promise is there with a valid front matter (E102) and its level-up file byte for byte (E170), every `§CM-` id a skill names exists (E130), the agents are short (E103). If a level-up file is not built yet the plugin is skipped with a note, like any later-phase target. The coach installs it in Claude with Customize → Plugins → Add → Upload plugin, and in ChatGPT with Settings → Security and login → Developer mode → Plugins → upload (OpenAI's plugin portal accepts a Claude plugin archive and converts it, so there is no second package), then types `Bắt đầu` or `Start`. It is a root file: `package.py` zips only `dist/<edition>/` and `build_sha256` hashes only those folders, so hand it out next to the release zips. `build.py` writes it itself (`portable_zip`, same sorted, fixed-date, fixed-mode rules) because `make_zip` drops dotfiles and a Claude plugin must hold `.claude-plugin/plugin.json`. Check it with `claude plugin validate <extracted content-machine folder>` (and the same on its `skills/` and `agents/` folders, which validates the components).
- **`dist/<edition>/CONTENT-MACHINE-<SUFFIX>-1-FILE.md`** is the fallback for a ChatGPT account without plugins: a short header telling the model what the file is, the instruction block, then the method file (under `METHOD` / `PHƯƠNG PHÁP`). The coach attaches this one file in a ChatGPT chat and types `Bắt đầu` (VN) or `Start` (EN). It ships in the edition's release zip.

Both carry the instruction block with its setup-check phrase and its save line swapped. The check phrase (`PORTABLE[<lang>]["check_from"]` → `check_to`: "Check for CONTENT-MACHINE-EN.md and the newest BRAND CARD" gains "(it is the METHOD section below, already in this text)") makes the "✓ method file" line true where the method is a section of the same text; unlike the save line this swap is soft, so a kit edit that moves the phrase adds a manifest note instead of stopping the build. The save line: a plugin or one-file chat is not a Project, so the "Save to project" and "Add text content" line becomes strings key `portable.save` (copy the card and keep it; next day say `tiếp`/`next`, in a new chat paste the card first). The kit line being replaced is `PORTABLE[<lang>]["save_from"]` in `build.py`, and the build stops with E170 unless the rendered kit holds it exactly once, so a kit edit that touches that line must update `build.py` too. The other texts (skill description, pointer, one-file header, README) are `PORTABLE` constants in `build.py`, not strings: strings are coach-visible and E140 bars `§CM` from them. Without `portable.save` both outputs are skipped like any later-phase target; the plugin needs both editions, and a one-edition build reads the other from `dist/` or, if it cannot, removes an older plugin zip.

A missing source for a later-phase target (for example `guides/` before P6) is skipped with a note in the manifest, not an error. `lint --release` turns every skipped target into an error.

## 7. Lint codes (G1)

Each finding has a stable code (`E` = error, `W` = warning), so fixtures can assert them.

| Code | Rule |
|---|---|
| E101 | Budget exceeded (artifact vs `targets.toml` budget, NFC chars, bytes or lines): the method file and each level-up file, each method anchor and each section of a level-up anchor (`method_section`), each task text |
| E102 | Skill name or description invalid (length, charset, folder match, forbidden words), in the Autopilot skill and in every plugin skill and agent front matter |
| E103 | Reference over 150 lines or 9 KB; references over 200 KB total; a route loads more than 4 files; a plugin agent over 60 lines |
| E110 | VN string missing (parity), including a `trigger_vn` / `rules_vn` (router) or `checks_vn` (format checks) that a skill reference needs |
| E111 | VN string stale (`src` hash mismatch) |
| E112 | Placeholder set differs between EN and VN |
| E113 | VN section missing, orphaned or stale |
| E114 | Duplicate section ID |
| E120 | PENDING_VN key not accepted (release) |
| E121 | `verified_on` older than `max_age_days`, or a release-blocking limit still `VERIFY` (release) |
| E122 | Limit marked VERIFY carries a date, or a verified limit has no date |
| E130 | Router: a route loads a missing file, a reference is unreachable, or a kit anchor is not named in the start-block; a `§CM-<ID>` in a built method file, level-up file or companion skill that no anchor has |
| E131 | Instruction sandwich missing (contract line at top and bottom of a reference or the start-block) |
| E132 | Ship Check card missing from the start-block, SKILL.md or a task template |
| E140 | Deny-listed jargon in coach-visible text (`locales/<lang>/deny-list.txt`) |
| E141 | Banned AI tell or calque in shipped examples or strings (`locales/<lang>/banned-tells.txt`) |
| E142 | A Matt Gray framework name anywhere in shipped text |
| E143 | Template-fill wording in coach text ("fill in", "fill out", "điền vào") |
| E144 | Possible PII (email, phone number, @handle) in shipped text |
| E145 | A date or "currently" outside `locales/<lang>/platform-notes.md` |
| E146 | A template with no verdict line (a script template missing `{{t:verdict.` usage) |
| E150 | Non-ASCII file name in dist |
| E151 | Dotfile, `__MACOSX` or `.DS_Store` in a zip |
| E152 | Non-deterministic zip (rebuilding gives a different sha256) |
| E153 | `qa/` or `evals/` content inside a shipped zip |
| E160 | Unknown hub property name used in prose (not in `schemas/hub.toml`) |
| E161 | Bad TOML, or a schema file missing a required key (`tools/cmschema.py` checks `schemas/*.toml` as a set) |
| E170 | Render error (unknown param or string key, unbalanced block), including an anchor with sections but no `anchor.<id>` title string; a plugin skill or agent the sources promise that is missing, or a level-up file in the plugin that differs from `dist/<edition>/Level-ups/` |
| W2xx | Warnings: budget above 90%, a string unused by any template, a section unused by any target |

## 8. Runtime lint and graders

**`tools/cmcore/checks.py`** is the shared check core, standard library only, with no repo imports. Two things use it:
- **`tools/shiplint.py`** is the runtime lint. It is copied into the skill as `scripts/ship_lint.py`, so it must be a single self-contained file. `build.py` inlines `cmcore/checks.py` into it.
- **`evals/graders.py`** is the transcript graders I1–I18.

This keeps the runtime and the build in agreement (QA spec §5.1 G1).

## 9. Verdict files

Verdict files follow `docs/research/wf12-qa-spec.md` §5.5. `tools/verdict_check.py` validates:
- the four fixed first lines (`Result:`, `Score:`, `Critical items failed:`, `Not run:`);
- the header table;
- no conditional-pass wording;
- no praise words;
- a matching `.second-read.md` for every PASS.
