Result: FAIL

# Retest VG3 (VN ×4) + G4 (EN coldstart) Day-0 after the retest fix round: independent review

Reviewer: independent and bilingual (EN, plus native Vietnamese for the VN runs). I wrote neither the kit nor the runs.

Kit under test: `bf1b910` (kit fixes) and `921999a` (graders G19–G26, P12/P13/VP-2). `659b14c` touches eval cases only.
Each run's `packet/kit/` is byte-identical to the current `dist/`:
- EN: block 6,487 chars NFC (the build reports 6,488) of 6,500; method file 49,041 of 51,200 B. Run build `1f3258d39313`.
- VN: block 7,499 of 7,500; method file 56,304 of 56,320 B. Run build `97ac3db975fb`.

How this review was done:
- All 5 transcripts were read in full, as the coach would read them on their phone.
- Scratch copies of the 5 folders were re-graded with the current `evals/run.py grade`. The verdicts match the stored
  `grades.json` exactly; `transcript.jsonl` equals `transcript.raw.jsonl` in 5/5 (edited: 0). Run folders untouched.
- Every failed check was traced to its transcript line and to the kit line or grader code behind it.
- Leaks were checked in 2 runs (Hạnh, Dan) with my own scan; method in section 5.
- VN naturalness was scored on `qa/standards/vn-naturalness.md` (VN1–VN8). Every line I mark is quoted with a fix.

## Why FAIL

- **VN grader passes: 0/4.** 9 failed checks in the 5 runs: 7 real (all VN), 2 false positives.
- **YOUR WORD only in the ask, in 3/4 VN runs.** It is always the one long-form text piece of Week 1: Hạnh's long
  post, Tuấn's Facebook long post, consultant's carousel. Hạnh's FILM TODAY caption has the same defect (ungraded).
  - The fix worked for every short and post: graded pieces with the defect went from 7 to 3.
  - Likely cause: the §CM-WEEK 4 rotation ends in "pinned comment" / "comment ghim", a spot outside the body. The 3
    shorts take hook, on-screen text, payoff and caption line 1, and the 4th piece lands on the pinned comment.
- **VN particles still too flat in 2/4** (`vn_natural`): Hạnh 17% of sentences against 53% in her own posts, Tuấn 15%
  against 46%. Counting each distinct sentence once, Hạnh is at 19%, still under the 21% floor. The method-file
  nudge "dày như bài họ" lifted coldstart (26% → 67%) but not these two.
- **VN release bar not met.** Two critical items are at 1:
  - coldstart, coach-facing VN6: "nên mình kể chuyện của chính bạn" (the same calque as last round);
  - Tuấn, 1:1 register VN4: past clients are called "bạn", but his own register with clients is chị/anh–em.
- **consultant VN film-ready 20.3** (max 20). The cut came on time, and he did not keep talking after it. The cause is
  his two 7-minute dictated chunks (P10). The machine and the kit had no slack left.
- **coldstart VN "Ngắn thôi" is a kit conflict.** The required card top counts as talk.
- **Leaks: clean on facts, but persona wording still primes the machine side** (4 lifts in EN, 1 in VN). P9 is still
  the real fix.

**What passed:**
- **EN coldstart passes the grader.** This is the first pass for this persona:
  - Map at coach turn 5, film-ready at 16.0;
  - "Shorter" got 88 words of talk, and the card came on the next message;
  - card top 437 chars, whole card 4,868.
- **The soft cut fired on time in 5/5 runs:**
  - always after chunk 2, never after chunk 1;
  - always one message with one question mark;
  - 0 extra coach turns.
- **`[Tên]` blanks in 1:1 messages: 0/4** (was 3/4).
- **The reminder names the day in 5/5.**
- **`multi_income`:** one question, and it reads natural.
- **"một góc của":** gone.
- **The two coach-facing strings:** right in 4/4.
- **Spoken objections to comment asks:** honoured at once in 2/2, and Dan's typed "quiet" was taken too.
- **Platform and list:** 0 wrong visible guesses (last round: 4), because VP-2 makes the up-front ask testable.
- **VN coach-facing prose passes in 3/4** (was 1/4).
- **0 quits.** Every coach comes back.

## 1. The runs

Previous-round figures are in brackets: VG2 for VN, G2 for EN coldstart.
- "Map turn" is the coach turn the Map answers. It is also the film-ready turn (K2).
- "Early win" shows the minute the copy box arrived, then, after "·", the minutes counted from the dump prompt
  (acceptance ≤4, graded as a warning).

Verdict codes:
- R(kit): the kit wording caused it.
- R(m): a machine slip.
- R(pace): the persona's dictation length caused it.
- FP: a grader false positive.
- W: a warning under the founder's "one more story" rule.

| Run | Lane · app | Valid | Coach turns | Map turn | Early win | Film-ready (active) | Grader failures: verdict |
|---|---|---|---|---|---|---|---|
| EN coldstart (Dan) | S1 · ChatGPT Plus, iPhone | yes | 8 (6) | 5 (5) | 6.1 · 5.7 | 16.0 (14.3) | **none: PASS** |
| VN Hạnh | S1 · ChatGPT Free, Android | yes | 8 (8) | 6 (6) | 7.8 · 6.0 | 21.6 W (22.5) | day0_shape R(kit) · vn_natural R |
| VN Tuấn | S1 · ChatGPT Plus | yes | 7 (8) | 6 (6) | 8.7 · 7.3 | 18.8 (22.7) | I11 FP · day0_shape R(kit) · vn_natural R |
| VN coldstart (Minh Anh) | S1 · ChatGPT Free, iPhone | yes | 9 (9) | 7 (7) | 8.3 · 6.7 | 17.8 (21.4) | day0_shape R(kit conflict): "Ngắn thôi" |
| VN consultant (Khoa) | S1 · Claude Pro | yes | 7 (7) | 6 (6) | 9.0 · 7.5 | 20.3 (21.4) | I8 FP · day0_timing R(pace) · day0_shape R(kit) |

Totals:
- **Valid: 5/5. Grader pass: 1/5** (EN coldstart). Quits: 0. Comes back: 5/5.
- **Failed checks: 9.** 7 are real (all VN) and 2 are false positives.
  - Real by cause: the kit's keyword rotation (3), a kit conflict (1), particle density (2), coach pacing (1).
  - On the same 4 VN personas last round: 17 failed checks, 12 real and 5 false positives.

| Budget (acceptance `[day0]`) | EN coldstart | VN 4 runs |
|---|---|---|
| Map ≤6 coach turns (VN ≤7) | 1/1 (5) | 4/4 (6–7) |
| Film-ready ≤20 active min | 1/1 (16.0) | 2/4 pass, Hạnh warn (kept talking +5.4), consultant fail (20.3) |
| Soft cut on time (≤1,200 words / tiếng) | 1/1 (1,371) | 4/4 (1,246–1,691) |
| ≤10 coach turns | 1/1 (8) | 4/4 (7–9) |
| Session ≤40 active min | 23.3 | 21.2–28.9 |
| Card top ≤500 / whole ≤5,700 EN, 6,600 VN | 437 / 4,868 | 419–474 / 5,036–5,692 |
| Early win ≤4 min after the dump prompt | 0/1 (5.7) | 0/4 (6.0–7.5); all on the first send |

## 2. Did the fixes aimed at each run work?

| Run | Fix aimed at it | Worked? | Evidence |
|---|---|---|---|
| VN all | VK-21 cut at ~1,200 tiếng | **yes, 4/4** | All 4 cut at T5, after chunk 2: Hạnh at 1,246 dictated (the same 1,246 stayed under ~1,500 last round), Tuấn 1,641, coldstart 1,423, consultant 1,691 |
| VN all | VK-22 no `[Tên]` | **yes, 4/4** | Hạnh "Em ơi, chị nhờ em một chút nhé…"; coldstart "Mình Minh Anh nè :))…"; consultant "Anh ơi, nhờ anh một chút…" under "(khách là chị thì đổi "anh" thành "chị")". Tuấn has no blank, but the register is wrong (§6) |
| VN all | K35/VK-25 keyword once in the body + the ask | **partly** | Pieces with the keyword only in the ask: 7 → 3. The shorts and posts now carry it (Tuấn 4 → 1). The long-form piece still does not: Hạnh long post, Tuấn FB long post, consultant carousel (coldstart 0). Hạnh's FILM TODAY caption too |
| VN + EN | K36 the reminder names the day | **yes, 5/5** | "Muốn em nhắc vào thứ Hai và thứ Sáu không?" (Hạnh, Tuấn, consultant); "…vào Chủ nhật…" (coldstart); "Want a nudge on Sunday and Friday?" (Dan). Consultant's Monday is a wrong guess (his day is Sunday); it is now where he will correct it |
| VN Tuấn | VK-23 `multi_income`, one question | **yes** | T5 has one "Đúng không anh?". "vì mấy thứ anh bán, họ đều cần: căn hộ, với bảo hiểm che người đứng tên vay" reads natural |
| VN Hạnh | VK-23 template | **false here; the machine adapted** | Her two incomes have different buyers, so "họ đều cần" is untrue. The machine wrote "vì việc kèm là chị bán cho các em ấy" instead (true) |
| VN coldstart, consultant | VK-24 "lồng vào ý lớn" | **yes** | "…ăn trưa tại bàn mình lồng vào chủ đề 1"; "cái nào dính tới giữ người mới thì em lồng vô bài" |
| VN coldstart | coach-turn count | **same as VG2** | 9 coach turns, Map at 7 (the VN limit). The avoidable second guess is back for a second round: T6 "bạn chưa bán gì online…" right after her "chưa có khách online nào hết" |
| VN Hạnh | film-ready ≤20 | **cut yes; minutes a warning** | Cut + guess at T5. She left for 25 min and came back with chunk 3 (+5.4 min), so the Map came at 21.6 active. A warning under the founder rule; without chunk 3 it is ≈16.2 |
| VN consultant | spoken objection to comment asks | **yes** | "Comment từ khóa nghe giống bán hàng online quá" → "Rồi, em bỏ xin comment, bài nào cũng mời nhắn riêng." Caption line 3 was reprinted; every Week-1 ask is quiet |
| VN coldstart | spoken objection to comment asks | **yes** | "Rồi, khỏi xin comment. Lời mời từ giờ là: "Nhắn mình chữ CỨNG ĐƠ…"" |
| VN all | the two coach-facing strings | **yes, 4/4** | "Quay luôn bây giờ, hoặc đăng phần chữ làm bài viết." · "(Ngại xin comment thì gõ 'nhẹ'.)" |
| VN all | 1:1 message register | **3/4** | Right in Hạnh (chị–em, Bắc), coldstart (mình–bạn) and consultant (tôi–anh + swap note). Tuấn calls past clients "bạn" |
| EN coldstart | K27 "Shorter" → card on the next message | **yes** | T6: Week 1 boxes only, 88 talk words, "NEXT → Say 'ok' and I'll print your Brand Card to save." The card came at T8, after "brb" / "ok back" |
| EN coldstart | Map ≤6, film-ready ≤20 | **yes** | Map at turn 5, 16.0 min |
| EN coldstart | list and platform heard or guessed visibly | **yes, right** | IG 340 and TikTok 210 heard in chunk 1; "email list: none (my guess; one word changes it)" (true: 0) |
| EN coldstart | card length, save line | **yes** | Top 437, whole 4,868. Route + "Backup: email it to yourself" (G2 had no backup) |

## 3. The founder's Day-0 rules in practice

| Run | Early win: line in the copy box | Arrived · postable? | Soft cut | One message, one question? | Cost? | Facts asked up front / guessed visibly |
|---|---|---|---|---|---|---|
| EN Dan | "30 minutes you actually do beats an hour you never do." | 6.1 · yes, his own principle | after c2 (1,371 words), with "no client result yet … not your brother's" | yes | no turn: he told one more story and the 22-lb pushback in the same turn | Platform heard; list "none" guessed (right); talk day Sunday (right) |
| VN Hạnh | "41 thẻ thì 27 thẻ khách bỏ dở giữa chừng… mình bán được thẻ chứ mình có giữ được người đâu." | 7.8 · partly: "41 thẻ" needs "Năm 2018 spa chị…" to stand alone (as VG2) | after c2, with the multi-income guess; "Không vội đâu, chị cứ ra với khách" merged with her "chờ chút" | yes | no turn; +5.4 min (her chunk 3, told after 25 min away) | Not VP-2 (answer bank only). FB guessed (right); list "chưa có" (her 3,200 Zalo contacts are spa customers: defensible); talk day Mon (right) |
| VN Tuấn | "Tui không hỏi anh chị thích căn nào, tui hỏi mỗi tháng góp bao nhiêu mà vẫn ngủ được." | 8.7 · yes, in his "tui" | after c2, with the multi-income guess | yes | no: "Đúng rồi em… Xong.", chunk 3 skipped (VG2: +5.7 min) | VP-2: TikTok, FB, Zalo 1,850 and no email heard. The plan line still tags them "(em đoán…)" |
| VN coldstart | "Đi tập 90 phút cuối tuần mà cả tuần ngồi y chang thì cũng chỉ là chữa cháy thôi. Cái lưng nó cần mỗi ngày, ko phải mỗi tuần." | 8.3 · yes | after c2, with the no-result guess (plus one line on the friend's story) | yes | the cut: no. The second guess at T6 cost +1 turn, +0.9 min | VP-2: TikTok 640, FB, Zalo 240, no email heard |
| VN consultant | "Tuyển 15 phút thì người ta ở 15 ngày." | 9.0 · yes | after c2, with the offer guess + "Có giá thì anh ghi luôn." (no "?") | yes | no | VP-2: LinkedIn, FB, Zalo 380, email 250 heard. Talk day Mon guessed (wrong: Sun); shown twice |

Findings:
- **Early win: 5/5** in a copy box on the first send; postable as is in 4/5.
  - It still lands 5.7–7.5 min after the dump prompt. Each persona's first send is 595–820 words dictated over
    5.4–7.2 min, while the kit asks for sends every 2–3 min (P10).
- **Soft cut: 5/5** were one message with one "?", and cost 0 extra turns.
  - One cost minutes: Hạnh's "one more story", accepted by the founder.
  - Tuấn, who cost 5.7 min last round, took the guess and stopped.
- **Facts up front:**
  - With VP-2, the up-front ask now works: 0 wrong platform or list guesses (VG2: 4).
  - `setup.plan_guess` prints its whole line, so heard facts get "(em đoán)" in Tuấn and consultant.

## 4. Failed grader checks: real or false positive

| # | Run · check | Transcript line | Kit line or grader code | Verdict |
|---|---|---|---|---|
| 1 | Hạnh · day0_shape | T7 long post opens "Các em ạ, chị nói thật nhé, bước các em hay bỏ nhất không phải lúc chào thẻ." "ngại chào" is only in "Em nào đang ngại chào thì comment NGẠI CHÀO…" | `modules/vn/plan.md` L17 §CM-WEEK 4, rotation "… → dòng 1 caption → comment ghim" | **R(kit)** |
| 2 | Hạnh · vn_natural 17% vs 53% | N1, N2 captions and the long post end flat: "…chị gửi 3 bước cầm gương nói thật." Her posts: "chị nói thật nhé", ":))", "e ạ" | `modules/vn/humanize.md` L32 "dày như bài họ" sits only in the method file; block `core/vn/start-block.md` L51 says only "tiểu từ theo bài coach" | **R** (VN5 = 1). Not the duplicated gift: distinct sentences give 19%, still under 21% |
| 3 | Tuấn · I11 "cam kết", "lãi suất cam kết" | card `not_now`: "sản phẩm mới công ty đang thi đua, lãi suất cam kết (dễ thành hứa quá lời)" | `i11_injection` (graders.py L1721) skips never_say, do_say and principles, but not `not_now` | **FP**: a parked item names the claim in order to refuse it |
| 4 | Tuấn · day0_shape | FB long post "Lương hai vợ chồng 32 triệu, suýt cọc căn 3 tỷ 1." … "gồng lãi" is only in "comment GỒNG LÃI hoặc inbox tui" | as #1 | **R(kit)** |
| 5 | Tuấn · vn_natural 15% vs 46% | long post: "…tui gửi tờ tính ngược trước khi cọc."; Bán kèm: "…thì inbox tui." His posts: "nha", "nè", "á" | as #2 | **R** (VN5 = 1) |
| 6 | coldstart · day0_shape "Shorter" 170 > 90 | T9, after "Viết ngắn thôi, đọc trên điện thoại mỏi mắt.": 95 tiếng are the card top (it must be outside the box) and 75 the rest. The card had already been put off once (T8) | `modules/vn/levelup.md` L12 §CM-TODAY 1 "lời nói ≤120 tiếng … card ở tin sau" vs §CM-CARD 2 visible top. The grader caps at EN's 90 (`acceptance.toml` L41, `SHORTER_MAX_WORDS` L288); the VN kit says 120 | **R(kit conflict).** The machine chose right (the card was due). Without the top: 75, under both caps |
| 7 | consultant · I8 "11" | carousel "Trang 11: Chuỗi quán hải sản 45 nhân viên…" | `i8_numbers` (L1485) reads the page label as a claim | **FP** |
| 8 | consultant · day0_timing 20.3 | Cut on time (T5, 1,691 tiếng). The offer guess is one of the 3 askable facts, and the card needs the price for inbox 2. Chunks: 822 and 871 tiếng, 7.2 and 7.1 min | `check_day0_timing`: a warning only when the coach keeps talking after the cut | **R(pace)**, +0.3 min. The machine had no slack: cut → answer → Map. P10, founder |
| 9 | consultant · day0_shape | carousel: TUYỂN HOÀI only on "Trang 12: Mẫu phiếu việc 1 trang: anh chị nhắn tôi chữ TUYỂN HOÀI, tôi gửi." | as #1 | **R(kit)** |

Rotation evidence for #1, #4 and #9: the Week-1 pieces before the failing one each used a spot inside the body.
- Hạnh: N1 on-screen "Ngại chào vì sợ lừa khách?", N2 caption line 2, N3 on-screen "Hai kiểu chủ spa ngại chào".
- Tuấn: N1 caption line 1 "Nói vụ gồng lãi…", N2 hook "…sợ gồng lãi không nổi…", N3 payoff "…về gồng lãi nha bạn".
- consultant: post 1, the email and post 2 all have "tuyển hoài" in the body.
- In each run, the next piece (long post or carousel) has the keyword nowhere but the ask.

Grader misses:
- **Hạnh's FILM TODAY caption** has "ngại chào" only in its ask sentence. The keyword item (graders.py L3863) reads
  Week-1 pieces only.
- **The "Shorter" cap** is one number for both editions, while the VN kit says ≤120 tiếng.
- Tuấn's Zalo broadcast holds "gồng lãi" only in its ask, but it is not a public piece (`_public_piece`). Left as is.

## 5. Leak spot-check (2 runs)

**Method:**
- For every machine turn, I listed each 5-gram (EN words, VN tiếng, case-folded) that is also in the persona's
  `persona.toml`, `answers.md`, `expected.toml`, `voice-samples.md`, `launch-brief.toml`, `pillar-transcript.md`,
  `paste-dump.md` or `written-posts.md`. I removed 5-grams of the coach's turns so far and of the kit.
- I also listed every number the coach had not said.
- Each hit was then read against the transcript.

**Hạnh: clean on facts; one wording lift.**
- 179 hits; all but one join her own words: "cầm gương nói thật", "bán buổi hẹn sau", "41 thẻ thì 27", "Loan Hưng Yên
  khóa 1", "6 tuần … tháng 7".
- New numbers: dates; "21" (her "tối thứ Hai 9 giờ" as 21h); "6.500.000" (her "6 triệu rưỡi" in the kit's price
  format).
- **The one lift is the save line**: "Không thấy nút đó thì chụp màn hình gửi vào Zalo "Cloud của tôi"".
  - `answers.md` L65 says "Cái gì cần giữ thì chụp màn hình gửi vào Zalo "Cloud của tôi"".
  - She said only "cái gì quan trọng chị gửi vào zalo cờ lao của tôi", nothing about screenshots.
  - The kit says "gửi vào Zalo", and a screenshot cannot hold a 1,100-word card.
  - So this is a persona habit lifted into the machine side, and it makes the backup worse.
- The card's never_say ("trị dứt điểm | nám kín mặt | giảm sốc") overlaps the persona's list. I do not count it: each
  item is a line from her 2018 story that she rejects.

**EN Dan: clean on facts; four wording lifts, all from text he never dictated.**

| Machine text | Persona source | What he said |
|---|---|---|
| gift, DM reply 1: "Pick 3 slots of 30 minutes in your real week" | `answers.md` L35 (chunk 3, skipped): "3 slots of 30 minutes that survive your actual family calendar"; pillar-transcript L72 | "30 minutes in the garage, 3 times a week" |
| gift: "Gear: one kettlebell. A pull-up bar…" | `answers.md` L55 "Gear: one kettlebell, a pull-up bar, maybe a bench" | the same facts, without the label (the simulator flagged this one too) |
| card `proof`: "carries both kids up the stairs at once" | `persona.toml` L121 / launch-brief "can carry both kids up the stairs at once" | "at the same time" (G2 flagged the same lift) |
| long caption: "every plan out there is built for a 25 year old with no kids" | pillar-transcript L18 "every plan out there is like that" | "Everything out there is built for a 25 year old with no kids" |

- Trap numbers (22, 4 months, 200) never appear. The hard stop quoted only "my brother lost…".
- New numbers are dates only (13, 14, 17, 2026).
- **Verdict:** no fact reached the machine before the coach said it, so both runs stay valid. But both simulators
  read the persona files before writing the machine side, and wording leaks through. Tuấn's notes.md says so
  ("the simulator had read persona.toml … possible contamination"). P13 freezes edits; only P9 (a machine side that
  never sees the persona) stops priming.

## 6. VN naturalness (VN1–VN8)

Bars, from `qa/standards/vn-naturalness.md`:
- **Pieces:** VN3, VN4, VN6 and VN7 at 2; total ≥13/16.
- **Coach-facing prose and Map lines:** VN3, VN4 and VN6 at 2; total ≥10/12.

Regions: Bắc (Hạnh), Nam (Tuấn, coldstart), Trung/Quảng (consultant).

| Run | Coach-facing /12 | Map lines /12 | QUAY HÔM NAY /16 | Week-1 posts /16 | Zalo + inbox /16 |
|---|---|---|---|---|---|
| Hạnh | 11 ✓ (VN1 1: "Brand Card", "Lưu vào dự án") | 11 ✓ (VN2 1: line 1 tacks on "bán thẻ 30 buổi, 3 bước học trong 6 tuần") | 15 ✓ (VN5 1) | 15 ✓ (VN5 1) | 16 ✓ |
| Tuấn | 11 ✓ (VN1 1) | 11 ✓ (VN2 1: four methods + a tail) | 16 ✓ | 15 ✓ (VN5 1; VN7 now 2: the FB post says "tui") | **14 ✗** (VN4 1: past clients called "bạn"; VN8 1: DỪNG in a one-off) |
| coldstart | **10 ✗** (VN6 1: "chuyện của chính bạn"; VN1 1) | 11 ✓ (VN2 1: methods stacked) | 16 ✓ | 16 ✓ | 16 ✓ |
| consultant | 11 ✓ (VN1 1: "Add text content") | 12 ✓ (fixed line 1) | 16 ✓ | 16 ✓ | 16 ✓ |

Totals:
- Coach-facing prose passes in **3/4** (VG2 1/4).
- QUAY HÔM NAY passes in **4/4**, and Week-1 posts in **4/4** (VG2 3/4).
- Messages pass in 3/4, with 0 `[Tên]` blanks.
- **Release bar not met:** coldstart VN6 and Tuấn VN4 (both critical) are at 1.
- 0 essay connectors and 0 banned tells in 4/4. `vn_natural` patterns: 0 in 4/4.

Lines that still read translated or stiff (D = translated, S = stiff), with a natural version:

1. D · coldstart T5 (`setup.guess_no_result` + "chính"): "nên mình kể chuyện của chính bạn."
   - Back-translates cleanly ("so I'll tell your own story"). The kit's "chuyện của bạn" became ambiguous after the
     friend's story, and the machine added "chính".
   - Fix: "nên mình kể chuyện hồi bạn còn làm kế toán, cái tối 9 giờ đó. Đúng không?"
2. VN4 · Tuấn, ask-3 Zalo: "Nhờ bạn chút nha: mình đang viết lại phần giới thiệu công việc, muốn dùng đúng lời của
   bạn. Hồi mới tìm tới mình, bạn đang loay hoay nhất chuyện gì?"
   - In his dump he calls clients "chị" ("Tui nói chị ra khỏi toilet đi"), and they call him "anh Tuấn".
   - "mình – bạn" is his TikTok pair. The machine read §CM-NATURAL 4's 'không "anh/chị"' as "don't use anh or chị".
   - Fix: "Chị ơi, em Tuấn nè. Nhờ chị chút nha: em đang viết lại phần giới thiệu công việc, muốn dùng đúng lời của
     chị. Hồi mới tìm tới em, chị đang loay hoay nhất chuyện gì?" Above the box: "khách là anh thì đổi 'chị' thành
     'anh'".
3. S (call-centre) · Tuấn's Zalo to acquaintances: "Không muốn nhận nữa thì nhắn mình chữ DỪNG.", under the title line
   "Lãi ưu đãi là lãi của năm đầu". This repeats last round's #9.
   - Fix: drop the title and end "Chưa cần thì cứ nói Tuấn một tiếng, Tuấn không nhắn nữa nha."
4. S · Hạnh T6 "Em chạy thử 4 tuần nhé." and consultant T6 "Em chạy thử 4 tuần nghe anh." (2/4 again)
   - The pair swap turns the inclusive "Mình" of `map.ok` into "Em".
   - Fix: "Chạy thử 4 tuần nhé chị." / "Chạy thử 4 tuần nghe anh." (subject dropped, §CM-NATURAL 2).
5. S (form label) · the jogger after the pasted posts is introduced with "Gợi ý:" in 4/4. Natural versions:
   - Hạnh: "Gợi ý: các em chủ spa hay than với chị câu gì, chị kể đúng nguyên lời các em ấy nhé." → "Các em chủ spa hay
     than với chị câu gì, chị kể đúng nguyên lời các em ấy nhé."
   - Tuấn: "Gợi ý cho chuyện kế: bên bảo hiểm anh chưa kể, kể em nghe một nhà mà hợp đồng anh bán gánh được lúc có
     chuyện." → "Bên bảo hiểm anh chưa kể nè: có nhà nào lúc có chuyện mà hợp đồng anh bán gánh được, anh kể em nghe."
   - coldstart: "Gợi ý: kể mình nghe bạn chỉ một bạn văn phòng làm gì, từng bước, rồi bạn đó khác đi ra sao." ("bạn"
     means two people) → "Kể mình nghe bữa bạn chỉ cho một học viên văn phòng: làm gì, từng bước, rồi người đó khác
     đi ra sao."
   - consultant: "Gợi ý cho đoạn kế: một khách đổi khác ra sao sau khi làm với anh, có số càng tốt." → "Anh kể thêm
     một khách: làm với anh xong thì khác ra sao, có số càng tốt."
6. S · coldstart Map: "TỪ KHOÁ: CỨNG ĐƠ (không dấu: CUNG DO) · mình đoán, Tuần 1 kiểm lại".
   - The keyword was heard many times, and "Tuần 1 kiểm lại" means nothing to her.
   - Fix: "TỪ KHOÁ: CỨNG ĐƠ (gõ không dấu "cung do" cũng tính)".
7. S (attribution) · coldstart N3 caption: "Lưng cứng đơ mà chỉ chữa cháy cuối tuần thì cháy hoài á. / Chị làm ngân
   hàng nói câu đó với mình, y chang mình hồi xưa luôn."
   - "câu đó" now points at her own line, so the bank client seems to have said "cháy hoài".
   - Fix: "Đi massage về được hai bữa rồi đâu lại vô đó, chị làm ngân hàng nói với mình vậy á. / Y chang mình hồi xưa
     luôn. Chữa cháy cuối tuần thì cháy hoài."
8. S · Hạnh N2 câu đầu: "Học mấy khóa chốt sale về, nhân viên em nói câu nào khách cũng sợ."
   - These are Loan's words, spoken by Hạnh, who calls herself "chị", with no attribution.
   - Fix: "Loan bảo chị: "Học mấy khóa chốt sale về, nhân viên em nói câu nào khách cũng sợ."" (17 tiếng).
9. VN5 · flat endings against the coach's own rate:
   - Hạnh: "…chị gửi 3 bước cầm gương nói thật." → "…chị gửi 3 bước cầm gương nói thật nhé :))"
   - Tuấn: "…tui gửi tờ tính ngược trước khi cọc." → "…tui gửi tờ tính ngược trước khi cọc nha."
   - Tuấn: "Nhà nào đang kiếm căn tầm giá này thì inbox tui." → "…thì inbox tui nha."
10. S (brochure) · Map line 1 still stacks methods in 3/4 (P3, as last round).
    - Tuấn: "…thì tìm Tuấn: tính ngược từ tiền góp, chừa quỹ 6 tháng, che người đứng tên vay rồi mới cọc, chứ không
      cọc trước tính sau, biết giá căn tối đa trước khi đi coi nhà."
    - Fix: "Vợ chồng trẻ nào hay than "sợ gồng lãi" thì tìm Tuấn: tính ngược ra giá căn tối đa rồi mới đi coi nhà, chứ
      không cọc trước tính sau."
11. S · Hạnh's save line "chụp màn hình gửi vào Zalo" → "chép card gửi vào Zalo "Cloud của tôi"" (section 5).

Keep these; they read like a person:
- Hạnh T5: "Dạ được chị, em nhận rồi. Không vội đâu, chị cứ ra với khách."
- Hạnh inbox 1: "Chị hỏi em một câu: em đang mở spa, tự tư vấn cho khách, hay em đang tìm chỗ làm da cho mình?"
- Tuấn T6: "Căn 2 tỷ 68 em không bỏ đâu: Tuần 1 có một bài bán kèm, với tin inbox cho nhà đang kiếm căn."
- Tuấn's long post: "Chuyện của một nhà thôi nha, nhà nào con số cũng khác, không phải cam kết."
- coldstart T8: "Được, quay động tác thôi, khỏi nói trước máy…" and "Không bỏ đâu: gối cao, nằm sấp lướt điện thoại tới khuya,
  ăn trưa tại bàn mình lồng vào chủ đề 1".
- consultant T7: "Vẫn một ý cho chủ doanh nghiệp nhớ anh, mà nói rõ anh làm nhân sự chứ không đăng tin hộ."
- consultant's LinkedIn post: "Có điều cái tuyển hoài nó ăn mòn họ. Tối nào cũng lo mai ai đứng ca."
- consultant inbox 2: "Chưa cần thì anh cứ giữ phiếu việc mà dùng."

## 7. What improved vs the previous round (same personas)

| Measure | VG2 (VN ×4) / G2 (EN coldstart) | VG3 / G4 |
|---|---|---|
| Grader passes | VN 0/4; EN coldstart fail | VN 0/4; **EN coldstart pass** |
| VN failed checks: real / FP | 17: 12 / 5 | **9: 7 / 2** |
| VN soft cut on time | 3/4 (Hạnh never cut) | **4/4** |
| VN film-ready, active | 21.4, 22.5, 22.7, 21.4: 0/4 | 17.8, 21.6 W, 18.8, 20.3: **2/4 + 1 warning** |
| "One more story" cost | Tuấn +5.7 min | Hạnh +5.4 (warning by founder rule); Tuấn 0 |
| VN coach turns / Map turn | 7–9 / 6–7 | 7–9 / 6–7 |
| `[Tên]` in 1:1 messages | 3/4 runs | **0/4** |
| VN pieces with the keyword only in the ask | 7 (Tuấn 4, Hạnh 2, consultant 1) | 3 graded + 1 FILM TODAY |
| Reminder says "ngày nói chuyện" / "talk day" | 4/4 VN | **0/5**: the day is named |
| `multi_income` | calque ("hơn một thứ") | natural, one question; the reason is untrue in 1/2 |
| "một góc của" | 2/4 | **0/4** |
| `vn_natural` (pieces / their posts) | coldstart 26/64, Hạnh 12/53, Tuấn 11/46 | coldstart **67/64**, Hạnh 17/53, Tuấn 15/46, consultant 6/6 |
| VN coach-facing prose passes | 1/4 | **3/4** |
| VN Week-1 posts pass | 3/4 (Tuấn's FB post said "mình") | **4/4** ("tui") |
| Wrong visible platform / list guesses | 4 | **0** |
| Wrong talk-day guesses | 3/8 | 1/5, now shown in the reminder |
| EN coldstart after "Shorter" | 1,930-word reply, 164 talk words, card in it | Week 1 boxes, **88 talk words, card next** |
| EN coldstart save line backup | missing | route + email backup |
| Early win ≤4 min after the dump prompt | 0/8 | 0/5 (first sends run 5.4–7.2 min) |

## 8. Prioritised fix list

Budgets now: EN block 6,488/6,500 (build count), EN method 49,041/51,200 B. VN block 7,499/7,500, VN method
56,304/56,320 B. Every VN change below names its cut. After items 1–7:
- **VN block 7,480** (−17 +3 −5).
- **VN method 56,314** (−33 +19 +11 +13; 6 B left).
- **EN method 49,085** (+21 +23). The EN block is unchanged.

### Kit

**P1: blocks acceptance**

1. **K37 / VK-26. A keyword spot inside long text pieces** (#1, #4, #9 and Hạnh's FILM TODAY).
   - EN: `modules/en/plan.md` L11 §CM-WEEK 4 "→ caption line 1 → pinned comment." → "→ caption line 1 → a long
     post's or carousel's opening." (+21 B).
   - VN: `modules/vn/plan.md` L17 "→ dòng 1 caption → comment ghim." → "→ dòng 1 caption → mở đầu bài dài,
     carousel." (+19 B). Refresh the `plan.kit-week` src hash.
   - Why: a pinned comment is not in the body, so the piece that draws that spot fails "once in the body" in 3 of 3
     failing runs.
2. **VK-27. Particle density in the block** (#2, #5).
   - Change: `core/vn/start-block.md` L51 TIẾNG VIỆT "tiểu từ theo bài coach" → "tiểu từ dày như bài coach" (+3
     chars).
   - Cut: L34 step 2 "Lộn xộn cũng được, để mình sắp xếp." → "Lộn xộn cũng được." (−17; EN has only "Messy is
     fine.").
   - Why: the method-file rule alone moved one run of three.

**P2: real defects, or VN critical items**

3. **VK-28. 1:1 register** (Tuấn VN4).
   - Change: `modules/vn/humanize.md` L32 §CM-NATURAL 4 'tin riêng gọi số ít, không "anh/chị", không [Tên].' →
     'tin riêng gọi một người, như coach gọi khách, không [Tên].' (+11 B).
   - "một người" still rules out the slash; "như coach gọi khách" points at the coach's own chị/anh.
4. **VK-29. `multi_income` carries a true reason** (Hạnh).
   - Change: `strings/vn.toml` L271 "vì mấy thứ bạn bán, họ đều cần." → "vì {lý do}." (−33 B in §CM-SETUP 6). This
     pays for items 1, 3 and 5.
   - It also stops the overclaim for a 3-income coach (Tuấn's buyer does not buy his sales classes).
   - EN mirror, optional: `strings/en.toml` L257 "write for {buyer}, the one buyer who could buy more than one." →
     "write for {buyer}, {why}." (−36 B).
5. **K38 / VK-30. "Shorter" leaves the card top out of the count** (#6).
   - EN: `modules/en/levelup.md` L8 '"Shorter": ≤90 words of talk;' → '"Shorter": ≤90 words of talk (card top not
     counted);' (+23 B).
   - VN: `modules/vn/levelup.md` L12 '"Ngắn thôi": lời nói ≤120 tiếng,' → '"Ngắn thôi": lời nói ≤120 tiếng (trừ
     card),' (+13 B).
   - Pair it with grader G27.
6. **VK-31. "Em chạy thử".**
   - Change: `strings/vn.toml` L273 `map.ok` "Mình chạy thử 4 tuần nhé." → "Chạy thử 4 tuần nhé." (−5 chars; block
     and phone starter).
   - With no subject, the pair swap has nothing to turn into "Em".

**P3: founder calls, consistency, or one run**

7. **VK-32. Card deferral mirrors EN.**
   - Change: `modules/vn/setup.md` L28 §CM-SETUP 9 "(dài quá: card ở tin sau)" → "(app cắt: card ở tin sau)" (0 B;
     EN says "app cuts it: card next").
   - Today "dài quá" has no threshold:
     - coldstart put the card off at 1,238 words, behind "Quay video hôm nay, xong nhắn 'tiếp'…";
     - Tuấn and consultant sent about 2,500 words with the card.
   - A put-off card waits on a message the coach may only send tomorrow, in a new chat.
8. **Founder calls:**
   - (a) **Film-ready over 20 from long dictation** with an on-time cut and no extra turn (consultant 20.3): a warning,
     like "kept talking", or a failure?
   - (b) **Map + FILM TODAY + gift in one reply is 2 phone screens** (Dan 368 words → "Bro I'm on my phone.
     Shorter."; Hạnh 508; Tuấn 514). Accept it under K2, or move the gift box to Week 1?
9. **Machine slips the kit already covers (no change):**
   - coldstart's avoidable second guess (2 rounds);
   - Tuấn's DỪNG in a one-off message (2 rounds);
   - Hạnh's "chụp màn hình" backup;
   - "(em đoán)" on heard facts;
   - the "Gợi ý:" labels;
   - coldstart's N3 caption attribution.
10. **Strings for the next native pass:**
    - `setup.guess_no_result` "nên mình kể chuyện của bạn" → "nên mình kể chuyện chính bạn trải qua" (+12 B: wait
      for a VN cut).
    - `ask3.consent` (EN "Can I share your answer, first name only?") puts a second question into a one-question
      message (Dan's ask-3); all 4 VN runs simply left it out. Make it a statement, EN and VN.

### Graders (`evals/graders.py`)

- **G27. "Shorter" (L3914–3928):** leave the card-top lines (`card_parts(...).top`) out of the talk. Add
  `shorter_max_words_vn = 120` to `evals/acceptance.toml` `[day0]`, as the VN kit says (§CM-TODAY 1). coldstart T9
  then reads 75.
- **G28. I8 (L1485):** a carousel page label at the start of a line ("Trang 11:", "Slide 11:", "Page 11:") is not a
  claim. FP in consultant VN.
- **G29. I11 (L1721):** skip the card's `not_now` items. FP in Tuấn.
- **G30. Keyword outside the ask (L3863):** read FILM TODAY's caption and script too. It misses Hạnh today.

### Protocol

- **P9. A machine side that never sees the persona.**
  - Wording still leaks from undictated persona text: Dan's "3 slots of 30 minutes", "Gear:", "at once" and "every
    plan out there"; Hạnh's "chụp màn hình".
  - P13 stops edits after the fact, not this priming.
- **P10. Chunk size.** `evals/run.py` L238 (COACH.md step 2), add: "A chunk over about 400 words (VN tiếng) goes in
  two sends, split at a paragraph, as the dump prompt asks."
  - The early win is a warning in 5/5 runs, and consultant's 20.3 comes from the same cause.
- **Re-run:**
  - Hạnh, Tuấn and consultant VN after items 1–3, 5 and G27–G30;
  - one EN text-first coach (consultant EN, carousel) after K37.
