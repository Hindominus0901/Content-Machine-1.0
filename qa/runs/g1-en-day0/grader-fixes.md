# G1 EN Day-0: grader fixes, before and after

The graders were fixed per review.md §6 (G1–G8 and G10; G9 was already done in `evals/run.py`), along with the grader gaps
that the wf15 EN case verifiers confirmed (`docs/research/wf15-case-impact.md`, "Status"). Each of the 9 runs was then
re-graded with `python3 evals/run.py grade evals/runs/<id>`, which rewrote `grades.json`.

- "Before" is the stored `grades.json` from the round. The grader at the start of this pass gave the same verdicts.
- R, FP and U are the review's labels from §1 and §4. U is counted as real.
- Protocol validity (turns, pace, leaks) comes from `run.py` and is unchanged here. The leak check marks 6 runs as
  invalid. The grader verdicts below do not depend on it.

## Result

- **False positives: all 24 are gone.** That is I8 ×8, I17 ×8, I6 ×4, I2 ×2, I11 ×1 and I23 ×1, plus the template item
  that I2 fed into quit_triggers in coldstart S1 and consultant S1.
- **Real defects: every one still fails.**
  - I17 "Perfect." (coldstart floor).
  - I12, a 13-word first line (service S1).
  - I5 (consultant floor).
  - quit_triggers in both floor runs.
  - day0_timing in all 9 runs.
  - The missing running tags in both floor runs, now caught by the new `running_tag` check.
  - The U item, I23 "follow your passion" (proof S1).
- **quit_triggers in S1/S0 (7 runs) now passes.** The review called it "R (kit)": the kit's ~400-word path to FILM TODAY
  tripped a cumulative counter, but no single reply before FILM TODAY was over 142 words. G6 changed what the counter
  measures, and the kit side is K3. The review's own S1/S0 table has no wall-of-text defect for this item to catch.
- **New detections: 5 runs fail the new `day0_shape` check.** These are proof S0, coldstart S1, coldstart floor,
  consultant floor and service S0. Each hit is a defect the review found by reading.

## Per run

| Run | Before (failed) | After (failed) | Review label → after |
|---|---|---|---|
| proof-coach S1 | I8, I17, I23, quit_triggers, day0_timing | I23, day0_timing | I8 FP ✓ gone · I17 FP ✓ gone (kit text, in details) · I23 U ✓ still fails ("follow your passion") · quit_triggers R(kit) → pass (G6) · day0_timing R ✓ 24.5 min |
| proof-coach S0 | I6, I8, I17, quit_triggers, day0_timing | day0_timing, **day0_shape** | I6 FP ✓ · I8 FP ✓ · I17 FP ✓ · quit_triggers R(kit) → pass · day0_timing R ✓ 25.0 · new: YOUR WORD "one more chapter" ≠ CTA "COFFEE"; Week 1 has no email although the coach named her 140-person list |
| coldstart-coach S1 | I2, I6, I8, I17, quit_triggers, day0_timing | day0_timing, **day0_shape** | I2 FP ✓ · I6 FP ✓ · I8 FP ✓ · I17 FP ✓ · quit_triggers (template item FP ✓ gone; words R(kit) → pass) · day0_timing R ✓ 21.4 · new: save line has no backup; 137 words of talk after "Shorter." (max 90) |
| coldstart-coach floor | I8, I17, quit_triggers, day0_timing | I17, quit_triggers, **running_tag**, day0_timing, **day0_shape** | I8 FP ✓ · I17 R ✓ (turn 7 "Perfect.") · quit_triggers R ✓ (turn 11 Week 1: 333 words with no copy box) · day0_timing R ✓ (Map at 8 turns, found by its labels; 13 coach turns) · running tags R ✓ (11 of 12 untagged) · new: FILM TODAY has no caption box and no quiet option; save line has no route or backup; `[today]` `[trial_ends]` `[plan_start]` |
| consultant S1 | I2, I6, I8, I17, quit_triggers, day0_timing | day0_timing | I2 FP ✓ · I6 FP ✓ · I8 FP ✓ · I17 FP ✓ · quit_triggers (template FP ✓; words → pass) · day0_timing R ✓ (Map at 7 turns; 327.2 min on the clock) |
| consultant floor | I5, I8, I11, I17, quit_triggers, day0_timing | I5, quit_triggers, **running_tag**, day0_timing, **day0_shape** | I5 R ✓ (the ask-3 question in a public caption + the NEXT question) · I8 FP ✓ · I11 FP ✓ · I17 FP ✓ · quit_triggers R ✓ (I5, and turn 10: 366 unboxed words) · day0_timing R ✓ (Map at 8 turns, 3 lines, 315.5) · running tags R ✓ (6 of 10) · new: no caption box, no quiet option; no email for a 380-person list; save line has no route or backup |
| linda S1 | I6, I8, I17, quit_triggers, day0_timing | day0_timing | I6 FP ✓ · I8 FP ✓ · I17 FP ✓ · quit_triggers R(kit) → pass · day0_timing R ✓ 29.9 |
| service-biz S0 | I17, quit_triggers, day0_timing | day0_timing, **day0_shape** | I17 FP ✓ · quit_triggers R(kit) → pass · day0_timing R ✓ (61.4 on the clock; 21.4 active) · new: YOUR WORD "the nothing room" ≠ CTA "TAPE" |
| service-biz S1 | I8, I12, I17, I23, quit_triggers, day0_timing | I12, day0_timing | I8 FP ✓ · I12 R ✓ (13-word first line) · I17 FP ✓ · I23 FP ✓ (4 of 8 pieces, 50%, on the corrected split) · quit_triggers R(kit) → pass · day0_timing R ✓ (63.8 / 23.8 active) |

Failed checks overall:

| Grade | Failed checks | False positives | Real defects in the failures |
|---|---|---|---|
| Before | 46 | 24 | 22 |
| After | 22 | 0 | 22 |

Of the 22 after:
- 15 carry over from the round's 22 real defects: all of them except the 7 S1/S0 quit_triggers items (G6).
  Consultant floor's I5 is one of the 15, still caught but on a corrected rule (see "Choices" below).
- 2 are the new `running_tag` failures (the floor runs).
- 5 are the new `day0_shape` failures.

### Active minutes (G7)

The round's transcripts have no `away_min` rows, so the check reads active time as clock time, and the timing verdicts
above are on the clock. To test G7 on real data, scratch copies of three runs were given the review's time away:
- 40 min for the site visit in service S0 and S1;
- 299.7 min for consultant S1's Claude Free break.

Re-graded, the copies give exactly the review's active minutes, and all three still fail:
- service S0: 21.4 active (61.4 on the clock);
- service S1: 23.8 active (63.8);
- consultant S1: 27.5 active (327.2).

## What changed, by fix

- **G1 (I8).** In `tools/cmcore/checks.py`:
  - `numbers_in` reads month-name dates as kind `date`: "Oct 8", "TUE, OCT 13", "Monday, Oct 19", "Oct 6, 2026",
    "6 Oct 2026", and "Oct 12–18" (both days). A lowercase "may" or "march" stays a verb.
  - `401(k)`, `401k`, `403(b)` and `457(b)` are structural ids. `$401k` stays money.

  In `i8_numbers`, dates and times are skipped. The cold-start result rule now reads only posted text, so the kit's
  "2–3 clients before → after" prompt no longer counts.
- **G2 (I6).** One decision per reply at most, and every reply that prints `map.ok` counts as the same decision. Not
  counted as decisions:
  - a guess line (`setup.guess*`, `setup.multi_income`, `setup.plan_guess`) with its "Right? Or…" and its NEXT line;
  - `check.pick`, the save-route strings (`save.claude_plain`, …), and declaratives such as "we pick one buyer";
  - UI clicks such as "choose Add text content".
- **G3 (I2).** I2 now reads only text outside copy and paste boxes.
- **G4 (I23 and piece titles).** `FORMAT_TITLE_RE` now takes:
  - an article, platform or adjective before the format: "**Facebook post**", "**Free gift**", "THE GIFT · DM reply 1",
    "LinkedIn PDF post";
  - day-first titles that name a format or a length, in any case: "FRI, OCT 9 · LONG POST", "**Monday · 15 s**",
    "Wed, Oct 7 · Email to your list".

  Capitals titles may carry numbers and asides: "ASK 3 PAST CLIENTS · …" and "THE GIFT · DM reply 1 (send to …)".
  `_voice_scrub` keeps a quote that is the whole value of a spoken field (First line, Last line, Hook, On-screen,
  Beat, Subject) or that holds one of the coach's phrases. The phrase share counts a phrase only where the coach said it
  earlier in the run. Consultant floor's Monday piece used a voice-samples phrase the coach never said, and it no
  longer scores.
- **G5 (I11).** The values of the Brand Card's `never_say` and `do_say` fields are dropped in every layout the runs
  used. A field ends at the next schema field name from `schemas/brand-card.toml`.
- **G6 (quit_triggers).** "More than 300 words before anything usable" now fires on either of two counts:
  - the session's words before the first copy-ready output;
  - one reply's words before anything copy-ready in it (a wall).

  Copy-ready output is a copy or paste box, a status line, the card box, a piece that holds a copy box, or the early win.
  The early win is 2+ list lines quoting the coach, matched on a shared 4-word run. A piece printed without its copy box
  is not copy-ready (§CM-FORMATS 8). The limit stays at 300.
- **G7 (day0_timing, running_tag).**
  - Transcript rows take an optional `away_min`. Film-ready is judged on active minutes, and the clock time is kept in
    the details.
  - With no running tag, the Map is found by its labelled lines (`map.*`) and FILM TODAY by `film.now_or_text` or its
    title. A Map reply that also prints FILM TODAY (K2) counts as both.
  - A new `running_tag` check covers every reply. The bar is acceptance `[day0] running_tag_min`, which is 1.0 and new,
    or `[week]` 0.98 outside Day 0.
- **G8 (day0_shape, new).** The check covers:
  - FILM TODAY's caption copy box, and the quiet option (`cmd.quiet`, `cta.not_pushy`) on a comment-keyword CTA;
  - YOUR WORD (`map.word`) equal to the CTA's {KEYWORD} (`cta.default` / `cta.quiet`);
  - an email or subject line in Week 1 when the coach named a list (or the card's `list_size` > 0);
  - the card top (`card.title` + `card.visible.*`) at most `[day0] brand_card_visible_max_chars`, which is 500;
  - the save line (`card.save_line`) with an app route and a backup;
  - no unfilled `[snake_case]` or `{slot}` placeholders, machine blocks included;
  - after "Shorter", at most `[day0] shorter_max_words` words of talk (90, new), copy boxes not counted.

  A question about a fact already given is listed under `not_checked`, because it needs a reader.
- **G10 (I16).** I16 is n/a while `locales/<lang>/examples.md` is not built. That file comes from passing golden runs.
  When the file exists, the check still runs.
- **Gaps the case verifiers confirmed:**
  - **I3.** A "why?" reply is exempt from the cap. Otherwise the cap counts the line minus its string's fixed tail, the
    text after the last {slot}: 8 words under Needs you, 4 under a hard stop or Draft, 0 under Ready.
  - **WHY_RE** now matches only `cmd.why` and close variants: "why this one?", "why N2?", "why did you pick it?",
    "tại sao?", "vì sao chọn bài này?".
  - **CHECK_ASK_RE** now matches "tell me if this is ready" and "can I post this".
  - **I20** accepts `setup.link_unread` for a links-only turn in Day 0's dump, before the Map.
  - **I17** does not fail on praise the machine printed word for word from the kit: the rendered strings, or the
    packet's `kit/*.txt` instruction block. These hits go to `details.kit_text` for the kit owner. "Perfect. One more…"
    still fails.

## Choices and limits

- **I3 cap.** The cap leaves out the fixed tail rather than raising a per-kind limit. The tail is the strings' text, the
  same in every line, and lint budgets it. This keeps verdict_max_words meaning "what the machine adds", in EN and VN,
  and it survives string edits without retuning.
- **I5, consultant floor.**
  - With the corrected piece split, "**Friday · Video, 30 s**" is a piece, so its caption is the audience's text.
  - I5 still counts a private ask's question (`research.ask3`, `research.ask3_cold`) when it is printed in a public
    piece's own text, outside any copy box. Such a question is the machine telling the coach to ask, not words to the
    audience. That is the defect the review describes ("the ask-3 question is pasted into a public caption").
  - A message piece, an "ASK 3" piece, the gift, or the ask in a copy box of its own is never counted. The copy-box
    rule matters for Linda S1, where a plain-titled ask box falls inside the post above it.
- **I17.** The kit-text exemption reads the packet the run was given. Old transcripts therefore keep their exemption
  after K7 ("Messy is fine.") lands.
- **Dates in I8.** Dates are kind `date`, not structural, so the runtime ship lint still traces a deadline date
  ("closes Oct 31") to the ledger. Only I8 skips them.
- **Not changed (not in scope):**
  - day0_timing still counts forwarded-post turns (liked.en.010).
  - `_unquoted` still drops only double quotes.
  - `NOT_ME_RE` still bans the whole rest of the line.
  - Card phrases are still not checked word for word.
- **Build.** `dist/` (gitignored) picks up the `checks.py` change in its inlined `ship_lint.py` on the next
  `tools/build.py`. This pass did not rebuild `dist/` while the kit is being edited.

## After the fix round

Re-graded on 6 Oct 2026 after the whole fix round landed (kit K1–K21 EN + the VN mirror, graders, fixtures, eval
cases): `python3 evals/run.py grade evals/runs/g1-*`, then `python3 evals/run.py summary evals/runs/g1-*`. The
transcripts are the round's own, run on the round's packet kit, so the kit fixes cannot change these verdicts; this
pass checks that the graders, the acceptance keys they read (`[day0]` `brand_card_visible_max_chars` 500,
`running_tag_min`, `shorter_max_words`) and the integrated tree still give the "After" result above.

- **22 failed checks, 0 false positives**: the same per-run lists as the "Per run" table. Build
  `8c9a978cdbbc`; lint 0 errors; 369 tests OK.
- **Valid** is `run.py`'s protocol check (turns, pace, leaks), not a grader verdict: 6 of 9 runs are still invalid,
  all 6 on leaks (P1), the two floor runs also on pace and the coldstart floor on turns (P3, P4). The floor runs'
  film-ready figures are raw `t_min` from that invalid timing (4.3 is the coldstart floor's impossible dictation pace).
  The clock figures for consultant S1 and both service-biz runs include time away (no `away_min` rows; G7).

| Run | Persona | Lane | Valid | Pass | Failed | Coach turns | Map turns | Film-ready min | Case |
|---|---|---|---|---|---|---|---|---|---|
| g1-day0-en-coldstart-coach-S1-r1 | en/coldstart-coach | S1 | no: leaks | no | day0_timing, day0_shape | 10 | 6 | 21.4 |  |
| g1-day0-en-coldstart-coach-floor-r1 | en/coldstart-coach | floor | no: turns, pace, leaks | no | I17, quit_triggers, running_tag, day0_timing, day0_shape | 13 | 8 | 4.306196581196583 |  |
| g1-day0-en-consultant-S1-r1 | en/consultant | S1 | no: leaks | no | day0_timing | 10 | 7 | 327.2 |  |
| g1-day0-en-consultant-floor-r1 | en/consultant | floor | no: pace, leaks | no | I5, quit_triggers, running_tag, day0_timing, day0_shape | 10 | 8 | 315.5 |  |
| g1-day0-en-linda-claude-pro-mac-newsletter-S1-r1 | en/linda-claude-pro-mac-newsletter | S1 | yes | no | day0_timing | 9 | 6 | 29.9 |  |
| g1-day0-en-proof-coach-S0-r1 | en/proof-coach | S0 | yes | no | day0_timing, day0_shape | 9 | 6 | 25.0 |  |
| g1-day0-en-proof-coach-S1-r1 | en/proof-coach | S1 | no: leaks | no | I23, day0_timing | 9 | 6 | 24.5 |  |
| g1-day0-en-service-biz-S0-r1 | en/service-biz | S0 | yes | no | day0_timing, day0_shape | 8 | 5 | 61.4 |  |
| g1-day0-en-service-biz-S1-r1 | en/service-biz | S1 | no: leaks | no | I12, day0_timing | 9 | 6 | 63.8 |  |
