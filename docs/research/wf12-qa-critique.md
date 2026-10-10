# QA review: what to keep, cut, simplify or move to build time

All three drafts copy the agency doctrine faithfully. The failures happen where that doctrine meets one LLM conversation. The same model checks its own work, can't count reliably, has nowhere to hide its work on ChatGPT, and the coach pays for every visible token and every extra question. The pattern below is to build quality into how pieces are written, make the checks code where code exists, record only failures, and enforce the real bar at build time.

## Cross-cutting

1. **KEEP:** "never claim a check you didn't run" and "anything the machine can't see becomes a coach tick." This is the honest core of the system.
2. **SIMPLIFY (shift QA earlier):** put the rigor into preflight, the slot-row brief, material-first drafting and the writing rules in the prompt. Post-hoc review becomes a short gate. Rules given at writing time get followed far more than a self-review in the same context, and they add no visible tokens.
3. **MECHANIZE:** split every runtime check into two kinds.
   - Checks an LLM can do reliably are presence or absence checks: banned list, keyword present, `[brackets]` left, every digit found in a cited row, every ID in the loaded bank, quote matches a string.
   - Everything else is counts, averages, percentages, ratios or medians: average sentence ≤15, word_rate ±15%, ≥70% verbatim, VN syllables, give:ask, trailing medians. These run only in code or at build time. Elsewhere they are writing targets.
   - Reason: a model's guessed count labelled "deterministic, final, never re-argued" is fake.
4. **MECHANIZE:** on Claude, make `ship_lint.py` the default, not an option. Code execution is already required at install, and it is the only truly deterministic runtime layer.
5. **CUT** the claim that QA on ChatGPT is "silent." ChatGPT has no hidden place to work. QA is either printed (tokens and clutter) or skipped, unless a reasoning model does it in its thinking. Design it as writing rules, one verdict line, and one Quality code in the paste block.
6. **SIMPLIFY:** at runtime, "uncertain = FAIL" becomes "uncertain = cut or downgrade the line." Ask only when the piece is built around the missing fact. A literal port makes most cold-start pieces Drafts and floods the coach with questions. Downgrading stays honest with no friction.
7. **FIX:** at most 1 Needs-you question per reply, not ≤1 per piece and ≤3 per batch. C's own G6 walkthrough quits on more than 1 question per message, so A as written fails C.
8. **CUT** every number from coach-facing lines ("9/10", "Edge 9/10", "my check: 6/10"). Self-graded scores are uncalibrated and cluster at 8–9. "Edge" is an unexplained term that breaks I3/G6, and a number invites "why not 10?".
9. **KEEP** "Would I post this?" as the one line, written as a fact and not praise. Use the format verb (film/post/send), e.g. "Ready to film: uses your <K> and Lan's call", ≤15 words. The evidence must point to a Bank item, never an adjective.
10. **KEEP** Edge 5 pillars, Result and Uses as internal hub properties. C's calibration ledger needs the runtime self-score. Write the full record only on Draft or Override (log exceptions only), which removes most QA output tokens.
11. **MOVE-TO-BUILD** the trust in the ≥8 bar. Keep ≥8 as the written rule, but runtime "Ready" is decided by:
    - hard gates;
    - no pillar at 0;
    - 0 open brackets;
    - the format's critical items.

    Whether "8" is real is proven only by the independent judge plus CALIBRATION. A same-context ≥8 is self-certification.

## A: runtime (Layer 1)

12. **SIMPLIFY:** replace L/M/H tiers with two classes set by a trigger list.
    - **claims:** a digit plus a result word, a client story, a testimonial, a price, an urgency word, or the formats offer, ad, sales email and launch P5–P8.
    - **normal:** everything else. Ideas get Edge-lite only.
    - Reason: picking a tier is itself a judgment the model gets wrong.
13. **CUT** the lens pass that prints 5–6 lines per piece. Fold three fail-only questions into the rubric:
    - compliance, mostly covered by the claims scan;
    - "sounds like me," checked against the Voice Card samples;
    - the 5-second test, on title hook plus first line.

    The buyer lens is already the A pillar, the Message Map lens is fixed by the slot row before writing, and the DM/call lens moves to the launch checklist. Same-context lenses rubber-stamp "ok."
14. **CUT** "name the weakest line even on a PASS" at runtime; keep it in build verdicts. It costs tokens and invites needless rewrites.
15. **SIMPLIFY** to 1 automatic fix round at runtime, limited to named gate or critical failures, then Draft plus one question. Keep 2 rounds at build. A second same-context round rarely changes the verdict and doubles output.
16. **SIMPLIFY** draft-then-check per path.
    - **Claude connected:** draft → write to Notion → check → patch → print the verdict lines. This works and stays invisible.
    - **ChatGPT standalone:** hard stops are refused while writing. The post-check only sets Ready or Draft and never reprints a fixed piece.
    - Reason: a post-hoc fix on ChatGPT prints every piece twice.
17. **CUT** the "You did not write these…" role-switch and the "independent checker" framing. Keep the `checker: same-context` label and keep re-opening the rubric and Bank rows right before checking, which is cheap and reduces drift. A prompt cannot create independence.
18. **CUT** the Claude Pro scheduled second read that prepends a v2, and the matching amendment to "never overwrite." If it stays, make it flag-only:
    - it sets Needs and adds one line to DROP;
    - at most 1 claims piece per run;
    - it never touches the body.

    Reasons: Notion's "Last edited by" is unverified; the coach may have filmed v1 without editing it; DROP is already ≤120 words plus the watcher plus catch-up; and the same model on a schedule is only weakly independent.
19. **CUT** the fresh-chat second read on ChatGPT, Claude Free and Gemini ("open a new chat and paste…"). It costs an extra message and a copy-paste on capped plans, and the same model in the same Project adds little independence. The coach's before-posting ticks are the truly independent read.
20. **MOVE-TO-BUILD** these into `qa/CALIBRATION.md`:
    - the frozen round-1 and round-2 scores;
    - the per-format machine QA ledger;
    - "gap ≥2 twice → load the full rubric and examples";
    - "raise the bar to 9."

    They need second-read data that most plans won't have, and loading extra files on the fly breaks the ≤4 references / ~16k token budget.
21. **CUT** the diagnostic's "temporary stricter bar" (A and Au must be 2 for 2 weeks). Change the plan instead: the next 2 weeks' slots become proof and story formats, which the diagnostic already outputs. A stricter self-score only produces more Drafts.
22. **CUT** per-pillar score-vs-performance calibration from REVIEW. Move it to the founder's analysis of opt-in exports. It needs ≥20 posts with full stats per pillar and doesn't fit REVIEW's one-screen budget.
23. **MECHANIZE** the claims scan as the #1 runtime check. It mirrors build invariant I6, and fabrication and claims are where the real harm is.
    - Every digit appears in a cited P or S row, or is a date, duration or Brief price.
    - Every urgency word maps to a Ledger row.
    - Claim words are marked GREEN, AMBER or RED by lookup.
24. **FIX AMBER** in arch §8.1/§8.4, B SG2 and House Rule 5, which all say "ships with Needs:". AMBER means "needs a record."
    - It is cleared mechanically by P-row fields: Substantiated, consent uses, and the context line.
    - With no record, first downgrade silently to process or founding framing. Draft only if the piece is about that result.
    - Reason: under "every VN result claim is AMBER until counsel signs off," VN result pieces would otherwise stay Drafts forever.
25. **MOVE** truth and consent confirmation from every post to proof intake. Ask once when the P-row is created ("written OK? which uses? backed by a record?"). Re-ask only when the re-check date passes at the monthly re-plan. Asking per post repeats friction; intake is when the coach actually knows.
26. **KEEP:**
    - preflight GO / DOWNGRADE / NEEDS YOU, with DOWNGRADE as the default path;
    - the hard stops;
    - "post anyway" on everything except hard stops;
    - `[NEEDS]` and never inventing;
    - "not supplied" ≠ 0;
    - never saying "saved" before the write returns, and never saying "your link works";
    - the no-praise word lists.
27. **MECHANIZE** "Not checked yet (usage limit)." A model can't detect its own cutoff. Rule: the verdict line prints right after each piece, so a piece with no line is unchecked. START-HERE says so, and Claude marks the Runs row Partial.
28. **SIMPLIFY** the hub record to four properties: Result (Ready / Draft / Override / Pending), Needs, Edge (number), Uses. Drop Tier, Round, Second Read and Coach Outcome. Drop the QA toggle on passes. This saves output tokens and calls against the ≤30 hub calls per run.
29. **KEEP** the Ship Check card at about 900 characters; don't grow it to 1,300–1,500.
    - The task variant (≤800 EN / ≤1,000 VN) carries only trace and digits, claims and Ledger, brackets, and the verdict line. No Edge, no lenses.
    - Reason: models skip long cards, and unattended tasks need only the hard gates.
30. **KEEP** B's Micro check for pieces under 40 words EN / 60 tiếng VN, and apply it to DROP hooks too. Scoring a 130-character post on 5 pillars is noise.
31. **SIMPLIFY** variation on standalone to date-formula rotation plus `recent_hook_stems`. Cut "keyword placement differs from the last piece" there. Standalone has no history, so rotation must be correct by construction.
32. **MOVE-TO-BUILD** the VN syllable limits as hard gates (≈18 tiếng hook, ≤25 tiếng quotes). Keep them as writing targets at runtime. LLM syllable counting in VN is unreliable.

## A: coach checklists (Layer 2)

33. **SIMPLIFY** "Before filming" to one line in the film list: "Read the first line out loud. Not you? Voice-note what you'd say." Ticks 2–4 are things the machine already enforces (no open `[NEEDS]`, keyword placement) or a coaching tip.
34. **SIMPLIFY** "Before posting" to at most 2 ticks. They appear only when the piece triggers them, and no reply is required ("say 'no on 2' if something's off").
    - First public use of a P-row: "true, and they said yes."
    - A keyword CTA: "it delivers today (link opens, DM reply ready)."
    - Tick 4 is machine-checkable, tick 5 becomes the NEXT line, and tick 3 moves to the launch list.
    - Reason: a required confirmation costs a message on capped plans.
35. **KEEP** all 5 "Before a launch" ticks at T-7. At cart-open, repeat only "walk the path on your phone." Launches happen 2–4 times a year, the stakes are high, and none of these can be verified by the machine.
36. **SIMPLIFY** the weekly review to 2 asks plus a default.
    - Stats, as numbers or a screenshot.
    - Calls, DMs and "how did you find me?" answers.
    - Ticks 3 and 4 merge into one optional question.
    - The bets apply by default ("I'll run these 3 unless you change one").
    - Reason: five questions every Friday breaks "≤1 decision per session."
37. **SIMPLIFY** the monthly re-plan to 3 questions. Ticks 1 and 5 overlap; "a format you dread" becomes optional.
    - Has anything changed: buyer, offer, price, dates?
    - Any new results or new OKs to share?
    - Anything you no longer believe, or that's no longer true publicly?
38. **CUT** the calendar-based fade and return logic (weeks 1–3, "after an incident"). Trigger lists by content instead, which is mechanical and works without stored state.

## A: feedback loops

39. **CUT** automatic edit detection (diffing the Notion body Scripted → Posted), the auto-allowlist after 3 reverts, and the four-way coach-outcome labels. Replace them with two commands:
    - "not me: <line>" adds it to the Voice Card banned list;
    - "I do say <word>" adds it to a personal allowlist.

    Diffing needs stored originals and extra hub calls, and coaches won't label outcomes.
40. **SIMPLIFY** the Claims view to P-row properties: Consent uses, Consent date, Substantiated, Re-check by. Cut the back-writes (Slot Keys used, first used, live/dated/retired). Those cost hub calls on every posted piece and depend on the coach reporting "posted."
41. **SIMPLIFY** retire rules. Keep format retire and keyword echo-0 at the monthly re-plan (the coach decides), and P-row retire when consent or the offer changes. Cut hook-stem performance retire and capture-question rotation: there will never be enough stats per stem.
42. **KEEP** Scarcity Ledger reconciliation as one debrief question: "Did the link close when you said?"
43. **KEEP** the opt-in "send feedback" export. In v1 it is an anonymised paste that the coach emails. It is the only bridge from the doctrine's human sample to the build evals.

## B: standards (Layer 4)

44. **MOVE-TO-BUILD** the 15 scored standards (0–2 tables, totals, ceil(0.8×max), auto-fix orders). They become the G3 judge rubric and the source for eval cases.
    - Appending ≤60-line standards breaks the reference budget of ≤150 lines / ≤9 KB. fmt-short alone would get NS + CA + TP, about 180 lines added.
    - It also breaks the ~16k-token budget per job.
45. **SIMPLIFY** the runtime standards to 3–5 critical yes/no items per format, placed in the existing render.py "CHECK BEFORE ANSWERING" footer. No 0–2 scores and no totals. Otherwise the model scores about 25 numbers per piece and rubber-stamps them.
46. **CUT** the 15 per-standard auto-fix orders. Use one shared order: truth and claims → format critical items → Edge (Character first, per wf6) → re-lint. Models rewrite holistically and skip ordered lists.
47. **DEDUPE:** format standards must not restate SG items (hook lengths, honesty, EM3/TP4 "Part A 6/6"). Also remove "the agency's writing checklist (Part A)" from shipped text: the runtime doesn't have it, so either inline 3 rules or drop it.
48. **MAKE** plan and calendar standards correct by construction (SP1–SP9, LA7). The build ships fixed Season slot grids per volume tier and launch calendars per type, designed to satisfy 4 rungs, phase mix, give:ask ≥3:1, CTA mix and variation. Lint verifies the grids. At runtime the model only fills slots. Rolling 8-week ratios and ±10-point mixes are arithmetic the model fumbles.
49. **MECHANIZE** WR1, WR4 and WR5 (medians, 2× trailing-10, the break-point trigger) and LA8 launch math.
    - Use code on Claude.
    - On ChatGPT, use its data-analysis tool only if Phase 0 confirms Free has it [VERIFY]. Otherwise REVIEW says "rough" and names no winner.
    - Launch math is always shown as the formula with its numbers.
50. **SIMPLIFY** the setup standards (MM, CC, SK) at runtime to "required fields present, each traced or tagged [guess]/[GAP]."
    - Cut CC's "≤2 probes per gap," which would blow the ≤8 coach turns to a film-ready script. Gaps become the optional homework.
    - Cut the required runtime second read on the Message Map; golden runs test it at build.
51. **SIMPLIFY** SK6: the machine picks a default keyword and shows its origin and a one-line reason. The coach says "change" to swap. A shortlist of 3 is a real decision, and setup already has its one.
52. **SIMPLIFY** the research G11/RB9 coach re-open to non-blocking: "Tap any of these 3 links; tell me if one doesn't say what I quoted." Where browsing exists, the machine re-fetches the quoted URLs itself and silently drops lines that don't match. Cut the coach-driven "delete, recount, re-issue" loop.
53. **CUT** B §S0.10's runtime second-read list and A's "Tier H required." Keep one rule: at build, every judged pass gets a second read; at runtime nothing is required, with an optional flag-only read on Claude Pro. The two lists are inconsistent, and the requirement is impossible on Free plans.
54. **SIMPLIFY** the shipped human docs.
    - HOUSE-RULES.md: one plain page, about 12 bullets, EN and VN, for the coach and their VA.
    - STANDARDS.md: per format, "what good looks like" plus "never" bullets only. No IDs, scores or fix orders.
    - Scoring tables are maintainer material and read like homework.
55. **KEEP** the House Rules content as model-facing text in guardrails.md and compliance.md, with rule 5's "AMBER ships" fixed per item 24. These are the founder's non-negotiables.
56. **FIX** the wf6 report example "Verdict: PASS — publish after 1 data fill" (wf6 line 674) before it becomes edge-rubric.md. It is exactly the conditional pass the doctrine forbids, and examples steer the model.
57. **FIX** the numeric conflicts before building:
    - word-count tolerance: NS3 says ±10%, A says ±15%;
    - quote cap: B says 15 words EN / 25 tiếng VN, arch §8.5 says 15 for both;
    - pass bar: A, B and wf6 say 8; arch §8.1/§8.2 and the card text say "ship ≥7/10."

    Lint and graders need one number for each.

## C: build QA (Layer 3)

58. **KEEP** C nearly whole; this is where the founder's rigor belongs:
    - G1 lint plus must-fail fixtures;
    - the judge, with canaries, blind to self-scores;
    - 3× blind generative tests, with hard gates never averaged;
    - a second read on judged passes;
    - held-out personas and the n-gram copy check;
    - the lift-over-no-pack baseline;
    - the walkthrough QUIT triggers;
    - human smoke tests and the founder's blind sheet;
    - `package.py` refusing to publish without SIGNOFF matching the build sha256.
59. **ADD** to the global invariants, so "QA invisible" becomes a test:
    - exactly 1 verdict line per piece, ≤20 words;
    - ≤1 question per reply;
    - no score, no "Edge" and no pillar codes in coach text;
    - codes allowed only inside the paste block.
60. **ELEVATE** CALIBRATION.md to a release gate, G3b. Per format, including the floor-model lane:
    - runtime Ready where the judge says FAIL on ≤10% of pieces;
    - average self-Edge minus judge-Edge ≤1.0.

    It is the only thing that makes the runtime one-liner trustworthy.
61. **ADD** a runtime-lint eval. For each check the model does by hand on ChatGPT, measure its miss rate against `ship_lint.py` on the same outputs. Any check missing more than 20% becomes a writing target only. This decides with data which runtime checks are real and which are theatre.
62. **SIMPLIFY** G2's cost. Run 3× only for setup → film-today → Week 1 plus the adversarial cases; run the rest of the journey once; full 3× runs only on release candidates. 5 personas × 2 editions × 3 lanes × 3 runs × the full journey is a large bill for the noise it removes.
63. **FIX** the founder-time estimate. Judge validation needs ≥40 labels per edition with ≥20 "don't post." That is a one-time labeling session of roughly 2–3 hours before any Phase 2 result counts. After that, about 45 minutes per release.
64. **FIX** the OpenAI API lane claim. The API is not a ChatGPT Project: it lacks Project retrieval, uses a different system prompt and model routing, and has no Free fallback model. Keep it as a cheap stand-in, but G7 must include one full first-session golden run per edition in real ChatGPT Free, the main VN buyer path.
65. **SIMPLIFY** the build run contract's paperwork.
    - Keep: preflight (fails closed), frozen self-score, independent judge, write allowlist plus landing_check, the ledger.
    - Merge agent-brief.md into preflight.
    - Replace the 20-point module scorecard with pass/fail on the critical gates: spec trace, budgets, experience invariants, cases, honesty. Budgets, experience rules and cases are already measured by lint and evals.
66. **SEQUENCE** the tools by phase so seven tools aren't built before the first module:
    - Phase 1: lint.py, preflight.py, verdict_check.py.
    - Phase 2 (first judge validation): blind.py, ingest_labels.py.
    - Phase 7: carry_check.py, landing_check.py, scorecard.py.
67. **KEEP** the runtime self-check J set (30 cases, within ±1, ≥85% agreement), and run it on the floor-model lane too.

## What runtime QA looks like after these changes

- **The coach sees:** one line per piece ("Ready to film: <fact>" or "Needs you: <one question>"), at most 1 question per reply, plus 1–2 ticks only when a claim or keyword CTA triggers them.
- **The model does:**
  - before writing: preflight with downgrade by default, material-first drafting;
  - after writing: claims and digit trace, Edge 5 pillars plus hard gates plus 3–5 format critical items, at most 1 fix.
- **Code does** (Claude, at runtime): lengths, averages, overlap, medians, launch math.
- **Build does:** scored standards, the independent judge, 3× blind tests, second reads, calibration of runtime against the judge, walkthroughs, smoke tests, and the founder's sign-off.

### Critical Files for Implementation

The repo has no source files yet (it holds only a file named `yeah`), so every path under the repo is still to be created.

- /home/user/Content-Machine-1.0/core/ship-check.md (the ≤900-character card and the ≤800 / ≤1,000-character task variant)
- /home/user/Content-Machine-1.0/modules/edge-rubric.md and /home/user/Content-Machine-1.0/modules/guardrails.md (Edge plus gates, AMBER-as-record, the Micro check, the fixed wf6 example)
- /home/user/Content-Machine-1.0/tools/ship_lint.py and /home/user/Content-Machine-1.0/tools/lint.py (runtime deterministic checks on Claude; build budgets and the grids that make plans correct by construction)
- /home/user/Content-Machine-1.0/evals/graders.py with /home/user/Content-Machine-1.0/qa/CALIBRATION.md (QA-visibility invariants, runtime-vs-judge release gate)
- /home/user/Content-Machine-1.0/strings/en.toml and /home/user/Content-Machine-1.0/strings/vn.toml (verdict lines with no scores, trimmed checklists)
- Sources:
  - /tmp/claude-0/-home-user-Content-Machine-1-0/085f5f0b-5883-504d-aefb-4af9a99859d9/scratchpad/research/arch-final-spec.md (§3.3 budgets, §8.1/§8.2/§8.4 conflicts)
  - /tmp/claude-0/-home-user-Content-Machine-1-0/085f5f0b-5883-504d-aefb-4af9a99859d9/scratchpad/research/wf6-character-design.md (§B, line 674)