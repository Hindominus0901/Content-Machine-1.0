# Content Machine v14.3 · Reviewer chấm mù (6 bài VN)

## Tóm tắt (tiếng Việt)

- Build: `python3 tools/build.py --edition vn` ở HEAD 3cef685, chạy sạch. Bài: `qa/runs/v143/BLIND-PIECES.md` (6 bài, 2 bài mỗi coach: chị Quyên, Nhi, anh Duy; mỗi người 1 video ngắn + 1 bài dài).
- Người viết làm đúng cm-writer.md và có chạy lượt giọng, đếm chữ trước khi nộp (lần đầu tiểu từ thiếu ở 4/6 bài, B-bài dài thiếu chữ; đã sửa trước khi nộp). Sau lượt đó độ dài cả 6 bài đều trong khung, tiểu từ đều trong ±10 điểm so với Card, từ khoá mùa đúng luật, dòng an toàn (sức khoẻ, kết quả) đủ ở bài của anh Duy.
- Reviewer (cm-reviewer.md, chỉ đọc bài + đầu vào coach): **20 cờ** trên 6/6 bài (4 HARD STOP, 16 FIX), gồm 3 cờ cấp tuần. Không bài nào PASS.
- Giám khảo đếm **20 lỗi thật**: reviewer bắt đúng **18** · sót **2** (cả hai nhẹ: chuyện trong B-bài dài ngắn hơn khung ≈150–200; dòng "Máy tự thêm: không" in ra trong khi luật nói không có thì bỏ dòng) · báo nhầm **2** ("quan trọng nhất" là ý chính Nhi nói trong lời xả; chữ ký "Nhi" sau lời mời là cách Nhi kết bài thật của chị). Precision 18/20 = 90%, recall 18/20 = 90%.
- Lỗi thật của người viết chủ yếu là **dữ kiện bị kéo dãn** (9/20: tần suất "ngày nào cũng", "bất cứ bài nào", "mấy lần cũng không sao"; chi tiết thêm vào chuyện coach; nhân quả dinh dưỡng anh Duy chưa nói), rồi **câu lặp giữa hai bài cùng coach** (3), **tiếng Anh lọt** (2), **hook video ngắn** (2), dòng "Máy tự thêm" sai/thiếu (3), lời mời không khép đúng món bài hứa (1).
- Mức nặng: 4 HARD STOP của reviewer đúng theo định nghĩa trong cm-reviewer.md (khái quát hay tần suất coach chưa nói = dữ kiện), nhưng cả 4 sửa được bằng cách cắt một câu; giám khảo xem là đúng luật, hơi nặng tay trên thực tế.
- Giới hạn: cùng một mô hình đóng cả ba vai (viết, soát, chấm), nên lần "đọc mới" không độc lập thật; tỷ lệ bắt lỗi nhiều khả năng cao hơn khi reviewer là một phiên khác. Không có Ledger tuần, khung viết từng bài, dòng nghiên cứu GIỮ, nên reviewer bỏ check 7 và không xét được luật "chưa mời mua trước tuần 2" cho C-bài dài.

---

## Bước 2 · Kết quả của reviewer (cm-reviewer.md, đọc một lần)

not given: khung viết của từng bài (bỏ check 7) · Ledger tuần (giới hạn thật lấy từ phần sản phẩm anh Duy gửi) · dòng nghiên cứu GIỮ · số tuần của từng bài (không xét luật mời mua trước tuần 2)

A-video · 1 Invented facts · "Có chủ spa còn kể dưới video của mình" · Bình luận "nhân viên em mới 19 tuổi" nằm dưới bài "3 tháng đầu bán bảo hiểm", không phải dưới video · FIX
A-video · 1 Invented facts · "Gửi bảng giá thì người mới làm được liền á." · Câu suy luận không có trong lời chị Quyên hay bình luận, mà đoạn Ý 1 không nằm trong dòng Máy tự thêm · FIX

A-bài dài · 1 Invented facts · "Khách lo gì, khách cần gì, mình chưa hỏi câu nào." · Thêm chi tiết vào chuyện của chị; bài chị viết chỉ nói nói một mạch 40 phút rồi bị chặn số · FIX
A-bài dài · 1 Invented facts · "Buông thì mất khách, dồn thì khách sợ." · Nhân quả máy tự nói, đoạn 7 không có trong dòng Máy tự thêm · FIX
A-bài dài · 1 Invented facts · "Nhắn kiểu đó thì nhắn lại mấy lần cũng không sao hen." · Khẳng định về số lần nhắn chị chưa nói; chị chỉ nói "Nhắn lại thì được, mà phải có cớ" · HARD STOP
A-bài dài · 1 Invented facts · "Máy tự thêm: đoạn 10" · Đoạn 10 là lời mời; đoạn dạy máy tự mở rộng là đoạn 9, đoạn 7 thì thiếu · FIX

B-video · 1 Invented facts · "ngày nào cũng phải đào trong nghiên cứu" (caption: "nghiên cứu là việc ngày nào cũng làm") · Nhi chỉ nói "thường phải làm với nhiều nghiên cứu", không nói ngày nào cũng · HARD STOP
B-video · 6 Vietnamese naturalness · "Mình là copywriter" · Chữ tiếng Anh ngoài tên nền tảng trong bài tiếng Việt · FIX
B-video · 3 Claims · "quan trọng nhất" · Chữ "nhất" phải viết lại hoặc có nguồn · FIX

B-bài dài · 1 Invented facts · "ba câu "vì sao" mình hỏi coach trước khi viết bất cứ bài nào" · Thói quen "trước bất cứ bài nào" Nhi chưa nói; chị chỉ nói hay hỏi lại "vì sao" khi coach than không có khách · HARD STOP
B-bài dài · 6 Vietnamese naturalness · "marketing", "podcast" · Chữ tiếng Anh ngoài tên nền tảng · FIX
B-bài dài · 8c Ask · "Comment TRƯỚC BÀI ĐĂNG là mình gửi ba câu "vì sao"" · Món gửi không phải điều bài này hứa và dạy (bài nói về lời đề nghị và một email cho một người); ba câu vì sao không có trong bài · FIX
B-bài dài · 9 Endings · "Nhi" · Bài không kết ở lời mời, còn một dòng sau đó · FIX

C-video · 8b Hooks · "Điều mình hay nghe: muốn bớt ký thì bỏ cơm trắng. Thật ra hơn 60 người văn phòng mình kèm, mình chưa bắt ai bỏ cơm trắng." · Hai câu khoảng 28 tiếng, quá dài cho câu nói đầu video ngắn (≤18 tiếng), lặp "bỏ cơm trắng" · FIX
C-video · 8b Hooks · "cơm vẫn ăn." · Chữ trên màn hình nói lại đúng ý Y của câu đầu, không thêm gì · FIX
C-video · 1 Invented facts · "mà đâu phải tại ăn nhiều cơm" · Anh Duy nói "tại mình đâu có ăn nhiều", không nói gì về cơm; chi tiết thêm vào chuyện của anh · FIX

C-bài dài · 1 Invented facts · "Ăn ít buổi trưa đâu có làm cả ngày ăn ít đi." · Nhân quả dinh dưỡng anh Duy chưa nói, đoạn này không nằm trong dòng Máy tự thêm · HARD STOP

Tuần · 8e Week · A-video "Ba tháng đầu đi bán bảo hiểm, mình không ký được hợp đồng nào" / A-bài dài "3 tháng đầu mình không ký được hợp đồng nào" · Câu gần như y nguyên ở hai bài · FIX
Tuần · 8e Week · "Giả sử bạn dạy tiếng Anh cho người đi làm." · Cùng một câu, cùng một ví dụ ở B-video và B-bài dài · FIX
Tuần · 8e Week · "Gọi cơm văn phòng thì thêm một phần đạm với một phần rau, cơm nửa chén thôi, bỏ nước ngọt, đổi trà đá không đường." · Cùng một câu ở C-video và C-bài dài · FIX

read: 6 · pass: 0 · flagged: 6

---

## Bước 3 · Giám khảo chấm độc lập

Đo lại từng bài (đếm theo tiếng; video tính câu đầu tới lời mời; tiểu từ cuối câu đếm tay, "đó" chỉ trỏ không tính):

| Bài | Chữ | Khung | Tiểu từ / Card | Hook theo khung | Lời mời khép hook | Từ khoá | Dòng an toàn |
|---|---|---|---|---|---|---|---|
| A-video NIỀM TIN | 352 | 250–400 ✓ | 9/24 = 38% / 40% ✓ | "nếu bạn {khổ}, coi cái này" ✓ | KHÁCH SEEN, chung chữ "seen" ✓ | không HỎI GIÁ ✓ | không cần |
| A-bài dài THU HÚT | 542 | 500–700 ✓ | 11/31 = 35% / 40% ✓ | ✓ (16 tiếng) | gửi bài, lý do từ hook ✓ | không ✓ | không cần |
| B-video THU HÚT | 302 | ✓ | 2/23 = 9% / 15% ✓ | ✓ (18 tiếng) | lưu, chung "từ khoá" ✓ | không ✓ | không cần |
| B-bài dài NIỀM TIN | 516 (+ "Nhi") | ✓ | 3/39 = 8% / 15% ✓ | ✓ (18 tiếng) | chữ comment lấy từ hook ✓, món gửi lệch (xem dưới) | không ✓ | không cần |
| C-video NIỀM TIN | 324 | ✓ | 4/19 = 21% / 25% ✓ | lật niềm tin ✓, mà dài | CƠM TRẮNG ✓ | không ĂN ĐỦ ✓ | "không thay cho bác sĩ, chuyên gia" ✓ |
| C-bài dài CHUYỂN ĐỔI | 570 | ✓ | 7/40 = 18% / 25% ✓ | ✓ (17 tiếng) | DM + hạn thật ✓ (chung chữ "ăn", hơi yếu) | ĂN ĐỦ 1 lần thân bài + lời mời ✓ | kết quả tuỳ người ✓, bác sĩ ✓, giới hạn 15 người có lý do ✓ |

Lỗi thật giám khảo thấy, đối chiếu với reviewer (TP = reviewer bắt đúng · MISS = reviewer sót · FA = reviewer báo nhầm):

| # | Bài | Lỗi thật (giám khảo) | Loại | Reviewer | Mức reviewer / ý giám khảo |
|---|---|---|---|---|---|
| 1 | A-video | "dưới video" đổi chỗ bình luận (thật ra dưới bài bảo hiểm) | dữ kiện | TP | FIX / đồng ý |
| 2 | A-video | "Gửi bảng giá thì người mới làm được liền á" suy luận, đoạn không được liệt kê | dữ kiện, Máy tự thêm | TP | FIX / đồng ý (nhẹ) |
| 3 | A-bài dài | "mình chưa hỏi câu nào" thêm vào chuyện của chị | dữ kiện | TP | FIX / đồng ý |
| 4 | A-bài dài | "Buông thì mất khách, dồn thì khách sợ" nhân quả tự thêm, đoạn 7 không liệt kê | dữ kiện, Máy tự thêm | TP | FIX / đồng ý |
| 5 | A-bài dài | "nhắn lại mấy lần cũng không sao" vượt luật của chị | dữ kiện (tần suất) | TP | HARD STOP / đúng luật, thực tế là cắt một câu |
| 6 | A-bài dài | "Máy tự thêm: đoạn 10" chỉ sai đoạn (10 là lời mời) | Máy tự thêm | TP | FIX / đồng ý |
| 7 | B-video | "ngày nào cũng" (lời đầu + caption) kéo dãn từ "thường" | dữ kiện (tần suất) | TP | HARD STOP / đúng luật, thực tế là sửa một chữ |
| 8 | B-video | "copywriter" tiếng Anh trong bài VN | giọng | TP | FIX / đồng ý |
| 9 | B-bài dài | "trước khi viết bất cứ bài nào" thói quen Nhi chưa nói | dữ kiện (tần suất) | TP | HARD STOP / đúng luật |
| 10 | B-bài dài | "marketing", "podcast" tiếng Anh | giọng | TP | FIX / đồng ý (nhẹ; chữ mượn phổ biến, nhưng luật người viết chỉ cho tên nền tảng) |
| 11 | B-bài dài | món gửi "ba câu vì sao" không phải điều bài này dạy | lời mời | TP | FIX / đồng ý |
| 12 | B-bài dài | phần chuyện chỉ ≈110 chữ, khung bài dài cần ≈150–200 (tổng vẫn đủ 500 nhờ bài học) | độ dài từng nhịp | MISS | reviewer chỉ đếm tổng |
| 13 | C-video | câu đầu 2 câu ≈28 tiếng, quá ≤18, lặp "bỏ cơm trắng" | hook | TP | FIX / đồng ý |
| 14 | C-video | chữ màn hình "cơm vẫn ăn." nói lại ý Y của câu đầu | hook | TP | FIX / đồng ý |
| 15 | C-video | "đâu phải tại ăn nhiều cơm" kéo lời anh Duy | dữ kiện | TP | FIX / đồng ý |
| 16 | C-bài dài | "Ăn ít buổi trưa đâu có làm cả ngày ăn ít đi" nhân quả dinh dưỡng tự thêm, không liệt kê | dữ kiện | TP | HARD STOP / đúng luật (niche sức khoẻ, nên nặng là hợp lý) |
| 17 | C-bài dài | in "Máy tự thêm: không" trong khi luật: không có thì bỏ dòng | Máy tự thêm (định dạng) | MISS | rất nhẹ, không có check nào của reviewer chỉ đúng chỗ này |
| 18 | Tuần A | câu "3 tháng đầu… không ký được hợp đồng nào" gần y nguyên ở 2 bài | lặp tuần | TP | FIX / đồng ý (nhẹ, câu gốc từ bài chị viết) |
| 19 | Tuần B | "Giả sử bạn dạy tiếng Anh cho người đi làm." y nguyên ở 2 bài | lặp tuần | TP | FIX / đồng ý |
| 20 | Tuần C | câu cách gọi cơm văn phòng y nguyên ở 2 bài | lặp tuần | TP | FIX / đồng ý (nhẹ, là chữ phương pháp của anh Duy) |

Báo nhầm (FA):
- B-video "quan trọng nhất": đây là ý Nhi nói trong lời xả ("the most important thing is to understand the client from their own point of view"), đặt là "mình thấy", không phải lời khẳng định về thị trường; có nguồn sẵn nên không cần viết lại.
- B-bài dài, chữ ký "Nhi" sau lời mời: bài Facebook Nhi dán (W1) kết đúng bằng chữ ký này; lời mời vẫn là câu cuối của thân bài. Check 9 nhắm vào câu kết kiểu chào mời và dòng gửi coach, không nhắm vào chữ ký.

Những gì giám khảo kiểm và thấy sạch (reviewer cũng không gắn cờ, đúng): độ dài 6/6 trong khung; tiểu từ 6/6 trong ±10 điểm, không trộn nhé/nha, không chồng tiểu từ; không dấu — ; xưng hô giữ một cặp từ đầu tới cuối ở cả 6 bài; từ khoá mùa (HỎI GIÁ, KHÔNG CÓ KHÁCH, ĂN ĐỦ) không lọt vào bài THU HÚT hay NIỀM TIN, ĂN ĐỦ đúng một lần ở thân bài cộng lời mời trong bài CHUYỂN ĐỔI; chữ comment xuất hiện ở lời mời (và dòng mời của caption, đúng bảng từ khoá); lời mời khép hook ở 6/6 theo luật chung chữ; không tên người thật trong bình luận chị Quyên dán, không dùng câu cài lệnh trong bình luận, không dùng "200%" hay "120 triệu"; chuyện chị Hạnh dùng đúng phần được phép (tên, hai câu nhắn, quần tây; không số ký, không hình); giá, giới hạn 15 người kèm lý do, ngày khai giảng và giờ chốt khớp đầu vào (2/11/2026 là thứ Hai, 29/10/2026 là thứ Năm); hai dòng "kết quả tuỳ người, không phải cam kết" và "không thay cho bác sĩ, chuyên gia" có mặt ở bài sức khoẻ, đặt trước lời mời.

## Đếm

| | Số |
|---|---|
| Bài | 6 (pass 0, gắn cờ 6) |
| Cờ của reviewer | 20 (4 HARD STOP, 16 FIX; 3 cờ cấp tuần) |
| Lỗi thật (giám khảo) | 20 |
| Bắt đúng (TP) | 18 |
| Sót (MISS) | 2 (cả hai nhẹ: nhịp chuyện ngắn ở B-bài dài; dòng "Máy tự thêm: không") |
| Báo nhầm (FA) | 2 ("quan trọng nhất"; chữ ký "Nhi") |
| Precision / recall | 90% / 90% |
| Lỗi thật theo loại | dữ kiện kéo dãn hay tự thêm 9 · lặp câu trong tuần 3 · dòng Máy tự thêm sai/thiếu 3 (tính chung với dữ kiện ở #2, #4) · hook 2 · tiếng Anh 2 · lời mời 1 · độ dài nhịp 1 |

## Nhận xét cho bản sau

1. Người viết vẫn hay kéo dãn **tần suất và thói quen** của coach ("ngày nào cũng", "bất cứ bài nào", "mấy lần cũng không sao") dù cm-writer.md có luật riêng; ba trên bốn HARD STOP rơi vào đúng loại này. Một dòng soát riêng cho các chữ tần suất (ngày nào cũng, lúc nào cũng, bất cứ, mấy lần cũng, luôn luôn) trước khi nộp sẽ chặn được.
2. Lặp câu giữa hai bài cùng coach (3/3 coach) xảy ra khi bài dài và video dùng chung chữ phương pháp của coach. Luật 8e đúng; người viết cần biết câu phương pháp nguyên văn của coach vẫn chỉ được nguyên văn ở một bài mỗi tuần.
3. Hook video ngắn kiểu lật niềm tin dễ vượt ≤18 tiếng vì phải nói đủ Y; cm-writer.md nói "một câu, nhiều nhất hai câu ngắn" nhưng không nhắc con số 18 tiếng ở chỗ đó.
4. Reviewer chỉ đếm tổng chữ, nên một nhịp chuyện quá ngắn trong bài dài không bị bắt; và chữ "nhất" nằm trong lời chính coach đã nói vẫn bị gắn cờ, nên check 3 cần một dòng miễn cho ý kiến có nguồn là lời coach.
