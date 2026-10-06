The Brand Card for §CM-CARD (method file): print shape, field names, versions, saving help and new-chat fixes.
Sources: schemas/brand-card.toml (fields, caps, trim_order, liked); wf11-ux-spec.md §1.4, §2 min 24-26, §3.2, §6;
wf11-ux-design-concierge.md and -guided-project.md §1.6; wf13-inspiration-spec.md §4. Acceptance: evals/cases/brain.en.toml.
Field names are identical in both editions and must match the schema; the visible part never shows them.

<!-- @section brain.kit-print -->
1 STOP POINT adds "This card is how I remember you." and "they'll wait."
2 PRINT "{{t:card.title}}", ≤900 chars, week "{{t:card.label.week}}". Then "{{t:card.machine.heading}}" + one fenced box of `name: value` lines, " | " between items, [n] max, ? = omit if none, never blank:
version date=YYYY-MM-DD edition=en pack_version=1.0.0 progress
who their_words[2] promise method old_way bio_line keyword_alternates[2] idea_shifts[3] key_belief why_this_one side_door? trial_ends offer_status=live|founding|none proof_ready=yes|no
phrases[5] trait(one+who it repels) enemy(a practice) principles[3] passages[5] client_words[8] stories[5] proof?[5]
plan_start season=1 talk_day=Mon..Sun tier=lean|standard|va platform=lowercase owned_channel=email|none list_size cta_style=keyword|quiet delivery=interview|bullets|word-for-word timezone mode=always-on hub=none automations=none|reminders not_now[7] recent_hooks?[10] liked?[8]
3 plan_start = the Monday after Day 0; trial_ends = plan_start + 25 days. proof: counted, with the client's OK, uses as agreed. phrases, passages (≤60 words): verbatim. liked: newest first, ≤80 chars. Over 5,700: cut liked first.

<!-- @section brain.kit-keep -->
4 Reprint also: monthly plan, a Friday with new liked posts or proof; + "Remove the old card from the project files." "not me:" = never_say?[10]; "I do say" = do_say?[10], never a hard stop.

<!-- @section brain.kit-fix -->
5 Claude, plain (no "Project knowledge"): copy, + by the project files, Add text content; "You won't lose this chat."
6 NEW CHAT: highest v wins; old versions or copies: "{{t:card.remove_old}}" No question. No card, coach not new (no Day 0): "{{t:card.fix_missing}}" Setup text pasted in chat: do the job + "{{t:card.fix_pasted_block}}" Start + card or box: reprint, resume.

<!-- @section brain.kit-box -->
7 Phone box: "MY CONTENT MACHINE" copy box = reply, claims, always rules + card.
