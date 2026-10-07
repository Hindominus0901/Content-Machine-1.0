Result: FAIL

# Retest VG6 (VN ×3) + G7 (EN consultant) Day-0 after the retest-4 fix round: independent review

Reviewer: independent and bilingual (EN, plus native Vietnamese for the VN runs). I wrote neither the kit nor the runs.

Kit under test: `e525244` (VK-35..38, K41, I12 "(count)") and `eab8d0a` (founder call a: a client phrase the coach
quotes from 3+ named clients counts as heard), with the cases of `7e4dea5`. Graded with `de5f122` (G39–G43, P16/P17).
Each run's `packet/kit/` is byte-identical to `dist/`, and a clean build of HEAD `7e4dea5` in a scratch worktree
reproduces `dist/` byte for byte:
- EN: block 6,493 of 6,500 chars; method file 49,171 of 51,200 B; §CM-MAP 2,798 of 2,800 B. Run build `e61e0c9a8a0a`.
- VN: block 7,496 of 7,500 chars; method file 56,319 of 56,320 B. Run build `edd1a11e0770`.

How this review was done:
- All 4 transcripts were read in full, as the coach would read them on a phone.
- Scratch copies were re-graded with the current `evals/run.py grade`: identical `grades.json` in 4/4.
  `transcript.jsonl` equals `transcript.raw.jsonl` in 4/4 and `edited` is 0 in 4/4. The run folders were not touched.
- Every failed check was traced to its transcript line and to the kit line or grader code behind it. The VN particle
  counts were re-listed sentence by sentence with the grader's own functions (`particle_share`, `split_script`).
- Leaks were checked in Tuấn (the run with lifts last round, and P17's target) and Khoa (not checked last round). §5.
- VN naturalness was scored on `qa/standards/vn-naturalness.md` (VN1–VN8). Every line I mark is quoted with a fix.

## Why FAIL

- **Grader passes: 2/4** (Khoa, Erin). 4 failed checks: **2 real** (`vn_natural` in Hạnh and Tuấn), **2 false
  positives** (Tuấn's I15 and `vn_messages`).
- **The new keyword rule was over-applied: 0/4 Day-0 keywords carry the guess tag.** In all four dumps the keyword comes
  from one identified client plus "they all say it", the case DECISIONS (7 Oct) keeps as "(my guess)".
  - Hạnh and Tuấn are clear misses. `evals/cases/signature.vn.toml` (case .025, rewritten in `7e4dea5`) names Hạnh's
    exact dump as "one named client plus 'many say it' … stays a guess".
  - Khoa and Erin turn on one word: their dumps add 2–3 anonymous example lines ("record year and I can't sleep").
    Read as DECISIONS words it, they are guesses too. The VG5 review counted Khoa's four lines as four owners.
  - VG5/G6 tagged 3 of 4. No grader checks the tag.
- **VN particles in written pieces fell in both coaches who write with them.** Hạnh 39% → 15% (hers 54%, min 27%),
  Tuấn 18% → 14% (his 38%, min 19%), on kit text that changed only by "câu nói". Spoken lines improved (Tuấn 0% → 38%).
- **A VN4 slip in Tuấn's ask-3 message** (critical item): "Nhờ chị một chút: em đang viết lại…" to old clients, with
  "đổi chị/anh cho đúng người". The one client he described calls him "anh Tuấn" and herself "em", so the self pronoun
  is wrong too, and the swap note does not cover it.

**What passed (every targeted fix landed):**
- **Valid 4/4, 0 edits, 0 quits.** Every coach comes back.
- **Khoa's save line has its Zalo backup again** (VK-36). **EN whole card 5,647 ≤ 5,700** (K41; G6 6,076).
- **On-screen text ≤6 words / tiếng in 14/14 scripts** (I12 clean in 4/4; Hạnh's re-sample clean).
- **Tuấn's voice per platform** (VK-37): "tui" ×12 in his Facebook post and ×8 in the Bán kèm post, "mình – bạn" on
  TikTok, "Tuấn đây" on Zalo. VG5 had "mình" ×15 on Facebook.
- **Tuấn's spoken lines** (VK-38): 3/8 end on a particle (38%, his 38%; VG5 0/9). His W1 "…đừng cầm theo tiền cọc nha
  bạn" is back word for word.
- **P16:** first sends 232, 306, 293 and 305 words / tiếng. The EN early win came 3.6 min after the dump prompt (G6:
  4.6, a warning).
- **Every Day-0 budget held in 4/4:**
  - Map at 7, 6, 6 · 6.
  - Film-ready at 19.8, 15.9, 16.9 · 17.1.
  - Soft cut: one message, one "?", 0 extra turns.
  - Early win 2.9–3.6 min after the dump prompt.
- **The VN plan line tags only unheard facts** (VK-35, 3/3). `research.ask3` "lấy đúng câu" landed in 3/3.
- **Leaks:** Khoa clean. Tuấn is valid but repeats the same 3 undictated lifts as VG5 (§5).

## 1. The runs

The Map turn and film-ready turn are counted as G31 counts them: a coach turn that only pastes posts is left out. The
raw number is in brackets.
- "Early win" shows the clock minute of the copy box, then, after "·", the minutes counted from the dump prompt (budget ≤4).
- Verdict codes:
  - R(m): a machine slip.
  - R(kit): the kit wording caused it.
  - FP: a grader false positive.

| Run | Lane · app | Valid | Coach turns | Map turn | Early win | Film-ready (active) | Grader failures: verdict |
|---|---|---|---|---|---|---|---|
| VN Hạnh | S1 · ChatGPT Free, Android | yes (0 edits) | 9 (8) | 7 (8) | 4.8 · 2.9 | 19.8 (30 min away) | vn_natural R(m), kit-assisted |
| VN Tuấn | S1 · ChatGPT Plus, iPhone | yes (0 edits; 3 undictated lifts, §5) | 8 (7) | 6 (7) | 4.6 · 3.3 | 15.9 | I15 FP · vn_natural R(m) · vn_messages FP |
| VN consultant (Khoa) | S1 · Claude Pro | yes | 8 (7) | 6 (7) | 4.5 · 3.3 | 16.9 | none |
| EN consultant (Erin) | S1 · Claude Free | yes (300 min away at the plan limit) | 8 (7) | 6 (7) | 4.0 · 3.6 | 17.1 | none |

Totals:
- **Valid 4/4. Grader passes 2/4** (VG5/G6: 0/4).
- **Failed checks: 4.** 2 are real: Hạnh's and Tuấn's `vn_natural`. 2 are FP: Tuấn's I15 and `vn_messages`.
  - VG5/G6 had 6: 4 real, 2 FP.
- Not graded, and real: the untagged keyword in 4/4 (§2).
- Quits: 0. Comes back: 4/4.

| Budget (acceptance `[day0]`) | EN consultant | VN 3 runs |
|---|---|---|
| Map ≤6 coach turns (VN ≤7), posts-only turn not counted | 1/1 (6) | 3/3 (7, 6, 6) |
| Film-ready ≤20 active min | 1/1 (17.1) | 3/3 (15.9–19.8; Hạnh 0.2 under) |
| Soft cut on time (~1,200 words / tiếng) | 1/1 (1,331 at the crossing send) | 3/3 (1,246–1,306) |
| ≤10 coach turns (VN ≤11) · session ≤40 active min | 8 · 19.2 | 8–9 · 19.1–23.2 |
| Card top ≤500 / whole ≤5,700 EN, 6,600 VN | 436 / 5,647 | 344–414 / 4,769–5,155 |
| Early win ≤4 min after the dump prompt | 1/1 (3.6) | 3/3 (2.9, 3.3, 3.3) |
| P16 first send ≤ about 300 | 305 | 232, 306, 293 |
| On-screen text ≤6 words / tiếng | 2/2 | 12/12 |

## 2. Did the fixes aimed at each run work?

| Run | Fix aimed at it | Worked? | Evidence |
|---|---|---|---|
| VN Khoa | VK-36: save line with route and Zalo backup | **yes** | T8 "Lưu lại để em nhớ anh (30 giây). Chép card, bấm + cạnh mục file của project, chọn Add text content, dán vào, bấm Save. Dự phòng: Zalo "Cloud của tôi"." Hạnh and Tuấn (ChatGPT): "bấm ⋯ dưới card → Lưu vào dự án. Dự phòng: gửi vào Zalo "Cloud của tôi"." |
| EN | K41: the whole card ≤5,700 | **yes** | Top 436 + box 5,210 = 5,647 (G6 6,076, G5 5,881) |
| all | I12 "≤6 words (count)" / "≤6 tiếng (đếm)" | **yes, 14/14** | EN "Record year. Empty account." (4), "Your P&L is 6 weeks late" (6). Hạnh "Khách không sợ giá", "Chào thẻ, khách toàn từ chối", "Để chị về suy nghĩ", "Bước các em hay bỏ" (4, 6, 5, 5). Tuấn 5, 6, 5, 6. Khoa "Tuyển 15 phút, ở 15 ngày" (6), 4, 6, 4 |
| VN Hạnh | a clean I12 re-sample | **yes** | Above. VG5's 7-tiếng N1 did not recur |
| VN Tuấn | VK-37: his own self-reference per platform ("tui" on Facebook) | **yes** | Facebook post "Sợ gồng lãi mà vẫn suýt cọc, chuyện này tui gặp hoài." · "Nói thiệt nè, tui làm môi giới, tui có nhận hoa hồng." The one "mình" in it is his inclusive "mai mình ngồi tính". The card keeps both: "mình – bạn (video) · tui (Facebook)" |
| VN Tuấn | VK-38: particles in spoken lines | **yes** | 3/8 spoken lines end on a particle (38%, his 38%; VG5 0/9). FILM TODAY "Đi coi nhà mẫu thì cầm theo tờ giấy ghi con số, đừng cầm theo tiền cọc nha bạn." · N1 "Dí cỡ nào thì cũng tính trước rồi hẵng cọc nha bạn." |
| VN Tuấn | particles as dense as his posts, a repeated sentence counted once (G42) | **no** | Written pieces 9/64 (14%) against a minimum of 19% (VG5 10/57, 18%). His Facebook post ends 1 of 19 sentences on a particle, and that one is the client's quoted "…hả anh" |
| VN Hạnh | (none aimed; carried) particles | **regressed** | 9/60 (15%) against her 54% (VG5 28/72, 39%). Her long post ends 2 of 19 on a particle |
| all | Day-0 keyword: no tag when quoted from 3+ named clients, tagged when not | **no: 0/4 tagged** | Table below |
| all | P16: the first send ≤300 | **yes** | 232, 306, 293, 305. EN early win 3.6 (G6 4.6 W) |
| VN all | VK-35: plan line "(chưa nghe thì mình đoán, …)" | **yes, 3/3** | Khoa "…danh sách Zalo, email: Zalo 380 người, email 250 người (chưa nghe thì em đoán, gõ một chữ là đổi)." Tuấn the same with "Zalo 1.850 người, email chưa có" |
| EN | plan line (no change made) | **regressed** | "For LinkedIn · talk day Monday · email list: 380 (my guess; one word changes it)." She said 380. G6's machine scoped it ("talk day is my guess"); the EN string never got VK-35 |
| VN all | `research.ask3` "lấy đúng câu" | **yes, 3/3**; greeting 2/3 | Khoa "Chào anh, tôi Khoa đây. Nhờ anh một chút: … muốn lấy đúng câu của anh." Hạnh "Em ơi, nhờ em một chút: …". Tuấn opens with no greeting (§6) |
| all | Map, film-ready, soft cut, early win budgets | **held, 4/4** | §1 |

**The keyword tag, run by run.** The rule in the kit: "3+ named clients the coach quotes" / "coach kể ≥3 khách có tên".
DECISIONS: "Fewer than 3 named clients (one client plus 'lots of people say it') stays '(my guess)'".

| Run | Map line | Who said it in the dump | By DECISIONS' wording | Printed |
|---|---|---|---|---|
| Hạnh | "TỪ KHOÁ: NGẠI CHÀO (không dấu: ngai chao)" | Thảo (named): "Chị ơi em ngại chào lắm…", then "sau này chị nghe bao nhiêu em nói y hệt". Card `why_this_one`: "nhiều em nói y hệt" | guess (case signature.vn.025 says so of this dump) | **no tag ✗** (VG5: tagged) |
| Tuấn | "TỪ KHOÁ: GỒNG LÃI (không dấu: gong lai)" | the preschool-teacher client (no name): "Mua thì sợ gồng lãi không nổi…", then "mười nhà ngồi với tui thì chắc bảy tám nhà nói 'sợ gồng lãi'" | guess | **no tag ✗** (VG5: tagged) |
| Khoa | "TỪ KHOÁ: TUYỂN HOÀI (không dấu: TUYEN HOAI)" | the seafood owner (no name): "Tôi tuyển hoài mà không giữ được ai.", then "không phải mình ảnh. Chủ doanh nghiệp nào gặp tôi cũng nói kiểu đó" + 3 anonymous lines | guess; heard only if anonymous example lines count | no tag ? (VG5: no tag) |
| Erin | "YOUR WORD: RECORD YEAR" | Marcus (named): "Record year. Empty account. Make it make sense.", then "that's what all of them say… record year and I can't sleep. record year and I put payroll on my personal card." Her card counts her own 2019 story and Dee, who never said it | guess; heard only if anonymous example lines count | no tag ? (G6: "(my guess)") |

Each machine's stated reason is the "everyone says it" sentence, so the kit line was read as "the coach reports many
clients say it". `eab8d0a` changed only that line in §CM-MAP, and the tags went from 3/4 to 0/4.

## 3. The founder's Day-0 rules in practice

| Run | Early-win copy box | Arrived · postable as is? | Soft cut | One message, one "?" · cost | Facts up front / guessed visibly |
|---|---|---|---|---|---|
| VN Hạnh | "Chị cũng làm kỹ thuật viên 5 năm cho một spa to ngoài phố, từ năm 2007, nên nói chung là chị đi lên từ cái giường massage em ạ, chị không học kinh doanh trường lớp gì đâu." | 4.8 · **partly**: a bio line spoken to the machine ("nói chung là… em ạ", "cũng"), not a line a spa owner stops on. Her standalone "Năm 2024 … inbox chị nổ tung luôn" (VG5's box) went in quotes | T7, at the crossing send, with the income-stream guess. The same message answers her "chi ra tiep khach ti": "Chị cứ ra với khách đi, chữ chị kể em giữ hết ở đây." | yes ("Đúng không chị?") · 0 (her answer came when she returned) | Her list was never said (the simulator adds VP-2 only from a later chunk). "danh sách Zalo, email: chưa có (chưa nghe thì em đoán…)" is wrong for her (240 on Zalo) but shown once and changeable |
| VN Tuấn | "Chị nói nhỏ xíu, nghe tiếng máy sấy tay ù ù phía sau, hóa ra chị đang trốn trong toilet nhà mẫu." | 4.6 · **partly** (third round): a scene with no why. At that send the deposit pressure was not yet told | T6, with the income-stream guess | yes ("Đúng không?") · 0 | Heard: TikTok, Zalo 1.850, no email; printed as heard. Talk day "tối Chủ nhật" guessed and tagged (his unheard answer: Monday; weekends are viewing days) |
| VN Khoa | "40 trên 210 người không quay lại sau Tết, không ai báo tiếng nào." | 4.5 · **yes**: a number hook any VN owner reads at once | T6, with the offer guess | yes ("Đúng không?") · 0 | Heard: LinkedIn, Facebook, Zalo 380, email 250; printed as heard. Talk day Monday guessed and tagged |
| EN Erin | "Best year in the history of the company and I'm in a stairwell asking the bank for payroll." | 4.0 · **yes** | T6, with the offer guess | yes ("Right?") · 0 | Heard: LinkedIn 2,900, list 380. The plan line tags the heard 380 as "my guess" (§2) |

Findings:
- **Early win: 4/4 in a copy box on the first send, 2/4 postable as is** (VG5: 3/4).
  - §CM-SETUP 2 asks that "câu vào khung đứng riêng thành bài được". Hạnh's pick broke it with a better line beside it.
  - Tuấn's needs context for the third round running. At minute 3 his first send holds no better line, so this is the
    dictation's order more than the kit's.
- **Soft cut: 4/4.** Each came at the crossing send, as one message with one "?", and cost no turn.
  - Over the line at the crossing: 46, 78, 106 and 131 words / tiếng.
- **Facts up front:**
  - The dump prompt asks for platform and list in 4/4.
  - The talk day is guessed in 4/4: Monday ×3, Sunday evening ×1. The kit gives no default (all 4 simulators flagged it).
    It is shown once and changeable, so no change is asked here.
- **The last Day-0 reply** runs past one phone screen of talk in 4/4. It holds Week-1 labels, the card top, the save
  line and the plan line: about 257 words (EN) and up to about 417 tiếng (Khoa) outside the boxes. This is the block's
  "one screen" rule against §CM-SETUP 9's "7–9 in one message", flagged by 3 simulators. Carried; no change asked.

## 4. Failed grader checks: real or false positive

| # | Run · check | Transcript line | Kit line or grader code | Verdict |
|---|---|---|---|---|
| 1 | Hạnh · vn_natural | "pieces end 9 of 60 sentences with a particle (15%); their own posts 54% (min 50% of theirs)". Long post: "Câu đấy là của Thảo ở Thái Bình, khóa 1 của chị." · "Các em là thợ lên làm chủ." · "Tuần này các em thử một việc thôi: …": 2 of 19 end on a particle. Her W1/W2 end on "nhé", "đấy", "ạ", "đâu", ":))" | §CM-NATURAL 4 "dày như bài họ, cả câu kể, câu mời, câu nói"; block TIẾNG VIỆT "tiểu từ dày như bài coach" | **R(m), kit-assisted.** The same rule gave 39% last round. About 5 of the 60 are grader noise (a piece title "Thứ Bảy, 10/10 · N2 · khoảng 25 giây", the label "Em ấy làm chủ spa:"); without them it is 9/55 (16%), still a fail |
| 2 | Tuấn · I15 "chị" | T3 NEXT "TIẾP → Kể tiếp chuyện chị trong toilet nhà mẫu." "chị" is his client, third person; em–anh holds in every turn | `i15_vn_language` L2212: the before-word list `các|những|mấy|của|tự|kết|tiếng|nước|nhà` lacks "chuyện" | **FP** |
| 3 | Tuấn · vn_natural | "pieces end 9 of 64 sentences with a particle (14%); their own posts 38% (min 50% of theirs)". Facebook post: 1 of 19 ("…hả anh", the client's quote). Spoken lines 3/8 | §CM-NATURAL 4 | **R(m).** Written pieces only; the spoken fix landed |
| 4 | Tuấn · vn_messages "no anh/chị slash" | Piece title, outside the box: "Hỏi 3 khách cũ · thứ Năm, 08/10 · Zalo, gửi riêng từng nhà, đổi chị/anh cho đúng người". The box keeps "chị" throughout | `check_vn_messages` L3284 matches on `p.body`, which starts with the title line (`_audience_chunks` L2084) | **FP** on the item. The message under it has a real VN4 slip the item does not test (§6, item 3) |

Grader misses:
- **The keyword guess tag has no check.** 4/4 untagged passed `day0_shape` (G46 below).
- **The EN plan line tags a heard fact as a guess.** No check; low stakes.
- **`particle_share` counts piece titles, bare labels and ALL-CAPS headings** ("TÍNH NGƯỢC TRƯỚC KHI CỌC") as
  sentences, and the demonstrative "đó" ("…không quá 40% số đó.") as a particle. No verdict changes this round.
- **P17 misses 2 of Tuấn's 3 repeated lifts** (§5): they share 4 tiếng or less with the source.

## 5. Leak spot-check (Tuấn, Khoa)

**Method:**
- For every machine turn, I listed each 5-gram (tiếng, case-folded) that is also in one of the persona files:
  `persona.toml`, `answers.md`, `expected.toml`, `voice-samples.md`, `launch-brief.toml`, `pillar-transcript.md`,
  `paste-dump.md`, `written-posts.md`, `research-paste.md` or `liked-paste.md`.
- I removed 5-grams of the coach's turns so far and of the kit, then merged the rest into runs.
- I listed every number the coach had not said.
- I searched for each fact that only the answer bank or the undictated chunks hold.
- I read each hit against the transcript.

**Khoa: clean.**
- 46 runs. All join his own words: the 3 steps, "15 phút", "60 ngày" and 31/19/17/4 come from T6; 45.000.000đ from T7;
  "Rứa là…" is his T3 with the mic's "dứa" fixed.
- The answer-bank and chunk-3 facts appear 0 times: 70%, 80%, "6 tháng lương", 200 triệu, the workshop's 6 → 3 weeks,
  the dental clinic's testimonial, the travel director's refused quote, 12 triệu training, the headhunt fee, Sunday
  6:30, "coach". His talk day was guessed Monday (his: Sunday) and tagged.

**Tuấn: valid. 0 edits. The same 3 lifts of undictated lines as VG5 are back.**

| Machine text | Persona source | What he said |
|---|---|---|
| Gift step 3 "…ra giá căn tối đa. Rồi mới đi coi nhà."; N3 "…rồi mới ra giá căn tối đa, rồi mới đi coi nhà." | `answers.md` chunk 2, never dictated: "…tính bằng lãi thả nổi, ra giá căn tối đa, rồi mới đi coi nhà" (9 tiếng word for word) | "căn tối đa khoảng 2 tỷ 2" (T4); W1 "Đi coi nhà mẫu thì cầm theo tờ giấy ghi con số" |
| Bán kèm "Mà trước khi dẫn ai đi coi, tui hỏi đúng một câu…" · "Mà nhà mình trả không nổi thì tui hổng dẫn đi coi." | answer bank "Tại tui ngồi tính trước rồi mới dẫn đi coi nhà" (never asked) | nothing about refusing to take a household to a viewing |
| card `offer` "Tuấn sống bằng hoa hồng căn hộ, bảo hiểm" | answer bank "Tui sống bằng hoa hồng: …" | W2 "tui có nhận hoa hồng" |

- No unsaid number appears: 68 triệu, "view sông", 68 m², 11 hồ sơ, his 2022 loan (1 tỷ 95, 13 triệu), 31 lớp, 3 tỷ 8
  are absent. The 2 tỷ 68 unit's rooms and area were asked through a "Cần anh" line, not filled in.
- **P17 caught one:** "ra giá căn tối đa rồi mới đi coi nhà" is in `leaks.warnings`, with "cọc rồi mới về tính". The
  other two share ≤4 tiếng with the source.
- **Verdict: valid.** The lifts add no number or name, and W1 implies "work it out before viewing". The Bán kèm line
  is a small undictated promise in his voice. This is the third round of the same lines, so P9 stays the real fix: a
  machine side that never sees the persona.

## 6. VN naturalness (VN1–VN8)

Bars, from `qa/standards/vn-naturalness.md`:
- **Pieces:** VN3, VN4, VN6 and VN7 at 2; total ≥13/16.
- **Coach-facing prose and Map lines:** VN3, VN4 and VN6 at 2; total ≥10/12.

Regions: Bắc (Hạnh), Nam (Tuấn), Trung/Quảng (Khoa).

| Run | Coach-facing /12 | Map lines /12 | QUAY HÔM NAY /16 | Week-1 posts /16 | Zalo + inbox (+ email) /16 |
|---|---|---|---|---|---|
| Hạnh | 11 ✓ (VN1 1: "Brand Card", "Lưu vào dự án") | 11 ✓ (VN2 1: line 1 says "hẹn" twice) | 16 ✓ | 15 ✓ (VN5 1: 15% vs her 54%) | 15 ✓ (VN5 1: "Dạ, kết bạn Zalo với chị nhé") |
| Tuấn | 10 ✓ (VN1 1: "cửa vào", "nằm trên bản đồ"; VN5 1: a bare "Đúng không?") | 11 ✓ (VN2 1: methods stacked, fifth round) | 16 ✓ (VG5 15) | 15 ✓ (VN5 1: Facebook post 1/19; VN7 2, his "tui" restored; VG5 14 ✗) | **14 ✗ (VN4 1, critical**: ask-3 "em – chị" with a swap note; VN8 1: "nhắn Tuấn chữ DỪNG" in a one-to-one) |
| Khoa | 10 ✓ (VN1 1: "Add text content"; VN5 1: "Em nhận rồi." ×4 with no "Dạ") | 11 ✓ (VN2 1: "60 ngày" twice in line 1) | 16 ✓ | 16 ✓ | 15 ✓ (VN1 1: "phần giới thiệu công việc") |

- **14/15 columns pass.** Tuấn's messages fail on VN4. Last round his posts failed on VN7, and that is fixed.
- 0 essay connectors, 0 banned tells. `vn_natural` found 0 translationese patterns in 3/3.

Lines that still read translated or stiff (D = translated, S = stiff), with a natural version:
1. **VN5 · Hạnh's long post**, 2 of 19 sentences on a particle. Her own posts end about every other line on one.
   - "Câu đấy là của Thảo ở Thái Bình, khóa 1 của chị." → "Câu đấy là của Thảo ở Thái Bình, khóa 1 của chị đấy."
   - "Các em là thợ lên làm chủ." → "Các em là thợ lên làm chủ mà."
   - "Tuần này các em thử một việc thôi: …" → "Tuần này các em thử đúng một việc thôi nhé: …"
2. **VN5 · Tuấn's Facebook post**, 1 of 19. His W2 ends "…tui nói thẳng luôn á", "…hổng bán gì hết 😅".
   - "Sợ gồng lãi mà vẫn suýt cọc, chuyện này tui gặp hoài." → "Sợ gồng lãi mà vẫn suýt cọc, chuyện này tui gặp hoài
     luôn á."
   - "Mà căn nào hợp là do con số, chứ hổng phải do cái rèm nhà mẫu." → "…chứ hổng phải do cái rèm nhà mẫu nha."
3. **VN4 · Tuấn's ask-3** (critical): "Nhờ chị một chút: em đang viết lại phần giới thiệu công việc, muốn lấy đúng câu
   của chị. Hồi mới tìm đến em, chị đang loay hoay nhất chuyện gì?" under "đổi chị/anh cho đúng người".
   - The toilet-house client says "anh Tuấn ơi … em có nên cọc không anh?", so "em" is wrong for her as well.
   - Fix, one text for every household, with no greeting missing and no swap: "Anh chị ơi, Tuấn đây. Tuấn đang viết
     lại mấy dòng giới thiệu, muốn mượn đúng câu của nhà mình. Hồi mới tìm tới Tuấn, nhà mình đang rối nhất chuyện gì
     vậy?" His own Zalo piece already opens "Anh chị ơi, Tuấn đây."
4. **D · Tuấn's plan line:** "Em đoán: cửa vào là buổi ngồi tính free, tiền về từ hoa hồng căn hộ với bảo hiểm."
   ("entry offer") → "Em đoán: anh mời người ta ngồi tính free trước, tiền thì về từ hoa hồng căn hộ với bảo hiểm."
5. **S · Tuấn T7:** "Căn 2 tỷ 68 vẫn nằm trên bản đồ: chủ đề 2, Tuần 1 có một bài riêng cho căn đó, chốt qua Zalo." →
   "Căn 2 tỷ 68 em có chừa chỗ rồi anh: Tuần 1 có một bài riêng cho căn đó, chốt qua Zalo."
6. **S (brochure) · Map line 1.**
   - Tuấn, fifth round: "…thì tìm Tuấn: tính ngược từ tiền góp mỗi tháng bằng lãi thả nổi, chừa quỹ 6 tháng, mua cái
     để che, chứ không bị dí cọc rồi mới về tính, ra căn tối đa trước khi cọc." → "Vợ chồng nào hay than "sợ gồng
     lãi" thì tìm Tuấn: tính ngược ra căn trả nổi rồi mới cọc, chứ không bị dí cọc rồi mới về tính." His own card top
     already says it in one breath: "Vợ chồng nào sợ gồng lãi thì tìm Tuấn, tính ngược trước khi cọc".
   - Hạnh: "…hẹn buổi sau chứ không dọa da, ép thẻ 30 buổi, để khách tự hẹn lại." → "…bán buổi hẹn sau chứ không dọa
     da, ép thẻ 30 buổi."
   - Khoa: "…kèm người mới 60 ngày, chứ không tuyển lấp chỗ, để người mới ở lại qua 60 ngày đầu." → "…kèm người mới,
     chứ không tuyển lấp chỗ, để người mới ở lại qua 60 ngày đầu."
7. **S · coach-facing lines.**
   - Khoa "Em nhận rồi." ×4 → "Dạ, em nhận rồi." (XƯNG HÔ: "Dạ" khi đáp; Hạnh and Tuấn have it).
   - Tuấn T6 and Khoa T6 "Đúng không?" → "Đúng không anh?" (Hạnh: "Đúng không chị?").
   - Khoa T8 "chuyện nhân sự khác anh vẫn kể, em lồng vào khi đúng chuyện" → "mấy chuyện nhân sự khác anh cứ kể, em
     lồng vô bài khi hợp."
8. **S · Hạnh's early-win box** (§3): box the line that stands alone, "Năm 2024 chị vào một cái nhóm chủ spa trên phây,
   có một em hỏi là sao em chào thẻ khách toàn từ chối, thế là chị ngồi gõ một cái comment dài ơi là dài, tối hôm đấy
   inbox chị nổ tung luôn."
9. **S · Hạnh's inbox 2:** "Dạ, kết bạn Zalo với chị nhé, chị xếp lịch buổi đầu cho." ("Dạ" with self "chị") → "Em
   kết bạn Zalo với chị nhé, chị xếp lịch buổi đầu cho em."
10. **S · labels before the joggers** (Hạnh ×3, Tuấn ×2; Khoa's machine dropped them).
    - "Gợi ý: chị kể em nghe chị chào khác đi thế nào, từng bước một." → "Chị kể em nghe chị chào khác đi thế nào
      nhé, từng bước một."
11. **S (call centre; founder hold until the VN legal sign-off) · Tuấn's Zalo** to acquaintances "gửi riêng người
    quen": "Không muốn nhận nữa thì nhắn Tuấn chữ DỪNG." In a one-to-one text: "Chưa cần thì nói Tuấn một tiếng nha."

Keep these; they read like a person:
- Hạnh T7 "Dạ, em nhận rồi. Chị cứ ra với khách đi, chữ chị kể em giữ hết ở đây."
- Hạnh's caption "Mà các em ngại chào cũng chỉ vì sợ thành người dọa khách thôi."
- Hạnh's long post "Hai kiểu nhìn thì ngược nhau, mà gốc là một: cứ tưởng chào là phải ép."
- Tuấn N1 "Câu đó mình thuộc lòng, tại mình đi dạy sale mà."
- Tuấn's Facebook post "Nói thiệt nè, tui làm môi giới, tui có nhận hoa hồng. Mà căn nào hợp là do con số, chứ hổng
  phải do cái rèm nhà mẫu."
- Tuấn's inbox 1 "Chào bạn, mình gửi tờ tính ngược nè:"
- Tuấn's Zalo "Nhà mình đang tính mua căn thì nhắn lại Tuấn một câu, Tuấn ngồi tính free cho."
- Khoa T8 "Dạ, dòng 1 em sửa cho rõ anh là người làm nhân sự, không phải người đăng tin:"
- Khoa N2 "Anh chị không có lỗi gì hết nghe. Cái sai là tuyển lấp chỗ."
- Khoa's ask-3 "Chào anh, tôi Khoa đây. Nhờ anh một chút: …" (the VG5 fix landed).

## 7. What improved vs the previous round (same personas)

| Measure | VG5 / G6 | VG6 / G7 |
|---|---|---|
| Valid | 4/4 | 4/4 |
| Grader passes | 0/4 | **2/4** |
| Failed checks: real / FP | 6: 4 / 2 | **4: 2 / 2** |
| Map coach turn (G31 count) | 7, 6, 6 · 6 | 7, 6, 6 · 6 |
| Film-ready, active | 18.9, 16.1, 16.5 · 19.7 | 19.8, 15.9, 16.9 · **17.1** |
| Early win, minutes after the dump prompt | 3.2, 4.0, 3.2 · 4.6 W | 2.9, 3.3, 3.3 · **3.6** |
| Early win postable as is | 3/4 | 2/4 ✗ (Hạnh) |
| Extra turns from the cut's question | 0 | 0 |
| I12 (on-screen >6) | EN + Hạnh | **none** |
| EN whole card | 6,076 ✗ | **5,647** |
| Save line route + backup | 3/4 | **4/4** |
| Tuấn's Facebook self-reference | "mình" ×15 ✗ | **"tui" ×12** |
| Particles, written (G42 count) vs their posts | Hạnh 39% (54), Tuấn 18% (38) | Hạnh 15% ✗, Tuấn 14% ✗ |
| Particles, spoken lines | Hạnh 3/8, Tuấn 0/9 | Hạnh 2/8, **Tuấn 3/8** |
| Day-0 keyword tagged where DECISIONS says guess | 3/4 (Khoa untagged) | **0/4** ✗ |
| Plan line tags only unheard facts | VN 1/3, EN yes | **VN 3/3**, EN no ✗ |
| VN critical items at 1 | Tuấn VN7 | Tuấn VN4 (ask-3) |
| Leaks found in the spot-check | 3 undictated lifts (Tuấn) | same 3 (Tuấn); Khoa clean |

## 8. Prioritised fix list

Budgets now:
- EN block 6,493/6,500 chars; EN method 49,171/51,200 B; EN §CM-MAP 2,798/2,800 B; EN §CM-SETUP 2,783/2,800 B.
- VN block 7,496/7,500 chars; VN method 56,319/56,320 B (§CM-MAP 3,334/3,600).

After items 1–3:
- **EN:** §CM-MAP 2,783 (−15), §CM-SETUP 2,798 (+15), method 49,171 (±0). The block is unchanged.
- **VN:** method 56,316/56,320 (+29 −33 −20 +21 = −3). The block and the Phone Starter are unchanged.
- Refresh the src hashes.
- Update the case notes and tests that quote the changed text:
  - "Voice line too", "Cả dòng giọng", "(cả kịch bản nếu đổi)": `message.en/vn`, `voice.en/vn`, `signature.vn`,
    `router.vn`.
  - "Else: the best buyer phrase": `signature.en`.
  - "(my guess; one word changes it)": `setup.en`, `router.en`, `tools/tests/test_checks.py`, `test_graders.py`.

### Kit

**P1: blocks acceptance**

1. **K42 / VK-39. Spell out the keyword counter-example** (0/4 tagged; founder rule over-applied).
   - EN `modules/en/signature.md` L6: "Else: the best buyer phrase "(my guess)"" → "Else (one client + "they all say
     it"): the best buyer phrase "(my guess)"" (+33 B).
     - **Cut:** `modules/en/message.md` L8, drop " (and FILM TODAY, if it changes)" (−32 B). Block step 4 already
       says "a change reprints its line, and the script if that changes".
     - **Cut:** the same line, drop " Voice line too." (−16 B). "change N" covers line 4, and §CM-VOICE 2 has "change 4".
   - VN `modules/vn/signature.md` L8: "Chưa đủ: cụm khách nói nhiều nhất" → "Chưa đủ (1 khách + "ai cũng nói"): cụm
     khách nói nhiều nhất" (+29 B).
     - **Cut:** `modules/vn/message.md` L13, drop " (cả kịch bản nếu đổi)" (−33 B). Block step 5 holds it.
     - **Cut:** the same line, drop " Cả dòng giọng." (−20 B). §CM-VOICE 2 has "sửa dòng 4".
   - Founder call (a) below settles Khoa and Erin; the text above already tags them.
2. **VK-40. Particles: count them, piece by piece** (Hạnh 39% → 15%, Tuấn 18% → 14% on the same rule).
   - `modules/vn/humanize.md` L32 §CM-NATURAL 4: "dày như bài họ, cả câu kể" → "dày như bài họ (đếm, mỗi bài), cả câu
     kể" (+21 B). Paid by item 1's VN surplus (−24 B).
   - The same "(đếm)" ended the I12 slips this round.

**P2: real defects, graded weakly or not at all**

3. **K43. The EN plan line scopes its guess** (VK-35's EN half; Erin's heard 380 is tagged as a guess).
   - `strings/en.toml` L258 `setup.plan_guess`: "(my guess; one word changes it)" → "(my guess, where unheard; one word
     changes it)" (+15 B in §CM-SETUP 5: 2,798/2,800; fits, no cut).
   - The comma keeps `tools/cmcore/checks.py` `_GUESS_AFTER` matching it.

**P3: one run, wording (left for room, no change now)**

4. **Map line 1 stacks methods** (Tuấn fifth round, Khoa, Hạnh).
   - `core/vn/start-block.md` L37 "{cách làm}" → "{một cách làm}" costs +4 chars and would fill the block to 7,500.
     No block cut is clean (", 1,5tr" is the money example §CM-LOCALE 5 points to). Leave until a cut is found.
5. **Tuấn's ask-3 register** (§6 item 3). A §CM-MESSAGES line ("nhiều người: tự xưng tên, gọi 'nhà mình'") needs about
   50 B with no VN cut left. Leave; re-check next round.
6. **Carried, no change:**
   - the "Gợi ý:" labels, which the block's own dump prompt models;
   - "Đúng không?" with no vocative;
   - "Em nhận rồi" with no "Dạ" (machine slips);
   - the DỪNG line (founder hold);
   - the talk day's missing default;
   - the long last Day-0 reply.

### Graders (`evals/graders.py` unless noted)

- **G44.** `i15_vn_language` L2212: add "chuyện" to the before-word list ("Kể tiếp chuyện chị trong toilet nhà mẫu" is
  the client). This fixes Tuấn's FP.
- **G45.** `check_vn_messages` L3284: match `SLASH_ADDRESS_RE` on the piece body without its title line. The title is
  coach-facing ("đổi chị/anh cho đúng người"). This fixes Tuấn's FP. A "Chào anh/chị," inside the box still fails.
- **G46.** `check_day0_shape` (L4187): new item "YOUR WORD carries the guess tag unless the dump quotes it from 3+
  named clients".
  - Ground truth goes in `expected.toml [keyword] day0_heard`: `false` for `vn/hanh-android-free-nocomputer` and
    `vn/tuan-multihat-plus`.
  - `vn/consultant` and `en/consultant` get theirs after founder call (a).
  - The tag strings to match: "(my guess", "(mình đoán", "(em đoán".
- **G47 (optional).** `vn_sentences` / `_vn_pieces`: leave out piece-title lines (" · N2 · "), bare labels ending in
  ":", ALL-CAPS headings, and "đó" after "số" or a number. No verdict changes now; it stops noise near the 0.5 line.

### Protocol

- **P18.** `evals/run.py`, MACHINE.md: "Today's date: the date in the transcript" → write the run's date ("Today's
  date: Tuesday 6 October 2026"). No transcript row has a date. All 4 simulators flagged it, and EN dated its card 12
  Oct while VN used 6 Oct.
- **Re-run** all four after items 1–3 and G44–G46:
  - all four for the keyword tag;
  - Hạnh and Tuấn for VK-40;
  - EN for K43.

### Founder call

- **(a) "Named" clients.** Does a phrase count as heard when the coach quotes one identified client and then gives
  2–3 anonymous example lines ("everyone says it: '…', '…'")?
  - Khoa: the seafood owner + 3 anonymous lines. Erin: Marcus + 2 anonymous variants.
  - **Recommendation: no.** Count only clients the coach names or tells apart, each saying the phrase. Otherwise nearly
    every dump qualifies ("everyone tells me X" is how coaches talk), the tag disappears, and the Week-1 check with it.
  - Item 1's text already reads this way.
