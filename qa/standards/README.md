# Standards (build-only)

One rubric per artifact (wf12-qa-spec §3.1). **Nothing here ships:** lint E153 fails any zip that carries `qa/` or `evals/`.

Each file is used three ways:
- **G3 judge rubric.** `evals/judge.md` reads this folder plus `edge-rubric.md`, `guardrails.md`, `compliance.md` and the strip lists. It never sees module prose, self-scores or the lane.
- **Eval cases.** P cases name a file here (`standard = "<id>"`, `critical = [...]`, `min_score = N`; see `evals/README.md`).
- **Runtime footer source.** Each file's "Runtime check shipped" section is the only part that reaches the coach's machine: 3–5 yes/no lines per format and language in `core/format-checks.toml`, rendered into the module's CHECK BEFORE ANSWERING footer. `shared` ships as the Ship Check card and `micro` as the Micro line instead. No scores, totals or fix orders ever ship.

## Shared pass rule (every file)

- Every critical item scores 2.
- The total is ≥ ceil(0.8 × max), with N/A items removed from the max. N/A never counts as a 2.
- All hard gates are clear.
- There is no conditional pass: "pass after edits" is a FAIL that names the edits.
- Uncertain = 0: an ID that doesn't resolve, a row that can't be opened, a quote that can't be matched, a count that can't be redone.

**Anchors:** 2 = fully met; 1 = partly met, with the gap named in one line; 0 = absent, contradicted by the evidence, or honesty broken. Gate items are pass/fail and have no 1. Every score cites its line and rule; a score below 2 quotes the offending line. No praise.

## Rules every file follows

- **Format standards never restate SG items.** A format is scored on top of `shared.md`, which must pass first.
- **"Part A 6/6" is gone.** Wherever voice is scored, three inline rules replace it: simple words with rhythm (no stacked fragments); nothing unnecessary; one person, "you".
- **No per-standard auto-fix orders.** Runtime fixes follow the one shared order in spec §2.2 step 4: truth and claims, then format criticals, then Edge (C, A, K, V, Au), then re-lint.
- **Settled numbers** (spec §0): Ready = gates, Edge ≥8, no 0, format checks yes, 0 open brackets, stance formats C = 2 · Micro under 40 words EN / 60 tiếng VN · quotes ≤15 words EN / ≤25 tiếng VN · AMBER = a record is needed (P-row fields clear it; otherwise a quiet downgrade) · word count ±15% · copy run 6 words EN / 8 tiếng VN (`evals/acceptance.toml [copy]`).
- **Never blocked** (DECISIONS): comment keywords, thresholds, "chấm"; copying, translating or a named comparison on the coach's explicit request. Each gets one dated note.
- **Calibration examples** use fictional coaches only, never a persona from `evals/personas/`.

## Index

All 18 standards in spec §3.1, plus `strategy-doc`, `hook-library` and `launch-campaign` (founder requests, 7 Oct), each written as `<id>.md` in this folder (≤150 lines, with a 3–5 line runtime check in EN and VN).

| id | Artifact | Critical items (must score 2) | Build pass |
|---|---|---|---|
| `shared` | Every script (SG + Edge v2) | SG1 trace, SG2 claims, SG3 polarity (hard gates); SG-copy distance (default path); SG5 Edge; SG6 ladder. SG4 and SG7 are code gates | Gates clear, Edge ≥8/10, no pillar at 0, stance formats C = 2 |
| `micro` | Under 40 words EN / 60 tiếng VN | MC1 trace, MC2 claims, MC3 polarity, MC4 no hedge in the hook, MC5 length, MC6 the keyword delivers a real A-row, MC7 urgency from the Ledger | All yes (N/A only for MC6, MC7) |
| `research-brief` | Research Brief | RB1 right people, RB3 depth, RB4 roots, RB8 swap test, RB9 honesty | ≥16/20, second read at build. Starter brief: RB1, RB9 at 2, ≥14/20, Week 1 only |
| `message-map` | Message Map | MM1 one buyer, MM2 problem in their words, MM6 Big Domino and chain, MM7 focus, MM10 traceable | ≥16/20 |
| `character-card` | Character Card | CC1 one trait, CC4 enemy, CC5 stances (3D), CC8 verbatim voice, CC10 honest and current | ≥16/20; Day-0 v0 ≥14/20 with [GAP] in CC3, CC6, CC7 |
| `signature-keyword` | Keyword pick | SK1 origin (≥3 people, ≥2 places), SK2 not owned, SK6 default shown with origin and reason, swappable | ≥13/16, no 0 |
| `season-plan` | Season / domino plan | SP1 chain, SP2 four rungs, SP3 funnel balance, SP4 give:ask, SP6 proof gate | ≥16/20 |
| `pillar-guide` | Pillar recording guide | PG1 one belief, PG2 clip-ready segments, PG3 the open, PG8 honest | ≥15/18 |
| `cut-kit` | Cut kit | CK1 ≥70% own words, CK2 exact ranges, CK3 standalone, CK7 truth and consent | ≥15/18, every asset passes its own standard |
| `native-short` | Native short | NS1 hooks aligned (+ NS4 Buyer Filter on Likable/Entertain) | `shared` passes; ≥12/14 (≥10/12 when NS4 is N/A) |
| `carousel` | Carousel | CA1 slide-1 hook, CA3 one rule per slide (+ CA5 when a keyword is used) | `shared` passes; ≥13/16 (≥12/14 when CA5 is N/A) |
| `text-post` | Text post | TP1 above the fold, TP4 rhythm, TP6 the CTA closes the loop | `shared` passes; ≥13/16 |
| `offer-post` | Direct-response offer post / client decision breakdown | OP1 offer unmistakable, OP2 not-for line, OP3 process guarantee only, OP4 urgency only from the Ledger, OP5 proof gate | All critical, ≥8/10 |
| `longform-packaging` | Title, thumbnail text, intro | LP1 clear title, LP3 thumbnail adds, LP4 proof-promise-plan, LP7 message match | ≥13/16 |
| `email-zalo` | Email / Zalo | EM1 one job, EM3 voice, EM6 consent and exit, EM7 truth | `shared` passes; ≥15/18; deliverability "not run" |
| `ad-script` | Ad | AD1 proof gate, AD2 pain not person, AD6 compliance, AD7 message match | ≥15/18, second read at build |
| `launch-assets` | Launch assets P0–P9 | LA1 Ledger, LA2 proof and claims, LA4 keyword CTAs written as asked, LA6 consent and capture | ≥16/20, every asset passes its format, second read on the Ledger and P5–P8 |
| `weekly-review` | Weekly review | WR1 traced, WR2 blank is not zero, WR4 honest calls | ≥15/18 |
| `strategy-doc` | Content strategy document (CONTENT-STRATEGY.md / CHIEN-LUOC-NOI-DUNG.md) | SD1 complete, SD2 the coach's own words, SD3 nothing invented, SD4 big ideas distinct and on-Map, SD7 a system they can run, SD10 plain, natural, deliverable | ≥16/20 |
| `hook-library` | Hook library entries (`HOOKS-EN/VN.md`) and the machine's use of it | HB1 fill-in shape, HB3 surfaces fit, HB4 passes the lab, HB5 example truth (+ HB6 VN native); per file HB9-HB12 and gates HG1-HG3; transcript HU1-HU3 | Per entry: the critical items at 2, HB2, HB7, HB8 ≥1; per file all yes and gates clear; build sample of 20 entries per edition |
| `launch-campaign` | One campaign plan (types 1-6) and the shared parts printed with it (`CAMPAIGNS-EN/VN.md`) | LC1 fit, LC2 math in their numbers, LC6 real limits, LC8 consent and mechanics, LC9 proof, LC10 the coach's own CTAs (+ LC12 VN native) | EN ≥18/22, VN ≥20/24; second read on the math, every checkpoint and every cart message |

## Changing a standard

A label, an incident or a judge miss becomes a line in `qa/rubric-proposals.md` naming the item that should have caught it. Only the founder approves a rubric change (spec §5.5). Fix the rubric or the module, never the verdict.
