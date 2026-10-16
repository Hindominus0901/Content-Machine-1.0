# Content Machine 1.0: final architecture spec

## 1. Thesis

**What it is.** Content Machine is a trust compiler. The coach meets it as one conversation, one board and three automations. It turns the coach's raw material, which AI cannot fake, into a 4-week domino "Season" of scripts. That material is their character, stories, clients' words, proof and the weekly pillar recording. The scripts move the right people from Admirable to Trustable, and when the coach is ready, through a real launch.

**How it is built.** There is one source repo:
- small method files written in English;
- coach-facing strings for each edition;
- locale libraries written natively for each market;
- one hub schema;
- one table of platform limits, each with the date it was verified.

A Python build that uses only the standard library compiles this into an EN pack and a VN pack. Each pack has exactly one install folder per AI app: a Claude skill plus a small Project, a ChatGPT Project, and a Gemini skill folder.

**How quality is enforced.** Every script passes one hidden Ship Check:
- anti-fabrication trace;
- humanize pass;
- claims and scarcity guard;
- variation guard;
- the founder's 5-pillar Edge Check: Keyword, Value, Authority, Authenticity, and Character & Polarity.

The coach only sees a one-line footer.

**What the coach has to do.** The coach learns three phrases. They get a script they can film by about minute 25 of the first session. Every reply ends with exactly one NEXT line. Claude Pro with Notion runs the loop by itself. ChatGPT and Gemini fall back to prompts that keep no memory, work from the date, and need a person to paste the output into the board.

### Base proposal and how the disagreements were settled

**Base: the "robustness" proposal.** Two of three judges picked it, and it has the highest total score (134, against 130 for coach-ux and 126 for outcomes). It brings the build and lint rigor, one schema, the Launch module, comment-keyword CTAs on by default, task prompts generated in the session, and date-based rotation.

**Grafted on top:**
- From "coach-ux", the whole coach-facing layer:
  - the first-session order (a script ready to film before any planning);
  - the "What's next?" state table and the single NEXT line;
  - catch-up of missed runs;
  - picking the hub from the AI app the coach uses;
  - Week 1 cut from the onboarding interview.
- From "outcomes":
  - buyer-signal measurement;
  - the swap test, the competence-first gate and the ≥70%-own-words rule;
  - the CTA kit, the no-pillar fallback and the 4-rung weekly sweep.

| Where judges or sources disagree | Decision | Why (one line) |
|---|---|---|
| ChatGPT: one "Daily Machine" task or 3 tasks | **3 named tasks by default.** The single weekday-router task is generated too, as a fallback | If the coach ignores daily drops and that one task auto-pauses, the Monday batch and Friday review stop with it. Three tasks also match the founder's naming and Free's 3-task cap. |
| Claude automation shape | 3 tasks, each with catch-up guards | One mental model on every platform. Catch-up gives the main benefit of a single schedule. |
| Hub default | **Chosen by app**: Claude uses Notion; ChatGPT and Gemini use a Google Sheet. The coach can override | Nothing writes to the board automatically on ChatGPT or Gemini, so the simplest place to paste wins, and one install decision disappears. |
| Claude Project (coach-ux dropped it) | **Keep it**, with instructions of 1,500 characters or less | It forces the skill to load (generic phrases may not trigger it otherwise) and holds the hub link. Cost: about one minute. |
| Claude Plugin | Not in v1 | Paid plans only. Installing it alongside the skill gives duplicate triggers, and it adds a decision for the coach. |
| All-in-one "Lite" file | Deferred to 1.1 | It would be an untested fifth path, and all three named apps are already covered by Skills or Projects. |
| How often the signature keyword appears (100% vs at least 3 times in 30 days) | **Every piece carries a chosen keyword exactly once, in a placement that rotates.** It is spoken only where it fits naturally | The founder's thesis requires repetition in every script. One rotating placement plus the variation guard avoids stuffing. |
| CARD/DEEP sections inside one file | Separate small files instead | Nothing can make a model read only part of a file; small files can be loaded selectively. |
| Language of the method prose in the VN edition | **English, wrapped in a VN output contract, behind a `method_prose` switch.** The founder makes the final call (§11) | One source and stronger instruction-following. Flip it if the golden runs show English leaking into VN output, or if the founder prefers VN files. |
| VN facts marked PENDING: block the release, or ship defaults | Each PENDING key must be filled, or accepted by the founder with a safe default | The VN launch is not held up by research, and every guess is written down explicitly. |
| Character Core: a separate interview, or folded into Day 0 | The Day-0 interview **opens** with 5 character questions inside the 10-question limit. A deeper excavation is optional homework | Meets the founder's "start from character" without making Day 0 longer. |
| Converting content: Week 4 only, or weekly | **At least 1 Trustable piece every week from Week 2.** Hard direct-response asks only once the proof gate is open | Nik Setting's funnel balance: people arriving in Weeks 1–3 need proof too. |
| Pillar cut: one-week lag, or same week | Cut as soon as the transcript is pasted; the pieces are scheduled Wednesday to the following Tuesday | Faster to an outcome, and the rolling 7 days still absorbs a missed pillar. |
| Stats per post: 8 numbers, or 4 | **4 numbers or a screenshot.** Calls, sales and attribution answers are logged weekly | Fits 1–2 h/week with no VA. |
| "Edited" status | Dropped | Editing is out of scope, so the coach has fewer states to track. |
| wf5 bait meter vs the founder's override | Comment keywords, comment thresholds and "chấm" are **never blocked or silently rewritten**; the coach sees one dated platform note. Only fake scarcity and unsubstantiated income or health claims are hard-blocked | Founder decision. |
| Optional skill zip in the ChatGPT folder | Not shipped | Two copies of the method in one account can drift apart. |

---

## 2. Coach journey

### 2.1 Install

START-HERE fits on one page and asks one question: **"Which AI app do you use?"** The answer picks the folder, the hub and the automation path.

| | **Claude Pro/Max: "runs itself"** | **Claude Free: "one message each morning"** | **ChatGPT (any plan): "drafts arrive each morning; you or your VA paste them"** | **Gemini (personal): "best effort, manual"** |
|---|---|---|---|---|
| 1 | Settings → Capabilities → turn on "Code execution and file creation" (30s) | Same as Pro | Projects → New project "Content Machine" (30s) | Skills → upload the **unzipped** `content-machine/` folder (1m) |
| 2 | Customize → Skills → + → Upload a skill → `content-machine.zip` → switch it on (1m) | Same as Pro. **If there is no Skills option:** use the ChatGPT folder inside a Claude Project (troubleshooting page) | Paste `1-paste-into-instructions.txt` (1m) | Open the Sheet template → Make a copy (1m) |
| 3 | Open the Notion template → Duplicate (2m) | Same as Pro | Add files `CM-A-PLAN.md` and `CM-B-WRITE.md` (2 uploads, 1m) | New chat: "Set up my Content Machine" |
| 4 | Customize → Connectors → Notion → share **only** the "Content Machine" page (2m) | Same as Pro (the connector works on Free; verify in Phase 0) | Open the Sheet template → Make a copy (1m) | Save the `MY-BRAND-BRAIN.md` it produces, and **attach it at the start of every new chat** |
| 5 | New Project "Content Machine" → paste `project-instructions.txt` and replace `[NOTION LINK]` (1m) | Same as Pro | Settings → Notifications → Tasks: Push + Email (30s) | Import `content-machine-weekdays.ics` (reminder only) |
| 6 | In the Project: **"Set up my Content Machine"** | Same as Pro, then import the `.ics` reminder at 07:07 on weekdays: "Content Machine: what's next?" | In the Project: **"Set up my Content Machine"** | Scheduling is not in v1 |
| Install time | About 7 min | About 7 min | About 5 min | About 3 min |

Things the session guides the coach through, so START-HERE stays short:
- **Claude Pro:** creating the three schedules, plus a Run now test.
- **ChatGPT:** uploading `MY-BRAND-BRAIN.md` (the third upload of day 1) and pasting the three generated task texts.
- **Claude Free and Gemini:** importing the `.ics` reminder.

### 2.2 First session (about 50 min; the coach is active for about 30)

The order is the same on every platform; only where things are saved differs.

| Min | Coach does | Machine does or gives |
|---|---|---|
| 0–2 | Types **"Set up my Content Machine"** | A 3-line promise: "A script you can film today by about minute 25. Then your Brand Brain, a 4-week plan and Week 1 scripted. Voice answers welcome; 'skip' is always fine." On Claude it checks it can find the Notion page; if not, it gives a 2-line fix. It writes a `SETUP` run row listing the steps to complete. |
| 2–4 | Optionally pastes a bio, sales page, 2–3 posts, DMs or testimonials | Pre-fills fields and crosses off the questions that are already answered. |
| 4–16 | Answers in **Fast lane**, the default for everyone: all remaining questions on one screen, answered in one voice message. Saying "one by one" switches to guided mode | The 10 questions (§5.1) are grouped as **You** (Q1–5, the Character Core), **Them** (Q6–7), **Proof** (Q8) and **Logistics** (Q9–10). |
| 16–19 | Answers at most 3 follow-up questions | Probes only for specifics ("What exactly did she say?"). **Cold-start branches:** no offer runs Offer v0 (Dunford's 5 questions, about 5 extra minutes) and produces a "Founding 5" pilot. No proof sets the proof gate to locked and puts converting pieces into founding-pilot framing. |
| 19–21 | — | Mines the answers into Bank v0 with IDs (V, S, B, P, R). **Quick Listen:** at most 5 web searches across up to 3 places where the audience talks, keeping verbatim quotes with their source. This is skipped if the app can't browse, and the full Research Sprint becomes Week-1 homework. |
| 21–23 | **The one real decision:** picks 1 of 3 signature keywords | The **Edge card** and **Character Card**: who you help; their #1 problem in their words (V-IDs); the promise; the offer or founding pilot; the one extreme trait; the enemy (the old way); 3 keyword candidates, each with its origin V-IDs, a reason it fits and a sample hook; the Big Domino sentence; the 7-belief chain, one line each. Claude saves the Brand Brain to Notion now, so the session can be resumed from here. |
| **23–26** | **First win** | **FILM TODAY:** a 20–40 second native short in the coach's delivery mode. It is a "Belief Bomb" built from Q2 (the enemy and the contrarian stance), the coach's story from Q1 or Q8, and the chosen keyword. It has already passed the Ship Check. Message: "Film it now (10 min) or after we finish." |
| 26–31 | Confirms record day and time zone | **Season 1:** 4 Domino Weeks, the weekly slots for the coach's volume tier (set by the time answer), 2 named recurring shows, and the **CTA kit**: comment or DM keyword, the real asset it delivers, the first DM line asking a qualifying question, and the booking-form attribution question. Claude writes about 30 dated Content rows. ChatGPT and Gemini get one block of rows to paste into the Sheet. |
| 31–41 | Skims | **Week 1, cut from the onboarding answers** (the interview counts as pillar #0): 3 shorts (belief to contrarian; client story to case; keyword reveal), 1 carousel or text post, and 1 email (a 5-line "why I'm starting this series" story). It also gives the **Pillar #1 recording guide** for this week's record day. Delivered in 2 batched replies. On Claude, the chat shows only titles, links and footers. |
| 41–47 | About 3 minutes of setup, or "later" | **Automations** (see §7):<br>- Claude Pro: the "Create with Claude" sentence, Run now on DROP, then a check that a Runs row appeared and that the approval mode doesn't stall.<br>- ChatGPT: "Set up my automations" produces 3 task texts plus click steps.<br>- Claude Free and Gemini: import the `.ics`.<br>If the coach says "later", "What's next?" brings it back. |
| 47–50 | — | Wrap-up:<br>- ChatGPT: "Upload `MY-BRAND-BRAIN.md` to this Project now."<br>- All platforms: "Today: film the short. {Record day}: record Pillar #1 (30 min), then 'Content Machine: here's my recording'. Friday: 3-minute stats."<br>- Ends with exactly one NEXT line. |

**Resume:** "What's next?" picks up at the first step not yet ticked in `SETUP`. On ChatGPT that progress is stored in the `setup_progress` field of `MY-BRAND-BRAIN.md`. **Message budget:** about 12–16 coach turns, which fits free-tier caps. Free plans get batches of 3 scripts per reply.

### 2.3 Weekly loop (about 75–100 min, no VA assumed)

| When | Machine (automatic on Claude Pro; delivered as drafts on ChatGPT) | Coach | Time |
|---|---|---|---|
| Mon 07:07, **BATCH** | Scripts the pillar recording guide plus N1 and N2, applying Friday's bets and this week's belief. Clip, carousel, text post and email slots stay Idea ("waiting for transcript"). | Reads, then says "ok" or "change N2" | 10 min |
| Weekdays 06:37, **DROP** | 1 idea, 3 hooks, the domino it links to, and 1 capture question (rotating; character prompts included). On Claude it also catches up a missed batch and runs the transcript watcher. Thursday's NEXT asks for stats. | Glances at it; optionally answers the capture question ("Content Machine: add to my brain: …") | 1–2 min a day |
| Record day (default Tue) | — | Records the pillar (20–40 min), then **5 hook pickups** (3 min), then N1 and N2 (10–15 min) | 45–60 min |
| After recording | **CUT** (on the paste, or the Claude "Transcript ready" watcher): 3–5 clips, 1 carousel, 1 text post, 1 email and an optional cut-down, scheduled Wednesday to the following Tuesday. | "Content Machine: here's my recording" plus the transcript | 5 min |
| Thu/Fri | — | Screenshots, or 4 numbers per post (§5.10) | 3–5 min |
| Fri 15:07, **REVIEW** | A one-screen scoreboard; More/Better/New; one break point (only when triggered); 3 bets; tops the plan back up to 4 weeks ahead; 1 optional homework item | Reads it | 5 min |

**Volume tiers**, set by the coach's answer to Q10:

| Tier | Weekly slots |
|---|---|
| **Lean** (1 h or less) | P, N1, C1–C3, T, E |
| **Standard** (1–2 h) | Lean plus N2, K and an optional D |
| **VA** | Standard plus C4, C5 and an optional A1 |

**Never a zero week.** If no pillar is recorded, the BATCH run swaps in a **mini-pillar**: "record 10 minutes answering these 3 questions into your phone". Mode A (guided interview) lets a VA or a friend run the pillar instead.

**Weekly homework:** at most one optional item of 10 minutes or less, each saying what it unlocks:
- **W1:** Buyer Mirror message to 3–5 clients, plus reviewing the Research Sprint.
- **W2:** objection mining (paste one sales-call transcript, or list 5 objections).
- **W3:** offer and proof layer: consent, substantiation, CTA asset links. This opens the proof gate.
- **W4:** a 10-minute Authenticity voice memo answering 5 questions.
- After that the items rotate.

### 2.4 Monthly, quarterly and launches

**Monthly: "Content Machine: plan next month" (25 min or less).** The last REVIEW of a Season ends with this NEXT line. The session covers:
1. A look back at winners, keyword exposures and echo, belief exposures, proof gaps and trust hours.
2. A research re-forage: at most 5 searches, plus newly pasted DMs and comments.
3. The next Season: a new belief chain, or the same chain with new proof.
4. Formats that have underperformed for 4 weeks are retired.
5. The Brand Brief is refreshed and its version number goes up.
6. In month 1 only, a **Start Here** path: a pinned-post script and a pre-call email script.
7. A launch check: if a launch is due within 4 weeks, Runway starts.

ChatGPT upkeep is **at most 2 actions in a normal month**: replace `MY-BRAND-BRAIN.md` and paste the next Season's rows into the Sheet. If the Task Brief's version changed (new keywords, offer or chain), the coach also pastes 3 replacement task texts. The version stamp flags when this is needed.

**Launches: "Content Machine: plan a launch"**, 2–4 times a year:
1. The picker asks 3 questions or fewer.
2. The Launch Brief asks at most 8 questions in one batch.
3. The launch math runs.
4. The Scarcity Ledger is filled.
5. The 7-, 14- or 21-day calendar is built, with a prep batch session (§5.8).

The automation state then moves through Always-on → Runway (4 weeks before) → Prep (7 days before) → Launch → Cooldown. The three tasks switch their behaviour from the dates stored in the Brand Brain (§7.5).

**Quarterly:** the pack update arrives as a zip by email. The coach re-uploads the skill and types "Content Machine: update check". That command repairs the hub by adding only (it never removes), migrates the Brand Brain (it asks only the new questions), and regenerates the task texts if their template changed.

---

## 3. Source repo, build outputs and limits

### 3.1 Source tree (`/home/user/Content-Machine-1.0`)

```
README.md                      maintainer guide: build, lint, eval, release checklist
CHANGELOG.md                   lines tagged [buyer] become a localised "What's new"
VERSION                        1.0.0 (only version source; stamped everywhere)
editions/
  en.toml  vn.toml             every edition parameter (§9); vn has PENDING_VN markers + provisional defaults
  vn.acceptance.toml           founder-signed list of PENDING keys shipping on safe defaults
strings/
  en.toml                      every coach-facing string, keyed (questions, labels, commands, footer, guide, task text)
  vn.toml                      same keys + src_hash per key (staleness gate)
core/
  SKILL.md.tmpl                frontmatter · edition contract · non-negotiables · router · Ship Check card · hub
                               write rules · NEXT state tables · menu · non-negotiables repeated (sandwich)
  ship-check.md                ~900-char QC card (rendered into SKILL.md, ChatGPT instructions, every task)
  router.toml                  intent → job → ≤4 reference files → write target; command phrases + synonyms per edition
  chatgpt-instructions.tmpl    router + non-negotiables + Ship Check + stateless NEXT logic
  claude-project.tmpl          "Always use content-machine; hub = [NOTION LINK]; edition"
modules/                       EN method prose; one file = one reference file (≤150 lines, ≤9 KB)
  setup.md brain.md character.md research.md signature.md ideas.md plan.md
  fmt-short.md fmt-long.md packaging.md convert.md launch-plan.md launch-scripts.md
  edge-rubric.md humanize.md guardrails.md review.md hub.md automation.md
locales/{en,vn}/               written natively per market, never translated
  language.md                  output contract, register/xưng hô, spoken-style rules, word rate
  market.md                    platform picker + defaults, CTA channels, keyword conventions, transcript tools, formats
  compliance.md                claims rules (EN: FTC/EU; VN: Law 19/2023, Advertising Law, superlatives, gift cap, PDP)
  platform-notes.md            the ONLY file allowed to hold dates or "currently"
  examples.md                  golden-persona few-shots (frozen from passing release runs)
  lib/ hooks.toml titles.toml moments.toml banned-tells.txt launch-phrases.toml
schemas/
  brand-brain.toml             fields, onboarding layer (L1/L2/L3), schema_version
  banks.toml                   Bank types, ID prefixes, fields
  hub.toml                     ONE schema → Notion template, Sheets tabs, paste formats, hub.md, prompt property names
  keys.toml                    Slot Key + Run Key grammar
automation/
  tasks.toml                   BATCH / DROP / REVIEW: schedule, run key, caps, reads/writes, launch-mode variants
  task-connected.tmpl          Claude (short; calls the skill)
  task-standalone.tmpl         ChatGPT (Task Brief + steps + Ship Check embedded)
  daily-machine.tmpl           single-task fallback (weekday router)
platform/targets.toml          every platform limit: value, source, verified_on, margin, budget
guides/ start-here.tmpl troubleshooting.tmpl whats-new.tmpl
evals/
  personas/{en,vn}/{coldstart-coach,consultant,service-biz}/
     persona.toml answers.md paste-dump.md pillar-transcript.md stats-w1.csv launch-brief.toml expected.toml
  cases/ router.{en,vn}.toml adversarial.toml idempotency.toml launch.toml variation.toml
  graders.py                   deterministic checks
  judge.md                     human/LLM judge protocol (reads modules/edge-rubric.md verbatim)
tools/ render.py build.py lint.py package.py ics.py hub_build_prompt.py
dist/                          gitignored
```

**Renderer.** `tools/render.py` is about 100 lines and uses only the standard library (`tomllib`, no Jinja). It supports:
- `{{param}}`, `{{t:key}}` (edition string), and `{{#if connected|standalone}}…{{/if}}`;
- tables built from libraries;
- a generated "WHEN TO USE / RULES" header and "CHECK BEFORE ANSWERING" footer on every reference file;
- an edition output-contract line at the top and bottom of every file.

### 3.2 Built outputs (one zip per edition; the coach sees at most 5 files per app)

```
dist/Content-Machine-EN-v1.0.0.zip                       (<1 MB)
├── START-HERE.html                                      1 page: "Which AI app do you use?"
├── 1-Claude/
│   ├── content-machine.zip                              → content-machine/SKILL.md + README.md + references/ (24 files)
│   └── project-instructions.txt                         ≤1,500 chars
├── 2-ChatGPT/
│   ├── 1-paste-into-instructions.txt                    ≤6,000 chars
│   ├── CM-A-PLAN.md                                     setup·brain·character·research·signature·ideas·plan·review·hub·automation·launch-plan·local
│   └── CM-B-WRITE.md                                    fmt-short·fmt-long·packaging·convert·launch-scripts·edge·humanize·guardrails·examples
├── 3-Gemini/content-machine/                            unzipped skill folder, dotfiles stripped
└── Help/
    ├── troubleshooting.html  whats-new.html
    ├── reminders/content-machine-weekdays.ics           (floating local time)
    └── examples/coach.md consultant.md service.md       frozen golden runs
dist/Content-Machine-VN-v1.0.0.zip                       same tree: BAT-DAU-TAI-DAY.html, content-machine-vn.zip,
                                                         ASCII file names only
dist/maintainer/ manifest.json (sha256 + % of each budget) · notion-build-prompt-{en,vn}.md · sheets-{en,vn}/*.csv
```

The founder hosts:
- the Notion templates (EN and VN), built from `hub.toml` with the build prompt;
- the Google Sheet templates (EN and VN) with "Make a copy" links.

### 3.3 Budgets vs platform limits

`lint.py` enforces these from `targets.toml`. Every character count is taken after NFC normalisation. A release fails if any `verified_on` date is more than 90 days old.

| Artifact | Platform limit (Oct 2026) | Our budget |
|---|---|---|
| Skill `name` | ≤64 characters, `[a-z0-9-]`, matches the folder, no "claude" or "anthropic" | `content-machine`, `content-machine-vn` (both can be installed side by side) |
| Skill `description` | 200 characters on claude.ai | ≤190. EN draft is 186. VN draft is 184 in NFC; the same text in NFD is 204 and would fail |
| SKILL.md | <500 lines (about 5k tokens) | ≤300 lines, ≤18 KB |
| References | one level deep; a TOC if over 100 lines | 24 files (+ README), each ≤150 lines and ≤9 KB, TOC added automatically, no cross-links between references; total ≤200 KB |
| Load per job | context rot | ≤4 references plus SKILL.md, about 16k tokens; the router names the files |
| Skill zip | not published (third parties say about 50 MB) | ≤300 KB; deterministic (sorted entries, fixed timestamps) |
| Gemini upload | ≤100 MB; .md is fine; hidden files make it fail | the same folder; `.DS_Store` and `__MACOSX` stripped |
| ChatGPT Project instructions | about 8,000 characters (practitioner figure) | ≤6,000 EN, ≤7,000 VN |
| ChatGPT Free project files | 5 files; about 3 uploads a day | 2 method files plus `MY-BRAND-BRAIN.md` = 3 files and 3 uploads on day 1 |
| ChatGPT knowledge retrieval | read in chunks | each file ≤110 KB; unique `§CM-…` anchors; sections ≤2 KB |
| ChatGPT tasks | Free/Go: 3 (at most once a day, in a time window); Plus: 5 | 3, or 1 Daily Machine |
| ChatGPT task prompt | not documented | target ≤5,000 EN / ≤5,800 VN; hard cap = the measured limit minus 15%. Sub-budgets: header ≤300, Task Brief ≤2,400 EN / ≤2,800 VN, steps ≤1,500 / ≤1,700, Ship Check ≤800 / ≤1,000 |
| Claude Project instructions | not published | ≤1,500 |
| Claude task prompt | — | ≤600 (it calls the skill) |
| Brand Brief | (research figure) | ≤600 words and ≤3,800 characters EN / ≤4,400 VN |
| `MY-BRAND-BRAIN.md` | — | ≤40 KB; banks capped (top 30 V, 15 S, 15 P, 12 R, 20 recent hook stems) |
| Notion | text property length per item (verify); Free plan uploads 5 MB | scripts and transcripts go in page bodies; 3 databases + 1 page; ≤30 hub calls per run |
| File names | VN diacritics in zips break on Windows | ASCII only |

---

## 4. Modules (one skill per edition; "modules" are reference files the router opens)

**Skill description (EN, 186 characters):**

> "Content Machine for coaches: set up, what's next, research, ideas, hooks, domino series, launches, and scripts (shorts, posts, carousels, pillar videos, email, ads), recordings, reviews."

The VN description is in Vietnamese, keeps the words "Content Machine", "hook", "script" and "launch" in English, and is 184 characters in NFC.

The "Trigger" column holds the router-row text (≤200 characters), used for routing, docs and the router evals.

| Module | Responsibility | Trigger (≤200 chars) | Reads | Writes | Loads |
|---|---|---|---|---|---|
| **SKILL.md** (router) | Find memory (Notion → project file → attached file → otherwise setup); check `schema_version`; route; apply non-negotiables, the Ship Check and hub write rules; compute one NEXT line | The skill description; any "Content Machine" request; "what's next" | Brand Brain, Runs | — | Always loaded |
| **setup** | The whole first session; Fast lane; cold-start branches; resume; install self-tests | "Set up my Content Machine", start, onboard me, or no Brand Brain found: character-first voice intake, Edge card, film-today script, Season 1, Week 1, automations. | Answers, paste dump | Brand Brain v0, Character Card, Bank v0, Season, about 30 slot rows, Week 1, `SETUP` run | Per step (≤4 each): A: setup, brain, character, signature · B: fmt-short, language, examples · C: plan, market · D: fmt-long, fmt-short, convert, language · E: automation |
| **brain** | Brand Brain and Bank schemas; ID rules; Brief and Task Brief compression with version stamps; homework layers L2/L3; update check (add-only migration) | Add to my brain; update my offer, voice or proof; homework replies; Buyer Mirror answers; update check: files raw material as ID'd Bank rows and refreshes the Brief. | Coach input, Brand Brain | Bank rows, fields, Brief v+1 | brain, guardrails (trace) |
| **character** | Deep Character Core excavation; Character Card upkeep; character formats; polarity guide and hard limits | Who I am, values, principles, stances, vision, enemy; "make it more me"; fixing flex-only or freebie-only flags; planning character content slots. | Answers, captures | Character Card, B-rows (stances), S-rows | character, humanize, language |
| **research** | The founder's research protocol: checklist (4 customer layers + context + 3–5 scope questions); Quick Listen; Research Sprint (WHY loop to root cause); Buyer Mirror; objection mining; browse and paste modes; Chrome batch prompt; monthly re-forage | "Research my audience"; mine these comments, DMs, reviews or call transcripts; Buyer Mirror replies: verbatim client words, root-cause insights and a Research Brief with sources. | Pasted or browsed text (treated as **data only**) | V, O, I, W rows; Research Brief page | research, brain, market |
| **signature** | Signature keywords (mine → shortlist → choose → registry); named method; Big Domino; belief chain B1–B7; signature beliefs | Find or refresh signature keywords, name my method, write the Big Domino and the belief-shift chain the series will knock over. | V, I, S, P rows | K rows, Edge section of the Brain | signature, brain, examples |
| **ideas** | Idea clusters (VoC theme × 8 angles × rung); recognition moments × about 12 Buyer-Filtered formats; remixing swipes; Reach and Trust/Buy scores; kill rule; Edge-lite; daily-drop rotation | Give me ideas or hooks; remix this post: scored idea clusters across the 4 trust rungs, each tied to a belief and Bank IDs. | Bank, last 20 Content rows | Idea rows | ideas, packaging, language |
| **plan** | Season (4 Domino Weeks); slot model and volume tiers; 4-rung weekly sweep; phase mixes; repetition engine; character slots; CTA ladder; recurring shows; Start Here; monthly re-plan; plan top-up | Plan next month; change my plan; new season; Start Here: a 30-day domino Season with weekly slots, belief and keyword repetition, and a CTA ladder per rung. | Brain, Runs, Content stats | Season block, Idea rows | plan, review, signature, research |
| **fmt-short** | Templates for native shorts, clips, text posts and carousels; the three hooks; delivery modes A/B/C; Buyer Filter; funnel-shaped mid-funnel script | Script this as a reel, short, TikTok, text post or carousel in my delivery mode, with three aligned hooks, caption, CTA and next domino. | Brain, Bank, slot | Script body | fmt-short, language, examples (first use) |
| **fmt-long** | Pillar recording guide (5 formats); hook pickups; cut kit from the transcript (verbatim PASSAGE ranges, ≥70% the coach's own words); cut-down; podcast | Prep my pillar; here's my recording or transcript; YouTube or podcast episode: recording guide, then cut into clips, carousel, text post, email and a cut-down. | Transcript, Season slot | Cut slots set to Scripted; pillar Cut = Done | fmt-long, fmt-short, convert, language |
| **packaging** | The Matt Gray and Soo Wei Goh library: title formulas, thumbnail text, long-form hook pattern, 5-line story, hook bank by awareness level, carousel rules, a 60/20/20 CTA mix | Titles, thumbnails, hooks or packaging for any piece; loaded with fmt-long for pillars, and whenever a hook scores low. | `lib/hooks`, `lib/titles` | — | packaging, language |
| **convert** | Editorial converting post; direct-response offer post; client decision breakdown; objection crusher; **CTA kit** (keyword + asset + DM scripts); email (soft, hard, nurture); ads | Write a sell post, offer post, case study, objection post, email, ad, or a comment-keyword CTA with its auto-reply DM; proof-gated. | Offer, P and A rows | Script body, A rows | convert, guardrails, language, compliance |
| **launch-plan** | Picker; launch math; Launch Brief; Scarcity Ledger; phases P0–P9; 7/14/21-day calendars; automation states; Launch Desk; debrief | Plan a launch, open cart, launch desk or launch debrief: picks the launch type, does the math, builds the 7/14/21-day calendar and switches on launch mode. | Brain, Bank, Launch Brief | Launch page, launch slot rows, automation state | launch-plan, guardrails, market, compliance |
| **launch-scripts** | Templates by phase and format: background-text post (≤130 chars), long Facebook post, reel, carousel, story frames, live/workshop outline, DM flow, email/Zalo, retargeting ad | Write launch assets for a phase: bait post, belief shift, value, case series, open cart, retargeting, urgency, close, post-launch. | Launch Brief, Ledger, chain | Script bodies | launch-scripts, convert, guardrails, language |
| **edge-rubric** | The full 5-pillar rubric with anchors and rung examples; Edge-lite | "Edge check this", or a piece scored under 7 or has a zero: full rubric with fixes. | Draft, Bank | Edge property | edge-rubric, humanize, guardrails, language |
| **humanize** | The 6-step pass; read-aloud voice match | "Make it sound like me", "I stumbled on line 3": spoken-language pass, AI-tell strip, Voice Card match. | Voice Card, banned tells | — | humanize, character, language |
| **guardrails** | Claims linter; proof gate; anti-fabrication trace; Scarcity Ledger check; polarity limits; AI-disclosure rule; keyword-CTA platform notes (a note only, never a block) | Any AMBER or RED claim, proof, testimonial, income or health number, scarcity or urgency line, ad, or launch close: checked against the edition's compliance rules. | Draft, P rows, Ledger | Claims property, "Needs:" line | guardrails, compliance, platform-notes |
| **review** | Scoreboard; buyer signals; 2× median rule; More/Better/New; break-point diagnosis; keyword echo; trust hours; launch scoreboard; homework pick | Here are my stats or screenshots; review my week; why isn't it working?: scoreboard, winners, break point, next 3 bets. | Posted rows, screenshots, Runs | Stats, Lesson, Reviewed, REVIEW run, bets | review, plan, automation |
| **hub** | Schema details; Notion and Sheet paste formats; Slot and Run keys; add-only repair; CSV | Save, export, paste block, fix my board, update check: reads and writes the hub by Slot Key under the state rules; never deletes. | `hub.toml` render | Rows, paste blocks | hub |
| **automation** | BATCH, DROP and REVIEW (connected and standalone variants); Daily Machine; catch-up; launch-mode variants; task-message generator with Brief stamp; self-tests; `.ics` | Set up or repair my automations; run Monday batch, today's drop or Friday review; any scheduled run: executes or generates the three jobs. | Brain, Runs, Content | Runs rows plus whatever the job writes | automation + the job's own files (≤4 total) |
| **language** (locale) | Output contract; register and xưng hô; spoken rules; AI-tell list; word rate | Paired with every writing job. | — | — | — |
| **market** (locale) | Platform picker and defaults; CTA channels; keyword conventions (VN: variants without diacritics); transcript tools; currency and date formats | Paired with plan, setup, launch and research. | — | — | — |
| **compliance** (locale) | Claims rules for the edition's market | Paired with guardrails. | — | — | — |
| **platform-notes** (locale, dated) | Meta, YouTube, Instagram and Zalo facts with dates | Paired with guardrails and launch. | — | — | — |
| **examples** (locale) | One golden persona: Brand Brain, Character Card, and one finished script per format | First script of a format, or whenever output reads generic. | — | — | — |

---

## 5. Core artifacts and schemas

### 5.1 Brand Brain (a Notion page, or `MY-BRAND-BRAIN.md`; same fields; `schema_version` 1)

**Day-0 questions (Layer 1, at most 10).** Character comes first. The tag after each question shows the field it feeds.
1. "Tell me the moment that made you do this work." → S (origin), Character Card
2. "What makes you angry, or quietly intolerant, in your industry? What do most people in your field do or believe that you think is wrong?" → enemy, B (stance), the film-today piece
3. "What would you never do, even for money? What principle do you run your work by?" → principles, values
4. "Name 3 things people admire you for. Which ONE trait would clients say you take to the extreme?" → Admire Triad, extreme trait
5. "What world are you building? Who are you 5 years ahead of?" → vision, Signal positioning
6. "Who do you help, and what is happening in their life or business when they find you? What do they call their #1 problem, in their exact words?" → WHO, stage, V-rows
7. "What have they tried that failed? What do you sell (name, price, how people buy), or is it 'nothing yet'? What result do clients typically get, and how fast?" → B3 (vehicle belief), offer, promise
8. "Tell me one client story: before, the turning point, after, with a number if you have one." → S, P
9. "Paste or say 2 things you have written or said." → Voice Card; VN pronoun pair (xưng hô) inferred, then confirmed
10. "Where do your buyers already see you? How many hours a week do you have? On camera, do you prefer being interviewed, working from bullets, or reading word for word?" → platform, volume tier, delivery mode A/B/C

**Fields:**
- **META:**
  - versions: `schema_version`, `pack_version`, `brief_version`;
  - edition, language, time zone, `week_start`;
  - platforms: main platform (1) + email or Zalo, long-form home;
  - weekly routine: volume tier, delivery mode, record day, `plan_start`;
  - hub: `hub_type`, hub link;
  - **`automation_state`** (always-on, runway, prep, launch or cooldown) with its dates;
  - `setup_progress`.
- **BRIEF** (≤600 words, version-stamped, the first block) and **TASK BRIEF** (≤2,400 characters EN, used only in ChatGPT tasks). Both are generated from the fields below; nobody edits them by hand.
- **CHARACTER CARD** (§5.2).
- **WHO:**
  - ideal client: role, stage, situation, the pains of the stage they are in now;
  - **dream follower** (shared aspirations; tagged `[AI inference]` until the coach ticks it);
  - who it is not for.
- **PROBLEM:** #1 problem (V-IDs); failed fixes; push, pull, anxiety and habit; the enemy (a belief or practice, never a person).
- **OFFER:**
  - name, promise (X to Y in Z, with conditions), price in the edition's currency, format;
  - CTA ladder; guarantee (on the process only);
  - real cap or deadline fields;
  - `status` (live, founding-pilot or none) and `proof_gate` (open or locked).
- **EDGE:** keywords K-1 to K-3; named method and its steps; problem and solution mechanisms; Big Domino sentence; belief chain B1–B7; 3 signature beliefs; recurring show names.
- **VOICE CARD:** 5 words I use and 5 I never use; sentence habits; humour; register; VN pronoun pair; 2 verbatim samples.
- **SEASON** (§5.5). **WHAT'S WORKING:** 3 lines, rewritten every Friday.
- **ChatGPT/Gemini file only:**
  - a mini-bank (the top-N caps in §3.3);
  - `recent_hook_stems` (20, the avoid-list);
  - `THEMES` T1–T12 and `MOMENTS`, used for date rotation;
  - `task_brief_version`.

**Layer 2 and Layer 3:**

| Layer | When | What it adds |
|---|---|---|
| L2 | Just in time, weeks 1–2 | Research Sprint, Buyer Mirror, objection mining, framework naming. Triggered when there are fewer than 10 V-rows or fewer than 3 S-rows. |
| L3 | Before the first hard sell | The Sales Brain: mechanisms, the 3 false beliefs mapped onto the chain, value-equation notes, guarantee, consent and substantiation on P-rows |

### 5.2 Character Card (≤150 words; a living document)

```
ONE EXTREME TRAIT: …            ENEMY / OLD WAY: … (belief or practice)
PRINCIPLES (I always / I never): 1… 2… 3…        VALUES: … · … · …
VISION (1 sentence): …           STANCES (polarizing, on ideas only): B-4 … · B-5 … · B-6 …
QUIRKS / RITUALS / TASTES: … (grows from capture answers)
HOW I TALK: 3 signature phrases · register · VN: pronoun pair
WHY CLIENTS CHOSE ME (Buyer Mirror): V-… V-…
```

**Character content slots:** at least 1 character piece every week, in N1 or N2. Formats include:
- a stance post;
- a principle story;
- "what I'd never do";
- values shown through lifestyle (e.g. a flipped paycheck breakdown);
- a ritual.

### 5.3 Banks (one Notion database, "Bank"; IDs are `<prefix>-<n>`; the next ID is the highest existing number plus 1, checked for uniqueness before writing)

| Type | Prefix | Key fields |
|---|---|---|
| Client/audience words | V | verbatim · source (label · link · date · place · **role only, never names**) · kind (pain, desire, fear, failed fix, identity, trigger) |
| Objection | O | verbatim · value-equation term it attacks · counter-belief B-n |
| Story | S | when · before → turning point → after · emotion · lesson · rung fit · consent (if it involves a client) |
| Belief | B | "Most [niche] believe __; I believe __ because [S/P]" · type (vehicle, internal, external, stance) · chain # · exposures in the last 30 days |
| Proof | P | client (anonymised is fine) · start · result (number + timeframe) · **context block** · quote · **Consent Y/N + date + allowed uses** (organic, ads, case) · **Substantiated Y/N** · typical-results line |
| Recognition moment | R | a moment only the ideal client has lived · buying stage · emotion · filter strength 1–3 |
| Signature keyword | K | §5.4 |
| Insight | I | pattern · seen in (at least 2 places) · why chain · root · for content (hook, what to say, what to avoid) · evidence against |
| Capture | C | raw daily answer · category (noticed, happened, believe, client said, refused) · where it was filed |
| CTA asset | A | keyword (plus variants without diacritics) · delivers (the real asset) · link · M0/M1/M2 scripts · channel |
| Swipe/outlier | W | link · ratio vs that creator's median · the pattern with topic removed · "my version" |

Columns shared by every row: `Ref | Type | Text | Detail | Source | Consent | Substantiated | AI inference | Uses 30d | Used In (→ Content) | Added`.

### 5.4 Signature keyword registry (K rows)

`term · meaning (1 line) · origin V-IDs (audience words it is built from) · status (candidate, chosen or retired) · uses_30d · placements_last_10 · echo_count (times the audience said it back)`

- At most 3 can be chosen.
- **Rule:** every piece carries a chosen keyword **exactly once**, rotating its placement: hook, on-screen text, spoken payoff, caption line 1, or pinned comment.
- It is spoken in Credible, Trustable and pillar pieces; it is spoken at most once per short and at most 3 times per pillar.
- The variation guard stops the same placement or stem appearing twice in a row.

### 5.5 Season / domino plan

```
SEASON n · start · phase (audience-building | steady | launch-runway) · offer · keyword K-1 · Big Domino
CHAIN: # | false belief (V/O-ref) | new belief (B-ref) | type | rung | week | proof needed (P-ref | NEEDS PROOF)
WEEK | beliefs | pillar format | mix Ent/Edu/Conv | Trustable piece | CTA focus
 W1  | B1–B2 problem/cause      | guided interview           | 40/50/10 | (pillar #0 case clip) | follow/save
 W2  | B3 vehicle → named method | whiteboard/method          | 30/50/20 | C3 proof clip ≥1      | comment KEYWORD
 W3  | B4–B5 proof + "I can"     | live consult               | 25/50/25 | decision or case piece | DM KEYWORD
 W4  | B6–B7 external/now + offer | client decision breakdown  | 20/40/40 | offer (proof gate) or founding invite | DM/book
```

**Slots and keys:**
- Weekly slot keys use the suffixes `YYYY-Www-` `P`, `N1`, `N2`, `C1`–`C5`, `K`, `T`, `E`, `D` and `A1`.
- Launch slots: `LCH-<id>-D<nn>-<FMT>`.
- Each daily drop: `DROP-YYYY-MM-DD`.

**Rules:**
- **The week sweeps all 4 rungs; the month advances the chain.**
- At least 1 Trustable piece every week from W2. Hard direct-response asks happen only once the proof gate is open.
- Each signature belief gets at least 3 spaced exposures per 30 days, in at least 2 formats (name it → make it personal → remind at the decision point).
- At least 1 character piece a week.
- Every piece has one rung, one belief, one CTA matched to its rung, and a link-forward line.
- **CTA ladder:**

  | Rung | CTA |
  |---|---|
  | Admirable | Follow the show |
  | Likable | A send-to-a-friend prompt |
  | Credible | Save, or comment KEYWORD for the asset (**the comment-keyword default**) |
  | Trustable | DM KEYWORD (the first DM asks a qualifying question), or book |

- Across a month: about 60% contextual lead magnet, 20% direct offer, 20% DM trigger. Give-to-ask stays at 3:1 or more over any 8 weeks.
- **Mixes by phase (Ent/Edu/Conv):** audience-building 40/45/15, steady 30/50/20, launch 20/30/50.

**SPCL tags by rung (Hormozi):** Status = Admirable, Likeness = Likable, Power (say-do) = Credible, Credibility (third-party proof) = Trustable.

### 5.6 Pillar → distribution map

Each segment of the pillar recording guide must work on its own as a clip and carries a verbatim **CLIP LINE**.

| Asset | Rung | Built from | Rule |
|---|---|---|---|
| C1 clip | Credible | The segment with the strongest old → new belief shift | Funnel shape: broad hook → keyword → belief shift → close |
| C2 clip | Credible | Keyword or framework reveal | Keyword spoken |
| C3 clip | Trustable (from W2) | Proof or client-decision segment | Consented P-ID, or process proof |
| C4–C5 (VA tier) | Likable / character | A stance or a relatable moment | Buyer Filter ≥2/3 |
| K carousel | Credible | Framework steps, one rule per slide | Comment keyword → A-asset |
| T text post | Likable / character | The 5-line story (Mirror, Friction, Realization, Shift, Invitation) or a stance | — |
| E email | Rung of the week | Story → one lesson carrying the keyword → link to the pillar → P.S. CTA | ≤250 words |
| D cut-down (5–10 min) | Credible | One idea | "How I'd…/Why…" title, 2–4-word thumbnail text, new 20-second verbatim intro |
| H1–H5 hook pickups | — | Read to camera at the end of the recording session | One per planned clip |

At least 70% of each clip's words come verbatim from the transcript. Assets are scheduled Wednesday to the following Tuesday.

### 5.7 Script templates (words only; every template ends with the Ship Check footer from §8)

**Native short** (Mode B by default):
```
N1 · Likable · B-2 · K-1 · 30–40s ≈ {word_rate×s} words · <platform>
TITLE HOOK (on-screen, ≤6 words) · VISUAL HOOK (1 line: what is in frame 1) · VERBAL HOOK (verbatim, ≤12 words)
LOCK-IN (3–10s, verbatim) · BEATS (one per take, joined by but/therefore): 1… 2… 3…
FINAL LINE (verbatim, written first) · LINK-FORWARD → <slot>
CAPTION: L1 keyword phrase · L2 extends · L3 send prompt / CTA · CTA (+ A-ref if keyword)
```
- **Mode A:** 4–6 questions asked off camera, with the bullets each answer should hit.
- **Mode C:** full word-for-word text with pause marks. Used for ads and compliance-sensitive pieces.

**Clip:**
```
C2 · Credible · from P <slot> · PASSAGE: from "<first words>" to "<last words>" (≤60s, verbatim)
TITLE HOOK · NEW VERBAL HOOK (H#, optional re-record) · ON-SCREEN TEXT · CAPTION · CTA · NEXT: "Full breakdown: <pillar title>"
```
The PASSAGE is the script. There are no timecodes and no editing notes.

**Text post:** hook (≤12 words) → re-hook → proof or context line → 3-beat body or 5-line story → one bold takeaway → CTA.

**Carousel** (10–12 slides):
- S1: hook in big type, ≤10 words (number + outcome + who + keyword).
- S2: confirms the payoff.
- S3–S9: one rule per slide (rule / why / example).
- Then a sendable summary slide.
- Last slide: contextual lead magnet + keyword.

**Pillar recording guide:**
```
P · Credible core + Trustable segment · B-3 · K-1 · format (guided interview | whiteboard | live consult |
client decision breakdown | "How I'd…") · 20–40 min
TITLES ×3 (formula library, parenthetical payoff) · THUMBNAIL TEXT ×3 (2–4 words, adds to the title, never repeats it)
OPEN (verbatim, ≤40s): contrarian line → Proof → Promise (+ open loop paid off at the end) → Plan → objection remover
SEGMENTS ×4–6: claim old→new · prompt "tell the time when…" [S/P-ID or NEEDS] · one how-step · CLIP LINE (verbatim)
MID CTA (~65%, 1 line) · CLOSE: takeaway → close the loop → next domino → soft keyword CTA
MODE A: 10–12 interviewer questions in belief order · HOOK PICKUPS H1–H5
```

**Email** (≤250 words): 3 subject lines, preview text, story → lesson → CTA by rung, P.S. The welcome/nurture sequence uses the 5-line story across 5 emails.

**Converting templates:**
- **Editorial:** counterintuitive hook → problem mechanism → named fix in 3 steps (the what) → proof line → CTA for the how.
- **Direct-response offer post:** name, outcome with conditions, who it is for, stack, process guarantee, **real** cap or deadline from the Ledger, not-for list, one action. Proof-gated.
- **Client decision breakdown:** each decision A→B → result → typical-results line.
- **Objection crusher:** O-ref verbatim → reframe → proof → risk reversal → CTA.

**CTA kit** (attached to every keyword CTA):
- **M0:** public replies, at least 5 that rotate.
- **M1:** the first private reply. It delivers the asset, asks an A/B question and includes the consent line.
- **M2:** after they answer, it captures email or Zalo for nurture.

On a personal Facebook profile, where DM automation isn't available, the machine adds a one-line dated note that a VA should send these by hand. It never blocks the CTA.

**Ads** (on request; proof-gated):
- 5 hooks × 2 bodies.
- **Talking head, 30–60 s:**

  | Time | Section |
  |---|---|
  | 0–3s | Call out the pain + key message |
  | 3–15s | Problem + mechanism |
  | 15–35s | Proof |
  | 35–50s | Offer |
  | 50–60s | CTA |

- **Short VSL** (90–180 s): small CTA at about 65%.
- **Static:** headline, primary text, CTA, with no personal-attribute phrasing.

**Launch formats** (in launch-scripts.md): background-text post (≤130 characters), long Facebook post (Epiphany Bridge; case part with the context block; open-cart post), reel, carousel, story frames, a 60-minute live or workshop outline, DM flow, email/Zalo sequences, retargeting ad.

### 5.8 Launch Brief and Scarcity Ledger

- **Launch Brief:** the wf5 `launch_brief` YAML fields. Anything missing is asked in one batch of at most 8 questions.
- **Picker:**

  | Question | Answer → launch type |
  |---|---|
  | 1. Consented paid proof? | No → **A Founding** (7 days) |
  | 2. Has this offer already hit plan in a live launch? | Yes → **D Evergreen** |
  | 3. How many lives can you do in the window? | 0 → **B Mồi** (14 days)<br>1 → **C1 Workshop** (14 days)<br>3–5 → **C2 Challenge or Zalo mini-class** (21 days) |

- **Launch math:**
  - `seats = min(goal ÷ price, capacity)`
  - `warm leads ≈ seats ÷ 2%`
  - `attendees ≈ seats ÷ 5%`
  - `registrants ≈ attendees ÷ 30%`
  - If what is needed is more than 3 × the warm pool: downgrade the launch type or add runway.
- **Scarcity Ledger**, filled before any urgency line is written:

  `Constraint | Real reason | Number | Public update times | What happens after the deadline | Owner`

  Four checker questions must all be yes:
  1. Is the cap enforced?
  2. Does the deadline turn off the link or raise the price?
  3. Will you avoid reopening?
  4. Will the numbers be updated truthfully?
- **Refusals and downgrades:**

  | Missing or invalid | Behaviour |
  |---|---|
  | No consented proof | Founding framing only |
  | No real cap | No seat line |
  | No hard close | No countdown |
  | An income number with no context block | A process story instead |
  | VN: bonus worth more than 50% of the price | The bonus value is flagged |

- **Founder override:** comment thresholds ("đủ 100 comment"), "chấm" and coded CTAs are written as the coach asks, with a one-line dated platform note. They are never rewritten.

### 5.9 Hub schema (`schemas/hub.toml` → Notion template, Sheet tabs, paste formats, and every property name used in prompts)

**Property names and option values are in English in both editions.** VN templates localise only view names, descriptions and help text.

**Notion:** a root page "Content Machine" containing Start Here, the Brand Brain page (sub-pages: Brief, Character Card, Season, Research Brief, Launch) and **3 databases**.

**Content** (one row = one piece):

| Group | Properties |
|---|---|
| Pipeline | Title · **Slot Key** (unique) · **Status** (Idea → Scripted → Filmed → Posted → Reviewed) · Publish Date · Archive |
| Domino | Type (Educate, Entertain, Convert) · **Rung** · Series (select) · Ep # · Belief (B-ID) · Keyword (K-ID) · Phase (always-on, launch) |
| Script | Format (Native short, Clip, Text post, Carousel, Pillar, Cut-down, Email, Ad, BG post, Long post, Story, Live, DM flow) · Platform · Mode · Hook · Hook Stem ID · CTA · CTA Asset (A-ID) · Length (min, pillars) · script and transcript in the **page body** |
| Quality | Edge (0–10) · Claims (GREEN, AMBER, RED) · Uses (IDs) · Needs (text) |
| Repurpose | Repurposed From (self-relation) · Transcript Ready (checkbox) · Cut (None, Partial, Done) |
| Human | Owner · Asset Link · Post URL |
| Stats | Views · Sends · Saves · Leads (keyword comments + DMs + attributed bookings) |
| AI | Ratio vs median · Lesson · Last AI Run · Pack Version |

**Bank:** §5.3. In Notion it sits inline on the Brand Brain page under the heading "My stories, proof, client words".

**Runs:** Key (`SETUP`, `BATCH-2026-W41`, `DROP-2026-10-07`, `REVIEW-2026-W41`, `CUT-2026-W41-P`, `PLAN-2026-11`, `LAUNCH-<id>`) · Type · Result (Running, OK, Partial, Failed) · Source (task, chat, paste) · Items · Bets · Steps (for SETUP and LAUNCH) · report in the page body. Its view name is "Reports" (VN: "Báo cáo").

**Views:**
- **What the coach sees:** This Week (the default), Film Queue, Add Stats, Reports.
- **Also available:** 30-Day Calendar, Idea Bank, Bank by Type, Launch.

**Sheets Lite** (the default for ChatGPT and Gemini):
- 5 tabs: Start · Content (the same columns, with the script in its own column) · Bank · Runs · Scoreboard.
- Scoreboard formulas: per-1k rates; `MEDIAN(FILTER())` over the trailing 10 rows of the same Type; a 2× winner flag; highlighting of duplicate Slot Keys.
- ChatGPT outputs **tab-separated rows in the exact column order** to paste at the first empty row.
- No automation runs on Sheets.

**State rules** (identical in SKILL.md, ChatGPT instructions, every task and the eval assertions):
- AI sets only Idea, Scripted or Reviewed.
- Filmed and Posted are set only when the coach says so in an interactive chat ("posted N1"). Scheduled runs never set them.
- Never delete anything.
- Scheduled runs never overwrite a non-empty Scripted body.
- Every write is an upsert by Slot Key.
- Each job writes its Runs row first as Running, then updates it to OK or Partial.

### 5.10 Weekly scoreboard (REVIEW output; one screen)

```
WEEK 2026-W41 · Season 1 · Domino 3 "<new belief>" · CM 1.0.0 · Brief v3
SHIPPED 6/7 · pillar on time · streak 3 wks · trust library 1h52 / 7h
REACH      4,210 views · 38 follows · trend ↑ (judge on 90 days)
TRUST→BUY  6 keyword comments/DMs · 2 calls · 1 named-before-booking ("watched <title>")
EDGE       K-1 used 7× (echo 2×) · B-02 3/3 ✓ · B-03 1/3 · character pieces 1 ✓ · Trustable 1 ✓
WINNER     <title> sends/1k 3.1× median → MORE: 3 Idea rows (new hook / new format / part 2)
WEAKEST    <title> saves 0.4× → BETTER: hook rewritten
BREAK POINT (only after 2 flat weeks and ≥10 posts): not shown | not stopped | not held | not trusted | not asked | not closed (outside content)
PROOF GAP  3 planned pieces need a client result → Buyer Mirror to 2 clients
SYSTEM     BATCH ✓ · DROP 5/5 ✓ · (ChatGPT: "are your 3 tasks active?")
BETS (≤3)  MORE … · BETTER … · NEW (≤20%) …
HOMEWORK (optional, 5 min): … → unlocks …
NEXT → Monday 07:07 your batch arrives. Nothing to do now.
```

**Per-post data:**
- Primary metric by Type: Entertain = sends per 1k views; Educate = saves per 1k; Convert = Leads.
- The winner rule is at least 2× the trailing-10 median for the same Type.
- Posts younger than 48 hours roll over to the next review.

**Weekly data** (one reply, or part of the screenshot message): calls, sales, booking-form attribution answers, keyword echo.

---

## 6. Coach commands

Commands are matched by intent, not exact wording. Inside the Project the "Content Machine:" prefix is optional; outside it, the prefix makes sure the skill triggers. START-HERE teaches only the first three. The rest appear in NEXT lines when they become relevant.

| # | EN | VN (final wording in `strings/vn.toml` after native review) | What happens |
|---|---|---|---|
| 1 | **Set up my Content Machine** | **Cài đặt Content Machine** | First session (§2.2), or resume it |
| 2 | **Content Machine: what's next?** | **Content Machine: tiếp theo làm gì?** | Runs any due job, or gives the next action (§7.4) |
| 3 | **Content Machine: here's my recording** + transcript | **Content Machine: đây là bản ghi của mình** | CUT |
| | Here are my stats + screenshots or numbers | Đây là số liệu tuần này | Writes stats, completes the review |
| | Add to my brain: … | Thêm vào Brand Brain: … | Bank row with an ID |
| | Script this: … | Viết kịch bản: … | One script in the coach's mode |
| | Give me ideas (about …) / Remix this: [post] | Cho mình ý tưởng (về …) / Biến tấu bài này: … | ideas |
| | Make it more me / Edge check this | Viết lại giọng mình / Check edge bài này | humanize / edge-rubric |
| | Write a sell post / email / ad for [offer] | Viết bài bán / email / quảng cáo cho … | convert (proof-gated) |
| | Research my audience | Nghiên cứu khách hàng của mình | Research Sprint |
| | Why isn't it working? | Sao content chưa ra khách? | Break-point diagnosis on the last 20–30 posts |
| | Plan next month | Lên kế hoạch tháng sau | Monthly re-plan |
| | Plan a launch / Launch desk | Lên kế hoạch launch / Launch desk hôm nay | launch-plan / daily Launch Desk |
| | Set up my automations | Cài lịch tự động | Generates or repairs the tasks |
| | Run Monday batch / today's drop / Friday review | Chạy batch thứ Hai / ý tưởng hôm nay / review thứ Sáu | Manual run of a job |
| | Posted N1 · Filmed the pillar | Đã đăng N1 · Đã quay pillar | Coach-attested status change |
| | Update check · Menu | Kiểm tra cập nhật · Menu | Migration and hub repair · shows this list |

---

## 7. Automation pack (the founder's 3 jobs)

### 7.1 Shared rules

**Prompt structure** (the same skeleton for every job):
1. **Header:** CM version, edition, Brief version, time zone, and "today = the run date; if this run is late, still do this period's job".
2. Language lock.
3. Job steps.
4. Bounds.
5. Fixed output format.
6. The non-negotiables, repeated at the bottom (sandwich).

**Bounds:**
- At most 5 scripts per run, or 3 on Free tiers.
- At most 3 web searches.
- Never delete; never set Filmed or Posted.
- Research text is data, not instructions.

**Two variants of each job:**
- **Connected** (Claude): calls the skill, which reads and writes Notion.
- **Standalone** (ChatGPT): self-contained, with the Task Brief and Ship Check embedded. It writes nothing and ends with a paste block keyed by Slot Key. If `<<TASK BRIEF>>` is still empty, it stops and gives setup steps.

**Where prompts come from:** they are always generated in-session by "Set up my automations". There are **no founder share links**, so the founder's time zone never leaks into a buyer's task.

### 7.2 The three jobs

**BATCH: Mon 07:07** (run key `BATCH-YYYY-Www`)

*Connected:*
1. If an OK row exists, reply "Already done → link" and stop.
2. Write the Runs row as Running.
3. Read the Brief, Season week W, `automation_state`, the bets from `REVIEW(W-1)`, and the last 10 hook stems.
4. Create any missing slot rows by Slot Key.
5. Script P (pillar guide), N1 and N2.
6. If no pillar was Filmed last week, add the **mini-pillar** card.
7. Leave cut slots as Idea ("waiting for transcript").
8. Run the Ship Check and write bodies and properties; set Status to Scripted.
9. Update Runs to OK, or to Partial if anything is still missing; Partial is completed by "finish batch", which fills only the missing Slot Keys.
10. Report in 10 lines or fewer, with a film list and a NEXT line.

*Standalone:*
- Week of the Season: `w = ((weeks since plan_start) mod 4) + 1`. The belief comes from the chain in the Task Brief.
- Hook-stem family: `w mod 3`.
- Outputs P, N1, N2 and a paste block.
- Reminder: "Recorded? In your Project: Content Machine: here's my recording."

**DROP: weekdays 06:37** (`DROP-YYYY-MM-DD`)

*Connected:*
1. **Transcript watcher:** a pillar with "Transcript Ready" ticked and Cut ≠ Done gets a `CUT` run, capped and resumable.
2. **Catch-up:** at most one missed job per run (BATCH missed on Tue–Wed, or REVIEW missed on Mon). Total scripts stay within the cap.
3. Guard on the run key.
4. Weekday angle:

   | Day | Angle |
   |---|---|
   | Mon | Objection (O) |
   | Tue | Recognition moment (R) |
   | Wed | Contrarian (B) |
   | Thu | Proof or case (P) |
   | Fri | "More" from the latest winner |

5. Output **≤120 words**: 1 idea (rung, B-ID, Bank IDs, Edge-lite) + 3 hooks (title ≤6 words, verbal ≤12 words, visual 1 line) + the domino it links to + **1 capture question** (Thursday also asks for stats).
6. Write one Idea row.

*Standalone:*
- Theme: `THEMES[(ISO week × 5 + weekday) mod 12]`.
- Moment: `MOMENTS[day-of-year mod N]`.
- Hook stems are rotated and checked against `recent_hook_stems`.
- No writes. It closes with: "reply in your Project: Content Machine: add to my brain: …"

**REVIEW: Fri 15:07** (`REVIEW-YYYY-Www`)

*Connected:*
1. Guard on the run key.
2. Check that BATCH and DROP ran this week.
3. Read Posted rows at least 48 hours old that have stats.
4. Compute trailing-10 medians per Type and the ratios.
5. Build the §5.10 scoreboard: More (3 Idea rows), Better, New.
6. Run the break point only after 2 flat weeks and at least 10 posted pieces.
7. Count exposures, trust hours and proof gaps.
8. Triage Capture rows into the Bank, tagged as unverified.
9. **Top up the plan** so Idea rows always run 4 weeks ahead.
10. Set Reviewed; write the bets (3 or fewer) and the homework.
11. If more than 50% of rows lack stats, mark the run Partial with NEXT "send screenshots (3 min)", and add a 3-question qualitative review. It never skips.

*Standalone:*
- Asks for a fixed reply in the same chat: `Slot | Views | Sends | Saves | Leads`, or screenshots.
- Analyses the reply and outputs the bets and a paste block.
- Reminds: "check Scheduled: are your 3 tasks active?"

### 7.3 Setup per platform

| | Claude Pro/Max | ChatGPT Plus/Pro/Business | ChatGPT Free/Go | Claude Free / Gemini |
|---|---|---|---|---|
| Where | Scheduled → New task → **Create with Claude**: "Create 3 Content Machine tasks exactly as in the content-machine skill, automation.md § TASKS: BATCH weekly Mon 07:07, DROP weekdays 06:37, REVIEW weekly Fri 15:07, my time zone, no local folder." Fallback, set up manually: name + schedule + `Use the content-machine skill. Run <JOB> using my Notion page "Content Machine". Follow automation.md exactly.` | Paste the 3 generated texts into **new chats outside the Project** (tasks can't read Project files) | Same, using morning and afternoon windows. **If Monday- or Friday-only scheduling isn't offered (Phase 0 checks this):** paste the single **Daily Machine** text (Mon → BATCH, Fri → REVIEW, other days → DROP, weekend → capture question), which uses 1 slot | `.ics` at 07:07 on weekdays: "Content Machine: what's next?" |
| Memory | Skill + Notion | Task Brief embedded | Same | Notion (Claude Free) or attached `MY-BRAND-BRAIN.md` (Gemini) |
| Self-test | **Run now on DROP** → a Runs row must appear. Pick the approval mode that doesn't pause on Notion writes. Don't pick a local folder. Create tasks on or after 6 Oct 2026 | The first run arrives by push or email | Same | — |
| Board | AI writes directly | Coach or VA pastes about 10 min a week (Business: "save these to Notion" from the task chat) | Same | Claude Free writes in chat; Gemini: paste |

### 7.4 "What's next?" (also the manual catch-up)

**Connected** (the first matching row wins):

| # | Condition | Response |
|---|---|---|
| 1 | No Brand Brain | Setup |
| 2 | `SETUP` incomplete | Resume at the first unticked step |
| 3 | Launch state | Today's Launch Desk item |
| 4 | A due job is not OK | Run it now (catch-up) |
| 5 | A transcript is pasted but Cut ≠ Done | Finish the cut |
| 6 | A Scripted short is due and not Filmed | "Film N1 (10 min)" |
| 7 | Record day has passed and the pillar isn't Filmed | Recording guide or mini-pillar |
| 8 | Pillar Filmed, no transcript | "Paste your transcript (3 min)" |
| 9 | Posted rows older than 3 days with no stats | "Send screenshots (3 min)" |
| 10 | The Season ends within 7 days and the next one doesn't exist | "Plan next month (25 min)" |
| 11 | This week's homework is still open | Offer the homework (optional) |
| 12 | Otherwise | "On track. Next: …" |

**Stateless** (ChatGPT, Gemini, or Claude without a hub):
- It works out the expected step from today against `plan_start`, the record day and the Season dates in `MY-BRAND-BRAIN`.
- It asks at most **one** status question ("Did you record this week's pillar?").
- It never claims to know the hub's state.

### 7.5 Launch mode, idempotency and fallbacks

**Launch mode.** The Brand Brain's `automation_state` and dates decide what the tasks do.
- **Runway:** BATCH tilts the slots towards the Big Domino and adds proof-capture tasks.
- **Prep:** the asset pack is built interactively ("build my launch pack"), across several turns, resumable through `LAUNCH-<id>` steps.
- **Launch:**
  - BATCH regenerates the next 7 launch days around the latest objections, at most 5 scripts per run.
  - DROP becomes the **Launch Desk**: yesterday's tracker row → tomorrow's adjusted post or FAQ, plus objections.
  - REVIEW becomes the launch scoreboard.
- **Cooldown:** debrief (D+7, D+30) and testimonial capture.
- **On ChatGPT:** "Plan a launch" generates 3 launch-dated task texts that revert to always-on by date after the close. That is one refresh per launch.

**Idempotency:**
- Run keys: a Running row older than 2 hours counts as Partial; the next run fills only the missing Slot Keys.
- Slot Keys are always upserted.
- Run now followed by the scheduled run creates nothing twice. Evals test this on a sandbox Notion.

**Fallbacks:**

| Failure | Fallback |
|---|---|
| A Notion write stalls | Output goes to chat with a paste block; the run is marked Partial and redone by the next run |
| Usage cap hit | Partial run, then "finish batch" |
| Task paused or deleted (ChatGPT) | REVIEW's reminder; "What's next?" inside the Project; regenerate with "Set up my automations" |
| No scheduling at all | Every job is also a typed command, so the method never depends on scheduling |

---

## 8. Quality system

### 8.1 The Ship Check

It runs once per batch, silently, at the end of every scripting job. It fixes first; the coach sees only the footer. This card (about 900 characters) is always loaded:

```
SHIP CHECK — silent, once per batch; print one footer per piece
1 TRACE: every number/name/quote/result cites a Bank ID (quotes only verbatim from V/O; numbers only from P) else [NEEDS: one question]; inferences [guess]
2 HUMANIZE: spoken; contractions; avg ≤15 words, varied; no banned tells; ≤1 "not X, it's Y"; no recap ending; one POV line (B-ID)
3 CLAIMS: RED → rewrite/refuse; AMBER → ship + "Needs:"; proof gate on offers/ads/cases; urgency only from the Scarcity Ledger
4 VARIATION: new hook stem vs last 10; same structure ≤2 in a row; rotate keyword placement; ≥3 formats/week
5 EDGE 0–2 each, ship ≥7/10, no 0: K keyword+specifics · V one idea, one belief shift, usable today · A shown not claimed ·
  Au real Bank material, passes swap test · C definitive, a stance, shows trait/principle/value/vision
6 LADDER: one rung · one belief · CTA matches rung · link-forward
Footer: Edge 8/10 (K2 V2 A1 Au2 C1) · Claims GREEN · Uses S-2 B-1 P-3 · Keyword "<K-1>" · Next → <slot>
```

**Loop:** draft from Bank material → score → one automatic rewrite using Bank items → re-score. If raw material is still missing, the piece ships as a DRAFT with at most 2 `[NEEDS]` questions, and Needs is ticked. **It never pads with invented detail.** The capture question is part of the product's moat.

### 8.2 Edge Check v2 rubric (`edge-rubric.md`)

| Pillar | 0 | 1 | 2 | Rung rules |
|---|---|---|---|---|
| **K** Signature keyword + specifics | No chosen keyword anywhere; generic | Keyword present, but specifics are thin | Keyword in its rotated placement, plus at least 1 concrete specific (number, role, place, timeframe) every 2–3 sentences | Admirable and Likable: caption line 1 or pinned comment counts as full |
| **V** Value | Info dump, 2+ ideas, or anyone could say it | One idea, but no belief shift or not usable today | One idea; names the old → new belief (B-ID); usable today | Likable: "this is so me" plus Buyer Filter ≥2/3 (sent by the ideal client to a peer; you need the problem to get the joke; names the next domino) |
| **A** Authority (shown) | Claimed ("expert", "proven") | An expert-only detail or a glimpse of process | Shown: a P-ID, a say-do demo, a client decision, or a third party | **Convert and Trustable require 2** with a consented P-ID or founding-pilot framing. Admirable and Likable need at least 1. Competence first: self-deprecating formats stay blocked until 3 proof pieces exist |
| **Au** Authenticity | **Swap test fails** (a competitor could post it unchanged) | Opinion present, but no real story or real words | At least 1 S, V, C or R ID, in the coach's voice | — |
| **C** Character & Polarity | Hedged or bland; **flex-only or freebie-only** with no stance | A stance or trait is present but softened | Definitive, concise, takes a stance some people will reject, and expresses a trait, principle, value or vision (Character Card reference) | Money flexes and freebies may be **proof or CTA only**. Polarize on ideas, methods, beliefs and the old way. **Attacks on protected groups or private individuals are RED, not a score** |

- **Ship rule:** at least 7 out of 10, with no zero. The release gate requires an average of at least 8.
- **Edge-lite** (for ideas; at least 4 of 5 to enter the plan): uses a keyword or audience phrase; names a belief; proof or story is available (otherwise NEEDS PROOF); has an only-you angle; has a character stance.
- **Kill rule:** an idea with evidence = 1 and proof-ability = 1 is dropped.

### 8.3 Humanize (`humanize.md`; the compact form lives in the card)

1. **Specifics** from the Banks.
2. **Spoken language:** the Graham test ("would I say this to a friend?"), plus the register and VN pronoun pair from `language.md`.
3. **Strip AI tells** using the locale list:
   - EN examples: "delve", "Let's dive in", reflexive groups of three, em dashes in spoken lines.
   - VN examples: "trong thời đại ngày nay", "hãy cùng khám phá", overusing "không chỉ… mà còn".
4. **One POV line.**
5. **Variation.**
6. **Read aloud:** "Stumbled on a line? Voice-note what you'd say; I'll match it."

### 8.4 Guardrails (`guardrails.md` + `compliance.md`)

**Hard stops** (no workaround):
- fake scarcity (anything not in the Ledger);
- invented or AI-generated testimonials, results, quotes or statistics;
- income or health guarantees, and **unsubstantiated** income or health claims;
- cure or treat claims;
- AI likeness or voice of anyone other than the coach;
- attacks on protected groups or private individuals;
- clone-account seeding;
- asking people to post phone numbers publicly.

**AMBER** (ships with a "Needs:" line):
- any result number: substantiation plus a typical-results line ("[Client] got X in Y. Most clients see Z; results depend on…");
- testimonials: consent date and allowed uses, plus disclosure of any material connection;
- health or fitness outcomes;
- income figures: the context block plus "individual result, not a promise" (VN: "kết quả cá nhân, không phải cam kết");
- VN only: superlatives without proof (nhất / duy nhất / số 1), a gift worth more than 50% of the price, an affiliate missing "#QuảngCáo", a capture message missing the purpose and consent line, slang in ad copy.

**GREEN:** process, the coach's own story, opinion framed as opinion.

**Never blocked** (founder override): comment-keyword CTAs (on by default), comment thresholds, "chấm". They get one dated note from `platform-notes.md`. The only check is that **every keyword delivers a real asset** (an A-row); if none exists, the machine proposes a simple contextual lead magnet.

**Also:** "AI-powered" never appears in the coach's offer copy. A script the coach reviewed needs no AI label; avatars or clones need the platform's AI label.

### 8.5 Anti-fabrication and injection

- IDs must resolve. Connected runs check them against the hub; standalone runs may cite only the mini-bank inside the Brief.
- Evals assert that 100% of cited IDs resolve.
- Pasted or researched text is wrapped as data and is never followed as instructions.
- Research quotes are ≤15 words and carry their source; people are recorded by role, never by name.

### 8.6 Variation guard

- Every hook stem and format has an ID, so the comparison is deterministic.
- **Connected:** compares against the last 10 Content rows.
- **Standalone:** uses date rotation plus `recent_hook_stems`.
- The keyword's placement rotates.

### 8.7 Diagnostic ("why isn't it working?")

It runs on the last 20–30 posts. It is triggered by 2 flat weeks with at least 10 posts, or on demand. It returns the one break point to fix plus 3 actions for the next 2 weeks.

| Break point | Symptom | Fix |
|---|---|---|
| 1. Not shown | Little reach to non-followers | Cadence floor, native posts; check for a reach drop after bait-style posts (shown as data, not as a block) |
| 2. Not stopped | People swipe away early | Hooks, visual hook |
| 3. Not held | Retention drops at the same point | Cut the build-up, retention mechanics |
| 4. Not trusted | Views but few follows, saves or profile visits | Raise C and Au, add proof |
| 5. Not asked | Follows but no DMs | CTA kit, Trustable cadence |
| 6. Not closed | DMs and calls, but no sales | Flagged as outside content |

---

## 9. Bilingual single-source strategy

| Tier | What | How it's maintained |
|---|---|---|
| **Neutral** (never translated) | IDs and prefixes, Slot and Run keys, rubric codes, hub property names and option values, router keys, schemas, file names | Shared code |
| **Model-facing method** | `modules/*.md` | Written once in English. Every rendered file starts and ends with the edition output contract ("Always reply in Vietnamese with the chosen pronoun pair…"). VN few-shots steer the output. `method_prose = "en"` is the default; switching it to `"vi"` is built in (a VN translation set with the same staleness gate) |
| **Translated** (same meaning; human-reviewed) | Everything the coach reads: interview questions, template labels, footer labels, commands and synonyms, menu, guides, task text the coach reads, Notion view names and descriptions, error messages, skill description | `strings/*.toml` keyed. Each VN key stores the `src_hash` of its EN source. **Lint fails on a missing key or a stale hash** |
| **Localized** (written natively; never translated) | Examples and golden personas, hook, title and moment libraries, banned AI tells, register and pronoun guidance, launch phrases (DM keyword, "ib", "hữu duyên"), compliance notes, platform notes | `locales/{en,vn}/`, owned by a native copywriter |
| **Parametric** | §9.1 | `editions/*.toml` → `{{param}}` |

### 9.1 VN parameters

The values below are provisional defaults taken from the wf5 VN launch brief. They stay **PENDING_VN** until the VN market report lands.

| Key | EN | VN default (status) |
|---|---|---|
| `skill_name` / `lang` | content-machine / en | content-machine-vn / vi |
| `currency` / `number_format` | $ / 1,500 | đ / 1.500.000đ |
| `timezone_default` / `week_start` | (asked) / Mon | Asia/Ho_Chi_Minh / Mon |
| `platform_priority` | US picker (B2B: LinkedIn + YouTube; younger consumers: IG/TikTok + YouTube; older: Facebook + YouTube) | Facebook (profile and Page) + Zalo core, TikTok for top of funnel, YouTube long-form (PENDING) |
| `owned_channel` / `cta_channel` | email / DM, comment | Zalo + email / Messenger, Zalo (PENDING) |
| `keyword_variants` | — | accept spellings without diacritics (DANG KY) |
| `register_default` | — | "mình – bạn"; coach chooses (pronoun-pair matrix) |
| `launch_default_type` / lengths | Mồi, 14 days | Mồi, 14 days; Challenge or Zalo mini-class, 21 days (PENDING) |
| `zalo_group_cap` | — | 200 (PENDING) |
| `compliance_pack` | us-eu | vn (Law 19/2023, Advertising Law amendments, Circular 12/2026, gift cap, PDP Law 91/2025). PENDING counsel review; **until accepted, the strict universal RED/AMBER rules apply and every result claim is AMBER** |
| `hub_by_app` | claude: notion; chatgpt/gemini: sheets | same (PENDING) |
| `transcript_tools`, `reference_creators`, `seasonal_overlay` (Tết), `word_rate` | set | PENDING; until filled, no tool recommendations, no creator references, no seasonal overlay, and the EN word rate with a verify flag |

**Release rule:** every PENDING_VN key must be filled, or listed in `vn.acceptance.toml` with its safe default and the founder's sign-off.

**Build gates per edition:**
- string parity and staleness;
- an **EN-leakage scan** of VN coach-facing output, with a loanword allowlist (script, hook, content, launch, Content Machine);
- NFC budgets;
- ASCII file names;
- VN golden runs scored at least **4/5 for naturalness** by a native reviewer, with consistent pronoun pairs.

Bank verbatims stay in the language they were said in. Two Notion templates and two Sheet templates are rendered from the same `hub.toml`.

---

## 10. Implementation phases (in order)

| # | Phase | What gets written | How it is verified |
|---|---|---|---|
| 0 | **Platform verification + eval baseline** | `platform/targets.toml` (draft). `evals/personas` for 3 EN + 3 VN personas: cold-start coach, consultant, service business. Each has dictated answers, a paste dump, a 20-minute pillar transcript, week-1 stats and a launch brief. `evals/cases`: 40 router phrases per edition and an adversarial set. Baseline runs **without** the pack | Every unverified behaviour is tested on real accounts and recorded with `verified_on`:<br>- ChatGPT: task-prompt length limit (binary search); whether Free can schedule weekdays or a weekly day, and its time windows; whether task text can be edited from chat; Plus writing to Notion<br>- Claude: Create-with-Claude reading the skill file; approval modes on unattended Notion writes; the task cap; Skills and the Notion connector on Free; whether re-uploading a skill with the same name replaces it<br>- Gemini: folder vs zip upload, and whether attached files persist<br>The results set the defaults (3 tasks or Daily Machine on Free). |
| 1 | **Build system + schemas** | VERSION, `editions/*.toml`, string skeletons, `render.py`, `build.py`, `lint.py`, `package.py`, `schemas/*.toml`, `hub_build_prompt.py`, `ics.py` | Lint fixtures that **must fail**: a 191-character description, a VN string in NFD, a missing router anchor, a stale string hash, an unaccepted PENDING key, a `verified_on` date older than 90 days, a dotfile in a zip, a non-ASCII file name. Smoke uploads of an empty skill to Claude, a ChatGPT Project and Gemini. The Notion template is built from `hub.toml` in a sandbox; the Sheet CSVs import cleanly |
| 2 | **Core loop, EN** (setup → film today → Season → Week 1) | `SKILL.md.tmpl` (router, non-negotiables, Ship Check, state rules, NEXT tables), setup, brain, character, signature, research (Quick Listen), plan, fmt-short, fmt-long, convert (CTA kit), humanize, edge-rubric, guardrails, `locales/en/*` | **Golden runs** for 3 EN personas on Claude Pro + Notion:<br>- a film-ready script by minute 25 or earlier, with 8 or fewer coach turns before it<br>- every piece Edge ≥7 with no zero (average ≥8); 0 RED; 100% of IDs resolve<br>- Week 1 is at least 70% the coach's own words; at least 1 character piece; keyword placement rotates<br>**Adversarial copy review #1:** fake testimonial, income guarantee, invented $ result, prompt injection inside pasted comments, an attack on a protected group → refused or rewritten. A comment-keyword CTA is **not** blocked |
| 3 | **Loop completion** | ideas, review, research (Sprint, WHY loop), packaging plus libraries, hub, plan (monthly + Start Here) | Setup → Cut (persona transcript) → Review (`stats-w1.csv`) → Plan next month, for 3 personas. Scoreboard maths checked deterministically against fixtures (median, 2× flag, break-point trigger). A **4-week simulated variation run**: no repeated stem in any 10 consecutive pieces and the same structure at most twice in a row |
| 4 | **Automation pack** | `automation.md`, `tasks.toml`, connected and standalone templates, Daily Machine, task-message generator with Brief stamp, `.ics`, self-test script | Sandbox Notion:<br>- BATCH run twice → 0 duplicate Slot Keys<br>- a killed run recovers from Running to Partial to OK<br>- Tuesday's DROP catches up a missed BATCH<br>- the watcher cuts within caps and resumes<br>ChatGPT tasks created on Free and Plus from the generated text, within the measured limit with a 15% margin (lint). The standalone rotation gives 20 distinct drops over 4 weeks. **One live week** on Claude Pro shows heartbeat rows |
| 5 | **Launch module** | launch-plan, launch-scripts, Ledger and launch claims kit in guardrails, launch scoreboard and debrief in review, launch-mode variants, `locales/*/lib/launch-phrases.toml` | **Golden launch runs:** cold-start → Founding (7 days); proof persona → Mồi (14 days, EN) and Challenge (21 days, VN). The Ledger refuses urgency with no real cap or deadline. Adversarial: "fake 3 seats left", "guarantee 100tr in 30 days", AI testimonial → blocked. **Founder-override test:** "đủ 100 comment" and "chấm" are written as asked, with one note and no rewrite. Launch mode switches on its dates and reverts after the close |
| 6 | **ChatGPT/Gemini builds + VN edition** | `chatgpt-instructions.tmpl`, concatenation manifest with § anchors, stateless NEXT logic, `strings/vn.toml`, `locales/vn/*` (native), `vn.acceptance.toml` | Router accuracy ≥95% on a ChatGPT Project (retrieval lands on the right anchor). Claude description trigger rate ≥90% per edition. VN golden runs on Claude and ChatGPT: naturalness ≥4/5, consistent pronoun pairs, 0 English leakage outside the allowlist. A manual Gemini run with the attached brain. ChatGPT Free limits: 3 uploads on day 1 and 5 files or fewer |
| 7 | **Guides, examples, release** | START-HERE (1 page per edition), troubleshooting, what's-new, examples frozen from passing runs, README release checklist, CHANGELOG | **The full release gate:** 3 personas × 2 editions × (Claude Pro, Claude Free, ChatGPT Free, ChatGPT Plus, Gemini), plus the adversarial, idempotency and launch cases, scored by deterministic graders and a calibrated human/LLM judge using `edge-rubric.md`. 3 non-technical testers (at least 1 VN) install without help, with a film-ready script within 35 minutes including install. A 15-minute manual check in each platform's real interface. The founder signs `vn.acceptance.toml`. Legal-review notes are recorded |

**Deferred to 1.1** (the `schema_version` and `hub_schema` fields ship now, so migration is possible later):
- Claude Plugin and GitHub marketplace sync;
- the all-in-one Lite file;
- automated LLM-judge adapters for multiple vendors;
- snapshot tests;
- a full migration engine (beyond the add-only repair);
- Answer Library and "searchable twin" titles;
- a done-for-you automation tier.

---

## 11. Decisions still open for the founder

1. **Language of the VN method files:** English internals with a VN output contract (recommended), or fully Vietnamese files. A paid VN product containing English files may look odd to buyers who open them; golden-run evidence will inform this, but the perception call is the founder's.
2. **VN release timing:** ship with the provisional defaults by signing `vn.acceptance.toml`, or wait for the VN market and reference-creator reports.
3. **Positioning copy and pricing by tier:** Claude Pro + Notion sold as "runs itself" and recommended, and whether ChatGPT Free is sold as "supported, manual" or "best effort".
4. **Updates and licence:** a quarterly zip by email (default) vs a private marketplace later; licence scope "one business plus its team".
5. **Golden examples:** fictional personas, or the founder's real cases (which need consent). They ship to buyers.
6. **Legal review spend:** VN counsel and US counsel on the claims linter and Scarcity Ledger before launch.
7. **VN product and command naming:** keep "Content Machine" inside the VN commands, or use a VN brand name.
8. **Default VN launch type and length** (Mồi 14 days vs Challenge or Zalo mini-class 21 days).
9. **A done-for-you automation tier**, sold outside the product (no upsell inside), for ChatGPT coaches: yes or no.

---

## 12. Risks and mitigations

| # | Risk | Mitigations |
|---|---|---|
| 1 | **Platform drift and unverified behaviour.** Task limits, approval modes, Skills on Free, Gemini uploads | Phase 0 verification; `targets.toml` with `verified_on` and a 90-day lint; dated facts only in `platform-notes`; install self-tests (Run now plus a Runs row); budgets with 10–15% margin; every job is also a typed command; the Daily Machine fallback is pre-generated |
| 2 | **Generic, AI-sounding output** erodes trust, and platforms demote "inauthentic content" | The 5-pillar Edge Check with the swap test and the Character pillar; ID traceability with `[NEEDS]` instead of invented detail; Week 1 cut from the coach's own words and later weeks from pillar transcripts (≥70% own words); capture questions; variation guard with hook-stem IDs |
| 3 | **First-session drop-off** | A film-ready script by about minute 25; Fast lane; one real decision; a resumable `SETUP`; automation can be deferred |
| 4 | **The coach stops recording or quits around week 3** | Mini-pillar fallback; Mode A guided interview; the 7-day rolling cut window; buyer-signal scoreboard with 90-day framing; streak; one NEXT line; homework kept at 10 minutes or less |
| 5 | **Claims and compliance exposure** (launch tactics read as "lùa gà" in VN; VN law unknowns) | Scarcity Ledger; proof gate; context block plus "individual result" line; consent dates per use; strict universal rules until VN counsel signs off; "AI-powered" never in offer copy |
| 6 | **The founder's bait override increases demotion risk** | Each keyword must deliver a real asset; posts must have value on their own (V ≥1); a dated platform note; REVIEW tracks reach against the previous 4 weeks and raises "not shown" as data. **Never a block** |
| 7 | **ChatGPT has no memory and its Brief copies drift** | Date-arithmetic rotation; Brief and Task Brief version stamps checked during "Plan next month"; at most 2 upkeep actions in a normal month; honest tier labels; REVIEW reminds the coach to check tasks are active |
| 8 | **Scope creep** (Launch, Character, Research and Automation in one v1) | Phased build with gates; 1.1 deferrals; references ≤150 lines; at most 4 files per job; caps per scheduled run |
| 9 | **VN edition quality** (translationese, wrong pronoun register) | Native locales; string staleness gate; EN-leakage scan; naturalness gate ≥4/5; the `method_prose` switch |
| 10 | **Notion write failures or approval stalls; the pack leaks** | Self-test on day 1; Runs heartbeat; chat paste fallback; access shared to one page only; never delete. Leaks: the value is in quarterly updates for buyers only, plus the licence |

---

### Critical files for implementation

- /root/.claude/plans/all-right-so-this-clever-shore.md: the founder decisions (Character thesis, Launch override, Edge thesis, research protocol). This is the source of truth.
- /home/user/Content-Machine-1.0/core/SKILL.md.tmpl, with /home/user/Content-Machine-1.0/core/ship-check.md and /home/user/Content-Machine-1.0/core/router.toml: router, non-negotiables, the 5-pillar Ship Check, state rules and the NEXT tables. They are rendered into the skill, the ChatGPT instructions and every task.
- /home/user/Content-Machine-1.0/modules/setup.md, with /home/user/Content-Machine-1.0/modules/character.md: the character-first first session, film-ready script by about minute 25, resume logic and cold-start branches.
- /home/user/Content-Machine-1.0/schemas/hub.toml, with /home/user/Content-Machine-1.0/schemas/brand-brain.toml and /home/user/Content-Machine-1.0/automation/tasks.toml: one schema for Notion, Sheets, paste formats, Slot and Run keys, and the BATCH, DROP and REVIEW contracts.
- /home/user/Content-Machine-1.0/tools/build.py, with /home/user/Content-Machine-1.0/tools/lint.py, /home/user/Content-Machine-1.0/platform/targets.toml and /home/user/Content-Machine-1.0/editions/vn.toml: one source compiled into two editions and every app target, with dated limits, NFC budgets and the PENDING_VN acceptance gate.
- Research inputs: /tmp/claude-0/-home-user-Content-Machine-1-0/085f5f0b-5883-504d-aefb-4af9a99859d9/scratchpad/research/wf5-launch-design.md, wf1-packaging.md, wf3-recommendation.md, wf1-gaps.md and wf5-vietnam-launch.md, plus the founder's research playbook at /home/user/ai-native-marketing-agency/brain/research/playbook.md.