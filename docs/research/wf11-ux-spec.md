# Content Machine 1.0: Final UX Spec (EN + VN)

**Basis.** I added up each design's scores across the 3 personas (5 scores per persona: install, first session, weekly, "know what to say", trust):
- concierge: 114
- zero-setup: 113
- guided-project: 101

The final design takes from each:
- **From concierge (the base):** one Project kit with the method file added during install, a setup-check line, a helper handoff, a Map screen showing "why this one" and NOT NOW, and a stop point.
- **From zero-setup:** one text that works in both apps, ONE method file, "next / tiếp" for everything, a 10–15 min audio-only chat interview each week, numbers given by voice, and no daily idea drops.
- **From guided-project:** the "what you'll have in 40 minutes" preview, the plain "✓ Checked" line, calendar reminders on Day 0, and compact mode (Day 0 runs even with no files).

Every quit point the personas reported is removed; §6 lists each one with its pass condition.

---

## 1. Install

### 1.1 The setup page
- **One hosted page per edition.** It is a plain mobile-first web page, not a Notion page (Hạnh got stuck at the Notion "Open in app" wall). It is linked from the purchase email and from the seller's Zalo message.
- **Top of the page:**
  - A sample Message Map and film-today script (Dana / chị Hạnh) under "What you'll have in 40 minutes".
  - Three lines: what it does, what it doesn't do ("you open it, it does the work; it doesn't post for you"), and "checked on {date}".
- **It asks one thing: which app.**
  - VN opens on ChatGPT, marked "Khuyên dùng".
  - EN: "use the one you already pay for; none yet → ChatGPT Free".
  - Gemini moves to the troubleshooting page.
  - The device is detected automatically.
- **Computer visitors** go to Door A.
- **Phone visitors** see 3 big buttons:
  - **[Ask someone to set it up]** sends the helper message by Zalo, WhatsApp or email.
  - **[Send this page to my computer]**
  - **[Phone only: start now, 30 s]** goes to Door B.
- **Phase-0 switch.** If the ChatGPT or Claude phone app can create a project, paste instructions and add a file, phone visitors get Door A first.

### 1.2 Door A: recommended for every plan (4 steps, about 3 min, identical text in both apps)

| # | ChatGPT (chatgpt.com in a browser or the Windows app; **Mac: use the browser, not the app**) | Claude (claude.ai or the desktop app) | Time |
|---|---|---|---|
| 1 | Sidebar → Projects → New project → "Content Machine" → Create. Keep Default memory. VN shared account: pick "Project only / Chỉ dự án" | Projects → + New project → "Content Machine" → Create | 30 s |
| 2 | Instructions → paste (**Copy button 1**) → Save | Set project instructions → paste the same text → Save | 45 s |
| 3 | Add files → `CONTENT-MACHINE-EN.md` / `-VN.md` (**one** file, direct download). Alternative: "Copy method text" → Sources → Add → Text | Project knowledge + → Upload from device → the same file (or "Add text content" → paste) | 45 s |
| 4 | New chat in the project → paste **Start / Bắt đầu** (Copy button 2) | Same | 15 s |

- **Pass test.** The first reply must begin `◆ Content Machine · Setup check: ✓ instructions ✓ method file · Brand Card: we make it today` (VN: `◆ Content Machine · Kiểm tra cài đặt: ✓ hướng dẫn ✓ file phương pháp · Brand Card: làm ngay hôm nay`).
- **If step 3 fails** (Free upload cap, file picker, Safari opening the file), compact mode runs all of Day 0 from the instruction block alone. Day 0 never sends the coach back to the setup page, and nothing can block it.
- **Optional:** reply 1 tells the coach they can talk from the phone: "Open the ChatGPT/Claude app → Projects → Content Machine → this chat." The setup page has a QR code to install the phone app.

### 1.3 By app and plan

| App / plan | Path | Steps | Time | Notes |
|---|---|---|---|---|
| ChatGPT Free / Go (**VN default**) | Door A (self or helper) | 4 | 2–3 min | 1 upload on Day 0. The kit never needs more than 3 sources: the method file, the Brand Card, and later the GROW file. Brand Card printed before anything long (27K context) |
| ChatGPT Plus / Pro | Door A | 4 | 2–3 min | Level 1 tasks later, at exact times |
| Claude Free | Door A | 4 | about 3 min | The method file loads into every message, so it is kept ≤50 KB. Save points about every 8 turns. Calendar reminders only (no scheduling) |
| Claude Pro / Max (**EN default if already paying**) | Door A; Autopilot from Week 2 | 4 (+12 min later) | about 3 min | Calendar reminders on Day 0 close the Pro reminder gap |
| VN on Claude | Door A | 4 | about 3 min | Use the **keyboard mic** (Gboard or iPhone); Claude's own mic doesn't support Vietnamese |
| Any app, phone only, no helper today | Door B | 2, plus 2 at the end | 30–60 s | Weaker (§1.4) |

### 1.4 Fallbacks
1. **Helper path** (the concierge pattern; the most natural option for VN).
   - The helper message says: "3 minutes, in MY account, sit with me or share my screen (Zalo/UltraViewer). You're done when step 4 shows '◆ Content Machine'."
   - It adds: "Later today, 30 s: open the first chat → ⋯ under BRAND CARD → Save to project."
   - The login stays with the coach.
   - The page pushes: "Don't wait for them. Start talking on your phone now (Door B); they'll move it in."
2. **Door B, phone only.**
   - Copy **Phone Starter** → new chat → paste → send.
   - The Phone Starter opens with "You only need to press Send. The rest is for the machine." (VN: "Bạn chỉ cần bấm Gửi. Phần dưới là hướng dẫn cho máy, không cần đọc.") It contains no § signs and no English.
   - The session runs exactly like Door A, including Week 1.
   - Door B **never mentions a project**. It ends with 2 actions:
     1. Long-press this chat → Rename → "Content Machine". This makes "open Content Machine" true.
     2. Copy the **MY CONTENT MACHINE** box (compact rules + Brand Card) → send it to yourself (VN: Zalo "Cloud của tôi"; EN: Notes or email).
   - When the chat gets long, the machine prints a fresh box and says "paste this into a new chat named Content Machine". That is one paste, never two.
3. **Move-in later.** The coach or helper does Door A steps 1–3, then pastes **Start + the MY CONTENT MACHINE box** in one message. The machine prints the Brand Card for saving and resumes where they left off. This does not depend on moving chats between projects, which is unverified.

### 1.5 What the founder pre-builds (per edition)

| Item | Spec |
|---|---|
| Setup page | Mobile-first and device-aware, with app tabs. Copy buttons for the instructions, Start and the Phone Starter. One direct download (served `Content-Disposition: attachment`; ASCII name) plus a "copy text" alternative. QR code; outcome preview; helper message with share buttons; "Stuck?" box with 8 fixes; dated. Five silent captioned videos of 60–90 s each: ChatGPT web, Claude web, phone start, saving the Brand Card, finding the mic (with an Android screenshot) |
| Instruction block (`1-INSTRUCTIONS.txt`, the same for both apps) | EN ≤6,500, VN ≤7,500 characters after NFC. VN is **written in Vietnamese**. Contents: running tag + one NEXT line; self-check; **the whole Day-0 engine**; compact locale rules (xưng hô, dialect, spoken particles, banned calques); **inline claims guard** (no guarantees or "tốt nhất"; insurance, real-estate, health and income rules); the router to the method anchors; compact Ship Check + FOCUS; save steps per app; level-up triggers; non-negotiables repeated at the bottom |
| Phone Starter | ≤7,500 characters, rendered from the same source. It has no router but adds a lite Week-1 writer |
| Method file `CONTENT-MACHINE-{EN,VN}.md` | **One** file, ≤50 KB EN / ≤55 KB VN, with `§CM-` anchors: TALK, WEEK, TODAY, NUMBERS, MONTH, FORMATS, CTA-KIT, CHARACTER-LITE, RESEARCH-LITE, EDGE, HUMANIZE, GUARDRAILS, LOCALE |
| Later kit | `GROW-{EN,VN}.md` (launch, deep research, ads, packaging library). Claude Autopilot skill zip. Notion template. Sheets Lite. Static `.ics` fallbacks |
| Human layer (founder decision; costs time) | VN buyers' Zalo group with a weekly 30-min "cài cùng nhau" group install session; EN optional |
| Generated in-session, never pre-built | Brand Card, gift asset, DM replies, calendar links, task texts (in the coach's own time zone) |

---

## 2. First session: minute by minute (Door A; Door B is identical)

**Rules for every reply:** it starts with `◆ Content Machine · {step}` and ends with exactly one `NEXT → … / TIẾP → …`. One screen per reply. "skip / bỏ qua" always works.

| Min | Coach | Machine and key lines |
|---|---|---|
| −3–0 | 4 install steps, or the helper does them | — |
| 0 | Pastes **Start / Bắt đầu** | Setup-check line, then the 3-line promise. **EN:** "Today, about 30 min: 1) Empty your head: talk 5–10 min. 2) I find the ONE thing you'll be known for and park the rest. 3) You get a video you can film today." **Mic tip by device:** "Phone: tap the small mic in the message box, NOT the sound-wave button. Mac: press fn (globe) twice. Windows: Win+H." Then the dump prompt. **VN** (neutral pronoun until it knows): "Hôm nay mình làm 3 việc, khoảng 30 phút: 1) Xả hết những gì bạn biết, nói 5–10 phút. 2) Mình tìm ra MỘT điều bạn nên được nhớ tới, phần còn lại cất để sau. 3) Bạn có ngay một video quay được hôm nay. Trước tiên: mình nên gọi bạn là anh, chị hay bạn? (gõ 1 chữ)" |
| 0–1 | VN: "chị" | **VN dump prompt in chị–em:** "Dạ, em chào chị. Giờ chị cứ xả hết ra nhé: bấm micro nhỏ trong ô chat (đừng bấm nút sóng âm), nói 2–3 phút rồi bấm gửi, rồi nói tiếp. Kể xong một chuyện thì gửi một lần, để không mất chữ nào. Lộn xộn càng tốt, sắp xếp để em lo." Followed by the 5 topic hints. On Claude: "Chị dùng micro trên bàn phím điện thoại nhé, micro của Claude chưa nghe được tiếng Việt." |
| 1–4 | Dump chunk 1 (2–3 min) | **EARLY WIN.** This fixes the minute 8–10 quit point. **EN:** "Got it. 3 lines you just said that are worth money: 1 '…' 2 '…' 3 '…'. Line 2 is a post as it stands. Keep going, or say 'done'. You haven't told me {what clients ask you most}." **VN:** "Em nhận rồi. 3 câu đáng tiền chị vừa nói: … Câu số 2 đăng được luôn. Chị kể tiếp, hoặc gõ 'xong'. Chị chưa kể {câu khách hỏi nhiều nhất}." |
| 4–11 | Chunks 2–3, then "done / xong" | One jogger per chunk. **What the machine extracts without showing it:** inventory, who candidates, client words, stories and proof, voice (5 verbatim phrases), energy per topic, income streams, and pillar-#0 passages. If a dictation fails: "Looks like that got cut off. Say it again in 2 shorter pieces." |
| 11–12 | — | **Inventory:** "You know a lot… about 6 months of content… nothing gets thrown away." / "Chị biết nhiều thật… khoảng 6 tháng content… không bỏ gì cả." **Pre-filled check, 7 lines**, with "?" on only 2–3 of them: Who · Their words · Old way · Best result · Your way · Offer · **7 How you'll work:** main platform + email/Zalo · email list size · past clients who'd vouch · hours a week · talk day · bullets or word-for-word. **If the dump shows 2+ income streams:** "You earn from 3 things. I'll look for the ONE person who could buy more than one. Or tell me: which pays the bills this month?" / "Anh đang có 3 nguồn thu. Em tìm MỘT kiểu khách có thể mua nhiều thứ của anh. Hoặc anh nói luôn: tháng này nguồn nào nuôi anh?" |
| 12–17 | "ok, fix 4" plus 2–3 live answers (their exact words; best result with a number) | At most 1 probe per question. Quick Listen runs silently. The why-chain gives big idea 1 its root cause. |
| 17–19 | — | **MAP SCREEN, one view:** the one message; **3 BIG IDEAS / 3 Ý LỚN**; keyword; offer; one "Why this one: {4} people paid you for it, you can quote them, you lit up about {X}" line; NOT NOW (≤7, each with a plain reason); "Nothing you know is wasted…". **Framing:** "We'll run this for 4 weeks, then check what your buyers say back." / "Mình chạy thử 4 tuần, rồi xem khách nói lại gì." (The coach never sees "lock".) The 3-line pocket version ends with "screenshot this". |
| **19–20** | **THE ONE DECISION:** "OK" / "change line 3" (VN: "ok" / "sửa dòng 3") | — |
| 20–24 | Reads it; films now or later | **FILM TODAY / QUAY HÔM NAY (under 30 s)**, built to memorise because one phone can't film and show the script at once: on-screen text (≤6 words), first line word-for-word, 3 beats (≤12 words each), last line word-for-word. Caption in a copy box; keyword CTA; `WHY THIS GETS CLIENTS / VÌ SAO RA KHÁCH` line. **"✓ Checked:** one idea · sounds like you · uses your 2019 story · keyword once · no risky claims" / "**✓ Đã kiểm:** 1 ý · đúng giọng chị · dùng chuyện spa 2018 · từ khoá 1 lần · không có câu hứa rủi ro". **Quiet CTA option:** "A comment word gets people something real, so it isn't pushy. Prefer quieter? Say 'quiet'." / "Muốn nhẹ nhàng hơn? Gõ 'nhẹ', em đổi thành 'nhắn em nhé'." **Before-you-film ticks:** say the first line out loud twice · keyword is in · say the last line slowly. "Not filming today? Post the caption as text." |
| 24–26 | Optional: save (30 s) | **STOP POINT + BRAND CARD.** Visible part ≤1 phone screen, then a fenced block labelled "for the machine, no need to read". **EN:** "That's today done. This card is how I remember you. Save it (30 s): ⋯ under this message → Save to project. Then say 'next' for your Week 1 scripts (8 min), or stop here; they'll wait." **VN:** "Hôm nay vậy là đủ rồi chị. Đây là Brand Card để em nhớ chị. Lưu lại (30 giây): bấm ⋯ dưới tin nhắn này → Lưu vào dự án (Save to project). Muốn làm tiếp kịch bản tuần 1 (8 phút) thì gõ 'tiếp', không thì mai làm." **Saving is never a gate:** "next" works either way. Claude steps follow a picture guide; backup line: "or email it to yourself / gửi vào Zalo Cloud". |
| 26–34 | "next / tiếp" | **Week 1, cut from the dump**, in 2 replies (3 per reply on Free). The mix follows the platform: <br>• FB/TikTok/IG: 3 shorts, 1 long post, 1 email or Zalo message. <br>• LinkedIn/newsletter: 2 posts, 1 email, 1 carousel, 1 optional short. If the list is ≥300, the **lead piece is an email with "reply to me"**. <br>Plus the free gift (fits in one DM), DM replies 1–2, and the **"ask 3 past clients one question"** message (VN: "hỏi 3 khách cũ một câu", sent via Zalo). |
| 34–36 | Optional: 1–2 taps | **Wrap-up in 3 lines:** today / talk day / Friday. Optional reminder: "Want a nudge on talk day and Friday? Say 'yes'." The machine then gives Google Calendar links or an iPhone `.ics`. Door B adds rename + save box. **NEXT:** "Film today's video. Tomorrow: open Content Machine, newest chat, say 'next'." / "Quay video hôm nay. Mai: mở Content Machine, đoạn chat mới nhất, gõ 'tiếp'." |

**Budget:**
- ≤12 coach turns.
- The Map within ≤8 turns EN / ≤9 VN (the xưng hô turn adds one).
- A film-ready piece ≤24 min after Start.
- The stop point ≤27 min after Start.
- Claude Free: save points after the dump and after the Map ("come back after {time}, same chat, say 'next'").

---

## 3. Weekly loop and progressive level-ups

### 3.1 Week 1 (raw material = the Day-0 dump; nothing runs automatically yet)

| Day | Coach | Min |
|---|---|---|
| 0 | Session + film and post today's short | 35 + 10 |
| 1 | "next" → copy → post. Film the remaining 2 shorts back to back (memorise beat cards, 1–2 takes each) | 3 + 15 |
| 2–5 | "next" → copy → post; answer keyword comments with DM reply 1 (saved in Notes / Zalo Cloud) | 3–5 a day |
| Any | Ask 3 past clients one question (unlocks real proof for Week 3) | ≤5 |
| Fri | "my numbers / số liệu tuần này", spoken: keyword comments · DMs/Zalo adds · calls · sales + best post. Screenshots and views are optional | 3 + 2 |

**Friday review: 5 lines, no codes.** Posted · hands up (keyword comments, DMs, calls) · your message (on-map count, keyword said / said back) · best post + why · next week's big idea. Then the **Level 1 offer**.

### 3.2 From Week 2 (Lean ≤60 min a week; Standard ≤90; the VA tier adds on top)

| When | Coach | Min |
|---|---|---|
| Talk day (default Mon) | New chat → "next" → **Weekly Talk / Buổi nói chuyện tuần**: audio only, no camera, one device. 5 questions, one per message, in belief order for this week's big idea ("tell me the time when…"). The machine replies "Got it. Next:" only. At the end it delivers the week: 3 re-say shorts (≥70% own words), 1 native/character short, 1 long post, 1 email/Zalo, ≥60% on this week's big idea, WHY lines and post days | 15 + 5 |
| Film day (can be the same day) | Film 4 shorts from beat cards; no editing | 20 |
| 5 days | "next" → copy → post | about 12 total |
| Daily | Reply to keyword comments (comment → Messenger → Zalo in VN) | about 5 |
| Fri | Spoken numbers → review + 3 bets | 5 |
| Busy week | "next" gives a **mini-talk** (3 questions, 5 min). Never a zero week | 5 |
| Anytime | "save this: …" → one-line verdict: on your map (big idea 2), or parked (reason) | 0.5 |

Additional rules:
- **Weekly model** (the founder's "pillar + native"): the Weekly Talk is the pillar, in its "guided interview" format. The filmed 20–40 min pillar is opt-in (Standard/VA or Season 2+). It defaults to **re-film, don't edit**; PASSAGE cuts are only for coaches with an editor.
- **Chat rule the coach learns:** "Content Machine, newest chat." The machine decides when a new chat is needed (a new week) and says so in the NEXT line.
- **Monthly:** the last Friday's NEXT line is "plan next month" (≤20 min). The one decision is KEEP / sharpen. Then save the new Brand Card and delete the old one: 2 taps.
- **Quarterly:** re-map, usually KEEP.

### 3.3 Level-ups: the machine offers each one at its trigger; the coach says "yes"; a helper or VA can do L2–L3

| Level | Trigger | App / plan | Steps / time | Adds |
|---|---|---|---|---|
| L0 Project kit | Day 0 | All | 4 steps / 3 min | The machine |
| L0.5 Reminders | End of Day 0, optional | All | 1–2 taps on calendar links | Talk day + Friday nudges |
| **L1 The 3 automations** | After the Week-1 Friday review ("You did a full week. Want me to message you Monday, each morning and Friday? Say 'yes'.") | ChatGPT, any plan: the model creates 3 tasks from the chat [Phase 0]. Fallback: one copy box per task. Free without weekday scheduling: 1 Daily Machine task. Claude Free: a daily calendar link. Claude Pro: goes to L3 | about 1 min (+ 2 taps for push) | **Mon "Your week"** (big idea + 3 hook starters), **weekdays "Today's one thing"** (no new ideas; a capture question 1 day in 5), **Fri "Numbers day"**. Each task is ≤900 characters: pocket Map + Season dates + date arithmetic, sending the coach back into the project. Full-draft tasks only for the VA tier |
| L2 Board | A VA or editor is mentioned; "where is everything?"; end of Season 1; or as a prerequisite for L3 | **Notion (default):** Duplicate; on Claude, connect and share one page. **Sheets Lite:** Make a copy. ChatGPT: honest note that rows are pasted by hand (about 10 min a week, VA) | 2–5 min | Calendar, VA workspace, stats history; the 2× median rule switches on |
| L3 Autopilot | Claude Pro/Max, after Week 2, coach says yes; helper recommended | Skill zip (download in Chrome) + L2 + "Create with Claude" + Run now | about 12 min, can be split over 2 days | BATCH, DROP and REVIEW run unattended and write to Notion. The coach films from the Notion phone app. Ship Check scores go to Notion properties |
| L4 GROW file | First "plan a launch", "research deeper" or "write an ad" | All (built into the L3 skill) | 1 upload | Launch, deep research, ads, packaging library |
| L5 Deep character | Week 3+, or when output reads generic: "Make it more me: 3 × 20-min talks?" | All | Conversation only | Full Character Card, stances, rituals |

---

## 4. Phrases to remember, and what the coach never sees

| # | EN | VN | Does |
|---|---|---|---|
| 1 | **next** | **tiếp** | Everything: resume setup, today's piece, the Talk, catch-up, plan next month, the next level-up |
| 2 | **save this: …** | **lưu lại: …** | A story, client words, result or idea → on-map or parked |
| 3 | **my numbers** | **số liệu tuần này** | Friday, by voice or typing |
| 4 | **make it sound like me** | **viết lại giọng mình** | Voice fix |
| 5 | **I'm stuck** | **mình bị kẹt** | Plain diagnosis; "send me a screenshot and I'll point" |

- **Universal words:** ok · skip / bỏ qua · later / lát nữa · quiet / nhẹ (the CTA switch).
- **Start / Bắt đầu** comes from a copy button and is never memorised.
- No "Content Machine:" prefix.
- "Here's my recording" and "cut it" are dropped: the Talk lives in the chat, and pasted transcripts or uploads are detected automatically.

**Never sees:**
- Templates or forms.
- Framework names: Admirable/Likable/Credible/Trustable, B1–B7, Big Domino, SPCL, 4-3-2-1, Signal, 3D test, Buyer Filter, Belief Bomb, Buyer Mirror.
- Focus Score or candidate tables.
- Edge scores and sub-scores, Ship Check steps, claims colours.
- Bank IDs (V-, S-, P-, X-), Slot/Run keys, `§CM` anchors, the method file contents, the router, task texts.
- "Pillar" (coach-facing it is "big idea / ý lớn" and "Weekly Talk / Buổi nói chuyện tuần").
- "Lock" or "khóa", "Week 0", M1/M2, "keyword asset" (it is "free gift / quà"), Pancake/ManyChat (unless asked).
- Views-based medians before a board exists.

**Sees:**
- The running tag and one NEXT line.
- The Map screen and pocket card.
- NOT NOW (≤7, with plain reasons).
- Finished words with a WHY line, a "✓ Checked" line and at most 1–2 "Needs you" lines.
- The 5-line Friday review.
- The Brand Card's one visible screen.

---

## 5. Changes to arch-final-spec (numbered)

1. **§2.1 Install** is replaced by the 4-step Project kit (identical in both apps), the helper path and Door B.
   - Removed from Day 0: code-execution toggle, skill zip, Notion duplicate, connector, Sheet copy, notification settings, `.ics` import, `MY-BRAND-BRAIN.md` upload.
   - Gemini leaves the main page (troubleshooting note only; build target deferred to 1.1). *Founder sign-off.*
2. **§3.2 dist tree:**
   - `START-HERE.html` (link + QR to the hosted page)
   - `1-INSTRUCTIONS.txt`
   - `CONTENT-MACHINE-{EN,VN}.md`
   - `PHONE-STARTER.txt`
   - `Help/` (troubleshooting, helper-message, reminders/*.ics, examples)
   - `Level-ups/` (`GROW-{EN,VN}.md`, `autopilot/content-machine(-vn).zip`, Notion and Sheets links)

   The `1-Claude/ 2-ChatGPT/ 3-Gemini/` folders are removed. File names are ASCII and identical across editions.
3. **§3.1 core:**
   - Merge `chatgpt-instructions.tmpl` and `claude-project.tmpl` into **`core/start-block.tmpl`**. It renders 2 variants (project, phone) and contains the self-check, running tag, full Day-0 engine, compact locale, inline claims guard, router, Ship Check + FOCUS, save steps per app and level-up triggers.
   - Add `core/self-check.md`.
4. **§9 tiers:** the VN instruction block and Phone Starter move to "Translated / Localized": written in Vietnamese and human-reviewed. The method prose stays English behind the output contract (open decision #1 is unchanged).
5. **Modules:**
   - New `modules/message.md` (Message Focus Engine) **plus** a multi-income bridge-buyer step, an early-win step after dump chunk 1, and "4-week trial" framing.
   - New `modules/talk.md` (Weekly Talk, mini-talk, re-say shorts).
   - New `modules/levelup.md` (L0.5–L5 triggers and guided steps, absorbing the coach-facing parts of `automation.md` and `hub.md`).
   - `setup.md` is rewritten to follow §2.
   - `fmt-long.md` keeps the opt-in video pillar and PASSAGE cuts.
6. **Method packaging:** the Day-0 kit has **one** method file, ≤50 KB EN / ≤55 KB VN.
   - `launch-plan`, `launch-scripts`, research Sprint/why-loop/deep, the packaging library, ads and the full libraries move to `GROW-*.md` (≤60 KB).
   - The full 24-reference skill becomes the L3 Autopilot artifact only.
   - If Phase 0 shows Claude Free gives fewer than 12 turns per 5 hours with the kit loaded, ship a ≤25 KB "Claude Free light" method.
7. **§5.1 Brand Brain → Brand Card** (`schemas/brand-card.toml`).
   - Size: ≤5,000 EN / ≤5,800 VN characters; visible top ≤900 characters.
   - The machine block uses plain field names, no framework words. It holds: Map fields, voice (5 phrases, xưng hô, dialect), compact character (trait, enemy, principles heard), 5 verbatim dump passages ≤60 words each, mini-bank (top 8 V / 5 S / 5 P), plan (`plan_start`, talk day, tier, platform, list size, `cta_style`), NOT NOW names, progress, version and date.
   - Saved as a project source; the highest version wins.
   - The Notion Brand Brain page renders from the same schema at L2/L3.
   - `MY-BRAND-BRAIN.md` and the ≤40 KB bank file are removed.
8. **§5.1 Day-0 questions:** the 10-question intake, Fast lane, Edge card and "pick 1 of 3 keywords" are removed. The keyword is pre-picked with 2 alternates. Character Core Q1–5 are covered by the dump; Excavation becomes L5.
9. **§2.2 order:** dump (early win) → check (7 lines) → Map (one decision) → film today → stop point + Brand Card (never a gate) → optional Week 1 → wrap-up. Automations move out of session 1.
10. **§2.3 weekly:**
    - The Weekly Talk replaces "record pillar + paste transcript" as the Lean default.
    - Lean target ≤60 min (was 75–100).
    - Friday input is 4 spoken numbers + best post. Per-post views/sends/saves and the 2× median rule apply only with a board.
    - Weekly homework item 1 becomes "ask 3 past clients one question".
11. **Platform-aware Week 1:** add `platform_mix` to `editions/*.toml` and `locales/*/market.md`. Email-first when the list is ≥300; text-first for LinkedIn/newsletter coaches.
12. **§6 commands:** reduced to the 5 phrases + ok/skip/later/quiet. `router.toml` keeps every old phrase as a synonym that routes to the same jobs.
13. **§7 automations:**
    - Add `automation/task-nudge.tmpl` (≤900 characters; pocket Map + Season dates + weekday branch). This is the default for solo coaches on ChatGPT at L1.
    - `task-standalone.tmpl` (embedded Task Brief) is used only for the VA tier.
    - Connected tasks are used only at L3.
    - The offer comes after the Week-1 Friday.
    - Never tell the coach to go "outside the project" unless Phase 0 proves the model can't create tasks from a project chat. In that case, one specially labelled copy box.
14. **§5.9 hub:** the schema is unchanged, plus the `Pillar` and `Why` properties. It is introduced only at L2. Notion is the default; Sheets Lite is the 1-click alternative. Remove `hub_by_app`. *Founder decision: Sheets-first for VN ChatGPT + VA.*
15. **§8.1 footer:**
    - The coach sees: WHY line · "✓ Checked: …" in plain words · "Needs you" (≤2) · NEXT.
    - Codes and scores go only to hub properties.
    - The Ship Check / Edge v2 logic is unchanged and stays hidden.
16. **CTA kit:**
    - Comment keyword stays the default (founder decision), with one "why it isn't pushy" line.
    - `cta_style = keyword | quiet` is stored in the Brand Card.
    - VN route: comment → Messenger → Zalo + voice-note follow-up.
17. **Message rules:**
    - Coach-facing "try 4 weeks / thử 4 tuần" replaces "locked 90 days". The internal 90-day lock and the monthly KEEP default stay.
    - Multi-income coaches may opt into ≤1 labelled **side-door piece** a week for a parked income stream. It counts toward the off-map budget, which for them is raised from 1 in 10 to 1 in 7. *Founder sign-off.*
18. **strings (EN/VN), new keys:**
    - Device mic tips: phone small mic, Mac fn×2, Windows Win+H, Claude VN keyboard mic.
    - xưng hô question in reply 1.
    - Early-win, stop-point, save-per-app, Door B rename/box and helper-message lines.
    - "✓ Checked" templates.
    - Renames: big ideas / ý lớn; Weekly Talk / Buổi nói chuyện tuần; free gift / quà; DM reply 1/2; "ask 3 past clients one question".
19. **lint.py:**
    - A coach-visible jargon deny-list (all the never-see terms in §4) scanned over golden-run outputs.
    - The Brand Card visible-part budget.
    - START-block NFC budgets with a hard cap = measured limit − 6%.
    - A "no detour between Start and the stop point" grader.
20. **§3.3 budgets:** replace the rows with:
    - instructions ≤6,500 / ≤7,500
    - phone starter ≤7,500
    - method ≤50 / 55 KB
    - GROW ≤60 KB
    - Brand Card ≤5,000 / 5,800
    - nudge task ≤900
    - Day-0 uploads = 1
    - lifetime sources ≤3
21. **guides:** `start-here.tmpl` becomes `guides/setup-page.tmpl` (mobile-first, device-aware, helper kit, QR, preview, videos, dated). `troubleshooting.tmpl` gains the 8 failure fixes.
22. **§10 phases:**
    - Phase 2 golden runs move to **ChatGPT Free and Claude Free with the Day-0 kit**.
    - Claude Pro + Notion moves to Phase 4 (L3).
    - Phase 7 release gate = §6.
23. **evals/personas:** add `vn/hanh-android-free-nocomputer`, `vn/tuan-multihat-plus`, `en/linda-claude-pro-mac-newsletter` and `evals/acceptance.toml` (§6 thresholds).
24. **platform/targets.toml:** add the unverified entries with `verified_on`:
    - Save-to-project on Free and mobile, and whether it counts toward the file cap.
    - Claude "Add text content" and artifact "Add to project".
    - Project creation on phones.
    - Task creation from a project chat; Free weekday scheduling.
    - Voice mode "acknowledge only".
    - Dictation length limits (VN).
    - Copy-box wrap and diacritics on Android.
    - Chat rename on mobile.
    - Mac dictation inside Claude and ChatGPT.
25. **§11 open decisions to add:**
    - Weekly Talk as the default pillar.
    - Gemini off the main page.
    - VN Zalo group and weekly install session.
    - VN instruction block in Vietnamese.
    - Sheets-first for VN ChatGPT + VA.
    - The side-door piece.

---

## 6. Persona acceptance criteria (release gate; both editions)

**Testers (unaided, real accounts):**
- **EN:**
  - T1: Claude Pro, Mac, LinkedIn + newsletter, 50+.
  - T2: ChatGPT Free, Windows, Instagram-first, 45+.
  - T3: cold start (no offer), ChatGPT Plus, phone-heavy.
- **VN:**
  - T4: ChatGPT Free, Android, no own computer, voice-mode habit, 45+.
  - T5: ChatGPT Plus, laptop + phone, multi-income, impatient.
  - T6: Claude, keyboard mic.
- **Plus:** one helper install over a Zalo screen share.

| Area | Pass condition |
|---|---|
| Install | Door A ≤4 actions, median ≤3 min, max ≤5 min. 100% see the pass-test tag. Door B ≤2 actions, first reply ≤60 s. Helper path ≤10 min including login/OTP, and the helper message is understood with no call |
| Early value | First substantive reply (early win) ≤4 min after the dump starts |
| Message | Map within ≤8 coach turns EN / ≤9 VN, and ≤20 min after Start. The Map passes the 6 message tests |
| First win | Film-ready piece ≤24 min after Start and ≤30 min from opening the purchase email. Stop point ≤27 min. Whole session ≤40 min and ≤12 turns |
| No detours | 0 instructions to download, upload, visit the setup page or switch app between Start and the stop point (transcript grader) |
| No gates | Week 1 is delivered with the Brand Card unsaved (forced test). The save instruction never precedes a reward |
| Memory | ≥5/6 testers have the Brand Card saved as a source by the end of Day 1. 6/6 have a recoverable copy (chat, Zalo Cloud or email). The next chat's self-check reports "Brand Card v1 ✓" |
| Plain language | 0 deny-list terms in coach-visible text. Visible Brand Card ≤900 characters (one phone screen) |
| VN quality | Pronoun applied from reply 2 with 0 slips. Naturalness ≥4/5 (native reviewer). 0 English leakage outside the allowlist. Inline claims guard blocks "cam kết lợi nhuận", "tốt nhất" and unfair comparisons on Day 0 with no method file |
| Voice | Every tester (Mac included) has working dictation ≤1 min after reply 1. Claude VN tester is told to use the keyboard mic in reply 1 or 2 |
| Trust | 6/6 can point to their own story in the first script (✓ line) |
| Recall | Core message repeated from memory the next day: ≥2/3 per edition |
| Return | Day 3: opens the right place and gets today's piece unaided, 6/6 (Door B: ≤1 paste) |
| Weekly | Weeks 2–3 Lean measured ≤60 min. Talk ≤15 min on one device, with no camera and no editing step. Friday works with spoken numbers only (6/6). ≥3 posts in Week 1 by ≥4/6 |
| Automations | ChatGPT testers who say yes have L1 running in ≤2 min, with no "leave the project" contradiction. ChatGPT Plus/Pro only: a task-paused check appears in the Friday review |
| Machine (golden runs) | Running tag ≥98% over 30+ turns on ChatGPT Free (27K) and Claude Free. Day 0 completes with 0 files and with 1 file. Claude Free finishes in one 5-h window or resumes via "next" with no lost answers. Self-check gives the right one-line fix for a missing file, a block pasted into chat, duplicate cards and a missing card (100%). Over 4 simulated weeks: ≥90% on-map, WHY line 100%, keyword exactly once 100%. Hidden Ship Check Edge ≥7 with no zero, 0 RED |
| Scores | Tester averages ≥8 on install, first session and "know what to say"; ≥7 on weekly and trust. No tester below 6 on any dimension |

**Quit-point checklist** (each must be absent or handled):
1. Method file requested mid-session (Hạnh, about minute 40).
2. Door B Day 2 refers to a project that doesn't exist.
3. Save-for-reward gate (Hạnh at minute 33, Tuấn at minute 22).
4. Nothing back during minutes 8–10 of the dump (Tuấn).
5. 12–15 KB brand wall with B1–B7 (Tuấn, Linda).
6. A paid income stream parked with no bridge or side door (Tuấn).
7. "Locked 90 days" wording.
8. "New chat outside the project" (Tuấn).
9. Mac mic not found (Linda).
10. Claude save without a picture route or backup (Linda).
11. Keyword CTA with no quiet option (Linda).
12. Email list ignored (Linda).
13. Two-device Weekly Talk or clip trimming (Hạnh, Linda).
14. FB insights screenshots required (all three).
15. xưng hô asked late (Hạnh).
16. Reading the script while filming on the same phone (Hạnh).
17. Notion-hosted setup page (Hạnh).

---

## 7. Remaining risks

1. **Unverified UI the default paths depend on:**
   - ChatGPT "Save to project" on Free and mobile, and whether it counts toward the cap.
   - Claude "Add text content" and "Add to project".
   - Project creation on phones.
   - The model creating tasks from a project chat; Free weekday scheduling.
   - Chat rename on mobile.

   Every one has a fallback, but if several fail at once, steps and minutes go up. Phase 0 must run before strings are frozen.
2. **Chatting outside the project** cannot be detected by the machine. Mitigated by the running tag, the "Content Machine, newest chat" rule, and reminder wording that names the path.
3. **ChatGPT Free context (about 27K)** with long Vietnamese dictation. In Door B the instructions are the oldest message and fall out of context first. Mitigation: a fresh-box trigger by turn count, and the Brand Card printed before long output. Needs a measured threshold.
4. **The helper path depends on another person.** Waiting 1–2 days loses momentum. Mitigation: "start talking on your phone while you wait" plus move-in.
5. **Door B stays weaker:** one paste per new chat, and memory relies on the coach keeping the box.
6. **Rubber-stamp "OK":** the coach approves a message they don't own. Mitigation: the "why this one" line, the change-a-line option, next-day recall in testing, and the first monthly check after real buyer signals.
7. **The side door versus focus:** multi-income coaches may drift. Mitigation: the off-map counter is shown in the Friday review, and promotion only happens at the monthly check.
8. **Cutting the method file to 50 KB** may lower script quality compared with the 200 KB references. This must be proven by golden runs before release, with GROW and the L3 skill as escape valves.
9. **Voice:** VN dictation cut-offs, accents, and the voice-mode habit (Hạnh). "Acknowledge only" voice mode is untested.
10. **Platform mechanics for the CTA:** personal Facebook profiles and LinkedIn have no DM automation, so replies are manual. Comment-keyword demotion risk remains (founder override; dated note only).
11. **ChatGPT tasks pause silently.** Mitigation: the Friday "did your morning messages arrive?" check (Plus/Pro); nothing depends on tasks.
12. **Support load on the founder:** the VN Zalo group and weekly session. Plus UI drift that makes videos stale, so videos are re-shot and labels re-checked every quarter.
13. **Claims and legal:** insurance, real-estate, health and income niches. VN counsel review is still pending; until then every result claim stays AMBER.
14. **Shared accounts in VN** (memory leaks between people), and Claude Pro needs an international card. Mitigation: the "Project only" memory line, and ChatGPT as the VN default.

### Critical Files for Implementation
- /root/.claude/plans/all-right-so-this-clever-shore.md: record this spec under "#1 PRIORITY: THE EXPERIENCE", along with the founder sign-offs in §5 items 1, 14, 17 and 25.
- /home/user/Content-Machine-1.0/core/start-block.tmpl: the one text for both apps, rendered as the project-instructions and phone-starter variants. It carries the Day-0 engine, self-check, running tag, inline locale rules and claims guard, router, save steps and level-up triggers.
- /home/user/Content-Machine-1.0/modules/setup.md (with modules/message.md, modules/talk.md and modules/levelup.md): the first-session order, early win, stop point, no-gate save, Weekly Talk, and the L0.5–L5 ladder.
- /home/user/Content-Machine-1.0/schemas/brand-card.toml (with strings/en.toml and strings/vn.toml): the Brand Card layout and budgets, and every coach-facing EN/VN line, rename and deny-list term.
- /home/user/Content-Machine-1.0/guides/setup-page.tmpl (with platform/targets.toml and evals/acceptance.toml): the mobile-first setup page and helper kit, the dated Phase-0 facts, and the §6 release thresholds.