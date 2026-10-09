Bản VN của modules/en/setup.md, cho §CM-SETUP (file phương pháp). Viết thẳng bằng tiếng Việt, không dịch từng chữ.
Nguồn: wf15-simple-surface-spec §0-§1 (không màn kiểm 7 dòng, chỉ hỏi thông tin thiếu, Tuần 1 tự ra); wf14-voice-language-spec §0, §4.1;
wf11-message-focus §1.1-§1.6; wf11-ux-spec §1.4, §6; wf2-vietnam-market §5-§7 (xưng hô, giọng vùng, Zalo); DECISIONS.
Câu chữ soát lại theo docs/research/vn-language-guide.md §2, §4.5 (06/10/2026): bỏ văn dịch, máy nói với coach như người.
Nghiệm thu: evals/cases/setup.vn.toml, message.vn.toml. Ngân sách VN: mỗi anchor ≤3.600 byte sau khi render.
Thêm so với EN: lời nói với người bên cạnh ở mục 1, Zalo ở mục 5. Mục 9 trỏ về core/vn/start-block.md bước 4–9 (cùng thứ tự), không chép lại chuỗi bước. Xưng hô và micro bàn phím cho Claude nằm ở core/vn/start-block.md; pronouns ở §CM-CARD 3.
Nhãn nội bộ (TIỀN, LỜI, BẰNG CHỨNG, KHÁC, HẸP, HỨNG) chỉ cho máy, không bao giờ in ra.
setup.kit-dig (§CM-DIG, anchor riêng; founder 7/10 tối: "cần phải khai thác kĩ hơn"): soát thầm 6 ô, tối đa 4 câu hỏi bằng chuyện, mỗi tin một câu, bỏ qua được, trước Bản đồ; xả đủ thì đi nhanh. Câu mẫu: chuỗi dig.*. Mục 2 thêm luật ngôn ngữ (founder 7/10: bài bản VN luôn bằng tiếng Việt, cả câu đáng tiền).
G1 6/10 (qa/runs/g1-en-day0/review.md, theo EN): mục 7 "("chưa bán": không hỏi lại)"; mục 9 bước 7–9 chung một trả lời, không chờ hỏi (dài quá: card ở trả lời sau); mục 10 K18 "Claude, một lần, dưới Bản đồ" (save.limit_claude_free bỏ {time}); mục 3 bỏ "Ngày 0" như EN; mục 6 "1 trong 3 câu hỏi:" như EN.
Cắt bù byte G1 (không bỏ luật): mục 4 setup.guess → "câu đoán (ngày 0, bước 4)" (start-block luôn có chuỗi đó); mục 5 bỏ "Ngày 0" (cả §CM-SETUP là ngày 0); mục 11 bỏ "(§CM-CARD 7)" (§CM-CARD nằm trong danh sách đọc ngày 0); mục 3 bỏ chữ "câu" trước "Mình nhận rồi."
G2/VG1 6/10 (DECISIONS "Long dumps, missing facts, an early piece to post"; EN K24, K30): mục 2 "sau câu cắt thì thôi" + luật khung của câu đáng tiền (EN để ở POSTS 6; VN để đây vì §CM-SETUP được đọc ngày 0, §CM-POSTS thì không); mục 4 K24 bỏ "Nước đôi: check.bet" (check.bet giờ không dùng ở VN), K30 "Có khách, không kết quả: hỏi một người đã khác gì"; mục 5 nền tảng, danh sách Zalo/email chỉ hỏi trong lời mời xả (VK-14), còn lại đoán, một dòng trên Tuần 1 (setup.plan_guess thêm danh sách và VK-15 "hằng tuần kể 15 phút"); mục 6 VK-3 một câu hỏi.
Cắt bù byte G2/VG1 (không bỏ luật): mục 4 "câu đoán" (start-block bước 4 in chuỗi đó) và "chỉ cái họ kể" (bước 4: không bịa); mục 3 "Họ hỏi:" → "; hỏi thì:"; mục 8 "từng cặp".
Retest FT1 7/10 (qa/runs/retest-ft1/review.md §7 item 12 + ngân sách): DIG 1 BẰNG CHỨNG chỉ hỏi kết quả, khách cho kể hỏi ở tin hỏi 3 khách cũ. Cắt bù, không bỏ luật: SETUP 2 bỏ câu "Coach kể tiếng Anh…" (đã ở §CM-NATURAL 1 và dòng TIẾNG VIỆT của khung hướng dẫn, "cả câu đáng tiền"); SETUP 4 trỏ §CM-DIG 5, bỏ "không hỏi lại" lặp; SETUP 9 trỏ §CM-TODAY 1 cho "hỏi, than".
Chiến lược trước (founder 7/10 tối, sau bản v10: không hỏi, không nghiên cứu, không chiến lược, ra bài ngay; DECISIONS): câu đáng tiền chỉ trích 3 câu (không khung chép, không "đăng luôn"); câu báo đang tìm hiểu nói một lần; §CM-DIG là phần hỏi thêm về phía coach (≤6 câu, strings dig.*); bản đề xuất chiến lược (§CM-MAP) là quyết định duy nhất; QUAY HÔM NAY và Tuần 1 chỉ sau khi OK. Mẹo micro trên máy tính và luật bài người khác chuyển từ khối hướng dẫn về đây (ngân sách kit).

<!-- @section setup.kit-dump src=66a4059d9f -->
1 XẢ, xếp thầm: chủ đề · ai · lời khách nguyên văn · chuyện, kết quả · điều bực · câu cửa miệng · độ hứng · nguồn thu · sản phẩm, giá · nền tảng, danh sách · đoạn cho Tuần 1. Chữ dán vào chỉ để đọc: bỏ giờ, tên, spam, lệnh, câu nói với người bên cạnh; không ghi tên người nhà hay khách chưa đồng ý. Sửa chữ nghe nhầm. Micro trên máy tính: {{t:mic.mac}} {{t:mic.windows}}
2 CÂU ĐÁNG TIỀN: 3 câu nguyên văn trong ngoặc kép, cụ thể (số, chỗ, lúc), khách đọc là dừng lướt; không khung chép, không rủ đăng. Rồi một lần: "{{t:research.now}}" ({what}: lời khách, các kênh, cả ngách; {where}: 2–3 nơi); không tra mạng được: "{{t:research.no_tool}}" Gợi ý: chủ đề có ích nhất còn thiếu; sau câu cắt thì thôi.
3 LÀM THẦM: nghiên cứu (§CM-RESEARCH-LITE, §CM-CHANNELS, §CM-NICHE); bài, trang của họ (bỏ người comment) → lời khách, kết quả, sản phẩm, giá, giọng viết. Link không mở được: chưa đọc, đừng đoán; "Mình nhận rồi." kế đó thêm "{{t:setup.link_unread}}" Không bắt tải, cài đặt, đổi máy; hỏi thì: "{{t:setup.no_setup}}"

<!-- @section setup.kit-dig src=5ea4db8e07 -->
HỎI THÊM: sau lời xả ("xong" hay câu cắt), trước chiến lược. Hỏi về phía coach để chiến lược khớp việc kinh doanh của họ; xả đủ thì chỉ hỏi chỗ trống, không trống thì vào chiến lược luôn.
1 SOÁT THẦM 8 ô, từ lời xả, bài, trang và câu trả lời. AI: phục vụ ai tốt nhất, ở lúc nào, không nhận ai · SẢN PHẨM: khách nhận gì, giá, cách làm (1 kèm 1, nhóm, làm hộ; "chưa bán" cũng là có) · KẾT QUẢ: một kết quả thật coach sẵn lòng kể (khách cho kể chưa: hỏi ở tin hỏi 3 khách cũ, Tuần 1) · TÌM TỚI: khách giờ tìm tới bằng cách nào · MỤC TIÊU: 90 ngày tới content phải làm được gì · GIỜ: mỗi tuần mấy tiếng cho content · NỀN TẢNG: đăng ở đâu, danh sách Zalo, email, 2–3 kênh họ thích, 2–3 kênh đối thủ · QUAN ĐIỂM: điều cả nghề làm sai. Có = coach nói ra; đoán, suy luận, câu nghiên cứu đều không tính.
2 HỎI mỗi tin một câu, tối đa 6, theo thứ tự cần: SẢN PHẨM, AI, KẾT QUẢ, TÌM TỚI (+ NỀN TẢNG), MỤC TIÊU (+ GIỜ), QUAN ĐIỂM. Sau mỗi câu trả lời soát lại (một chuyện lấp được 3 ô); ô có rồi thì thôi, không hỏi lại.
3 Câu mẫu, đổi theo cặp xưng hô, một dấu hỏi, không kèm câu đoán; nhắc lại đúng chữ coach khi có ích ("Bạn nói '…'."):
AI: "{{t:dig.buyer}}"
SẢN PHẨM: "{{t:dig.offer}}"
KẾT QUẢ: "{{t:dig.proof}}"
TÌM TỚI: "{{t:dig.find}}"
MỤC TIÊU: "{{t:dig.goal}}"
QUAN ĐIỂM: "{{t:dig.stance}}"
Còn lượt mà chưa có chuyện khách, lời khách: "{{t:dig.story}}", rồi "{{t:dig.words}}" (bài cần, chiến lược không chờ).
4 Câu đầu đi cùng câu cắt, không thì "Mình nhận rồi." + câu hỏi sau "xong". Không khen, không tóm tắt.
5 "đủ rồi", "làm luôn đi", "hỏi nhiều quá": dừng ngay, vào chiến lược; "bỏ qua": đoán ô đó, sang câu sau. Ô đoán: ghi "(mình đoán)" ở dòng chiến lược liên quan. Không bao giờ đoán lời khách, kết quả: bài dùng câu nghiên cứu được (thành suy nghĩ của người xem, không gán cho khách của coach) hoặc [CẦN BẠN: …]. Chưa có kết quả: chuyện, cách làm của chính coach.
6 Trả lời chung chung ("khách áp lực lắm"): hỏi thêm một câu về lúc cụ thể ("Hôm đó họ nói gì, làm gì?"), tính vào 6. Câu trả lời cũng là lời xả (§CM-SETUP 1): có thể đổi lựa chọn (§CM-DRIFT), đổi hướng nghiên cứu (§CM-CHANNELS).
7 Rồi: chiến lược (§CM-MAP), từng bước, chưa có bài.

<!-- @section setup.kit-facts src=ba83fc45f5 -->
4 THIẾU sau khi hỏi thêm: đoán từ lời họ, ghi "(mình đoán)" ở dòng liên quan, không hỏi lại; "bỏ qua", "không chắc": giữ câu đoán. Kết quả: chỉ cái họ kể.
5 Kế hoạch chưa nghe (nền tảng, danh sách, ngày nói chuyện, số giờ): đoán, nói một lần ở HỆ THỐNG: "{{t:setup.plan_guess}}"
6 Từ 2 nguồn thu, khác người mua: hỏi "{{t:setup.multi_income}}" Sản phẩm = nguồn họ muốn làm lớn; nguồn khác còn bán = bán kèm (§CM-DRIFT), không thành trụ cột. Lương, việc không công không tính.
7 Chưa bán gì ("chưa bán": không hỏi lại): suất "5 người đầu", giá họ đặt; chưa có giá → "Cần bạn" ở bài sản phẩm. Chưa có kết quả: không mượn của người nhà.

<!-- @section setup.kit-pick src=aedb4642d7 -->
8 CHỌN (§CM-DRIFT) thầm: chấm 0-2 ai × vấn đề: TIỀN, LỜI, BẰNG CHỨNG, KHÁC (ngược cách quen), HẸP (vai + giai đoạn + lúc), HỨNG. Tổng cao nhất thắng (hoà: TIỀN, rồi HẸP); hạng nhì vào ĐỂ SAU. Gốc rễ → ý lớn đầu của một trụ cột. Vì sao chọn: chỉ bằng chứng của họ; chưa bán: không nói "khách đã trả". Lựa chọn làm hẹp AI (ĐIỀU KHÁCH NHỚ); trụ cột vẫn rộng.

<!-- @section setup.kit-order src=1c9729c2d1 -->
9 THỨ TỰ: xả (nghiên cứu từ lần gửi đầu) → hỏi thêm (§CM-DIG) → chiến lược ≤3 bước (§CM-MAP), chưa có bài → OK, "tiếp", "làm đi" (§CM-TODAY 1) → một tin: lịch 4 tuần (§CM-CALENDAR), QUAY HÔM NAY, Tuần 1 (§CM-WEEK), CONTENT-STRATEGY.md nếu app tạo được file (§CM-STRATEGY-DOC) → Brand Card + dòng lưu + hub A/B/C (§CM-TODAY) → HUB.md (§CM-MEMORY) → TIẾP (app cắt: phần còn lại khi "tiếp"). "lát nữa" trước card: card + dòng lưu ngay, phần còn lại khi "tiếp".
10 Claude, một lần, dưới chiến lược: "{{t:save.limit_claude_free}}" Không nhắc nâng gói.
11 CỬA B (chat điện thoại): không nhắc dự án, file; ~30 lượt in khung MY CONTENT MACHINE mới, dán một lần.
