# UX walkthrough as Chị Hạnh: 45, spa owner who also coaches other spa owners, Hà Nội, ChatGPT Free on Android, uses voice

**Assumptions I played with:**
- The purchase link reaches her by Gmail and by a Zalo message from the seller.
- When she says "voice" she means the sound-wave voice mode, not the small dictation mic.
- She answers every question with a 3–5 minute story.
- Staff or customers interrupt her every 20–30 minutes.
- She has no computer of her own. The spa's reception PC is used by her receptionist, Linh.

**Problems that hit all three designs:**
- **Projects on Android.** All three designs mark it [UNVERIFIED] whether projects can be created on a phone. My recollection is that OpenAI's September 2025 rollout of Projects to Free accounts named web and Android. If that holds, Door A works on her phone, and that would be the biggest single improvement. This needs a hands-on test.
- **"⋯ → Save to project".** Saving a single message into the project is unverified in every design, and two of them depend on it.
- **The voice button.** All three tell her to tap the small mic and not the sound wave. She will tap the wave out of habit, and the AI will start talking over her stories.
- **One phone.** She cannot read a script on the same phone that is filming her, and she cannot film and dictate at the same time.
- **Long chats on Free.** The ChatGPT Free context is about 27K. 15–20 minutes of Vietnamese dictation, plus a pasted START block, plus the Map and Week 1, gets close to that limit. In a phone chat (Door B) the instructions are the oldest message, so they are the first thing that falls out of context.

---

## Design 1: zero-setup

**Walkthrough.** The page detects Android and sends her to Door B automatically.
1. She taps Copy, switches to ChatGPT, long-presses, taps Dán and sees a 7,500-character bubble full of §0, §1, "NEXT →" and English labels.
   - Her reaction: "Ủa, sao dài thế, chị dán nhầm à?" She hesitates about a minute, then sends it.
2. "bấm micro trong ô tin nhắn (không phải nút sóng âm)": she taps the wave anyway and voice mode answers her after a pause. On her second try she dictates for 9 minutes straight.
   - If the transcription fails or gets cut off, she loses 9 minutes of talking, and that is **rage risk #1**. If it works, the "Chị chưa nhắc đến…" prompts feel like talking with a junior staff member. She likes it.
3. The inventory message ("Chị biết rất nhiều… đủ 6 tháng nội dung… không bỏ đi thứ gì") is the moment she feels understood.
4. On the pre-filled check she answers with stories instead of "sửa 3". That's fine as long as the machine copes.
5. The Map arrives around minute 30 at her pace. "3 Ý LỚN" is clear to her. She screenshots the pocket version and sends it to Zalo "Cloud của tôi" on her own.
6. FILM TODAY: "đọc trên màn hình" is impossible, because the script is on the phone that is filming. She memorizes the 3 beats and does about 4 takes, roughly 15 minutes.
   - A caption inside a copy box on Android may not wrap. This needs a test.
7. The xưng hô question comes at minutes 24–26. For 25 minutes before that the machine has been calling her "bạn", and she has noticed.
8. Saving the Brand Card on Door B means nothing to do (a memory note). That part is good.
9. **Minutes 29–30: "Thêm file phương pháp… để viết tuần 1".** She has to download a .md in Chrome, then in ChatGPT tap + → Tệp → find the Downloads folder. She has never attached a file. **This is the first quit point, around minute 40 at her pace:** "thôi để mai."
10. **Day 2:** the NEXT line says "Monday: open Content Machine, NEW chat, say 'next'". She has no project called Content Machine. In a new chat, "tiếp" gets a generic ChatGPT answer. **This is the second quit point.**
    - If she instead finds the old chat (its title is auto-generated), the long-chat problem above kicks in, and the ◆ tag disappears.
    - Door B contradicts itself: "new week = new chat" breaks it, and "same chat forever" overflows it.
11. The weekly loop is the best of the three for her. The Monday interview is a 10-minute talk on one device, which plays to her strength. Friday numbers by voice are easy for her: "được 9 chị comment, 2 chị nhắn, 1 chị đặt lịch".
    - The reminder tasks say "open Content Machine", which again doesn't exist on Door B.

**What she skips:** the method file, notifications and calendar, "make it permanent" (it stays queued forever because she is never at a computer), and Notion. She would actually do the Buyer Mirror, because it goes out on Zalo and she loves her clients. She films 1 of the 3 shorts.

**When she quits:** most likely around minute 40 at the file step. If she gets past it, on days 2–4 at the "new chat" mismatch.

**Time:** about 3 minutes of setup, 45–50 minutes of session and 15 minutes of filming on Day 0. Week 1 is about 2.5 hours if she survives.

**Does she know what to say?** Yes. She has her one sentence by about minute 30, the fastest of the three. **Does she know what to post this week?** Only if she gets past the file step.

**Will it bring clients?** Small signals in Week 1 if she posts 3 or more times: keyword comments from spa owners and 1–2 DMs. Real clients would come in weeks 3–6, but only if the Day-2 continuity problem is fixed.

**Scores:** install 8 · first session 8 · weekly 5 (7 if she had a real project) · "I finally know what to say" 8 · trust 6

---

## Design 2: guided-project

**Walkthrough:**
1. The setup page is a Notion public page. On Android it shows "Open in app" and "Try Notion" banners.
   - Her reaction: "Notion là gì, phải cài app à?" She loses 1–2 minutes and may install the Notion app by mistake.
2. Q1: ChatGPT ("Khuyên dùng"). Q2: "Đang ở máy tính?" → Không → Door B. She gets the same wall of text as Design 1.
   - xưng hô is folded into line 7 of the check at about minute 13. That is better than Design 1, but still late.
3. **The save gate:** "Bấm ⋯ → Lưu vào dự án… gõ 'đã lưu', mình đưa kịch bản đầu tiên". On Door B there is no project, and the design doesn't say whether the gate is skipped. If it fires, she is stuck. **This is the first quit point, around minute 33.**
4. MY BRAND is up to 15 KB in Vietnamese, which is 8–10 phone screens. It ends with "Phần dành cho máy" containing B1–B7, the Big Domino and focus scores.
   - Her reaction: "Cái này lỗi à?" Her trust drops, and the file uses up about 5–7K of her Free context.
5. FILM TODAY carries "✓ Đã kiểm: … dùng chuyện spa 2018 …". **This is the best trust line in any of the three designs.** She sees her own story in it and believes the script is hers.
6. Then: "permanent in 3 minutes on a computer". **Season 1 and Week 1 are held back until she moves in on a computer.** She has one short and no plan. **This is the second quit point, on days 1–2.**
7. The Weekly Talk is "phone on a stack of books… tap the mic on your computer". That needs two devices, and the phone-only variant needs a laptop camera. She can't do it. Trimming clips herself won't happen either.
8. She is asked to keep separate Week, Talk and Month chats, and to give her Friday numbers "In Monday's chat". She will lose track of which chat is which.
9. The automation setup says "new chat OUTSIDE the project". That contradicts the "always open the project" rule she was just taught.

**What she skips:** the Notion detour, calendar links, the Grow file, reading MY BRAND, and the filmed Talk.

**When she quits:** around minute 33 if the save gate fires, otherwise on days 1–2 because Week 1 never arrives.

**Time:** about 45 minutes on Day 0 for 1 short. If Linh moves her in on day 3, about 1 hour that week for 2–4 posts.

**Does she know what to say?** Yes (8). **Does she know what to post this week?** No, not on Door B.

**Will it bring clients?** Unlikely in Week 1 with only 1–2 posts.

**Scores:** install 6 · first session 6 · weekly 3 · "I finally know what to say" 8 · trust 7

---

## Design 3: concierge

**Walkthrough:**
1. The page asks only which app she uses → ChatGPT. It then shows 4 computer steps. Because it doesn't detect her phone, she reads the computer steps first, about a minute of confusion.
2. She finds "Nhờ người cài giúp" and forwards the Vietnamese helper message on Zalo to Linh or her daughter. **This is the most natural action in the whole test**: asking someone for help ("nhờ") is how she solves every tech problem. The UltraViewer mention fits, and she can read the login code out to Linh.
3. **Risk: waiting for the helper.** If Linh is busy, setup slips 1–2 days and her excitement fades. The page should push "start talking on your phone while you wait" more strongly.
4. After setup, "Pick up your phone, open this chat" depends on projects showing up in the Android app [unverified].
5. The stop point ("Hôm nay vậy là đủ… gõ 'tiếp'") gives her permission to stop. She will probably say "tiếp" because she's excited.
6. **The save step happens on the computer:** "No button? save it next time at the computer". The PC is downstairs and she never goes back, so the Brand Card is never saved and the self-check nags her in every chat. The helper's job should include saving it after her session.
7. One rule ("Content Machine, newest chat") is much simpler than Design 2's three chat types. The VN Weekly Talk in voice mode matches her habit, needs one device, and the shorts are re-filmed rather than edited.
8. Friday needs 3 insight screenshots. A personal Facebook profile without professional mode doesn't show insights, so she won't find them. Voice numbers would work better.
9. **Phone-only path:** every session needs two pastes from two places, the Continue prompt from the setup page and the Brand Card from Zalo Cloud. She quits on day 2.
10. The footer "Cần bạn: không" still says "bạn". The Zalo "cài cùng nhau" group is what VN course buyers expect, and she would join it.

**When she quits:** on the helper path, no early quit. The risks are the wait for the helper and the unsaved Brand Card. On the phone-only path, day 2.

**Time:** about 1 minute to forward the message, 5–10 minutes with Linh (login and OTP), a 45-minute session and 15 minutes of filming, so roughly 65 minutes on Day 0. Week 1 is another 70–80 minutes.

**Does she know what to say?** Yes (8). **Does she know what to post this week?** Yes, if she says "tiếp" at the stop point.

**Will it bring clients?** Keyword comments, DMs moved to Zalo, and first booked calls in weeks 2–4.

**Scores:** install 7 (9 if the helper does it the same day, 5 on phone only) · first session 8 · weekly 6 (7 helper path, 3 phone-only) · "I finally know what to say" 8 · trust 7

---

## Score summary
| Design | Install | 1st session | Weekly | Know what to say | Trust |
|---|---|---|---|---|---|
| zero-setup | 8 | 8 | 5 | 8 | 6 |
| guided-project | 6 | 6 | 3 | 8 | 7 |
| concierge | 7 | 8 | 6 | 8 | 7 |

## Which design she would buy
She would buy **concierge**. "Có người cài giúp, có nhóm Zalo để hỏi" is what gets a 45-year-old Vietnamese spa owner to pay.

The experience she would actually succeed with is a merge: concierge's helper-built project, plus zero-setup's phone-first start, its 10-minute chat interview and its voice numbers on Friday. She would not buy guided-project.

## The 5 most important fixes, merged across designs
1. **Make the phone the main device, not the fallback.**
   - First hands-on test: can ChatGPT Free on Android create a Project, take pasted instructions and a file, and does "Save to project" exist there? If yes, Door A is 3 actions on the phone.
   - If no: use the helper path (the Zalo message, with "save the Brand Card after the session" added to the helper's job).
   - Door B must never mention a project that doesn't exist and never need two pastes. Make the Brand Card self-starting: a short START block plus the card in one text kept in Zalo Cloud, so one paste restores everything. When the chat gets long, the machine prints a fresh copy to paste into a new chat.
2. **Nothing between "OK" on the Map and Week 1.** No upload, no save and no computer step in that stretch.
   - The starter block carries the Day-0 steps and a lite Week-1 writer. This is concierge's "Day 0 works with zero files".
   - Offer saving only after Week 1 is in her hands, and never let it block anything.
   - Remove guided-project's save-for-reward gate and its Door B rule that holds back Week 1.
3. **Fit the voice habits she already has.**
   - Let her do the brain-dump in voice mode with the AI only acknowledging ("Dạ, chị kể tiếp ạ"); this needs testing. Otherwise show one Android screenshot that points to the small mic.
   - Ask her to send after each story ("kể xong một chuyện thì bấm gửi") and handle failed transcriptions.
   - Use chị–em from the very first message.
   - Friday numbers by voice. The Weekly Talk is audio-only on one device.
   - For filming, use the CapCut teleprompter or a 3-beat card she memorizes. Never "read from the screen" on the filming phone, and never require two devices.
4. **Keep everything she reads short and in Vietnamese.**
   - The starter opens with "Chị chỉ cần bấm Gửi. Phần dưới là hướng dẫn cho máy, chị không cần đọc."
   - No §, English, IDs or B1–B7 anywhere she can see them.
   - The Brand Card shows about one phone screen to her, with a compact part for the machine.
   - One piece per reply.
   - Test that caption boxes wrap and copy correctly with Vietnamese diacritics on Android.
   - Keep zero-setup's "3 Ý LỚN" naming and guided-project's "✓ Đã kiểm: … dùng chuyện spa 2018" line.
5. **Run Vietnamese support and the sales path through Zalo.**
   - The setup page should be a plain mobile web page, not a Notion page, with Android screenshots, "Gửi vào Zalo của tôi" buttons and the "Nhờ người cài giúp" message.
   - A buyers' Zalo group with a weekly "cài cùng nhau" session.
   - The keyword CTA should route comments → Messenger → Zalo, with a voice-note follow-up, because sales close on Zalo in Vietnam.
   - Reminder tasks should be worded so they work with or without a project.

**Extra hands-on tests for Phase 0** (add an "Android + Free + no computer + voice-mode habit" tester to the release gate):
- Creating a project and using Save-to-project on Android Free.
- Maximum dictation length in Vietnamese, and what happens when it fails.
- Whether voice mode follows an "only acknowledge" rule.
- Whether ChatGPT Free switches to a weaker model after a number of messages, causing a mid-session quality drop.
- Whether the START message survives about 40 minutes of Vietnamese dictation in one chat.
- Whether code blocks wrap on Android.

### Critical Files for Implementation
These are the planned paths named in the designs; most do not exist yet (the repo has only a placeholder file).
- /root/.claude/plans/all-right-so-this-clever-shore.md
- /home/user/Content-Machine-1.0/core/project-instructions.tmpl (the one starter/instruction block, carrying the Day-0 steps and the lite Week-1 writer)
- /home/user/Content-Machine-1.0/schemas/brand-card.toml (the self-starting Brand Card)
- /home/user/Content-Machine-1.0/strings/vn.toml (xưng hô from message 1, "3 Ý LỚN", the "✓ Đã kiểm" line, the starter's opening line)
- /home/user/Content-Machine-1.0/guides/setup-page.tmpl (mobile-first page, the helper Zalo message, Zalo send buttons)