# MEASURE · v1312-sales · chị Quyên · build v13.12 (HEAD bef1431, packet 9139d78121b7)

Run: Day 0 to the end, then all 7 Week-1 posts (one a day, N1 = the Day-0 video), one Claude Project chat (transcript.md / transcript.jsonl, 24 coach turns, 24 replies).
Tier: coach picked C, **3,5 tiếng → standard**. Posts: **4 filmed** (N1, N3, N4, N6 video) · **3 written** (N2 carousel, N5 bài dài, N7 tin Zalo). Mix 3 THU HÚT / 3 NIỀM TIN / 1 CHUYỂN ĐỔI.
Grade (grades.json): **invalid** on protocol `pace` (my slip: turn 4, two pasted posts modelled in 0.9 min, protocol wants ≥1.0). A scratch copy with only that coach time moved by 0.2 min grades **valid** with the same failures, so nothing else in the protocol fails; `leaks` warn (15 phrase echoes, see end), `research_leaks` pass (11 queries, 0 hits). **pass: false**, 15 checks fail: I8, I9, I11, I15, quit_triggers, day0_timing, day0_strategy, day0_shape, vn_natural, vn_messages, hook_lab, source_check, week_dedupe, style, week1_plan (details at the end).

Pieces measured (7 posts + 2 extras): N1 QUAY HÔM NAY video (+caption, + her gift retyped from her lines) · N2 carousel · N3 video · N4 video · N5 bài dài (+ one-page gift) · N6 video · N7 tin Zalo · extras: inbox replies 1/2 and ask-3 (turn 17).
Sources: T# = coach turn (T3 chunk 1, T4 pasted W1/W2, T5 chunk 2, T6 chunk 3 + typed corrections, T7 offer, T8 proof, T9 find, T10 channels, T12 goal, T13 pillar fix, T15 gift) · card = Brand Card (built only from those) · research = notes.md KEEP lines (used once, as a framing, not quoted: "giá vẫn nói thẳng", N2 trang 7).

## (a) Source trace

The draft marked every machine sentence and the "Máy tự thêm" line was computed from the marks, so every block holding a machine sentence is listed.

### Counts
| Piece | Facts traced (≈) | "Máy tự thêm" paragraphs listed | Added paragraphs NOT listed | Untraceable FACTS | Stretches | Teaching lines phrased as general fact (listed) |
|---|---|---|---|---|---|---|
| N1 video | 27 | 5 (¶6–10) | 0 | 0 | 0 | 1 |
| N2 carousel | 14 | 6 (trang 4, 6, 7, 9, 10, 11) | 0 | 0 | 0 | 0 |
| N3 video | 20 | 5 (¶6–10) | 0 | 0 | 1 | 0 |
| N4 video | 17 | 7 (¶5–11) | 0 | 0 | 0 | 2 |
| N5 bài dài | 18 | 19 of 21 (all but ¶1, ¶5) | 0 | 0 | 1 | 0 |
| N6 video | 12 | 7 (¶5–11) | 0 | 0 | 0 | 1 |
| N7 Zalo | 6 | 3 (¶1–3) | 0 | 0 | 0 | 0 |
| **Total** | **114** | **52** | **0 (target 0: met)** | **0 (target 0: met)** | **2** | **4** |

### Untraceable FACTS: 0
No number, name, scene, client action or quote outside T3–T15. No trap number (200%, gấp đôi, 120 triệu, 199k, 1.000 kịch bản, 30 triệu) and no "lùa gà"; bác sĩ Long never named (N2 says "một phòng khám nha"). Results carry "kết quả tuỳ người, không phải cam kết" (N3, N5, N3 caption). Every number in a piece is the coach's: 10 năm, 3 tháng, 40 phút, 3 năm, 6 chi nhánh, 30 buổi, 112/14 → 98/33, tháng 7/9, 10 → 3, 24 giờ, 41/23, 2 tháng, khóa 3, tháng 6, 38 nghìn, 5 ảnh.

### Stretches (sourced fact bent; inside listed paragraphs)
- N3 ¶7: "Mỗi tuần một chỗ, sửa trên chính tin nhắn thật của spa." applies the class routine (T7) to chị Trâm's case; she said only "Học xong" (T8).
- N5 ¶3: "Anh Tài **mở** trung tâm tiếng Anh" (T6 says "anh Tài trung tâm tiếng Anh ở Biên Hòa"; owner, not necessarily founder).

### Teaching written as a general fact (listed, not facts about her clients, but they read as claims)
N1 "Câu hỏi về chính khách làm khách thấy mình đang được nghe…" · N4 "Lâu dần người giỏi nghề nhất lại là người ngại tư vấn nhất." · N4 "Một khách về nhà thấy mình bị dồn thì không quay lại, lại còn kể cho người khác nghe nữa." · N6 "Người không muốn mua thì đâu cần hỏi đắt hay không, họ im luôn rồi."

### Why so many listed paragraphs
The length floor, again: this coach's usable facts fill ≈250–300 words of a video. N1, N3, N4, N6 reach 500 spoken words only with 5–7 listed teaching paragraphs each; N5 reaches 902 with 19 of 21 paragraphs touched (her Tài story is ≈90 words; the long-post shape asks ≈300 story + 3×150–200 lessons). The v13.12 rule (list every paragraph, no cap) removes v13.9's "unlisted" problem but makes the list long: in N5 the list covers almost the whole post, so it no longer tells the coach which parts are hers.

### Traced, by piece (main facts)
- N1: bảo hiểm nhân thọ, 10 năm, 3 tháng 0 hợp đồng, quán cà phê, 40 phút quyền lợi, "để chị suy nghĩ", chặn số, khóc trong xe, câu quản lý (T3) · spa/nha khoa/trung tâm tiếng Anh/gym, câu seen là câu nghe nhiều nhất, câu suy nghĩ là câu thứ hai (T3) · nói thật / câu chưa dám hỏi (T5, W1) · bỏ nói một mạch, hỏi trước, mấy đứa nhỏ, lo nhất, rồi mới ký (T3) · "Dạ chị đang cân nhắc chỗ nào nhất ạ?", hỏi xong thì im, đừng gửi ưu đãi (W1) · nhắn ba lần mang theo, "chị ơi…" (T6) · quay trong xe (T6) · gift name, một trang (T15).
- N2: "gần như chủ cơ sở nào… y chang" (T3) · lễ tân nha khoa, giá niềng, bảng giá, seen (T6 + typed fix) · tin đầu hỏi một câu (T6, W2) · bảo hiểm câu hỏi (T3) · hỏi trước báo giá sau, cân nhắc chỗ nào, nhắn lại, "chị ơi…" (T6) · trực page (T6).
- N3: chị Trâm, spa Thủ Đức, đưa điện thoại, trang tin seen, câu "như đi năn nỉ" (T6) · 112/14 tháng 7, 98/33 tháng 9, sổ lịch hẹn, cho kể tên và số, câu "tụi nhỏ nhà em không còn sợ nữa" (T8) · lớp: tuần 1/2/4, 5 ảnh chat che tên, chữa từng cái, đóng vai (T7).
- N4: 3 năm quản lý tư vấn, chuỗi 6 chi nhánh, cái ghét nhất, ép thẻ, khách nằm trên giường, chào thẻ 30 buổi, ký đại, đòi hoàn tiền, lên mạng chửi, doanh số đẹp/mất khách, chốt không phải ép, hội thảo 0 đồng ở khách sạn, ép lên khóa đắt, khóc kể đổi đời, ghét lắm (T5) · câu seen (T3).
- N5: anh Tài, trung tâm tiếng Anh Biên Hòa, học thử, học phí, "để anh về bàn với vợ", mất (T6) · khóa 3, 10 → khoảng 3, gọi lại trong 24 giờ, hỏi bé thích gì trước rồi mới nói học phí, 2 tháng sau 41/23, cho dùng, không tên trung tâm (T8) · hỏi trước báo giá sau, nhắn ba lần (T6).
- N6: video tháng 6 "khách nói đắt quá thì nói gì", khoảng 38 nghìn, có người nhắn (T9) · đánh trận, trăm câu, sai, nhân viên đọc kịch bản như máy, khách biết liền, "đắt quá" là câu hỏi (T5) · TikTok khách nói A đáp B (T10).
- N7: Quyên, dạy chốt sale cho chủ cơ sở nhỏ (T3) · 3 câu khách (T3, T5) · DỪNG (kit).
- Extras: inbox 2 class line (T7: 6 tuần, thứ Ba 8 giờ, 5.900.000đ, tối đa 2 nhân viên; khai giảng T12) · ask-3 to chị Trâm, anh Tài (T8).

## (b) Repeats across the week
| Repeat | Where | Kit limit | Verdict |
|---|---|---|---|
| Copied sentence (≥5 words, exact) across posts | none (script check over all 7) | "không chép câu" | **0 (target 0: met)** |
| "Kết quả tuỳ người, không phải cam kết nha." | N3, N5 | required line | allowed |
| "hỏi trước, báo giá sau" (method line, verbatim) | N2 trang 7, N5 lesson 2 | belief ≤2/week | 2: OK |
| Same-format paraphrase, videos: "hỏi (khách) trước" line | N1 ¶7, N4 ¶11, N6 ¶8 | "nói khác đi… cùng dạng = lặp" | **1 group (3 videos)** |
| Same-format paraphrase, videos: example device "Giả sử / Ví dụ khách hỏi…" | N1 ¶7, N4 ¶11, N6 ¶8, ¶9 (+ N5 ×3) | each piece its own example | **1 group** |
| Same-format paraphrase, videos: "nhắn lại có một thứ / có lý do" | N1 ¶9, N3 ¶9 | same | **1 group** |
| Hooks | N1 call-out · N2 "đang mất khách" · N3 receipt · N4 "đang mất khách" · N5 client scene · N6 "cho mình một phút" | "không hai hook mở giống nhau" | N2 and N4 share the frame (different formats) |
| Stories | N1 bảo hiểm · N2 lễ tân nha khoa · N3 Trâm · N4 chuỗi spa + hội thảo · N5 Tài · N6 TikTok tháng 6 | one story, one post | distinct |

Ideas reused across formats (allowed 2–3 posts): "để chị suy nghĩ = nói thật" N1, N2 trang 8, N5 (3) · "đừng nhắn 'chị ơi… tới đâu rồi'" N1, N2 (2, + N5 gift) · "nhắn lại phải mang theo một thứ" N1, N2, N5 (3) · bảo hiểm "mấy đứa nhỏ" N1, N2 (2) · "hỏi trước" as an idea N2, N4, N5, N6 (+N1) = **5 posts, over the 2–3 allowance** (it is the method; the verbatim line stays at 2).
Grader week_dedupe fails on fuzzier pairs: N1 seen line ~ N3 Trâm's quote; N1 gift text ~ N2 trang 8 and N4 ("chốt sale không phải là ép"); the HUB.md box and N7 counted as pieces; N5 vs its own gift page.

## (c) Style
| Piece | Em dash | Pet phrase | Asks | Sentences ending in a particle (my count, broad list) |
|---|---|---|---|---|
| N1 | 0 | "nói thiệt" ×1 | 1 (comment SUY NGHĨ) | 8/40 (20%) |
| N2 | 0 | none | 1 (lưu, gửi) | 2/22 (9%) |
| N3 | 0 | "nghe hoài luôn á" ×1 | 1 (comment LỊCH HẸN) | 4/39 (10%) |
| N4 | 0 | "nói thiệt" ×1 | 1 (lưu, gửi) | 5/47 (10%) |
| N5 | 0 | "y chang" ×1 | 1 (comment BÀN VỚI VỢ) | 2/66 (3%) |
| N6 | 0 | "nói thiệt" ×1 | 1 (lưu lại) | 6/45 (13%) |
| N7 | 0 | none | 1 (nhắn lại A/B/C) | 1/7 (14%) |
- Em dash: 0 in the whole transcript. Northern particles (nhé, nhỉ, đấy): 0.
- Pet phrase ≤1 per piece, never the same one in two posts in a row: held.
- Asks: exactly 1 per post. "?" outside a piece ≤1 in every reply (I5 pass).
- Particles: **far under the card**. Card says ~40%; grader vn_natural: 9/170 sentences (5%); my broader count 3–20% per post. Same failure as v13.9 (11%), worse. The added teaching paragraphs are written in flat "written" Vietnamese and pull the ratio down.
- Cần lines: 2 (turn 16 gift text; turn 20 "ba câu hỏi… là ba câu nào?"). Each asks one thing in my reading; grader `style` counts both as >1 ask because of the kit's own tail "(em không đoán bừa; gõ "bỏ qua" cũng được)". Lines with >1 ask by my count: **0**; by the grader: 2.

## (d) Lengths vs founder rules
| Piece | Words | Rule | Verdict |
|---|---|---|---|
| N1 video | 538 in the box, 503 spoken | short video 500–800 | at the floor, with 5 listed paragraphs |
| N2 carousel | 12 trang, 220 words | 10–12 trang, ≤40 tiếng/trang | OK |
| N3 video | 534 / 502 spoken | 500–800 | at the floor, 5 listed |
| N4 video | 536 / 503 spoken | 500–800 | at the floor, 7 listed |
| N5 bài dài | 902 | ≈1.000 (kit floor 900) | **≈100 short of 1.000**, floor met with 19 listed paragraphs |
| N6 video | 539 / 505 spoken | 500–800 | at the floor, 7 listed |
| N7 tin Zalo | 93 tiếng | ≤150 | OK |
| Inbox 1 / 2 / ask-3 | 40 / 70 / 50 | Zalo length | OK |
Format variety over the 7: video ×4, carousel, bài dài, tin Zalo = **4 formats** (≥4 ✓); no format 3 times in a row (N3, N4 videos, then N5) ✓. Every length-ruled piece lands at its floor; the floor, not the coach, sets how much the machine writes.

## (e) Minutes
- **Day-0 piece (QUAY HÔM NAY) at 27.0 active minutes** (strategy tin 1 at 19.9, last OK at 26.7). Promise "~35 phút": met; quit trigger "30 phút chưa có gì đăng được": 3 min to spare.
- Brand Card + Week 1 at 31.2 active min (56.2 incl. 25 min away filming).
- Coach minutes for the week: chat ≈ 48 active min (Day 0 31.2 + Tue 3.8 + Wed 3.8 + Thu 9.2) + production per §CM-CALENDAR 2 (4 videos có dựng ≈30 each = 120, carousel 15, bài dài 10, Zalo 5 = 150) = **≈198 min ≈ 3 h 18**, of which the Week-1 posts after Day 0 ≈ 2 h 47. Tier promise: standard ≈3,5 tiếng (calendar math "≈3 tiếng"): **inside the promise**. Not counted: the 15-min weekly talk (starts week 2) and Friday numbers (not played).
- Grader day0_timing: 23 coach turns in one session (Week-1 turns counted), 50.6 active session minutes (max 45), early win at 20.9 min after the dump (the 3 lines came at turn 3, but the grader reads the strategy as the early win).

## (f) v13.11/12 checks
| Check | Result |
|---|---|
| Day-0 asks per reply | ≤1 "?" and ≤1 decision in all 17 Day-0 replies (I5, I6 pass) |
| Strategy replies each end on one OK | tin 1 "'OK' là lấy cả tin này, kênh lấy A", tin 2 "Gõ A, B hay C… hoặc 'OK' để lấy B", tin 3 and the gift fix "OK hay sửa một dòng?": ✓ (grader item passes) |
| Browser question alone | turn 10: the read-access A/B/C alone in its reply ✓ |
| Card reply: one ask + one NEXT | turn 17: no Cần line, the only ask is TIẾP "Mai quay lại đoạn chat này, nhắn 'tiếp'." ✓ (save line is an instruction) |
| Hooks: frame fit | 5/7: N1 call-out ✓, N2 "đang mất khách (và cách sửa)" ✓, N3 receipt ✓, N4 "đang mất khách" ✓, N6 "cho mình một phút" ✓; N5 opens on a client scene ✗ (grader hook_lab agrees); N7 Zalo title is no frame |
| Hooks: method hidden | 6/6 hooks hide the how (N2 names the mistake, not the fix) ✓ |
| Hooks: mình/tôi voice | 7/7; no "chị" self-reference in any piece ✓ |
| Hooks: insider detail (PRINCIPLES 3) | N3 names "chị Trâm" + 14/33, N5 names "anh Tài": 2 hooks too specific ✗ |
| Thumbnail 2–4 words | N1 "Khách đang nói thật" 4 · N3 "14 lên 33" 3 · N4 "Đừng ép thẻ" 3 · N6 "Không phải từ chối" 4: length 4/4 ✓; adds to the title 2/4 (N1 repeats "khách… nói", N3 repeats the numbers ✗, grader agrees) |
| CTA: {WORD} on TRUST | N1 SUY NGHĨ, N3 LỊCH HẸN, N5 BÀN VỚI VỢ, each from its hook, each with its own payoff ✓ |
| CTA: save/send on ATTRACT | N2, N4, N6 ✓ |
| No offer in Week 1 | posts: none ✓ (N7 asks a reply only); inbox reply 2 gives the class and price only to someone who writes "muốn học" |
| ≥1 in 4 save/send only | 3/7 ✓ |
| 40/40/20 | 3/3/1 = 43/43/14 (≈3/3/1 the kit's weekly reading) ✓ |
| "bạn" to the coach | 4× in turn 1 (the kit's scripted reply 1, before xưng hô is chosen); 0 after ✓. "bạn" in pieces = staff ("bạn trực page"), not the coach |

## (g) v13.9 → v13.12
| Measure | v13.9 (v139-sales) | v13.12 (this run) |
|---|---|---|
| Grade | valid, pass false, 12 checks fail | **invalid (pace, my 0.1-min slip; valid when fixed)**, pass false, 15 checks fail |
| Week-1 posts | 5 (3 video, bài dài, Zalo) | **7** (4 video, carousel, bài dài, Zalo) |
| Tier / filmed vs written | 3,5 h, kept "khởi động nhẹ" shape | 3,5 h standard: 4 filmed / 3 written |
| Untraceable FACTS | 2 | **0** |
| Added lines/paragraphs not listed | 27 lines | **0** (52 paragraphs listed) |
| Stretches | 4 | 2 |
| Copied sentences across posts | 2 (one exact, one near-exact ×3) | **0** |
| Same-format paraphrase groups | 3 (example device, method line, opener shape) | 3 (example device, "hỏi trước" line, "nhắn lại có lý do") |
| Em dash | 0 | 0 |
| Particles (grader) | 11% vs card 35% | **5% vs card 40%** (worse) |
| Pet phrase ≤1 per piece | held | held |
| Asks per post | N1 had 2 | 1 in every post |
| Cần lines >1 ask | 1 (by both counts) | 0 by my count; 2 by grader (kit tail) |
| Lengths | videos 505–515, bài dài 892 (short) | videos 502–505 spoken, bài dài 902 (floor met, ≈1.000 not) |
| Minutes to Day-0 piece | 28.6 | **27.0** |
| Week coach time | not measured | ≈3 h 18 incl. Day 0, inside standard ≈3,5 h |
| Hooks in a frame | N2, N3, N5 failed hook_lab | N5 fails; on-screen text repeats the title in N1, N3 |
| Strategy | copy box in tin 2 flagged; pillars narrow | ends on OK each step ✓; WHAT I FOUND "nói ngược" line unlabelled; pillar "Tin nhắn đầu tiên" judged narrow |
| Research | 0 KEEP (1 place) | 1 KEEP (2 people, 2 hosts: Voz, Otofun) + 1 counter-line; research_leaks pass |
| Leaks | warn (3 echoes) | warn (15 echoes, all of answer-bank lines the coach did say at T7–T10; grader reads them as undictated) |

## Grader failures, short
- I8: "1 N", "3 N" (HUB.md "3 việc tiếp theo" numbering) and pack_version "1.3.10" (the kit's own card field) not in allowed_numbers.
- I9: tuyến name "Tin đầu, sửa lại" in quotes read as a quote not in sources (it is a name, kit asks for names "bằng chữ của coach").
- I11: "đổi đời" in N4 (her chunk-2 words "khóc kể đổi đời"), matched as a banned claim.
- I15: "mình" in turn 17 (the inbox replies and HUB written in the coach's voice) read as breaking the chị–em pair; "that" in turn 19 (grader).
- quit_triggers: 829 words before the first copy box (the interview + strategy turns; the 3 lines at turn 3 are not counted as usable).
- day0_timing: Map has 5 labelled lines (no "HỆ THỐNG" label: it is "KÊNH VÀ NHỊP"); 23 coach turns, 50.6 min (Week-1 turns in the same session count); early win timing.
- day0_strategy: "Nói ngược" WHAT I FOUND line without a source/guess label; pillar "Tin nhắn đầu tiên" narrow; N2 title has "12 trang", not a word count.
- day0_shape: CTA keyword read as "chị ơi" (matched inside the quoted "chị ơi chị suy nghĩ…" line); "Week 1 has no Zalo message" (N7 is in the table; grader false); card top/save line flagged at the wrong turn (the card top is outside the box and the save line has the app route + Zalo backup); FILM TODAY's text version lacks HỎI GIÁ XONG outside the ask (it is only in the script body, not caption/line 1: real miss).
- vn_natural: particles 5% vs 40% (real miss). vn_messages: "anh/chị" slash in inbox replies (real miss: pick one address).
- hook_lab: on-screen text repeats the title (N1, N3); N5 line 1 not a frame (real misses).
- source_check: wants "¶n" style and counts paragraphs differently (it sees "Giả sử" in N1 ¶3 unlisted; in my numbering, which counts the screen-text and first-frame lines, it is ¶7, listed); N5's "Máy tự thêm" line printed after the gift box, so the grader pinned it to the 7-line gift (real print slip).
- week_dedupe: fuzzy pairs above. style: the two Cần lines (kit tail). week1_plan: reads the hours as the recommended B (2,5 h) though the coach picked C (3,5 h): grader misread.
