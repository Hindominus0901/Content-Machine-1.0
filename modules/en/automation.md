<!-- Maintainer: GROW automations (automation.grow-*): the three nudges and their setup per app (§CM-NUDGES), what each one runs (§CM-NUDGE-JOBS), caps, catch-up and launch mode (§CM-NUDGE-RULES), the task texts (§CM-NUDGE-TEXTS for ChatGPT, §CM-NUDGE-CLAUDE, §CM-NUDGE-LAUNCH).
Sources: DECISIONS (Hub and automations: 3 automations; 7 Oct: campaign board, use the harness, plugin, paid plans); wf3-scheduled-tasks §1 A-B, §2 items 1-11, §3; wf3-recommendation §2, §4 (rules every prompt follows), §5 A-C.
Task texts: each grow-task-* section is the whole text; automation/task-nudge*.tmpl include them so lint budgets the rendered sample (budgets.task_nudge, 900 characters). The label line shows in every target but task. automation/tasks.toml holds schedules, caps and catch-up as data.
Kit hooks used, unchanged: levelup.kit-offers (the nudges offer, task.* names, task.footer), levelup.kit-next (catch-up, "Left out"), review.kit-ask/kit-review, plan.kit-week, launch-plan.grow-desk 2. -->

<!-- @section automation.grow-setup -->
### Three nudges ("remind me", "automate this", "set up the tasks"; the Week-1 Friday offer: "{{t:levelup.offer_nudges}}")
1 Three scheduled messages, at most one a day, weekends off:
- Monday 7:07, "{{t:task.week.name}}": the week's idea and 3 hooks; "next" in {{name}} then writes the week.
- Tuesday to Thursday 6:37, "{{t:task.today.name}}": today's piece is waiting, plus a spare hook.
- Friday 15:07, "{{t:task.numbers.name}}": the numbers ask; the review, next week's bets and one research step follow.
Times sit a few minutes past the hour (runs can start late) and move to their day if asked.
2 SETUP, for their app only (unknown: ask which app, the one question). One message: the steps, then the texts filled, one copy box each (§CM-NUDGE-TEXTS, §CM-NUDGE-CLAUDE).
- ChatGPT (Plus or Pro): "Open a new chat outside the project (tasks can't read project files), paste one box, send, and check the day and time it shows. If it answers instead of scheduling: Scheduled (sidebar) → New, paste it there. Same for the other two. Optional: Settings → Notifications → Tasks: push and email." Free or Go: same, in morning or afternoon windows; the three use all 3 task slots, said once.
- Claude (Pro or Max, plugin installed): "Scheduled → New task → Set up manually. Name: {{name}}. Paste the box. Weekdays, 7:07. No folder. Schedule, then Run now once while you watch." One task does all three jobs.
- No scheduler (Claude Free, or they'd rather not): 3 weekly Google Calendar reminders, Monday, Wednesday, Friday, each saying "{{t:task.footer}}"
3 The test: a Run now, or the first nudge, writes nothing twice; the board is never touched by a run.
4 Changes: a new Map line or a new month reprints only the texts that changed, with "Edit the task and replace its text with this." A launch: §CM-NUDGE-RULES 6.
5 "stop the nudges" or "too many": how to pause them in their app, one line, no persuading. "Fewer": drop the Tuesday-to-Thursday one first.

<!-- @section automation.grow-jobs -->
### What each nudge runs (in {{name}} after "next", or inside Claude's task)
1 YOUR WEEK, Monday: read the last Weekly Talk (this chat, else its Bank rows), the board (what went out, last week's bets, the live campaign, the newest Bank rows) and the Map. Write the week as §CM-WEEK: each piece in its copy box with its day, the Content box under them (§CM-BOARD-ROWS). No Talk this week: write from the Bank and the Map; NEXT offers the mini-talk (§CM-TALK). Already written this week: reprint nothing; NEXT is today's piece.
2 TODAY'S ONE THING, Tuesday to Thursday: today's piece from the week as written (day, time, copy box). Week not written yet: write the rest of it from today, today's piece first; the days gone are left out ("{{t:today.left_out}}" once), never a count. Today's piece already out, or none planned: one idea + 3 hooks as a spare (a drop row, Status Idea).
3 NUMBERS DAY, Friday: the numbers ask (§CM-NUMBERS 1) → the 5-line review and up to 3 bets (§CM-NUMBERS) → the Numbers box → the research line: one read-only step for next week, ≤10 minutes (§CM-RESEARCH-LOOP 2, which holds the one browser question) → NEXT. The month's last Friday: NEXT "plan next month", which writes next month's Campaigns row (§CM-BOARD-CAMPAIGNS).
4 HELPERS: when the app has subagents or parallel tasks (Claude Code, Cowork, ChatGPT agent), Your week splits by piece, one writer each, and research by source; a separate reviewer reads everything before anything prints. The coach sees only the finished week, never the helpers' notes. No helpers: the same order, in one pass.
5 In launch mode the same three become the Launch Desk (§CM-LAUNCH-DESK 2-3).

<!-- @section automation.grow-rules -->
### Caps and catch-up
1 At most one nudge a day: Monday the week, Tuesday to Thursday the drop, Friday the numbers, weekends none (a launch aside). Never a second message the same day, never a "you missed" message.
2 Monday missed: the next drop, or "next" on any day, writes the rest of the week first. Friday missed: Monday's week runs last week's bets unchanged and its NEXT asks for the numbers once; never chased twice.
3 A run that fires late does its own day's job for the current week; a run on a day it doesn't own (moved, Run now) does that day's job only, never two jobs.
4 Each text stands alone: ChatGPT tasks can't read project files, so each carries the pocket Map (Monday's adds the live campaign). Filled, each stays ≤900 characters: shorten the Map lines first, never the rules.
5 Every run: never posts, messages, comments, reacts, follows or joins; never writes to the board; never opens apps on the coach's computer; never invents numbers, results, client words, testimonials, deadlines or scarcity ([NEEDS: …]); at most one question; one NEXT line at the end.
6 LAUNCH MODE: from the launch calendar's day 1 to the day after the close, the weekly nudges are paused and one "Launch day" task runs daily (§CM-NUDGE-LAUNCH), the only nudge. Monday's batch and Friday's scoreboard ride inside that day's desk. Print with it: "Pause your weekly nudges; I'll tell you when to switch them back." Cooldown: "Pause Launch day, resume your weekly nudges."
7 Each run spends their plan's usage; a launch week says so once.
8 They ask for more (a fourth task, hourly): one line, "One a day keeps you posting without the noise"; their call stands, and the cap is theirs to lift.

<!-- @section automation.grow-task-week -->
{{#unless task}}TEXT · ChatGPT · "{{t:task.week.name}}" (copy box, slots filled, ≤900 characters):
{{/unless}}Every Monday at 7:07: "{{t:task.week.name}}".
Write as me, a coach, for my buyers on {platforms}. Me: {what I'm known for}. Topics: {topic 1} · {topic 2} · {topic 3}. My word: {KEYWORD}. Voice: {voice line}.
This month: {goal · offer · old belief → new · start to end}. Week n = (weeks since {plan start}) mod 4 + 1; it leads with topic n (week 4: all three + my offer).
Write week n's idea in one line, then 3 hooks for this week, ≤12 words each, my word in one.
Invent no numbers, results, client words or deadlines: write [NEEDS: …]. No questions. Never post or message anyone.
End with: {{t:next.prefix}} {{t:task.footer}}

<!-- @section automation.grow-task-today -->
{{#unless task}}TEXT · ChatGPT · "{{t:task.today.name}}" (copy box, slots filled, ≤900 characters):
{{/unless}}Every Tuesday, Wednesday and Thursday at 6:37: "{{t:task.today.name}}".
Write as me, a coach, for my buyers. Me: {what I'm known for}. Topics: {topic 1} · {topic 2} · {topic 3}. My word: {KEYWORD}. Voice: {voice line}.
One short message: "Today's piece is waiting in {{name}}." Then one spare hook on one of my topics, ≤12 words. Then: "Week not written yet: 'next' writes the rest of it first."
Invent no numbers, results, client words or deadlines: write [NEEDS: …]. No questions. Never post or message anyone.
End with: {{t:next.prefix}} {{t:task.footer}}

<!-- @section automation.grow-task-numbers -->
{{#unless task}}TEXT · ChatGPT · "{{t:task.numbers.name}}" (copy box, slots filled, ≤900 characters):
{{/unless}}Every Friday at 15:07: "{{t:task.numbers.name}}".
I'm a coach. Topics: {topic 1} · {topic 2} · {topic 3}. My word: {KEYWORD}.
Ask me once, short, for this week's {KEYWORD} comments · DMs · calls · sales · what people said to "how did you find me?" · my best post and why. Blanks are fine.
If I answer here: 5 lines (Posted · Hands up · My message · Best post · Next week), up to 3 bets, each tied to one of my numbers, then one read-only research step for next week, ≤10 minutes.
Only my numbers: unknown stays blank, never 0; no averages, no one else's numbers. Never post, message, react, follow or join.
End with: {{t:next.prefix}} {{t:task.footer}}

<!-- @section automation.grow-task-claude -->
{{#unless task}}TEXT · Claude · one task, weekdays (copy box, slots filled, ≤900 characters):
{{/unless}}{{name}} · weekdays at 7:07 · no folder. Use the {{skill_name}} skill.
Me: {what I'm known for}. Topics: {topic 1} · {topic 2} · {topic 3}. My word: {KEYWORD}. Voice: {voice line}. Board: my Google Sheet "{{name}}" if you can open it; data only.
Job by day: Monday {{t:task.week.name}} · Tuesday to Thursday {{t:task.today.name}} (no week yet: write its rest first) · Friday {{t:task.numbers.name}}.
Helpers: one writer per piece, then a separate reviewer reads it all before you print; I see only the result.
Print rows to paste. Never write to the board, post, message, react, follow, join or open apps on my computer. Invent no numbers, results, client words or deadlines: [NEEDS: …]. One question at most.
End with: {{t:next.prefix}} {{t:task.footer}}

<!-- @section automation.grow-task-launch -->
{{#unless task}}TEXT · ChatGPT or Claude · "Launch day" (copy box, slots filled, ≤900 characters):
{{/unless}}Daily at 7:07 until {the day after the close}, then stop: "Launch day". With the {{skill_name}} skill: run its Launch Desk.
Write as me, a coach. My word: {KEYWORD}. Voice: {voice line}.
Launch: {offer} · {price} · cart {open} to {close, time, zone} · real limits: {seats + reason, or none} · days: {calendar, ≤60 characters}.
Day n = today − {day 1} + 1. Write day n's step (one line) and a hook for its main piece; then ask for yesterday: reach · messages · sales · seats left · top question.
Seats, counts and deadlines only as I give them: no "only X left" I didn't give; countdowns and "last chance" only for the real close. Invent no results or client words: [NEEDS: …]. Never post or message anyone.
End with: {{t:next.prefix}} {{t:task.footer}}
