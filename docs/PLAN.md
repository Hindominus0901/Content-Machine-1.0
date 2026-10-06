# Content Machine 1.0 — Implementation Plan (final)

## Context
- **Repo:** `Hindominus0901/Content-Machine-1.0`. It is empty except the placeholder file `yeah`.
- **Branch:** `claude/relaxed-einstein-h9m241`. Commit and push there; no PR unless asked.
- **Product:** a paid DIY pack for coaches, consultants and service businesses.
  - Two editions, EN and VN, built from one source.
  - Non-technical buyers load it into ChatGPT or Claude.
  - Two outcomes only: **reach**, and **trust → purchase**.
- **Buyer insight** (VN, verbatim): "Tôi biết rất nhiều thứ, nhưng tôi không biết nên muốn nói gì, và tôi sợ nói nhiều thứ quá thì bị loãng, và tôi ko biết nên nói cụ thể như nào để ra khách hàng."
- **Pain:** other products hand over formats and templates the buyer can't execute.
- **So the machine does the work in conversation:**
  - it picks ONE message (anti-dilution);
  - it asks for ≤1 real decision per session;
  - it hands back finished words;
  - it checks them silently;
  - every reply ends with one next step.
- **v1 scope:** research, ideation, scripting (words only), systemizing (hub plus 3 automations), launches, and QA. Design, editing and posting come later.
- **Status:** all research and design is done (12 workflows; specs in the scratchpad `research/` folder). In P0 they are committed to `docs/research/`.
- **Precedence when specs conflict:** founder decisions (Appendix A) > UX spec (`wf11-ux-spec.md`) > QA spec (`wf12-qa-spec.md`) > architecture spec (`arch-final-spec.md`) > other research. Known conflicts are settled under "Reconciliations" below.

## Added after approval: posts and channels you like or follow (5 Oct 2026)
Founder request: "user có thể đưa lên các bài hoặc các kênh mà họ thích hoặc theo dõi". Final spec: [research/wf13-inspiration-spec.md](research/wf13-inspiration-spec.md); decisions in [DECISIONS.md](DECISIONS.md).

- **Save first.** A screenshot, caption, "let me tell you" or link goes to the swipe file ("Posts you like"). The AI uses it later when planning, packaging, when the coach is stuck and in the monthly New slot.
- **"Your version" on request.** The post's shape, the coach's topic, stories and words.
- **Copying, translating or naming comparisons** on explicit request: done with one dated note, never blocked. Others' results are never presented as the coach's own.
- **Monthly "Your angle" card:** EVERYONE SAYS · NOBODY SAYS · YOU CAN SAY, from accounts the coach follows.
- **No new phrase. Day 0 untouched.**
- **Built across phases:**

  | Phase | Work |
  |---|---|
  | P0 | fixtures |
  | P1 patch | schemas, graders I19–I22, shiplint `--source` |
  | P2 | kit line + `§CM-LIKED` |
  | P3 | monthly angle |
  | P4 | skill references |
  | P5 | GROW channels + opt-in Browse |
  | P6 | house rule 3 |

## Added: Voice & Language as a first-class pillar (6 Oct 2026)
Founder: "Voice and Languages (how to say), Content Strategy (what to say)". Spec: [research/wf14-voice-language-spec.md](research/wf14-voice-language-spec.md).

- **What to say:** the Map.
- **How to say it:** the Voice Card. It is built from the dump, 2–3 pasted posts (invited in the Day-0 dump prompt, no extra turn) and the Weekly Talks, and refined by "not me:" / "I do say".
- **Shown:** one voice line on the Map; two lines on the Brand Card under WHAT YOU SAY / HOW YOU SAY IT.
- **VN audience address:** inferred and shown on the Map.
- **QA:** Ship Check VOICE step, graders I15 extension + I23, `voice` cases.
- **Built in P2:** schema, start-block, Ship Check, VOICE anchor, strings, fixtures, cases. This runs as a patch right after the EN method modules land.

## What we're building

### Coach journey (UX spec)
- **Install = the "Project kit".** Identical in ChatGPT and Claude: 4 steps, about 3 minutes.
  1. New project "Content Machine".
  2. Paste one instruction block.
  3. Add one method file, or paste it as text.
  4. New chat → paste "Start / Bắt đầu".
  - The first reply proves the install: `◆ Content Machine · Setup check: ✓ instructions ✓ method file`.
  - Compact mode runs Day 0 even with no file.
  - Other routes: a helper path (someone installs it in the coach's account over Zalo screen share); Door B, a phone-only "Phone Starter" paste.
  - A hosted, mobile-first setup page with 5 silent videos.
  - VN default app = ChatGPT.
- **Day 0** (about 35 minutes, ≤12 coach turns):
  1. Voice brain-dump, with an early win after chunk 1: "3 lines you just said that are worth money".
  2. A 7-line check.
  3. **MAP screen** (THE one decision): one message, 3 big ideas, keyword, offer, "why this one", NOT NOW ≤7, framed as "try 4 weeks".
  4. **FILM TODAY** script within ≤24 minutes.
  5. Stop point plus Brand Card. Saving is never a gate.
  6. Optional Week 1, cut from the dump.
  7. Wrap-up, plus optional calendar reminders.
  - VN asks xưng hô in reply 1.
- **Weekly** (Lean ≤60 minutes):
  1. **Weekly Talk:** a 15-minute audio-only interview in chat, 5 questions in belief order. This is the default pillar.
  2. The machine writes the week: 3 re-say shorts (≥70% the coach's own words), 1 character short, 1 long post, 1 email/Zalo.
  3. The coach films 4 shorts from beat cards.
  4. "next" each day.
  5. Friday: spoken numbers → 5-line review → 3 bets.
  - Mini-talk for busy weeks; never a zero week.
  - Monthly "plan next month" (KEEP or sharpen).
  - A filmed 20–40-minute pillar is opt-in.
- **Level-ups**, offered by the machine at their triggers:
  - L0.5: calendar reminders.
  - L1: the 3 automations (ChatGPT nudge tasks ≤900 characters), offered after the Week-1 Friday.
  - L2: the board (Notion default; Sheets Lite).
  - L3: Autopilot (Claude Pro: skill zip + Notion + scheduled tasks).
  - L4: the GROW file (launch, deep research, ads, packaging library).
  - L5: deep character excavation.
- **5 phrases:**
  - next / tiếp
  - save this: / lưu lại:
  - my numbers / số liệu tuần này
  - make it sound like me / viết lại giọng mình
  - I'm stuck / mình bị kẹt
- **The coach never sees** framework names, scores, IDs, templates or the method file. A lint deny-list enforces this.

### Content engine (internal; never shown)
- **Message Map** (`wf11-message-focus.md`):
  - one buyer, one problem in their words, one promise, one named method, one enemy, one offer;
  - ≤3 big ideas, and NOT NOW ≤7, each with a plain reason;
  - a side-door piece for multi-income coaches.
- **Domino trust:**
  - Admirable → Likable → Credible → Trustable (≈ Attract → Trust → Convert), with a belief-shift chain.
  - A Season is 4 domino weeks.
  - Series markers, plus a 14-day Domino Series for offer pushes (`wf2-synthesis.md`).
- **Three content types:** educational, entertainment/relatable and converting.
  - Entertainment is ≤20–30% and must pass the Buyer Filter.
  - Source: the 24-format catalog (`wf9-entertainment-catalog.md`).
- **Edge:** signature keywords + value + authority + authenticity + character & polarity, scored by Edge Check v2 (`wf6-character-design.md`).
- **Character:** a lite Character Card from the Day-0 dump; full excavation at L5.
- **Research** (the agency protocol, ported: `wf7-research-module-spec.md`, `wf10-access-modes-design.md`):
  - Day 0: a silent Quick Listen.
  - Week 1: "ask 3 past clients one question".
  - Weekly: a 10-minute drip inside the Friday review.
  - Research Hour and R0–R8 (the why-loop to root cause; demand → product → bridge) live in GROW and L3.
  - Access modes:
    - Search;
    - Browse-Claude (Claude in Chrome);
    - Browse-ChatGPT (desktop app + browser extension);
    - Deep research (context only);
    - Paste (the default for VN and phone-only coaches).
  - Never full computer use. Listening is read-only, with no names or handles.
- **Converting:**
  - CTA kit: comment keyword ON by default, a "quiet" option, and DM/Zalo reply scripts.
  - Editorial and direct-response posts, email/Zalo, and ads.
- **Launch** (GROW; `wf5-launch-design.md`):
  - Types A–D, phases P0–P9, launch math, the Scarcity Ledger, 7/14/21-day calendars, and launch mode in the automations.
  - Keywords, "chấm" and thresholds are never blocked; they get one dated note.
- **Packaging library:** from Matt Gray and Soo Wei Goh patterns (`wf8-mattgray-playbook.md`), renamed in the founder's own words. No Matt Gray framework names.

### Quality: 4 layers (`wf12-qa-spec.md`)
1. **Runtime (hidden):**
   - one Ship Check per batch;
   - the card is ≤900 characters EN, ≤1,000 VN;
   - output classes: Idea / Micro / Script / Script-claims / Structured;
   - Ready = gates pass, Edge ≥8 and no pillar at 0;
   - 2 rounds: the draft, then one fix;
   - ≤1 question per reply;
   - `[NEEDS: …]` / `[CẦN BẠN: …]`; nothing is ever invented;
   - `why?` reveals the record.
2. **Coach checklists:** before filming, before posting, weekly, before a launch, monthly.
   - Yes/no only, ≤5 ticks, shown inside messages the coach already gets.
3. **Build QA:**
   - gates G0–G9 and invariants I1–I18;
   - ≥20 eval cases per module;
   - a judge validated on the founder's labels;
   - 3× blind generative tests and a second read (the lower score stands);
   - simulated walkthroughs, platform smoke tests and human testers;
   - SIGNOFF bound to the build sha256.
4. **Standards:**
   - `qa/standards/` holds 18 build-only rubrics;
   - a 12-bullet HOUSE RULES page and a plain standards page ship to the coach and their VA.

## Reconciliations (applied during the build)
1. **VN is fully Vietnamese,** including the method file and the Ship Check card (`method_prose = "vn"`).
   - EN is the source. Each VN section stores the `src_hash` of its EN section; a lint gate catches stale sections.
   - IDs, rubric codes and property names are shared (the neutral tier).
   - This supersedes arch §11.1 and the QA spec's English-card assumption.
2. **Per piece, the coach sees:**
   - one WHY THIS GETS CLIENTS line;
   - one verdict line (≤20 words, the QA §2.4 states). Day 0's "✓ Checked: …" is the plain form of the Ready state;
   - ≤1 "Needs you" line.
   - No scores or codes anywhere visible.
3. **Bars:** runtime Ready = Edge ≥8 with no 0. Release judge: average ≥8, no piece below 7. The UX spec's "≥7" is the per-piece release floor.
4. **The Brand Card** (`schemas/brand-card.toml`) replaces `MY-BRAND-BRAIN.md` everywhere, including the monthly upkeep line.
5. **Gemini is off the main path.** It is dropped from the lanes and G7; build target 1.1.
6. **G6/G8 thresholds** come from UX §6: Map ≤8 turns EN / ≤9 VN, film-ready ≤24 minutes, ≤12 turns, the 17-item quit checklist, plus the QA QUIT triggers.
7. **Hub "Quality" properties** exist only from L2. Before that, the QA record appears only on `why?`.
8. **`ship_lint.py`** runs only in the L3 skill (and in the kit, if Phase-0 shows Claude can call it there). Everywhere else the card's manual checks run, and G3b measures them.
9. **Personas per edition:**
   - the 4 core personas: coldstart-coach, proof-coach, consultant, service-biz;
   - the UX personas: EN `linda-claude-pro-mac-newsletter`; VN `hanh-android-free-nocomputer`, `tuan-multihat-plus`;
   - plus a rotating held-out persona. All fictional.
10. **Research folds into the single skill as references.** There is no separate research skill. Day 0 carries only RESEARCH-LITE.
11. **No Matt Gray framework names** (Content Waterfall, Content GPS, 4-3-2-1, Authenticity Machine, Founder OS). They are on the lint deny-list.

## Repo layout
```
README.md  CHANGELOG.md  VERSION  .gitignore (dist/, evals/runs/)  .github/workflows/ci.yml
docs/  PLAN.md  DECISIONS.md  founder/phase0-checks.md  research/ (whole corpus + README index + founder-sources.md)
editions/  en.toml  vn.toml  vn.acceptance.toml        params, platform_mix, PENDING_VN markers
strings/   en.toml  vn.toml                              every coach-facing line, keyed; VN keys carry src_hash
core/      router.toml  format-checks.toml  method.toml (which modules/anchors go into kit / GROW / skill)  SKILL.md.tmpl
core/{en,vn}/  start-block.md  phone-starter.md  self-check.md  ship-check.md  ship-check-task.md
modules/{en,vn}/  setup message talk levelup brain character research signature ideas plan fmt-short fmt-long
                  packaging convert launch-plan launch-scripts edge-rubric humanize guardrails review hub automation
locales/{en,vn}/  language market compliance platform-notes (only file with dates) examples
                  lib/{hooks,titles,moments,launch-phrases}.toml  banned-tells.txt  deny-list.txt
schemas/   brand-card.toml  banks.toml  hub.toml (Notion + Sheets + paste formats from one schema)  keys.toml
automation/ tasks.toml  task-nudge.tmpl (≤900)  task-standalone.tmpl (VA)  task-connected.tmpl (L3)  daily-machine.tmpl
platform/targets.toml                                    every limit: value, source, verified_on (90-day lint)
guides/    setup-page.tmpl  troubleshooting.tmpl  helper-message.tmpl  house-rules.tmpl  standards.tmpl  whats-new.tmpl
qa/        README LEDGER CALIBRATION rubric-proposals incidents  standards/ (18)  verdicts/  releases/  runs/  inbox/
evals/     personas/{en,vn}/<persona>/ (persona.toml answers.md voice-samples.md pillar-transcript.md stats-*.csv
           launch-brief.toml paste-dump.md research-paste.md expected.toml)  personas/heldout/
           cases/<module>.{en,vn}.toml  judge/cases.jsonl  judge.md  graders.py  run.py  acceptance.toml  baselines/
tools/     render build lint package ics shiplint preflight verdict_check blind ingest_labels carry_check
           landing_check scorecard hub_build_prompt  tests/ (unittest + must-fail fixtures)
```

**Built outputs** (`dist/`, gitignored; CI uploads them as artifacts):
```
Content-Machine-{EN,VN}-v1.0.0.zip
  START-HERE.html                link + QR to the hosted setup page
  1-INSTRUCTIONS.txt             EN ≤6,500 / VN ≤7,500 chars (NFC); one text for both apps
  CONTENT-MACHINE-{EN,VN}.md     ≤50 / 55 KB; §CM anchors: TALK WEEK TODAY NUMBERS MONTH FORMATS CTA-KIT
                                 CHARACTER-LITE RESEARCH-LITE EDGE HUMANIZE GUARDRAILS LOCALE
  PHONE-STARTER.txt              ≤7,500 chars; no § signs, no English in VN
  Help/                          troubleshooting, helper-message, house-rules (noi-quy), standards (tieu-chuan), reminders/*.ics, examples/
  Level-ups/                     GROW-{EN,VN}.md (≤60 KB), autopilot/content-machine(-vn).zip (≤300 KB, with scripts/ship_lint.py), Notion + Sheets links
site/{en,vn}/index.html          hosted setup page
maintainer/                      manifest.json (sha256 + % of each budget), notion-build-prompt-{en,vn}.md, sheets-{en,vn}/*.csv
```

## Phases
**Each phase runs the same loop:**
1. QA-role agents write the eval cases before any module exists (a producer never writes its own cases).
2. Producers write modules, each to distinct files, in one workflow of ≤10 agents.
3. Build and lint (G1).
4. Simulated golden runs, then the judge and a second read.
5. One fix round.
6. Commit with the verdict path in the message, then push.

From P2 on, every phase ends with its **native VN port**: written in Vietnamese, not translated.

**How simulated runs work** (no API keys needed):
- A "machine" agent runs with the rendered kit as its operating instructions, against a persona's scripted, messy coach turns.
- Lanes:
  - S0: compact mode, no file.
  - S1: the Project kit (ChatGPT/Claude stand-in).
  - S3: the L3 skill with a fake hub.
  - Floor: the same as S1 on a smaller model, standing in for the weaker free-tier model.
- `graders.py` asserts I1–I18 on each transcript.
- A fresh judge scores `qa/standards/`.
- G6 persona players walk the kit and quit on any QUIT trigger.
- `evals/run.py` builds the run packets and grades the transcripts. It gains an `--api` mode if keys are ever provided.

### P0 Foundations (right after approval)
- Remove `yeah`. Add `.gitignore`, `README.md` (stub), `VERSION` 1.0.0 and `CHANGELOG.md`.
- **docs:**
  - `docs/research/`: copy the full scratchpad corpus and add an index README.
  - `docs/PLAN.md` (this plan) and `docs/DECISIONS.md` (Appendix A).
  - `docs/research/founder-sources.md` (Appendix B).
- **`docs/founder/phase0-checks.md`:** the real-account checks, step by step, with a results table (list under "What needs the founder").
- **`platform/targets.toml` draft:**
  - every limit from the specs, with its source;
  - web-verified items dated 2026-10-05;
  - unverified items marked `[VERIFY]` with a blank date, so the release fails until they are filled.
- **evals:**
  - personas (4 per edition + the UX personas + held-out), with their trap files;
  - `acceptance.toml` (UX §6 thresholds);
  - case files for the P1–P2 modules;
  - a **no-pack baseline**: Day 0 for 2 personas per edition with no pack, so we can prove the pack's lift later.
- **Workflow:** about 8 agents (persona writers EN/VN, case writers, baseline runner, completeness critic).

### P1 Build system, schemas and deterministic QA
- **`tools/` (stdlib Python):**
  - `render.py`:
    - `{{param}}`, `{{t:key}}` and `{{#if}}`;
    - a generated WHEN/RULES header and a CHECK BEFORE ANSWERING footer drawn from `format-checks.toml`;
    - the output-contract sandwich.
  - `build.py`: assembles per edition from `core/method.toml`: instructions, phone starter, method file, GROW, skill.
  - `lint.py`:
    - budgets from `targets.toml`, after NFC;
    - parity and `src_hash` staleness; PENDING_VN acceptance; the 90-day `verified_on` rule;
    - router coverage; the sandwich; card presence;
    - deny-lists: jargon, banned tells, Matt Gray names, template-fill wording, PII;
    - dates allowed only in `platform-notes`; ASCII names; zip hygiene.
  - `package.py`: deterministic zips. `--release` refuses to publish without PASS verdicts and a SIGNOFF.
  - `ics.py`.
  - `shiplint.py`, sharing its core with `evals/graders.py`.
  - `preflight.py`, `verdict_check.py` and `hub_build_prompt.py`.
- **Data files:**
  - `schemas/*.toml`;
  - `editions/*.toml` (including `platform_mix` and the PENDING_VN keys);
  - string skeletons.
- **Tests:**
  - `tools/tests/` (unittest), plus must-fail fixtures:
    - a 191-character description, NFD Vietnamese, a stale hash, an unaccepted PENDING key, an old `verified_on`;
    - a dotfile in a zip, a non-ASCII name, a 151-line reference, a job loading 5 files, an unknown hub property;
    - a template with no verdict line, "fill in" in coach text, "Hãy cùng khám phá", "Content Waterfall", a date in `market.md`, a non-deterministic zip.
- **CI:** GitHub Actions runs unittest, lint, a build of both editions, and uploads `dist/`.
- **Workflow:** 3 producers (render/build/package; lint + fixtures; shiplint/preflight/verdict/graders) + 1 independent reviewer. I integrate.
- **Exit:**
  - the fixtures catch 100%;
  - an empty-skill build passes;
  - CI is green.

### P2 Day-0 kit (EN, then VN) — the #1 priority
- **`core/{en,vn}`:**
  - `start-block.md`, which holds:
    - the Day-0 engine;
    - self-check and the running tag;
    - compact locale rules;
    - the inline claims guard;
    - the router to the §CM anchors;
    - compact Ship Check + FOCUS;
    - save steps per app;
    - level-up triggers;
    - non-negotiables at top and bottom.
  - `phone-starter.md`, `self-check.md`, and `ship-check.md` (card + task variant).
- **`core/`:** `router.toml` and `format-checks.toml`.
- **Modules:** setup, message, brain (Brand Card), character (lite), signature, research (Quick Listen), fmt-short, convert (CTA kit), edge-rubric, humanize, guardrails. Plus `locales/{en,vn}/*`.
- **`qa/standards`:** shared, micro, message-map, character-card, signature-keyword, native-short, text-post, carousel, email-zalo.
- **Eval tooling:** `evals/run.py`, `graders.py`, `judge.md`, `blind.py` and `ingest_labels.py`.
- **Verify:**
  - G1 and the budgets.
  - Golden Day-0 runs: 3 runs per persona on lanes S0, S1 and Floor.
    - Map ≤8 turns EN / ≤9 VN; film-ready ≤24 minutes; ≤12 turns.
    - 0 detours and 0 gates; Week 1 delivered with the Brand Card unsaved.
  - I1–I18 hold on every transcript.
  - Judge plus second read. These stay provisional until the founder's labels validate the judge.
  - G6 walkthroughs (Dana, chị Hạnh, Tuấn, Linda): 0 QUITs; all 17 quit points handled.
  - Adversarial #1 is refused: a fake testimonial, an income guarantee, an invented $ result, an injection in pasted comments, an attack on a protected group.
  - A comment-keyword CTA is **not** blocked.
- **VN:**
  - a native-writer agent writes `modules/vn` and `core/vn` from the EN source, with `src_hash`;
  - EN-leakage scan and pronoun consistency;
  - the founder's native reviewer scores naturalness (≥4/5).
- **Exit:** G1–G6 pass on both editions. The founder gets a **preview kit** to try in their own ChatGPT or Claude: the earliest real check of the experience.

### P3 Weekly loop, checklists and L0.5–L2 (EN, then VN)
- **Modules:**
  - talk: Weekly Talk, mini-talk, re-say shorts;
  - plan: Season, slot grids per tier, repetition, CTA ladder, monthly re-plan;
  - review: 5-line Friday, spoken numbers, the 2× median rule only once a board exists, the diagnostic;
  - ideas;
  - fmt-long: the opt-in filmed pillar and cut kit;
  - packaging-lite;
  - levelup L0.5–L2;
  - hub.
- **Strings:** the five coach checklists.
- **Hub:** the Notion build prompt and Sheets Lite CSVs. With the founder's OK, I build the Notion template in their workspace through the connected Notion connector.
- **`qa/standards`:** season-plan, pillar-guide, cut-kit, longform-packaging, weekly-review.
- **Verify:** a 4-week simulated journey per persona (Day 0 → 4 Talks → 4 Fridays → plan next month):
  - ≥90% of pieces on the Map;
  - WHY line 100%;
  - keyword exactly once in 100% of pieces;
  - no repeated hook stem within 10 pieces;
  - review math exact against the fixtures;
  - Lean week ≤60 minutes;
  - the judge passes.

### P4 Automations and L3 Autopilot (EN, then VN)
- **Automations:**
  - the automation module;
  - `tasks.toml`: BATCH Mon, DROP weekdays, REVIEW Fri; Slot and Run keys; caps; catch-up; launch-mode variants;
  - `task-nudge`, `task-standalone`, `task-connected` and `daily-machine`;
  - `.ics` files.
- **L3 skill:**
  - `SKILL.md.tmpl`: router ≤300 lines, Ship Check, hub write rules, NEXT tables, the sandwich;
  - references ≤150 lines and ≤9 KB each, ≤4 per job;
  - `scripts/ship_lint.py`;
  - description ≤190 characters;
  - a flag-only second read inside DROP.
- **Verify:**
  - router evals: route ≥95%, trigger ≥90%, false trigger ≤10%;
  - task budgets pass lint;
  - 20 distinct drops over 4 weeks;
  - idempotency on a fake hub. With the founder's OK, also on a sandbox Notion:
    - BATCH run twice → 0 duplicate Slot Keys;
    - a killed run recovers;
    - DROP catches up a missed BATCH.
- **Founder:** one live week on Claude Pro.

### P5 GROW: research, launch, packaging, ads, entertainment, deep character (EN, then VN)
- **research, R0–R8:**
  - R0 access check;
  - R1 plan;
  - R2 primary kit;
  - R3 listening sprint;
  - R4 context sweep;
  - R5 why-loop;
  - R6 brief, with self-check gates G1–G13;
  - R7 drip;
  - R8 re-forage.
  - Batch prompts for Browse-Claude, Browse-ChatGPT and Paste, in EN and VN.
- **launch-plan:** picker, math, Brief, Ledger, P0–P9 calendars, automation states, Launch Desk, debrief.
- **launch-scripts:** per phase × format.
- **Other modules:**
  - ads in convert;
  - the packaging library (renamed);
  - the entertainment catalog → `lib/moments` + formats;
  - full character excavation (L5);
  - `launch-phrases`.
- **`qa/standards`:** research-brief, offer-post, ad-script, launch-assets.
- **Verify:**
  - Golden launch runs:
    - cold-start → Founding, 7 days;
    - proof persona → Mồi, 14 days (EN);
    - Challenge, 21 days (VN).
  - The Ledger refuses fake urgency.
  - Blocked: "fake 3 seats left", "guarantee 100tr in 30 days", an AI testimonial.
  - Founder-override test: "đủ 100 comment" and "chấm" are written as asked, with one note.
  - The persona's research brief passes G1–G13.
  - GROW is ≤60 KB.

### P6 Guides, setup page and release
- **Guides:**
  - the setup page: mobile-first, device-aware, copy buttons, QR, outcome preview, helper kit, 8 fixes, dated, video slots;
  - troubleshooting, helper message, house rules, standards, what's new.
- **Examples:** frozen from passing runs, using the fictional personas (Dana; chị Hạnh).
- **Docs:** the README maintainer guide with the release checklist; the CHANGELOG.
- **Release:**
  - G0–G9 → `qa/releases/v1.0.0/`;
  - the founder's 1-page sign-off packet;
  - `package.py --release`.

## Verification (end-to-end)
- **Every push (CI):**
  - `python3 -m unittest discover -s tools/tests`
  - `python3 tools/lint.py` (G1, including the must-fail fixtures)
  - `python3 tools/build.py --edition all` (budget report in `dist/maintainer/manifest.json`)
- **Per phase:**
  - `python3 evals/run.py --suite <phase> --edition <en|vn> --lane <S0|S1|S3|floor>` builds the run packets; the workflow agents produce the transcripts.
  - `graders.py` asserts I1–I18.
  - Judge and second-read verdicts go in `qa/verdicts/<id>/` and are checked by `verdict_check.py`.
  - `qa/LEDGER.md` is updated.
- **Release:**
  - G0 preflight → G1 → G2 golden runs → G3 judge (+ G3b calibration) → G4 3× blind tests → G5 second read → G6 simulated walkthroughs → G7 platform smoke (human) → G8 6 testers + 1 helper install (human) → G9 sign-off.
  - Pass rules per QA §5.1 and UX §6.

## What needs the founder (and when)
| When | Action |
|---|---|
| P0–P1 | Real-account **Phase-0 checks** (I write the step list; you or a VA spend about 2 h). See the list below this table |
| Start of P2 | The **judge labelling session** (about 2–3 h): ≥40 pieces per edition, ≥20 of them "don't post". I prepare the blind sheet |
| P2 onward | A **VN native reviewer** (naturalness ≥4/5). **VN legal counsel** on the claims rules (until they sign off, every result claim is AMBER). US counsel is optional |
| End of P2 | Try the preview kit in your own ChatGPT or Claude and send reactions |
| P3–P4 | OK to create the Notion template and a sandbox page through the connected Notion connector. One live week on Claude Pro |
| P6 | Host the setup page (GitHub Pages or Vercel), the Notion and Sheets templates, and the 5 silent setup videos. A VA runs G7 smoke (about 10 combinations × 15 min). Recruit 6 testers + 1 helper (G8). Sign `vn.acceptance.toml` and `SIGNOFF.md` (≤45 min per release) |
| Ongoing | The VN buyers' Zalo group and the weekly 30-min "cài cùng nhau" install session. Optional API keys (OpenAI/Anthropic) for automated lanes |

**Phase-0 checks:**
- **ChatGPT:**
  - Save-to-project on Free and on mobile, and whether it counts toward the file cap.
  - "Add text" sources.
  - Creating a project on a phone.
  - Whether the model can create tasks from a project chat.
  - Weekday scheduling and time windows on Free.
  - The task-prompt length limit.
  - The Free message cap and its fallback model.
  - VN dictation length.
- **Claude:**
  - "Add text content" and "Add to project".
  - Code execution with a project file on Free.
  - Skills and the Notion connector on Free.
  - Whether re-uploading a skill replaces it.
  - Scheduled-task creation.
  - Free turns per 5 hours with the kit loaded.
  - Mac dictation.
- **Browser agents:** reading comments on Facebook groups, TikTok and IG, with both Claude in Chrome and the ChatGPT extension.

## Defaults I'll use unless you change them
1. Edge bar 8; "two rounds" = the draft + one fix.
2. The OpenAI API stand-in lane stays **off** until you provide a key. ChatGPT is proven by the real-account G7 golden runs instead.
3. The Claude Pro flag-only second read is **on**.
4. The labelling session is scheduled at the start of P2. It blocks judge-scored results, not building.
5. Freebie-led background posts get the Micro check (never Edge-failed).
6. VN ships only with a signed `vn.acceptance.toml`. PENDING keys use safe defaults.
7. VN default launch = Mồi, 14 days. Challenge / Zalo mini-class (21 days) is an option.
8. Updates = a quarterly zip by email. Licence = "one business plus its team". No done-for-you tier in v1.
9. Pricing and positioning copy are your call, outside the build.

Founder decisions: [DECISIONS.md](DECISIONS.md). Founder-provided source digests: [research/founder-sources.md](research/founder-sources.md).

## Research index (docs/research/)
| Area | Files |
|---|---|
| UX (final) | `wf11-ux-spec.md`, `wf11-message-focus.md`; designs, facts and walkthroughs (`wf11-*`) |
| QA (final) | `wf12-qa-spec.md`; drafts and critique (`wf12-qa-*`) |
| Architecture | `arch-final-spec.md`; proposals and judgments (`arch-*`) |
| Research module + access modes | `wf7-research-module-spec.md`, `wf7-research-port.md`, `wf7-source-map.md`, `wf10-*` |
| Character + Edge v2 | `wf6-character-design.md`, `wf6-*` |
| Launch | `wf5-launch-design.md`, `wf5-launch-frameworks.md`, `wf5-vietnam-launch.md` |
| Packaging and hooks | `wf8-mattgray-playbook.md`, `wf8-*` |
| Entertainment / POV | `wf9-entertainment-catalog.md`, `wf9-pov-*` |
| Creators + VN market | `wf2-synthesis.md`, `wf2-vietnam-market.md`, `wf2-*` |
| Hub + automations | `wf3-recommendation.md`, `wf3-*` |
| Packaging, gaps, frameworks | `wf1-packaging.md`, `wf1-gaps.md`, `wf1-*` |
