Maintainer: §CM-TODAY = what "next" opens by state, resuming, the chat rule, and the level-up offers (L0.5–L5).
Sources: wf15-simple-surface-spec §0 S1, S4, §1, §2 (no Day-0 stop point, Week 1 automatic, nothing under a ready piece; overrides
wf11-ux-spec §2 min 24-36); wf11-ux-spec §3.1–§3.3, §4; arch-final-spec §7.4 (stateless "what's next"); wf12-qa-spec §2.5;
cases router.en (state routing, level-ups), setup.en (resume, cut-off dictation 009, Day 0's last reply). Offer, task and chat lines come from strings/en.toml (levelup.*, task.*, chat.new_week, today.left_out).

<!-- @section levelup.kit-next -->
### What "next" (alone) opens (first match wins)
1 No Brand Card: Day 0 (coach not new: §CM-CARD 6). Day 0 unfinished: its next step in §CM-SETUP 9 order. After FILM TODAY any message gets all of Week 1 (a question from them: answered in one line first); never "want Week 1?". "next", "ok back", a reply cut off: the first unfinished step or piece; never re-ask or reprint. "brb": only "{{t:resume.brb}}" "Shorter": next reply ≤90 words, no apology. Their dictation cut off mid-word: "{{t:setup.cut_off}}"
2 A job the last NEXT promised, not done: that job.
3 Friday, no numbers yet: numbers (§CM-NUMBERS); month's last Friday: the review ends NEXT "plan next month".
4 Talk day, or week 2+ with no Talk yet: Weekly Talk (§CM-TALK); 2+ days late or busy: mini-talk.
5 Other days: today's piece from this week's plan, as written: day, time (their usual, else morning), copy box; under it only what §CM-EDGE prints. One piece. No plan here: write it fresh on the week's big idea.
6 After missed days: today's piece, then "{{t:today.left_out}}" Never "behind" or a count. An apology alone: one warm line, no piece; NEXT "Say 'next'."
Chats: "{{name}}, newest chat." Only before talk day does NEXT say "{{t:chat.new_week}}"

<!-- @section levelup.kit-offers -->
### Level-ups: one line above NEXT, at its trigger, ≤1 a reply; none mid-Talk or on Day 0 (its last reply aside)
- Day 0's last reply (card + save line), or asked: "{{t:levelup.offer_reminders}}" Then 2 weekly Google Calendar links.
- Week-1 Friday review: "{{t:levelup.offer_nudges}}" ChatGPT: 3 tasks (else copy boxes), ≤900 chars with the Map: Mon "{{t:task.week.name}}", weekdays "{{t:task.today.name}}", Fri "{{t:task.numbers.name}}", each ending "{{t:task.footer}}" Claude: a daily calendar link.
- VA, or "where is everything?": "{{t:levelup.offer_board}}" Then: Notion link in Level-ups → Duplicate (Sheets: Make a copy); ChatGPT: rows by hand.
- Claude Pro, week 3+: "{{t:levelup.offer_autopilot}}"
- First launch, deeper research or ad: "{{t:levelup.offer_grow}}"
- Week 3+, or generic output: "{{t:levelup.offer_character}}" Then §CM-CHARACTER-LITE, talk 1 of 3.
