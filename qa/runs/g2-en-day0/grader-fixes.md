# G2 EN Day-0: grader fixes, before and after

The graders were fixed per review.md §7 "Grader fixes" (G11–G18) and P8, with the founder's decision of 6 Oct
("Long dumps, missing facts, an early piece to post", docs/DECISIONS.md) in mind. Files: `evals/graders.py`,
`tools/cmcore/checks.py`, `evals/run.py`, `evals/acceptance.toml` (two new `[day0]` keys) and their tests.

How the regression was run:
- Scratch copies of the 8 run folders were graded twice. The run folders in `evals/runs/` were not touched.
- "Before" is the grader at HEAD (`c4c6298`). It gives the same verdicts as the stored `grades.json`.
- "After" is the fixed grader. Both use the HEAD strings, which are the strings the transcripts were made with.
- The working tree's new kit strings (`dump.enough`, `setup.plan_guess`, `dump.post_it` and the rest) give the
  same verdicts. Every check reads its kit wording from `strings/<edition>.toml` keys, never from literal kit text.
- Labels: R, R(kit), R(m) and FP are the review's, from §1 and §4.

## Result

- **False positives: all 8 are gone.** That is YOUR WORD ×6, `[name]` ×1 and I9 ×1.
- **Real defects: all 11 in the valid runs still fail.** The floor's 3 real items still fail too, and the floor
  stays invalid.
- **New detections:** the review asked for these checks.
  - `{first name}` (G12).
  - The whole card over 5,700 characters (G14).
  - KNOWN FOR over 35 words, the keyword only in the ask, and the floor's "minus 6 … to 51" pair (G17).
- **Service-biz S1 now passes every check.** Its one failure was the YOUR WORD false positive.

## Per failed item (review §4)

| # | Run · check | Label | Before | After |
|---|---|---|---|---|
| 1 | proof S1 · I8 `"0" not in allowed_numbers` | R(kit) | fail | fail ✓ |
| 2 | proof S1 · day0_timing, Map after 7 | R(kit) | fail | fail ✓ |
| 3 | proof S1 · YOUR WORD `TOO LATE, from "…" (my guess)` | FP | fail | pass ✓ (G11) |
| 4 | proof S0 · I12, first lines of 13 and 15 words | R(kit) | fail | fail ✓ |
| 5 | proof S0 · Map after 7 | R(kit) | fail | fail ✓ |
| 6 | proof S0 · YOUR WORD `CHAPTER (Lorraine's "…")` | FP | fail | pass ✓ (G11) |
| 7 | coldstart S1 · I23, 2 of 6 pieces (33%) | R (low) | fail | fail ✓ (still 2 of 6, card phrases included) |
| 8 | coldstart S1 · YOUR WORD `"keep up" (…)` | FP | fail | pass ✓ (G11) |
| 9 | coldstart S1 · save line has no backup | R(m) | fail | fail ✓ |
| 10 | coldstart S1 · 164 words of talk after "Shorter" | R(kit conflict) | fail | fail ✓ |
| 11 | consultant S1 · film-ready at 23.0 | R(kit) | fail | fail ✓ |
| 12 | linda · Map after 7 | R(kit) | fail | fail ✓ |
| 13 | linda · film-ready at 27.3 | R(kit + persona) | fail | fail ✓ |
| 14 | linda · YOUR WORD `BADGE (…)` | FP | fail | pass ✓ (G11) |
| 15 | linda · `[name]` in the card's client_words | FP | fail | pass ✓ (G12) |
| 16 | service S0 · I9 `someone asks …, or "can you do my room"` | FP | fail | pass ✓ (G13) |
| 17 | service S0 · YOUR WORD `the nothing room` | FP | fail | pass ✓ (G11) |
| 18 | service S0 · `Hi [name],` in a copy box | R(m) | fail | fail ✓ |
| 19 | service S1 · YOUR WORD `MISTAKE: from …` | FP | fail | pass ✓ (G11) |

Floor (invalid, not counted):
- quit_triggers (t9, 334 words, no copy box): R, fail → fail.
- day0_timing (Map at 7, 3 labels): R, fail → fail.
- day0_shape (no save line): R, fail → fail.
- **New:** I8 fails on "from minus 6 to 51" (t3) and "minus 6 percent to 51 percent" (t5, t9, t10). This is the
  fused result the review found by reading (G17).
- The leak check still fails. Of its 4 hits, 2 were list items run together and are gone (G18). The never-say list
  and "…you just can't keep it by accident" still fail.

## Per run

| Run | Failed before | Failed after | New items after |
|---|---|---|---|
| proof S1 | I8, day0_timing, day0_shape | I8, day0_timing, day0_shape | whole card 5,894 (review 5,893); `{first name}` in the t8 message box; N2 and N3 hold TOO LATE only in the ask |
| proof S0 | I12, day0_timing, day0_shape | I12, day0_timing, day0_shape | KNOWN FOR 42 words (review: 41); SHORT 2 and SHORT 3 hold CHAPTER only in the ask |
| coldstart S1 | I23, day0_shape | I23, day0_shape | KNOWN FOR 36 words (one over; not in the review) |
| consultant S1 | day0_timing | day0_timing, day0_shape | whole card 6,091 (review 6,090) |
| linda S1 | day0_timing, day0_shape | day0_timing | none |
| service S1 | day0_shape | – (passes) | none |
| service S0 | I9, day0_shape | day0_shape | KNOWN FOR 42 words (review: 41) |
| floor | quit_triggers, day0_timing, day0_shape; invalid | I8, quit_triggers, day0_timing, day0_shape; invalid | the minus 6 → 51 pair |

Counts in the 7 valid runs:

| Grade | Failed items | False positives | Real defects |
|---|---|---|---|
| Before | 19 | 8 | 11 |
| After | 19 | 0 | 11 carried over, plus 8 new items from the checks the review asked for |

The 8 new items (10 counting each short):
- whole card ×2 (proof S1, consultant S1);
- `{first name}` ×1 (proof S1);
- keyword only in the ask ×2 runs (proof S1 N2/N3, proof S0 SHORT 2/3);
- KNOWN FOR ×3 (proof S0, service S0, coldstart S1).

The review counted words one lower than `ck.count_words` (41 for 42). The +1 is the same in every run. So the one item
the review never saw, coldstart's 36-word KNOWN FOR, may be at 35 by the review's count. It needs a reader.

## What each fix does on these runs

- **G11 YOUR WORD.** `word_head()` reads the keyword at the head of the value. It drops quotes and a leading "the", and
  cuts at a bracket, comma, colon, dash, " from " or a no-diacritics note. 6 of 6 false positives are gone. A real
  mismatch still fails (tested: "COFFEE" against CTA "CHAPTER").
- **G12 placeholders.**
  - A name redacted inside someone's words in the card's machine block passes: a `client_words` / `their_words` /
    `passages` value, or a quoted value.
  - A `{first name}` slot in a copy box fails. This catches proof S1 t8 "Hi {first name},".
  - service S0's `Hi [name],` in a copy box still fails.
- **G13 I9.** Words given to a hypothetical speaker are no quote. This covers "someone / anyone / they asks, says,
  messages…" and the VN "ai đó hỏi…" (`checks.quotes_in`). A past "someone told me" stays attributed.
- **G14 whole card.** The card top plus its machine block must fit `platform/targets.toml` `[budgets.brand_card]`
  (5,700 EN). This catches consultant S1 and proof S1, as the review measured.
- **G15 early win and session minutes.**
  - day0_timing now reads `session_max_minutes`. All 7 runs pass (16.5–32.0 active minutes).
  - It also reads `early_win_max_minutes_after_dump_start`. The early win came 5.5–8.0 active minutes after the dump
    prompt, each time in the reply to the coach's first send. The personas sent that first chunk at minute 5.3–7.7,
    where the kit asks for 2–3.
  - The miss is graded against the coach's own send (VG1 VP-4, G2 P10). Here it is a warning, with the minutes in
    `details.early_win`. An early win that comes later than the reply to that send fails.
  - The review expected these 7 to fail. See "Choices".
- **G16 run name and summary.**
  - `grades.json` "run" comes from the resolved folder, so a grade run from inside the folder is named.
  - The summary column is now "Film-ready min (clock)": active minutes, with the clock in brackets (service S1
    "16.1 (56.1)", S0 "16.9 (61.9)"). It also shows "(edited: n)" next to Valid.
- **G17 optional Day-0 checks.**
  - **Keyword outside the ask.** This checks EN Week-1 public pieces (acceptance `[week]` scopes the rule to EN). It
    flags proof S1 N2 and N3, as the review predicted, and also proof S0 SHORT 2 and SHORT 3, the same class.
  - The review also named service S1 N1, but N1 carries the keyword in its on-screen line, "The first mistake: the
    sofa", so it passes.
  - **KNOWN FOR ≤35 words.** This uses the new `[day0] known_for_max_en = 35`.
  - **Before → after pairs (in I8).** The two numbers of a pair must appear together in one coach sentence, one proof
    item sentence or one allowed_numbers entry. This catches the floor's fused result. No valid run trips it.
- **G18 leak check.** The persona's TOML is read one string value at a time, and each list item (" | ", " · ") apart.
  The machine side is read the same way: field labels cut, each item read alone, including bracketed lists.
  - The "openers closers here's the thing nobody" kind of hit can no longer happen (tested).
  - A whole persona phrase copied as one list item still leaks however short it is ("Okay. Here's the math.").
  - On these 8 runs, the valid runs had 0 leak fails before and after, and their warnings dropped. The floor keeps 2
    real fails.
  - The pre-edit transcripts behind the review's 3 false positives were not kept (P8). The case is covered by a unit
    test.
- **P8 frozen transcripts.**
  - The first `grade` writes `transcript.raw.jsonl`.
  - Each later grade runs a new protocol check, `edits`. Every changed row must be a machine turn's text, logged in
    `meta.json` "edits" with turn, field, before, after and reason `leak: …`.
  - Anything else makes the run invalid: an unlogged edit, a coach row, a time, or a reason that is not a leak.
  - New turns added after the last frozen row are not edits.
  - `grade` prints "· edited: n", and `grades.json` carries `"edited"`. The packet README tells the simulator so.

## Choices to know

- **G15 is graded against the coach's first send.** By the clock the early win missed the 4-minute budget in 7 of 7
  runs, but each time it came in the machine's first possible reply. Failing it would fail every run on a persona
  artefact (P10). The DECISIONS early win ("usable at minute 5–6") is checked the same way once in-budget personas
  exist.
- **The keyword check is EN only.** acceptance `[week] keyword_exactly_once_rate` says "EN". The VN kit has the same
  rule, but nobody has reviewed VN pieces against it. Side-door and off-map pieces (`message.label.*`) are skipped.
- **I23 also counts the Brand Card's own `phrases` / `openers_closers`.** A phrase still counts only when the coach
  said it in the run, and the keyword never counts. coldstart stays at 2 of 6.
- **The kit's new strings:** a slot may now hold a choice (`{n | none}`, `{your first guess | say 'done'.}`).
  `_slot_pattern` and `_slot_capture` read any `{…}`. A piece title followed by `film.list_open` on the same line is
  still read as a title (K33).

## Not done here

P9 (separate machine-side model, required-paste check, floor notes from grades.json), P10 (in-budget personas) and P11
(re-run) are protocol and persona work outside the grader files.
