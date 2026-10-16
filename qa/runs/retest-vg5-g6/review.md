Result: FAIL

# Retest VG5 (VN ×3) + G6 (EN consultant) Day-0 after the retest-3 fix round: independent review

Reviewer: independent and bilingual (EN, plus native Vietnamese for the VN runs). I wrote neither the kit nor the runs.

Kit under test: `6e61e51` (VK-33, K39, K40/VK-34), graded with `b77820f` (G31–G38, P14/P15) and the later grader
commits `ff35c08`, `2d3c1a3`, `e15164c`. Each run's `packet/kit/` is byte-identical to the current `dist/`:
- EN: block 6,493 of 6,500 chars; method file 49,140 of 51,200 B. Run build `2f66a5750747`.
- VN: block 7,493 of 7,500 chars; method file 56,312 of 56,320 B. Run build `7156d410e57d`.

How this review was done:
- All 4 transcripts were read in full, as the coach would read them on a phone.
- Scratch copies were re-graded with the current `evals/run.py grade`. The result matches the stored `grades.json` in 4/4.
  `transcript.jsonl` equals `transcript.raw.jsonl` in 3/4. Tuấn has 2 logged leak edits (`edited: 2`). The run
  folders were not touched.
- Every failed check was traced to its transcript line and to the kit line or grader code behind it.
- Leaks were checked in 2 runs, Hạnh and Tuấn. Last round covered the two consultants. Method in §5.
- VN naturalness was scored on `qa/standards/vn-naturalness.md` (VN1–VN8). Every line I mark is quoted with a fix.

## Why FAIL

- **Grader passes: 0/4.** There are 6 failed checks: 4 real and 2 false positives (both in Tuấn).
  - Hạnh: N1's on-screen text has 7 tiếng.
  - VN consultant: the save line lost its Zalo backup. VG3 and VG4 both had it.
  - EN: the optional short's on-screen text has 7 words, and the whole card is 6,076 characters (max 5,700).
- **Tuấn's particles pass the grader only through the CTA template.** The grader reads 20% against his 38% (ratio 0.53).
  - Without the 7 ask lines his share is 13%. With a repeated sentence counted once it is 18% (0.47).
  - His spoken script lines end on a particle 9% of the time (the grader's own count).
  - N2's last line again drops his own "nha bạn".
- **A VN7 regression in Tuấn.** His long Facebook post swaps his Facebook "tui" for "mình" 15 times, including his own
  opener "Nói thiệt nè, tui bán bảo hiểm".
  - VG3 and VG4 kept "tui" 9 and 8 times.
  - The kit line "giữ y mọi bài" (XƯNG HÔ) reads as one self-reference for every platform.
- **Leaks:** Tuấn has 3 more lifts from undictated answer-bank lines. The simulator's edit pass missed them (§5). No
  number or claim leaked, so the run stays valid. It is the P9 pattern again.

**What passed (every targeted budget):**
- **Valid 4/4.** Tuấn's pace is valid this time, with 2 pasted posts in 1.2 min.
- **Map within budget in 4/4** with G31: VN 7, 6, 6; EN 6. **Film-ready ≤20 in 4/4:** 18.9, 16.1, 16.5 and EN 19.7
  (G5: 21.4).
- **Soft cut:** 4/4 on time, each one message with one "?". It **cost 0 extra turns in 4/4** (VG4/G5: 2 turns lost).
- **Multi-income right in 4/4.**
  - Asked in Hạnh and Tuấn, whose streams sell to different buyers.
  - Not asked of the VN consultant (one stream) or of Erin (K39: a sprint then a retainer is one buyer).
- **YOUR WORD outside the ask in FILM TODAY's text version: 4/4** (VG4/G5: 1/4).
- **Particles:**
  - Every VN invite ends on the coach's regional particle: "nhé", "nha", "nghe".
  - Hạnh's pieces went from 19% to 41% against her 53%. Her story lines now carry particles too.
- **1:1 register right in 3/3.** No critical VN item at 1 except Tuấn's VN7.
- **0 quits.** Every coach comes back.

## 1. The runs

The Map turn and film-ready turn are counted as G31 counts them: a coach turn that only pastes posts is left out. The
raw number is in brackets.
- "Early win" shows the clock minute of the copy box, then, after "·", the minutes counted from the dump prompt (budget ≤4).
- Verdict codes:
  - R(m): a machine slip.
  - R(kit): the kit wording caused it.
  - FP: a grader false positive.
  - W: a warning.

| Run | Lane · app | Valid | Coach turns | Map turn | Early win | Film-ready (active) | Grader failures: verdict |
|---|---|---|---|---|---|---|---|
| VN Hạnh | S1 · ChatGPT Free, Android | yes | 9 (8) | 7 (8) | 5.0 · 3.2 | 18.9 (30 min away) | I12 R(m) |
| VN Tuấn | S1 · ChatGPT Plus, iPhone | yes (2 logged leak edits; 3 lifts missed, §5) | 8 (7) | 6 (7) | 5.5 · 4.0 | 16.1 | I11 FP · I15 FP |
| VN consultant (Khoa) | S1 · Claude Pro | yes | 8 (7) | 6 (7) | 4.4 · 3.2 | 16.5 | day0_shape (save backup) R(m), kit-assisted |
| EN consultant (Erin) | S1 · Claude Free | yes | 8 (7) | 6 (7) | 5.0 · 4.6 W | 19.7 | I12 R(m) · day0_shape (card 6,076) R(kit) |

Totals:
- **Valid 4/4. Grader passes 0/4.**
- **Failed checks: 6.** 4 are real: I12 ×2, the save backup and the EN card. 2 are FP: Tuấn's I11 and I15.
  - VG4/G5 had 10 failed checks plus 1 protocol failure: 5 real, 2 R(protocol), 3 FP.
- Quits: 0. Comes back: 4/4.

| Budget (acceptance `[day0]`) | EN consultant | VN 3 runs |
|---|---|---|
| Map ≤6 coach turns (VN ≤7), posts-only turn not counted | 1/1 (6) | 3/3 (7, 6, 6) |
| Film-ready ≤20 active min | 1/1 (19.7) | 3/3 (16.1–18.9) |
| Soft cut on time (~1,200 words / tiếng) | 1/1 (1,468 at the crossing send) | 3/3 (1,319–1,397) |
| ≤10 coach turns · session ≤40 active min | 8 · 22.7 | 8–9 · 19.5–22.6 |
| Card top ≤500 / whole ≤5,700 EN, 6,600 VN | 390 / **6,076** | 372–449 / 4,886–5,736 |
| Early win ≤4 min after the dump prompt | 0/1 (4.6 W: her first send alone took 4.3) | 3/3 (3.2, 4.0, 3.2) |

## 2. Did the fixes aimed at each run work?

| Run | Fix aimed at it | Worked? | Evidence |
|---|---|---|---|
| VN all | VK-33 `cta.*` end with a particle; "cả câu mẫu" swaps it by region | **yes, 3/3** | "…chị gửi 3 bước cầm gương nói thật nhé." · "…mình gửi tờ tính ngược trước khi cọc nha." · "…tôi gửi mẫu phiếu việc 1 trang nghe." |
| VN Hạnh | particle share ≥ half her own | **yes** | 41% against her 53% (VG4: 19% against 54%). Without the asks it is 36%. Story lines carry particles: "còn khao cả spa đi ăn lẩu cơ", "khách nào cũng khen đấy", "rồi mất hút luôn" |
| VN Tuấn | particle share ≥ half his own | **grader yes, reading no** | 20% against 38% (VG4: 3%). It is 13% without the 7 ask lines and 18% with a repeated sentence counted once (0.47). Spoken lines 9%. N2's last line "Đi coi nhà mẫu thì cầm theo tờ giấy ghi con số, đừng cầm theo tiền cọc." drops his W1 "…nha bạn" (second round) |
| VN consultant | particles | n/a | His pasted posts end 0 of 14 sentences on a particle. His pieces are at 18%, with "nghe" in every ask and "đâu" in captions |
| VN all | §CM-NATURAL 4 "cả câu kể, câu mời" | **2/3** | Hạnh yes. Tuấn's long post has "Nói thiệt nè", "luôn á", but his spoken lines are flat (above) |
| VN all + EN | K40/VK-34: YOUR WORD outside the ask in FILM TODAY's text version | **yes, 4/4** | Hạnh "Em nào đang ngại chào vì sợ mình thành dọa khách thì chị hiểu lắm." · Tuấn "…góp gần 20 triệu một tháng, gồng lãi sao nổi." · Khoa "Chỗ nào đang tuyển hoài thì coi lại mấy tuần đầu…" · Erin "2019 was the agency's record year…" |
| VN all | 1:1 register as the coach addresses clients | **yes, 3/3** | Hạnh "Em ơi c nhờ e một chút nhé." (her own c/e) · Tuấn "Gửi anh chị tờ tính ngược trước khi cọc nè:" (a household) · Khoa "Chào anh, tôi Khoa." + "(khách nữ thì đổi "anh" thành "chị")" |
| VN all | Map ≤7 with the posts-only turn left out (G31) | **yes, 3/3** | 7, 6, 6 |
| VN all | film-ready ≤20 | **yes, 3/3** | 18.9, 16.1, 16.5 |
| VN Tuấn | a valid sample (pace) | **yes** | Two pasted posts took 1.2 min, against a minimum of 1.0 (P14) |
| VN Tuấn | `multi_income` only if his streams sell to different buyers | **yes** | His streams are insurance and brokerage, sold to young families, and sales training, sold to sàn and đại lý. T6, one "?": "…cùng một nhà mua được cả căn qua anh lẫn hợp đồng bảo hiểm… Đúng không?" He answered "Đúng rồi em" |
| VN Hạnh | `multi_income` | **yes** | Spa clients and spa owners are different buyers. She corrected "2 nguồn" to 3. The spa and the cosmetics went into `side_door` |
| EN | K39: no multi-income question for one buyer | **yes** | T7 she typed the Margin Sprint and the "$3,500 a month" retainer. The next reply was the Map (G5: an extra "You earn from 2 things…" turn) |
| EN | Map ≤6, film-ready ≤20 | **yes** | Map at coach turn 6, film-ready at 19.7 (G5: 8 and 21.4) |
| EN | K37: keyword in a carousel's or long post's opening | **yes** | PDF "Slide 1: Record year. Empty account. 7 steps to find the client." · the email's subject 1 and first line. The Wed post opens without it, which the rotation allows |
| all | founder warning rules | **held** | No film-ready over 20, so no warning was needed. EN's early win at 4.6 is a warning, not a failure, because her first send alone took 4.3 (G32) |
| VN consultant | save line with route + backup | **regressed** | "…chọn Add text content, dán vào, bấm Save." and nothing more (VG3, VG4: "…Dự phòng: gửi vào Zalo "Cloud của tôi"") |
| VN Tuấn | his voice in the Facebook post | **regressed** | "Nói thiệt nè, mình bán bảo hiểm…", "Mình hổng cãi, mình cười…". His W2: "Nói thiệt nè, tui bán bảo hiểm"; T6: "Tui hổng cãi, tui cười" |

## 3. The founder's Day-0 rules in practice

| Run | Early-win copy box | Arrived · postable as is? | Soft cut | One message, one "?" · cost | Facts up front / guessed visibly |
|---|---|---|---|---|---|
| VN Hạnh | "Năm 2024 chị vào một cái nhóm chủ spa trên phây, có một em hỏi là sao em chào thẻ khách toàn từ chối. Thế là chị ngồi gõ một cái comment dài ơi là dài, tối hôm đấy inbox chị nổ tung luôn." | 5.0 · **yes**: a two-line story that stands alone; the mic's "trào" was fixed to "chào" | T7, at the crossing send. The same message answers her "ra tiếp khách" with "chị cứ ra với khách đi, không vội đâu" and carries the buyer guess | yes · 0 turns (her answer came when she returned) | No VP-2 sentence in her script. FB, "chưa có" list and thứ Hai were guessed in one tagged line. Her price was never heard; the card says "giá: chưa nghe" |
| VN Tuấn | "Tui nói chị ra khỏi toilet đi, cảm ơn bạn sale, nói về hỏi chồng, mai mình ngồi tính rồi hẵng cọc." | 5.5 · **partly** (second round): it needs the toilet scene first | T6, with the buyer guess | yes · 0 | VP-2 heard TikTok, FB, Zalo 1.850 and no email, but the plan line tags them "(em đoán…)". The unit's rooms and area were unheard, so N3 carries one "Cần anh" line |
| VN Khoa | "Người ta không có nghỉ sau Tết đâu, người ta quyết định nghỉ từ mấy tuần đầu mới vô rồi, Tết chỉ là cái cớ để đi thôi." | 4.4 · **yes** | T6, with the offer guess. TIẾP "có giá thì ghi luôn" brought the price (45.000.000đ) without a second question | yes · 0 (VG4: +1) | VP-2 heard LinkedIn, FB, Zalo 380 and email 250. The plan line again tags the heard lists as guesses |
| EN Erin | "Your biggest client is not your best client until you've done the math." | 5.0 · **yes** | T6, with the offer guess | yes · 0 (G5: +1) | VP-2 heard LinkedIn and the list of 380. "(talk day is my guess; one word changes it)" is scoped right |

Findings:
- **Early win: 4/4 in a copy box on the first send, 3/4 postable as is** (VG4: 2/4).
  - Tuấn's line needs one clause of context for the second round running. §CM-SETUP 2 asks that "câu vào khung đứng
    riêng thành bài được".
- **Soft cut: 4/4.** Each came at the crossing send, as one message with one "?", and cost no turn.
  - The consultant machine pulled the price through TIẾP rather than a second question. That pattern is worth keeping.
- **Facts up front:**
  - The dump prompt asks for platforms and lists in 4/4.
  - The talk day was guessed as Monday in 4/4. The kit gives no basis for the guess, but it is shown once and changeable.
  - VN `setup.plan_guess` still tags heard facts as guesses in 2/3 (VK-35, carried over).
- **Map reply length:** about two phone screens in 4/4, accepted under DECISIONS.
  - The Week-1 reply runs about 2,400–2,600 tiếng / 2,363 words, mostly copy boxes, as §CM-SETUP 9 requires.
  - It is the main "comes back" risk each simulator names.

## 4. Failed grader checks: real or false positive

| # | Run · check | Transcript line | Kit line or grader code | Verdict |
|---|---|---|---|---|
| 1 | Hạnh · I12 | N1 "Chữ trên màn hình: Ngại chào vì sợ như đi lừa" (7 tiếng). FILM TODAY's "41 thẻ, 27 khách bỏ dở" was 6 | block step 6 and §CM-FORMATS 1 "chữ trên màn hình ≤6 tiếng" | **R(m)** |
| 2 | Tuấn · I11 "sinh lời" | FB post "Ai hỏi tích lũy với sinh lời là mình nói thẳng: cái đó không phải chỗ để kiếm lời." It is his own refusal from T6, re-voiced | `i11_injection` (graders.py L1857–1878) tests only `NEGATED_BEFORE_RE` (L1810) before the match; `expected.toml` `compliance` lists bare "sinh lời" | **FP** |
| 3 | Tuấn · I15 "chị" | T6 "…như nhà chị dạy mầm non với nhà anh khách gãy chân." "chị" is a client household, third person; em–anh holds to him | `i15_vn_language` L2161: the before-word list `các|những|mấy|của|tự|kết|tiếng|nước` lacks "nhà" | **FP** |
| 4 | Khoa · day0_shape save backup | T8 "Lưu lại để em nhớ anh (30 giây): chép card, bấm + cạnh mục file của project, chọn Add text content, dán vào, bấm Save." | Block BRAND CARD "Dự phòng: gửi vào Zalo "Cloud của tôi"." against `modules/vn/brain.md` §CM-CARD 5, which quotes `save.claude_plain` with no backup, and §CM-CARD 1 "Coach chỉ thấy dòng lưu (ngày 0, bước 8)." EN §CM-CARD 1 says "+ the app's route and backup". `6e61e51` also shortened `save.claude_plain` | **R(m), kit-assisted.** The machine copied §CM-CARD 5 word for word |
| 5 | EN · I12 | Optional short "On-screen: The bank app is not a forecast" (7 words) | block step 5 and §CM-FORMATS 1 "on-screen text ≤6 words" | **R(m).** The second EN I12 in a row, both in the Week-1 optional short (G5: a 13-word first line) |
| 6 | EN · day0_shape whole card 6,076 | Top 390 + box 5,685. The machine trimmed the box alone to 5,700 | `modules/en/brain.md` L16 "Over 5,700: trim liked, then passages…" sits in the machine-box paragraph; `platform/targets.toml` `[budgets.brand_card]` is "Brand Card (whole)" | **R(kit)** (G5: 5,881) |

Grader misses:
- **EN FILM TODAY's text-version item did not run** (G36). Erin's caption box has no "Caption" label, so
  `film_text_version` (L4068) returns None. The box does carry RECORD YEAR outside the ask, so the verdict would not
  change.
- **`vn_natural` counts a repeated sentence every time.** Tuấn's "Nhắn mình chữ GỒNG LÃI, … nha." is printed 3 times word for word (7 ask lines in all), and the run passes on them
  (above).
- **The leak check misses short lifts of undictated answer-bank lines.** VN `LEAK_N` = 8 tiếng (run.py L517). Tuấn's 3
  lifts are 5–7 tiếng (§5).
- **`acceptance.toml` `session_max_turns = 10`, but the VN block says "coach nhắn ≤11 lượt".** No run came near it.

## 5. Leak spot-check (Hạnh, Tuấn)

**Method:**
- For every machine turn, I listed each 5-gram (tiếng, case-folded) that is also in one of the persona files:
  `persona.toml`, `answers.md`, `expected.toml`, `voice-samples.md`, `launch-brief.toml`, `pillar-transcript.md`,
  `paste-dump.md`, `written-posts.md`, `research-paste.md` or `liked-paste.md`.
- I removed 5-grams of the coach's turns so far and of the kit, then merged the rest into runs.
- I listed every number the coach had not said.
- I searched for each fact that only the answer bank holds.
- I read each hit against the transcript.

**Hạnh: clean.**
- 63 runs. All join her words: "lớp kèm chủ spa nhỏ 6 tuần" comes from "Học xong 6 tuần" and "khóa 1"; "tháng
  7/2026" comes from "tháng 7 vừa rồi".
- New numbers are dates, durations and the pack version.
- The answer-bank-only facts appear 0 times: the price, 6 suất, 21h, Zalo 3.200/240, TikTok, Loan, cô Hoa, Vân and
  "no computer". The card says "giá: chưa nghe" instead of a price.

**Tuấn: valid. The 2 logged edits were right, but 3 lifts from undictated `answers.md` lines were missed.**

| Machine text | Persona source | What he said |
|---|---|---|
| Map line 1 "…che cho khoản vay rồi mới đi coi nhà"; the gift's "Căn nào quá số đó thì khỏi đi coi." | `answers.md` L37 (chunk 2, never dictated) "ra giá căn tối đa, rồi mới đi coi nhà" | "mai mình ngồi tính rồi hẵng cọc": before the deposit, not before viewing |
| Zalo "nhà nào muốn coi thì mình ngồi tính trước rồi mới dẫn đi"; N3 "Trước khi dẫn đi coi, mình hỏi lương bạn trước." | `answers.md` L75 "Tại tui ngồi tính trước rồi mới dẫn đi coi nhà" (never asked) | nothing about the order of viewing |
| card `offer` "Tuấn sống bằng hoa hồng khi nhà đó mua căn hay tham gia bảo hiểm qua anh" | `answers.md` L66 "Tui sống bằng hoa hồng: nhà nào mua căn qua tui … nhà nào tham gia bảo hiểm với tui…" | "tui có nhận hoa hồng" (W2) |

- No unsaid number appears.
  - The 68 triệu payout stays out, as the client asked.
  - The 2 tỷ 68 unit's details were asked through a "Cần anh" line, not filled in.
  - "view sông" appears 0 times.
- **Verdict: valid.** The three lifts add no claim, number or name, and all are consistent with what he said. Still,
  the viewing order and "sống bằng hoa hồng" are small undictated facts.
  - The protocol's 8-tiếng scan did not list them.
  - The simulator's notes call every remaining warning a rebuild.
  - P9, a machine side that never sees the persona, remains the real fix (P17 below).

## 6. VN naturalness (VN1–VN8)

Bars, from `qa/standards/vn-naturalness.md`:
- **Pieces:** VN3, VN4, VN6 and VN7 at 2; total ≥13/16.
- **Coach-facing prose and Map lines:** VN3, VN4 and VN6 at 2; total ≥10/12.

Regions: Bắc (Hạnh), Nam (Tuấn), Trung/Quảng (Khoa).

| Run | Coach-facing /12 | Map lines /12 | QUAY HÔM NAY /16 | Week-1 posts /16 | Zalo + inbox (+ email) /16 |
|---|---|---|---|---|---|
| Hạnh | 11 ✓ (VN1 1: "Brand Card", "Lưu vào dự án") | 11 ✓ (VN2 1: line 1 runs method, old way, result and "như Thảo") | 16 ✓ | 15 ✓ (VN2 1: N1 on-screen) | 15 ✓ (VN1 1: "muốn dùng đúng lời của các em") |
| Tuấn | 10 ✓ (VN1 1; VN5 1: "Em nhận rồi." ×4 with no "Dạ", a bare "Đúng không?") | 11 ✓ (VN2 1: methods stacked, fourth round) | 15 ✓ (VN5 1: spoken lines flat) | **14 ✗ (VN7 1, critical**: the FB post's "mình" for his FB "tui"; VN5 1) | 14 ✓ (VN8 1: title line + DỪNG in the Zalo, both kit lines; VN1 1) |
| Khoa | 11 ✓ (VN1 1: "Add text content") | 11 ✓ (VN2 1: "3 bước: phiếu việc…, làm thử…, kèm…" in line 1, both prints) | 16 ✓ | 16 ✓ | 15 ✓ (VN1 1: ask-3 "dùng đúng lời", no greeting) |

- **14/15 columns pass.** Tuấn's Week-1 posts fail on VN7, a regression; last round every column passed.
- 0 essay connectors and 0 banned tells. `vn_natural` found 0 translationese patterns in 3/3.
- The machine fixed two mic slips silently and right: Khoa's "dứa" → "Rứa", Hạnh's "trào thẻ" → "chào thẻ".

Lines that still read translated or stiff (D = translated, S = stiff), with a natural version:
1. **VN7 · Tuấn's Facebook post** (regression).
   - "Nói thiệt nè, mình bán bảo hiểm, mà mình hiểu sao nhiều người nghe tới là né." → "Nói thiệt nè, tui bán bảo
     hiểm, mà tui hiểu sao nhiều người nghe tới là né."
   - The same fix throughout: "Tui hổng cãi, tui cười, gắp cho ổng thêm miếng nữa." (his T6).
2. **VN5 · Tuấn's spoken lines** drop his particles.
   - N2 last line: "…đừng cầm theo tiền cọc." → "…đừng cầm theo tiền cọc nha bạn." (his W1, word for word).
   - Inbox 2: "Chưa cần thì nói mình." → "Chưa cần thì nói mình một tiếng nha."
3. **D · `research.ask3`, 3/3 runs.**
   - "…muốn dùng đúng lời của {anh | anh chị | các em}." → "…muốn lấy đúng câu {anh} hay nói."
   - Khoa's and Tuấn's open with no greeting. Fix: "Anh ơi, Khoa đây. Nhờ anh một chút: …"
4. **S · labels before the joggers**, 7 times in 3/3 runs (fourth round).
   - Hạnh "Gợi ý: chị gỡ cho Thảo thế nào, rồi Thảo đổi khác ra sao sau khi học chị." → "Chị kể tiếp đoạn chị gỡ
     cho Thảo nhé, rồi Thảo khác đi thế nào."
   - Tuấn "Gợi ý cho đoạn sau: phần bảo hiểm dính gì tới chuyện mua nhà, anh kể một nhà thật." → "Đoạn sau anh kể em
     nghe bên bảo hiểm nha, một nhà thật."
5. **S · the plan line (Tuấn, Khoa).**
   - "…danh sách Zalo, email: Zalo 1.850 người, email chưa có · … (em đoán, gõ một chữ là đổi)." → "Viết cho TikTok ·
     Zalo chừng 1.850 người, chưa có email · thứ Hai hằng tuần kể 15 phút (ngày này em đoán, anh gõ một chữ là đổi)."
6. **S · the keyword tag on the Map (Hạnh, Tuấn).**
   - "TỪ KHOÁ: NGẠI CHÀO (không dấu: NGAI CHAO) · từ câu các em hay than, em đoán, tuần đầu kiểm lại" →
     "TỪ KHOÁ: NGẠI CHÀO (không dấu: NGAI CHAO)".
   - Khoa's Map, with four owners quoted, printed no tag. The kit's rule ("Không lấy: câu coach … nhớ lại") makes every
     Day-0 keyword a guess (founder call below).
7. **S (brochure) · Tuấn's Map line 1, fourth round.**
   - "…tính ngược tiền góp bằng lãi thả nổi, chừa quỹ 6 tháng, che cho khoản vay rồi mới đi coi nhà, chứ không cọc rồi
     mới về tính, biết trước căn nào trả nổi." → "Vợ chồng trẻ nào hay than "sợ gồng lãi không nổi" thì tìm Tuấn: tính
     ngược ra căn trả nổi rồi mới cọc, chứ không cọc rồi mới về tính."
8. **S · coach-facing lines.**
   - Tuấn "Em nhận rồi." → "Dạ, em nhận rồi."
   - Tuấn T6 "Đúng không?" → "Đúng không anh?"
   - Khoa T8 "Bài vẫn nói với đúng một kiểu khách" → "Bài vẫn nhắm đúng một kiểu khách".
9. **S · Hạnh's N1 on-screen** (also I12): "Ngại chào vì sợ như đi lừa" → "Chào thẻ mà thấy như lừa" (6 tiếng).
10. **S (call centre) · Tuấn's Zalo** (§CM-MESSAGES 3, fourth round): "Không muốn nhận nữa thì nhắn mình chữ DỪNG." →
    "Chưa cần mấy tin này thì nói mình một tiếng nha."

Keep these; they read like a person:
- Hạnh T7 "Dạ được chị, chị cứ ra với khách đi, không vội đâu."
- Hạnh's long post "Chào thì vẫn phải chào chứ, mà chào bằng nói thật thôi."
- Hạnh N3 "Đường thứ hai chị đi rồi, năm 2018, nên chị không dạy các em đi lại đâu."
- Hạnh's inbox 1 "Em đang có spa riêng rồi, hay em hỏi cho da của em?"
- Tuấn's caption "Nhà mẫu đẹp dữ lắm: rèm trắng, đèn vàng, bàn ăn bày sẵn bốn cái ly rượu vang."
- Tuấn N2 "Chiều nay cọc mới được chiết khấu, qua mai là hết: nghe quen hông?"
- Tuấn N3 "Gồng lãi không nổi thì đẹp cỡ nào cũng hổng phải căn của bạn."
- Tuấn T8 "Dạ, từ giờ em không xin comment nữa, chỉ mời nhắn riêng."
- Khoa's N3 caption "Họ giỏi nghề của họ. Có ai dạy họ tuyển người đâu."
- Khoa's inbox 2 "Chưa cần thì anh nói tôi nghe, tôi gửi anh phần 2: bài làm thử 2 tiếng việc thật."
- Khoa T6 "Còn chuyện nào thì anh kể luôn, không thì em đoán: …"

## 7. What improved vs the previous round (same personas)

| Measure | VG4 / G5 | VG5 / G6 |
|---|---|---|
| Valid | 3/4 (Tuấn: pace) | **4/4** |
| Grader passes | 0/4 | 0/4 |
| Failed checks: real / R(protocol) / FP | 10 + 1 protocol: 5 / 2 / 3 | **6: 4 / 0 / 2** |
| Map coach turn (G31 count) | 7, 6, 7 · 7 ✗ | **7, 6, 6 · 6** |
| Film-ready, active | 18.9, 16.0, 17.4 · 21.4 ✗ | 18.9, 16.1, 16.5 · **19.7** |
| Early win, minutes after the dump prompt | 3.2, 4.3, 3.4 · 4.9 | 3.2, **4.0**, 3.2 · 4.6 W |
| Early win postable as is | 2/4 | **3/4** |
| Extra turns from the cut's questions | 2 | **0** |
| YOUR WORD outside the ask in FILM TODAY's text | 1/4 | **4/4** |
| Multi-income handled right | 3/4 (EN asked needlessly) | **4/4** |
| Particle share vs their posts (grader) | Hạnh 19% (54), Tuấn 3% (38) | **41% (53), 20% (38)** |
| VN critical items at 1 | none | Tuấn VN7 (FB "tui" → "mình") ✗ |
| Save line route + backup | 4/4 | 3/4 (Khoa lost the backup) ✗ |
| EN whole card | 5,881 ✗ | 6,076 ✗ |
| I12 | EN (13-word first line) | EN + Hạnh (7-word on-screen) ✗ |
| Leaks found in the spot-check | 3 identical compressions of dictated facts (EN) | 3 lifts of undictated lines (Tuấn) |

## 8. Prioritised fix list

Budgets now:
- EN block 6,493/6,500; EN method 49,140/51,200 B; EN §CM-CARD 2,787/2,800 B (my count).
- VN block 7,493/7,500; VN method 56,312/56,320 B.

After items 1–6:
- **EN method 49,151** (49,159 with item 3's optional line). EN §CM-CARD 2,798.
- **VN method 56,315/56,320** (−52 +38 +11 −13 +16 −1 +4 = +3).
- **VN block 7,496.** VN Phone Starter 7,276/7,500. The EN block is unchanged.
- Refresh the src hashes. Re-run the cases that quote `save.claude_plain`, `setup.plan_guess` or `research.ask3`.

### Kit

**P1: blocks acceptance**

1. **VK-36. The VN save line keeps its backup** (#4, a regression).
   - `strings/vn.toml` L134 `save.claude_plain`: append " Dự phòng: Zalo "Cloud của tôi"." (+38 B, §CM-CARD 5).
   - **Cut:** `modules/vn/brain.md` L15 §CM-CARD 1, drop " Coach chỉ thấy dòng lưu (ngày 0, bước 8)." (−52 B).
     - The sentence contradicts the block's BRAND CARD, which shows the card top.
     - Block step 8 already holds the save line.
2. **K41. EN whole-card budget** (#6; over budget two rounds running).
   - `modules/en/brain.md` L16 §CM-CARD 3: "Over 5,700:" → "Whole card over 5,700:" (+11 B; fits, no cut).
   - The VN cards are within 6,600 (4,886–5,736), so VN is unchanged.
3. **I12 (#1, #5).**
   - VN: no change. The rule sits in block step 6 and in §CM-FORMATS 1, and FILM TODAY was right in 3/3.
   - EN, optional, after two rounds of the same slip: `modules/en/fmt-short.md` L6 §CM-FORMATS 1 "on-screen text ≤6
     words" → "on-screen text ≤6 words (count)" (+8 B; fits).

**P2: real defects, graded weakly or not at all**

4. **VK-37. The coach's self-reference per platform** (Tuấn's VN7 regression).
   - `core/vn/start-block.md` L27 XƯNG HÔ: "suy từ lời họ, giữ y mọi bài." → "suy từ lời họ, giữ y như bài họ."
   - Cost: +3 chars, VN block 7,496/7,500; it fits, no cut. The Phone Starter carries it too.
5. **VK-38. Particles in spoken lines too** (Tuấn's spoken lines 9%; his "nha bạn" dropped two rounds running).
   - `modules/vn/humanize.md` L32 §CM-NATURAL 4: "…, cả câu kể, câu mời." → "…, cả câu kể, câu mời, câu nói." (+11 B).
   - **Cut:** `modules/vn/setup.md` L16 §CM-SETUP 3, "Không bắt tải, đính kèm, cài đặt, đổi máy" → "Không bắt tải, cài
     đặt, đổi máy" (−13 B). "tải" covers it, and EN has no "attach".

**P3: one run, wording, carried over**

6. **Native-pass strings, all in `strings/vn.toml` and the method file, fitting the totals above:**
   - **VK-35** `setup.plan_guess` (L272): "(mình đoán, gõ một chữ là đổi)" → "({chỗ đoán}: mình đoán, gõ một chữ là đổi)".
     - +16 B. It is the second round that heard lists were tagged as guesses.
   - `research.ask3` (L224): "muốn dùng đúng lời của bạn" → "muốn lấy đúng câu của bạn" (−1 B; D in 3/3).
   - §CM-MESSAGES 3 (`modules/vn/fmt-short.md` L45): "Không muốn nhận nữa thì nhắn mình chữ DỪNG." → "Chưa cần mấy
     tin này thì nói mình một tiếng nhé." (+4 B).
7. **Left for room (no change now):**
   - Tuấn's early win needing context. §CM-SETUP 2 "(1–2 câu)" would cost +13 B with no cut left.
   - The "Gợi ý:" labels, which the block's own dump prompt models.
   - "Đúng không?" with no vocative. The block step 4 template would cost +4 chars, which would fill the block to 7,500.

### Graders (`evals/graders.py` unless noted)

- **G39.** `i11_injection` L1857–1878: a banned phrase in a sentence that carries a negation ("không phải", "đừng",
  "chứ không") and is ≥60% the coach's own words is their refusal, not a claim. Tuấn's "sinh lời" FP.
- **G40.** `i15_vn_language` L2161: add "nhà" to the before-word list ("nhà chị dạy mầm non" is a household).
  Tuấn's "chị" FP.
- **G41.** `film_text_version` L4068: when no caption label is found, take the first copy box after the script's last
  line. Erin's item did not run.
- **G42.** `particle_share` L2991: count an identical sentence once, as G37 does for boxes. Tuấn would read 18% against
  38% and fail. That matches the native reading (VN5 = 1). Regress the older VN runs first.
- **G43.** `evals/acceptance.toml` L35: add `session_max_turns_vn = 11` to match the block's "≤11 lượt" (VN adds the
  xưng hô turn, as `map_max_turns_vn` does). Alternatively, set the block to ≤10.

### Protocol

- **P16.** `evals/run.py` COACH.md step 2 (P10 split): chunk 1's first send ends at ≤300 words / tiếng (about 3 min),
  as the dump prompt says "every 2–3 minutes". Erin's 425-word first chunk took 4.3 min and turned the early win into a
  warning.
- **P17.** `evals/run.py` `check_leaks` (L711; `LEAK_N` L517): add a warning tier at 5 tiếng / words for `answers.md`
  paragraphs no coach turn covered (the POST_RUN coverage test). It catches Tuấn's 3 lifts without the noise of
  dictated lines. P9 stays the real fix.
- **Re-run** all four after items 1–5 and G39–G42.
  - Tuấn for VK-37/38.
  - Khoa for VK-36.
  - EN for K41.
  - Hạnh as the I12 re-sample.

### Founder call

- **(a) The keyword tag on Day 0.** §CM-MAP TỪ KHOÁ excludes "câu coach … nhớ lại", so every Day-0 keyword prints
  "(mình đoán, Tuần 1 kiểm lại)" / "(my guess)" on the one decision screen. Two runs did this.
  - Recommendation: a buyer phrase the coach quotes from ≥3 named clients counts as heard. Khoa's machine already read
    it that way.
  - Cost: 0 B. `modules/vn/signature.md` L8 "câu coach nói hay nhớ lại" → "câu của chính coach" saves 8 B. EN "never
    the coach's line or recall" → "never the coach's own line".
