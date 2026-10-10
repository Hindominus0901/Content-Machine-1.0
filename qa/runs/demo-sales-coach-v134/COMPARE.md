# COMPARE · v13.3 so với v13.4 · chị Quyên từ A tới Z

Cùng nhân vật (chị Quyên, hư cấu), cùng bộ câu trả lời, cùng 5 buổi, chạy lại trên build v13.4. Trang này cho anh thấy 12 lỗi của bản v13.3 giờ ra sao, hook mạnh lên hay yếu đi, buổi nào nhanh hơn, nghiên cứu được tới đâu, và lỗi mới nào lộ ra. Bản cũ: [qa/runs/demo-sales-coach/](../demo-sales-coach/REVIEW.md). Bản mới: [TRANSCRIPT.md](TRANSCRIPT.md) · [HOOKS.md](HOOKS.md) · [REVIEW.md](REVIEW.md).

Câu trong «…» là trích nguyên văn từ chat hay file của từng bản, đã soát bằng máy (cột "v13.3" so với bản cũ, cột "v13.4" so với bản mới). Không ghi tên người bình luận; tên trang bán phần mềm, dịch vụ đổi thành vai.

## Nói gọn

- **12 lỗi cũ: Đã sửa 6 · Sửa một phần 6 · Chưa sửa 0.** 6 việc nhỏ ghi thêm ở bản cũ: đã sửa cả 6.
- **Hook tốt lên rõ:** Mạnh 43% (v13.3: 34%), Yếu 3 câu (v13.3: 12). Chữ trên màn hình của bài đăng không còn câu phán suông nào; mục hook_lab của grader Buổi 1 qua.
- **Máy gọn hơn:** không in lại bài khi chị gõ "tiếp", không nhắc mãi một việc, không còn "nhé", hỏi quà trước khi bày quà, mở bán hỏi từng câu thay cho danh sách ☐. Tổng chữ máy viết giảm chừng một phần tư.
- **Chưa đổi:** Ngày 0 vẫn sát giờ bỏ cuộc (video sẵn sàng phút 29,2); bài vẫn ít tiểu từ cuối câu hơn giọng chị (15% so với 50%); máy vẫn khuyên C (chỉ HUB.md) cho người ngày nào cũng mở Google Sheet; tìm web thường vẫn không chạm được chỗ khách nói chuyện.
- **Lỗi mới đáng sửa nhất:** chữ "bạn" và ô trống thô vẫn lọt ra chat («Cam kết: [CẦN BẠN: học xong thấy không hợp thì sao]»), tin cuối Ngày 0 có 2 dòng "Cần chị", và thư đầu cho 210 email cũ là thư tặng quà ở Buổi 2 nhưng là thư xin phép ở Buổi 5.

## 12 lỗi của v13.3: giờ ra sao

| # | Lỗi (theo bảng của bản v13.3) | Kết quả | Trước (v13.3) | Sau (v13.4) | Ghi chú |
|---|---|---|---|---|---|
| 1 | Hook phán suông, lặp ý vẫn lọt ra | **Đã sửa** | «Chữ trên màn hình: Đắt quá là một câu hỏi» | «Chữ trên màn hình: Câu khách chưa dám hỏi» | Grader hook_lab Buổi 1 qua (v13.3 trượt). Chữ trên màn hình của bài đăng: 0 câu Yếu (v13.3: 2). Còn sót 1 câu phán suông trong cặp hook của file chiến lược («Đọc kịch bản, khách biết liền») và 1 dòng caption chép y câu đầu. |
| 2 | Nghiên cứu không tới nơi khách nói | **Sửa một phần** | «Em chưa đọc được nhóm Facebook chủ spa: A) chị có Claude in Chrome, em gửi khung, chị dán vào, 15 phút (máy khuyên)» (chôn trong tin chiến lược 3, khuyên Chrome chị không có) | «B) dán 20 comment, chừng một phút, điện thoại nào cũng được (máy khuyên)» (hỏi ngay sau khi chị kể kênh, lượt 11) | Đúng như đề xuất: hỏi sớm, mặc định dán một phút, nói thẳng khi web không đủ («web chưa ra câu nào của chủ cơ sở dịch vụ»). Nhưng chỗ khách nói chuyện vẫn không đọc được, comment YouTube cũng vậy, và kit còn ghi YouTube "thường mở được". Câu khách thật lần này đến từ bản chị dán ở Buổi 3. |
| 3 | Ngày 0 quá dài; "tiếp" in lại cả kịch bản | **Sửa một phần** | «Hôm nay · thứ Ba 13/10, buổi sáng · video ngắn · NIỀM TIN · 601 chữ» (rồi in lại nguyên kịch bản) | «Hôm nay: thứ Ba · video ngắn "Câu khách chưa dám hỏi", ở tin hôm qua; gõ 'in lại' nếu cần.» | Nửa "tiếp" đã sửa. Ngày 0 không ngắn hơn: chiến lược xong phút 26,9 (v13.3: 26,4; mốc 25), video sẵn sàng phút 29,2 (v13.3: 29,4), tin cuối Ngày 0 vẫn chừng 4.900 tiếng, kịch bản video vẫn in đủ 600 chữ. |
| 4 | Khung chiến lược không giữ đúng nhãn; từ khoá chỉ nằm ở lời mời | **Sửa một phần** | «QUAY HÔM NAY · khoảng 601 chữ» · «TỶ LỆ: thu hút 40 · niềm tin 40 · chuyển đổi 20» | «QUAY HÔM NAY · THU HÚT · video ngắn, Sự thật về nghề · 600 chữ» · «TỶ LỆ NỘI DUNG: THU HÚT 40 · NIỀM TIN 40 · CHUYỂN ĐỔI 20» | Grader thấy đủ nhãn. Còn: N3 không có SUY NGHĨ trong thân bài, bản chữ của video chỉ có từ khoá ở lời mời, dòng nguồn ghi «Câu khách:» thay cho nhãn "Nguồn câu khách:". |
| 5 | Nhãn nội bộ lọt ra cho coach | **Đã sửa** | «Kết quả: ĐẠT · K 2 · V 2 · A 1 · Au 2 · C 2 = 9/10» | «VÌ SAO RA KHÁCH: "để chị suy nghĩ rồi mất luôn" → khách đang nói thật, còn một câu chưa dám hỏi» | "Tại sao?" giờ là một câu VÌ SAO và một câu "Cách viết", không điểm, không mã. Nhãn THU HÚT / NIỀM TIN / CHUYỂN ĐỔI vẫn in trên đầu bài: nay là luật có chủ ý (grader đòi nhãn vai trong tiêu đề QUAY HÔM NAY). |
| 6 | Câu cố định giọng Bắc, "bạn/mình"; ít tiểu từ | **Sửa một phần** | «TIẾP → Chạy thử 4 tuần nhé. OK hay sửa một dòng?» | «Chạy thử 4 tuần theo bản này. OK hay sửa một dòng?» | "nhé" trong lời máy: 3 lần → 0. Dòng "Cần" nay theo cặp xưng hô («Cần chị · phòng khám nha đó cho kể chuyện chưa (không ghi tên)?»). Còn sót: «Cam kết: [CẦN BẠN: học xong thấy không hợp thì sao]» (Buổi 5), «[anh/chị]» trong tin Buổi 4, «Bài bạn thích» trong bảng Kho. Tiểu từ cuối câu trong bài vẫn 15% (giọng chị 50%). |
| 7 | Hỏi chỗ lưu (hub) quá muộn và khuyên sai | **Sửa một phần** | «Em chọn C: Notion chưa kết nối ở đây, HUB.md đã nằm sẵn trong Project.» (lượt 14 Buổi 2, chỉ sau khi chị hỏi "lưu đâu em?") | «Máy khuyên C: ở đây chưa kết nối Notion, còn HUB.md đã nằm sẵn trong project.» (lượt 1 Buổi 2, lần "tiếp" đầu) | Đúng lúc rồi, vẫn khuyên sai. Kit ghi "khuyên B nếu coach ngày nào cũng dùng Google Sheet" mà không câu nào hỏi chuyện đó, nên máy không bao giờ biết. Chị vẫn phải tự xin Sheet. |
| 8 | Bày quà mới khi coach đã có quà | **Đã sửa** | «QUÀ: 1 trang "3 tin nhắn lại khi khách nói để chị suy nghĩ", em viết theo cách chị dạy.» | «QUÀ: có sẵn file tặng thì chị gõ tên nó kèm OK, em dùng đúng nó; chưa có thì em viết một trang.» | Chị không phải cãi lần nào; Buổi 2 máy nói «dùng đúng file "Khách nói để chị suy nghĩ thì nhắn gì" của chị, không làm cái mới». Câu hỏi quà nằm chung tin với câu OK, thành hai quyết định một tin (xem lỗi mới 2). |
| 9 | TIẾP nhắc mãi một việc chị chưa làm | **Đã sửa** | «TIẾP → Gõ A hay B cho 2 lời nhắc.» (7 trên 15 dòng TIẾP Buổi 2 quay về việc này) | «File quà em thôi nhắc; khi nào chị dán chữ trong file thì em làm tiếp chỗ đó.» | Buổi 2: 0 trên 14 dòng TIẾP quay lại việc chị chưa trả lời; file quà hỏi 2 lần rồi vào "Đang chờ chị". Một buổi sáng vẫn có 3 dòng "Cần chị" khác nhau, chị không trả lời dòng nào. |
| 10 | Lời nhắc tự chạy không hợp coach chỉ có Project | **Đã sửa** | «Cần gói Pro hay Max, có Content Machine cài dạng plugin.» | «A) vẫn cài hai tác vụ đó: chỉ nhắc, tự mang tóm tắt riêng; bài thì viết khi chị vào Project nhắn 'tiếp' (máy khuyên): nhắc đúng giờ, không cần plugin B) 3 lời nhắc trên Google Calendar C) để sau» | Đủ 4 ý đề xuất: đường "chỉ có Project", có Google Calendar, khung có «Gọi mình là chị», tổng kết thứ Sáu chạy chiều («T6 15:07 Số liệu thứ Sáu»), nói rõ Scheduled ở app máy tính. Lỗi phụ mới ở lỗi mới 8. |
| 11 | Định dạng khó đọc trên điện thoại | **Đã sửa** | «Ngày \| Kênh \| Trụ cột nội dung \| Tuyến \| Loại \| Dạng \| Số chữ \| Hook \| Cách viết \| Lời mời \| Trạng thái» · «☐ Trả góp: có hay không» | «\| Ngày \| Dạng \| Hook \| Lời mời \|» · «Học xong mà thấy không hợp thì sao chị: có hoàn tiền, hay chị cam kết gì về cách làm?» | Bảng trong chat 4 cột, khung dán Sheet ≤6 cột, mở bán hỏi từng câu thay cho 19 dòng ☐. Giá phải trả: giới hạn 3 khung dán mỗi tin làm thêm lượt "ok em" (lỗi mới 6). |
| 12 | Mẫu mở bán không soát lịch thật và hoàn cảnh coach | **Sửa một phần** | «Tệp ấm bây giờ: khoảng 1.780 (Zalo 1.400 + email 210 + 170 người comment, nhắn)» · «Anh chị từng điền form đăng ký lớp Chốt Khách Không Ép của mình, nên hôm nay mình gửi thư đầu tiên.» (Buổi 2) | «Tệp ấm bây giờ: chưa đếm; riêng 210 email form đăng ký lớp với chừng 170 người nhắn, comment 3 tháng nay đã hơn 30 nhiều» · «Thư đầu tiên gửi họ là thư tặng file của chị» (Buổi 2) | Phần mở bán sửa hết: tệp ấm chỉ tính người mua được đúng lớp này, soát ngày 5 dòng (20/11, giờ yên, đóng sát khai giảng), phương án DỪNG không chạm 24/11, kịch bản Zoom chạy một mình, thư đầu Buổi 5 là thư xin phép. Phần Buổi 2 chưa: thư đầu cho 210 email vẫn là thư tặng quà, vì luật "xin phép lại" chỉ nằm trong file mở bán. |

### 6 việc nhỏ ghi thêm ở bản v13.3

| Việc | Kết quả | Trước (v13.3) | Sau (v13.4) | Ghi chú |
|---|---|---|---|---|
| "Hook khác" chỉ cho 2 câu (đáp án muốn 3) | **Đã sửa** | «Em chọn hook 1 cho video hôm nay vì nó là chuyện của chính chị, không có giọng rao; muốn hook 2 thì gõ 2.» | «Dạ, 3 cách mở khác, nói như chị đang ngồi nói chuyện với một chủ spa.» | Chuẩn hook-lab nội bộ vẫn ghi "đúng 2"; kit và đáp án ghi 3. Nên sửa chuẩn cho khớp. |
| Luật số kết quả trong quảng cáo chưa khớp đáp án | **Đã sửa** | «Chuyện anh Tài vô quảng cáo được (anh Tài cho dùng cả quảng cáo); chuyện, số của chị Trâm thì không.» | «Báo giá xong, khách nhắn đúng hai chữ: "đắt quá".» | 3 hook, 3 dòng tiêu đề quảng cáo, không con số kết quả nào, đúng đáp án. |
| Thư mục Level-ups/Board thiếu trong gói tải | **Đã sửa** | «không thấy thì dùng 5 file em gửi dưới tin này.» | «5 file này nằm trong thư mục Level-ups/Board của bộ tải về.» | Gói v13.4 có đủ 5 file CSV. |
| Tab Nội dung thiếu cột comment từ khoá | **Đã sửa** | (lỗi nằm trong file bảng, không in ra chat) | «Comment từ khoá,Tin nhắn/khách hỏi» | Buổi 4 ghi được 21, 3, 19, 12, 26 comment SUY NGHĨ cho từng bài. |
| Luật "đổi tuyến chỉ khi tổng kết tháng" vênh với gợi ý thêm tuyến | **Đã sửa** | «B) thêm tuyến "Nhắn lại có cớ" từ tuần 2» | «Tuyến bài chỉ đổi ở buổi nhìn lại tháng (thứ Sáu 30/10):» | Lựa chọn A/B/C ở thẻ góc nhìn giờ tôn trọng luật tháng. |
| Ô kho tuần vênh với luật chỉ lưu câu GIỮ | **Đã sửa** | «THEO DÕI · sợ nhắn lại thành làm phiền: giờ 2 người, vẫn 1 nơi (Voz)» (ô bỏ trống) | «Chưa dùng làm hook, từ khoá hay bằng chứng tới khi chỗ thứ hai nói ra.» | Câu THEO DÕI được vào kho, có nhãn rõ, không bị dùng sớm. |

## Hook: v13.3 so với v13.4

Chấm cùng một thang (chuẩn hook-lab nội bộ; Mạnh = cụ thể, chữ khách, hé hay lật; Được = đúng việc mà thiếu một điều; Yếu = phán suông, lặp, chung chung, chị đã chê). Chi tiết từng câu ở [HOOKS.md](HOOKS.md) và [HOOKS của v13.3](../demo-sales-coach/HOOKS.md).

| | v13.3 | v13.4 |
|---|---|---|
| Hook đưa chị xem | 128 | 118 (8 là khung hình đầu, bản cũ không ghi loại này) |
| Mạnh | 43 (34%) | 51 (43%) |
| Được | 73 | 64 |
| Yếu | 12 (9%) | 3 (3%) |
| Mục hook_lab của grader (Buổi 1) | trượt | qua |

Theo bề mặt (Mạnh · Được · Yếu):

| Bề mặt | v13.3 | v13.4 |
|---|---|---|
| **Chữ trên màn hình, tất cả** | 14: 0 · 11 · 3 | 20: 3 · 16 · 1 |
| · trên bài đăng | 11: 0 · 9 · 2 | 10: 1 · 9 · 0 |
| · trong file chiến lược | 3: 0 · 2 · 1 | 10: 2 · 7 · 1 |
| Khung hình đầu | không ghi | 8: 4 · 4 · 0 |
| Câu đầu, dòng 1–2 của bài | 44: 24 · 17 · 3 | 40: 28 · 12 · 0 |
| Dòng 1 caption | 6: 0 · 6 · 0 | 5: 2 · 2 · 1 |
| Tiêu đề, chữ ảnh bìa | 9: 4 · 4 · 1 | 9: 2 · 7 · 0 |
| Trang 1–2 carousel | 2: 1 · 1 · 0 | 3: 2 · 1 · 0 |
| Tiêu đề email, dòng xem trước | 25: 7 · 15 · 3 | 16: 6 · 9 · 1 |
| Quảng cáo | 6: 4 · 1 · 1 | 6: 4 · 2 · 0 |
| Câu mở tin Zalo, inbox | 22: 3 · 18 · 1 | 11: 0 · 11 · 0 |

Theo buổi (Mạnh · Được · Yếu): Buổi 1: 7 · 13 · 4 → 17 · 18 · 2 · Buổi 2: 12 · 14 · 3 → 14 · 14 · 0 · Buổi 3: 1 · 1 · 0 → 3 · 1 · 0 · Buổi 4: 5 · 1 · 0 → 1 · 1 · 0 · Buổi 5: 18 · 44 · 5 → 16 · 30 · 1.

Đọc số này thế nào: chữ trên màn hình hết phán suông nhưng phần lớn vẫn chỉ "Được" (câu hỏi gọn, chưa có gì để nhìn); cái mạnh lên thật nằm ở câu đầu và khung hình đầu, nơi máy dùng cảnh và chữ khách. Câu mở tin Zalo vẫn là chỗ phẳng nhất: 6 trên 7 tin của Buổi 5 mở y một kiểu "Dạ anh chị,". Câu mạnh nhất cả hai bản vẫn là một câu: «Khách đang nằm trên giường, tư vấn viên đứng kế bên chào thẻ ba chục buổi.»

## Thời gian và số lượt

| Buổi | v13.3: phút · lượt chị · chữ máy | v13.4: phút · lượt chị · chữ máy | Ghi chú v13.4 |
|---|---|---|---|
| 1 · Ngày đầu | 29,4 · 16 · 7.256 | 29,2 · 16 · 6.420 | chiến lược xong 26,9 (v13.3: 26,4); tin cuối 4.912 tiếng (v13.3: 5.845) |
| 2 · Hôm sau | 30,2 · 15 · 4.220 | 27,0 · 14 · 2.551 | có 6 phút rời máy để cài Google Sheet; có bài đăng được ở phút 11,8 |
| 3 · Nghiên cứu | 10,4 · 5 · 2.895 | 15,0 · 4 · 1.079 | có 7 phút rời máy để chép bình luận, tin nhắn |
| 4 · Thứ Sáu | 34,0 · 12 · 4.054 | 22,9 · 10 · 3.533 | 9 phút rời máy cài 2 tác vụ (v13.3: 8) |
| 5 · Mở bán | 57,1 · 14 · 10.518 | 55,4 · 22 · 8.129 | nhiều lượt hơn vì hỏi từng câu trước khi mở và in thẻ ngày theo đợt |
| **Tổng** | **161,1 · 62 · 28.943** | **149,5 · 66 · 21.712** | |

Phút là giờ mô phỏng (máy trả lời sau 0,3 phút; lượt có tìm web ở Buổi 3 tính 1 phút), không phải đồng hồ thật. "Chữ máy" đếm bằng máy theo khoảng trắng (gần bằng số tiếng), gồm cả khung chép.

## Grader tự động Buổi 1: thật hay báo nhầm

Cả hai lượt đều **hợp lệ** (đủ lượt, tốc độ đúng, kiểm tra lộ dữ kiện chỉ có cảnh báo). Cả hai đều trượt 8 mục, nhưng không phải 8 mục giống nhau.

| Mục | v13.3 | v13.4 | Lỗi thật của máy ở v13.4? |
|---|---|---|---|
| hook_lab | trượt, thật | **qua** | |
| I8 (số không có nguồn) | trượt, kit và grader vênh | **qua** | |
| I15 (xưng hô) | trượt, báo nhầm | **qua** | |
| vn_natural | trượt, thật: 15% câu kết bằng tiểu từ, chị 50% | trượt, thật: 15% (29/199), chị 50% | Thật. Lỗi chất lượng lớn nhất còn lại. |
| day0_timing | trượt, thật | trượt | Thật một phần: chiến lược xong phút 26,9 > 25. Báo nhầm: "chưa cắt lời xả" (grader cộng câu trả lời phỏng vấn vào lời xả; chị gõ "xong rồi" ở lượt 6). |
| day0_strategy | trượt, lẫn | trượt | Lẫn. Thật: dòng nguồn ghi «Câu khách:» thiếu nhãn; bài tuần 1 không ghi trụ cột. Báo nhầm: khung tuyến bài kit bắt in ở tin chiến lược 2; "6 trụ cột" (grader đọc dòng ghi chú "(em chọn;" thành trụ cột); "QUAY HÔM NAY sau một lượt không phải OK" (lượt đó kết bằng "OK em."). |
| day0_shape | trượt, phần lớn thật | trượt | Phần lớn thật: ĐIỀU KHÁCH NHỚ 53 tiếng (mốc 50); N3 không có SUY NGHĨ trong thân bài. Báo nhầm: "lời mời xin chữ chị ơi" (đó là câu mẫu xấu trong bài), "tuần 1 không có tin Zalo" (N5 là tin Zalo). |
| I9 (trích nguyên văn) | trượt, thật một chỗ | trượt | Phần lớn báo nhầm: các câu bị bắt là câu mẫu cho lễ tân nói («Dạ da chị đang lo chỗ nào nhất ạ?»), không phải lời khách. Cần một luật cho câu mẫu trong ngoặc. |
| I3 (dòng "Cần") | qua | **trượt** | Thật: tin cuối có 2 dòng "Cần chị", một dòng dài 27 chữ (mốc 20). |
| I5 (tối đa 1 câu hỏi) | qua | **trượt** | Báo nhầm: grader đếm hook «Tin đầu tiên, gửi gì?» trong bảng tuần 1 là một câu hỏi. |
| quit_triggers | qua | **trượt** | Báo nhầm, cùng chứng cứ với I5: chị chỉ bị hỏi một câu. |

Gọn lại: v13.3 có 4 mục trượt thật, 2 lẫn, 1 vênh, 1 báo nhầm. v13.4 có 2 mục trượt thật (vn_natural, I3), 3 thật một phần (day0_timing, day0_strategy, day0_shape), 3 báo nhầm (I5, quit_triggers, I9). Ba lỗi của grader (I5, quit_triggers, I9) nên sửa trước lần chấm tới, vì quit_triggers báo nhầm sẽ làm người đọc tưởng coach bỏ đi.

## Tiểu từ cuối câu (nha, nè, á, hen…): bài so với giọng chị

| Đo bằng | v13.3 | v13.4 |
|---|---|---|
| Grader Buổi 1 (bài Tuần 1 so với 2 bài chị dán) | 15% so với 50% | 15% so với 50% |
| Đếm thô bằng máy, mọi khung bài, cùng một cách cho hai bản (bài chị dán đếm cùng cách: 38%) | Buổi 1: 13% · Buổi 2: 18% · Buổi 5: 11% | Buổi 1: 13% · Buổi 2: 30% · Buổi 5: 10% |
| Đếm tay Buổi 2 (ghi chú phiên chạy) | không đo | caption đầu 33%; sau khi chị đòi "viết lại giọng chị": 60% và 62% (giọng chị chừng 53%) |

Buổi 3 và 4 quá ít câu bài để đếm. Nói thẳng: máy chỉ viết đúng giọng chị khi chị đòi. Bài đầu tiên của mỗi buổi vẫn phẳng hơn giọng chị, như bản v13.3.

## Nghiên cứu: đọc được gì

| Buổi | v13.3 | v13.4 |
|---|---|---|
| 1 · Ngày đầu | 33 lượt tìm · thử 17 trang · đọc được 11 · 9 câu nguyên văn của người bán hàng (diễn đàn) · 1 mẫu GIỮ (người bán, không riêng spa) | 23 lượt tìm · thử 7 trang · đọc được 6 · 3 câu của chủ shop online do báo trích (nhóm gần, chỉ THEO DÕI) · 0 mẫu GIỮ. Câu của chủ cơ sở dịch vụ: 0 ở cả hai bản. |
| 3 · Kênh đối thủ | 20 lượt tìm · 3 kênh YouTube, 186 tiêu đề, view, ngày · 0 comment | 17 lượt tìm · thử 14 trang · đọc được 5 (4 trang bán kịch bản, 1 báo) · TikTok trống 5 lần, YouTube trống 4 lần · 0 kênh · bản chị dán 28 dòng → 14 câu khách, 2 mẫu GIỮ, 4 người đang muốn mua |
| 4 · Thứ Sáu | 12 lượt tìm · thử 10 trang · đọc được 6 · thêm 3 câu (THEO DÕI) | không tìm web; trả lời từ thẻ đã lưu và đưa khung dán một phút |
| 5 · Mở bán | không tìm web | không tìm web |

**Lưu ý thật thà khi so.** Ở Buổi 3 bản v13.3, người mô phỏng đọc YouTube bằng cách tải trang thô và gọi oEmbed, việc mà Claude của một coach thật thường không làm được; 3 kênh và 186 tiêu đề vì vậy là con số lạc quan. Bản v13.4 chỉ dùng công cụ tìm và đọc web thường, nên "0 kênh đọc được" là trần thật của web thường hôm nay. Ngược lại, 14 câu khách thật của v13.4 đến từ bản dán cố định của nhân vật (bình luận trên chính trang chị, không phải của đối thủ), thứ bản v13.3 chưa bao giờ có vì chị không dán. Hai bản không so ngang được; điều so được là: cả hai bản, web thường không đọc được nơi khách của chị nói chuyện, và lần này máy nói thẳng điều đó ngay trong chiến lược.

## Lỗi mới thấy ở v13.4 (gộp 5 buổi, bỏ trùng, xếp theo ảnh hưởng)

Xếp theo mục tiêu của anh: hook tốt, nghiên cứu thật, chiến lược trước, có A/B/C, không kết lửng, nhanh, tiếng Việt tự nhiên. Lỗi nào là phần còn lại của 12 lỗi cũ thì đã ghi ở bảng trên, không lặp ở đây.

| # | Lỗi mới | Ở đâu trong kit | Thấy ở | Sửa đề xuất |
|---|---|---|---|---|
| 1 | Chữ "bạn" và ô trống thô lọt ra chat với một coach bỏ đi khi bị gọi "bạn": «Cam kết: [CẦN BẠN: học xong thấy không hợp thì sao]», «Hỏi nhỏ để lần sau mình gửi sát hơn: chuyện nhắn lại khách, giờ [anh/chị] thấy khó nhất chỗ nào ạ?», loại kho «Bài bạn thích» | 1-INSTRUCTIONS (dòng "[CẦN BẠN: …]"), RESEARCH R7 (câu hỏi sau quà), BOARD-COLUMNS (Kho · Loại), BOARD §CM-NUDGE-CLAUDE (khung tác vụ), STRATEGY §CM-LIKED ("Bài nào bạn nhớ mãi") | B4, B5 | Mọi chuỗi cố định dùng {xưng hô}: "[CẦN {XƯNG HÔ}: …]", "{anh/chị}" điền sẵn theo Card; đổi "Bài bạn thích" thành "Bài mẫu"; thêm một dòng soát "không còn [ ] hay 'bạn' trong chữ gửi coach". |
| 2 | Tin cuối Ngày 0 có 2 dòng "Cần chị" («Cần chị · dán file "Khách nói để chị suy nghĩ thì nhắn gì" vào đây một lần…», «Cần chị · phòng khám nha đó cho kể chuyện chưa (không ghi tên)?»); và câu hỏi quà gộp vào tin chiến lược 3 cùng câu OK, thành hai quyết định một tin | §CM-STRATEGY-ENGINE tin 3 (dòng QUÀ), §CM-CTA-KIT 2, 1-INSTRUCTIONS ("một Cần bạn") | B1 (grader I3) | Hỏi "chị có sẵn file quà chưa?" trong lúc phỏng vấn (thêm ô QUÀ vào 8 ô soát thầm), để tin 3 chỉ còn câu OK; dòng "Cần" thứ hai chờ tới hôm bài đó lên (N3 thứ Năm), ghi vào HUB "Đang chờ chị". |
| 3 | Thư đầu cho 210 email chưa từng gửi: Buổi 2 là thư tặng quà («Thư đầu tiên gửi họ là thư tặng file của chị»), Buổi 5 là thư xin phép («210 email chưa nhận thư nào của chị, nên thư đầu chỉ xin phép lại, không bán») | Luật "xin phép lại" chỉ có ở CAMPAIGNS §CM-LAUNCH-SEQUENCES; §CM-MESSAGES 3 (email ngày thường) không có, cũng không có dòng DỪNG cho email | B2, B5 | Đưa một luật lên §CM-MESSAGES 3: danh sách chưa từng nhận thư hay im 6 tháng → thư đầu xin phép lại (quà làm lý do), ai trả lời CÓ mới nhận thư sau; kèm dòng DỪNG cho email. |
| 4 | Nhánh nghiên cứu thiếu: kit nói YouTube "thường mở được tiêu đề, số view" mà trang video, trang tìm, danh sách phát đều trắng; không có nhánh "tìm không ra kênh nào"; thẻ góc nhìn không có dạng "0 kênh"; "một nơi" định nghĩa hai kiểu (luật 5 và C3 1) | RESEARCH R1 6, §CM-CHANNELS C1–C2, §CM-RESEARCH 5, §CM-AUDIENCE C3–C4 | B3, B4 | Cho YouTube cùng nhánh với TikTok (thử 1 trang, trắng → khung dán); thêm A/B/C "không tìm ra kênh: dán dưới video đầu tiên khi tìm '{câu khách}' (máy khuyên) / gõ tên kênh / đọc trang web cùng loại"; một định nghĩa "nơi"; dòng đầu thẻ cho trường hợp 0 kênh. |
| 5 | Bản dán có người đang muốn mua (hỏi học phí, giữ chỗ khóa 4, xin gọi) mà kit chỉ dạy chia nỗi đau, mong muốn, câu hỏi; máy tự thêm «4 người đang chờ chị trả lời, tối nay chị nhắn họ trước» | RESEARCH §CM-LISTEN R3, BANKS §CM-RESEARCH-BANK 4–5 | B3 | Thành luật: người hỏi mua trong bản dán lên đầu kết quả, theo vai, không số điện thoại; rồi mới tới mẫu và thẻ. |
| 6 | Bảng Sheet làm thêm lượt và không chứa nổi bài chị tự viết: tối đa 3 khung dán mỗi tin (Buổi 4 ba lượt "ok em" liền, Buổi 2 «Cột Trạng thái của 5 bài này em in ở tin sau.»); tab Noi-dung không có cột tiêu đề, không tách số theo nền tảng; Trạng thái thiếu "Đã tổng kết"; Kho không có loại "hook" | BOARD §CM-BOARD 4, BOARD-ROWS 1, BOARD-COLUMNS, §CM-BOARD-CAMPAIGNS 2 | B2, B4, B5 | Cho phép 4 khung ở tin cài bảng và tin thứ Sáu, hoặc một khối A→G cho dòng mới; thêm cột Tiêu đề và Nền tảng tách dòng; thêm "Đã tổng kết" và loại "Hook từng ăn"; dòng Noi-dung của cả đợt mở bán nằm trong file, nói rõ. |
| 7 | Luật ngày mở bán vênh nhau: "đóng cách khai giảng ≥3 ngày" với "không bao giờ dời hạn thật" (hạn chị 22/11, khai giảng 24/11); "đóng vào tối ngày thường" không có trong bước soát; mẫu tin "4–6 tiếng sau live", "còn 48 giờ", "giờ cuối" rơi vào giờ yên 22h–7h | CAMPAIGNS §CM-LAUNCH-DAYS (SOÁT NGÀY), §CM-LAUNCH-TIMING 2 và 5, §CM-LAUNCH-SEQUENCES | B5 | Ghi rõ: hạn coach đã chốt thì báo một dòng, giữ hạn, ngày giữa chỉ để xác nhận; thêm "đóng ngày thường" vào soát ngày (hay bỏ); mẫu nào rơi giờ yên → 7h30 hôm sau hay gộp vào tin trước. |
| 8 | Tác vụ hẹn giờ: khung cố định chiếm 794 trên 900 ký tự nên phần giới thiệu bị cắt còn «Mình: chữa tin nhắn thật.»; "Run now" ngay tối thứ Sáu chạy lại việc thứ Sáu; "(máy khuyên)" ở A/B/C "chỉ có Project" không kèm lý do, không hỏi gói | BOARD §CM-NUDGE-CLAUDE, §CM-NUDGE-RULES 3, §CM-OPTIONS 3 | B4 | Rút phần cố định còn ≤600 ký tự; "Run now" chỉ khi hôm nay không phải ngày tổng kết; lý do khuyên A trong một vế ("chị có app máy tính, gói Pro"). |
| 9 | Việc hỏi một lần rồi rơi mất: HUB.md không có chỗ cho dòng "Cần" mới hỏi một lần (xin phép kể chuyện phòng khám nha không được ghi lại, bài vẫn lên thứ Năm); quà "thôi nhắc" mà đợt mở bán dựa trên quà không hỏi lại, nên video ngày 2 phải viết vòng | BOARD §CM-HUB-MD, §CM-MEMORY 2, CAMPAIGNS §CM-CAMPAIGN-GIFT | B2, B5 | Thêm mục "Đã hỏi, chưa trả lời" trong HUB; mở bán bằng quà thì coi là "mở lại" việc đang chờ, hỏi một lần. |
| 10 | Mở bán: kit bảo viết cả bộ trong tuần chuẩn bị mà mỗi tin một màn hình; buổi thành 22 lượt, 8.129 chữ, 55 phút. Tệp ấm "chưa đếm" chưa có nhánh | CAMPAIGNS §CM-LAUNCH-DAYS, LAUNCH §CM-LAUNCH 4 | B5 | Ghi rõ cách chia máy đã tự làm: ngày 1–3 in đủ chữ, phần còn lại in ở Bàn mở bán sáng hôm đó; "chưa đếm" → lấy phần chắc (danh sách đăng ký lớp, người nhắn 90 ngày) làm sàn, ghi "(em đoán)". |
| 11 | Lời dặn mở chat không thống nhất: «Mai mở Content Machine, vào đoạn chat mới nhất, nhắn 'tiếp'.» (Buổi 1–3, khung tác vụ) và «mở Content Machine, tạo đoạn chat mới rồi nhắn 'tiếp'» (Buổi 4, 5) | §CM-TODAY (dòng cuối), BOARD §CM-NUDGE-CLAUDE | B1–B5 | Một câu duy nhất, kèm lý do nửa dòng (chat mới cho nhẹ, máy đọc lại HUB và Card). |
| 12 | Ba luật vênh ở các yêu cầu ngày 2: trang cuối carousel phải có quà đúng chủ đề mà mỗi mùa chỉ một quà; "hook khác" vừa "thêm 3", vừa "hỏi chọn câu nào", vừa "máy tự chọn"; từ khoá viết "không dấu" (CTA-BANK) hay "SUY NGHĨ" có dấu (Map) | STRATEGY §CM-TEXT-FORMATS 1, HOOKS §CM-HOOK-TEXT 3 với §CM-CTA-KIT 1 · §CM-FORMATS 1, HOOK-LIBRARY 2 và 6, §CM-OPTIONS 4 · BANKS CTA-BANK 2, HOOK-CTA 3 với §CM-MAP | B2 | Cho lời mời dự phòng khi chủ đề khác quà ("Lưu lại, lần tới … thì mở ra"); chọn một luật "hook khác" (máy tự chọn, ghi "muốn khác thì gõ số"); một cách viết từ khoá. |
| 13 | Quảng cáo và kênh: không có đường cho TikTok (video tốt nhất của chị ở TikTok); câu "trang cá nhân không chạy quảng cáo được" cần kiểm lại với trang cá nhân chế độ chuyên nghiệp; YouTube cần link quà mà không có bước làm link | LAUNCH §CM-ADS, §CM-CTA-KIT | B2 | Thêm một dòng TikTok Quảng bá; kiểm lại và ghi ngày cho câu về trang cá nhân; bước "file quà → link Drive" một lần. |
| 14 | Hai "tuần sau" trong tổng kết thứ Sáu (dòng 5 của tổng kết và A/B/C tuần sau), dòng So-lieu in trước khi chị chọn nên không ghi được lựa chọn; R7 nói "dán 10 comment" mà khung dán cùng tin nói 20 | §CM-NUMBERS, BOARD §CM-NUDGE-JOBS 3, RESEARCH R7 với R0 | B4 | Một chỗ "tuần sau" (A/B/C), dòng So-lieu in sau khi chọn; một con số cho bản dán. |
| 15 | ĐIỀU KHÁCH NHỚ dài 53 tiếng (mốc 50), mẫu không có dòng tự đếm | §CM-MAP, §CM-STRATEGY-ENGINE tin 1 | B1 (grader) | Thêm "≤50 tiếng, đếm trước khi in" vào mẫu. |

Lỗi của grader, không phải của kit (nên sửa trước lần chấm tới): I5 và quit_triggers đếm hook dạng câu hỏi trong bảng là câu hỏi cho coach; I9 đọc câu mẫu cho lễ tân là lời khách; day0_strategy bắt khung tuyến bài mà kit đòi, đọc "(em chọn;" thành trụ cột thứ 6, không nhận "OK em." ở cuối lượt; day0_timing cộng câu trả lời phỏng vấn vào lời xả; research_leaks bắt chữ thường ngày ("chê đắt") đã có trong kết quả tìm trước đó.

## Lỗi của người mô phỏng (không phải lỗi kit)

- **Một người chơi cả hai vai.** Người chạy đã đọc bộ câu trả lời trước khi viết lượt của máy. Đã quét sau: Buổi 1 gỡ trước lần chấm vài câu dùng dữ kiện chị chưa nói (một câu về bác sĩ Long, mấy câu cảnh bịa); Buổi 5 gỡ vài cụm chữ của hồ sơ nhân vật lọt vào nháp. Không còn dữ kiện nào chị chưa nói trong bản cuối.
- **Lượt tìm web.** Buổi 1 có 2 lượt tìm dùng chữ chị chỉ nói ở đoạn xả thứ 3 (ghi vào đúng lượt chữ đó xuất hiện); Buổi 3 có 2 lượt tìm dùng chữ thường ngày ("chê đắt", "tư vấn viên spa") mà kết quả tìm đã hiện trước. Grader sẽ bắt; người đọc có thể coi là lẫn.
- **Lượt của chị không có trong bộ câu trả lời.** Buổi 2: trang 1 carousel, lời mời cho 3 nền tảng, "viết lại giọng chị" (theo kịch bản buổi); "tại sao?" được đưa lên sớm để rơi vào một bài có thật. Buổi 5: giờ báo số 21h và "chừng 170 người" lấy từ hồ sơ mở bán; "em tính giùm chị", "bỏ qua em" thay cho câu trả lời còn thiếu.
- **Bản dán Buổi 3** là bản dán cố định của nhân vật (bình luận, tin nhắn trên trang của chị), không phải bình luận dưới video đối thủ chị nhờ đọc. Máy nói đúng điều đó.
- **Số liệu Buổi 4** lấy ngày và tên bài từ bộ số của kế hoạch bản v13.3 (bài bảo hiểm, video "đắt quá" không nằm trong lịch của bản này); máy khớp theo tên và ghi "(mình đoán)".
- **Thứ tự chạy khác bản cũ.** Buổi 3 và 5 chạy từ trạng thái sau Buổi 2 (v13.3: sau Buổi 1), nên biết Google Sheet. Buổi 5 chạy trước khi có Buổi 4: dùng Brand Card v1, không biết lời nhắc đã cài, lấy số tuần 1 từ bộ số của nhân vật.
- **Thời gian và chấm.** Quy ước 0,3 phút mỗi câu trả lời che thời gian viết và tìm web. Chỉ Buổi 1 được grader chấm; Buổi 2–5 là bản trình diễn, chấm bằng tay. Buổi 2 người mô phỏng bỏ bước đếm tiểu từ ở caption đầu (33%), chỉ sửa khi chị đòi; máy thật làm đúng §CM-NATURAL 4 thì phải đếm ở mọi bài.
