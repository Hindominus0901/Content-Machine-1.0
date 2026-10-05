# Content Machine 1.0: recommended architecture for the content hub and automation (synthesized 5 Oct 2026)

## 1. The recommendation

The system has three parts: one Brain, one Board and one Engine.

- **Brain (the method).** This is the pack itself, delivered in two forms:
  - On Claude, one Skill ZIP per language.
  - On ChatGPT, a Project with at most 5 files per language. Five files is the ChatGPT Free project limit, so this is a hard packaging constraint.

  Each buyer also gets a Brand Brief of 600 words or less, written during setup.
- **Board (the one place).** A Notion template called "Content Machine". It holds every idea, series, script, the calendar, status, stats and a log of every automated run. The AI connector and the VA are given access to this one page and nothing else.
  - For coaches who refuse Notion, a Google Sheets "Lite" edition uses the same columns. It runs manually only.
- **Engine (the automation).** One set of five task prompts, three of them core, shipped in two variants:
  - **Claude variant:** reads and writes the Board through the Notion connector. Tasks pass work to each other through the Board, so the Friday review feeds the Monday batch.
  - **ChatGPT variant:** fully self-contained, with the Brand Brief pasted inside the prompt. It delivers drafts to chat, push and email, and a human or VA pastes them into the Board.
  - **Fallback for every tier:** the same five prompts as run-sheet cards, plus calendar reminders (.ics).

Be honest in the product copy about the two platforms:
- **Claude Pro (US$20 a month, or $17 billed annually) with Notion is the only native setup that runs the whole loop by itself, including the Board.**
- **ChatGPT works as "drafts arrive in your inbox, a person files them."**

Sell Claude Pro as the recommended path and ChatGPT as fully supported but semi-manual. Neither path depends on Pulse, agent mode or Routines. Pulse was retired, agent mode is reportedly removed, and Routines need GitHub, which non-technical coaches won't have.

## 2. What each platform can actually do (October 2026)

| Capability | Claude Pro/Max | Claude Free | ChatGPT Plus | ChatGPT Free/Go | ChatGPT Business |
|---|---|---|---|---|---|
| Scheduled tasks | Yes. Run in the cloud while the laptop is asleep, unless they use a local folder. Presets: hourly, daily, weekly, weekdays, manual. **No monthly preset.** Task limit not documented | **None** | 5 tasks, exact times | 3 tasks, at most once a day, in a morning, afternoon or night window | 10 tasks |
| Can a task use the Brain? | Yes. Skills and connectors work in tasks | n/a | **No.** Tasks can't read Project files or Custom GPTs, so the brief is pasted into each prompt | Same as Plus | Same as Plus |
| Can a task write to the Board? | Yes, through the Notion connector. Approval-mode behaviour is not documented, so test with Run now | n/a | **No.** Named task apps are Gmail, Slack and GitHub. Waiting for approval auto-pauses the task | No. Output is a chat message only | No inside the task |
| Can you write to the Board from a normal chat? | Yes | **Yes** (directory connectors work on every plan) | Not verified; test it during setup | Unlikely or not verified | Yes, once the admin enables the Notion app's write actions |
| Can one task hand work to the next? | Yes, through the Board | n/a | No. Each run is its own chat | No | No |
| Can the coach share the Project with a VA? | Team and Enterprise only | No | Yes | Yes | Yes |

On ChatGPT, web search inside tasks on Free counts against the normal chat quota. On both platforms, every scheduled run uses up plan usage.

## 3. Hub schema (Notion: one root page called "Content Machine")

The root page holds one "Start Here" page, the Brand Brain page and four databases.

**Start Here (page):** the weekly routine for the coach and the VA, links to the views, and the date the instructions were last revised.

**Brand Brain (page, not a database):**
- **Brand Brief**, 600 words or less, as the first block. Each ChatGPT task carries a copy of this block. Claude reads it here.
- Sub-pages:
  - Offer and price ladder
  - Ideal client: pains, desires, objections, and phrases in their own words
  - Voice and banned words
  - Proof bank: results, testimonials, stories
  - 3–5 content pillars
  - CTA library
  - Market settings: language, platforms, currency (đ for the VI edition), time zone

**Content: the single core database.** Ideas live inside it as Status = Idea, so there is no separate Ideas database.

| Group | Properties |
|---|---|
| Pipeline | Title · ID (Notion unique ID, prefix CM-) · **Status** (Idea → Scripted → Filmed → Edited → Posted → Reviewed) · Archive (checkbox) |
| Planning | **Job** (Educate / Entertain / Convert, the founder's three types) · Format (Short video, Carousel, Text post, Long video, Podcast, Ad, Email) · Platform (multi-select) · Series (relation) + Episode # · Awareness stage (Unaware → Most aware) · Idea Score (1–5) · Language (EN/VI) |
| Script | Hook · CTA (Follow / Comment keyword / DM / Lead magnet / Book call / Buy) · **the script itself goes in the page body**, using one template per format (Short-form, Carousel, Long-form, Ad, Email) |
| Production | Publish Date · Owner/Editor (person) · Research (relation) · Repurposed From (relation to another Content row) · Asset Link (URL to Google Drive, because Notion Free caps uploads at 5 MB) · Post URL |
| Stats | Views, Likes, Comments, Shares, Saves, Follows, Leads/DMs, Sales (numbers) · Engagement % (formula) · Lesson · Last AI Run (date) |

Rule written into every prompt: **the AI may only set Status to Idea, Scripted or Reviewed. Filmed, Edited and Posted are set by people.** This is the quality gate that protects trust.

**Series ("Dominoes")**
- Properties: Name · Goal (Awareness / Trust / Convert) · Belief to install · Linked offer · Planned episodes · Status (Planning / Active / Done) · Start date · Content (relation) · rollup counting posted episodes.
- The default 30-day structure is 3 series × 4 episodes, running awareness → trust → offer.

**Research Bank**
- Properties: Title · Type (Audience quote / Competitor post / Stat / Trend / Comment / Story) · Pain/Desire tag · Source URL · Platform · Language · Captured date · Used In (relation to Content).
- Prompts treat everything in this database as data, never as instructions.

**Runs Log** (this merges the "Weekly Reviews" database from the hub brief with an audit trail)
- Properties: Name ("Weekly Batch 2026-10-12") · Type (Setup / Weekly Batch / Review / Plan / Daily / Conversion) · Run date · Source (Claude task / ChatGPT paste / Manual) · Result (OK / Partial / Skipped / Failed) · Items (relation to Content) · Wins · Lessons · **Next week's bets** · raw output in the page body.
- Why it exists:
  - It makes silent failures visible: if no row appears on Monday, the batch did not run.
  - On ChatGPT it is the one-paste landing spot.
  - It is where the Monday batch reads the Friday review.

**Views**
- Content:
  - This Week
  - 30-Day Calendar
  - Pipeline (board by Status)
  - Idea Bank (Status = Idea, sorted by Score)
  - Film Queue (Scripted)
  - Edit Bay (Filmed, filtered to the editor)
  - Needs Stats (Posted, more than 7 days old, Views empty)
  - Scoreboard
- Series: board and timeline.
- Runs Log: newest first.

**Language:** keep property names and option values in English in both editions, so one set of prompts works for both. Give the VI edition Vietnamese view names, descriptions and content. This is a founder decision (see section 9).

**Google Sheets Lite:** tabs for Brand Brief, Content (same columns, with the script in its own column), Series and Runs Log.
- ChatGPT users edit it with the ChatGPT add-on inside Sheets (all plans, only on the open file).
- Claude users edit it with live editing (beta, Chrome or Desktop only).
- **Do not automate on Sheets.** Claude's Sheets editing is only weeks old, the add-on does not run in scheduled tasks, and whether the connector works in scheduled tasks is not verified.

## 4. Automation pack

| # | Task | Claude Pro | ChatGPT | Tier |
|---|---|---|---|---|
| T1 | **Weekly Batch:** research + scripts for the week | Mon 07:07 | Mon 07:07 (morning window on Free) | Core |
| T2 | **Friday Review:** stats → keep / stop / try → next week's bets | Fri 15:07 | Fri 15:07 (afternoon window on Free) | Core |
| T3 | **Runway Planner:** the 30-day plan and series arcs | Fri 16:07 weekly, with a state check: plan only if fewer than 14 days are scheduled ahead, then top up to 4 weeks | Weekly, with a date check: "if today is not in days 1–7 of the month, reply SKIP" | Core |
| T4 | **Daily Spark:** today's post pack, or one POV / "if you know you know" relatable post | Weekdays 06:37; reads This Week | Weekdays 06:37; standalone, works from the brief only | Optional (Claude Pro, ChatGPT Plus+) |
| T5 | **Conversion Check:** best educational post → 1 editorial-style converting post + 2 ad hooks + 1 email | Wed 12:07 | Wed 12:07 | Optional |

- ChatGPT Free and Go users stop at the 3 core tasks.
- Plus users can run all 5, which **uses every slot they have**. Warn them that this leaves no slots for other tasks.

On Claude, the tasks chain through the Board: T2 → T3 → T1.
- T2 writes "Next week's bets" to the Runs Log.
- T3 fills the Calendar.
- T1 reads both.

### Rules every prompt follows

- **Header:** today's date; output language and market hard-coded (VI: Vietnamese, local platforms, đ pricing, local examples); and "if this run is late, still produce this week's batch."
- **Brain:** on Claude, "Use the content-machine skill; read Brand Brain from Notion." On ChatGPT, the Brand Brief block is pasted into the prompt.
- **Safe to re-run:**
  - Only act on rows with Status = Idea and a Publish Date in the target week.
  - Skip anything already Scripted.
  - Never delete anything.
  - Never set Posted.

  This matters because Run now followed by the scheduled run must not create duplicates.
- **Bounded:**
  - A fixed piece count: 5 a week by default (2 Educate, 2 Entertain, 1 Convert), right for 1–2 hours a week.
  - A cap on web searches per run.
  - A fixed output table: Day | Format | Series | Hook ×3 | Script | CTA | Caption.
- **Claude only:** write scripts into the page bodies, set Hook, CTA, Status and Last AI Run, then add a Runs Log row with Result = OK or Partial.
- **ChatGPT only:**
  - End with a "Paste checklist" saying which dated Content row each script goes into.
  - T2's output asks the coach to reply with their numbers in a fixed format, then analyses them in the same chat.
  - T3's output includes (a) a CSV of the plan and (b) a ready-made "Plan block" to paste into T1's instructions. If the plan block is not pasted, T1 falls back to the evergreen weekly rhythm in its prompt.
- **Scheduling:** schedule a few minutes past the hour (7:07, not 7:00), because runs can start several minutes late.

## 5. Setup steps

### A. Claude Pro + Notion, the recommended path (installs in about 13–15 minutes)

The brand interview comes on top of this, at about 15–25 minutes, and voice dictation is fine.

1. **(2 min)** Create a Notion account. Open the template link and click **Duplicate**.
2. **(2 min)** In Claude, go to **Customize → Connectors → Notion → Connect**. Sign in through the browser and grant access **only to the "Content Machine" page**.
3. **(2 min)** Turn on code execution. Go to **Customize → Skills → + → Create skill → Upload a skill** and upload content-machine-EN.zip or content-machine-VI.zip.
4. **(2 min)** Create a Project called "Content Machine". Paste the one-block project instructions, which include the Notion page link.
5. **(interview)** Type "Set up my Content Machine." Claude:
   - interviews the coach;
   - writes the Brand Brain;
   - creates 3 series;
   - adds about 30 dated Content rows (the 30-day plan);
   - fully scripts Week 1 (Status = Scripted);
   - logs a Setup run.
6. **(5 min)** Inside the project, go to **Scheduled → New task → Create with Claude** and paste: "Create the Content Machine core tasks T1–T3 from the skill's automation file." You can also use **Set up manually** and paste each prompt.
   - Do **not** pick a local folder, or the task falls back to running locally and stops when the laptop sleeps.
   - Click **Run now** on T1 while you watch. Check whether the approval mode stalls on Notion writes, and pick the setting that lets writes go through. Because of the idempotency rules, this test run does not duplicate Week 1.
   - Create the tasks on or after 6 Oct 2026. That is the date from which new Cowork tasks on Pro and Max run in the cloud.
7. **(1 min)** Invite the VA to the Content Machine page as a **guest** with *Can edit*. Notion Free allows 10 guests and is "limited for 2+ members".

### B. Claude Free: manual machine

- Same as steps 1–5 above. The connector, Skills (code execution must be on) and Projects all work on Free.
- There is no scheduling. Import the .ics reminders. Each one says: open Claude → Content Machine → type "run weekly batch" (or "run review", "run plan").
- Claude still writes to Notion. Free usage limits are tight, so batches stay small.

### C. ChatGPT Plus (Free and Go work the same way, capped at 3 core tasks with time windows)

1. **(2 min)** Duplicate the Notion template, or copy the Sheets Lite file.
2. **(3 min)** Create a Project called "Content Machine". Upload the 5 edition files and paste the project instructions.
3. **(interview)** In the project, type "Set up my Content Machine." ChatGPT returns:
   - the Brand Brief block;
   - a 30-day plan as a CSV file;
   - Week 1 scripts.
4. **(3 min)** In Notion, open the Content database **••• → Merge with CSV**.
   - Merge only ever *adds* rows. That suits a new month's plan, which is all new rows.
   - Paste the Week 1 scripts into the bodies of the matching dated rows, or have the VA do it.
5. **(1 min)** **Settings → Notifications:** set tasks to Push + Email.
6. **(4 min)** Create the tasks **outside the Project** (tasks can't read Project files).
   - Click the founder's **share links** for T1–T3, or T1–T5 on Plus. Paste in your Brand Brief, **change the time zone** (share links keep the creator's), and save.
   - Without share links: go to Sidebar → Scheduled and paste each prompt.
7. **(1 min)** Write test: in a normal chat, ask the Notion app to add a test row to Content.
   - If it works (confirmed on Business; not verified on Plus and Pro), the weekly routine becomes: open the task's chat → "save these to Notion" → approve.
   - If not, paste manually.
8. **Weekly VA routine, about 10 minutes:**
   - open each delivered task chat;
   - paste the raw output into a new Runs Log row;
   - paste each script into its dated Content row and set Status = Scripted.
9. **Monthly, about 5 minutes:**
   - merge T3's CSV into Notion;
   - paste T3's "Plan block" into T1's instructions;
   - update the Brand Brief in each task if it has changed.

### D. ChatGPT Business

The admin enables the Notion app's write actions. Tasks still deliver to chat. The coach or VA then writes to the Board from the task chat. Up to 10 tasks are available.

### E. Optional add-ons (not in the default pack)

| Add-on | Cost | What it does | Fit |
|---|---|---|---|
| Notion Custom Agents | Business plan $20 per member per month + $10 per 1,000 credits | Run T1–T5 inside Notion on monthly or weekly schedules, with Claude or GPT models | The only hands-off option that doesn't depend on Claude or ChatGPT |
| Zapier Pro | about $20 a month | Schedule → AI by Zapier → Notion | Possible done-for-you upsell |
| Make | $12 a month + API costs | Same idea, with your own API key | Possible done-for-you upsell |
| n8n, Apps Script | — | Same idea | Too technical for this buyer |

## 6. Feature ladder by plan

| Tier | Runs by itself | Board updated by | Coach effort each week |
|---|---|---|---|
| Claude Pro + Notion | T1–T5 | AI writes directly | Review scripts, film. VA: stats, editing |
| ChatGPT Business + Notion | T1–T5 (drafts) | Person approves in chat | + about 5 min |
| ChatGPT Plus + Notion | T1–T5 (drafts) | VA pastes; CSV monthly | + about 10 min |
| ChatGPT Free/Go | T1–T3 (time windows) | VA pastes | + about 10 min |
| Claude Free | Nothing (calendar reminders) | AI writes when you run a command | + about 5 min to trigger |
| Any plan, Sheets Lite | As per the plan | Manual or add-on | + about 15 min |

## 7. Zip layout (one per language edition)

| Folder | Contents |
|---|---|
| `00-START-HERE` | One-page setup checklist for each platform, dated "last revised" |
| `claude/` | content-machine skill ZIP, project instructions |
| `chatgpt/` | 5 files: Method, Formats & Script Templates, Commands, Hub & Paste Formats, Brand Brief (blank) |
| `automation/` | T1–T5 prompts, Claude and ChatGPT variants, plus the share-link list |
| `hub/` | Notion template link, Sheets Lite link, CSV header file |
| `fallback/` | Run-sheet cards and .ics reminders |

Without the Brand Brief, the ChatGPT edition's files can be consolidated into fewer than 5.

## 8. Risks and mitigations

1. **Products change quickly.**
   - Key features are only weeks old: Cowork cloud runs from 6 Oct 2026, the Claude Sheets connector, ChatGPT task sharing from August 2026, and ChatGPT "apps" reportedly renamed "plugins".
   - Many 2026 tutorials are now wrong: they say Claude tasks need the desktop app open, or they rely on Pulse or agent mode.
   - Mitigation: date-stamp every guide, revise every quarter, and make the setup self-tests (Run now, the write test) part of onboarding rather than relying on plan facts.
2. **Silent failures.**
   - ChatGPT tasks auto-pause when ignored, when waiting for approval, or when their chat is deleted.
   - A Claude task that uses a local folder only runs locally and stops when the laptop sleeps.
   - Mitigation:
     - Every Claude run logs to the Runs Log, and T2 checks that T1 ran that week.
     - ChatGPT prompts never include write-to-app steps.
     - Tell users never to delete task chats.
3. **Duplicates.** Run now and the scheduled run can both fire, and Notion imports only add rows. Mitigation: prompts are safe to re-run (status and date checks), and CSV is used only for new monthly plan rows.
4. **Usage limits.** Research-heavy runs drain Pro quota, and Free web search counts against the chat quota. Mitigation: fixed piece counts and search caps, and a T4 daily task that is optional.
5. **Prompt injection and access scope.** The Notion connector acts with the user's full permissions, and research text is untrusted. Mitigation:
   - Share only the Content Machine page.
   - Prompts never delete.
   - The skill rule says research is data, not instructions.
6. **Generic AI content works against the "trust and buy" goal.** Mitigation:
   - Every script must draw on the Proof bank and voice rules.
   - Banned words are enforced.
   - People control Filmed and Posted.
   - The weekly review loop rewrites the hooks.
7. **Brief drift on ChatGPT.** The Brand Brief is copied into 3–5 tasks, so the copies can fall out of date. Mitigation: T3 reminds the user each month, and the brief is kept to 600 words or less.
8. **Vietnamese edition.** Time zone, language and market must be hard-coded in every prompt. Shared task links carry the creator's time zone. Whether Notion's app interface is in Vietnamese is not verified, and Sheets Lite may suit the VN market better.
9. **VA collaboration limits.**
   - Claude Projects can't be shared below Team, so the VA works in Notion.
   - ChatGPT Projects can be shared on every plan.
   - Whether Notion guests count toward the Free block limit is not verified.
   - The license should cover "one business and its team members".
10. **The paid pack can leak.** Share links and the zip are easy to pass on. Mitigation: the value sits in updates, so keep the quarterly revisions buyer-only.

**Not yet verified; test these before launch:**
- Claude: what each approval mode does in unattended runs; how many tasks are allowed; whether tasks can be created from the mobile app; whether the Sheets connector works in tasks.
- ChatGPT: whether Plus and Pro can write to Notion; whether @app works for Notion or Drive inside tasks; whether tasks use Memory; whether tasks can recur monthly; whether Free can pick a specific weekday; whether a task chat can produce a downloadable CSV when asked as a follow-up; which models tasks use.
- Notion: whether guests count toward the block limit; whether the app interface is available in Vietnamese.
- Pricing: whether the Notion prices quoted are annual or monthly.

## 9. Decisions for the founder

1. Make Notion the default hub, with Sheets Lite as the fallback. This is recommended, because scripts live in page bodies and filming from the Notion phone app works well. Consider whether Sheets should be the default for the VI edition.
2. Keep property names in English across both editions (recommended), or localize them and maintain two sets of prompts.
3. Position Claude Pro openly as "full auto" and ChatGPT as "drafts and paste".
4. Decide whether to sell a done-for-you automation tier (Notion Custom Agents or Zapier) for coaches who stay on ChatGPT but want everything hands-off.

No files were created or edited; the repo at /home/user/Content-Machine-1.0 holds only an empty placeholder file called `yeah`.