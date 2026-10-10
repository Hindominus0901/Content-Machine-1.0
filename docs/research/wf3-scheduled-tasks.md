# Brief: Scheduled and recurring AI tasks for Content Machine 1.0 (checked 5 Oct 2026)

Method note: help.openai.com, openai.com and chatgpt.com all returned HTTP 403 to my fetches. Every ChatGPT fact below therefore comes from dated secondary sources that cite the OpenAI Help Center or release notes. They agree with each other unless I say otherwise. I read the Claude, Notion, Zapier, Make, n8n and Google sources directly. The session's web-search budget ran out partway through, so a few items are marked UNVERIFIED.

---

## 1) Facts (with sources)

### A. ChatGPT

**Scheduled tasks (core feature)**
- **History:**
  - Tasks were relaunched around 17–18 June 2026, with their own **"Scheduled" page in the sidebar**. That page lets you view, pause, edit and delete tasks and shows exact run times.
  - Free accounts got tasks on **25–26 Aug 2026**, and paid plans got event triggers the same week. Sources: [usecarly, 22 Jun 2026](https://www.usecarly.com/blog/chatgpt-scheduled-tasks/), [yellow.com, Jun 2026](https://yellow.com/news/chatgpt-pulse-scheduled-tasks-hub), [AndroidHeadlines, 26 Aug 2026](https://www.androidheadlines.com/2026/08/chatgpts-task-scheduling-feature-is-now-free-but-not-without-limits.html).
- **How to create:** two ways.
  1. In any chat, describe the action and the time, e.g. "Every weekday at 8am, …".
  2. Use Sidebar → **Scheduled**.

  Sources: [ai-toolbox, updated 15 Sep 2026](https://www.ai-toolbox.co/chatgpt-management-and-productivity/how-to-use-chatgpt-tasks-schedule-2026), [promptoptimizer, 4 Sep 2026](https://promptoptimizer.tools/blog/chatgpt-scheduled-tasks-free-automations).
- **Active-task limits:** these agree across ai-toolbox, [everydayaitech (27 Aug 2026, citing the OpenAI Help Center and the 25 Aug release notes)](https://www.everydayaitech.com/en/articles/chatgpt-scheduled-tasks-free-2026) and [notis.ai (updated 2 Oct 2026)](https://www.notis.ai/blog/chatgpt-limitations-2026-workarounds/).

  | Plan | Active tasks | Timing | Event triggers (Gmail / Slack / GitHub) |
  |---|---|---|---|
  | Free, Go | 3 | At most once a day, in a **window** (morning / afternoon / night), no exact time | No |
  | Plus | 5 | Exact times, as often as hourly | Yes |
  | Business, Edu | 10 | Hourly | Yes |
  | Pro, Enterprise | 15 | Hourly | Yes |

- **What tasks cannot use** (all plans): voice, file uploads, **Custom GPTs**. **"Tasks created in a project cannot access files uploaded to or stored in that project."** Sources: ai-toolbox, everydayaitech, notis.ai, yellow.com.
- **What tasks can use:**
  - **Web search.** Free users' web search inside tasks counts against their normal chat quota (promptoptimizer, everydayaitech).
  - **Connected apps:** you type **@** in a task to pull in a connected app ([mavgpt, 14 Sep 2026](https://mavgpt.ai/resources/chatgpt-scheduled-tasks-guide-2026)).
  - **Memory** (mavgpt; one source only).
  - **On Free, a task produces a chat message only.** Sending, posting and other actions in apps stay manual (promptoptimizer).
- **Write actions need approval.** By default, apps ask the user to approve "important actions" (notis.ai). Tasks **auto-pause** when they are ignored, when they are waiting for approval of an external action, or when their chat is deleted (everydayaitech, yellow.com).
- **Notifications:** Settings → Notifications → Push, Email or both (ai-toolbox, mavgpt).
- **Sharing (since 25 Aug 2026; Free, Go, Plus and Pro):**
  - A share link carries the title, instructions, schedule and timezone.
  - Recipients review it, connect their own apps and save an independent copy.
  - It does **not** carry chat history, past results, credentials or attached files (everydayaitech, ai-toolbox).
- **Models:** sources only say "eligible ChatGPT models". **UNVERIFIED** which models.

**ChatGPT Pulse:** launched 24–25 Sep 2025 for Pro only and **retired 17 Jun 2026**; its job moved into scheduled tasks. Sources: [justinmckelvey (reviewed through 15 Sep 2026)](https://justinmckelvey.com/blog/chatgpt-pulse), [prowlo, 12 Jul 2026](https://prowlo.com/blog/chatgpt-pulse-shut-down). Do not design around Pulse.

**ChatGPT agent and other changes (single sources, UNVERIFIED):**
- ChatGPT agent launched in July 2025. Wikipedia's [OpenAI Operator article](https://en.wikipedia.org/wiki/OpenAI_Operator) says it was "**removed from ChatGPT in early August 2026** without an advance deprecation notice." I could not confirm this officially.
- Wikipedia's [ChatGPT article](https://en.wikipedia.org/wiki/ChatGPT) says "ChatGPT Work", an agent that makes documents, launched in July 2026.
- The same article says ChatGPT "apps" were **renamed "plugins"** in July 2026, so the UI label may now read "plugins".
- Do **not** build the pack on agent mode or agent-scheduled runs.

**Notion with ChatGPT:** Notion's help center lists ChatGPT as a client of Notion MCP for reading and writing ([notion.com/help/notion-mcp](https://www.notion.com/help/notion-mcp), undated). Whether a *scheduled task* can write to Notion or Google Drive without an approval stall is **UNVERIFIED**.

### B. Claude

**Scheduled tasks (Cowork, now "just Claude")** — [Help Center: Schedule recurring tasks in Claude Cowork, "updated this week" (as of 5 Oct 2026)](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)
- **Plans:** all paid plans (Pro, Max, Team, Enterprise). They work in Cowork and in the "new Claude experience" now rolling out to Pro and Max. The Free plan has **no** scheduled tasks.
- **Create with Claude:** Sidebar **Scheduled → New task → "Create with Claude"**. You describe the task and the cadence, Claude asks multiple-choice clarifying questions, then you review the name, schedule and instructions and click **Schedule**.
- **Set up manually:** Sidebar **Scheduled → New task → "Set up manually"**. You enter a name, the prompt, the **approval mode**, the frequency, and optionally a model and a folder.
- **Frequency:** hourly, daily, weekly, weekdays, or manual (on demand). There is **no monthly preset**.
- **Where tasks run:**
  - The article says: "Scheduled tasks run remotely, so they run on their cadence even when your computer is asleep or the Claude Desktop app is closed."
  - It also says: "**If a scheduled task requires local files or apps, it will only run locally.**"
  - This is a **recent change.** Guides from May–July 2026 say the desktop app must be open and the computer awake, and that missed runs are skipped ([claudeforoperators, verified 5 May 2026](https://www.claudeforoperators.com/workflows/scheduled-tasks/); [playingaws, 9 Jul 2026](https://www.playingaws.com/posts/automate-tasks-with-claude-cowork-and-routines/)). Older tutorials are wrong on this point.
- **Capabilities:** tasks get "the same capabilities as regular Cowork tasks, including connected tools, skills, and installed plugins." You can view upcoming and past runs, edit, pause or resume, delete, and Run now.
- **Not documented:** the maximum number of tasks, completion notifications, and what each approval-mode option does. All three are **UNVERIFIED**.

**Projects** — [Help Center: Organize your tasks with projects in Claude Cowork](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) (updated about 2+ weeks before 5 Oct 2026)
- A project has its own instructions, files/context, memory and **"recurring tasks that are specific to the project."**
- You can **import an existing claude.ai Project**, which brings its files and instructions.
- **Gotcha:** a project created from a local folder stays on that computer and does not sync.

**Timeline** ([Claude release notes](https://support.claude.com/en/articles/12138966-release-notes)):

| Date | Change |
|---|---|
| 25 Feb 2026 | Scheduled tasks introduced in Cowork |
| 9 Apr 2026 | Cowork generally available on macOS and Windows |
| 7 Jul 2026 | Cowork on **web and mobile**, with remote sessions |
| 25 Aug 2026 | Memory works across chat and Cowork in the cloud |
| 16 Sep 2026 | Unified experience: everything Cowork does is available from any conversation; chats, Cowork tasks, projects, connectors and skills carry over |

The [pricing page](https://claude.com/pricing) says "Claude Cowork is now just Claude."
- Creating a scheduled task **from the mobile app** is **UNVERIFIED**.

**Skills** — [Help Center: Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude) ("updated over a week ago")
- Available on Free, Pro, Max, Team and Enterprise. **Code execution must be turned on.**
- Upload path: **Customize → Skills → "+" → Create skill → Upload a skill (ZIP)**.
- Skills are available in Cowork projects and scheduled tasks. The ZIP size limit is not stated.

**Connectors that can write**
- **Google Drive:** search and read Docs, Sheets, Slides, PDFs and Office files; upload files; create folders; "save Claude-generated files directly to your Drive." Live editing of Docs, Sheets and Slides is in **beta**, with separate toggles. Reads extract text only. Source: [Help Center, "updated this week"](https://support.claude.com/en/articles/10166901-using-the-google-drive-integration).
- **Notion MCP:** read and write, including creating and updating database entries, for Claude Desktop and claude.ai ([notion.com/help/notion-mcp](https://www.notion.com/help/notion-mcp); [developers.notion.com/docs/mcp](https://developers.notion.com/docs/mcp)).

**Routines** — [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines), research preview
- Cloud runs on a schedule (hourly minimum), via API, or on GitHub events. Pro and above.
- They are **Claude Code features that require GitHub repositories** and a cloud environment, and they run fully autonomously with no permission prompts. Limit: 100 scheduled runs per hour per account.
- **Not suitable for non-technical coaches.**
- "Local" desktop scheduled tasks need the app open and the computer awake. They do one catch-up run within 7 days ([desktop-scheduled-tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks)).
- **Prompt-design tip from these docs:** a run at exactly the hour can start several minutes late, so schedule for something like 9:07.

**Pricing** ([claude.com/pricing](https://claude.com/pricing)): Pro is $20/month, or $17/month billed annually. Pro includes Projects, Skills, Connectors and scheduled tasks. Max starts at $100/month.

### C. Third-party tools that can glue this together

| Tool | What it does here | Cost (date) | Fit for a non-technical coach |
|---|---|---|---|
| **Notion Custom Agents** ([help](https://www.notion.com/help/custom-agents), [pricing](https://www.notion.com/pricing)) | Triggers: schedules (daily, weekly, **monthly**, yearly), database or page changes, Slack. Can write to databases. Models include Claude, GPT and Gemini | **Business plan $20/member/month** plus credits at **$10 per 1,000**, after a free trial | Good. The hub and the automation live in one place |
| **Zapier** ([pricing, 5 Oct 2026](https://zapier.com/pricing)) | Schedule → AI step → Notion/Sheets. "AI by Zapier" works without your own API key on Pro and above | Free: 100 tasks, two-step Zaps only. Pro from **$19.99/month** (annual) | Good |
| **Make** ([pricing](https://www.make.com/en/pricing)) | Scheduled scenarios with OpenAI or Anthropic modules (your own API key) | Free: 1,000 credits. Core **$12/month**, plus API spend. My rough estimate is cents per run | Medium |
| **n8n** ([pricing](https://n8n.io/pricing/)) | Same idea | Starter **€20/month** (2.5k executions). Self-hosted Community edition is free | Low; too technical |
| **Google Apps Script** ([quotas, updated 3 Sep 2026](https://developers.google.com/apps-script/guides/services/quotas)) | Time-driven trigger → AI API → write to a Sheet | Free. Limits: 90 minutes of trigger runtime per day, 6 minutes per run, 20 triggers, 20k URL fetches per day. Plus API cost | Low; needs pasted code and an API key |

---

## 2) Limitations and gotchas

1. **ChatGPT tasks cannot see Project files or Custom GPTs.** Each ChatGPT task prompt must be **self-contained**, or rely on Memory (one source only) or an @app fetch (UNVERIFIED for Drive and Notion). The "brain" in your pack does not reach scheduled tasks on ChatGPT.
2. **ChatGPT tasks cannot hand off to each other.** Every run is its own chat, so a Sunday research task cannot feed a Monday script task. **Merge dependent steps into a single task.**
3. **Plan caps on ChatGPT:** 5 tasks on Plus and 3 on Free or Go. Free and Go only get loose time windows. Design a **3-task core**.
4. **Writes on ChatGPT stall.** Write actions to apps usually need approval, and a waiting or ignored task **auto-pauses**. Treat ChatGPT as "delivers a draft to your inbox." The human or VA pastes it into the hub.
5. **Claude tasks run in the cloud only when they need nothing local.** If the content hub is a local folder, the task falls back to running locally and stops when the laptop sleeps. **Put the hub in Notion or Google Drive.**
6. **Claude has no monthly preset.** Use weekly with a guard in the prompt ("only run fully if today is in the first 7 days of the month; otherwise reply 'skip'"), or set it to Manual.
7. **Unknown approval behaviour on Claude.** What each approval mode does during an unattended run is undocumented. Click **Run now** once while you are present to see whether it stalls.
8. **Usage limits.** Every run consumes plan usage on both platforms. Long research runs can hit Pro limits.
9. **Out-of-date tutorials.** Many guides from early 2026 say Claude tasks need the desktop app open, which is no longer true. Many also mention Pulse or ChatGPT agent, which are gone or reportedly gone. Date-stamp the pack's instructions and plan to revise them every quarter.
10. **Timing and timezones.** Schedule a few minutes past the hour (7:07, not 7:00). Prompts should state today's date and say "if this runs late, still produce this week's batch."
11. **Vietnamese edition.** Every task prompt must hard-code the output language and the market (VN platforms, đ pricing, local examples). Shared ChatGPT task links keep the creator's timezone; buyers must change it.

---

## 3) Recommendation: the Content Machine automation pack

**Architecture:** one hub, five recurring tasks, three of them core.
- **Hub ("one place"):** a Notion template, with Google Sheets as the alternative. It holds these databases: Brand Brief (one page), Ideas, Series, Scripts (status: Idea → Scripted → Filmed → Posted), Calendar, Stats.
  - On **Claude**, tasks read and write the hub through connectors.
  - On **ChatGPT**, tasks deliver drafts by push or email notification, and the user or VA pastes them into the hub.
- **Brand Brief block:** a ≤600-word compressed brief (audience, offer, pillars, voice, banned words, CTA, language). It is generated during setup and **pasted at the top of every ChatGPT task**. Claude reads it from the Project or Skill instead.

### The tasks

| # | Task | Cadence | Core? |
|---|---|---|---|
| 1 | **Weekly Batch:** research and scripts | Monday 7:07 | CORE |
| 2 | **Friday Review:** performance and next-week adjustments | Friday 16:07 | CORE |
| 3 | **Daily Post Pack:** today's post, captions and one comment prompt | Weekdays 6:37 | CORE |
| 4 | **Monthly Series Planner:** the next 30-day plan and series arcs | 1st of the month (weekly + guard on Claude) | Plus and Claude |
| 5 | **Conversion Check:** offer, ads and email angles from the month's top content | Weekly Wednesday, or monthly | Plus and Claude |

### Prompt outlines (each one is a file in the zip, EN and VI)

1. **Weekly Batch:**
   - "[Brand Brief]. Today is {date}."
   - Search the web for the past 7 days of news, trends and questions in {niche}; pick 3.
   - Check the Series plan for this week. On Claude it reads the hub; on ChatGPT it is pasted into the prompt.
   - Write N scripts using the mix this week calls for (educational / entertaining / converting): hook ×3 variants, body, CTA, and a caption for each.
   - Output as a table: Day | Format | Series | Hook | Script | CTA.
   - Claude only: "Create one page per script in Scripts with status = Scripted."
2. **Friday Review:**
   - Read the Stats table, or ask the user to paste numbers.
   - Name the top and bottom 2 posts and say why.
   - List 3 keep / stop / try changes.
   - Rewrite next week's hook angles.
   - Claude only: write a "Weekly Review" page.
3. **Daily Post Pack:**
   - Pull today's scheduled script.
   - Produce a final caption, an on-screen text line, a 15-second version, and one engagement reply prompt.
   - If nothing is scheduled, write one quick POV or "if you know you know" post from the backlog.
4. **Monthly Series Planner:**
   - Guard: "If today is not in days 1–7 of the month, reply SKIP."
   - Plan a 30-day domino sequence: awareness → trust → offer, 3 series × 4 episodes.
   - Fill the Calendar.
5. **Conversion Check:**
   - Turn the best-performing educational post into 1 editorial-style converting post, 2 ad hooks and 1 email.

### Install on Claude (Pro, $17–20/month)

1. Turn on **code execution**. Then go to **Customize → Skills → + → Create skill → Upload a skill** and upload the Content Machine skill ZIP.
2. Go to **Customize → Connectors** and connect **Notion** (or **Google Drive**). Duplicate the hub template.
3. Create a **Project** called "Content Machine". Import your claude.ai project or start a new one. Add the Brand Brief and the instructions.
4. Inside the project, open **Scheduled → New task → Set up manually**. Paste the Task 1 prompt and set Weekly, Monday, 7:07. Select the model if offered. **Do not select a local folder.**
5. Click **Run now** once while you watch. Approve any connector actions, then check that pages appear in Notion.
6. Repeat steps 4–5 for Tasks 2–5. For Task 4, use Weekly with the guard prompt.
7. **Shortcut:** choose **Create with Claude** and paste: "Set up the 5 Content Machine tasks from the skill's automation-pack file."
8. **Fallbacks:**
   - **Claude Free:** no scheduling. Ship the same 5 prompts as "Run-sheet" cards plus a calendar reminder (an ICS file in the zip), and the user pastes the prompt into the project chat.
   - **Notion Business users:** Notion Custom Agents can run Tasks 1–5 inside Notion.

### Install on ChatGPT (Plus at minimum is recommended)

1. **Settings → Notifications:** set task notifications to **Push + Email**.
2. Optional: in a normal chat, say "Remember this as my Content Machine brand brief: …". Do not rely on this alone, because Memory use in tasks has only one source.
3. **Do not create tasks inside a Project.** They cannot read its files. Open **Sidebar → Scheduled → New**, or a new normal chat, and paste "Every Monday at 7:07am: [Brand Brief] + [Task 1 prompt]". Confirm the schedule and the timezone.
4. Repeat for Tasks 2–3 (Free and Go stop at 3, which use morning-window timing). Plus users add Tasks 4–5 (5 is the maximum). Task 4: set it to monthly if the scheduler accepts that; otherwise use weekly with the guard (UNVERIFIED which recurrences ChatGPT offers).
5. **Founder distribution:** create each task once and publish its **share link** (Aug 2026 feature). The buyer clicks, edits the Brand Brief block and the timezone, and saves a copy. This is the easiest install path, but attached files do not travel with the link.
6. Open each delivered result in the task's chat. Copy it to the hub, or have the VA do it.
7. Do not add write-to-app steps; they cause approval stalls and auto-pause.
8. **Fallbacks:**
   - Feature missing or at the cap: use the Run-sheet cards plus calendar reminders.
   - Hands-off write-back to Notion or Sheets: Zapier Pro (~$20/month; schedule → AI by Zapier → Notion or Sheets) or Make Core ($12/month plus API spend).

**Bottom line:** Claude Pro, with Skill + Project + Notion connector + cloud scheduled tasks, is the only native option that can run the whole loop including the hub. ChatGPT works as a "drafts arrive in your inbox" engine with 3–5 self-contained tasks. The pack should ship the same five prompts in both forms, plus manual Run-sheet cards as the universal fallback.