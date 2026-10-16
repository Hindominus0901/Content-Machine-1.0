# Content Hub Brief for Content Machine 1.0 (researched 2026-10-05)

**Research note:** the session hit its web-search limit (200 calls) partway through. After that I only fetched official pages I could reach directly. OpenAI help pages blocked direct fetching, so I read them through the r.jina.ai reader proxy. Items I could not confirm are marked **[UNVERIFIED]**. Where no page date is given, the date is the day I accessed the page.

---

## 1) Facts (with sources)

### Notion
- **Claude can read and write.** Notion's official connector in Claude was added in November 2025. Its tools include search, fetch, create-pages, update-page, create-database, update-database, move and duplicate pages, and comments. The connection URL is `https://mcp.notion.com/mcp` ([claude.com/marketplace/connectors/notion](https://claude.com/marketplace/connectors/notion)).
  - Notion's own tool list confirms that `notion-create-pages` creates pages "with properties and content" and that `notion-update-page` changes properties, content and templates ([developers.notion.com/docs/mcp-supported-tools](https://developers.notion.com/docs/mcp-supported-tools), accessed 2026-10-05).
  - Further tools: `notion-create-database`, `notion-update-data-source`, `notion-create-view` and `notion-update-view`. The view tool supports table, board, list, calendar, timeline, gallery, form, chart, map and dashboard views. So Claude can build the whole hub, not just add rows to it.
  - **Query limit:** `notion-query-data-sources` is capped at 20 calls per 10 seconds. It is "unlimited on Business and Enterprise plans with Notion AI" (same source).
  - I also checked this session's own Notion connector on 2026-10-05. It exposes these same create, update and view tools.
- **Claude plan requirement:** directory connectors work on every plan (Free, Pro, Max, Team, Enterprise) on web, desktop and mobile. Installing connectors on mobile is beta. Free users are limited to one *custom* connector ([support.claude.com/…/11176164](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities), updated the week of 2026-10-05).
- **Claude scheduled tasks can write to Notion.** Cowork scheduled tasks are available on "all paid plans (Pro, Max, Team, Enterprise)".
  - They run hourly, daily, weekly, on weekdays, or manually.
  - They run remotely "even when your computer is asleep", and they can use "connected tools, skills, and installed plugins".
  - Each task has an "approval mode" setting ([support.claude.com/…/13854387](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)).
  - From 2026-10-06, new Cowork tasks on Pro and Max run in the cloud. Connectors work on desktop, web and mobile ([support.claude.com/…/15520349](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)).
- **ChatGPT access is mixed:**
  - Notion's help page lists "ChatGPT Pro" as a supported client ([notion.com/help/notion-mcp](https://www.notion.com/help/notion-mcp)).
  - OpenAI's Notion help page says ChatGPT "may be able to create or update Notion pages, depending on the app or plugin, your connected account's permissions, workspace settings, and required approvals". Personal sync "is no longer available" ([help.openai.com/…/12532955](https://help.openai.com/en/articles/12532955-notion-app-and-setup-in-chatgpt), undated).
  - The ChatGPT **Business** release notes (March 2026) say updated Box, Notion, Linear and Dropbox apps "add new app actions", including write ([help.openai.com/…/11391654](https://help.openai.com/en/articles/11391654-chatgpt-business-release-notes)). The page rendered without years in places, so the year is taken from a search snippet that said "March 2026".
  - OpenAI's developer-mode page says full MCP support with write actions is for "Business, Enterprise, and Edu" only. It says "Pro users can connect MCPs with read/fetch permissions" and "OpenAI-built apps are search-only today" ([help.openai.com/…/12584461](https://help.openai.com/en/articles/12584461-developer-mode-apps-and-full-mcp-connectors-in-chatgpt-beta)).
  - A third-party review dated 2026-07-09 claims ChatGPT can read and write Notion through MCP, with "Pro offers the most" ([usecarly.com/blog/chatgpt-notion-integration](https://www.usecarly.com/blog/chatgpt-notion-integration/)).
  - **[UNVERIFIED]** Whether ChatGPT **Plus** can reliably create or update Notion database rows.
- **Cost** ([notion.com/pricing](https://www.notion.com/pricing)):
  - Free: unlimited blocks for one person but "limited for 2+ members", 10 guests, 5 MB uploads, 7-day page history.
  - Plus: $10 per seat per month. Business: $20 per seat per month. The page says "save up to 20% with yearly". **[UNVERIFIED]** whether these are the annual or monthly prices.
  - Business includes Notion Agent. Custom Agents need Business or Enterprise. They run on schedules (daily, weekly…) or on database events, and can update records. They cost "$10 per 1,000 monthly Notion credits" after a free trial ([notion.com/help/custom-agents](https://www.notion.com/help/custom-agents)).
- **Import:** Notion imports CSV, Markdown, .txt, .docx, HTML, PDF and ZIP. In a CSV, "Rows import as pages. Columns import as properties." Data can be added to an existing database with "Merge with CSV". However, "Imports add rows. They don't update existing rows." Relations, rollups and formulas are not created on import. Size limit is 5 MB per file on Free and 50 MB on paid plans ([notion.com/help/import-data-into-notion](https://www.notion.com/help/import-data-into-notion)).
- **Sharing a template:** a published Notion Site can turn on "Duplicate as template" so visitors copy it into their own workspace ([notion.com/help/public-pages-and-web-publishing](https://www.notion.com/help/public-pages-and-web-publishing)).
- **Vietnam:** Notion has a full Vietnamese-language site ([notion.com/vi-vn](https://www.notion.com/vi-vn)). **[UNVERIFIED]** whether the app interface itself is in Vietnamese, and how popular Notion is in Vietnam. Claude.ai is supported in Vietnam ([anthropic.com/supported-countries](https://www.anthropic.com/supported-countries)).

### Google Sheets / Drive
- **Claude:**
  - The Drive connector searches, reads, uploads and saves files, and can share, move or trash them.
  - Separate Docs, Sheets and Slides connectors can "Create new … files" and "Edit files live in a pane beside the chat (beta)". This live editing needs Chrome on the web or Claude Desktop. Known issue: "edits may not display live in the pane" ([support.claude.com/…/10166901](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors), updated the week of 2026-10-05).
  - The Claude add-on that runs inside Google Sheets needs Pro, Max, Team or Enterprise and is beta. It "works only on the file it's opened in", and "Mobile/Scheduled tasks: Not supported" ([support.claude.com/…/16951679](https://support.claude.com/en/articles/16951679-use-claude-in-google-docs-sheets-and-slides)).
  - Earlier in 2026 the Drive connector worked on whole files only. It could not append rows or edit single cells (GitHub issue [#95178](https://github.com/anthropics/claude-code/issues/95178), opened 2026-09-17). A review dated 2026-08-14 said "There is no Sheets app in Anthropic's directory" ([usecarly](https://www.usecarly.com/blog/can-claude-edit-google-sheets/)). The live Sheets editing is therefore only weeks old.
  - **[UNVERIFIED]** Whether the new Sheets connector works in scheduled tasks or on mobile.
- **ChatGPT:**
  - The Google Drive app supports "Actions that change a file, such as creating, updating, moving, sharing, or deleting it". Availability "depends on your ChatGPT plan, location, workspace settings" ([help.openai.com/…/10929079](https://help.openai.com/en/articles/10929079-google-drive-app-and-setup-in-chatgpt)).
  - The Business release notes record "Write actions for Microsoft and Google apps" on March 13 (2026, year inferred).
  - The ChatGPT add-on inside Sheets edits cells in place, after asking for permission. It is available on Free, Go, Plus and Pro, and in Business, Enterprise and Edu. Launch dates conflict: 2026-04-22 per a [usecarly review dated 2026-07-09](https://www.usecarly.com/blog/chatgpt-google-sheets-integration/), and 2026-05-05 "globally" per the [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes). It only works on the sheet you have open and does not run on its own.

### Airtable
- The Claude connector was built by Airtable and added in February 2026. It has 12 tools, including create and update records, create tables and fields, and read table schemas ([claude.com/marketplace/connectors/airtable](https://claude.com/marketplace/connectors/airtable)).
- Airtable's MCP server works on "all plans" and with Claude and ChatGPT. It creates at most 10 records per request and is subject to API rate limits ([support.airtable.com](https://support.airtable.com/docs/using-the-airtable-mcp-server)).
- Free plan: 1,000 records per base, **1,000 API calls per month**, up to 5 editors. Team: $20 per seat per month billed annually, $24 monthly ([airtable.com/pricing](https://airtable.com/pricing)).
- **[UNVERIFIED]** Whether MCP calls count against the 1,000-call monthly limit, and which ChatGPT plans can write to Airtable.

### ClickUp
- The Claude connector was added in January 2026 and has 35 tools for tasks, docs, lists and time tracking ([claude.com/marketplace/connectors/clickup](https://claude.com/marketplace/connectors/clickup)).
- The MCP server is in public beta and has no delete tools. **Free Forever is limited to 50 MCP calls per 24 hours**; Unlimited and above get 300 ([developer.clickup.com](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server)).
- Free plan storage is 60 MB ([clickup.com/pricing](https://clickup.com/pricing)).

### Trello
- The Claude connector was built by Atlassian and added in July 2026. It can read and write boards, lists, cards and checklists ([claude.com/marketplace/connectors/trello](https://claude.com/marketplace/connectors/trello)).
- Free plan: 10 boards and 10 collaborators per workspace. Calendar, Table and Dashboard views are paid only. Standard costs $5 per user per month annually, $6 monthly ([trello.com/pricing](https://trello.com/pricing)).
- **[UNVERIFIED]** Whether ChatGPT can write to Trello.

### No external tool (Projects, artifacts, canvas)
- **Claude Projects:** available on all plans; Free users get up to 5 projects. Only Team and Enterprise can share projects ([support.claude.com/…/9517075](https://support.claude.com/en/articles/9517075-what-are-projects)). **[UNVERIFIED]** Whether Claude can edit project knowledge files from a chat (the documentation does not say).
- **ChatGPT Projects:** 5 files on Free, 25 on Go and Plus, 40 on Pro and Business. Project sharing works on every plan, including Free, on web and mobile ([help.openai.com/…/10169521](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)).
- **ChatGPT scheduled tasks:**
  - Limits: 3 on Free and Go, 5 on Plus, 10 on Business, 15 on Pro and Enterprise.
  - **"If you create a task in a project, it cannot access uploaded files or files stored in that project."**
  - Named app support covers only "Gmail, Slack, and GitHub" ([help.openai.com/…/10291617](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt)).
  - ChatGPT Work (launched 2026-07-09 for paid plans except Free and Go) "work[s] across connected apps" ([release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)).
- **[UNVERIFIED]** I have no evidence that Claude artifacts or ChatGPT canvas can serve as a structured hub that AI can write to. Canvas belongs to a single chat.

### Creator "Content OS" templates
- Notion's Content Calendar category lists 1,006 templates ([notion.com/templates/category/content-calendar](https://www.notion.com/templates/category/content-calendar)).
- Notion's free "Content calendar" template has publish date, owner, content type, platform and status properties. It offers a Calendar view and a Board grouped by status, and is rated 4.85 ([notion.com/templates/content-calendar](https://www.notion.com/templates/content-calendar)).
- **Thomas Frank's Creator's Companion** costs $99–$228 ([product page](https://thomasjfrank.com/creators-companion/)).
  - **Databases:** Content, Channels, Sponsors, Keywords, B-Roll, Research, Swipes, Wiki, Audience Submissions, Tasks and Projects.
  - **Ideas live inside the Content database** as Status = "Idea" rather than in a separate database.
  - **Views:** "Writer's Room", "Film Queue", "Edit Bay" (with an Edit Stage status) ([docs](https://thomasjfrank.com/docs/creators-companion/)).
  - **Content properties** include Status, Publish Date, Review Date, Idea Merit, Media Type, Channel, Editor, Writer, Research (relation), Repurposing (relation), Views, Likes, Comments, Stats (formula), Performance Notes, URL and Files. It has six page templates: Video, Podcast, Stream, Blog, Newsletter and Classic ([Content DB docs](https://thomasjfrank.com/docs/creators-companion/databases/content/)).

### Comparison summary
| Hub | Claude write | ChatGPT write | AI writes on a schedule | Ease for coach | VA collaboration | Mobile | Cost (solo + VA) |
|---|---|---|---|---|---|---|---|
| **Notion** | Yes, rows, properties and views (all plans) | Business: yes. Pro: unclear. Plus: [UNVERIFIED] | Claude Pro+ Cowork: yes. Notion Custom Agents: Business | High; templates can be duplicated | Guests (10 free) | Yes | $0–$10 |
| Google Sheets | New files, plus live edit (beta) | Sheets add-on (all plans); Drive app writes (plan-dependent) | Claude add-on: no. Connector: [UNVERIFIED] | Highest familiarity | Excellent | Yes | $0 |
| Airtable | Yes (connector) | MCP; plan [UNVERIFIED] | Claude: yes, but Free has 1,000 API calls a month | Medium | Good | Yes | $0 / $20–24 |
| ClickUp | Yes, 35 tools | Synced connector (Business) | 50 MCP calls a day on Free | Low (complex) | Good | Yes | $0+ |
| Trello | Yes (Jul 2026) | [UNVERIFIED] | Yes via Claude | High, but board only | Good | Yes | $0 / $5 |
| Projects only | Can't update its own files [UNVERIFIED] | No | ChatGPT tasks can't read project files | Highest | Sharing on ChatGPT only | Yes | $0 |

---

## 2) Limitations and gotchas
1. **ChatGPT writes to Notion depend on the plan.** Writes are confirmed only for Business, Enterprise and Edu. For Plus and Pro, OpenAI's own pages contradict each other ("search-only" vs "may create or update"). The pack needs a fallback for ChatGPT users that doesn't depend on write access.
2. **ChatGPT scheduled tasks are weak for this use.** A task made inside a Project can't read that project's files, and Notion isn't listed among the apps tasks can use. So "every Monday write scripts" in ChatGPT has to carry the brand profile inside the task prompt, and its output lands in chat rather than in the hub.
3. **Claude's Google Sheets editing is new and in beta.** It needs Chrome or Desktop, the add-on doesn't run in scheduled tasks or on mobile, and before about September 2026 the Drive connector could only write whole files. It isn't yet reliable as the base for automation.
4. **Notion limits:**
   - Imports only add rows and never update them, so re-importing creates duplicates.
   - Relations and formulas have to be built in the template beforehand.
   - Free plan uploads are capped at 5 MB, so videos belong in Google Drive and the hub links to them.
   - "Limited for 2+ members": add the VA as a **guest**, not a member. **[UNVERIFIED]** that guests don't trigger the block limit.
   - The query tool is rate-limited below the Business plan.
   - MCP tools act with the user's full Notion permissions, so grant access to the Content Machine page only.
   - Notion MCP needs a one-time OAuth sign-in in a browser. "Non-interactive authorization" is not yet supported.
5. **Approval prompts.** Approval modes in Cowork, and "Actions that require approval may pause the task" in ChatGPT, can stall unattended runs. Set approval for the hub's write actions deliberately.
6. **Airtable and ClickUp free plans** (1,000 API calls a month and 50 MCP calls a day respectively) can be used up by weekly automations. **[UNVERIFIED]** whether MCP calls count toward Airtable's limit.
7. **Prompt injection.** Copying competitor posts or comments into a Research Bank lets that untrusted text reach the AI ([aitoolsreview, 2026-06-07](https://aitoolsreview.co.uk/insights/notion-claude-connector)). The skills should treat research text as data, not as instructions.
8. **Products changed fast in 2026.** Several facts are only weeks old (the Sheets connector, Cowork moving to the cloud on 2026-10-06, the Plugin Directory replacing the App Directory on 2026-07-09). Re-check them at launch.

---

## 3) Recommendation for Content Machine

**Architecture: a "brain" plus a "board".**
- **Brain:** a Claude or ChatGPT Project holding the pack's skills and instruction files, plus the brand profile.
- **Board:** one Notion template, which is the single place for every idea, series, script, the calendar, status and stats.
- **Primary path: Claude Pro with Notion.** It is fully automated and Claude writes directly into Notion.
- **ChatGPT path:**
  - **Business:** Notion app write actions, enabled by the workspace admin.
  - **Plus or Pro:** a semi-manual "CSV bridge". ChatGPT outputs a CSV with exact column headers and the user runs Notion's "Merge with CSV". New rows import this way; status changes are done by hand.
- **Fallback for coaches who refuse Notion:** a Google Sheets edition with the same columns. ChatGPT users edit it with the ChatGPT add-on inside Sheets; Claude users with live editing (beta). It has no scheduled writes.

### Notion schema ("Content Machine" page)
1. **Brand Brain** is a page, not a database. Sub-pages: Offer and price ladder, Ideal client (pains, desires, objections, their own words), Voice and banned words, Proof bank (results, testimonials, stories), Content pillars, CTA library, and a page in each language (EN and VI).
2. **Content** is the single core database, following Thomas Frank's ideas-inside-content pattern. Properties:
   - **Pipeline:** Title; **Status** (status type: To-do = *Idea*; In progress = *Scripted, Filmed, Edited*; Complete = *Posted, Reviewed*); Archive (checkbox)
   - **Planning:** Job (select: Educate / Entertain-Relate / Convert); Format (Short video, Carousel, Text post, Long video, Podcast, Ad, Email); Platform (multi-select); Series (relation) + Episode # (number); Awareness stage (Unaware → Most aware); Idea Score (1–5); Language (EN or VI)
   - **Script:** Hook (text); CTA (select: Follow / Comment keyword / DM / Lead magnet / Book call / Buy); script in the page body using database templates (Short-form, Carousel, Long-form, Ad, Email)
   - **Production:** Publish Date (date); Owner/Editor (person); Research (relation); Repurposed From (self-relation); Raw/Asset Link (URL to Drive); Post URL
   - **Stats:** Views, Likes, Comments, Shares, Saves, Follows, Leads/DMs, Sales (all numbers); Engagement % (formula); Review Date; Lesson (text); Last AI Run (date)
3. **Series ("Dominoes"):** Name; Goal (Awareness / Trust / Convert); Belief to install; Linked offer; Planned episodes (number); Status (Planning / Active / Done); Start date; Content (relation) with a rollup of posted count.
4. **Research Bank:** Title; Type (Audience quote / Competitor post / Stat / Trend / Comment / Story); Pain-Desire tag; Source URL; Platform; Language; Captured date; Used In (relation → Content).
5. **Weekly Reviews:** Week of (date); Top posts (relation); Wins; Lessons; Next week's bets; Totals (rollups).

**Views on Content:**
- Idea Bank (table, Status = Idea, sorted by Score)
- Pipeline (board by Status)
- 30-Day Calendar (calendar by Publish Date)
- This Week (table, Publish Date this week)
- Writer's Room (Idea with a date set)
- Film Queue (Scripted)
- Edit Bay (Filmed, filtered to the editor)
- Needs Stats (Posted and more than 7 days old)
- Scoreboard (Reviewed, sorted by Leads and Views)
- Optional Chart view

**Views on Series:** board by Status and a timeline.

### Setup steps for a non-technical coach (about 20 minutes)
1. Create a free Notion account at notion.com. The site is available in Vietnamese at /vi-vn.
2. Open the Content Machine template link and click **Duplicate**. It lands in your workspace.
3. In Claude (Pro plan), go to **Customize → Connectors → Notion → Connect**. Sign in and give access **only** to the "Content Machine" page.
4. In Claude, create a Project called "Content Machine". Upload the pack's files or install its Skills, and paste the Notion page link into the project instructions.
5. Run the **Setup** prompt. Claude interviews you, writes the Brand Brain page, creates 3–4 Series, and adds 30 ideas and the 30-day calendar to Content. It then writes full scripts for Week 1 inside each page and sets those items to Status = Scripted.
6. Automate it in Claude: **Cowork → Scheduled task**.
   - "Mondays 7:00: write scripts for this week's Content items, then set them to Scripted."
   - "Sundays 18:00: read Posted items that have stats, create a Weekly Review page, mark the items Reviewed, and add 5 new ideas."
   - Set approval mode so Notion writes don't stall the task.
7. Invite your VA or editor as a **guest** on the Content Machine page with *Can edit*. They work from Film Queue and Edit Bay and fill in the stats after 7 days.
8. Use the Notion phone app to film from the Film Queue view. The Claude app on your phone has the same connector.
9. **ChatGPT users:**
   - **Business plan:** connect the Notion app under Settings → Apps and ask your admin to enable its write actions.
   - **Plus or Pro plan:** say "export this week as CSV" in ChatGPT, then in Notion choose Content database **••• → Merge with CSV**. You can also use a ChatGPT scheduled task to receive Monday's scripts in chat. Paste the Brand Brain into the task itself, because tasks can't read project files.