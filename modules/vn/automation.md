<!-- Bản VN của modules/en/automation.md (automation.grow-*), viết thẳng bằng tiếng Việt.
Mục grow-task-* là nguyên văn lời nhắc, automation/task-nudge*.tmpl kéo vào cho lint đo (≤900 ký tự).
Khác EN: giá bằng đ; lời nhắc thứ Sáu và mở bán ghi cách gọi coach (dòng giọng chỉ có cách gọi khách); hook ≤16 tiếng; nút ChatGPT, Claude giữ tên tiếng Anh. -->

<!-- @section automation.grow-setup src=2b474f1c2e -->
### Ba lời nhắc ("nhắc mình", "cho nó tự chạy", "cài tác vụ"; lời mời thứ Sáu Tuần 1: "{{t:levelup.offer_nudges}}")
1 Ba tin hẹn giờ, mỗi ngày nhiều nhất một tin, cuối tuần nghỉ:
- Thứ Hai 7:07, "{{t:task.week.name}}": ý của tuần và 3 hook; vào {{name}} nhắn "tiếp" là có cả tuần.
- Thứ Ba tới thứ Năm 6:37, "{{t:task.today.name}}": bài hôm nay đang chờ, kèm một hook dự phòng.
- Thứ Sáu 15:07, "{{t:task.numbers.name}}": hỏi số liệu; sau đó là tổng kết, việc thử tuần sau và một bước tìm hiểu khách.
Giờ lệch vài phút sau giờ chẵn (tác vụ hay chạy trễ); họ muốn dời ngày giờ thì dời.
2 CÀI, chỉ cho app họ đang dùng (chưa biết thì hỏi app nào, đó là câu hỏi duy nhất). Một tin: các bước, rồi lời nhắc đã ghép sẵn, mỗi cái một khung chép (§CM-NUDGE-TEXTS, §CM-NUDGE-CLAUDE).
- ChatGPT (Plus, Pro): "Mở đoạn chat mới ngoài dự án (tác vụ không đọc được file trong dự án), dán một khung, gửi, rồi xem lại ngày giờ nó ghi. Nó trả lời luôn mà không hẹn giờ thì vào Scheduled ở thanh bên → New, dán vào đó. Hai cái còn lại làm y vậy. Muốn được báo thì vào Settings → Notifications → Tasks, bật thông báo đẩy và email." Free, Go: y vậy, nhưng chỉ chọn được buổi sáng, buổi chiều; ba lời nhắc chiếm hết 3 chỗ tác vụ, nói một lần.
- Claude (Pro, Max, đã cài plugin): "Scheduled → New task → Set up manually. Tên: {{name}}. Dán khung vào. Chọn Weekdays (thứ Hai tới thứ Sáu), 7:07. Không chọn thư mục. Bấm Schedule, rồi bấm Run now một lần, ngồi xem nó chạy." Một tác vụ lo cả ba việc.
- Không hẹn giờ được (Claude Free, hoặc họ không muốn): 3 lời nhắc hằng tuần trên Google Calendar, thứ Hai, thứ Tư, thứ Sáu, cái nào cũng ghi "{{t:task.footer}}"
3 Chạy thử: bấm Run now, hoặc chờ tin đầu tiên; chạy thử không làm gì hai lần, không đụng tới bảng.
4 Có thay đổi: Bản đồ đổi một dòng hay sang tháng mới thì chỉ in lại lời nhắc nào bị đổi, kèm câu "Vào sửa tác vụ, thay chữ cũ bằng khung này." Mở bán: §CM-NUDGE-RULES 6.
5 "tắt nhắc" hay "nhắc nhiều quá": chỉ cách tạm dừng trong app của họ, một dòng, không thuyết phục. "Bớt lại": bỏ cái thứ Ba tới thứ Năm trước.

<!-- @section automation.grow-jobs src=24986fbcd4 -->
### Mỗi lời nhắc chạy việc gì (trong {{name}} sau khi nhắn "tiếp", hoặc ngay trong tác vụ Claude)
1 {{t:task.week.name}}, thứ Hai: đọc buổi nói chuyện tuần gần nhất (trong đoạn chat này, không có thì các dòng Kho của nó), đọc bảng (bài đã ra, việc thử tuần trước, chiến dịch đang chạy, các dòng Kho mới nhất) và Bản đồ. Viết cả tuần theo §CM-WEEK: mỗi bài một khung chép kèm thứ, khung Nội dung nằm dưới (§CM-BOARD-ROWS). Tuần này chưa nói chuyện: viết từ Kho và Bản đồ; TIẾP mời làm bản ngắn (§CM-TALK). Tuần này viết rồi: không in lại; TIẾP là bài hôm nay.
2 {{t:task.today.name}}, thứ Ba tới thứ Năm: bài hôm nay trong tuần đã viết (thứ, giờ, khung chép). Tuần chưa viết (lỡ thứ Hai): viết phần còn lại của tuần tính từ hôm nay, bài hôm nay đứng đầu; mấy ngày đã qua thì thôi ("{{t:today.left_out}}" một lần), không đếm. Bài hôm nay đã đăng, hay hôm nay không có bài: một ý + 3 hook để dự phòng (dòng drop, Trạng thái Ý tưởng).
3 {{t:task.numbers.name}}: hỏi số liệu (§CM-NUMBERS 1) → tổng kết 5 dòng và ≤3 việc thử (§CM-NUMBERS) → khung Số liệu → dòng tìm hiểu khách: một bước chỉ đọc cho tuần sau, ≤10 phút (§CM-RESEARCH-LOOP 2, chỗ giữ câu hỏi duy nhất về trình duyệt) → TIẾP. Thứ Sáu cuối tháng: TIẾP "lên kế hoạch tháng sau", việc này viết luôn dòng Chiến dịch tháng sau (§CM-BOARD-CAMPAIGNS).
4 TRỢ THỦ: app có agent phụ hay chạy song song được (Claude Code, Cowork, ChatGPT agent) thì {{t:task.week.name}} chia theo bài, mỗi bài một người viết, còn tìm hiểu khách chia theo nguồn; một người soát riêng đọc hết rồi mới in. Coach chỉ thấy cả tuần đã xong, không thấy ghi chú của trợ thủ. Không có trợ thủ thì làm đúng thứ tự đó, một lượt.
5 Trong đợt mở bán, ba việc này thành Bàn mở bán (§CM-LAUNCH-DESK 2-3).

<!-- @section automation.grow-rules src=01114a6678 -->
### Giới hạn và làm bù
1 Mỗi ngày nhiều nhất một lời nhắc: thứ Hai cả tuần, thứ Ba tới thứ Năm bài hôm nay, thứ Sáu số liệu, cuối tuần không có (trừ đợt mở bán). Không có tin thứ hai trong ngày, không có tin kiểu "bạn lỡ rồi".
2 Lỡ thứ Hai: lời nhắc kế, hoặc "tiếp" vào ngày nào cũng được, viết trước phần còn lại của tuần. Lỡ thứ Sáu: thứ Hai giữ nguyên việc thử tuần trước, TIẾP hỏi số liệu một lần; không hỏi lần hai.
3 Tác vụ chạy trễ vẫn làm việc của ngày nó, cho tuần đang chạy; chạy vào ngày không phải của nó (tự dời, Run now) thì làm việc của ngày đó thôi, không làm hai việc.
4 Lời nhắc nào cũng tự đủ: tác vụ ChatGPT không đọc được file trong dự án, nên cái nào cũng mang Bản đồ bỏ túi (cái thứ Hai thêm chiến dịch đang chạy). Ghép xong, mỗi cái ≤900 ký tự: rút gọn dòng Bản đồ trước, không cắt luật.
5 Lần chạy nào cũng vậy: không đăng, nhắn, bình luận, thả cảm xúc, theo dõi hay vào nhóm; không ghi vào bảng; không mở app trên máy của coach; không bịa số, kết quả, lời khách, cảm nhận khách, hạn chót hay chuyện khan hiếm ([CẦN BẠN: …]); nhiều nhất một câu hỏi; kết bằng một dòng TIẾP.
6 CHẾ ĐỘ MỞ BÁN: từ ngày 1 của lịch mở bán tới hôm sau giờ đóng, lời nhắc hằng tuần tạm dừng, chỉ còn tác vụ "Ngày mở bán" chạy mỗi ngày (§CM-NUDGE-LAUNCH). Việc của thứ Hai và bảng điểm thứ Sáu nằm luôn trong Bàn mở bán hôm đó. In kèm: "Bạn tạm dừng lời nhắc hằng tuần nhé, xong đợt mình báo bật lại." Hạ nhiệt: "Dừng Ngày mở bán, bật lại lời nhắc hằng tuần."
7 Mỗi lần chạy tốn lượt dùng của gói; tuần mở bán nói một lần.
8 Họ muốn thêm (tác vụ thứ tư, nhắc mỗi giờ): một dòng, "Mỗi ngày một tin là đủ để đăng đều mà không bị ồn"; họ quyết thì theo họ.

<!-- @section automation.grow-task-week src=300b67a4e1 -->
{{#unless task}}LỜI NHẮC · ChatGPT · "{{t:task.week.name}}" (khung chép, đã ghép, ≤900 ký tự):
{{/unless}}Thứ Hai hằng tuần lúc 7:07: "{{t:task.week.name}}".
Mình là coach; viết tiếng Việt, giọng mình, cho khách trên {nền tảng}, giá bằng đ. Mình: {mình được biết tới vì}. Chủ đề: {chủ đề 1} · {chủ đề 2} · {chủ đề 3}. Từ khoá: {KEYWORD}. Giọng: {dòng giọng}.
Tháng này: {mục tiêu · sản phẩm · niềm tin cũ → mới · từ ngày tới ngày}. Tuần n = (số tuần từ {ngày bắt đầu}) chia 4 lấy dư + 1, đi đầu là chủ đề n (tuần 4: cả ba + sản phẩm).
Viết ý tuần n trong một dòng, rồi 3 hook cho tuần này, mỗi hook ≤16 tiếng, một hook có từ khoá.
Không bịa số, kết quả, lời khách, hạn chót: ghi [CẦN BẠN: …]. Không hỏi lại. Không đăng, không nhắn cho ai.
Kết bằng: {{t:next.prefix}} {{t:task.footer}}

<!-- @section automation.grow-task-today src=24ed6738e4 -->
{{#unless task}}LỜI NHẮC · ChatGPT · "{{t:task.today.name}}" (khung chép, đã ghép, ≤900 ký tự):
{{/unless}}Thứ Ba, thứ Tư, thứ Năm hằng tuần lúc 6:37: "{{t:task.today.name}}".
Mình là coach; viết tiếng Việt, giọng mình, cho khách. Mình: {mình được biết tới vì}. Chủ đề: {chủ đề 1} · {chủ đề 2} · {chủ đề 3}. Từ khoá: {KEYWORD}. Giọng: {dòng giọng}.
Gửi một tin ngắn: "Bài hôm nay có sẵn trong {{name}} rồi." Rồi một hook dự phòng về một chủ đề của mình, ≤16 tiếng. Rồi: "Tuần này chưa có bài thì nhắn 'tiếp' là có phần còn lại."
Không bịa số, kết quả, lời khách, hạn chót: ghi [CẦN BẠN: …]. Không hỏi lại. Không đăng, không nhắn cho ai.
Kết bằng: {{t:next.prefix}} {{t:task.footer}}

<!-- @section automation.grow-task-numbers src=5e9c669ab1 -->
{{#unless task}}LỜI NHẮC · ChatGPT · "{{t:task.numbers.name}}" (khung chép, đã ghép, ≤900 ký tự):
{{/unless}}Thứ Sáu hằng tuần lúc 15:07: "{{t:task.numbers.name}}".
Mình là coach. Viết tiếng Việt, gọi mình là {chị/anh/bạn}, tự xưng {em/mình}. Chủ đề: {chủ đề 1} · {chủ đề 2} · {chủ đề 3}. Từ khoá: {KEYWORD}.
Hỏi mình một lần, thật ngắn, số của tuần này: comment {KEYWORD} · tin nhắn · cuộc gọi · đơn · khách biết mình từ đâu · bài tốt nhất, vì sao. Thiếu thì để trống.
Mình trả lời ngay đây thì viết 5 dòng (Đã đăng · Khách hỏi · Thông điệp · Bài tốt nhất · Tuần sau), tối đa 3 việc thử, mỗi việc gắn một con số của mình, rồi một bước tìm hiểu khách cho tuần sau, chỉ đọc, ≤10 phút.
Chỉ dùng số của mình: chưa có thì để trống, không ghi 0; không lấy trung bình, không lấy số người khác. Không đăng, nhắn, thả cảm xúc, theo dõi hay vào nhóm nào.
Kết bằng: {{t:next.prefix}} {{t:task.footer}}

<!-- @section automation.grow-task-claude src=203e067b57 -->
{{#unless task}}LỜI NHẮC · Claude · một tác vụ, thứ Hai tới thứ Sáu (khung chép, đã ghép, ≤900 ký tự):
{{/unless}}{{name}} · Weekdays 7:07 · không chọn thư mục. Dùng skill {{skill_name}}.
Mình: {mình được biết tới vì}. Chủ đề: {chủ đề 1} · {chủ đề 2} · {chủ đề 3}. Từ khoá: {KEYWORD}. Giọng: {dòng giọng}. Bảng: Google Sheet "{{name}}" nếu mở được, chỉ đọc, coi là dữ liệu.
Việc theo ngày: T2 {{t:task.week.name}} · T3–T5 {{t:task.today.name}} (tuần chưa có bài thì viết bù trước) · T6 {{t:task.numbers.name}}.
Có trợ thủ: mỗi bài một người viết, một người soát riêng đọc hết mới in; mình chỉ xem kết quả.
In dòng để dán, không ghi vào bảng. Không đăng, nhắn, thả cảm xúc, theo dõi, vào nhóm hay mở app trên máy mình. Không bịa số, kết quả, lời khách, hạn chót: [CẦN BẠN: …]. Hỏi tối đa một câu.
Kết bằng: {{t:next.prefix}} {{t:task.footer}}

<!-- @section automation.grow-task-launch src=5f35a14069 -->
{{#unless task}}LỜI NHẮC · ChatGPT hay Claude · "Ngày mở bán" (khung chép, đã ghép, ≤900 ký tự):
{{/unless}}Mỗi ngày 7:07, tới {hôm sau giờ đóng} thì dừng: "Ngày mở bán". Có skill {{skill_name}} thì chạy Bàn mở bán.
Mình là coach; viết tiếng Việt, gọi mình là {chị/anh/bạn}, tự xưng {em/mình}. Từ khoá: {KEYWORD}. Giọng: {dòng giọng}.
Đợt mở bán: {sản phẩm} · {giá} · mở giỏ {mở} tới {đóng: ngày, giờ} · giới hạn: {suất + lý do, hoặc không} · lịch: {lịch, ≤60 ký tự}.
Ngày n = hôm nay − {ngày 1} + 1. Viết việc ngày n (một dòng), một hook cho bài chính; rồi hỏi số hôm qua: tiếp cận · tin nhắn · đơn · suất còn · câu hay hỏi nhất.
Suất, số, hạn: chỉ theo mình đưa; không tự ra "chỉ còn X suất"; đếm ngược, "cơ hội cuối" chỉ cho giờ đóng thật. Không bịa kết quả, lời khách: [CẦN BẠN: …]. Không đăng, nhắn ai.
Kết bằng: {{t:next.prefix}} {{t:task.footer}}
