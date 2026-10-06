Result: FAIL

# G2 EN Day-0 golden round: independent review

Build `8c470d4cdd28`. Kit under test: each run's `packet/kit/`, identical to the current `dist/en`
(`1-INSTRUCTIONS.txt` md5 fa410b44…, 6,617 B / 6,463 NFC chars; `CONTENT-MACHINE-EN.md` 48,428 B). Working tree clean.

How this review was done:
- All 8 transcripts were read in full, as the coach would read them.
- Scratch copies of the 8 folders were re-graded with the current `evals/run.py`/`graders.py`. The verdicts match the
  stored `grades.json` exactly. The run folders were not touched.
- Leaks were checked three ways in all 7 valid runs (more than the 3 asked for):
  - a separate 5-gram scan against every persona file, minus earlier coach turns and the kit;
  - a scan for numbers and proper nouns the coach never said;
  - a hand check of each hit.
- Each failed check is traced to the transcript line and to the kit line or the grader code behind it.

Why FAIL:
- **The Day-0 budgets still fail in 4 of the 7 valid runs.**
  - The Map came at coach turn 7 in 3 runs (proof S1, proof S0, Linda). In round 1 only 1 of these 7 personas
    went past 6.
  - Film-ready was over 20 active minutes in 2 runs: consultant 23.0 and Linda 27.3.
  - Proof S0 was film-ready at exactly 20.0.
- **K1 (the dump cut-off) saved minutes but added a turn and lost facts.**
  - Its line "Say 'done', or one more minute." costs a round trip.
  - It skips chunk 3, so the 140-person list and the platform (Instagram) in both proof runs, and Linda's refusal of
    comment asks, were never heard.
  - As a result, quit point #12 (email list ignored) is hit by omission in 2 runs, and the card stores
    `list_size=0` as fact (I8).
- **Real defects remain in 6 of the 7 valid runs** once the false positives are taken out. Only service-biz S1
  would pass.
- **8 of the 19 failed items in valid runs are grader false positives.** Six of them are one new class: the
  YOUR WORD line written in the K5 wording.
- **The floor lane is still invalid** (turns, pace, leaks). It also prints a false client result in a public email.
- **The single Week-1 + card reply now runs 1,523–2,426 words.**
  - "Shorter" cannot be honoured when the card is due.
  - Two cards are over the 5,700-character limit.

## 1. The runs

"Map turn" is the number of coach turns up to the Map. With K2, the film-ready turn is the same turn.

Film-ready is in active minutes; clock time is in brackets where the coach was away.

Verdict codes: R = real defect, FP = grader false positive, R(kit) = the kit caused it, R(m) = machine slip.

| Run | Lane · app | Valid | Outcome | Coach turns | Map turn | Film-ready | Failed (grader) | Verdict per failed item |
|---|---|---|---|---|---|---|---|---|
| proof-coach S1 | S1 · ChatGPT Free | yes | Map + video, Week 1 + card, no quit | 8 | 7 | 19.1 | I8, day0_timing, day0_shape | I8 R(kit) · Map 7 R(kit) · YOUR WORD FP |
| proof-coach S0 | S0 · ChatGPT Free | yes | same | 8 | 7 | 20.0 | I12, day0_timing, day0_shape | I12 R(kit, compact) · Map 7 R(kit) · YOUR WORD FP |
| coldstart-coach S1 | S1 · ChatGPT Plus, iPhone | yes | same | 6 | 5 | 14.3 | I23, day0_shape | I23 R (low) · YOUR WORD FP · no save backup R(m) · "Shorter" R(kit conflict) |
| consultant S1 | S1 · Claude Free | yes | same; 5-h limit break after the Map | 7 | 6 | 23.0 | day0_timing | film-ready 23.0 R(kit): the cut never fired |
| linda S1 | S1 · Claude Pro, Mac | yes | same; 2 pushbacks handled | 8 | 7 | 27.3 | day0_timing, day0_shape | Map 7 R(kit) · film-ready 27.3 R(kit + slow typist) · YOUR WORD FP · `[name]` FP |
| service-biz S1 | S1 · ChatGPT Plus | yes | same | 5 | 4 | 16.1 (56.1) | day0_shape | YOUR WORD FP |
| service-biz S0 | S0 · ChatGPT Plus | yes | same | 7 | 6 | 16.9 (61.9) | I9, day0_shape | I9 FP · YOUR WORD FP · `[name]` R(m, minor) |
| consultant floor | floor · Claude | **no**: turns, pace, leaks | Week 1 over 3 machine turns in a row, card, no quit | 9 | 7 | invalid (11.5 on compressed `t_min`) | quit_triggers, day0_timing, day0_shape | all R (floor); not counted |

Totals:
- **Grader passes: 0 of 8.**
  - Valid runs: 7 of 8. In round 1 it was 3 of 9 once the leak check ran.
  - Quits: 0.
  - Every run came back the next day ("comes back"), per the simulator.
- **Failed items in the 7 valid runs: 19.**
  - 11 are real: 6 R(kit), 3 R(m), 1 R (low, a proxy check), and 1 R(kit + persona).
  - 8 are false positives: 6 × YOUR WORD, 1 × `[name]`, 1 × I9.
- **The floor run has 4 real items.** It is invalid and is not counted.
- **Two summary-table bugs:**
  - The floor row's Run cell is blank: its `grades.json` has `"run": ""`, because it was graded from inside the folder.
  - The "Film-ready min" column prints clock time (56.1, 61.9) for runs whose active time passes.

## 2. Day-0 shape and budgets (wf15 §1 as amended; acceptance `[day0]`)

Key: ✓ = matches · ~ = partly · ✗ = missing or wrong.

| Step / budget | proof S1 | proof S0 | cold S1 | cons S1 | linda S1 | svc S1 | svc S0 | floor |
|---|---|---|---|---|---|---|---|---|
| Start: setup line, promise, mic tip, dump prompt + posts/link | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Early win after chunk 1 (min after dump start; acceptance ≤4, ungraded) | ✓ 6.5 | ✓ 6.4 | ✓ 5.5 | ✓ 6.2 | ✓ 8.0 | ✓ 6.2 | ✓ 6.6 | ✓ |
| Dump closed by the K1 line | ✓ after c2 | ✓ after c2 | ✓ after c2 | ✗ jogger, c3 dictated | ✓ after c2 | ✓ after c2 | ✓ after c2 | ✓ |
| Missing facts ≤3, one a message, each a guess | ✓ 2 | ~ 2; consent guessed "OK'd" | ✓ 0 | ✓ 1 | ~ 2; first one reads as unheard | ✓ 0 | ✓ 1 | ✗ 3, 1 re-ask |
| Map: 4 lines + "OK, or change a line." last | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ 3 labels |
| FILM TODAY in the Map reply (K2) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Caption copy box + quiet option | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ instructions inside the box |
| Week 1 on the next answer, one reply with card + save + NEXT | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ 3 machine turns, no coach turn |
| Week-1 mix by platform/list | ~ no email: list never heard | ~ same | ✓ | ✓ email first (380) | ✓ email first (guess) | ✓ email first (guess) | ✓ | ~ email says "comment" |
| Card top ≤500 chars | ✓ 465 | ✓ 371 | ✓ 466 | ✓ 466 | ✓ 473 | ✓ 475 | ✓ 370 | ✓ 351 |
| Whole card ≤5,700 (`schemas/brand-card.toml` whole_chars) | ✗ 5,893 | ✓ 3,675 | ✓ 5,579 | ✗ 6,090 | ✓ 5,370 | ✓ 5,118 | ✓ 3,887 | ✓ |
| Save line: route + backup | ✓ | ✓ | ✗ no backup, no app name | ✓ | ✓ | ✓ | ✓ | ~ no "Save this…" line |
| NEXT | ✓ | ✓ | ✓ | ✓ | ✓ (adapted to text) | ✓ | ✓ | ✗ "NEXT → Done." |
| **Map ≤6 coach turns** | ✗ 7 | ✗ 7 | ✓ 5 | ✓ 6 | ✗ 7 | ✓ 4 | ✓ 6 | ✗ 7 |
| **Film-ready ≤20 active min** | ✓ 19.1 | ✓ 20.0 (at the limit) | ✓ 14.3 | ✗ 23.0 | ✗ 27.3 | ✓ 16.1 | ✓ 16.9 | invalid |
| **≤10 coach turns** | ✓ 8 | ✓ 8 | ✓ 6 | ✓ 7 | ✓ 8 | ✓ 5 | ✓ 7 | ✓ 9 |
| Session ≤40 active min | ✓ 22.0 | ✓ 23.6 | ✓ 16.5 | ✓ 25.3 | ✓ 32.0 | ✓ 21.5 | ✓ 19.3 | – |
| Week-1 reply length (words) | 1,907 | 1,523 | 1,930 | 2,426 | 2,003 | 2,172 | 1,876 | 3 replies |

Where the turns go: every run where the Map came at turn 7 has the same shape:
- Start;
- chunk 1;
- the posts paste;
- chunk 2, after which the machine says "That's plenty for today. Say 'done', or one more minute.";
- "done";
- 2 one-a-message checks.

That is 7 coach turns. Without the "done" round trip, all three would land at 6.

Where the minutes go:
- The dump's first two chunks run 11–14 minutes of talk.
- The cut can only fire between chunks, and the personas send 5–8-minute chunks (the kit asks for 2–3).
- Each typed answer costs 1.5–5.6 minutes.

## 3. Leak spot-check (all 7 valid runs, plus the floor)

The protocol check gives 0 fails in the 7 valid runs. My separate scans agree that no persona fact appears before
the coach said it. Every 5-gram hit is a join of the coach's own words (field labels, reordered list items, or two
quotes run together). The proof S1 KNOWN FOR, consultant's clients and numbers, Linda's three clients and service's
Priya figures were each traced to a coach turn.

Weak suspects (wording, not facts):

| Run | Machine text | Persona source | Coach said |
|---|---|---|---|
| coldstart S1 t6 card | `proof: own: … carries both kids up the stairs at once` | persona.toml / launch-brief proof text "both kids up the stairs at once" | "at the same time" |
| coldstart S1 t6 card | `audience_address: you (one dad)` | expected.toml `"you (one dad to another)"` | – (an inference that fits) |
| service S1 t4 | First frame "a roll of blue painter's tape" | voice-samples.md "Get a roll of blue painter's tape" | "painters tape, the blue kind" (a common phrase) |

Talk-day guesses: coldstart Sunday and Linda Monday both match persona.toml. Each also matches a cue in the run:
coldstart's Day 0 is a Sunday, and Linda's dump keeps saying "Monday". Not counted.

The floor has 4 real leaks, all marked fail by the protocol check:
- `bio_line … CPA, Illinois`;
- `timezone America/Chicago` and "Wednesday 7 to 8 in the morning **Central**";
- a never_say list copied from the persona's never-list;
- `side_door … (referral only)`.

None of these was said by the coach.

**Protocol concern.** Four simulators edited machine turns after a first INVALID grade: proof S1, consultant S1,
service S1 and service S0. They reordered or rewrote Voice Card lines. Three of those first fails were the leak
check's own false positive:
- `evals/run.py` `check_leaks` (L578) builds its corpus from whole `.toml`/`.md` files, so a TOML key sits next to
  its value. For example, `openers_closers = ["Here's the thing nobody…"]` yields the 6-gram "openers closers
  here's the thing nobody".
- A card line `openers_closers: "Here's the thing nobody tells you." …` then matches it, although the coach pasted
  that line herself (W1).
- Reordering the items "fixed" it.

The edits are logged in notes.md, and none changes a fact. But it means the leak rate this round reports is
partly hand-tuned (see G18 and P8).

## 4. Failed grader checks: real or false positive

| # | Run · check | Transcript line | Kit line or grader code | Verdict |
|---|---|---|---|---|
| 1 | proof S1 · I8 `"0" not in allowed_numbers` | t8 card box: `… platform=facebook owned_channel=none list_size=0 cta_style=keyword …` | §CM-CARD 3 (`modules/en/brain.md` L15): `list_size` has no unknown value and the box is "never blank". §CM-SETUP 5 (`modules/en/setup.md` L15): list size is "Never asked on Day 0". Her 140 is in chunk 3, which was never dictated | **R (kit)**. A guess is stored as fact, and it drives "List 0: no email" |
| 2 | proof S1 · day0_timing, Map after 7 | t4 "That's plenty for today. Say 'done', or one more minute." → t5 "done…" → t5 streams guess → t6 consent guess → t7 Map | start-block L23 + `strings/en.toml` L106 `dump.enough`; step 3 "one per message" | **R (kit)**: the "done" round trip |
| 3 | proof S1 · day0_shape YOUR WORD | t7 `YOUR WORD: TOO LATE, from "Is it too late for me?", what every client asks on the first call (my guess)`; CTA "Comment TOO LATE" | `graders.py` `_norm_word` (L2953) strips only "(my guess)". The kit template "YOUR WORD: the {KEYWORD}: from their clients' words" invites the note | **FP** |
| 4 | proof S0 · I12, first lines of 13 and 15 words | t8 SHORT 2 "You apply online with a whole career behind you, and you hear nothing."; SHORT 3 "If they handed you a box on the way out, what goes in the box?" | Kit L20 (start-block L26) caps only "3 beats ≤12 words". The first-line cap is in §CM-FORMATS 1, which compact mode does not have | **R (kit, S0)** |
| 5 | proof S0 · Map after 7 | t4 plenty → t5 "done" → consent + result guess → t6 streams guess → t7 Map | as #2 | **R (kit)** |
| 6 | proof S0 · YOUR WORD | t7 `YOUR WORD: CHAPTER (Lorraine's "one more chapter")`; "Comment CHAPTER" | as #3 | **FP** |
| 7 | coldstart S1 · I23, 2 of 6 pieces (33%) | FILM TODAY, N1, N2 and DM reply 1 use none of his card phrases ("You're not lazy, you're booked.", "Zero is the killer.", "I'm not gonna lie", …). The long post and N3 do | §CM-VOICE 7 "one of their phrases … where it fits"; I23 proxy ≥50% (`i23_voice` L2317) | **R (low)**. The pieces are in his words (the soccer dad, the 2015 gym member), but no card phrase. N2's "my real test" is a partial match of "honestly that's my real test" |
| 8 | coldstart S1 · YOUR WORD | t5 `YOUR WORD: "keep up" (what dads keep saying to you)`; "Comment KEEP UP" | as #3 | **FP** |
| 9 | coldstart S1 · save line has no backup | t6 "Save this so I remember you (30 s). ⋯ under the card → Save to project." | Kit L27 has "Backup: email it to yourself."; §CM-CARD 1 (`brain.md` L8) names only "the app's route" | **R (machine; the anchor invites it)** |
| 10 | coldstart S1 · 164 words of talk after "Shorter" (max 90) | t6 coach "ok. quiet. Bro I'm on my phone. Shorter." → a 1,930-word reply. Of the 164 talk words, 97 are the card title, the top and the "no need to read" heading. The rest (67) is under 90 | §CM-TODAY 1 (`modules/en/levelup.md` L8) "a due card or week prints its boxes only" conflicts with §CM-CARD 2's plain-line top. The grader (L3084) counts the top as talk | **R (kit conflict)**. The coach asked for shorter and got about 10 phone screens |
| 11 | consultant S1 · film-ready at 23.0 | t4 at 13.5 min: 1,282 dictated words (≈11.4 min) plus the paste, then "Got it. Next: what you sell, and what it costs." (a jogger). Chunk 3 followed: 845 words, 6.9 min | Kit L17 "Past ~10 min of talk": the model cannot see minutes, so the trigger is not observable | **R (kit)** |
| 12 | linda · Map after 7 | t4 plenty → t5 "Okay. Done." → t5 result guess → t6 offer guess → t7 Map | as #2 | **R (kit)** |
| 13 | linda · film-ready at 27.3 | The cut came at min 16.5 (chunk 1 7.7 min + posts 2.0 + chunk 2 5.6). Then two typed answers: 5.6 and 4.1 min. The first guess, "My guess: no client result to show yet, so I'll use your own story. Right?" (t5), came after she had named 3 paying clients | `setup.guess_no_result` (strings L254) is used for "clients without an outcome"; step 3 allows 2 questions for a slow typist | **R (kit + persona)**. Saving the "done" turn takes off only ~0.5 min here |
| 14 | linda · YOUR WORD | t7 `YOUR WORD: BADGE (your clients' word: "without the badge")`; "Comment BADGE" | as #3 | **FP** |
| 15 | linda · placeholder `[name]` | t8 card box: `client_words: … I've been [name] from sales since 1996. Who is [name]?` | `PLACEHOLDER_RE` (L268) reads a deliberate redaction in the private card as a template slot | **FP**. Kit note: the other runs keep client names in the card. §CM-SETUP 1 "client names only with their OK" does not say whether that covers the card |
| 16 | service S0 · I9 "can you do my room" | t7 box label `DM REPLY 1 · someone asks the price, or "can you do my room"` | `i9_quotes` (L1450): `ck.quotes_in` takes "someone asks … "…"" as an attributed quote | **FP**: a hypothetical incoming DM in a label |
| 17 | service S0 · YOUR WORD | t6 `YOUR WORD: the nothing room`; "Comment NOTHING ROOM" | as #3. The literal "the" comes from the K5 kit wording "the {KEYWORD}" | **FP** (caused by the kit wording) |
| 18 | service S0 · placeholder `[name]` | t7 `TEXT TO 3 PAST CLIENTS … Hi [name], quick one…` | Kit line 7 "Never show templates". Compact mode has no ask-3 text (`research.ask3`) | **R (machine, minor)**. The grader misses the same slot in proof S1 t8, "Hi {first name},", because `{first name}` has a space |
| 19 | service S1 · YOUR WORD | t4 `YOUR WORD: MISTAKE: from your clients' "I'm terrified of making an expensive mistake." (my guess)` | as #3 | **FP** |

Floor (invalid, not counted), all real:
- quit_triggers: t9 runs 334 words with no copy box.
- day0_timing: the Map comes at turn 7 with 3 labelled lines ("TOPICS:" instead of "3 TOPICS:").
- day0_shape: t10 has no "Save this so I remember you" line.
- Not graded: a false result. In t9's public email, "his biggest client went from minus 6 percent to 51 percent" fuses two true figures (that client was at −6%; delivery margin went 38 → 51%). It repeats in t3 and t5. I8 cannot catch two allowed numbers that are mis-paired.

## 5. Read as the coach

**proof-coach S1 (Dana, ChatGPT Free, skims past one screen):**
- At t5 (min 15) she says "I'm starting to wonder if this was a waste of money". Nothing usable arrives before
  min 19.1. The early win is three quotes, not a post.
- The checks come one a message: the buyer guess, then the consent guess. The consent guess is safe ("haven't OK'd
  … I'll lead with your own story").
- The Week-1 reply is 1,907 words (~10 screens). About 5,400 of its characters are the card box.
- Three guesses are wrong, and she will need three one-word fixes tomorrow:
  - platform Facebook (she is Instagram-first);
  - talk day Monday (her mother's day);
  - no email for her 140-person list.

  The guess line names platform and talk day, but not the list, so she cannot see that one.
- Resume reviews "stay on offer in your DMs", but the Week-1 DMs have no route or price for them.

**proof-coach S0:**
- Same impatience at min 15.
- The consent guess defaults to "OK'd" ("My guess: Lorraine, Bev and Gail OK'd you sharing … Right?"). On "skip",
  that is an unsafe default.
- KNOWN FOR is 41 words, not one breath.
- Two hooks are over 12 words.
- FILM TODAY says "say it from memory" (good for quit point #16).

**coldstart-coach S1 (Dan, phone only):**
- The smoothest run: 6 turns, film-ready at 14.3, no questions (correct: no clients).
- He wrote "Bro I'm on my phone. Shorter." and got 1,930 words.
- The save line lacks "ChatGPT:" and the backup, so on an iPhone he has one route and no fallback.
- DM reply 2 points to "part 2 is on my page", a post that goes up 6 days later.

**consultant S1 (Erin, Claude Free):**
- Chunk 3 was taken as dump (no cut), so the Map came at min 23.
- The Claude limit line worked as designed: she left for 5 h with FILM TODAY in hand and came back with "next".
- The Week-1 reply is 2,426 words: an email first to her 380, 2 posts, a 12-slide PDF post, a Dee short, and DM
  reply 2 with the $275 deal-prep branch.
- Her card is 6,090 characters, over the 5,700 budget.
- Her plain "talk day Wednesday (my guess)" repeats a day she stated.

**linda S1 (Claude Pro, Mac, slow typist):**
- She dictated with fn-fn (Mac tip worked).
- The first check, "no client result to show yet", came right after she named Renee, Joan and Carol, so it reads as
  if she was not heard. She corrected it in a 160-word typed answer.
- "Comment BADGE" drew her verbatim pushback. Her refusal sat in the unheard chunk 3, so K11 could not fire.
- The machine switched to quiet in one line and reprinted today's caption as text. The NEXT became "Post today's
  caption as text." Well handled.
- The card box shows her parked life-coaching topics under not_now. That is her "parking lot" pushback trigger,
  but she does not read the box.

**service-biz S1 (Corinne):**
- Fastest: Map at turn 4, active min 16.1, after a 40-min site visit.
- The email leads Week 1 on `list_size: 300+ (my guess)`, a guess she never sees.
- Talk day Wednesday is arbitrary.
- 2,172 words to skim. Bree, her VA, can copy every box.

**service-biz S0:**
- One question (the buyer). FILM TODAY "to memorise" (UK spelling).
- The past-client text is a template ("Hi [name]").
- The "no need to read" box shows MAP / PROOF / TRAIT / ENEMY / NOT NOW labels.

**Asked twice:** none in S1/S0. The floor re-asked the clients' exact words (t6, "Ask 3").

**Reading load:**
- Talk before the Map stays short: the setup reply is 123–129 words and every later reply is ≤76.
- The Map + FILM TODAY reply is 239–303 words.
- The load is all in the one Week-1 + card reply: 1,523–2,426 words, about 8–12 phone screens.

**Impatience:** the persona trait "nothing usable by minute 10" fired in 4 of 7 runs (both proof runs, both
service runs), because the first usable piece comes with the Map at min 14–27.

Acceptance `[quit_points]` (17):

| # | Quit point | This round |
|---|---|---|
| 1 | method file requested mid-session | no |
| 2 | Door B project that does not exist | n/a |
| 3 | save-for-reward gate | no; Week 1 always came before the card |
| 4 | nothing back during min 8–10 of the dump | no; every chunk was answered within 0.5 min |
| 5 | brand wall with framework codes | handled by the "no need to read" label. The risk stays: S1 boxes carry `pack_version`, `cta_style`, `proof_ready=yes`; S0 boxes carry TRAIT/ENEMY/NOT NOW. Linda's quit list includes "codes or a long brand wall" (no quit) |
| 6 | paid stream parked with no bridge or side door | no; consultant and service route theirs in DM reply 2 with a price. Proof's resume reviews: "stay on offer in your DMs", no DM line |
| 7 | "locked 90 days" | no |
| 8 | "new chat outside the project" | no |
| 9 | Mac mic not found | no; Linda used the Mac tip |
| 10 | Claude save without a picture route or backup | no; the Claude route + backup are printed (consultant, Linda, floor) |
| 11 | keyword CTA with no quiet option | no; 8/8 offer quiet |
| 12 | email list ignored | **hit by omission: proof S1, proof S0** (the 140 list is in the cut chunk 3; no list in the guess line) |
| 13 | two-device Talk or clip trimming | no |
| 14 | FB insights screenshots | no |
| 15 | xưng hô asked late | n/a (EN) |
| 16 | reading the script while filming on the same phone | not hit; partly covered. Only the S0 runs print "to memorise" / "say it from memory"; §CM-FORMATS 5's title "FILM TODAY · under 30 s" drops it in S1, including for phone-only coldstart |
| 17 | Notion-hosted setup page | no |

Hit: #12 in 2 runs (round 1: 6 points hit, all in the floor runs or S0).

## 6. Round 1 → round 2, item by item

Numbers on the 7 personas both rounds ran in S1/S0:

| Run | Coach turns R1 → R2 | Map turn R1 → R2 | Film-ready active R1 → R2 |
|---|---|---|---|
| proof S1 | 9 → 8 | 6 → **7** | 24.5 → 19.1 |
| proof S0 | 9 → 8 | 6 → **7** | 25.0 → 20.0 |
| coldstart S1 | 10 → 6 | 6 → 5 | 21.4 → 14.3 |
| consultant S1 | 10 → 7 | 7 → 6 | 27.5 → 23.0 |
| linda S1 | 9 → 8 | 6 → **7** | 29.9 → 27.3 |
| service S1 | 9 → 5 | 6 → 4 | 23.8 → 16.1 |
| service S0 | 8 → 7 | 5 → 6 | 21.4 → 16.9 |

What the numbers show:
- Film-ready: median 24.5 → 19.1; within 20 minutes in 0/7 → 5/7.
- Map ≤6 turns: 6/7 → 4/7 (worse).
- Coach turns: median 9 → 7.
- Valid runs: 3/9 → 7/8.
- Real failed checks (FPs removed): 12 across the 7 runs in R1 → 9 in R2.
- The coldstart floor was not re-run.

| Fix | Worked? | Evidence |
|---|---|---|
| K1 close a long dump | **partly** | Fired in 6/7 plus the floor. It did not fire in consultant S1: no observable trigger, so film-ready was 23.0. **New cost:** "Say 'done', or one more minute." adds a turn (Map 7 in 3 runs), and skipping chunk 3 loses lists, platform, consent facts and Linda's refusal |
| K2 FILM TODAY in the Map reply | **yes** | 8/8, with "OK, or change a line." last. Film-ready is now the Map turn (−1 turn, −1–3 min per run). Consultant hit the Claude Free limit right after it and still had a video to film |
| K3 talk vs boxes / "Shorter" / Day-0 one line above boxes | **partly** | Talk outside boxes is short. "Shorter" still fails (the card top is 97 words of talk). `film.list_open` adds a second line above the first short in 4 runs: §CM-FORMATS (fmt-short L19) vs §CM-WEEK 10 (plan L17) |
| K4 Week-1 dates | **yes (S1)** | plan_start = Day 0 + 1 and the Week-1 dates agree in 5/5 S1 runs; trial_ends = +25 in 5/5. S0 starts Week 1 today (no method file), but is self-consistent |
| K5 YOUR WORD = the keyword | **yes in substance; new grader FP** | The same word in 8/8 (S0 "COFFEE"/"TAPE" mismatches gone). The wording "the {KEYWORD}: from their clients' words" produced "the nothing room" and source notes, giving 6 FPs |
| K6 Week-1 mix in all lanes | yes | S0: 3 shorts, a long post, an email or message |
| K7 "Messy is fine." | yes | I17 clean in 8/8 |
| K8 card enums | yes | `delivery=beat-cards`, `timezone=ask` or a zone, `tier=lean` |
| K9 keyword once, plus the ask | mostly | 3 shorts break it: proof S1 N2 and N3 carry it only in the ask; service S1 N1 not at all. Not graded on Day 0 |
| K10 Lean default | yes | 7/7 lean |
| K11 a refusing dump starts quiet | not exercised | The refusal was in Linda's skipped chunk 3; her pushback fired and was handled in one line |
| K12 Map details only | yes (S1) | No known_for/topics/keyword duplicates in S1 cards. S0 still prints a MAP block |
| K13 kit example words | yes | Own DM questions in S1/S0. The floor's "still in the role… or already working with a numbers person?" is still kit-shaped |
| K14 "Replies go by hand." | yes | Consultant's DM reply 1 label |
| K15 "Quick favor" | yes | 5/5 S1 |
| K16 DM reply 2 | yes | Their own call. Side-door price lines: consultant $275, service S1 $18,000. Proof S1 has no price, so no branch |
| K17 range, else process | yes | No question spent on a range; service S1 asked 0 |
| K18 Claude limit line | yes | Printed once under the Map (consultant, Linda); consultant used it |
| K19 "guess the ONE buyer" | yes | No I6 hits |
| K20 as text = first line + caption | yes | Linda's text-post box starts with the first line |
| K21 contract line | yes for tags | `running_tag` 100% in 8/8, the floor included. The floor still prints Week 1 with no copy boxes |
| Also settled: Week 1 + card + save in one reply | yes, at a cost | Saves the card turn (session turns 5–8, down from 8–10). The reply is now 1,523–2,426 words; "Shorter" can't be met; 2 cards are over 5,700 |
| G1–G10 graders | held | No date/401k I8 FPs, no I17/I6/I2/I11 FPs, I23 split OK. G7 `away_min` works (service runs). G8 `day0_shape` caught 4 real items, plus a new FP class (YOUR WORD, `_norm_word`) |
| P1–P7 protocol | partly | P1: leaks gone from S1/S0 facts, still in the floor, and the leak check's TOML-key FP drove machine-turn edits. P2: still long talkers; the early win comes 5.5–8 min after the dump starts, against the acceptance limit of 4, which is ungraded. P3/P4: the pace and turns checks caught the floor; the required-paste check is still missing (the floor never pasted W1/W2). P5, P6: yes. P7: floor notes still unreliable (its "kit_breaks" are grader complaints and advise compressing the persona) |

New breaks this round:
1. **The "done" round trip:** +1 coach turn in every run where the cut fires and a question is still needed.
2. **Facts lost to the cut, and the guesses are invisible:**
   - list (proof 140), platform (proof: Instagram), consent scope, Linda's refusal;
   - `list_size` has no unknown value (`0` stored as fact; I8);
   - the list guess never shows to the coach.
3. **YOUR WORD FPs** (6) from the K5 wording.
4. **One ~2,000-word Week-1 + card reply:** "Shorter" conflict; whole card over 5,700 in 2 runs.
5. **The consent guess has no safe default** (proof S0 guessed "OK'd").
6. **The leak check's TOML-key FP leads simulators to edit machine turns** after grading (4 runs).

## 7. Prioritised fix list

Budgets now:
- EN instruction block: 6,463 of 6,500 chars. K22, K23, K25 and K26 together net −14, giving 6,449 (6,460 with K31).
- EN anchors (of 2,800 B; measured here with the heading line, and lint passes): SETUP 2,792 · MAP 2,783 · EDGE 2,759 · CARD 2,743 · VOICE 2,720 · TODAY 2,584 · WEEK 2,467 ·
  FORMATS 2,282.
- VN instruction block: 7,493 of 7,500 chars.
- VN method file: 56,311 of 56,320 B. Each VN mirror below names its cut.

### Kit fixes

**P1: blocks acceptance**

**K22. Drop the "done" round trip, and give the cut a trigger the model can see.**
- Seen in: Map 7 in proof S1, proof S0 and Linda; consultant's cut never fired.
- Changes:
  - `core/en/start-block.md` L23: `Past ~10 min of talk: "{{t:dump.enough}}"` becomes
    `Past ~1,200 words of talk: "{{t:dump.enough}}" + step 3 now.`
  - `strings/en.toml` L106 `dump.enough`: `That's plenty for today.` (drop "Say 'done', or one more minute.").
  - EN −13 chars.
- Expected effect:
  - Map at 6 in all three runs;
  - consultant cut after chunk 2, film-ready ≈16–18;
  - proof S1/S0 ≈18–19.
- VN:
  - `core/vn/start-block.md` step 3: `quá ~10 phút: "{{t:dump.enough}}"` becomes `quá ~1.500 tiếng: "{{t:dump.enough}}" + bước 4 luôn.`
  - `dump.enough` = "Hôm nay vậy là đủ rồi."
  - Net −16 chars; no cut needed.
- `COACH.md` already says to answer what the machine asks, so the simulator needs no change.

**K23. YOUR WORD wording (EN only; VN already reads "{KEYWORD}, từ lời khách").**
- Change: start-block L25 `{{t:map.word}} the {KEYWORD}: from their clients' words` becomes
  `{{t:map.word}} {KEYWORD}, from their clients' words` (−4).
- This stops the literal "the". Pair it with G11, which removes all 6 FPs.

**K24. Unknown list size, and a list guess the coach can see.**
- Seen in: I8 in proof S1; quit point #12 by omission in proof S1/S0; service's email leads on an invisible
  "300+ (my guess)".
- Changes:
  - `modules/en/brain.md` L15 (§CM-CARD 3): `list_size` becomes `list_size=ask|{n}` (+8 B).
  - `strings/en.toml` L256 `setup.plan_guess`: insert ` · {email list | no list}` before ` (my guess; …)` (+26 B in
    §CM-SETUP 5).
  - Pay for it by cutting `Hedge: "{{t:check.bet}}" once. ` from §CM-SETUP 4 (`modules/en/setup.md` L14, −50 B; used
    in no G1/G2 run).
- Result: SETUP 2,768, CARD 2,751.
- VN: same three edits.
  - Cut `Nước đôi: "{{t:check.bet}}" một lần.` from `modules/vn/setup.md` L17 (−84 B).
  - Add `list_size=ask|{n}` (+8) and ` · {email | chưa có danh sách}` (+34).
  - Net −42 B.

**K25. First-line cap in the kit block** (I12 in proof S0; compact mode has no §CM-FORMATS).
- Change: start-block L26 `first line word-for-word` becomes `first line ≤12 words, word-for-word` (+11).
- Fix the spelling on the same line: `to memorise` becomes `to memorize` (US spelling, §CM-LOCALE 1; 0).
- VN: `câu đầu nguyên văn` becomes `câu đầu ≤18 tiếng, nguyên văn` (+11), paid by K26's cut.

**P2: real defects in 1–2 runs, or a safety default**

**K26. Fold the client's OK into the result check, with a safe default.**
- Seen in: proof S0 guessed "OK'd"; proof S1 spent its check on consent.
- Change: start-block L24 `the best result (never invent)` becomes
  `the best result + the client's OK (never invent; unsure: no)` (+30).
- Pay for it by cutting ` Offer calendar reminders in one line.` from start-block L29 (−38). This duplicates
  §CM-TODAY (`levelup.md` L18 "Day 0's last reply … `levelup.offer_reminders`"), which S1 keeps; S0 loses the
  offer on Day 0.
- VN: `kết quả tốt nhất (không bịa)` becomes `kết quả tốt nhất + khách đồng ý chưa (không bịa; không chắc: chưa)` (+38).
  Cut ` Mời đặt nhắc lịch, một dòng.` from VN step 9 (−29).
- VN block total with K22, K25 and K26: net +4, giving 7,497/7,500.

**K27. "Shorter" when the card is due** (coldstart: 1,930 words after "Shorter").
- Change: `modules/en/levelup.md` L8 (§CM-TODAY 1): `a due card or week prints its boxes only, no apology.` becomes
  `a due week prints its boxes only, the card on the next message; no apology.` (+22 B; TODAY 2,606).
- This follows the §CM-SETUP 9 precedent "app cuts it: card next".
- VN: `modules/vn/levelup.md` "Ngắn thôi" line, same edit (+11 B), paid by K24's VN cut.

**K28. Save line backup** (coldstart).
- Change: `modules/en/brain.md` L8 (§CM-CARD 1): `+ the app's route (start-block)` becomes
  `+ the app's route and backup (start-block)` (+11 B).
- VN: the same clause in `modules/vn/brain.md` §CM-CARD 1 (≈+15 B), paid by K24's VN cut.

**K29. Whole-card trim order** (consultant 6,090, proof S1 5,893).
- Change: `modules/en/brain.md` L16: `Over 5,700: trim liked first; voice fields last.` becomes
  `Over 5,700: trim liked, then passages, stories, client_words; voice last.` (+25 B; CARD 2,787).
- VN: wait until a cut is named. After K24/K27/K28 the VN file has about 25 B left, which is not enough. Candidate
  cut: the duplicate "Nước đôi …" hedge in §CM-CHARACTER-LITE.

**P3: cosmetic, or one run**

**K30. "No client result" guess** (Linda t5).
- Change in §CM-SETUP 4 (`setup.md` L14): `none → "{{t:setup.guess_no_result}}"` becomes
  `no client named → "{{t:setup.guess_no_result}}"; clients named, no outcome → ask what changed for one`
  (≈+60 B).
- Needs a further SETUP cut, e.g. §CM-SETUP 3 `Asked: "No, nothing today."` (−27) plus a trim of 8 PICK.

**K31. KNOWN FOR length in compact mode** (S0 runs: 41 words each).
- Change: start-block L25 `one breath:` becomes `one breath, ≤35 words:` (+11), matching §CM-MAP.

**K32. Quit point #16 in S1.**
- Change: `modules/en/fmt-short.md` L10 (§CM-FORMATS 5): `(Day 0: "FILM TODAY · under 30 s")` becomes
  `(Day 0: "FILM TODAY · under 30 s, say it from memory")` (+20 B).

**K33. Film-list opener vs Day-0 prose.**
- Change: `modules/en/plan.md` L17 (§CM-WEEK 10): `Day 0: one line above each box, no other prose.` becomes
  `Day 0: one line above each box (+ the film-list opener), no other prose.` (+28 B).
- Or drop `film.list_open` on Day 0.

**K34. Founder question, no change proposed.** Make the early win usable: one of the 3 lines in a copy box,
"post it as text today if you like". 4 of 7 personas voiced "nothing usable yet" at min 14–15.

### Grader fixes

**G11. `_norm_word`** (`evals/graders.py` L2953) for the day0_shape YOUR WORD item (L3010–3013).
- Change: compare the CTA keyword with the head of the YOUR WORD value: drop quotes and a leading "the", and cut
  at the first `(`, `,`, `:`, ` from ` or `—`.
- Effect: removes 6/6 FPs. No real mismatch occurred this round, so G11 hides none.

**G12. `PLACEHOLDER_RE`** (L268, used at L3080).
- Change: pass a `[name]` / `[first name]` redaction inside a quoted value of a card machine block. Also catch
  `{first name}`-style slots (lowercase words with a space) inside copy boxes.
- Effect: removes Linda's FP and catches proof S1 t8's "Hi {first name},".

**G13. I9** (`i9_quotes` L1450).
- Change: skip quotes in a piece's label line that follow a hypothetical speaker ("someone/anyone/they asks|says|
  messages|comments").
- Effect: removes the service S0 FP.

**G14. day0_shape: whole card ≤ `platform/targets.toml` `[budgets.brand_card]`** (5,700 EN / 6,600 VN).
- Effect: catches consultant S1 and proof S1.

**G15. day0_timing: check the acceptance keys it ignores today.**
- Keys: `early_win_max_minutes_after_dump_start` (4) and `session_max_minutes` (40).
- Effect: the early win fails 7/7 today (5.5–8.0 min); see P10.

**G16. Run name and summary.**
- `graders.grade` L3118: `"run": run_dir.resolve().name`. This fills the floor row's blank Run cell.
- `evals/run.py` `summary_rows` (L661): print `film_ready_active_minutes`, with the clock in brackets.

**G17. Optional Day-0 checks.**
- Week-1 keyword outside the ask (§CM-WEEK 4): catches proof S1 N2/N3 and service S1 N1.
- KNOWN FOR ≤35 words.
- A number-pairing check for "from X to Y" claims: catches the floor's "minus 6 percent to 51 percent".

**G18. Leak check** (`evals/run.py` `check_leaks` L578).
- Changes:
  - build the corpus from TOML string values only (parse, one value per string), not raw TOML text;
  - strip the `name:` / `name=` label from machine field lines;
  - split list items on ` | ` and ` · ` before n-gramming.
- This removes the key + value FPs that pushed 4 simulators to reorder or rewrite card lines. The real persona-leak
  detection is kept.

### Simulator and protocol fixes

**P8. Machine turns are frozen after the first grade.**
- Write `transcript.raw.jsonl` before any edit, and keep an edit log in `meta.json` (turn, field, before/after,
  reason).
- Allow only leak removals.
- Have `grade` report "edited: n".
- Why: in this round 4 runs were edited to pass the leak check, 3 of them on G18's FP.

**P9. The floor lane is unusable again** (invalid on turns, pace and leaks; no W1/W2 paste; 3 machine turns in a
row; notes that misread the grader).
- Carry out the deferred P1: the machine side as a separate model call that never sees persona paths, driven by a
  script that alternates turns and stamps `t_min` from word counts.
- Add the deferred P4 required-paste check.
- Generate floor notes from `grades.json` (P7).

**P10. Chunk length vs the kit's "Send every 2–3 minutes"** (P2 still open).
- Each persona's chunk 1 is 608–758 words (5.5–8 min), so the early win always misses its 4-minute limit, and the
  cut can only fire at 11–14 min.
- Add one in-budget persona per lane (≤400-word chunks), so the kit is tested as written.

**P11. `COACH.md` "say you are done … as one more turn".**
- Keep it as is. After K22 the machine asks its question in the cut reply, and the coach answers it.
- Re-run proof S1, proof S0, Linda and consultant S1 to confirm Map ≤6 and film-ready ≤20.
