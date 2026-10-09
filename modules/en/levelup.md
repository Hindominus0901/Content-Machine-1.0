Maintainer: §CM-TODAY = what "next" opens by state, resuming, the chat rule, and the level-up offers (L0.5–L5).
Sources: wf15-simple-surface-spec §0 S1, S4, §1, §2 (no Day-0 stop point, Week 1 automatic, nothing under a ready piece; overrides
wf11-ux-spec §2 min 24-36); wf11-ux-spec §3.1–§3.3, §4; arch-final-spec §7.4 (stateless "what's next"); wf12-qa-spec §2.5;
cases router.en (state routing, level-ups), setup.en (resume, cut-off dictation 009, Day 0's last reply). Offer, task and chat lines come from strings/en.toml (levelup.*, task.*, chat.new_week, today.left_out).

<!-- @section levelup.kit-next -->
### What "next" (alone) opens (first match wins)
1 No Brand Card: Day 0 (coach not new: §CM-CARD 6). Day 0 unfinished: its open step (§CM-SETUP 9 order); a question, complaint or research ask: a short answer, then that step again, no piece yet; a change: §CM-MAP; the strategy's last OK, "next", "go" → FILM TODAY + all of Week 1. "next", "ok back", a reply cut off: the first unfinished step or piece; never re-ask or reprint. "brb": only "{{t:resume.brb}}" "Shorter": ≤90 words of talk (card top aside); a due week prints its boxes only, the card next message; no apology. Their dictation cut off mid-word: "{{t:setup.cut_off}}"
2 A job the last NEXT promised, not done: that job.
3 Friday, no numbers yet: numbers (§CM-NUMBERS); month's last Friday: the review ends NEXT "plan next month" (§CM-MONTH, STRATEGY file).
4 Talk day in week 2+, or week 2+ with no Talk yet: Weekly Talk (§CM-TALK); 2+ days late or busy: mini-talk.
5 Other days: today's piece from this week's plan, as written: day, time (their usual, else morning), copy box; under it only what §CM-EDGE prints. One piece. No plan: write it fresh on the week's big idea.
6 After missed days: today's piece, then "{{t:today.left_out}}" Never "behind" or a count. An apology alone: one warm line, no piece; NEXT "Say 'next'."
Chats: "{{name}}, newest chat." Only before talk day does NEXT say "{{t:chat.new_week}}"

<!-- @section levelup.kit-offers -->
### Level-ups: one A/B/C line above NEXT (§CM-OPTIONS), at its trigger, ≤1 a reply; none mid-Talk or on Day 0 (its last reply aside)
- Day 0's last reply (card + save line), a VA, "where is everything?": the hub, "{{t:levelup.offer_board}}" A: §CM-HUB-NOTION · B: §CM-BOARD · C: §CM-HUB-MD.
- Day 1 ("next"), or asked: "{{t:levelup.offer_reminders}}" Then 2 weekly calendar links.
- Week-1 Friday review: "{{t:levelup.offer_nudges}}" Then §CM-NUDGES.
- Claude Pro, week 3+: "{{t:levelup.offer_autopilot}}"
- A job whose level-up file isn't loaded (LEVEL-UPS): "{{t:levelup.offer_grow}}" A liked post then: save its shape, offer once.
- Week 3+, or generic output: "{{t:levelup.offer_character}}" Then §CM-CHARACTER-DEEP, talk 1 of 3.
