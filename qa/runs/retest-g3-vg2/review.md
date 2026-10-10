Result: FAIL

# Retest G3 (EN) + VG2 (VN) Day-0 after the G2/VG1 fix round: independent review

Reviewer: independent and bilingual (EN, plus native Vietnamese for the VN runs). I wrote neither the kit nor the runs.

Kit under test: commit `ba679c2`, working tree clean. Each run's `packet/kit/` is byte-identical to the current `dist/`:
- EN: block 6,488 of 6,500 chars; method file 49,032 B. Run build `d0155d7ace49`.
- VN: block 7,495 of 7,500 chars; method file 56,318 of 56,320 B. Run build `d5449fc3fe7d`.

How this review was done:
- All 8 transcripts were read in full, as the coach would read them on their phone.
- Scratch copies of the 8 folders were re-graded with the current `evals/run.py grade`. The verdicts match the stored
  `grades.json` exactly, and the run folders were not touched.
- Every failed check was traced to its transcript line and to the kit line or grader code behind it.
- Leaks were checked in 2 runs (proof-coach S0 and Tuấn) with my own scans; method in section 5.
- VN naturalness was scored on `qa/standards/vn-naturalness.md` (VN1–VN8). Every line I mark is quoted with a natural
  fix (section 6).

## Why FAIL

- **VN film-ready is over 20 active minutes in 4 of 4 runs** (21.4, 22.5, 22.7, 21.4). Two of these are real; two are
  a timing artefact.
  - **Hạnh (real, kit):** the soft cut never fired. After chunk 2 she was at 1,436 tiếng with posts (1,246 without),
    which is just under "quá ~1.500 tiếng". The machine sent a jogger that asked her price with no guess, so she
    dictated a third chunk of 5.3 minutes.
  - **Tuấn (real, by design):** the cut fired, and its own line "Còn chuyện nào thì kể luôn" invited the third chunk he
    had announced ("ờ còn nữa, chờ tui chút"). That chunk added 5.7 minutes. It also brought in the apartment he has
    to sell and "đừng bỏ BĐS", so this is a trade-off for the founder to rule on.
  - **coldstart and consultant VN (timing artefact):** these simulators stamped the 2.5-minute read of the Map reply on
    the machine turn. Five of the other six runs stamped reading time on the coach's next turn. On that convention,
    coldstart is at ≈19.0 and consultant VN at ≈19.2. The protocol does not say which convention to use (P12).
- **`[Tên]` blanks in the 1:1 messages of 3 of the 4 VN runs.** The cause is the VK-7 wording itself:
  `modules/vn/humanize.md` §CM-NATURAL 4 says 'không "anh/chị", [Tên]', and the machine reads the list as "use [Tên]".
- **YOUR WORD only in the ask** (the Week-1 piece carries the keyword only in its "Comment X" line):
  - EN: 2 of 4 runs, 5 pieces. The grader caught 4 and missed consultant's Fri post because of a piece-split bug.
  - VN: the same defect in Tuấn (4 pieces) and consultant VN (N3); Hạnh's N2 and N3 carry it only inside the ask
    sentence. It is ungraded, because G17 runs for EN only.
  - Cause: the kit's "Keyword once, plus the ask" reads as a cap.
- **VN language:**
  - The pieces still end flat. Particles are on 11–26% of their sentences, against 46–64% in the coaches' own posts,
    so `vn_natural` is real in 3 of 4.
  - The coach-facing replies pass in 1 of 4. The two fixed strings now read right; the remaining VN6 hits are
    `setup.multi_income`, the §CM-MAP shorthand "một góc của ý lớn", and one machine calque.
- **5 failed grader checks are still false positives**, all VN, plus 2 false-positive sub-items inside real checks. The
  grader also misses 3 real defects.
- **Protocol:** the first draft of the consultant VN machine side used the persona's real talk day (Chủ nhật, never
  said). The simulator changed it before grading. Pre-grade self-scans and edits get round P8's freeze.

**What passed:**
- All 4 EN runs meet every Day-0 budget:
  - Map in ≤6 coach turns;
  - film-ready in ≤20 active minutes;
  - ≤10 coach turns;
  - card ≤5,700 characters.
- 2 runs pass the grader outright (EN proof S1, Linda): the first grader passes in any round.
- In VN, the Map turn and the coach-turn budgets are met in 4 of 4.
- All 3 spoken objections to comment asks were honoured at once.
- The two coach-facing strings are fixed in 4 of 4 runs.
- Every coach comes back (per the simulators); 0 quits.

## 1. The runs

Previous-round figures are in brackets (G2 for EN, VG1 for VN). "Map turn" is the coach turn the Map answers; with K2,
that is also the film-ready turn. "Early win" is the minute the copy box arrived; after the "·" is the minute counted
from the dump prompt (acceptance ≤4; graded as a warning).

Verdict codes:
- R: a real defect. R(kit): the kit wording caused it. R(m): a machine slip.
- R\*: real on the graded number, but inflated by the timing convention.
- FP: a grader false positive.

| Run | Lane · app | Valid | Coach turns | Map turn | Early win | Film-ready (active) | Grader failures: verdict |
|---|---|---|---|---|---|---|---|
| EN proof-coach | S1 · ChatGPT Free | yes | 7 (8) | 6 (7) | 6.7 · 6.4 | 19.1 (19.1) | **none: PASS** |
| EN proof-coach | S0 · ChatGPT Free | yes (1 logged leak edit) | 7 (8) | 6 (7) | 7.2 · 6.3 | 19.3 (20.0) | I12 R(m; S0 block has no cap for the Week-1 shorts) · day0_shape R(kit): keyword only in the ask ×3 |
| EN Linda | S1 · Claude Pro, Mac | yes | 7 (8) | 6 (7) | 7.7 · 7.2 | 18.6 (27.3) | **none: PASS** |
| EN consultant | S1 · Claude Free | yes | 6 (7) | 5 (6) | 6.5 · 6.2 | 17.6 (23.0) | day0_shape R(kit): keyword only in the ask ×3 (grader saw 2) |
| VN coldstart | S1 · ChatGPT Free, iPhone | yes | 9 (11) | 7 (8) | 9.2 · 7.1 | 21.4\* ≈19.0 (18.4) | I11 FP · day0_timing R\* · day0_shape R(kit) `[Tên]` · vn_natural R |
| VN Hạnh | S1 · ChatGPT Free, Android | yes | 8 (8) | 6 (6) | 7.9 · 6.3 | 22.5 (20.2) | I23 R (proxy, low) · day0_timing R(kit): cut never fired · vn_natural R |
| VN Tuấn | S1 · ChatGPT Plus | yes | 8 (9) | 6 (7) | 8.3 · 7.1 | 22.7 (18.2) | I8 FP · day0_timing R (founder trade-off) · day0_shape R(kit) `[Tên]` + "no email" FP item · vn_natural R |
| VN consultant | S1 · Claude Pro | yes | 7 (9) | 6 (7) | 8.6 · 6.9 | 21.4\* ≈19.2 (19.9) | I6 FP · I9 FP · I11 FP · I12 R(m): 19 tiếng · day0_timing R\* · day0_shape R(kit) `[Tên]` + CTA "của" FP item |

Totals:
- **Valid: 8 of 8. Grader pass: 2 of 8** (0 of 8 on these personas last round). Quits: 0. Comes back: 8 of 8.
- **Failed checks: 20.**
  - 15 are real: EN 3, VN 12. Two of the VN ones are timing-inflated.
  - 5 are false positives, all VN. Two more false-positive sub-items sit inside real `day0_shape` checks.
  - Last round, on the same 8 personas: 30 failed checks, 13 real and 17 false positive.
- **Grader misses (real, not failed):**
  - consultant EN Fri post: keyword only in the ask;
  - VN keyword only in the ask: Tuấn 4 pieces, consultant 1 (Hạnh 2 inside the ask sentence);
  - proof S0 DM reply box: "(paste the 3 questions)", a slot left for the coach to fill.

Budgets:

| Budget (acceptance `[day0]`) | EN 4 runs | VN 4 runs |
|---|---|---|
| Map ≤6 coach turns (VN ≤7) | 4/4 | 4/4 |
| Film-ready ≤20 active min | 4/4 | 0/4 graded; 2/4 on one timing convention |
| ≤10 coach turns | 4/4 (6–7) | 4/4 (7–9) |
| Session ≤40 active min | 4/4 (20.9–23.1) | 4/4 (26.0–33.5) |
| Card top ≤500 / whole card ≤5,700 EN, 6,600 VN | 4/4 (whole 3,243–5,662) | 4/4 (whole 4,467–≈6,600; consultant VN at the limit) |
| Early win ≤4 min after the dump prompt | 0/4 (6.2–7.2) | 0/4 (6.3–7.1) |

## 2. Did the fixes aimed at each run work?

| Run | Fix aimed at it | Worked? | Evidence |
|---|---|---|---|
| EN proof S1 | K22 cut with no "done" round trip → Map ≤6 | **yes** | Map at turn 6 (was 7); the cut and the consent guess came in one message (T4), and she answered both in T5 |
| EN proof S1 | K24 list/platform heard or guessed visibly | **yes, but guessed wrong** | Platform heard from the paste ("first one was on instagram"). Plan line: "email list: none (my guess; one word changes it)", and the card says `list_size=ask` (I8 gone). Her 140-person list is in chunk 3, which was skipped. Week 1 has a message to 3 women instead of an email: quit point #12 is now visible and takes one word to fix |
| EN proof S0 | K22 → Map ≤6; K26 safe consent default | **yes** | Map at 6; "she hasn't OK'd sharing it yet, so I won't post it until she does" (G2 guessed "OK'd") |
| EN proof S0 | K24 visible guesses | **yes, both wrong** | "you post on Facebook … no email list yet" (she is on Instagram, with a list of 140). Visible and one-word fixable |
| EN proof S0 | K25 first line ≤12 words | **FILM TODAY yes; Week 1 no** | FILM TODAY line is 12 words; Short 3 is 13 (I12). In compact mode the cap sits only in step 5 |
| EN Linda | K22 → Map ≤6, film-ready ≤20 | **yes** | Map 6 (was 7), 18.6 min (was 27.3) |
| EN Linda | K30 "clients named, no outcome → ask what changed" | **yes** | T4: "what changed for Renee after you worked together…" (G2 told her "no client result") |
| EN Linda | VK-2/VK-4 mirrors: spoken objection → quiet, then Week 1 | **yes** | "Quiet it is … And text is fine; nothing to film." Caption reprinted, Week 1 in the same reply, NEXT adapted to "Post today's caption as text" |
| EN consultant | K22 cut on a word count → film-ready ≤20 | **yes** | Cut after chunk 2 (1,282 dictated words), Map at turn 5, 17.6 min (was 23.0) |
| EN consultant | K29 card trim order | **yes** | Whole card 5,662 (was 6,090); proof S1 5,641 (was 5,893) |
| EN, all | K27 "Shorter" | **not exercised** | No coach said it (EN coldstart was not re-run) |
| VN coldstart | coach-turn count (VK-4: Map pushback, then Week 1) | **yes** | 11 → 9 coach turns, Map 8 → 7. Three pushbacks in one message got one line each, then Week 1 in the same reply |
| VN coldstart | VK-19 gift written out, no blanks | **yes** | "Lịch 1 ngày cho cái lưng ngồi máy" in full under the caption |
| VN Hạnh | film-ready ≤20 (soft cut) | **no** | 1,436 tiếng with posts at the end of chunk 2 → no cut. T5 jogger: "Lúc quay lại, chị kể nốt lớp kèm của chị: các em học thế nào, giá bao nhiêu." → a 655-tiếng chunk 3 → 22.5 |
| VN Tuấn | VK-3 `multi_income` one question | **yes** | T5: one "Đúng không?", and I5 is gone. Its wording still reads translated (§6, line 1) |
| VN consultant | VK-2 spoken objection → quiet at once | **yes** | "Dạ, từ giờ em không xin comment nữa, chỉ mời nhắn riêng." Every Week-1 ask is quiet; no argument |
| VN all | VK-1 the two coach-facing strings | **yes, 4/4** | "Quay luôn bây giờ, hoặc đăng phần chữ làm bài viết." and "Ngại xin comment thì gõ 'nhẹ'." both read natural |
| VN all | VK-6/7/8/9 1:1 register | **mostly; VK-7 backfired** | No "anh/chị" slash; no DỪNG in inbox replies (4/4); no "Dạ" from chị to em (Hạnh); "Em ơi, nhờ em một chút … loay hoay nhất chuyện gì?" in Hạnh's Bắc voice. **New:** `[Tên]` 1–3 times in each 1:1 message in coldstart, Tuấn and consultant |

## 3. The founder's new Day-0 rules in practice

| Run | Early win: line in the copy box | Arrived · postable? | Soft cut | One message, one question? | Cost a coach turn? | Facts asked up front / guessed visibly |
|---|---|---|---|---|---|---|
| EN proof S1 | "I sent out 63 applications in 7 months. I got 2 interviews. And both interviews were for my old job at a different company." | 6.7 · yes. Repeats her own W2 post, which arrived after | after c2, with the consent guess | yes | no | Prompt ✓ · platform heard · list guessed "none" (wrong, 140) |
| EN proof S0 | "I didn't want that job. I wanted it because it was the only job I knew how to want." | 7.2 · partly: "that job" has no context | after c2, with the consent guess | yes | no | Prompt ✓ · platform guessed FB (wrong) · list "none" (wrong) |
| EN Linda | "I sat in the parking lot until like 9:15 and I didn't go in. I didn't know who to be at 9 o'clock on a Monday." | 7.7 · yes (she'd drop "like") | after c2, with the Renee question | yes, but compound ("what changed … and is she OK…?") | no | Prompt ✓ · LinkedIn + newsletter heard · size "not known yet" |
| EN consultant | "Best year in the history of the company and I'm in a stairwell asking the bank for payroll." | 6.5 · yes | after c2, with the offer guess | yes | no | Prompt ✓ · LinkedIn + Monday Number heard · size "not given" (she has 380; the email went last, not first) |
| VN coldstart | "Đi tập 90 phút cuối tuần mà cả tuần ngồi y chang thì cũng chỉ là chữa cháy thôi. Cái lưng nó cần mỗi ngày, ko phải mỗi tuần." | 9.2 · yes, in her own words and spelling | after c2 (1,551 with posts), with the no-result guess | yes | no; but a second, avoidable question followed (T6 "bạn chưa bán gì online"; chunk 1 said "muốn làm cái gì đó online") | Prompt ✓ · TikTok guessed (kit default for young buyers; right) · list "chưa có" |
| VN Hạnh | "Chị lôi cái sổ thẻ ra lật từng trang đếm, 41 thẻ thì 27 thẻ khách bỏ dở… Tức là mình bán được thẻ chứ mình có giữ được người đâu." | 7.9 · partly: needs "Năm 2018" to stand alone | **never fired** (1,436 < ~1,500) | n/a | n/a; cost 5.3 min of dictation | Prompt ✓ · FB guessed (right) · list "chưa có" |
| VN Tuấn | "Tui hay lấy mốc là tiền góp ngân hàng không quá 40% lương hai vợ chồng, mà tính bằng lãi thả nổi chứ đừng tính bằng lãi ưu đãi năm đầu." | 8.3 · yes, in his "tui" | after c2, with the multi-income guess | yes | no turn; **+5.7 min**, because he told the "one more story" | Prompt ✓ · TikTok, FB, Zalo 1,850 all heard in chunk 3 |
| VN consultant | "Tuyển 15 phút thì người ta ở 15 ngày." | 8.6 · yes | after c2, with the offer guess | yes | no | Prompt ✓ · FB guessed (his main channel is LinkedIn) · list "chưa có" (wrong, 250 emails) |

Findings:
- **Early win: delivered 8/8** in a copy box, with the "post it" line, in the reply to chunk 1. It is postable as is in
  6/8; 2 need a few words of context (§CM-POSTS 6 "stands alone").
  - It still lands 6.2–7.2 minutes after the dump prompt, not "minute 5–6", because each persona's first chunk takes
    4.6–6.4 minutes to dictate (P10/VP-4, still open).
  - Last round both proof-coach runs said "I'm starting to wonder if this was a waste of money" at minute 15; this
    round neither did.
- **Soft cut: fired 7/8.** Every time it was one message with one question mark, and it cost no coach turn.
  - Linda: the cut message's question was compound.
  - Hạnh: it never fired.
  - Tuấn: it fired, but cost 5.7 minutes when he took up the "one more story" offer.
- **Facts asked up front:**
  - The dump prompt names platform and list in 8/8, and the plan line shows every unheard guess in 8/8, marked "my
    guess / mình đoán, one word changes it".
  - **The up-front ask cannot change these runs.** COACH.md has the coach dictate the persona's chunks word for word,
    and every persona keeps list and channel facts in chunk 3 (VP-2). So 4 visible guesses are wrong: proof S1 list,
    proof S0 platform and list, consultant VN list.
- **Talk day:** guessed blind in 8/8 (the kit never asks it) and wrong in 3: proof S1, consultant EN and consultant VN.
  Day 0's last reply then offers a nudge "on talk day", which is undefined for the coach (K36).

## 4. Failed grader checks: real or false positive

| # | Run · check | Transcript line | Kit line or grader code | Verdict |
|---|---|---|---|---|
| 1 | proof S0 · I12 | T7 Short 3: "On the way out, they hand you a box. What goes in it?" (13 words) | S0 block step 5 caps only the FILM TODAY first line; step 6 has no cap | **R(m)**: a miscount; the kit gap matters in compact mode only |
| 2 | proof S0 · day0_shape | Shorts 1–3 carry CHAPTER only in "Comment CHAPTER…"; the long post has "One more chapter" | block ship.kit "keyword once + one specific" (`core/en/ship-check.md` L12) | **R(kit)** |
| 3 | consultant EN · day0_shape | Tue post, Thu PDF post (slide 11 only) and **Fri post** carry RECORD YEAR only in the ask. The simulator says it "misread 'Keyword once, plus the ask' as a cap" | `modules/en/plan.md` L11 §CM-WEEK 4. Grader miss: "Mon, Oct 19 · the Monday Number (email)" is not read as a piece title, so the email (which has "A record year…") merges into the Fri piece | **R(kit)**; grader miss (G25) |
| 4 | coldstart · I11 "tốt nhất" (T7, T8, T9) | Her catchphrase "tư thế tốt nhất là tư thế kế tiếp" on the GIỌNG line, N3's last line, inbox 2 and the card | `i11_injection` (graders.py L1630) skips never_say/do_say and principles, but not the coach's verbatim phrase | **FP**. The phrase is not a claim about her service; §CM-VOICE keeps their phrases word for word |
| 5 | coldstart · day0_timing | Map at 21.4: c7 at 18.7 ("đúng, chưa có gì hết") + 2.7 min to read a 491-word reply | packet README (`evals/run.py` L197): "`t_min` is the modelled minute the turn ends"; COACH.md "Time:" (L249) names reading speed but not which turn it goes on | **R\***: ≈19.0 when reading time goes on the coach's next turn, as in proof S1, Linda, consultant EN, Hạnh and Tuấn. A second question was also avoidable (T6) |
| 6 | coldstart · day0_shape `[Tên]` | T8 Zalo: "[Tên] ơi, mình Minh Anh nè. Nhờ [Tên] một chút… giờ [Tên] thấy khó nhất chỗ nào?" | `modules/vn/humanize.md` L32 §CM-NATURAL 4 'không "anh/chị", [Tên]' | **R(kit)**: the VK-7 wording is read as an instruction to use [Tên] |
| 7 | coldstart · vn_natural 26% vs 64% | Captions mostly carry "nha/á"; the Ý lines and long post end flat | same L32: "không câu nào cũng có" pulls the rate down | **R** (VN5 = 1, soft) |
| 8 | Hạnh · I23 1/7 | Pieces rarely use her listed phrases ("chị nói thật nhé", "Các em ạ"), though they are full of her dump lines ("bán được thẻ chứ có giữ được người đâu", "các em không có máu buôn") | `i23_voice` L2503 proxy | **R (proxy, low)**. Read as the coach, VN7 = 2; only her opener is unused |
| 9 | Hạnh · day0_timing 22.5 | No cut at 1,436 tiếng; T5 jogger asks the price → 655-tiếng chunk 3 | `core/vn/start-block.md` L35 "quá ~1.500 tiếng" | **R(kit)** |
| 10 | Hạnh · vn_natural 12% vs 53% | "Không chào thêm gì cả." · "…chị gửi 3 bước cầm gương nói thật." Her posts: "chị nói thật nhé", ":))", "e ạ" | humanize L32 | **R** (VN5 = 1) |
| 11 | Tuấn · I8 "15" | T7 plan line "thứ Hai hằng tuần kể 15 phút cho tuần sau" | `strings/vn.toml` L272 `setup.plan_guess` (kit digit); `i8_numbers` L1454 does not take rendered string digits as kit tokens | **FP** |
| 12 | Tuấn · day0_timing 22.7 | T5 soft cut "Còn chuyện nào thì kể luôn…" → he dictates chunk 3 (679 tiếng) | `strings/vn.toml` L122 `dump.enough`, as DECISIONS wrote it | **R (by design)**: a founder trade-off (facts vs minutes) |
| 13 | Tuấn · day0_shape | (a) "coach named an email list, and Week 1 has no email": he said "Email thì không có"; the card's `list_size: 1850` counts Zalo contacts. (b) `[Tên]` ×5 in the Zalo pieces | (a) graders.py L3594–3598 reads any `list_size>0` as an email list. (b) as #6 | (a) **FP item** (Week 1 has its Zalo message) · (b) **R(kit)** |
| 14 | Tuấn · vn_natural 11% vs 46% | "Nhắn mình chữ GỒNG LÃI, mình gửi bạn Tờ tính trước khi cọc." on 4 captions; his posts end "nha", "á", "nè" | humanize L32 | **R** (VN5 = 1) |
| 15 | consultant VN · I6 | Topic "Người mới quyết định nghỉ từ tuần đầu" | `DECISION_RE` (L224) matches "quyết định" anywhere | **FP** |
| 16 | consultant VN · I9 | "Rứa là năm nay mình tuyển lại từ đầu hả Khoa?" (he dictated "dứa", a mic mishearing) | §CM-SETUP 1 allows fixing misheard words; `i9_quotes` L1526 wants verbatim | **FP** |
| 17 | consultant VN · I11 "tốt nhất", "số 1" | Card `phrases` "người phỏng vấn tốt nhất là…" (his opinion line); `written_vs_spoken` "đánh số 1 2 3" | `i11_injection`: VG-10 dropped `principles` only | **FP** |
| 18 | consultant VN · I12 | QUAY HÔM NAY câu đầu: 10 giờ đêm, anh chủ quán hải sản nói với tôi: "Tôi tuyển hoài mà không giữ được ai." (19 tiếng) | step 6 "≤18 tiếng" | **R(m)**: a miscount, marginal |
| 19 | consultant VN · day0_timing | Map at 21.4: c6 at 18.9 + 2.5 min to read 458 words | as #5 | **R\***: ≈19.2 on the common convention |
| 20 | consultant VN · day0_shape | (a) "CTA asks for 'của'": the parser read Ý 1 "tin nhắn của em phục vụ" as an ask; the real CTA is "Comment TUYỂN HOÀI". (b) "Chào [Tên], tôi Khoa đây." ×3 | (a) `cta_keyword` L3402 / `_ASK_BEFORE` L3511: "nhắn" after "tin" is a noun. (b) as #6 | (a) **FP item** · (b) **R(kit)** |

## 5. Leak spot-check (2 runs) and protocol

The two scans:
- **Method:** for every machine turn, every 5-gram (EN words, VN tiếng) that is also in the persona's `persona.toml`,
  `answers.md`, `expected.toml`, `voice-samples.md`, `launch-brief.toml`, `pillar-transcript.md`, `paste-dump.md` or
  `written-posts.md`, minus 5-grams of the coach's turns so far and of the kit. I also listed every number and word the
  coach had not yet said.
- **proof-coach S0: clean.**
  - 42 hits, each a join of the coach's own words: "$2,400 or 3 payments of $800" (T4), "kids grown or in college"
    (T2), "first coffee to job offer" (T4).
  - The only new number is 2026, a date. "designer" is the mic's "design er" (T4) made whole.
  - The one logged edit (T7, Bev's line in the card) was a real persona-file phrase, removed and logged as P8 asks.
- **Tuấn: clean.**
  - 101 hits, all said by the coach: "toilet nhà mẫu", "32 triệu", "2 tỷ 68", "58 hợp đồng", "quỹ 6 tháng".
  - New numbers are dates only; "1850" is his "1.850".
  - The one new idea word, "kẻo" in `key_belief`, is a paraphrase, not a fact.
- **Talk-day guesses that match persona.toml are not leaks.**
  - coldstart's Chủ nhật follows from her class days (Mon/Wed/Fri evening, Sat morning).
  - Hạnh's thứ Hai and Tuấn's thứ Hai are the kit's `{thứ Hai}` default.

**Protocol concern (P13).** The single-agent simulator still reads the persona before writing the machine side.
- consultant VN notes.md: "The persona's real day is Sunday; I first drafted 'Chủ nhật' and changed it before grading."
  The coach never said Sunday, so that draft leaked a persona fact.
- Tuấn notes.md: "Before the first grade, I ran the protocol checks on a scratch copy of the draft. I then reworded a
  few machine lines…" (about 8).
- P8 freezes the transcript only at the first grade, so these edits show as `edited: 0`.
- Both are disclosed, and the final transcripts are clean. But the leak rate this round is partly hand-tuned, as in G2.
  The real fix is still P9: a machine side that never sees the persona.

## 6. VN naturalness (VN1–VN8)

Bars, from `qa/standards/vn-naturalness.md`:
- **Pieces:** VN3, VN4, VN6 and VN7 at 2; total ≥13/16.
- **Coach-facing prose and Map lines:** VN3, VN4 and VN6 at 2; total ≥10/12.

Regions: Nam (coldstart, Tuấn), Bắc (Hạnh), Trung/Quảng (consultant).

| Run | Coach-facing /12 | Map lines /12 | QUAY HÔM NAY /16 | Week-1 posts /16 | Zalo + inbox /16 |
|---|---|---|---|---|---|
| coldstart | 10 ✗ (VN1 1: "Brand Card", "Caption"; VN6 1: "của chính bạn", "một góc của chủ đề 1") | 11 ✓ (VN2 1: tacked-on tail) | 15 ✓ | 15 ✓ (VN5 1) | 16 on language ✓, but `[Tên]` ×3 is a fill-in template |
| Hạnh | 11 ✓ (VN1 1: "Brand Card", "⋯ … Lưu vào dự án") | 12 ✓ | 16 ✓ | 15 ✓ (VN5 1) | 16 ✓ |
| Tuấn | 10 ✗ (VN6 1: `multi_income` "hơn một thứ"; VN1 1) | 11 ✓ (VN2 1: four methods stacked) | 15 ✓ | 14 ✗ (VN5 1; VN7 1: the Facebook long post says "mình" where his Facebook voice is "tui") | 15 ✓ (VN8 1: call-centre DỪNG in a personal Zalo), `[Tên]` ×5 |
| consultant | 10 ✗ (VN6 1: "thành một góc của 3 chủ đề"; VN1 1: "Add text content") | 11 ✓ | 16 ✓ | 16 ✓ | 14 ✗ (VN4 1: "Chào [Tên]": a bare name to a business owner, no anh/chị; "Nhờ một chút" with no object) |

Totals:
- Coach-facing replies pass in **1/4**; last round 0/7. Both kit strings that failed every VG1 run now read right.
- QUAY HÔM NAY passes in **4/4**, and Week-1 posts in **3/4**.
- Messages pass on language in **3/4**, but 3 runs need `[Tên]` removed before sending.
- **Release bar G3 not met**: the critical items VN7 (Tuấn) and VN4 (consultant) are at 1.
- No essay connectors and no banned tells in 4/4.

Lines that still read translated or stiff (D = translated, S = stiff), with a natural version:

1. D · Tuấn T5, from `setup.multi_income`: "Em đoán nên viết cho vợ chồng trẻ đang ở trọ, tính vay ngân hàng mua căn hộ, vì họ
   có thể mua của anh hơn một thứ: căn hộ, rồi hợp đồng che người đứng tên vay."
   - Back-translates cleanly ("they could buy more than one thing from you").
   - Fix: "Em đoán nên viết cho vợ chồng trẻ ở trọ tính vay mua căn, vì nhà đó cần cả căn qua anh lẫn hợp đồng che người
     đứng tên vay. Đúng không anh?"
2. D · coldstart T8: "gối với giấc ngủ là một góc của chủ đề 1". consultant T7: "chuyện nhân sự khác vẫn vào bài
   thành một góc của 3 chủ đề".
   - Both come from the §CM-MAP shorthand "chủ đề họ mê → một góc của ý lớn".
   - Fixes: "gối với giấc ngủ thì mình lồng vô chủ đề 1" · "mấy chuyện nhân sự khác vẫn viết, lồng vô 3 chủ đề đó nghe
     anh".
3. D (guide A14) · coldstart T5: "nên mình kể chuyện của chính bạn, cái tối 9 giờ mùa quyết toán".
   - Fix: "nên mình kể chuyện hồi bạn còn làm kế toán, cái tối 9 giờ mùa quyết toán".
4. S · Hạnh T6 "Em chạy thử 4 tuần nhé." and consultant T6 "Em chạy thử 4 tuần nghe anh."
   - The XƯNG HÔ rule "Câu mẫu đổi theo cặp" swapped the inclusive "Mình" of `map.ok` for "Em". It now sounds as if the
     machine runs the trial alone.
   - Fix: "Mình chạy thử 4 tuần nhé chị." / "Mình chạy thử 4 tuần nghe anh."
5. S (jargon) · coldstart T9, Tuấn T8, consultant T7: "Muốn mình nhắc vào ngày nói chuyện và thứ Sáu không?"
   - Source: `levelup.offer_reminders`. Nobody has told the coach what "ngày nói chuyện" is.
   - Hạnh's run already wrote "Muốn em nhắc vào thứ Hai và thứ Sáu không?". Fix the string the same way (K36).
6. S · the plan line in 4/4: "thứ Hai hằng tuần kể 15 phút cho tuần sau".
   - Better than VG1's "ngày nói chuyện", but telegraphic: who tells whom?
   - Fix: "thứ Hai nào anh cũng kể em nghe 15 phút để em viết tuần sau". No bytes for this now; P3.
7. S · coldstart, the caption (today's text post):

   ```
   Có bạn mua cái ghế công thái học cả chục triệu mà lưng vẫn y chang.
   mà 4 giờ chiều vẫn cứng đơ, vì vấn đề hông phải ngồi sai, là ngồi yên quá lâu
   ```

   - Two "mà" back to back: the câu đầu was glued onto a caption written to stand alone (§CM-FORMATS 7 "câu đầu +
     caption, một khung").
   - Fix for line 2: "4 giờ chiều vẫn cứng đơ như thường, tại hông phải ngồi sai đâu, mà là ngồi yên quá lâu á".
8. VN7 · Tuấn, Facebook long post: "Nói thiệt, mình bán bảo hiểm, mình làm môi giới, mình có nhận hoa hồng."
   - His own Facebook post and his card ("Facebook xưng tui") say "tui".
   - Fix: "Nói thiệt nè, tui bán bảo hiểm, tui làm môi giới, tui có nhận hoa hồng, tui nói thẳng luôn á."
9. S (call-centre) · Tuấn's one-off Zalo to acquaintances: "Không muốn nhận nữa thì nhắn Tuấn chữ DỪNG.", under a title
   line "Tính trước rồi hẵng cọc".
   - §CM-MESSAGES 3 scopes DỪNG to a Zalo **series**; this is one personal message.
   - Fix: drop the title line and end "Chưa cần thì cứ nói Tuấn một tiếng, Tuấn không nhắn nữa nha."
   - Ruling on VG1's open question: a one-off outbound 1:1 gets this human exit line; a series or a list keeps the
     DỪNG line.
10. VN4 · consultant Zalo + inbox: "Chào [Tên], tôi Khoa đây. Nhờ một chút: …"
    - Fix: "Anh ơi, tôi Khoa đây. Nhờ anh một chút: …", with one line above the box: "gửi chị thì đổi 'anh' thành
      'chị'".
11. VN5 · flat endings against the coach's own rate (fixed by K/VK-22):
    - Tuấn: "…mình gửi bạn Tờ tính trước khi cọc." → "…Tờ tính trước khi cọc nha."
    - Hạnh N2: "Không chào thêm gì cả." → "Không chào thêm gì cả các em ạ."
    - Hạnh, the long post's ask: "…chị gửi 3 bước cầm gương nói thật." → "…nói thật nhé :))"
12. S (brochure) · Map line 1, which stacks methods in 4/4 (45–50 tiếng). Example, Tuấn: "…thì tìm Tuấn: tính ngược từ
    tiền góp, để riêng quỹ 6 tháng, che người đứng tên vay chứ không cọc trước tính sau, ra giá căn tối đa rồi mới đi
    coi nhà."
    - Fix: "Vợ chồng trẻ ở trọ nào hay than "sợ gồng lãi" thì tìm Tuấn: tính ra giá căn tối đa rồi mới đi coi nhà, chứ
      không cọc trước tính sau."
    - Not scored below 11/12; P3.

Keep these; they read like a person:
- Hạnh T5: "Dạ được chị, chị cứ ra với khách. Không vội đâu."
- Tuấn T8: "Dạ, câu "view sông" em không viết: căn nhìn ra hồ bơi nội khu, người ta tới coi thấy khác là mất tin."
- coldstart T5: "Chuyện nhỏ bạn thì mình không đưa vô bài: nhỏ là bạn chứ không phải khách, không đo, chưa xin phép, mà lại dính
  tới thuốc giảm đau."
- Hạnh's long post: "Hai kiểu nhìn thì ngược nhau, mà gốc là một."
- Hạnh's inbox 2: "Chưa cần thì em cứ làm 3 bước trước, vướng đâu nhắn chị."
- consultant N1: "Ai quen chủ doanh nghiệp nào sau Tết cũng phải tuyển lại thì gửi họ coi."

## 7. What improved vs the previous round (same 8 personas)

| Measure | G2 / VG1 | G3 / VG2 |
|---|---|---|
| Grader passes | 0/8 | **2/8** |
| Failed checks: real / FP | 13 / 17 | 15 / 5 (2 real are timing-inflated) |
| EN Map ≤6 turns | 1/4 | **4/4** |
| EN film-ready ≤20 | 2/4 (19.1, 20.0, 23.0, 27.3) | **4/4** (17.6–19.3) |
| EN coach turns | 7–8 | 6–7 |
| EN whole card ≤5,700 | 2/4 | **4/4** |
| VN Map ≤7 turns | 3/4 | **4/4** |
| VN coach turns | 8–11 | 7–9 |
| VN film-ready ≤20 | 3/4 | **0/4** (2/4 on one timing convention) |
| Unheard list stored as fact (I8 `list_size=0`) | proof S1 | gone; `list_size=ask` + a visible guess |
| Unsafe consent default | proof S0 "OK'd" | gone ("unsure: no") |
| VN two coach-facing calques | 7/7 runs | **0/4** |
| VN spoken objection argued back | 3/3 | **0/3** (quiet at once) |
| VN two questions in one message (Tuấn) | yes | no |
| VN 1:1: "anh/chị" slash · DỪNG in inbox · "Dạ" chị→em | 1 · 3 · 2 runs | **0 · 0 · 0** |
| VN `[Tên]` in 1:1 messages | 2 runs | **3/4 runs** (worse; VK-7 wording) |
| Early win usable | three quotes, not a post | **a copy box in 8/8, postable as is in 6/8** |
| "Waste of money" voiced at min 15 (proof S1, S0) | 2/2 | 0/2 |

## 8. Prioritised fix list

Budgets now: EN block 6,488/6,500 chars, ship.kit 899/900, method 49,032/51,200 B. VN block 7,495/7,500, ship.kit
923/1,000, method 56,318/56,320 B (anchors ≤3,600). Every VN change below names its cut.
- **VN method net −11 B** → 56,307: +11 +7 −7 −14 −3 −5.
- **VN block +4** → 7,499.
- **EN block −1** → 6,487; ship.kit 898.
- **EN method +9 B** → 49,041.

### Kit

**P1: blocks acceptance**

1. **VK-21. VN cut threshold.**
   - Change: `core/vn/start-block.md` L35 "quá ~1.500 tiếng" → "quá ~1.200 tiếng" (0 chars).
   - Effect: Hạnh is cut after chunk 2 (1,246 dictated), film-ready ≈18.7. All 4 VN runs cut after chunk 2, and none
     after chunk 1 (chunk 1 + posts peaks at 917).
   - This changes a number in the DECISIONS bullet ("VN about 1,500 tiếng"), so it needs the founder's OK.
2. **VK-22. `[Tên]`.**
   - Change: `modules/vn/humanize.md` L32 §CM-NATURAL 4 'không "anh/chị", [Tên]' → 'không "anh/chị", không [Tên]'
     (+7 B).
   - Paid in the same line: "không câu nào cũng có" → "dày như bài họ" (−7 B). This also aims at `vn_natural` (11–26%
     vs 46–64%).
3. **K35 / VK-25. YOUR WORD in the body, not only in the ask.**
   - EN method: `modules/en/plan.md` L11 §CM-WEEK 4 "Keyword once, plus the ask" → "Keyword once in the body, plus the
     ask" (+12 B).
   - EN block, `core/en/ship-check.md` L12:
     - "keyword once + one specific" → "keyword in the body + a specific" (+5);
     - "a stance someone could disagree with" → "a stance someone could dispute" (−6).
   - VN method: `modules/vn/plan.md` L17 "Từ khoá 1 lần + lời mời" → "Từ khoá 1 lần trong bài + lời mời" (+11 B),
     paid by K36.
   - VN block: `core/vn/ship-check.md` L20 "từ khoá 1 lần" → "từ khoá trong bài" (+4 chars).

**P2: real defects in 2+ runs, or language**

4. **K36. The reminder names the day.**
   - VN: `strings/vn.toml` L144 `levelup.offer_reminders` "…nhắc vào ngày nói chuyện và thứ Sáu…" → "…nhắc vào {day} và
     thứ Sáu…" (−14 B, §CM-TODAY).
   - EN: `strings/en.toml` L130 "on talk day and Friday" → "on {day} and Friday" (−3 B).
   - Effect: removes the undefined jargon, and shows a wrong talk-day guess (3/8 this round) at the one moment the coach
     will correct it.
5. **VK-23. `multi_income` calque.**
   - Change: `strings/vn.toml` L271 "vì họ có thể mua của bạn hơn một thứ" → "vì họ cần cả {món này} lẫn {món kia}"
     (−3 B, §CM-SETUP 6).
6. **VK-24. "một góc".**
   - Change: `modules/vn/message.md` L20 §CM-MAP "chủ đề họ mê → một góc của ý lớn" → "chủ đề họ mê → lồng vào ý lớn"
     (−5 B).

**P3: founder calls, or one run**

7. **Founder: the soft cut's "one more story" (Tuấn +5.7 min).** Either:
   - (a) accept film-ready >20 when the coach chooses to keep talking, and grade it as a warning; or
   - (b) ask for a short one:
     - EN `strings/en.toml` L108 "If you have one more story" → "If you have one more short story" (+6; block 6,493).
     - VN `strings/vn.toml` L122 "Còn chuyện nào" → "Còn một chuyện ngắn" (+5). Pay for it with reply 2's "Lộn xộn
       cũng được, để mình sắp xếp." → "Lộn xộn cũng được." (−17; EN has only "Messy is fine.").
8. **EN plan-line jargon:** "talk day {day}" (`strings/en.toml` L258) is as undefined as VN's was.
   - SETUP has 8 B left, so this waits for a SETUP cut. K36 covers the reminder.
9. **Machine slips the kit already covers** (no change):
   - VN coldstart's avoidable second question;
   - consultant VN's 19-tiếng first line;
   - proof S0's "(paste the 3 questions)" in a DM box;
   - Tuấn's DỪNG in a one-off message;
   - "Em chạy thử" (§6, line 4).

### Graders (`evals/graders.py`)

- **G19. I11 (L1630):** skip superlatives inside the coach's verbatim phrase (in a coach turn, or the card's
  `phrases`/`passages`/`written_vs_spoken`). FP in coldstart (3 turns) and consultant VN.
- **G20. I8 (L1454):** digits of rendered kit strings (`setup.plan_guess` "15") are kit tokens. FP in Tuấn.
- **G21. I6 (`DECISION_RE` L224):** "quyết định" in a 3 CHỦ ĐỀ line or a piece is not a decision prompt. FP in
  consultant VN.
- **G22. I9 (L1526):** a quote that matches the coach's words except for one misheard token (folded, edit distance
  ≤1, §CM-SETUP 1) is verbatim. FP in consultant VN ("dứa" → "Rứa").
- **G23. CTA parser (`_ASK_BEFORE` L3511, `cta_keyword` L3402):** "nhắn" right after "tin" is a noun, and an ask needs a
  keyword in caps or quotes after it. FP in consultant VN.
- **G24. "named an email list" (L3594–3598):** in VN, a `list_size` that counts Zalo contacts is not an email list, and
  the Zalo message is the list piece. FP in Tuấn.
- **G25. Piece split (`DAY_TITLE_RE`/`SEP_TITLE_RE` L146–170):** start a piece at a day title whose rest names a
  format anywhere ("the Monday Number (email)"), and at VN "Tin Zalo · thứ Ba…" / "Hỏi 3 khách cũ · …". Misses today:
  consultant EN Fri post; Tuấn's two Zalo pieces merge into N3.
- **G26. Keyword outside the ask in VN:** drop `run.lang == "en"` at L3628. It would catch Tuấn (4 pieces) and
  consultant VN (1). To catch Hạnh's two as well, count a keyword in the ask sentence's lead-in ("Em nào đang ngại
  chào thì comment NGẠI CHÀO") as part of the ask.

### Protocol

- **P12. One timing convention.**
  - Change: `evals/run.py` L249 (COACH.md "Time:"), add "A machine turn's `t_min` is when the reply arrives (the coach's
    turn + about 0.3 min); the coach's reading time goes on their next turn."
  - Why: 3 runs this round (coldstart VN, consultant VN, proof S0) stamped 1.8–2.5 min of reading on the Map reply.
- **P13. Freeze from the first write.** In the packet README (`evals/run.py`), add: "Write each machine turn once;
  never run `grade` or a leak scan on a draft; a draft that used a persona fact stays and fails the run." P9 (a
  separate machine side) is still the real fix.
- **VP-2 / P10.** In COACH.md: "If the dump prompt asks where you post and about your list, and the persona's answer is
  in a later chunk, add it as one sentence at the end of chunk 1." Without this, the up-front ask can never be tested.
  P10's in-budget personas (≤400-word chunks) are still needed for the early win's 4-minute target.
- **Re-run:** Hạnh S1 and Tuấn S1 after VK-21/VK-22, plus one EN coach who says "Shorter" (K27 is still unproven).
  Grade VN keyword placement once G26 lands.
