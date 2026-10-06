Result: FAIL

# G1 EN Day-0 golden round: independent review

Build 3b520a41384a. Kit under test: the packet `kit/`, which is the `dist/en` build at review start
(`1-INSTRUCTIONS.txt` 6,257 bytes, md5 551c9bc4…).

The working tree moved while this review ran. `dist/en/1-INSTRUCTIONS.txt` is now 6,286 bytes / 6,132 chars and
adds §CM-NATURAL and "linking words". The defects below are unchanged by that edit. Line references point to the
current tree: start-block and module line numbers did not move, while strings and the schema shifted by a few
lines and are cited as they are now.

The graders were re-run on all 9 folders and gave the same verdicts as the stored `grades.json`. Every transcript was read in full. For leaks, a
4-gram scan compared each machine turn with the persona files, minus earlier coach turns and minus the kit, and
every hit was checked by hand.

Why FAIL:
- Film-ready ≤20 min was missed in 9/9 runs: 21.4–29.9 active minutes in the 7 runs with valid timing.
- One coach quit (consultant, floor).
- Quit points hit: 6 of the 17, all in the floor or S0 lanes.
- Persona facts leaked into machine text in 8/9 runs, although 7 notes files say "no leaks". So S1 voice quality is
  over-stated.
- Real kit conflicts show up in every S1 run: one screen vs Week 1, Week-1 dates, card enums, and the keyword
  counted once vs the comment ask.
- Every grader verdict is FAIL. 24 of the 46 failed checks are false positives, which hides which runs really broke.

## 1. The 9 runs

"Map turn" is the number of coach turns up to the Map. Film-ready is given as clock time / active time (active =
clock minus scripted time away). In the "Failed checks" column, R = real defect, FP = grader false positive, and
U = uncertain, counted as real.

| Run | Outcome | Coach turns | Map turn | Film-ready min (clock / active) | Grader | Failed checks |
|---|---|---|---|---|---|---|
| proof-coach S1 | film-ready + Week 1 + card | 9 | 6 | 24.5 / 24.5 | FAIL | I8 FP · I17 FP (kit text) · I23 U · quit_triggers R (kit) · day0_timing R |
| proof-coach S0 | film-ready + Week 1 + card | 9 | 6 | 25.0 / 25.0 | FAIL | I6 FP · I8 FP · I17 FP (kit text) · quit_triggers R (kit) · day0_timing R |
| coldstart-coach S1 | film-ready + Week 1 + card | 10 | 6 | 21.4 / 21.4 | FAIL | I2 FP · I6 FP · I8 FP · I17 FP (kit text) · quit_triggers R (words; its template item is FP) · day0_timing R |
| coldstart-coach floor | film-ready + Week 1 + card (defective) | 13 | 8 (untagged) | invalid (t_min 4.3; about 20 at 130 wpm) | FAIL | I8 FP · I17 R ("Perfect.") · quit_triggers R · day0_timing R (no running tags, 13 turns) |
| consultant S1 | film-ready + Week 1 + card | 10 | 7 | 327.2 / about 27.5 (5-h Free break) | FAIL | I2 FP · I6 FP · I8 FP · I17 FP (kit text) · quit_triggers R (words; template item FP) · day0_timing R (Map at 7 turns; 27.5 active) |
| consultant floor | QUIT (inferred in notes, no quit line written) | 10 | 8 | invalid (315.5 clock; dictated at about 250 wpm) | FAIL | I5 R · I8 FP · I11 FP (but exposes a leak) · I17 FP (kit text) · quit_triggers R · day0_timing R (Map 8 turns, 3 lines) |
| linda (Claude Pro, Mac) S1 | film-ready + Week 1 + card | 9 | 6 | 29.9 / 29.9 | FAIL | I6 FP · I8 FP · I17 FP (kit text) · quit_triggers R (kit) · day0_timing R |
| service-biz S0 | film-ready + Week 1 + card | 8 | 5 | 61.4 / 21.4 (40-min site visit) | FAIL | I17 FP (kit text) · quit_triggers R (kit) · day0_timing R (21.4 active) |
| service-biz S1 | film-ready + Week 1 + card | 9 | 6 | 63.8 / 23.8 (40-min site visit) | FAIL | I8 FP · I12 R · I17 FP (kit text) · I23 FP · quit_triggers R (kit) · day0_timing R (23.8 active) |

Totals:
- Grader passes: 0/9.
- Outcomes: 8 runs reached the card (7 of them clean S1/S0 runs); 1 quit.
- Failed checks: 46. Of these, 22 are real (21 R + 1 U) and 24 are false positives (I8 ×8, I17 ×8, I6 ×4, I2 ×2,
  I11 ×1, I23 ×1).
- I16 did not run in any of the 9 runs, because `locales/en/examples.md` is missing.

## 2. Day-0 shape against wf15 §1, and budgets

Key: ✓ = matches wf15 · ~ = partly · ✗ = missing or wrong.

| Step (wf15 §1) | proof S1 | cold S1 | cons S1 | linda S1 | svc S1 | proof S0 | svc S0 | cold floor | cons floor |
|---|---|---|---|---|---|---|---|---|---|
| Promise line + mic tip + dump prompt (+ posts/link) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ phone tip only | ~ phone tip only; Windows user |
| Early win after chunk 1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ no tag | ~ no tag |
| Missing facts only (≤3, one a message, with a guess) | ✓ 1 | ✓ 1 | ✓ 1 | ✓ 1 | ~ 1, on the range | ✓ 1 | ✓ 0 | ✗ 3, no guesses, 2 re-asks | ✗ 3; one is options with no default |
| Map: 4 lines + "OK, or change a line" | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ no tag | ✗ 3 lines |
| FILM TODAY: script, caption copy box, CTA with quiet option, "Film it now…" | ✓ | ✓ | ✓ | ✓ | ✓ | ~ CTA word ≠ YOUR WORD | ~ CTA word ≠ YOUR WORD | ✗ no box, no quiet | ✗ no box, no quiet |
| Week 1 unasked in the next reply | ✓ | ✓ | ✓ | ✓ | ✓ | ~ no email to her 140-person list | ✓ | ~ no boxes; kit example copied | ✗ wrong mix, no email |
| Card: top ≤500 chars + machine block + save line | ✓ 445 | ~ 308, no backup | ✓ 361 | ✓ 457 | ✓ 413 | ✓ 399 | ✓ 331 | ✗ [today] placeholders, no route | ✗ no route or backup |
| NEXT | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ a 2nd question inside it |
| Map ≤6 coach turns | ✓ | ✓ | ✗ 7 | ✓ | ✓ | ✓ | ✓ | ✗ 8 | ✗ 8 |
| Film-ready ≤20 min | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| ≤10 coach turns | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ 13 | ✓ |

Notes on the table:
- Week 1 + card length. In the S1 runs, Week 1 replies ran 824–1,338 words and card replies 1,006–1,215. In the S0
  runs they were shorter: 377/639 and 720/734.
- Card as a separate reply. 7 of 7 S1/S0 runs gave the card in its own reply after an extra coach turn (the kit
  doesn't say whether the card shares Week 1's reply).

Lane comparison:
- **S1.** The kit was followed closely. Every remaining failure is a kit design conflict (sections 4–5).
- **S0 (compact mode).** It does as well as S1 on turns and timing, and its replies are about half as long. Two defects
  come from gaps in the instruction block alone:
  - YOUR WORD ≠ the CTA word in 2/2 runs: "one more chapter" vs `COFFEE`, and "the nothing room" vs `TAPE`.
  - The Week-1 mix is undefined, so proof S0 dropped the email to her list.
- **Floor.** The weaker model breaks the surface contract: running tags are missing on 11/12 and 6/10 replies; it uses
  no copy boxes and no quiet option; it re-asks facts the coach already gave; it praises ("Perfect."); and it leaves
  `[today]`/`[plan_start]` placeholders and 2 questions in one reply. Simulator defects also make both floor timings
  invalid (section 6, P3–P4).

Why film-ready misses everywhere. The dictated dumps ran 1,866–2,295 words, which is 14–18 minutes at 130 wpm,
plus 1–2 minutes of pasted posts, against the kit's "Talk 5–10 min". Nothing in the kit closes a long dump, and FILM TODAY waits for done → question
→ Map → OK. Even counting only active minutes, no run is under 20.

## 3. Leakage spot-check (all 9 transcripts)

The machine used persona facts the coach never said in 8/9 runs. Most come from `voice-samples.md` or
`expected.toml` [voice]; the coach brief tells the shared simulator agent to read these files.

| Run | Leak (machine text) | Source never said by the coach |
|---|---|---|
| proof S1 t9 card | `rhythm: short lines; story first, then the step` | expected.toml rhythm "short lines; story first, then the step; fragment punch"; voice-samples "Tells the story first, then the step" |
| proof S1 t9 · proof S0 t9 | Gail "now trains staff at small insurance agencies (on her own)" | proof_items P3 / answer bank; the dump said one agency her friend owns |
| proof S0 t6, t9 | KNOWN FOR "anywhere from 11 weeks in to about 5 months after we finish" | answer bank "anywhere from Lorraine's 11 weeks to about 5 months after we finish" (suspect) |
| proof S1 + S0 | talk day Tuesday, delivery bullets | persona.toml talk_day / delivery_mode (suspect; "bullets" is forced by the card enum, see K8) |
| coldstart S1 t10 | `rhythm: short lines, then one long run-on story` | voice-samples "Short sentences, then one long run-on when a story gets going" |
| linda S1 t9 | `rhythm: long looping stories that start in the middle` | voice-samples "talks in long, looping sentences … Starts in the middle of a story" |
| service S1 t9 | `rhythm: fast; the scene first, then the rule` | expected.toml rhythm "the scene first, then the rule" |
| service S0 t5, t8 | "the story first, then the rule"; `rhythm: the scene, who said what, then the rule` | voice-samples "Tells the scene first (who was in the room, what they said), then the rule" |
| coldstart floor t13 | `talk_day Sunday`; `never_say shred · beast_mode · certified · coach_dan` | persona.toml talk_day; answers.md / voice-samples never-list |
| consultant floor t10 | `timezone=America/Chicago`; never_say "Cash is king… Agree?…"; passages "You can keep a client you love on purpose…", "I'm not here to make you feel bad about your numbers…"; openers "Okay. Here's the math.", "So here's what I'd do" | persona.toml timezone; voice-samples phrases 1, 7, 8 and never-list (no posts were pasted in this run) |
| consultant S1, linda S1 | Claude-only save route; "Hit the limit?" (consultant) | the coach never named her app or plan. A real Claude knows its own app but not the plan (packet gap, P5) |

Consultant S1 is otherwise clean: every number and name was checked against the coach turns.

Effect of the leaks:
- They bias the S1 Voice Card upward, and so I23 and any SG4 voice judging.
- They make the "leaks_fixed: []" claims in proof S1 and linda S1 wrong.

## 4. Failed grader checks: real or false positive

- **I8 numbers: 8 × FP.**
  - The flagged numbers are dates and one account name:
    - month-name dates: proof S1 t8 "Thu, Oct 8" / "Fri, Oct 9"; cold S1 t9 "TUE, OCT 13" / 14 / 17; cons S1 t9
      "FRIDAY, OCT 16".
    - ISO dates in the card box, which §CM-CARD 3 requires (`date=YYYY-MM-DD`, `trial_ends`, `plan_start`): 7 runs.
    - "401(k)" / "401k" (proof S1 and S0), her own "four oh one K".
  - The cold-start rule also fires on the kit's own prompt "2–3 clients before → after" (start-block line 22).
  - Grader code: `tools/cmcore/checks.py` `numbers_in` has no month-name dates, and `evals/graders.py` `i8_numbers`
    checks `kind == "date"` against allowed_numbers. `COLD_RESULT_RE` (L167) is applied to prose as well.
  - Side note: consultant floor's `trial_ends=2026-10-31` is wrong arithmetic (plan_start + 25 days); this is real
    but not an I8 matter.
- **I17 praise.**
  - 8 × FP against the machine: "Messy is perfect." is mandated by `core/en/start-block.md` line 22. It is a kit text
    defect and the fix is one word (K7).
  - 1 × R: coldstart floor t7 "Perfect. One more: …".
- **I6 decisions: 4 × FP.**
  - The hits:
    - the Map OK restated after a Map pushback (cold S1 t6/t7, which §CM-MAP "MAP PUSHBACK, one line, same OK"
      requires);
    - the streams guess-question (cons S1 t5 "tell me which one pays the bills"; proof S0 t5 "so we pick one buyer
      … Right?");
    - the save-route click word "choose Add text content" (cons S1 t10, linda t9).
  - `DECISION_RE` (L161) counts repeats and UI words. Proof S0's wording ("we pick one buyer") does read like a
    choice, which K19 fixes.
- **I2 template: 2 × FP.** Buyer blanks inside the gift: cold S1 t9 "Yours: ______ ______ ______" and cons S1 t9
  "Client: ____ …". §CM-CTA-KIT 2 (convert.md line 7) allows "blanks only for the buyer". `i2_template` scans copy
  boxes. This also creates the false "asked to fill a template" item under quit_triggers in those two runs.
- **I11 injection: 1 × FP** (consultant floor t10). The hits are never_say entries inside the card's machine block,
  not claims. The entries themselves are leaks (section 3).
- **I23 voice.**
  - service S1 is FP (5/8 = 62% on a correct split):
    - day-first titles like "FRI, OCT 9 · LONG POST" are not piece titles (`FORMAT_TITLE_RE` L110), so the long post
      merges into N1;
    - `_voice_scrub` blanks 4-word quotes, so N2's "Last line: "Rug before sofa. Always."" is lost;
    - DM reply 2 counts as a piece.
  - proof S1 is U, counted real: the email subject "Please don't follow your passion" uses a never-word in hook
    position. She says it herself only to reject it, and the persona never-list is absolute (wf14 §5). Low severity.
- **I12 formats: R.** service S1 t8: N1's first line is 13 words, over the ≤12 limit (§CM-FORMATS 1). This is a
  one-off machine slip; the kit rule exists.
- **I5 questions: R.** consultant floor t10: the ask-3 question is pasted into a public caption, and the NEXT line
  adds "Want a nudge…? Say 'yes'."
- **quit_triggers "300 words before anything usable": R (kit structure) in all 9 runs.**
  - Counts were 372–752 words. The kit's mandatory path alone before FILM TODAY is about 360–400 words: setup ≈140,
    early win ≈60–80, joggers ≈30 each, question ≈30–70, Map ≈115–140.
  - No single reply before FILM TODAY was over 142 words, so the personas' actual "wall of text" trigger did not
    fire in S1/S0. Both the kit and the proxy need fixing (K3, G6).
  - In the floor runs the count is real: there are no copy boxes, so nothing usable is recognised.
- **day0_timing: R in all 9 runs.**
  - The kit cause is that the dump never closes and FILM TODAY sits behind the Map OK (K1, K2).
  - Grader limitations:
    - For service S0/S1 and consultant S1, the clock includes scripted time away. The verdict still holds on active
      minutes.
    - The coldstart floor's "no Map / film step reached" is real: the replies carry no running tag, as the kit
      requires. The floor notes call it a false positive, which is wrong.
  - Consultant S1's Map at 7 turns comes from the persona's "give me a second, I'm writing" pause turn.

## 5. Read as the coach: confusion, reading load, repeats, quits

Problems by run:
- **Reading load.**
  - Week 1 and the card arrive as two replies of 4–6 phone screens each, in all 5 S1 runs.
  - Coldstart S1 t10: the coach wrote "Bro I'm on my phone. Shorter." and got 1,096 words. §CM-TODAY 1 says ≤90
    words, but the card was due next.
  - Proof S1 and service S1 personas "skim anything longer than one screen".
- **Asked twice.**
  - Coldstart floor t6 asked the soccer dad's exact words, which the coach had already said in chunk 2.
  - Coldstart floor t7 asked "what you sell"; chunk 1 had said "I don't have anything to sell yet".
  - Consultant floor t6–t7 asked about a client story (Marcus) she had already told.
  - None in S1/S0.
- **Confusion.**
  - S0 Map word vs CTA word ("YOUR WORD: one more chapter", then "Comment COFFEE").
  - Card boxes show `keyword:`, `pack_version`, `cta_style`, `recent_hooks` to coaches who are confused by
    "keyword" (proof, coldstart, consultant, service, linda). These are labelled "no need to read", but 5,000–5,600
    chars of `name: value` lines is the brand wall code-averse personas quit on.
  - Week 1 dates disagree with the card's `plan_start`:
    - proof S1 prints Oct 7–11 but `plan_start: 2026-10-12`;
    - cold S1 and cons S1 leave Wed–Sun empty while NEXT says "Tomorrow … say 'next'";
    - consultant and linda: tomorrow's "next" lands on the guessed talk day before Week 1 has started.
  - Service S1/S0 "where does all this live?" → "in this chat". Bree, the VA, cannot reach the chat.
  - Linda's dump already refused comment asks ("my old CEO reads my posts. I can't."). The kit still forced
    "Comment BADGE", which drew her pushback.
- **Quit.** Consultant floor: 2 questions in one reply, a 752-word wall with no copy boxes, and no quiet option.

Acceptance [quit_points] (17):

| # | Quit point | Hit? |
|---|---|---|
| 1 | method file requested mid-session | no; S0 carried on in compact mode |
| 2 | Door B project that does not exist | n/a |
| 3 | save-for-reward gate | no; Week 1 always came before the card |
| 4 | nothing back during minutes 8–10 of the dump | no; every chunk answered within 0.5 min |
| 5 | brand wall with framework codes | **coldstart floor** (snake_case codes, `[today]`/`[plan_start]`). Handled in S1/S0 by the "no need to read" label, but the risk stays |
| 6 | paid stream parked with no bridge or side door | **consultant floor** (deal prep only as `side_door=…referral-only`, no DM route); S1/S0 routed side doors in DM reply 2 |
| 7 | "locked 90 days" | no |
| 8 | "new chat outside the project" | no |
| 9 | Mac mic not found | Linda got the Mac tip. **consultant floor** dropped the Windows tip for a Windows dictation user (same failure) |
| 10 | Claude save without a picture route or backup | **consultant floor** (no route, no backup). Consultant and linda S1 got words plus backup but no picture; Linda's persona "needs a picture-guided save" |
| 11 | keyword CTA with no quiet option | **coldstart floor, consultant floor** |
| 12 | email list ignored | **proof S0** (140-person list, no email), **consultant floor** (380-person list, no email) |
| 13 | two-device Weekly Talk or clip trimming | no |
| 14 | FB insights screenshots required | no |
| 15 | xưng hô asked late | n/a (EN) |
| 16 | reading the script while filming on the same phone | not hit, and not covered: FILM TODAY never says "memorise it" (start-block line 26 has "to memorise", but no run printed it), and the coldstart persona is phone-only |
| 17 | Notion-hosted setup page | no |

In all: 6 of the 17 were hit (5, 6, 9, 10, 11, 12), every one in a floor run, plus #12 in S0. None was hit in S1.

## 6. Prioritised fix list

Headroom today:
- Instruction block: now 6,286 bytes of ≤6,500 (measured against the current `dist`):
  - with K1, K3, K5, K6 and K7 applied: 6,454;
  - adding K17 and K19: 6,486;
  - adding K21, with the ALWAYS line dropped: 6,496.
  K12 is written below so that it costs nothing.
- §CM anchors (bytes of ≤2,800): SETUP 2,761 · CARD 2,696 · MAP 2,751 · EDGE 2,759 · VOICE 2,720 · TODAY 2,507 ·
  WEEK 2,385 · FORMATS 2,182 · CTA-KIT 2,183 · MESSAGES 1,983.

### Kit fixes

**P1: blocks acceptance**

K1. **No way to close a long dump.**
- Effect: film-ready >20 min in 9/9.
- Change: `core/en/start-block.md` line 23 (step 2), after `"Got it." + one jogger.`, add:
  ` Past ~10 min of talk: "That's plenty for today. Say 'done', or one more minute."`
  (+81 chars; put the text in a new `strings/en.toml` key such as `dump.enough`).
- Expected result: with a dump of about 10–12 min, film-ready lands around 16–18 min.

K2. **FILM TODAY waits for a separate OK turn, and a Claude Free coach who hits the limit there leaves with nothing to
film** (consultant S1: 5 hours).
- Change: print FILM TODAY in the same reply as the Map, under "OK, or change a line." A "change" reprints both.
  - `core/en/start-block.md` lines 25–26.
  - `modules/en/setup.md` line 23 (§CM-SETUP 9): `Map → "ok" → FILM TODAY → Week 1` becomes
    `Map + FILM TODAY → "ok" → Week 1` (−6 bytes).
- This saves 1 coach turn and 1–2 min in every run. It changes the order in wf15 §1.4–1.5, so it **needs a founder
  OK**. Without it, keep K1 and K18.

K3. **"One phone screen" can't hold Week 1 or the card, and "Shorter" can't be honoured.**
- Seen in: S1 ×5; coldstart S1 t10.
- Changes:
  - `core/en/start-block.md` line 12: `One phone screen.` becomes `One phone screen of talk; copy boxes don't count.`
    (+32).
  - `modules/en/levelup.md` line 8 (§CM-TODAY 1): `"Shorter": next reply ≤90 words` becomes
    `"Shorter": ≤90 words of talk; a due card or week prints its boxes only` (+40).
  - `modules/en/plan.md` line 17 (§CM-WEEK 10): add `Day 0: one line above each box, no other prose.` (+45).

K4. **Week-1 dates undefined** (three readings in 7 runs; the card contradicts the printed week; the Talk lands in
Week 1).
- Changes:
  - `modules/en/brain.md` line 16 (§CM-CARD 3): `plan_start = the Monday after Day 0` becomes
    `plan_start = the day after Day 0; week n = 7-day blocks from it` (+25).
  - `modules/en/levelup.md` line 11 (§CM-TODAY 4): `Talk day, or week 2+` becomes `Talk day in week 2+, or week 2+`
    (+8).
  - `schemas/brand-card.toml` `plan_start` note (L586): the same wording.

K5. **YOUR WORD ≠ CTA keyword in compact mode** (S0 2/2).
- Change: `core/en/start-block.md` line 25: `{{t:map.word}} from their clients' words` becomes
  `{{t:map.word}} the {KEYWORD}: from their clients' words` (+15).

K6. **Week-1 mix missing in compact mode, so the email list was ignored** (proof S0).
- Change: `core/en/start-block.md` line 27: drop the `{{#if phone}}…{{/if}}` guard around
  `3 shorts, 1 long post, 1 email or message.` so the kit target renders it too (+45).

K7. **"Messy is perfect." breaks "no praise"** (I17 in 8 runs).
- Change: `core/en/start-block.md` line 22 becomes `Messy is fine.` (−3).

**P2: real defects seen in 2+ runs**

K8. **Card enums.**
- Problems:
  - `delivery` has no "beat cards", the §CM-FORMATS default. Runs wrote "bullets", "word-for-word" or
    "beat cards".
  - `timezone` must never be blank, but it can't be asked on Day 0.
  - `tier=va` has no rules anywhere.
- Changes:
  - `modules/en/brain.md` line 15 (§CM-CARD 3): `delivery=beat-cards|interview|bullets|word-for-word`,
    `timezone=ask|{zone}`, `tier=lean|standard` (net +12).
  - `schemas/brand-card.toml` `delivery.options` gains `"beat-cards"`, and `timezone` accepts `"ask"`.

K9. **The keyword is counted "exactly once" while the default ask contains it** (all runs).
- Change: `modules/en/plan.md` line 11 (§CM-WEEK 4): `Keyword exactly once;` becomes
  `Keyword once, plus the ask;` (+5).
- Align acceptance [week] `keyword_exactly_once_rate` and wf11 §4 rule 7 to "outside the ask".

K10. **No rule for choosing a tier** (2 h/week gave Lean in proof but Standard in consultant, whose Week 1 ran 1,338
words).
- Change: `modules/en/plan.md` line 9 (§CM-WEEK 2): `Lean ≤60 min a week;` becomes `Lean (default) ≤60 min a week;`
  and `Standard ≤90 adds` becomes `Standard, only when asked, ≤90 adds` (+30).

K11. **A dump that already refuses comment asks still gets "Comment {KEYWORD}"** (Linda).
- Change: `modules/en/convert.md` line 10 (§CM-CTA-KIT 5): after `Never drop it yourself`, add
  `; a dump that refuses comment asks starts quiet` (+50).

K12. **The card box duplicates Map fields because start-block says "every Map field"** (all S1 runs added
known_for/topics/keyword).
- Change: `core/en/start-block.md` line 32: `every Map field and NOT NOW` becomes `the Map's details and NOT NOW`
  (+2). The schema already keeps message, topics and keyword in the top.

K13. **Kit example copied verbatim as content** (coldstart floor: Dana's "still in the job, or already out?" sent to
dads).
- Change: `modules/en/fmt-short.md` line 38 (§CM-MESSAGES 5): mark the examples `e.g.` and add `never these words`
  (+20).

**P3: one run or cosmetic**

K14. `strings/en.toml` `cta.by_hand` (L159): `Replies go by hand, you or your VA.` becomes `Replies go by hand.`
(3 coaches without a VA saw it).

K15. `strings/en.toml` `research.ask3` (L207): `Quick favour` becomes `Quick favor`. §CM-LOCALE 1 asks for US
spelling, and 3 runs printed "favour".

K16. **§CM-MESSAGES 5 DM reply 2.**
- Problems: it hard-codes a 15-minute call, and it has no route for a side door (3 runs improvised one).
- Change: `modules/en/fmt-short.md` line 38: `an invite to a 15-minute call (their length)` becomes
  `an invite to their usual call`, and add `side door asked → its price line` (+25).

K17. **Map `{promise as a range}` is undefined when the dump has no range** (service S1 spent its one question on
it).
- Change: `core/en/start-block.md` line 25: `{promise as a range}` becomes
  `{promise as a range, else their process}` (+16).

K18. **§CM-SETUP 10 can't be carried out** (the plan can't be seen and `{time}` is unknown).
- Changes:
  - `modules/en/setup.md` line 24: `Claude Free: after the dump and the Map:` becomes `On Claude, once under the Map:`.
  - `strings/en.toml` `save.limit_claude_free` (L108): `after {time}` becomes `when it resets`.
- Moot if K2 is accepted.

K19. **Step 3's buyer wording reads like a decision** (proof S0).
- Change: `core/en/start-block.md` line 24: `pick the ONE buyer who could buy more than one` becomes
  `guess the ONE buyer who could buy more than one ("Right?")` (+10).

K20. **"post the caption as text" leaves the hook out** (Linda).
- Change: `modules/en/fmt-short.md` line 12 (§CM-FORMATS 7): add `as text = first line + caption, one box` (+40).

K21. **Floor lane drops the running tag and copy boxes.**
- Change: `strings/en.toml` `contract.output` (printed as the first and last line) becomes
  `Always reply in English. First line ◆ Content Machine · <step>; pieces in copy boxes; one screen of talk; end with one NEXT line.`
  (+46 ×2).
- Pay for it by deleting start-block line 40 `ALWAYS: …`, which repeats EVERY REPLY (−81).

### Grader fixes

G1. **I8.**
- `tools/cmcore/checks.py` `numbers_in` (L196): make month-name dates ("Oct 8", "TUE, OCT 13", "Monday, Oct 19") and
  ISO dates structural, and make `401(k)`/`401k`/`403(b)` an id.
- `evals/graders.py` `i8_numbers` (L1078): skip `kind in ("date","time")`, and apply `COLD_RESULT_RE` only to
  `r.publishable()`, not to prose.
- Removes 8/8 FPs.

G2. **I6** `DECISION_RE` (L161) / `i6_decisions` (L1026): count distinct decisions (a repeated `map.ok` counts
once), and ignore the `setup.guess` / `setup.multi_income` questions, declarative "we pick", and UI clicks
("choose Add text content"). Removes 4/4 FPs.

G3. **I2** `i2_template` (L918): check prose only (`r.visible(("",))`); copy boxes are buyer-facing (§CM-CTA-KIT 2).
Removes 2/2 FPs and the derived quit_triggers template item.

G4. **I23** `i23_voice` (L1928).
- Add day-first titles (`^(?:mon|tue|…|sun)[a-z]*,? [a-z]{3} \d{1,2} · …`) to `FORMAT_TITLE_RE` (L110).
- `_voice_scrub` (L1907) should keep a quote that is a whole First line/Last line value or one of the coach's
  phrases.
- `voice_phrases` (L1854) should keep only the phrases the coach actually said in the run. Phrases that appear only
  in voice-samples.md reward leaks.

G5. **I11** `i11_injection` (L1210): skip `never_say` / `do_say` lines of the machine block.

G6. **quit_triggers** `words_before_usable` (L2040): stop at the early win's quoted lines, which are copy-ready, or
measure the longest single reply before something usable (≤300). Keep 300.

G7. **day0_timing** `check_day0` (L2086).
- Compute active minutes from a new transcript field `away_min`.
- When the running tag is missing, detect the Map by its labels and FILM TODAY by its title.
- Add a separate `running_tag` check on every reply.

G8. **New `day0_shape` checks** for defects that are ungraded today. Each would have caught a real defect in this
round:
- FILM TODAY has the quiet option and a caption copy box;
- YOUR WORD equals the CTA keyword;
- Week 1 has an email when the coach named a list >0;
- card top ≤500 chars — align acceptance `brand_card_visible_max_chars` (now 900) to wf15's 500;
- the save line has an app route and a backup;
- no unfilled placeholders (`[today]`, `[plan_start]`);
- "Shorter" gets ≤90 words of talk;
- no question about a fact given in an earlier coach turn.

G9. **Leak check in `evals/run.py grade`.** Flag runs of 5+ words in machine turns that appear in persona files but
not in earlier coach turns, and fail on any hit in Voice Card fields. This scan found leaks in 8/9 runs whose notes
said none.

G10. **I16** did not run in 9/9 runs: add `locales/en/examples.md`, or mark I16 n/a for Day 0.

### Simulator and protocol fixes

P1. **Leaks.**
- One agent plays both sides, and `COACH.md` sends it to `voice-samples.md` (and the run can see `expected.toml`).
- Fix: run the machine side as a separate agent that never gets persona paths; give the coach only `answers.md`,
  `written-posts.md` and `persona.toml` behaviour. Block "no leaks" in notes until G9 passes.

P2. **Persona dump length.**
- `persona.toml` says "2–4 minute chunks", but the `answers.md` chunks are 485–876 words (3.7–6.7 min); the dumps
  total 1,866–2,295 words (14–18 min).
- Fix: trim the chunks to ≤450 words, or label these personas as long talkers on purpose and keep at least one
  in-budget persona per lane.

P3. **t_min validation.**
- Both floor runs dictated 600–850 words in 0.3–2.5 min, which is impossible at 130 wpm.
- Fix: `evals/run.py` should reject t_min steps faster than 130 wpm dictation, 30/40 wpm typing or 200 wpm reading,
  and require `away_min` for site visits and plan limits.

P4. **Transcript integrity.**
- Coldstart floor t10 has no machine reply (two coach turns in a row).
- Consultant floor never pasted W1/W2 (`COACH.md` step 2). Its quit was inferred after the fact from the grader, with
  no quit line, and its notes contradict themselves ("No quit triggers fired" and "Quit triggers fired").
- Fix: `run.py` should check that turns alternate, that the required pastes are there, and that a quit has an
  explicit quit line.

P5. **Packet.**
- `MACHINE.md` says "ChatGPT or Claude", so 7 runs printed both save routes and 2 guessed Claude. Name the app the
  machine runs in, which a real model knows, but not the plan.
- `answers.md` sets the coldstart Day 0 on Sunday 2026-10-11, but the packet date is Tue 2026-10-06.

P6. **Free-plan limit.**
- Modelled for consultant but not for proof-coach ("may hit around turn 9"), in both S1 and S0.
- Fix: model it, or record it as skipped in `meta.json`.

P7. **Floor notes are unreliable.** The coldstart floor notes call real failures false positives: no running tags,
"Perfect.", re-asked facts. Floor runs need this reviewer pass, or notes generated from `grades.json` and the
transcript.
