# Content Machine 1.0: concierge coach experience (EN + VN)

**Design in one line.** On Day 0 the coach does one thing: a "Project kit" that is the same in both apps. On a computer that means 4 steps and about 3 minutes, and a helper can do it for them. After that the coach just talks and taps "OK" once. Everything else (skill, Notion, connector, tasks, Sheet) leaves Day 0. Each of those comes back later as a "level-up" that the machine offers at the right moment, ideally done by a helper.

---

## 1. Install

### 1.1 Which app (the setup page asks only this)
- **Use the app you already use.** If you use both: the VN edition goes to **ChatGPT**, because it has Vietnamese voice, unlimited Free text and needs no international card. The EN edition goes to Claude if you already pay for Pro (autopilot is possible later); otherwise ChatGPT.
- If you use neither, start on **ChatGPT Free**. The Brand Card is plain text, so the coach can move apps later.
- **Gemini moves off the main setup page** and gets a troubleshooting note only. One fewer choice.

### 1.2 Day-0 steps (computer: web or desktop app; about 3 min; identical texts in both apps)

| # | ChatGPT (chatgpt.com or Windows app) | Claude (claude.ai or desktop app) | Time |
|---|---|---|---|
| 1 | Sidebar → Projects → New project → name "Content Machine" → Create. VN line: "Nếu tài khoản dùng chung: chọn bộ nhớ 'Chỉ dự án'" (if you share the account, pick "Project only" memory) | Projects → + New project → "Content Machine" → Create | 30s |
| 2 | Instructions → paste the block (Copy button on the setup page) → Save | Set project instructions → paste the same block → Save | 45s |
| 3 | Add files → select **both** `CM-1-PLAN.md` and `CM-2-WRITE.md` in one go → Open | Project knowledge + → Upload from device → both files | 45s |
| 4 | New chat in the project → paste "Start" / "Bắt đầu" → Send. **Pass test:** the reply begins "Content Machine ·" and shows a setup-check line | Same | 15s |
| 5 | Pick up the phone: ChatGPT app → Projects → Content Machine → the same chat → mic | Claude app → the project → the same chat. **VN:** use the keyboard mic (Gboard or iPhone keyboard). Claude's own mic doesn't support Vietnamese | — |

Notes:
- The picture guide shows each button. In the VN edition it shows both the EN and the VN UI label ("Dự án / Projects"). Every picture is dated.
- The 2 files are **direct downloads, not a zip**. That avoids the Safari auto-unzip problem and Windows extraction confusion. File names are ASCII.

**Setup-check line (the machine's first output):**
- EN: "Content Machine · Setup check: instructions OK · method files 2/2 · Brand Card: not yet (we make it now). Ready."
- VN: "Content Machine · Kiểm tra cài đặt: hướng dẫn OK · 2/2 file phương pháp · Brand Card: chưa có (mình làm ngay). Sẵn sàng."

**Plan differences (the steps don't change):**

| Plan | What's different |
|---|---|
| ChatGPT Free | Uses 2 of the 5 project files and 2 of about 3 uploads per day. With about 27K of context, the machine keeps replies compact and decides when to open a new chat. Tasks come later: 3, in time windows. |
| ChatGPT Go / Plus / Pro | Same steps, more room. Tasks run at exact times. |
| Claude Free | Same steps. With 15–40 messages per 5 hours, the machine inserts save points about every 8 turns ("come back after the reset, say What's next?"). No scheduled tasks; calendar links instead. Knowledge loads into every message, so the files must stay lean. |
| Claude Pro / Max | Same steps. Level 3 Autopilot is available later. |

### 1.3 Phone-only path (no computer; about 30 s; weaker)
1. Open the setup page → "No computer?" → Copy Starter (≤4,000 chars).
2. Open the app → new chat → paste → talk.
3. At the end, the machine has the coach say "Remember my Brand Card" and keep a backup. VN: send it to Zalo "Cloud của tôi". EN: Notes, or email it to yourself.
4. Each later session: paste the short "Continue" prompt plus the Brand Card.
5. The machine nudges once per session: "3 minutes at a computer, or a helper, makes this permanent."
6. Upgrade: do steps 1–4 above → paste the Brand Card into the new project chat → save it.

The Starter prompt and the instruction block are rendered from one Day-0 source, so they cannot drift apart.

### 1.4 Helper handoff (button on the setup page; forwards by Zalo, WhatsApp or email)

**EN:** "Could you set this up for me on a computer? 3 minutes: [link]. Do it in MY ChatGPT/Claude account (sit with me or share my screen). You're done when step 4 shows 'Content Machine ·'. I'll do the talking part."

**VN:** "Nhờ bạn cài giúp mình Content Machine trên máy tính, chỉ 3 phút: [link]. Làm trong tài khoản ChatGPT của mình nhé (ngồi cùng mình, hoặc chia sẻ màn hình qua Zalo/UltraViewer). Thấy chữ 'Content Machine ·' ở bước 4 là xong, phần nói chuyện để mình tự làm."

Rules:
- The helper never does the brain-dump.
- The login stays with the coach, who receives the code.

### 1.5 What the founder pre-builds
1. **The setup page.** Four variants: EN/VN × ChatGPT/Claude.
   - 5 numbered pictures, each with one sentence.
   - Copy buttons for the instruction block and for "Start".
   - 2 direct file downloads.
   - A QR code that opens the page on the phone.
   - A "checked on" date.
   - "What it looks like": 6 screenshots of the Dana or chị Hạnh session, so the coach knows what is coming.
2. **One app-neutral instruction block** (EN ≤6,000 chars, VN ≤7,000). It contains:
   - the **whole Day-0 engine**: dump → check → Map → OK → save → film today;
   - the self-check (Brand Card in sources → project memory → "paste it or say start");
   - the router, the Ship Check with FOCUS, the running tag and the NEXT logic.

   Day 0 works with **zero files**, so an upload failure never blocks the first session.
3. **Two lean method files**: about 30K chars each, sectioned with `§CM-` anchors.
4. **Phone Starter and Continue prompts.**
5. **The helper kit** (section 1.4).
6. **One-tap reminders:** Google Calendar template links with weekly recurrence, plus Apple `.ics` files, for Mon 07:00, Tue 09:00 and Fri 15:00.
7. **Level-up pages** (section 4), each with 5 pictures or fewer.
8. **Notion template, Sheets Lite and the Claude skill zip** (Level 2/3 only).
9. **Optional human layer:** a weekly 30-minute "install together" live session (VN: inside the buyers' Zalo or Facebook group). This is a founder decision because it costs ongoing time.

**Verdict on share links:**

| Link | Use it? | Why |
|---|---|---|
| Hosted setup page | **Yes, it is the core** | Copy buttons replace templates and zips |
| ChatGPT shared project | No | Every member sees every chat; member caps; memory off; link broke on 10 Sep and 24 Sep 2026 |
| ChatGPT shared-chat "continue" | Read-only demo at most | Instructions and files don't carry over |
| ChatGPT task share links | Not on Day 0 | No files or memory, so the brief must be pasted anyway. EN would leak the creator's time zone. VN (one time zone) is a later option *if* tasks can read memory or the project |
| Claude shared chat | Demo only | View-only |
| Claude published artifact | Optional pre-purchase "Message Map taster" | Uses the visitor's limits, no skills or memory, link leaks. Not the machine |
| Notion Duplicate / Sheets Make a copy | Yes, Level 2 | 1 click each |
| Calendar template links | Yes, Level 1 | 1 tap |

### 1.6 What can fail, and the fix

| Symptom | Cause | Fix |
|---|---|---|
| Reply doesn't start with "Content Machine ·" | Chatting outside the project, or instructions not saved | Guide, shown in big type: "Always: Projects → Content Machine → newest chat." Reopen Instructions → Save |
| "Upload limit reached" (Free) | About 3 uploads a day | Ignore it today; the block runs Day 0 alone. Next day the machine says: "Add the 2 files now (Step 3), 1 minute" |
| Machine says "method files not found" | Step 3 skipped | Same one-line nudge. It never blocks |
| No "Projects" on the phone | Creation is computer-only (unverified for Claude) | "Normal. Do steps 1–4 once on a computer; use the phone after" |
| A downloaded file opens as gibberish | The coach opened the file | "Don't open it, just upload it" |
| Vietnamese voice comes out wrong in Claude | Claude dictation lacks Vietnamese | The machine's first VN Claude message: "Dùng micro trên bàn phím điện thoại" (use the phone keyboard's mic) |
| "You've reached your limit" (Claude Free) | Usage cap | Save points every 20 minutes or so; "What's next?" resumes |
| Brand Card missing in a new chat | Save step skipped | Self-check: "Your Brand Card isn't saved. On the computer: open the first chat → ••• → Save to project. Or paste it here" |
| Output sounds generic or uses the wrong xưng hô | Drift | "Make it sound like me" / "Viết lại giọng mình"; "Sửa xưng hô: mình – chị em" |
| Coach can't find yesterday's script | Too many chats | Every NEXT line names where things are ("newest chat in Content Machine") |
| Coach is lost or anxious | — | "I'm stuck" / "Mình bị kẹt" → the machine diagnoses in plain words (this needs the coach to be inside the project) |

---

## 2. First session, minute by minute

| Min | Coach does | Machine gives |
|---|---|---|
| −3–0 | Section 1.2 steps on the computer (or a helper does them) → pastes "Start" | Setup-check line + 3-line promise ("1) Empty your head 2) I pick the ONE thing 3) You film today") + "Pick up your phone, open this chat, tap the mic" |
| 0–11 | Brain-dump by voice in 2–3 chunks, or pastes a webinar or live transcript | "Got it. Keep going or say 'done'." plus one jogger not covered yet |
| 11–12 | — | **Inventory** (EN: "You know a lot… about 6 months of content, in the right order. Nothing gets thrown away.") + **pre-filled check**: 6 lines, with "?" only where it needs live words |
| 12–17 | "yes, fix 4" + 2–3 live answers (their exact words, best result with a number) | At most 1 probe per question; Quick Listen (≤5 searches) → root cause |
| 17–19 | — | **Message Map** (one screen) + "Why this one: {4} people paid you for it…" + NOT NOW (≤7 items) + reassurance |
| 19–20 | **THE ONE DECISION:** "OK" (or "change line 3") | — |
| 20–21 | **Save (10 s):** on the computer, ••• under the Map → Save to project → "saved". Claude: + → add text content, or "remember this". Screenshot the pocket card | **Pocket card:** core message, 3 pillar names, keyword, plus the 3 phrases. Backup tip (Zalo Cloud / Notes). No button visible? "I'll remember it for now; save it next time at the computer" |
| 21–24 | — | **FILM TODAY:** a Pillar-1 "Belief Bomb" short, 20–40 s, Mode B: on-screen text, first line, 3 beats, last line, a copy-ready caption, the WHY line, and "Ready to post" |
| 24–25 | "film now" or "later" | If now: a 3-tick "before you film" card (hook out loud twice, keyword in, last line slow) |
| 25–26 | Confirms one defaults line | Platform · record day (Tue) · script style (bullets) · xưng hô · hours a week |
| 26–27 | — | Week 1 at a glance (5 lines) + **stop point**. EN: "Stop here, or 'go' for Week 1 scripts (8 min)?" VN: "Hôm nay vậy là đủ. Muốn làm tiếp tuần 1 (8 phút) thì gõ 'tiếp'." |
| 27–35 | "go" (optional) | Week 1 cut from the dump (pillar #0): 3 shorts + 1 text post, compact. Generated now while the dump is still in context |
| 35–37 | — | Wrap-up + exactly one NEXT line: "Tomorrow: post today's video. Open Content Machine → 'What's next?' → copy the caption." Optional: the 2 calendar links |

About 10–12 coach turns; 8 or fewer before the Map.

**The coach walks away with:**
1. The Message Map, saved in the project, and the pocket card on their phone (it doubles as the cheat-sheet).
2. One video to film today, with its caption.
3. The Week-1 plan, and the scripts if they said "go".
4. A record day set.
5. One next step.

The Brand Card's hidden block also stores 5 verbatim passages from the dump. Week 1 can therefore be regenerated in any new chat with at least 70% the coach's own words.

---

## 3. Week 1 and the weekly loop

**The rule the coach remembers:** "Open Content Machine, newest chat." The machine decides when a new chat is needed (new week, or a recording) and says so in the NEXT line. This protects Free's 27K context and prevents long-chat drift.

### Week 1 (nothing runs automatically yet, on purpose)

| Day | Coach | Minutes | Where it comes from |
|---|---|---|---|
| 0 | First session; film the short | 37 + 10 | — |
| 1 | "What's next?" → copy caption → post. Optional: forward the ready-written Buyer Mirror message to 3 clients on Zalo or Messenger | 3 (+3) | Start chat |
| 2, record day | "What's next?" → film 2 Week-1 shorts (12 min) → **Weekly Talk**: a 15–20-minute interview where the machine asks the questions (VN: ChatGPT voice mode inside the project; otherwise dictation) → the machine cuts it into Week 2 | 35–40 | New chat, as the machine says |
| 3–4 | Post today's piece (copy caption) | 2–3 each | — |
| 5 (Fri) | 3 insight screenshots → "Here are my numbers" | 3 | 5-line review + Week-2 preview + Level 1 offered |

About 70 minutes after Day 0.

**Weekly Talk** means the founder's "guided interview" pillar format, used as the Lean default. There is no transcript tool and no editing: the shorts are re-filmed in 1–2 takes from verbatim passages of the talk.

### Weekly loop from Week 2 (Lean ≤1 h is the default; Standard and VA add on top)

| When | Coach | Min | Arrives automatically (Level 1 on) |
|---|---|---|---|
| Mon | Tap the reminder → New chat → "What's next?" → the week (pillar of the week, 4–5 posts from last week's talk, 1 native short) → "ok" | 5 | 07:07 nudge: the week's pillar + 3 hooks |
| Tue | Film 4 shorts from last week's talk (20) + this week's Weekly Talk (20) → cut arrives | 40 | 09:00 reminder |
| Wed–Sun | "What's next?" → copy caption → post | about 10 total | Optional 07:07 idea + 1 question |
| Any day | "Park that: …", or a screenshot of a client message (optional) | 0–2 | — |
| Fri | Screenshots → "Here are my numbers" → 5-line review + 3 bets, which next Monday applies | 5 | 15:07 nudge |

Totals and variants:
- **Lean:** about 60 minutes a week. Output: 3 talk-based shorts, 1 native short, 1 text post, 1 email or Zalo message.
- **Standard:** the pillar is filmed as a video (FB Live, YouTube or phone) and the transcript is sent. Getting the transcript is the risky part (section 7).
- **VA:** the VA trims clips, posts, and sends stats.

### What gets copied or pasted, and where

| What | From → to | How |
|---|---|---|
| Caption | Chat → the Facebook, TikTok or Instagram post box | Long-press → Copy, or the copy button on a caption block (test readability) |
| Video | Phone camera → platform | As-is; no editing in Lean |
| Weekly Talk | — | Nothing to paste; the talk lands in the chat |
| Numbers | Insight screenshots → chat | + → Photos |
| Client words | DM or comment screenshots → chat | The machine keeps the person's role, never their name |
| Buyer Mirror | Chat → Zalo or Messenger | Copy → paste (Week 1 only) |
| Brand Card | Chat → project sources | Monthly: ••• Save (new) + Remove (old). 2 actions, keeps Free at 3 files |

**Monthly** (the last Friday's NEXT line): "Plan next month" (20 min or less). The message check defaults to KEEP, which is the one decision. A new Season block goes into the refreshed Brand Card.

**Quarterly:** re-map, usually KEEP.

---

## 4. Hub and the 3 automations: when, by whom, how many steps

| Level | Offered when | By whom | Steps | What changes |
|---|---|---|---|---|
| **0 Project kit** | Day 0 | Coach or helper | 4 | The machine itself |
| **1 Reminders / tasks** | After the first Friday review: the coach has done one full loop and knows what a nudge means | Coach | ChatGPT: 1 paste per task. Claude Pro: Scheduled → New task → paste → pick day and time (4 clicks). Claude Free: 1 tap per calendar link | Mon, Tue and Fri pings |
| **2 Team board (hub)** | Coach mentions a VA or editor, or at "Plan next month" | Helper or VA | Notion (default): Duplicate (1 click). On Claude: + Connect Notion → share only the "Content Machine" page (3 clicks). Sheets Lite: Make a copy (1 click) | ChatGPT: the machine adds a paste block for the VA. Claude: writes rows directly. **The coach does nothing new** |
| **3 Autopilot** (Claude Pro/Max only) | After Week 1, if the coach says yes | Helper recommended | About 6 steps, about 10 min: skill zip (download in Chrome) → Skills upload → Level 2 Notion → "Turn on autopilot" → Create with Claude → Run now | BATCH, DROP and REVIEW run, read and write Notion, with catch-up |

**How the three automations behave for each kind of coach:**

| Coach | BATCH (Mon) | REVIEW (Fri) | DROP (daily) |
|---|---|---|---|
| **Solo coach, ChatGPT or Claude without autopilot** (recommended) | Nudge + preview: the week's pillar and 3 hooks, then "tap Content Machine → What's next?" | Nudge: "send your screenshots in the project" | Optional, only if asked: 1 idea + 1 question |
| VA tier | Full-work standalone task (arch spec §7, with the brief embedded); the VA files the output | Same | Same |
| Claude Pro Autopilot | Connected full runs | Connected full runs | Connected full runs |

- **Why nudges for solo coaches:** script work stays in ONE place (the project, with its method files and Brand Card). Otherwise scripts land in separate task chats the coach can't find later. If the hand-test shows a ChatGPT task can live inside a Project and read its sources, the tasks become full-work tasks and stay in one place anyway.
- **Staging:** Monday first, Friday after Week 2, daily only on request. That fits Free's 3-task cap. If Free can't schedule a specific weekday, use one "Daily Machine" nudge.

**Why the hub stays optional for a solo coach:**
- On ChatGPT nothing writes to it automatically, so a hub means copy-pasting rows. That is exactly the "templates I can't execute" pain.
- The project already holds the Brand Card and the scripts.
- The hub's value is coordinating a team and seeing a calendar. So: "the board is for your team, not for you."
- Notion remains the default whenever a hub is added (founder decision kept).

---

## 5. The phrases the coach ever needs

These are printed on the pocket card. Plain words always work too.

| # | EN | VN | Does |
|---|---|---|---|
| 1 | **What's next?** | **Tiếp theo làm gì?** | Starts setup if there's no card; resumes; gives today's piece and caption; recovers anything |
| 2 | **Here's my recording** | **Đây là bản ghi của mình** | Weekly Talk or transcript → the week's pieces |
| 3 | **Here are my numbers** | **Số liệu tuần này** | Screenshots → 5-line review + bets |
| 4 | Park that: … | Để sau: … | New idea → bridged to a pillar or parked; never derails |
| 5 | Make it sound like me | Viết lại giọng mình | Voice fix |

Safety net (not memorised; printed in the guide): "I'm stuck" / "Mình bị kẹt".

"Start" / "Bắt đầu" comes from a copy button, so the coach doesn't need to remember it.

---

## 6. What the coach never sees vs. what they see

| Never sees (stays internal) | Sees (plain words) |
|---|---|
| Any blank template or form to fill in | Finished words: what to say, on-screen text, a caption ready to copy |
| Framework names: Admirable…Trustable, SPCL, B1–B7, Big Domino, 4-3-2-1, Signal, 3D test, Buyer Filter, Offer v0 | "Pillar 1/2/3" by name; "a simple first offer" |
| Focus Score, Edge 0–10 with K/V/A/Au/C, the Ship Check steps, claims colour codes | One footer per piece. EN: "Ready to post · Needs you: nothing · Next: Thursday video". VN: "Sẵn sàng đăng · Cần bạn: không · Bài tiếp: video thứ Năm" |
| Bank IDs (V-, S-, P-, B-, K-, X-), Slot keys (N1, C3), Run keys | "Proof: your 2019 story" / "Maria's result: ask her OK first". The Brand Card's machine block is labelled "for the machine, don't edit" |
| The 12-line scoreboard | A 5-line Friday review: posted, buyer signals, best piece and why, one fix, next week's pillar ("details" shows more) |
| Method files, router, hub schema, platform policy details | One dated platform note, only when relevant (for example, comment keywords on a personal profile) |
| — | The Message Map, the pocket card, NOT NOW (≤7 items, with the "nothing is wasted" line), the "Why this one" line, the WHY THIS GETS CLIENTS line on every piece, a "Content Machine · step x/y" tag, exactly one NEXT line, and short checklists only at the moment they're needed |

---

## 7. Biggest risks for a non-technical 45-year-old

| # | Risk | Mitigation |
|---|---|---|
| 1 | Gives up at the computer step | Helper handoff; a 30-second phone path that still gives a script on day one; picture guide; optional "install together" live session |
| 2 | **"Where do I go?"**: chats outside the project, task chats, many chats | The running tag; one rule ("Content Machine, newest chat"); the machine decides when to open new chats and names where things are; nudge tasks for solo coaches |
| 3 | **Recording → transcript** stalls the weekly loop | Weekly Talk by default (voice inside the project, nothing to paste); Week 1 needs no recording; mini-talk fallback ("10 minutes, 3 questions") |
| 4 | Brand Card never saved or lost → generic output → "it stopped working" | Self-check every chat; memory backup; Zalo Cloud / Notes copy; verbatim passages in the card |
| 5 | Rubber-stamps "OK", doesn't own the message, stops posting | "Why this one" line; change-any-line option; pocket card; human gate "can repeat it the next day"; first monthly check after real buyer signals |
| 6 | Overwhelmed reading long replies on a phone | One piece per day by default; just-in-time scripts; stop point at minute 27; compact batches of 3 on Free |
| 7 | Free caps interrupt a session (Claude Free) | Save points; "What's next?" resumes; lean files |
| 8 | UI labels change and pictures go stale | Dated guide; both UI labels shown; quarterly refresh; label-proof wording ("the ••• under the message") |
| 9 | VN specifics: Claude voice, shared accounts mixing memory, claims that break the 2026 law | ChatGPT default for VN; Project-only memory line; the Ship Check claims guard with "Needs you" questions |
| 10 | Concierge support load swamps the founder | Self-serve first (setup check, "Mình bị kẹt"); the live session is weekly and group, not 1:1 |

---

## Changes to arch-final-spec
1. **§2.1 install.** Replace with the 4-step Project kit, identical on Claude and ChatGPT.
   - Removed from Day 0: the code-execution toggle, the skill zip, Notion Duplicate, the connector, the Sheet copy, notification settings, and the `MY-BRAND-BRAIN.md` upload.
   - START-HERE becomes the **hosted setup page**. The zip remains as an archive.
2. **The instruction block carries the full Day-0 engine** and the self-check. Method files go down to about 30K chars each. `targets.toml` needs new budgets.
3. **`MY-BRAND-BRAIN.md` becomes the "Brand Card".** It is one saved reply (≤4,000 chars): a "for you" part (the Map) plus a "for the machine" part (mini-bank, 5 verbatim passages, Season block, `plan_start`). It is replaced monthly.
4. **Automations:**
   - Staged: Monday first, then Friday, then daily.
   - Solo coaches get nudge tasks; full-work tasks are for the VA tier and Claude Autopilot.
   - Claude Free and anyone without tasks get calendar links instead of the `.ics` import step.
5. **Hub moves to Level 2** (done by the helper or VA). The skill, Notion and scheduled tasks together become Level 3 Autopilot.
6. **Footer, review and IDs are rewritten into plain words** (section 6). Commands are reduced to section 5.
7. **The Lean pillar becomes the Weekly Talk** (audio only; shorts are re-filmed from verbatim passages).
8. **Gemini leaves the main setup page.**

## Hand-test before launch (in addition to the research list)
1. **Can a ChatGPT scheduled task be created inside a Project chat and read its sources?** This decides between nudge tasks and full-work tasks.
2. ChatGPT voice mode in a Project:
   - Does it follow the interview rules?
   - Does it leave a usable transcript, in VN and in EN?
3. Can an audio or video file uploaded to the chat be transcribed (ChatGPT; Claude)?
4. Can a project be created from the phone's **browser**?
5. Does a full Day-0 session complete on ChatGPT Free (Luna, 27K) with zero files, and with the 2 files?
6. Does the running tag survive 30+ turns?
7. "Save to project": the label in the VN UI, whether it works on mobile, and whether it counts toward the file cap.
8. Claude's "add text content" label.
9. Do the recurring calendar links open correctly on iPhone and Android?
10. Are caption blocks readable on a phone, and does one tap copy them (VN diacritics)?
11. Three testers aged 40+ (at least 1 VN) install from the pictures alone in 5 minutes or less, plus one helper test over Zalo screen share.

## Founder decisions this design needs
1. Nudge tasks for solo coaches, or full-work drafts delivered in separate task chats.
2. The Weekly Talk (audio-only, Lean) as the default pillar, or a video pillar for everyone.
3. Whether to offer a group "install together" session and a buyer Zalo group, and at what cost.
4. Drop Gemini from the main setup page.
5. Write the VN instruction block (the part the buyer pastes and sees) in Vietnamese, while the method files stay in English.

### Critical Files for Implementation
- /root/.claude/plans/all-right-so-this-clever-shore.md: the source of truth; record the changes listed above.
- /home/user/Content-Machine-1.0/core/chatgpt-instructions.tmpl: becomes the app-neutral `core/project-instructions.tmpl`. It holds the Day-0 engine, self-check, running tag and Ship Check, and also renders the phone Starter and Continue prompts.
- /home/user/Content-Machine-1.0/modules/setup.md, with /home/user/Content-Machine-1.0/modules/message.md: the minute-by-minute first session, the save moment, the stop point, Weekly Talk and the level-up offers.
- /home/user/Content-Machine-1.0/guides/start-here.tmpl, with /home/user/Content-Machine-1.0/strings/en.toml and /home/user/Content-Machine-1.0/strings/vn.toml: the setup page in 4 variants, the helper kit, troubleshooting, and every EN/VN line above.
- /home/user/Content-Machine-1.0/schemas/brand-brain.toml, with /home/user/Content-Machine-1.0/automation/tasks.toml and /home/user/Content-Machine-1.0/platform/targets.toml: the Brand Card format and its versioning, nudge vs full-work task variants, and the new budgets (the instruction block with the Day-0 engine, and method files of about 30K chars).