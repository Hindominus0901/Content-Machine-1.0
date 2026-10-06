The Brand Card for §CM-CARD (method file): print shape, field names, versions, saving help and new-chat fixes.
Sources: wf15-simple-surface-spec.md §0 S3-S4, §1.7 (short visible top, one save line, no stop point; overrides wf11-ux-spec §2
min 24-26); wf14-voice-language-spec.md §1-§3 (WHAT YOU SAY / HOW YOU SAY IT, Voice Card fields); schemas/brand-card.toml
(fields, caps, trim_order, liked); wf11-ux-spec.md §1.4, §3.2, §6; wf13-inspiration-spec.md §4. Acceptance: evals/cases/brain.en.toml.
Field names are identical in both editions and must match the schema; the visible top never shows them. VN adds pronouns, dialect.

<!-- @section brain.kit-print -->
1 WHEN: Day 0, after Week 1 (§CM-SETUP 9); reprints: 4. Coach-facing: one save line, "{{t:card.save_line}}" + the app's route (start-block); it never blocks.
2 TOP, ≤500 chars, 3 lines: "{{t:card.title}}" · "{{t:card.visible.what}} {message} · {3 topics} · "{word}"" · "{{t:card.visible.how}} {tone} · {rhythm} · "{phrase}", "{phrase}" · {{t:card.visible.to_them}} "{address}"", + · {{t:card.visible.never}} "{word}" after a "{{t:cmd.not_me}}". Over 500: shorten the message, never the voice line.
3 Then "{{t:card.machine.heading}}" + one fenced box of `name: value` lines, " | " between items, [n] max, ? = omit if none, never blank:
version date=YYYY-MM-DD edition=en pack_version=1.0.0 progress
who their_words[2] promise method old_way offer bio_line keyword_alternates[2] idea_shifts[3] key_belief why_this_one side_door? trial_ends offer_status=live|founding|none proof_ready=yes|no not_now[7]
tone rhythm phrases[5] openers_closers?[3] audience_address code_mix humour=none|dry|playful|self-roast written_vs_spoken? never_say?[10] do_say?[10]
trait(one+who it repels) enemy(a practice) principles[3] passages[5] client_words[8] stories[5] proof?[5]
plan_start season=1 talk_day=Mon..Sun week tier=lean|standard platform=lowercase owned_channel=email|none list_size cta_style=keyword|quiet delivery=beat-cards|interview|bullets|word-for-word timezone=ask|{zone} mode=always-on hub=none automations=none|reminders recent_hooks?[10] liked?[8]
plan_start = the day after Day 0; week n = 7-day blocks from it; trial_ends = plan_start + 25 days. proof: counted, with the client's OK, uses as agreed. phrases, passages (≤60 words): verbatim. audience_address: how they address buyers (you, y'all, friend), not how I address them. code_mix: their jargon level. written_vs_spoken: only from pasted posts. liked: newest first, ≤80 chars. Over 5,700: trim liked first; voice fields last.

<!-- @section brain.kit-keep -->
4 Reprint also: monthly plan, a Friday with new liked posts or proof; + "{{t:month.save_card}}" never_say, do_say: §CM-VOICE 6. A Talk's new phrases and openers ride the next reprint.

<!-- @section brain.kit-fix -->
5 Claude, saving: "{{t:save.claude_plain}}"
6 NEW CHAT: highest v wins; old or extra copies: "{{t:card.remove_old}}" No question. No card, coach not new (no Day 0): "{{t:card.fix_missing}}" Setup text pasted: do the job + "{{t:card.fix_pasted_block}}" Start + card or box: reprint, resume.

<!-- @section brain.kit-box -->
7 Phone box: "MY CONTENT MACHINE" copy box = reply, claims, always rules + card.
