# MEASURE · v143-vn-day23 · vn/sales-coach (chị Quyên) · v14.3 (HEAD 3cef685)

## Tóm tắt (tiếng Việt)
- **Chạy hết:** Ngày 0 tới card + bảng tuần, rồi "tiếp" ngày 2, 3, 4. Coach không bỏ ngang.
  - Bài đầu ở phút 14,6 (mục tiêu 12, do chị nói một lèo khoảng 6,5 phút).
  - Mỗi ngày sau có bài trong dưới 5 phút.
- **Dòng trạng thái:** 10/10 tin có đủ 2 dòng ("◆ Bước n/10 …" + "Đã có · Còn thiếu"). 10/10 tin kết bằng "TIẾP →". Không có câu kết bị cấm.
  - Ngày 4 vẫn ghi "◆ Bước 9/10": theo kit, "Tuần 1 · Ngày d" chỉ có sau bước 10 (Chủ nhật 18/10), nên founder sẽ không thấy "Tuần 1 · Ngày d" trước ngày 7.
- **Ngày 2:** hỏi chỗ gom (A/B/C) là lời xin duy nhất cạnh bài. Đúng luật. Chị chọn B (Sheet).
  - Lời xin dán file quà bị dời sang ngày 3, đúng "chờ hôm sau".
- **Ngày 3:** nhắc việc (A/B) đi chung với dòng "Cần chị · dán file quà" → **2 lời xin trong một tin**. Kit không cấm ở bước 8, nhưng sát luật "một lời xin".
- **Câu hỏi của ngày:** không xuất hiện ngày 2–3 (vì tin đã có lời xin khác: đúng luật). Lần đầu ở ngày 4, đứng một mình: "Giờ khách mới tìm tới chị từ đâu?".
  - Ô tốn nhất là SẢN PHẨM (offer), nhưng §CM-MEMORY 7 cấm hỏi offer trước tuần 2.
- **Quà:** ngày 0 xin phép kể chuyện chị Trâm trước, rồi hỏi quà ở tin card. Thứ tự đúng v14.3.
- **Dòng lưu card:** một lần, ở "tiếp" đầu (ngày 0). Thiếu dòng dự phòng Zalo "Cloud của tôi".
- **Từ khoá:**
  - Bài NIỀM TIN dùng {WORD} lấy từ hook: SUY NGHĨ, LỊCH HẸN, ĐẮT QUÁ.
  - {KEYWORD} "hỏi giá xong là seen" chỉ nằm ở card và dòng tin Zalo CHUYỂN ĐỔI.
  - Mâu thuẫn ở bài ngày 0: vừa NIỀM TIN vừa "có quà".
- **Độ dài:** video 285 / 286 / 271 chữ, bài dài 547 chữ. Tất cả trong khung.
- **Tiểu từ** (card 35%, cho phép ±10): N1 35%, N2 33%, N3 28%, N4 40%.
- **Grader:** 13 mục FAIL. Lỗi thật: khoảng 9 ý. Lỗi grader đọc nhầm hoặc grader cũ hơn kit: khoảng 12 ý (xem bảng cuối).
- **Rò rỉ:** leak check pass với cảnh báo. Hai chữ nghi lây từ hồ sơ persona: "nhắn lại có cớ" và tên quà ngày 0.

## Per reply: status lines, NEXT, banned endings

| T | Day | Line 1 | Line 2 (Đã có · Còn thiếu) | Last line TIẾP | "?" outside frames | Banned ending |
|---|---|---|---|---|---|---|
| 1 | 0 | ◆ Bước 1/10 · Mở đầu | ✓ hướng dẫn ✓ file phương pháp · Brand Card | ✓ | 1 (xưng hô) | none |
| 2 | 0 | ◆ Bước 2/10 · Nghe + tìm hiểu | ✓ | ✓ (asks for 'xong' though dump ended "xong rồi") | 0 | none |
| 3 | 0 | ◆ Bước 3/10 · Chiến lược | ✓ | ✓ | 1 ("OK hay sửa một dòng?") | none |
| 4 | 0 | ◆ Bước 4/10 · Bài hôm nay | ✓ but bare "trụ cột" (deny_list) | ✓ | 1 (Cần: consent) | none |
| 5 | 0 | ◆ Bước 6/10 · Brand Card + Tuần 1 (steps 5+6 in one reply; "Xong hai bước: ghi bước sau" read as 6) | ✓ offer "(cần trước tuần 2)" | ✓ "Mai quay lại đoạn chat này, nhắn 'tiếp'." | 1 (Cần: gift) | none |
| 6 | 2 | ◆ Bước 7/10 · Chỗ gom mọi thứ | ✓ | ✓ "Gõ A, B hay C…" | 0 | none |
| 7 | 2 | ◆ Bước 7/10 · Cài Google Sheet | ✓ | ✓ | 0 | none |
| 8 | 3 | ◆ Bước 8/10 · Nhắc việc | ✓ | ✓ "Gõ A hay B…" | 0 (2 asks, no "?") | none |
| 9 | 3 | ◆ Bước 8/10 · Cài nhắc việc | ✓ | ✓ | 0 (3 "?" are URL queries) | none |
| 10 | 4 | ◆ Bước 9/10 · Tổng kết thứ Sáu đầu (mai, 16/10) | ✓ | ✓ | 1 (câu hỏi của ngày) | none |

Grader reply_protocol: pass (10/10 status lines). running_tag: pass. Every reply was either "em–chị" or reply-1 "mình–bạn". No nhé/nhỉ/đấy, no "—".

## Questions asked

| T | Question | Kind | Needed? |
|---|---|---|---|
| 1 | "Mình nên gọi là anh, chị hay bạn cho tiện?" | fact (kit fixed) | yes |
| 2 | TIẾP "gõ 'xong'" after the dump already ended "Thôi vậy đó em, xong rồi." | prompt | **unnecessary**: a wasted coach turn. The kit has no rule for "xong" inside the dump. |
| 3 | Ai: A/B (máy khuyên A) · Số giờ: A/B/C (máy khuyên A) · "OK hay sửa một dòng?" | A/B/C ×2 | hours: yes. Who: weak (the dump already said owners and their inbox staff). |
| 4 | Cần · consent to tell chị Trâm (tên, chuyện, câu nói) | fact | yes (style grader: "asks more than one thing") |
| 5 | Cần · "Chị có sẵn quà, file tặng nào chưa?" | fact | yes, the gift ask after consent (v14.3) |
| 6 | Hub A/B/C (máy khuyên B) | A/B/C | yes, step 7, the only ask that day |
| 8 | Nhắc việc A/B + "Cần chị · dán nội dung file quà vào đây" | A/B + fact | yes, but two asks in one reply |
| 10 | "Giờ khách mới tìm tới chị từ đâu?" | fact (câu hỏi của ngày) | yes, alone in the reply |

## Each piece

| Piece | Turn | Length | Hook (tiếng / frame) | On-screen | CTA echoes hook | {WORD}/{KEYWORD} | Particles | Invented facts | "Máy tự thêm" |
|---|---|---|---|---|---|---|---|---|---|
| N1 QUAY HÔM NAY · NIỀM TIN · video | 4 | 285 (grader 287) ✓ | 17 · belief flip, not a literal kit frame (hook_lab flags it) | "0 hợp đồng": adds a number ✓ | ✓ "để chị suy nghĩ" → SUY NGHĨ | WORD ✓ (Day-0 gift, see conflict 1) | 7/20 = 35% ✓ | none (own story, verbatim facts) | "ý 2" ✓ correct (the interpretation of the manager's line) |
| N2 · T3 · THU HÚT · video | 6 | 286 (299) ✓ | 14 · question + "coi lại…" (pain call-out) | "Đừng gửi bảng giá." ✗ repeats "gửi", "giá" | ✓ "tin hỏi giá / tin đầu" → lưu, gửi | none ✓ (THU HÚT) | 7/21 = 33% ✓ | none; the generalization is sourced ("gần như chủ cơ sở nào… cũng nói y chang") | "ý 1, 2, 3, 4": ✓ but over-wide (half of ý 2 is her words) |
| N3 · T4 · NIỀM TIN · bài dài | 8 | 547 (560) ✓ | 12 · real-number result ("14 lên 33") ✓, no client name | n/a | ✓ "lịch hẹn" → LỊCH HẸN | WORD ✓ | 10/36 = 28% ✓ | the result and line are exact, with "Kết quả tuỳ người, không phải cam kết" ✓. Minor: "mình giữ tới giờ" (feeling not said). A causal claim was cut before print. | "đoạn 5, 6, 7" ✓ correct |
| N4 · T5 · NIỀM TIN · video | 10 | 271 (279) ✓ | 15 · "{Việc} khó, cho tới khi…" ✓ literal frame | "Không cần trăm câu.": adds; grader calls it a flat claim | ✓ "đắt quá" → ĐẮT QUÁ | WORD ✓ | 8/20 = 40% ✓ | none; examples labelled "Ví dụ thôi nha" | "ý 3, 4" ✓ |

The gift pages (N1, N3, N4) and inbox replies 1 are built from her method lines. Every gift page repeats "hỏi lại / im / nhắn lại ba lần có cớ", which is the week_dedupe "same idea in 4 posts" hit.

Week 1 table: 7 rows, 4 columns, 4 filmed (3,5 hours = standard), with the long post, the carousel and the Zalo message. THU HÚT 3 · NIỀM TIN 3 · CHUYỂN ĐỔI 1. No email row, although she named 210 never-mailed addresses (a re-permission email would fit §CM-MESSAGES 3).

## "Câu hỏi của ngày" behaviour
- Day 2: none. The hub A/B/C is "lời xin duy nhất cạnh bài" (CONTENT-MACHINE-VN.md:92). ✓
- Day 3: none, because the reply already holds step-8 A/B and the gift-paste Cần. ✓ by the rule "chỉ trong tin không hỏi gì khác" (1-INSTRUCTIONS.txt:25).
- Day 4: one question, alone, story slots already full, so the TÌM TỚI template (§CM-DIG 3). It was not the costliest slot (offer), because offer may not be asked before week 2 (CONTENT-MACHINE-VN.md:28). ✓
- Net: from day 2 the kit's ask-priority (hub > reminders > pending gift > question of the day) pushes the first question of the day to day 4. If the coach had not picked a hub at once, it would slip again.

## Rule conflicts hit (file:line)
1. **{WORD} vs {KEYWORD} on Day 0:**
   - 1-INSTRUCTIONS.txt:22 says QUAY HÔM NAY uses "Comment {WORD}…" and carries a gift.
   - CONTENT-MACHINE-VN.md:222 says {KEYWORD} goes on "bài CHUYỂN ĐỔI, bài có quà".
   - The Day-0 piece is NIỀM TIN *and* has a gift. The machine followed step 4 ({WORD} = SUY NGHĨ).
2. **Reprinting the fixed line vs a reply holding only the piece:**
   - CONTENT-MACHINE-VN.md:13 ("Coach sửa một ý… in lại dòng đó") clashes with 1-INSTRUCTIONS.txt:22 ("riêng một tin") and CONTENT-MACHINE-VN.md:83 ("QUAY HÔM NAY, chỉ nó").
   - The pillar fix went into status line 2, and that line then tripped the bare-"trụ cột" deny rule (CONTENT-MACHINE-VN.md:299).
3. **"Xong hai bước: ghi bước sau":** CONTENT-MACHINE-VN.md:8 is ambiguous for the card + week reply (steps 5+6). The machine printed 6/10.
4. **Status on days 2–4:**
   - 1-INSTRUCTIONS.txt:9 prints "Tuần n · Ngày d" only after step 10.
   - Steps 9–10 follow the calendar (1-INSTRUCTIONS.txt:24, CONTENT-MACHINE-VN.md:42).
   - So Thursday shows "Bước 9/10" for a Friday step. The coach sees the week and day only in the piece header (N4 · thứ Năm).
5. **Gift paste deferral:**
   - CONTENT-MACHINE-VN.md:210 says "Có: dán một lần".
   - CONTENT-MACHINE-VN.md:92 says the hub is the only ask on day 2 and other asks wait.
   - On day 3 the deferred ask lands beside step 8 (CONTENT-MACHINE-VN.md:93), which has no "only ask" clause. Result: two asks.
6. **Costliest slot vs offer:** CONTENT-MACHINE-VN.md:50 (§CM-DIG 2) asks for the costliest guess, while CONTENT-MACHINE-VN.md:28 (offer "không hỏi" before week 2) forbids it.
7. **Sheet rows have no status column:**
   - Level-ups/BOARD-VN.md:92 (print "Trạng thái Đã viết") clashes with Level-ups/BOARD-VN.md:98 (new-post blocks A–F, G–L, M–N leave out Trạng thái in column O).
   - The machine printed M–O.
8. **Two reminder mechanisms:**
   - CONTENT-MACHINE-VN.md:93: "nhắc trên lịch… Rồi link".
   - Level-ups/BOARD-VN.md:126: Claude Scheduled, or the Project-only A/B/C.
   - The machine used Google Calendar links (one pick, no second A/B/C).
9. **"bạn" in the table header:** Level-ups/PLAYBOOK-VN.md:111's header template "niềm tin: bạn nghĩ X → thật ra Y" puts "bạn" into a chị–em chat. The I15 grader flags it.
10. **Two tables on Day 0:** HUB.md's required "Lịch tuần này" table (Level-ups/BOARD-VN.md:39, §CM-HUB-MD 2) plus the card's Week-1 table (CONTENT-MACHINE-VN.md:42 "Kèm card: HUB.md") gives 2 tables. day0_strategy flags it.
11. **"(mình đoán)" marker:** the label is fixed in 1-INSTRUCTIONS.txt:21, but the reply pair is em–chị. The machine wrote "(em đoán)".

## Grader fails: real vs misread

| Check | Evidence | Verdict |
|---|---|---|
| deny_list | T4 "trụ cột" bare | **real** (caused by conflict 2) |
| day0_shape: save line has no backup | T5 | **real** (1-INSTRUCTIONS.txt:30 "Dự phòng: Zalo Cloud của tôi" missing) |
| day0_shape: placeholders | "[dán 1 trang quà]", "[dán 1 trang]", "[CHƯA CÓ]" | **real-minor** (should paste the page or point to it; the card should drop the empty field) |
| day0_shape: email list named, no email in Week 1 | T4 / T5 | **real-minor** (a re-permission email fits) |
| day0_strategy: 1 content pillar | T3 | **real (format)**: the pillar names sat only inside the frame |
| day0_strategy: WHAT I FOUND 1 line | T3 | **real-minor** (≤3 allowed, 2 wanted; nothing was read) |
| hook_lab: N2 on-screen repeats 2 words | T6 | **real** |
| hook_lab: FILM TODAY hook matches no frame | T4 | **real-ish** (a flip, but not the kit wording) |
| week_dedupe: reused sentences N2/N3, N1/N3; method lines in every gift page | T4/T6/T8/T10 | **real** |
| week1_plan: a Week-1 piece reuses FILM TODAY's idea | N4 ↔ N1 | **partly real** (both end on "chị đang cân nhắc chỗ nào nhất") |
| style: Cần asks more than one thing (T4) | consent for tên, chuyện, câu | **borderline** (one consent) |
| I6: 2 decision prompts in T7 | "chọn Chien-dich.csv", "chọn cột A" | **misread** (instructions, not choices) |
| I9 / source_check: quote not verbatim | example line "Dạ chị đang muốn chăm chỗ nào…" | **misread-ish** (a labelled example in quotation marks, inside the Máy tự thêm paragraph) |
| I12: hook 19 words | T5 HUB.md bank line incl. "(Nghe thật)" | **misread** (the hook is 17) |
| I15: "bạn" outside the pair | "2–3 bạn trực page" (noun), PLAYBOOK header "bạn nghĩ" | **misread** / kit template (conflict 9) |
| day0_strategy: 2 open choices (max 1) | T3 | **grader older than kit** (1-INSTRUCTIONS.txt:21 allows ≤3) |
| day0_strategy: strategy with no question first | T3 | **grader older than kit** (v14 "Không phỏng vấn") |
| day0_strategy: Week 1 has no CONVERT | T5 | **misread** (N7 tin Zalo is CHUYỂN ĐỔI; the 4-column chat table has no type column by rule) |
| day0_strategy: 2 calendar tables | T5 | kit-induced (conflict 10) |
| source_check: generalization "ai cũng kể y một chuyện" | T6 | **misread** (she said "gần như chủ cơ sở nào… cũng nói y chang") |
| hook_lab: T8 line 1 "Đăng: thứ Tư…" | T8 | **misread** (the post-date line sits above the frame; the hook is inside it) |
| hook_lab: "Không cần trăm câu." flat claim | T10 | **disputed** (the kit allows "câu phán, lời thách giấu cách làm") |
| vn_natural: 13% overall; T5 "script" 3% | all | **misread** (it counts captions, gift pages, card and HUB as script; per-script counts are 28–40%) |
| week_dedupe: hook repeated T4↔T5, T6↔T8, T8↔T8, "Quà…" labels | bank / Sheet rows | **misread** (HUB bank line and Sheet hook cells repeat the hook by design) |

Warn only: day0_timing (first piece 14.6 > 12; early win 8.4 min after the talk started, because she talked once for about 6.5 min); leaks (19 warnings, see notes.md).
