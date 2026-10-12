# MEASURE · v13.15 fixes · v1315-vn-skip (vn/copywriter-thin, address question skipped)

Grade: FAIL (I15, I23, day0_strategy, day0_shape, hook_lab) and **invalid run: pace**. The pace failure is the simulator's mistake (2 pasted posts timed at 0.7 min, needs ≥1.0); under the protocol coach times are frozen after the first grade, so the run stays invalid. The transcript is still readable for the checks below.

| # | Fix | Result |
|---|---|---|
| 1 | Opener reads natively; after a skip, sensible guess + at most one re-ask; no bare "bạn" mismatch | **Pass.** T1: "Mình nên gọi là anh, chị hay bạn cho tiện?" reads natively. The coach ignored it (deliberate deviation) and again at T3. At T2 the machine guessed "bạn" from context, since there was no name yet: "mình tạm gọi là bạn, xưng mình (mình đoán…)". It re-asked once, softly and without a "?": "Muốn mình gọi anh hay chị thì gõ một chữ là đổi." It never asked again. From T2 to T18 it kept mình–bạn with no switch to chị/em after the name "Nhi" appeared (T4), and no bare "bạn" mismatch. em–chị appears only as address_1to1 in the client Zalo ask, which is correct. |
| 2 | Reply 1 has the short voice tip | **Pass.** "Cứ nói vào micro, khỏi gõ." The Claude-specific mic line and the Mac fn tip came in reply 2, because reply 2's dump prompt was folded into the post-chunk-1 reply after the skip. |
| 3 | Day-0 piece on thin material: ĐĂNG HÔM NAY or one story question; % "Máy tự thêm" ≤30% | **Pass with a caveat.** It printed ĐĂNG HÔM NAY (a long Facebook post), with "Máy tự thêm: đoạn 8, 11, 17, 18, 24, 25" = 6/26 paragraphs = **23%**. Caveat: about 795 tiếng, under the kit's bài dài floor of ≥950. Thin material can't meet both the 950 floor and the ≤30% limit, so the kit has a real tension here. N2 video: 2/7 = 29%, about 305 tiếng (floor 500). |
| 4 | Brand Card shows pack_version=1.3.15 | **Pass** (T17 machine block, line 1). |
| 5 | First line "◆ Content Machine · … · …" consistent | **Pass.** All 18 machine replies have it: setup check, Ngày 0 · …, Hỏi thêm n/6, Bước n/3, ĐĂNG HÔM NAY · …, Brand Card v1, N2 · …. |
| 6 | "kết quả tuỳ người, không phải cam kết" where results appear | **Pass with a caveat.** It is in the Day-0 post (paragraph 7), the card's proof line, and N2 (spoken idea 4 + caption). Caveat: the post's line 2 states the result (1 email → 180 → 1 buyer), and the disclaimer comes 5 paragraphs later. Better to put it near the first mention. |
| 7 | Hooks in a frame | **Pass.** Day 0 uses the "Nếu bạn {đang khổ vì…}, xem cái này" frame: "Nếu bài nào cũng có tim mà không ai hỏi giá, đọc cái này." (14 tiếng; "đọc" in place of "xem" for a text post). N2 uses "Lầm tưởng: {X}. Sự thật: {Y}." The grader flags N2 (see below). |
| 8 | Strategy ≤3 replies each ending on one OK; minutes to Day-0 piece | **Pass.** 3 replies (T13–T15), each with one OK: "'OK' là sang bước 2", "'OK' để lấy B", "Chạy thử 4 tuần… OK hay sửa một dòng?". At most one A/B/C (hours, B recommended). Day-0 piece at **21.0 min**; Brand Card + week at 29.3; N2 at 31.3. |

## Grader fails: real vs misread
- **pace (invalid run): REAL, simulator side.** Pasted posts were under-timed. Not a kit issue.
- **I15 "pronoun chị outside the pair" T2: MISREAD.** "chị" appears only inside the re-ask ("gọi anh hay chị"). The grader should exempt the address question and its one re-ask.
- **day0_strategy, interview 7 questions / "dig.buyer asked twice (T2, T6)": MISREAD.** T2 has no interview question. The match is probably the money line "Muốn ai thành khách…" or the address re-ask. The real interview was 6 questions (T6–T10, T12) plus the NGUỒN ĐỌC A/B/C.
- **day0_strategy, pillar holds a number ("Chuyện nghề với coach 1-1"): MISREAD**, since "1-1" means one-to-one, not a result. Cheap to avoid ("làm riêng").
- **day0_strategy, WHAT I FOUND line without guess label: REAL (minor).** "Chưa đọc được trang nào…" should carry "(mình đoán)" or name what is still a guess on that line.
- **day0_shape, CTA "HỎI GIÁ" ≠ YOUR WORD "không ai hỏi giá": REAL by grader rule, ambiguous in the kit.** §CM-CTA-KIT 1 gives NIỀM TIN/QUAY HÔM NAY a comment word (≥2 tiếng from the hook), but the step-5 ladder and the grader want the season keyword. The kit should say which one applies on Day 0.
- **day0_shape, "Week 1 has no email when coach named a list" (T16): MISREAD.** The T17 table has "T6 16/10 · Email 320 người · xin trả lời, chưa bán". The grader seems to read T16 rather than the week reply.
- **hook_lab, N2 first line fills no frame: MISREAD.** "Lầm tưởng: đọc vài bài là nghiên cứu xong. Sự thật: phải nghe người thật nói." is the kit's frame verbatim. Possibly the two sentences trip the one-sentence check.
- **I23, 0/4 pieces use the coach's phrases: MIXED.** The card phrase "Đó không phải nghiên cứu." is in the Day-0 post and in N2 Ý 1, so the card-phrase parse may be missing it. On the other hand, the pieces don't reuse her written-post openers (W1 style), so a key from voice-samples would rightly fail.

## Other notes
- The dump was abstract and in English. 3 money lines were given in Vietnamese meaning without quotes, so no English reached a post.
- No customer words were collected in 6 questions, so the keyword and ĐIỀU KHÁCH NHỚ are guesses (labelled).
- The coach chose reading access A (browser). With no web lane, the machine said honestly that nothing is connected.
- Small miss: the coach's own gift file was named at "tiếp". The kit says to have it pasted once and used; the machine parked it for Friday's email.
