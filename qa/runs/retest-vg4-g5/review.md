Result: FAIL

# Retest VG4 (VN ×3) + G5 (EN consultant) Day-0 after the retest-2 fix round: independent review

Reviewer: independent and bilingual (EN, plus native Vietnamese for the VN runs). I wrote neither the kit nor the runs.

Kit under test: `f22d32e` (kit fixes K37–K38, VK-26–VK-32) and `80e092a` (graders G27–G30, P10). The later commits
`1f78fcc`, `f46a094` and `ce09d30` touch eval cases only. Each run's `packet/kit/` is byte-identical to the current `dist/`:
- EN: block 6,487 chars NFC (the build reports 6,488) of 6,500; method file 49,097 of 51,200 B. Run build `83ba1816c3c5`.
- VN: block 7,480 of 7,500; method file 56,317 of 56,320 B. Run build `e2b97d4daf6d`.

How this review was done:
- All 4 transcripts were read in full, as the coach would read them on a phone.
- Scratch copies of the 4 folders were re-graded with the current `evals/run.py grade`. The verdicts match the stored
  `grades.json` exactly, and `transcript.jsonl` equals `transcript.raw.jsonl` in 4/4 (edited: 0). The run folders
  were not touched.
- Every failed check was traced to its transcript line and to the kit line or grader code behind it.
- Leaks were checked in 2 runs (EN consultant, VN consultant) with my own scan. The method is in section 5.
- VN naturalness was scored on `qa/standards/vn-naturalness.md` (VN1–VN8). Every line I mark is quoted with a fix.

## Why FAIL

- **Grader passes: 0/4.** Tuấn's run is **invalid** (protocol `pace`).
  - There are 10 failed grader checks: 5 real, 2 real only against the turn budget (`R(protocol)`), and 3 false positives.
- **The VN particles fix did not work** (`vn_natural`, 2/3, a second round).
  - Hạnh's pieces end 16% of sentences on a particle, against 53% in her own posts (VG3: 17%).
  - Tuấn's pieces are at 4% against 46% (VG3: 15%).
  - The invites copy the particle-less `cta.*` templates word for word. Tuấn's "…mình gửi tờ tính 3 bước." appears 4 times.
- **EN film-ready 21.4 and Map at coach turn 8 (max 6).** Both are real.
  - Erin had just said "Then an optional monthly CFO retainer". The machine still asked "You earn from 2 things…".
    That question cost a coach turn and 1.9 minutes.
  - The kit's multi-income rule has no "different buyers" condition.
- **P10 pushed the Map past its turn budget in 2/3 VN runs.** Hạnh and VN consultant reach the Map at coach turn 8,
  against a max of 7.
  - The machine had no slack. It replied to every send at once and asked only the questions the kit asks.
  - The extra turns are the P10 second sends and a turn that holds only pasted posts. DECISIONS says posts "add no
    extra turn". This is a founder call (section 8).
- **YOUR WORD only in the ask, ungraded:**
  - FILM TODAY's caption (it doubles as the text post) in Tuấn, VN consultant and EN;
  - Tuấn's N3.
  - The grader misses all four: G30 reads the script and caption as one piece, and a piece-boundary bug hides N3.

**What passed:**
- **Keyword in the long text pieces: 3/3 VN + EN** (VG3: 3 failures).
- **Film-ready ≤20 in 3/3 VN** (18.9, 16.0, 17.4). This is the first round with every VN run inside the budget.
- **Early win ≤4 min after the dump prompt in 2/4** (Hạnh 3.2, VN consultant 3.4). The last two rounds had 0/13.
- **Soft cut: 4/4.** It came at the crossing send each time, as one message with one "?".
- **Other fixes that held:**
  - 1:1 register right in 3/3 (Tuấn fixed);
  - `multi_income` with a true reason in 2/2;
  - "Chạy thử 4 tuần" without "Em" in 3/3;
  - the two coach-facing strings in 3/3;
  - the consultant's objection to comment asks honoured at once.
- **VN naturalness:** no critical item at 1 in any run (VG3: 2). 0 essay connectors, 0 banned tells.
- **Leaks:** no persona fact before the coach said it, in both runs checked.
- **0 quits.** Every coach comes back.

## 1. The runs

Previous-round figures are in brackets: VG3 for VN, G3 for EN consultant.
- "Map turn" is the coach turn the Map answers. It is also the film-ready turn (K2).
- "Early win" shows the clock minute of the copy box, then, after "·", the minutes counted from the dump prompt
  (acceptance ≤4).

Verdict codes:
- R(kit): the kit wording caused it.
- R(m): a machine slip.
- R(protocol): real against the budget, but the coach's sends (P10 and a turn that holds only pasted posts) caused it,
  not the machine.
- FP: a grader false positive.
- W: a warning.

| Run | Lane · app | Valid | Coach turns | Map turn | Early win | Film-ready (active) | Grader failures: verdict |
|---|---|---|---|---|---|---|---|
| VN Hạnh | S1 · ChatGPT Free, Android | yes | 9 (8) | 8 (6) | 5.1 · 3.2 (7.8 · 6.0) | 18.9 (21.6 W) | day0_timing R(protocol) · vn_natural R |
| VN Tuấn | S1 · ChatGPT Plus | **no: pace** | 8 (7) | 7 (6) | 5.8 · 4.3 (8.7 · 7.3) | 16.0 (18.8) | I11 FP · day0_timing FP · vn_natural R |
| VN consultant (Khoa) | S1 · Claude Pro | yes | 9 (7) | 8 (6) | 4.6 · 3.4 (9.0 · 7.5) | 17.4 (20.3) | I6 FP · day0_timing R(protocol) |
| EN consultant (Erin) | S1 · Claude Free | yes | 9 (6) | 8 (5) | 5.3 · 4.9 W (6.5 · 6.2) | 21.4 (17.6) | I12 R(m) · day0_timing R(kit) · day0_shape R(m) |

Totals:
- **Valid: 3/4. Grader pass: 0/4.** Quits: 0. Comes back: 4/4.
- **Failed checks: 10, plus 1 protocol failure.**
  - Real: 5. Particles ×2, EN 13-word first line, EN multi-income turn, EN card length.
  - R(protocol): 2. These are Map-turn budget failures.
  - FP: 3.
  - On the same personas last round: 9 failed checks, 7 real (including R(pace)) and 2 FP.

| Budget (acceptance `[day0]`) | EN consultant | VN 3 runs |
|---|---|---|
| Map ≤6 coach turns (VN ≤7) | 0/1 (8) | 1/3 (8, 7, 8) |
| Film-ready ≤20 active min | 0/1 (21.4: machine turn) | **3/3** (16.0–18.9) |
| Soft cut on time (≤1,200 words / tiếng) | 1/1 (1,482 at the crossing send) | 3/3 (1,312–1,378) |
| ≤10 coach turns | 1/1 (9) | 3/3 (8–9) |
| Session ≤40 active min | 24.1 | 19.4–22.3 |
| Card top ≤500 / whole ≤5,700 EN, 6,600 VN | 449 / **5,881** | 371–468 / 5,495–5,628 |
| Early win ≤4 min after the dump prompt | 0/1 (4.9, warning: first send at 4.6) | 2/3 (3.2, 3.4; Tuấn 4.3, his first send at 4.0) |

## 2. Did the fixes aimed at each run work?

| Run | Fix aimed at it | Worked? | Evidence |
|---|---|---|---|
| VN all | VK-26 keyword in the long text piece | **yes, 3/3** | Hạnh's long post opens "Em nào ngại chào thì đọc hết bài này nhé." · Tuấn's FB post: "Đầu buổi chị còn nói: "Mua thì sợ gồng lãi không nổi…"" · consultant carousel Trang 2 "…"Tôi tuyển hoài mà không giữ được ai."", both LinkedIn posts, the email |
| VN all | keyword in FILM TODAY's caption | **1/3** | Hạnh ✓: "Em nào ngại chào thì nghe chị kể, năm 2018 chị dọa khách đấy." Tuấn: only in "Bạn nào sắp đi coi nhà mẫu thì comment GỒNG LÃI…". Consultant: only in the ask sentence "Anh chị nào đang tuyển hoài một chỗ, comment TUYỂN HOÀI…". In both, the script carries it (Ý 3 "gồng lãi sao nổi"; Ý 1), so G30 passes them |
| VN Tuấn | keyword in each Week-1 piece | **4/5** | N3 "Anh khách nằm viện…" has GỒNG LÃI only in "Nhắn mình chữ GỒNG LÃI, mình gửi tờ tính 3 bước." The grader missed it (section 4) |
| VN Hạnh, Tuấn | VK-27 "tiểu từ dày như bài coach" | **no** | Hạnh 17% → 16% (her posts 53%); Tuấn 15% → **4%** (46%). Every invite is flat: "…chị gửi 3 bước cầm gương nói thật." / "…mình gửi tờ tính 3 bước." Tuấn's FILM TODAY last line drops his own "nha bạn" from W1 |
| VN all | VK-28 1:1 as the coach addresses clients | **yes, 3/3** | Tuấn "Anh chị ơi, Tuấn nhờ anh chị một chút…" (VG3: "bạn") · Hạnh "Thảo ơi c nhờ e một chút nhé." (her own c/e) · consultant "Nhờ anh một chút: tôi đang…" + "người nhắn là chị thì đổi…" |
| VN Hạnh, Tuấn | VK-29 `multi_income` with a true reason | **yes, 2/2** | Hạnh "vì chị có kết quả thật với các em ấy: Thảo từ khoảng 2 lên khoảng 5 trên 10 khách hẹn buổi sau" · Tuấn "vì nhà đó vừa cần căn vừa cần cái che cho khoản vay, như anh khách gãy chân…"; one "?" each |
| VN all | VK-31 `map.ok` without a subject | **yes, 3/3** | "Chạy thử 4 tuần nhé chị." · "…nha anh." · "…nghe anh." (VG3: "Em chạy thử" in 2/4) |
| VN all | VK-32 card waits only if the app cuts | **yes, 3/3** | Week 1, card and save line in one reply |
| VN Hạnh | film-ready ≤20 | **yes** | 18.9 active (VG3: 21.6 W). She stepped out at the cut and came back with the answer, not with chunk 3 |
| VN Hạnh | save-line backup | **yes** | "Không thấy nút đó thì chép card gửi vào Zalo "Cloud của tôi"" (VG3: "chụp màn hình") |
| VN Tuấn | one-question `multi_income` | **yes** | T6 has one "Đúng không?" He answered it in a line and skipped chunk 3 |
| VN consultant | spoken objection to comment asks | **yes** | T9 "Dạ, em bỏ xin comment." The caption's last line was reprinted as "nhắn tôi chữ TUYỂN HOÀI". 4/4 Week-1 asks are quiet, `cta_style: quiet` |
| VN all | the two coach-facing strings | **yes, 3/3** | "Quay luôn bây giờ, hoặc đăng phần chữ làm bài viết." · "(Ngại xin comment thì gõ 'nhẹ'.)" |
| VN coldstart | turn count | not in this retest | — |
| VN all | VK-30 "Ngắn thôi" leaves out the card | not triggered | — |
| EN consultant | K37 keyword in a long post's or carousel's opening | **yes** | Wed post opens "Record year. Empty account. Make it make sense." · PDF Slide 1 "Record year, empty account." · email "A record year is the symptom." · Fri post "record year, and I can't sleep" (G3: 3 pieces had it only in the ask) |
| EN consultant | `ask3.consent` as a statement | **yes** | "If I may quote you (first name only), just add 'OK to share'." One "?" |
| EN consultant | Map ≤6, film-ready ≤20 | **no** | Map at coach turn 8, film-ready 21.4. Causes: 4 dump sends (P10), the paste turn, the cut's offer guess, then a 2+ streams guess she did not need (T7) |
| EN consultant | list and platform heard or guessed visibly | **yes** | VP-2 "LinkedIn… an email list of 380" was heard. "For LinkedIn · talk day Monday · email list: 380 (talk day is my guess; one word changes it)." The email went first (380 ≥ 300). The talk day is wrong (Wed) |
| EN consultant | "Shorter" | not triggered | — |
| EN consultant | card length | **no** | 5,881 > 5,700 (G3: 5,662). The top is 449. The kit's trim order was not applied |

## 3. The founder's Day-0 rules in practice

| Run | Early win: line in the copy box | Arrived · postable? | Soft cut | One message, one "?"? | Cost? | Facts asked up front / guessed visibly |
|---|---|---|---|---|---|---|
| VN Hạnh | "Chị làm kỹ thuật viên 5 năm cho một spa to ngoài phố, chị đi lên từ cái giường massage em ạ, chị không học kinh doanh trường lớp gì đâu." | 3.2 ✓ · yes, but weak: a bio line, no buyer pain | T7, at the crossing send, with the multi-income guess and her "chờ chút" handled in one line: "Không vội đâu chị, chị cứ ra tiếp khách, em giữ nguyên đây." | yes | 0 turns | No VP-2 (answer bank only). FB, list "chưa có" and talk day Mon were guessed, all right |
| VN Tuấn | "Tui nói chị ra khỏi toilet đi, cảm ơn bạn sale, nói về hỏi chồng, mai mình ngồi tính rồi hẵng cọc." | 4.3 · partly: needs the toilet setup to stand alone | T6, with the multi-income guess | yes | 0 | VP-2: TikTok, FB, Zalo 1,850 and no email were heard, but the plan line tags them "(em đoán…)" |
| VN consultant | "40 trên 210 người không quay lại sau Tết, không ai báo tiếng nào." | 3.4 ✓ · partly: whose 210? needs "Mùng 8 Tết 2016, xưởng tôi" | T6, with the result guess | yes | +1 turn: the offer was also unheard, and the kit asks one fact per message | VP-2: LinkedIn, FB, Zalo 380 and email 250 were heard, also tagged "(em đoán…)". Talk day Mon is wrong (Sun) |
| EN Erin | "Your biggest client is not your best client until you've done the math." | 4.9 W · yes | T6, with the offer guess | yes | +1 turn and +1.9 min: the 2+ streams guess at T7 | VP-2: LinkedIn and list 380 heard. The talk-day guess is scoped right; the day is wrong (Wed) |

Findings:
- **Early win: 4/4** in a copy box on the first send; 2/4 postable as is.
  - The kit asks that "câu vào khung đứng riêng thành bài được" (§CM-SETUP 2). Tuấn's and the consultant's lines need
    one clause of context.
  - P10's shorter first sends brought 2/4 inside 4 minutes. Tuấn's first send alone took 4.0.
- **Soft cut: 4/4** on time, as one message with one "?".
  - It cost no turn in 2/4.
  - In the consultant VN run, the second unheard fact (the offer) added a turn, as the kit requires.
  - In EN, the extra turn was the needless streams question.
- **Facts up front:**
  - VP-2 worked in 3/4, and Hạnh's three guesses were all right.
  - VN `setup.plan_guess` ends with one "(mình đoán…)" that covers the whole line, so heard facts read as guesses in
    2/3. The EN machine scoped its tag ("talk day is my guess").
- **Founder warning rules:**
  - EN 21.4 stays a failure, as the rule says: the over-threshold send covers 1.1 min, the machine's extra turn 1.9.
  - Nobody kept talking after the cut.
  - The Map reply at about two screens (VN 490–541 words, 284–297 outside boxes) is accepted under DECISIONS.

## 4. Failed grader checks: real or false positive

| # | Run · check | Transcript line | Kit line or grader code | Verdict |
|---|---|---|---|---|
| 1 | Hạnh · day0_timing "Map after 8 coach turns (max 7)" | T3 232 tiếng, T4 363, T5 posts only, T6 288, T7 363 (cut + guess), T8 answer → Map. Each send was answered at once, with one question merged into the cut | `acceptance.toml` `map_max_turns_vn = 7`; COACH.md step 2: posts "as one more turn", P10 two sends; DECISIONS "Written voice … adds no extra turn" | **R(protocol)**: 7 without the posts-only turn |
| 2 | Hạnh · vn_natural 16% vs 53% | FILM TODAY caption, N1–N3 captions and the long post: 8 of 36 sentences end on a particle (22%: over the grader's 21% floor, under half her rate, 26.5%). Flat invites: "Em nào cần thì comment NGẠI CHÀO hay nhắn riêng chị, chị gửi 3 bước cầm gương nói thật." The grader's 67 also counts the gift's steps twice (gift box + inbox 1, 18 flat lines), the card top (3) and a dated platform note (1) | `core/vn/start-block.md` L51 (dist L38) "tiểu từ dày như bài coach"; `strings/vn.toml` L172–173 `cta.*` with no particle; `modules/vn/humanize.md` L32 "ở chỗ dặn, rủ, làm thân" | **R** (VN5 = 1); the count is inflated (G37) |
| 3 | Tuấn · **pace** (run invalid) | T5, the W1+W2 paste of 135 tiếng, came 0.7 min after the reply | `evals/run.py` `check_pace` L566: one 12-gram shared with the dump (W2 repeats a chunk-2 line) makes the whole turn dictation | **Protocol slip, caught for the wrong reason.** COACH.md "a pasted post takes about half a minute" gives about 1.1 min, so the paste was 0.4 min short. Content unaffected; the Map would be at 16.4 (P14) |
| 4 | Tuấn · I11 "cam kết" | FB post and N3 caption: "kết quả tuỳ người, hổng phải cam kết." | `NEGATED_BEFORE_RE` graders.py L1704 has không/chẳng/chả but not Southern "hổng/hông" | **FP** |
| 5 | Tuấn · day0_timing "early win 4.3 … (max 4)" | First send at 4.0 after the dump prompt (407 tiếng); the copy box came in the reply to it | `check_day0` L3550: a warning only when `first_send > limit`; 4.0 is not > 4 | **FP** (boundary): no reply to the first send can come sooner |
| 6 | Tuấn · vn_natural 4% vs 46% | FB post 1/19 (only a quote), captions 0/14. "Nhắn mình chữ GỒNG LÃI, mình gửi tờ tính 3 bước." ×4. FILM TODAY's last line drops his "nha bạn" | as #2 | **R** (VN5 = 1), worse than VG3 |
| 7 | consultant · I6 "quyết định" | Week-1 heading "TUẦN 1 · 07/10 – 13/10 · Người mới quyết định nghỉ từ tuần đầu" (Map topic 1) | `DECISION_RE` L245; G21 exempts only the Map's own lines | **FP** (the same word as VG2, now in a heading) |
| 8 | consultant · day0_timing "Map after 8 coach turns (max 7)" | T3 and T4 sends, T5 posts only, T6 send (cut + result guess), T7 result, T8 offer → Map | as #1; block step 4 "tối đa 3 … mỗi tin một câu" with the result and offer both unheard | **R(protocol)**: 7 without the posts-only turn. Splitting chunk 2 after its results paragraph would also have saved a turn (the simulator says so) |
| 9 | EN · I12 | Optional short N1, first line "Dee told me: "I check the bank app like it's a heart monitor."" (13 words) | block step 5 "first line ≤12 words" | **R(m)** |
| 10 | EN · day0_timing: Map 8 (max 6), film-ready 21.4 | T7: "You earn from 2 things. My guess: write for agency owners…, because the Margin Sprint is how they start and the retainer comes after. Right?" She had just typed "Then an optional monthly CFO retainer" | `core/en/start-block.md` L22 "Several income streams: guess the ONE buyer…"; `modules/en/setup.md` L16 "2+ paid streams: one of the 3" (nothing about different buyers) | **R(kit)**: +1 turn and +1.9 min. Without it, film-ready is ≈19.5 and the Map is at 7, or 6 without the posts-only turn |
| 11 | EN · day0_shape card 5,881 | 5 passages of about 50 words, a long proof field | `modules/en/brain.md` L16 "Over 5,700: trim liked, then passages…" | **R(m)** |

Grader misses:
- **FILM TODAY's text version** carries YOUR WORD only in the ask in Tuấn, VN consultant and EN, but G30 joins the script
  and caption. The coach is told to "post the caption as text" / "đăng phần chữ làm bài viết". The EN on-screen text
  "Record year. Out of cash." and the VN scripts are not posted as text.
- **Tuấn N3:** the N3 piece runs on through the inbox replies, the side-door line and the card top, which holds
  "gồng lãi", so `_keyword_outside_ask` sees the keyword outside the ask.
  - The same bug adds the card to the last piece of every Week-1 reply: Hạnh's inbox 2, consultant's inbox 2, EN's N1.
- **vn_natural** counts the card top and the dated notes. It counts a box printed twice twice. It compares with
  written-posts.md W3, which the coach never pasted (COACH.md pastes W1 and W2).
- **"Week 1 has an email when the coach named a list"** was not run for VN consultant ("email thì có 250 người"; card
  `list_size: email 250 · Zalo khoảng 380`). The email is there.

## 5. Leak spot-check (2 runs)

**Method:**
- For every machine turn, I listed each 5-gram (EN words, VN tiếng, case-folded) that is also in the persona's
  `persona.toml`, `answers.md`, `expected.toml`, `voice-samples.md`, `launch-brief.toml`, `pillar-transcript.md`,
  `paste-dump.md` or `written-posts.md`. I removed 5-grams of the coach's turns so far and of the kit.
- I also listed every number the coach had not said.
- I read each hit against the transcript.

**EN Erin: clean on facts; three compressions identical to the answer bank.**
- About 45 runs. Nearly all join her own words across sentences, or are card field labels.
- New numbers are dates, "25 s" and the pack version.
- The talk day was guessed as Monday; `persona.toml` L30 says Wednesday, so the persona did not reach the machine side.
- Three machine lines match the answer bank character for character. The facts in them are hers:

| Machine text | Persona source | What she said |
|---|---|---|
| Wed post "He runs a 22-person paid media agency in Milwaukee." | `answers.md` L82 "a 22-person paid media agency in Milwaukee" | "he runs a paid media agency, 22 people, Milwaukee" |
| card proof "first name only, no dollar amounts, no revenue" | `answers.md` L96, L108 | "first name only, but don't put the amount out there and don't put our revenue out there" |
| card offer "path: LinkedIn DM or email reply, 30-minute fit call (last year's P and L first), proposal" | `answers.md` L102 "Path: LinkedIn DM or email reply, 30-minute fit call (she asks for last year's P and L first), proposal." | "They DM me on LinkedIn or reply to my email, 30-minute fit call, I ask for last year's P and L first, then a proposal." |

**VN Khoa: clean.**
- About 70 runs. All join his words or reorder them: "Mùng 8 Tết năm 2016" for his "Tết năm 2016, mùng 8 khai xuân",
  and "40 trên 210 công nhân".
- The trap numbers (70%, 80%, 200 triệu) appear 0 times.
- The talk day was guessed as thứ Hai; `persona.toml` L34 says Chủ nhật.
- New numbers are dates and "30 giây".

**Verdict:** no fact reached the machine before the coach said it, so both runs stay valid.
- The wording priming is down from G4: 3 identical compressions of dictated facts, against 4 lifts of undictated text.
- P9 (a machine side that never sees the persona) is still the only real fix.

## 6. VN naturalness (VN1–VN8)

Bars, from `qa/standards/vn-naturalness.md`:
- **Pieces:** VN3, VN4, VN6 and VN7 at 2; total ≥13/16.
- **Coach-facing prose and Map lines:** VN3, VN4 and VN6 at 2; total ≥10/12.

Regions: Bắc (Hạnh), Nam (Tuấn), Trung/Quảng (consultant).

| Run | Coach-facing /12 | Map lines /12 | QUAY HÔM NAY /16 | Week-1 posts /16 | Zalo + inbox /16 |
|---|---|---|---|---|---|
| Hạnh | 11 ✓ (VN1 1: "Brand Card", "Lưu vào dự án") | 11 ✓ (VN2 1: tail "3 bước làm được ngay ở quầy") | 15 ✓ (VN5 1) | 15 ✓ (VN5 1; one D line, #3) | 16 ✓ (her c/e in Zalo) |
| Tuấn | 11 ✓ (VN1 1) | 11 ✓ (VN2 1: methods stacked, third round) | 15 ✓ (VN5 1) | 15 ✓ (VN5 1) | 15 ✓ (VN8 1: title line + DỪNG to a few acquaintances) |
| consultant | 11 ✓ (VN1 1: "Add text content") | 12 ✓ (line 1 as fixed; the first print was VN2 1) | 16 ✓ | 16 ✓ | 16 ✓ |

Totals:
- **Every column passes in 3/3.** VG3 had coach-facing prose at 3/4 and messages at 3/4.
- **No critical item at 1 in any run** (VG3: coldstart VN6 and Tuấn VN4). Piece averages are 15, 15 and 16.
- VN5 at 1 in 2/3 is non-critical, but `vn_natural` fails on it.
- 0 essay connectors, 0 banned tells, 0 `vn_natural` patterns.
- No "một cách", "điều này", "giúp bạn" or "chia sẻ rằng" in any machine turn.

Lines that still read translated or stiff (D = translated, S = stiff), with a natural version:

1. VN5 · flat invites and endings against the coach's own posts:
   - Hạnh caption "…chị gửi 3 bước cầm gương nói thật." → "…chị gửi 3 bước cầm gương nói thật nhé :))" (her W1
     closes "chị kể cho nghe :))")
   - Tuấn "Nhắn mình chữ GỒNG LÃI, mình gửi tờ tính 3 bước." → "…mình gửi tờ tính 3 bước nha."
   - Tuấn FB "Ai sắp cọc mà chưa ngồi tính thì nhắn tui chữ GỒNG LÃI, tui gửi tờ tính 3 bước." → "…tui gửi tờ tính 3
     bước, free nha, hổng bán gì hết." (his W2)
   - Tuấn FILM TODAY last line "Đi coi nhà mẫu thì cầm theo tờ giấy ghi con số, đừng cầm theo tiền cọc." → keep his own
     "…đừng cầm theo tiền cọc nha bạn." (W1, word for word)
2. S (label) · "Gợi ý:" before the joggers, in 3/3 runs (7 times; VG3 4/4). Natural versions:
   - Hạnh "Gợi ý chuyện kế: chị gỡ cho Thảo thế nào, chị dạy em ấy chào khách ra sao." → "Chị kể tiếp đoạn chị gỡ cho
     Thảo nhé, chị dạy em ấy chào khách ra sao."
   - Tuấn "Gợi ý: bên bảo hiểm, anh kể một nhà anh nhớ nhất." → "Bên bảo hiểm thì anh kể em nghe một nhà anh nhớ nhất
     nha."
   - consultant "Gợi ý cho đoạn sau: anh kể em nghe cách anh làm…" → "Đoạn sau anh kể em nghe cách anh làm với một chủ
     doanh nghiệp nghe, từ buổi đầu ngồi với nhau tới lúc người mới ở lại được."
3. D · Hạnh N2 last line "Hết ngại chào là lúc em biết mình bán buổi hẹn sau, chứ không bán thẻ."
   - It back-translates cleanly ("The end of shyness is when you know you sell the next appointment").
   - Fix: "Mình bán buổi hẹn sau chứ có bán thẻ đâu, thì ngại gì mà không chào."
4. S · the plan line tags heard facts as guesses (Tuấn, consultant): "…danh sách Zalo, email: Zalo chừng 1.850 người,
   email chưa có (em đoán, gõ một chữ là đổi)."
   - Fix: "Viết cho TikTok · Zalo chừng 1.850 người, chưa có email · thứ Hai hằng tuần kể 15 phút cho tuần sau (ngày này
     em đoán, anh gõ một chữ là đổi)."
5. S (brochure) · Map line 1 still stacks methods (Tuấn, third round): "…thì tìm Tuấn: tính ngược từ tiền góp bằng lãi
   thả nổi chứ không cọc vì bị dí, ra căn tối đa, quỹ 6 tháng và cái che cho khoản vay."
   - Fix: "Vợ chồng nào hay than "mua thì sợ gồng lãi không nổi" thì tìm Tuấn: tính ngược ra căn tối đa rồi mới cọc,
     chứ không cọc vì bị dí."
   - Hạnh: drop ", 3 bước làm được ngay ở quầy".
6. S (call centre) · Tuấn's Zalo to a few acquaintances: "Không muốn nhận nữa thì nhắn Tuấn chữ DỪNG." (third round)
   - It is the kit's own line for "chuỗi tin Zalo" (§CM-MESSAGES 3).
   - Fix: "Anh chị chưa cần mấy tin này thì nói Tuấn một tiếng nha, Tuấn không gửi nữa."
7. S · consultant ask-3 opens with no greeting: "Nhờ anh một chút: tôi đang viết lại phần giới thiệu công việc…"
   (`research.ask3`).
   - Fix: "Anh ơi, Khoa đây. Nhờ anh một chút: …"
8. S · consultant T6 "quán hải sản ở Sơn Trà là chỗ đổi khác rõ nhất" → "…là khách đổi khác rõ nhất". Tuấn T6 "Đúng
   không?" → "Đúng không anh?"

Keep these; they read like a person:
- Hạnh T7: "Dạ, em nhận rồi. Không vội đâu chị, chị cứ ra tiếp khách, em giữ nguyên đây."
- Hạnh N2: "Giá để trên bảng, không giảm sốc gì hết, thì chặt chém ai được."
- Hạnh N3: "Mình có đòi tiền đâu mà sợ, mình hỏi da khách thôi mà."
- Hạnh's Zalo: "Em ơi c Hạnh đây. Dạo này c đang viết mấy bài về chuyện chào liệu trình ở spa nhỏ."
- Tuấn T7: "Căn 2 tỷ 68 anh cần chốt tháng này: em gắn vô tin trả lời inbox ở Tuần 1, nhà nào tính ra vừa thì anh mời coi
  căn đó."
- Tuấn N3: "Anh khách nằm viện, chân bó bột, câu đầu tiên hổng hỏi bảo hiểm trả bao nhiêu."
- consultant's LinkedIn post: "Ông giám đốc đứng kế bên hỏi đúng một câu: "Rứa là năm nay mình tuyển lại từ đầu hả
  Khoa?"" (the machine fixed the mic's "dứa") and "Chừ đi làm với chủ doanh nghiệp, tôi vẫn nghe hoài một câu".
- consultant's carousel caption: "Có người nghỉ thì khoan đăng tin. Lướt hết mấy trang này rồi hẵng đăng."
- consultant's inbox 2: "Tự tuyển thì đúng việc tôi hay làm. Anh kết bạn Zalo với tôi nghe, để tôi gửi lịch."

## 7. What improved vs the previous round (same personas)

| Measure | VG3 (Hạnh, Tuấn, consultant) / G3 (EN consultant) | VG4 / G5 |
|---|---|---|
| Valid | 3/3 / 1/1 | 2/3 (Tuấn: pace) / 1/1 |
| Grader passes | 0/3 / 0/1 | 0/3 / 0/1 |
| Failed checks: real / R(protocol) / FP | VN 8: 6 / 0 / 2 · EN 1: 1 | VN 7: **2 / 2 / 3** · EN 3: 3 |
| Graded pieces with the keyword only in the ask | VN 3 · EN 3 | **VN 0 · EN 0** (ungraded: 3 FILM TODAY captions, Tuấn N3) |
| Early win, minutes after the dump prompt | 6.0, 7.3, 7.5 · 6.2 | **3.2, 4.3, 3.4 · 4.9** |
| Film-ready, active | 21.6 W, 18.8, 20.3 · 17.6 | **18.9, 16.0, 17.4** · 21.4 ✗ |
| Map coach turn | 6, 6, 6 · 5 | 8, 7, 8 · 8 (P10 sends, posts-only turn, EN streams turn) |
| Particle share (their posts) | Hạnh 17% (53), Tuấn 15% (46) | 16%, **4%** |
| VN 1:1 register right | 2/3 (Tuấn "bạn") | **3/3** |
| "Em chạy thử" | 2/3 | **0/3** |
| `multi_income` reason true | 1/2 (Hạnh adapted it) | **2/2** |
| VN critical items at 1 | Tuấn VN4 | **none** |
| Hạnh's save backup | "chụp màn hình" | **"chép card"** |
| EN email for the 380 list | last, size "not given" | **first, 380 heard** |
| EN card | 5,662 | 5,881 ✗ |

## 8. Prioritised fix list

Budgets now:
- EN block 6,488/6,500 (build count); EN method 49,097/51,200 B, with §CM-SETUP at 2,765/2,800.
- VN block 7,480/7,500; VN method 56,317/56,320 B.

After items 1–4:
- **VN block 7,493.**
- **VN method 56,315** (+5 −7 +35 −38 +16 −13).
- **EN block 6,494.**
- **EN method 49,140** (+18 +25), with §CM-SETUP 2,783.
- Phone Starters: VN 7,273/7,500, EN 5,807/7,500.

Lint E146 keeps the `verdict.needs` example in every script section, so those are not cut.

### Kit

**P1: blocks acceptance**

1. **VK-33. Particles where the machine copies a template** (#2, #6; VK-27 alone moved nothing).
   - (a) `strings/vn.toml` L172 `cta.default` and L173 `cta.quiet`: "…, mình gửi {gift}." → "…, mình gửi {gift} nhé."
     - That is +4 chars in the block (step 6) and +5 B in the method file (§CM-CTA-KIT 5).
     - "cả câu mẫu" already makes the machine swap "nhé" by region: `map.ok` became "nha anh" / "nghe anh" in 3/3.
     - It also removes the clash with §CM-NATURAL 8's own example "…ngại thì nhắn riêng nhé."
   - (b) `core/vn/ship-check.md` L21 ship.kit: "4 GIỌNG + NGƯỜI MUA: giọng, nhịp, câu hay nói" → "…giọng, nhịp, tiểu từ,
     câu hay nói" (+9 chars; ship.kit 932/1,000).
     - Every piece then passes a particle check silently.
   - (c) `modules/vn/humanize.md` L32 §CM-NATURAL 4: ", ở chỗ dặn, rủ, làm thân, dày như bài họ." → ", dày như bài họ, cả
     câu kể, câu mời." (−7 B).
     - The coaches' own story lines carry particles ("Năm 2018 spa chị cũng dọa khách đấy."). The place list
       leaves story lines flat.
   - Refresh the src hashes. Re-run the cases that quote `cta.*`.
2. **K39 (EN). The multi-income question only across different buyers** (#10).
   - `core/en/start-block.md` L22: "Several income streams:" → "Streams for different buyers:" (+6 chars).
   - `modules/en/setup.md` L16 §CM-SETUP 6: "2+ paid streams:" → "2+ paid streams, different buyers:" (+18 B).
   - A sprint followed by a retainer is one buyer, and the question cost Erin a turn and 1.9 min.
   - VN is unchanged: both VN guesses were across different buyers.

**P2: real defects, ungraded**

3. **K40 / VK-34. FILM TODAY's text version carries the keyword outside the ask** (Tuấn, consultant VN, EN).
   - VN `modules/vn/fmt-short.md` L21 §CM-FORMATS 7: "bài chữ = câu đầu + caption, một khung" → "…, một khung, có từ
     khoá ngoài lời mời" (+35 B).
   - EN `modules/en/fmt-short.md` L12 §CM-FORMATS 7: "as text = first line + caption, one box" → "…, one box, keyword
     outside the ask" (+25 B).
   - **VN cut:** `strings/vn.toml` L134 `save.claude_plain`, drop " Đoạn chat này không mất đâu." (−38 B, §CM-CARD 5;
     a reassurance, not a rule).
   - Pair it with G36.

**P3: one run, wording, or optional**

4. **VK-35. The plan-line tag names the guess** (Tuấn, consultant).
   - `strings/vn.toml` L272 `setup.plan_guess`: "(mình đoán, gõ một chữ là đổi)" → "({chỗ đoán}: mình đoán, gõ một chữ
     là đổi)" (+16 B).
   - **Cut:** `modules/vn/setup.md` L16 §CM-SETUP 3: "Không bắt tải, đính kèm, cài đặt, đổi máy" → "Không bắt tải, cài
     đặt, đổi máy" (−13 B; "tải" covers it, and EN has no "attach").
5. **Machine slips the kit already covers (no change):**
   - EN's 13-word first line;
   - EN's card not trimmed. If it recurs, change `modules/en/brain.md` L16 "passages (≤60 words)" → "(≤40 words)" (0 B);
   - Tuấn's FILM TODAY last line losing "nha bạn";
   - the "Gợi ý:" labels (line 2 above). They need block room that is not there now.
6. **Strings for the next native pass** (need a VN cut):
   - §CM-MESSAGES 3 DỪNG line → "Chưa cần mấy tin này thì nói mình một tiếng nha." (+3 B);
   - `research.ask3` opening with "{gọi} ơi," (line 7 above).

### Graders (`evals/graders.py` unless noted)

- **G31** (if the founder agrees, below). `check_day0` L3477 (the Map turn count): leave out a coach turn that is mostly
  pasted posts, using the POST_RUN test `dump_cut` already uses. Hạnh and consultant VN then read 7.
- **G32.** `check_day0` L3550: an early win in the reply to the first send is a warning whenever it is over budget.
  Drop `first_send > limit`. Tuấn's FP.
- **G33.** `NEGATED_BEFORE_RE` L1704: add "hổng|hông". Tuấn's I11 FP on "hổng phải cam kết".
- **G34.** `reply_decisions` L1363 (I6): skip a line that reprints a Map topic, as a Week-1 heading does. Consultant's FP.
- **G35.** Piece boundaries: a piece ends at its copy box. A bare label line ("Tin trả lời inbox 1", "DM reply 1") or
  the card title starts the next block. This catches Tuấn's N3 and keeps the card out of the last Week-1 piece.
- **G36.** `check_day0_shape` L3974–3978 (G30): grade FILM TODAY's text version (first line + caption) on its own, together
  with K40.
- **G37.** `check_vn_natural` L2919: leave out the card top, dated notes and bare labels. Count a box printed twice once
  (the gift and inbox 1). Compare with the posts the coach pasted, not all of `written-posts.md`.
- **G38.** "Week 1 has an email when the coach named a list" L3923–3953: read VN "email thì có 250 người" and `list_size:
  email 250 · …`. It was not run for consultant VN.

### Protocol

- **P14.** `evals/run.py` `check_pace` L566: drop pasted-post paragraphs (POST_RUN against `written-posts.md`) from the
  dictated words, and require ≥0.5 min per pasted post instead. Tuấn's run was invalid for the wrong reason; the real
  slip was 0.4 min.
- **P15.** The round brief told all 3 VN simulators "about 1,500 tiếng". DECISIONS lowered it to 1,200 after VG2, and
  the acceptance comment leaves pasted posts out. Fix the brief. Three of the "kit breaks" filed this round (one per VN
  run) come from it.
- **P9** still applies: wording priming (section 5).
- **Re-run:**
  - Hạnh and Tuấn VN after VK-33 and G37 (Tuấn also needs a valid sample);
  - EN consultant after K39 and K40;
  - consultant VN after G31/G34.

### Founder call

- **(a) The Map turn budget with P10.** The kit asks for a send every 2–3 minutes, and P10 splits long chunks.
  - So a 10-minute dump is 4 sends. Add Start, the xưng hô turn, a posts turn and one answer, and a VN Map lands at
    turn 8 (EN: 7), even when the machine asks only the one question the kit allows.
  - DECISIONS says the posts "add no extra turn".
  - Recommendation: do not count a posts-only turn (G31), and keep counting dump sends.
  - The alternative is to raise `map_max_turns_*` by one.
