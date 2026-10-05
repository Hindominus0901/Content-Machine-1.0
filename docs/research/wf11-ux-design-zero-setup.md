# Content Machine 1.0: coach experience design (EN + VN, ChatGPT + Claude)

**Core idea:** keep Day 0 to 3 actions. The coach starts by talking and adds everything else later, at the moment it's needed, with the machine guiding them.
- **One text** (the START block) works in two ways: pasted as Project instructions on a computer, or pasted as the first message of a normal chat on a phone.
- After that the coach only talks, by voice.
- The machine decides, writes and saves. The coach saves one Brand Card using the app's own button, makes one decision per session, and gets one NEXT line per reply.
- The method file, reminders, Notion/Sheets and the Claude skill each arrive later, guided by the machine, only when a job needs them.

---

## 1. Install

### 1.1 Two doors. The setup page picks one by device; the coach never chooses

There is one unlisted setup page per edition, linked from the purchase email. It has app tabs: the VN page opens on ChatGPT, with "Dùng Claude? Bấm đây" as a small link.

| | **Door A: computer (default)** | **Door B: phone (or a stuck computer user)** |
|---|---|---|
| Actions | 3 | 3 |
| Time | about 2 min | about 30–60 s |
| ChatGPT (Free, Go, Plus, Pro) at chatgpt.com in a browser. The Mac app can't create projects | 1. Sidebar → Projects → New project → "Content Machine" → Create (keep Default memory)<br>2. Instructions → paste START (setup-page **Copy** button) → Save<br>3. New chat in the project → "Start" / "Bắt đầu" | 1. Tap **Copy** on the setup page<br>2. Open ChatGPT → new chat → paste<br>3. Send |
| Claude (Free, Pro, Max) on web or desktop | 1. Projects → + New project → "Content Machine"<br>2. Set project instructions → paste START → Save<br>3. Chat in the project → "Start" / "Bắt đầu" | Same 3 steps in the Claude app |
| What persists | Instructions; Brand Card saved as a project source at about minute 27 | The chat itself, plus a 3-line essence saved to memory. "Make it permanent" is queued for later |

**Deliberately not on Day 0:** the method file, the skill zip, Notion, any connector, any task, notification settings, the Sheet, and the code-execution toggle (it is on by default now).

### 1.2 Differences by plan the coach never has to think about

| Plan | Constraint | How the design absorbs it |
|---|---|---|
| ChatGPT Free | 5 files per project; about 3 uploads a day; about 27K instant context | The kit uses at most 3 sources over its whole life (method, Brand Card, optional LAUNCH file). Day 0 uses 1–2 uploads. Session-1 replies stay short until the Map. The Brand Card is printed before anything long |
| Claude Free | 5 projects; roughly 15–40 messages per 5 h; all knowledge loads into every message | Session 1 is about 10–12 coach turns. The method file is capped at 60 KB or less. If the coach keeps hitting the cap, the machine offers the "lighter" swap (skill instead of method file, §4). The machine keeps save points: "if you hit a limit, come back and say 'next'" |
| Claude Pro/Max | Same Day 0 | Autopilot is offered in Weeks 2–3 (§4) |
| VN | Claude's own mic doesn't support Vietnamese | ChatGPT is the default. Claude VN users are told to use the keyboard mic (Gboard / iOS). The machine detects garbled text and repeats the tip |

### 1.3 "Make it permanent" (Door B users only; guided in chat when they say they're at a computer)

1. Create the project and paste START into its instructions (2 actions).
2. ChatGPT: open the old chat → ⋯ → Move to project → Content Machine, then on the Brand Card message → ⋯ → Save to project. Claude: copy the Brand Card → project knowledge + → Add text content → paste. ([UNVERIFIED] whether Claude can move a chat into a project.)
3. Add the method file (same as §2, minute 29).

About 3–4 min. The machine walks through one step per message with "done?" checkpoints and links the 60-second video.

### 1.4 What the founder pre-builds

| Item | Spec |
|---|---|
| Setup page × 2 (EN, VN) | Device-aware; app tabs; Copy START; Download method (served with `Content-Disposition: attachment`, so Safari doesn't open the .md as text); "Copy method text" alternative; four 60–90 s captioned screen recordings (EN/VN × ChatGPT/Claude); 8-item troubleshooting; ASCII file names |
| **START block** × 2 | ≤7,500 characters after NFC (lint), app-specific lines inside. §0: if pasted as a user message, begin now; every reply starts `◆ Content Machine · Week n/4` and ends with one `NEXT →`. §1: state detection (Brand Card, highest version wins; method present?). §2: the compact Message Focus Engine, with only the key VN strings verbatim (dump prompt, inventory line, Map labels, the one decision). §3: phrase router. §4: compact Ship Check + FOCUS + coach footer. §5: save rules per app plus the memory essence. §6: non-negotiables repeated at the bottom |
| **Method file** × 2 (`CONTENT-MACHINE-EN.md`, `-VN.md`) | **One** file of 60 KB or less with `§CM-` anchors: WEEK (Monday interview), CUT, TODAY, NUMBERS, MONTH, FORMATS, CTA KIT, RESEARCH-lite, EDGE, GUARDRAILS, LOCALE. VN method prose stays English behind the output contract |
| Power-ups, later | `LAUNCH` file × 2; Claude skill zip × 2; Notion template × 2; Sheets Lite × 2; Google Calendar template links + `.ics` (Mon and Fri reminders) × 2 |
| Generated in session, never pre-built | Brand Card, keyword asset, DM lines, task texts (the coach's own time zone, so no founder share links), paste rows, the Claude task sentence |

### 1.5 What fails, and the in-chat fix

| Failure | How it shows | Fix |
|---|---|---|
| Chatting outside the project | No `◆ Content Machine` tag; generic answers | Setup page: "If a reply doesn't start with ◆, open Content Machine." ChatGPT: at the end of session 1 the machine saves a memory, "remind me to open my Content Machine project when I ask for content outside it" [UNVERIFIED: saving global memory from inside a project]. NEXT lines always say "in Content Machine" |
| START pasted into global Custom Instructions (1,500-character cap) | Truncated; no tag | Video shows the box *inside the project*. The phone door is the fallback |
| Tried to create the project on a phone or in the ChatGPT Mac app | Can't find "New project" | Setup page Door A says "computer browser". In chat: "Projects are made on a computer. Let's keep going here; we'll make it permanent later" |
| Method file missing | Machine can't find `§CM-` | "To write your Week 1, add my method file (30 s): Add files → CONTENT-MACHINE.md" / "Để viết tuần 1, bạn thêm file phương pháp (30 giây)…" |
| Method attached to a chat, not the project | Present in the chat but absent from sources | "I see it here, but not in the project. Add it there so I have it next time." |
| Two Brand Cards (forgot to delete the old one) | Two versions found | Use the highest version, then: "Delete Brand Card v1 in Sources (it's older)." |
| VN voice garbled in Claude | Nonsense words | "Claude's mic doesn't do Vietnamese. Use the 🎤 on your phone keyboard." |
| Free usage cap mid-interview | The app blocks | Pre-announced save point; the machine resumes from the last open "?" |
| Long chat drifts | — | Rule: **new week = new chat**. Friday's NEXT says so |
| Account shared (common in VN) | Foreign memories leak in | Brand Card in Sources is the source of truth. Tip: switch the project to Project-only memory |

---

## 2. First session, minute by minute (about 30–40 min; the coach is active about 25)

| Min | Coach does | Machine does or gives |
|---|---|---|
| 0 | "Start" / "Bắt đầu" (Door A), or sends START (Door B) | Tag + 3-line promise (engine §5.1) + **brain-dump prompt** (engine §1.2, EN/VN verbatim) + "tap the **mic in the message box** (dictation, not the voice-mode wave). Talk 2–3 min, send, repeat." |
| 1–11 | Talks in 2–3 chunks (or pastes a livestream transcript or the last 10 posts) | After each chunk: "Got it. Keep going or say 'done'. You haven't mentioned {jogger}." Silently extracts inventory, candidates, stories, client words, voice and xưng hô |
| 11–12 | — | **Inventory** ("You know a lot… about 6 months of content… nothing thrown away") + **pre-filled check** (6 numbered lines, 2–3 marked "?") |
| 12–17 | "yes / fix 3: …" + 2–3 live answers (their exact words; best result with a number) | At most 1 probe each. Quick Listen runs silently if browsing is available (≤5 searches) |
| 17–19 | — | **Message Map** (one screen) + pocket version (3 lines) + one "why this one" line. Coach-facing label: **"3 BIG IDEAS / 3 Ý LỚN"**, not "pillars" (see §6) |
| **19–20** | **The ONE decision: "OK", or "change line N"** | Locks the Map for 90 days (at most 1 rewrite) |
| 20–24 | — | **FILM TODAY:** a 20–40 s Big-idea-1 short in Mode B (verbatim title, verbal and visual hooks, 3 beats, final line). Caption in a copy box; keyword CTA; WHY line. "Not filming today? Post the caption as a text post." NEXT → "Film it now (10 min) or after we finish." |
| 24–26 | Confirms one defaults line: main platform (+ Zalo/email), hours a week, interview/filming day, bullets or word-for-word, xưng hô (VN) | — |
| 26–29 | **Save (1 tap on ChatGPT):** ⋯ under the Brand Card → Save to project. **Claude:** Copy → knowledge + → Add text content → paste. Door B: nothing | **BRAND CARD v1** in a copy box (≤4,500 characters EN / 5,000 VN): MAP · VOICE · MATERIAL (stories, results with consent flags, client words, stances) · PLAN (start date, days, platform, tier, mode) · CTA KIT (keyword + no-diacritic variants, DM-ready asset of ≤900 characters, M1/M2) · NOT NOW (names) · PROGRESS. Door B: saves the 3-line essence to memory and queues "make it permanent" |
| 29–30 | Adds the method file (1 upload, or paste as a text source) | Verifies it can see it |
| 30–38 | "next" | **Season 1 in 4 lines** (W1–W3 = Big ideas 1–3, W4 = all + offer). **Week 1 cut from the dump** (pillar #0), across 2 replies: 3 shorts, 1 long post (FB "chia sẻ" / LinkedIn), 1 email or Zalo message, the keyword asset and its DM lines. Anything to paste goes in a copy box; anything to say on camera is plain text |
| 38–40 | — | Wrap-up and one NEXT: "Film today's short. Tomorrow: say 'next'." / "Quay video hôm nay. Mai gõ 'tiếp'." Reminders and the board are **not** offered yet |

That is about 10–12 coach turns. The Map arrives within 8 turns.

**What the coach walks away with:**
1. One sentence they can say (pocket Map; "screenshot this").
2. A short they can film today, plus a post-as-text fallback.
3. Their keyword, with an asset that fits in one DM and the reply lines.
4. A 4-week plan in 4 lines.
5. Week 1 written in their own words.
6. A saved Brand Card.
7. One word to remember: **next / tiếp**.

---

## 3. Week 1 and the weekly loop

### 3.1 Week 1 (raw material = the session-1 dump)

| Day | Coach | Minutes | Machine | Copy/paste where |
|---|---|---|---|---|
| 0 | Session 1 + film and post the short | 35 + 10 + 3 | Map, short, Brand Card, Week 1 | Caption → the platform |
| 1 (filming day) | "next" → films the 3 remaining shorts back to back | 20–25 | Re-prints today's filming list in delivery mode | — |
| 2–6 | "next" each morning → post today's piece; answer keyword comments | 3–5 a day | Today's single piece re-printed in a copy box; M1 DM reply | Caption → TikTok, Reels or FB. Long post → FB profile. Email/Zalo text → email tool, Zalo group or Nhật ký. M1 → inbox (VA or a Pancake/ManyChat reply set once). The asset is saved once in phone Notes / **Zalo "Cloud của tôi"** |
| Optional | Buyer Mirror message to 3–5 clients | ≤10 | Writes the message | → Zalo / DM |
| 5 (Fri) | "my numbers": says or types 4 things (keyword comments, DMs, calls/sales, best post) or sends ≤3 screenshots (Free upload cap) | 3 | Plain scoreboard (example below). **Then the first upgrade offer: reminders (§4)** | — |

Example scoreboard:
```
◆ Content Machine · Week 1/4
POSTED 5/6 ✓ · BUYERS 9 "EXIT" comments · 2 DMs · 1 call
BEST "Not burnout. A dead end." (2.1× your usual)
NEXT WEEK Big idea 2 "Test before you jump" · Monday: 10-min interview
3 BETS part 2 of the best one · 1 Maria story (if she says yes) · same hook style
NEXT → Monday: open Content Machine, NEW chat, say "next".
```

### 3.2 The weekly loop from Week 2 (Lean, about 65 min a week)

**Recommended change, which needs founder sign-off:** in Season 1 the weekly "pillar" is a **10-minute voice interview in the chat**, not a filmed 20–40 min recording.
- The chat is the transcript, so the coach needs no transcript tool and no editing.
- It is the same habit as Day 0: talk, then film the short takes, then post.
- The filmed video pillar becomes opt-in (Standard/VA tier, or Season 2+).
- In video mode, clip cutting defaults to **"re-film, don't edit"**: the machine turns the best moments into 30–60 s scripts that are at least 70% the coach's own words. PASSAGE cuts are kept for coaches with an editor.

| When | Coach | Minutes | Arrives automatically (once reminders are on) | Machine output |
|---|---|---|---|---|
| Mon | New chat → "next" → answers all 5 questions in one or two dictations | 15–20 | Push: "Big idea 2 this week. Open Content Machine → 'next'" | The week (≥60% on this week's big idea): 3 shorts, 1 long post, 1 email/Zalo message (Standard: + 1 character/relatable short + carousel). Each has a WHY line and a post day |
| Tue | Films the shorts back to back (reading from the screen) | 20–25 | — | — |
| Daily | "next" → copy → post; reply to the keyword | 3–5 | Push: "Today's one thing: open → 'next'" | Today's piece + 1 optional capture question ("what did a client say?"). **No new ideas**: daily ideas would work against focus |
| Anytime | "save this: …" | 0.5 | — | One-line verdict: "On your map (Big idea 3)" or "Parked: different buyer" |
| Fri | "my numbers" | 3–5 | Push: "Numbers day" | Scoreboard + 3 bets |
| Video mode (opt-in) | Records the guide (20–40 min), then "here's my recording" + transcript or file | +40 | — | Long-form post + re-film scripts, or PASSAGE cuts |
| Last week of the Season | "next" | 20 | — | Message check (KEEP is the default), new Season, **Brand Card v+1 → Save to project, delete the old one**. This is the only regular upkeep: 2 taps a month |

On ChatGPT, the week of the Season comes from the Brand Card's start date by simple date arithmetic. The machine asks at most one status question.

---

## 4. Hub and automations: when, who, how many steps, and why they stay optional

| Upgrade | Offered when | Who | Steps and time | What it adds |
|---|---|---|---|---|
| **Reminders, ChatGPT (the founder's 3 automations, reframed)** | End of Week 1's Friday review: "Want me to nudge you Monday, weekdays and Friday? Say 'yes'." | The coach says "yes"; the model creates 3 tasks [UNVERIFIED: whether the model can create tasks from a project chat]. Fallback: copy box → new chat → paste → send | 1 action, or 2 with the fallback; + Settings → Notifications → Tasks: Push (2 taps, guided). Free: 3 slots, morning/afternoon windows | **Mon "Your week"**, **weekdays "Today's one thing"**, **Fri "Numbers day"**. Each task holds only the pocket Map + Season dates and sends the coach back into the project, where the method and Brand Card produce full-quality output. No Brand Brief drift and no prompt-length risk. Plus option: full Monday drafts inside the task |
| **Reminders, Claude Free** | Same moment | Coach | 1 tap on a calendar link (Google template link or iPhone `.ics`) | Mon and Fri: "Open Claude → Content Machine → 'next'" |
| **Autopilot, Claude Pro/Max** | Weeks 2–3, if the coach confirms they're on Pro | Coach, guided one step per message | Skill (download in Chrome → Customize → Skills → + → Upload → on, 2 min) + Notion (Duplicate the template 2 min; Connectors → Notion → share only that page, 2 min) + Scheduled → New task → Create with Claude → paste one sentence → Schedule → Run now (3 min). **About 10–12 min, one sitting** | BATCH and REVIEW really run unattended and write to Notion "This Week". The coach films from the Notion phone app |
| **Board: Notion (default) / Sheets Lite** | Only on a trigger: a VA or editor joins; Autopilot; the coach asks "where is everything?"; or 3+ weeks posted and they want a calendar | Coach or VA | Notion: Duplicate (2 min); ChatGPT users or their VA paste rows each Friday (about 10 min a week). Sheets: Make a copy (1 tap) + paste rows | A calendar, VA handoff and stats history. **Suggestion for VN:** Sheets Lite as the default for ChatGPT + VA setups |
| **LAUNCH file** | "plan a launch", or Season 3+ | Coach | Add 1 file (30 s) | Launch module |
| **"Lighter" swap, Claude** | When the coach keeps hitting usage caps | Coach | Install the skill, then remove the method source (3 min) | Much less loaded per message |

**Why these stay optional:**
- Every job is a phrase, so the method never depends on a schedule.
- The project plus the Brand Card is the memory; project chats are the library.
- ChatGPT tasks can't read project files, and Claude Free has no scheduling. Making automation a Day-0 requirement would bring back the complexity the founder wants removed.

---

## 5. The phrases the coach ever needs (EN / VN)

1. **"next" / "tiếp"**: the only must-know. It starts, resumes setup, gives today's piece, catches up a missed step and runs the monthly plan.
2. **"save this: …" / "lưu lại: …"**: a story, a client's words, a result or an idea. The machine files it and says whether it's on the Map or parked.
3. **"write this: …" / "viết giúp mình: …"**: any one-off piece. The machine bridges it to the Map.
4. **"my numbers" / "số liệu tuần này"**: Friday, by voice or up to 3 screenshots.
5. **"here's my recording" / "đây là bản ghi"**: video mode only.

"Start" / "Bắt đầu" is used once. No "Content Machine:" prefix is needed inside the project. NEXT lines teach each phrase at the moment it's needed. Plain language always works too.

---

## 6. What the coach never sees vs what they see

| Never sees (internal) | Sees (plain words) |
|---|---|
| Focus Scores, criteria, candidate tables, Q1–Q6 labels, the root-cause chain | The inventory line, the pre-filled check, the "why this one" line |
| B1–B7, Big Domino, rungs (Admirable…Trustable), SPCL, domino and series jargon | The Message Map, the pocket version, the 4-line Season, "Part 1/2" |
| Edge scores and letters (K2 V2…), RED/AMBER/GREEN, Ship Check steps | **WHY THIS GETS CLIENTS** line; **NEEDS YOU: …** only when a fact or consent is missing; "I changed 'guaranteed' to … because…" |
| Bank IDs (S-2, P-3, V-1), Slot/Run keys, schema and brief versions | "your 2019 exit story", "Maria (needs her OK)", "Short #2 this week", "Brand Card v2, 3 Nov" |
| Templates, the method file, the router, task texts (they say "yes", or paste without reading) | Finished scripts in their delivery mode; captions in copy boxes |
| The full Bank | NOT NOW (≤7 names) + "nothing is wasted" |
| The ops-style scoreboard | A plain 6-line scoreboard (example in §3.1) |

**One collision to fix in the strings:**
- "Pillar" means the 3 belief hills on the Map, and it also means the weekly recording.
- Coach-facing fix: **"3 big ideas / 3 ý lớn"** on the Map, and **"weekly interview / weekly video" ("buổi nói chuyện tuần" / "video tuần")** for the recording.
- "Pillar" stays internal.
- **The spec's footer change:** the old footer `Edge 8/10 (K2…) · Uses S-2…` is replaced by **WHY · NEEDS YOU · NEXT**. In Autopilot, the scores go to Notion properties, not into the chat.

---

## 7. Biggest risks for a non-technical 45-year-old

| # | Risk | Mitigation |
|---|---|---|
| 1 | Stalls before any value (can't find Projects, Mac app, wrong instruction box) | Device-aware doors; 3 actions; the phone door as the universal fallback; 60-second videos; value (the Map) before any file work |
| 2 | Chats outside the project and gets generic output, then blames the product | Running tag; ChatGPT memory guard; "new week = new chat *in Content Machine*" in every Friday NEXT |
| 3 | **Weekly friction: transcripts and clip editing** (the real quit point in the old design) | Chat interview by default; re-film instead of editing; video mode opt-in |
| 4 | Voice input problems (long dictation cut off, VN accents, Claude VN) | Chunks of ≤3 min; keyboard-mic tip; paste a transcript instead; "fix only obvious errors" rule |
| 5 | Lost or duplicated Brand Card | Save button; highest version wins; duplicate detection; memory essence as a backup |
| 6 | Free-tier walls (27K context, 3 uploads a day, Claude caps) | Short replies until the Map; ≤3 sources; a 3-screenshot cap or voice numbers; save points; the Claude "lighter" swap |
| 7 | Overwhelm: walls of text on a phone | One piece per day via "next"; copy boxes; Week 1 split across 2 replies; one NEXT line |
| 8 | Expects "it runs itself" on ChatGPT | Honest label: "you open it, it does the work." Reminders, not full automation; Autopilot only on Claude Pro |
| 9 | Feels boxed in by focus rules ("but I also teach X") | Bridge by default; 1 off-map piece in 10; NOT NOW shown as "later, on purpose"; promotion path |
| 10 | Camera fear: the real reason coaches stop | 20–40 s first piece; read-from-screen mode; post-as-text fallback; streak in the scoreboard |
| 11 | Platform UI drift (labels like "Save to project" change) | Fix lines name 2 likely labels; dated setup page; quarterly update; Phase-0 retest |

### Changes to arch-final-spec (need founder sign-off)
1. Day 0 goes from 5–7 steps to 3 actions (two doors).
2. ChatGPT and Claude use the same kit: one START block plus **one** method file, added at about minute 29. The skill, Notion and connectors move to later upgrades.
3. The Brand Card in project sources replaces `MY-BRAND-BRAIN.md` and the hub as the Day-0 memory.
4. The Season-1 weekly pillar becomes a chat interview; the video pillar is opt-in; re-film instead of editing.
5. ChatGPT automations become reminder tasks created with one "yes". DROP becomes "today's one thing".
6. The coach footer becomes WHY / NEEDS YOU / NEXT; "pillars" become "big ideas" in coach-facing text.
7. The commands shrink to "next" plus 4 optional phrases.

### Phase-0 hands-on tests (all [UNVERIFIED])
**ChatGPT:**
- "Save to project" on Free and on mobile; whether it counts toward the 5-file cap.
- The size limit for a text source (can the method be pasted instead of uploaded?).
- Moving a chat into a project.
- Whether the model can create tasks from a project chat, whether task runs show up inside the project with its instructions, and whether Free can pick weekdays.
- Whether ChatGPT can transcribe an uploaded video or audio file.
- Saving a global memory from inside a project.

**Claude:**
- The label of "Add text content" and the artifact "Add to project" option.
- Free usage cost with 60 KB of project knowledge (caching).
- Whether projects can be created on a phone.

**Both:** whether START works as well pasted as a message as it does as instructions (golden runs).

**Release gate:** 3 non-technical testers aged 45+ (at least 1 VN tester on ChatGPT Free) must, without help, reach the first message in 3 actions or fewer, get a film-ready piece and a saved Brand Card within 40 min, and repeat their core message the next day.

### Critical Files for Implementation
- /root/.claude/plans/all-right-so-this-clever-shore.md: the decisions above get recorded here (Day-0 kit, chat-interview pillar, reminder automations, the "big ideas" rename).
- /home/user/Content-Machine-1.0/core/start-block.tmpl (new; replaces chatgpt-instructions.tmpl and claude-project.tmpl): the single START text, ≤7,500 characters, used as instructions or as a pasted message.
- /home/user/Content-Machine-1.0/modules/setup.md, with /home/user/Content-Machine-1.0/modules/message.md: the first session, the save flow per app, and the "make it permanent" and upgrade dialogues.
- /home/user/Content-Machine-1.0/schemas/brand-card.toml (new; replaces brand-brain.toml as the Day-0 store), with /home/user/Content-Machine-1.0/strings/en.toml and /home/user/Content-Machine-1.0/strings/vn.toml: the Brand Card format and every coach-facing line and fix line.
- /home/user/Content-Machine-1.0/guides/setup-page.tmpl, with /home/user/Content-Machine-1.0/automation/tasks.toml and /home/user/Content-Machine-1.0/platform/targets.toml: the device-aware setup page, the reminder tasks, calendar links and Claude Autopilot, and every dated limit and Phase-0 result.