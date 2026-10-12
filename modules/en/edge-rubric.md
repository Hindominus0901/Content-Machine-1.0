Maintainer: §CM-EDGE = how the Ship Check runs and what prints per piece state (the card itself is core/en/ship-check.md, never repeated here).
Sources: wf15-simple-surface-spec §2-§3 (what prints per state; WHY, checks and the record only on "why?"; I3 at most one status line, none for Ready); wf12-qa-spec §0-§2.6 (§2.4 superseded where wf15 differs); wf6-character-design §B5-§B6 (Edge v2, gates, detector, Flip it); qa/standards/shared.md, micro.md;
PLAN reconciliations 2-3, 8, defaults 1, 5; DECISIONS (6 Oct: simple outside, rigorous inside). Acceptance: evals/cases/edge-rubric.en.toml.
K V A Au C, gate names and "Edge" are internal labels: never printed, "why?" included (v13.4: it prints the WHY line and how the piece is built). Claims class → §CM-GUARDRAILS. Voice → §CM-VOICE.

<!-- @section edge-rubric.kit-run -->
CLASS: Ideas (options, plan rows): weak ones dropped silently, no ranks. Micro (under {{micro_threshold}} words): no score, a freebie lead is fine; truth, claims, polarity, length, real gift. Claims (results, money, prices, client words, urgency): + §CM-GUARDRAILS.
SCORE 0-2: K keyword or buyer words in hook or punch line · V the idea by line 2, usable today · A proof by each claim; others' outcomes only as their record · Au a detail only they have · C a stance: their enemy, old view refuted, a not-for line; "both work" = 1. Stance formats (stance, old vs new way, quiet truth, not for you) need C 2. No card here: Au, C max 1; ask once to paste it.
GATES. Polarity: heat on practices, never people ("coaches are frauds" → "programs skip X"), same heat. Truth: an off-record edit → the real figure. Voice (§CM-VOICE): hook ≤{{hook_max}} words, no hedge in hook or claims, sentences ~15 words, none over 25, one ≤5; questions: a hook the last line answers, a real quote, the CTA. Fix, never refuse.
BORROWED: money, freebie or résumé as the whole hook, no why by line 3 → C 0, Draft. Flip: lead with the choice or story.
READY: gates, ≥8, no 0, no [NEEDS]; never "Ready after". Not Ready → one silent fix of the named defects only (≤5; polarity; borrowed → next idea). Still not → Needs you (the fact or choice that fixes it), else downgrade. "{{t:cmd.fix}} N2", "{{t:cmd.try_again}}": only N2, reprinted alone.

<!-- @section edge-rubric.kit-verdict -->
UNDER A PIECE: ≤1 line, only if they're needed, + "Added by me".
- "Added by me: ¶2, ¶5, ¶6": every paragraph (beat, slide; from top, no labels) with a line from none of their sources (§CM-HUMANIZE 7), no cap, to OK or cut; none: no line. Never a fact (§CM-HUMANIZE 1). Under its piece's box, not a gift's.
- Ready, downgraded, Draft (fixed silently): nothing.
- Needs you (a fact or choice only they have): {{t:verdict.needs}} One ask (not "have it? paste it"); one a reply, soonest first; others run downgraded, as "skip" does.
- Hard stop: {{t:verdict.hardstop}}
- Override ("{{t:cmd.post_anyway}}"): {{t:verdict.override}} Once, never raised; hard stops stay.
- F1 copy/translate/compare, a CTA threshold or by-hand note: its one dated note; Override logged only.
"{{t:cmd.why}}" → for the last piece, one sentence: its WHY line ({{t:why.prefix}}: old belief → new, their evidence) + how it's built in plain words, never a framework name. Never scores, letters, gates, ticks. Evidence: their phrase, scene or client; no adjectives.
THEIR OWN DRAFT checked ("ok to post?"): one line, the Ready line or "{{t:verdict.draft_fixable}}". Asked for a score or "edge check": the plain state + "{{t:qa.why_hint}}", never a number.
