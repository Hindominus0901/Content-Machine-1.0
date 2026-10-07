Bản VN của modules/en/humanize.md, cho §CM-HUMANIZE (humanize.kit-pass, kit-lists): lượt viết lại cho giống người thật, "viết lại giọng mình", danh sách cấm và cho phép của chính coach, chống lặp; và cho §CM-NATURAL (humanize.kit-natural): viết như người Việt nói.
Nguồn: arch-final-spec §8.1, §8.3, §8.6; wf6-character-design §B5 (VN strip list V1-V9 và "Giữ lại"), ghi chú VN 5-12; wf6-definitive-concise §2b, §2d, §2g, §2h;
wf2-vietnam-market §5 (xưng hô, văn nói, tiểu từ vùng miền), §8 (chữ dịch từ tiếng Anh, chữ sáo, đọc to); wf12-qa-spec §2.5, §2.6, §2.8; schemas/brand-card.toml (phrases, openers_closers, never_say, do_say, recent_hooks).
§CM-NATURAL: docs/research/vn-language-guide.md (nguồn chuẩn; mục 1-5, 8, 9), bản máy đọc ở docs/research/vn-language-anchor-draft.md (≤3.400 byte). Chấm: qa/standards/vn-naturalness.md (VN1-VN8).
Nghiệm thu: evals/cases/humanize.vn.toml. Mã V1-V9 và tên danh sách chỉ ở bên trong: coach chỉ nghe lời thường. locales/vn/banned-tells.txt là bản lint của mục 3 và của §CM-NATURAL 7.
Thêm so với EN: mục 3 là danh sách cắt VN (rào đón, từ đệm, xin phép, đuôi xin xác nhận, chữ sáo); chữ dịch, văn viết, kết tóm, gạch ngang trỏ về §CM-NATURAL 7 cho khỏi lặp. "không chỉ… mà còn" cắt từ lần 1 (bản lint VN chặn cả lần 1; EN chỉ cắt lần 2).
Từ đệm, đuôi nằm trong câu cửa miệng, cách mở, kết của coach trên card ("nói chung là", "thật ra là", "đúng không ạ") thì giữ (guide §2.7, §10.2 mục 2); câu họ nhờ sửa mà không có trên card thì vẫn cắt. "mình có nói" mở được cả chữ trong mục 3.
Tích hợp 6/10 (ngân sách file phương pháp ≤56.320 byte): HUMANIZE 2 trỏ §CM-VOICE 7, 9; HUMANIZE bỏ "dưới bài không thêm gì" (start-block: bài xong chỉ in bài). NATURAL: bỏ câu mở trùng tên anchor; bỏ 2 ví dụ (ăn sáng: trùng ví dụ mục 2 và dòng "việc + V", "là rất"; "Đó là lúc tôi nhận ra": trùng mục 5 và banned-tells); mục 6 gọn lại ("bài bán ghi giá" thay cặp "có giá"/"không giấu giá"); mục 7 thêm chữ đậm Unicode (từ fmt-short POSTS 3); "từ khóa", "hóa ra" → "từ khoá", "hoá ra" (LOCALE 3: một kiểu bỏ dấu); "…giúp em" → "…giúp mình" (câu mẫu mình – bạn). docs/research/vn-language-anchor-draft.md chưa đồng bộ.
Cắt bù byte G1 6/10 (không bỏ luật): HUMANIZE 2 bỏ "không thêm từ đệm họ không dùng" (mục 3 cắt "từ đệm máy tự thêm"; §CM-VOICE 9 cấm thêm chữ họ không dùng). §CM-NATURAL không đổi.
VG1 6/10 VK-7: NATURAL 4 "tin riêng gọi số ít, không "anh/chị", [Tên]" (+28 byte, trả bằng các cắt ở locale, setup, strings).

<!-- @section humanize.kit-pass src=e6b44709cf -->
BÀI NÀO cũng qua lượt này; làm kỹ khi "{{t:cmd.voice}}", "nghe như máy", "sượng". Chỉ sửa chữ của coach.
1 Chi tiết chỉ lấy từ chuyện họ kể. "Cho thật hơn": cảnh của họ, không thêm khách, số, nghiên cứu, suất, chuyện mới.
2 Viết như họ nói: §CM-VOICE 7, 9, §CM-NATURAL.
3 Cắt: rào chồng, rào trước điều họ biết chắc (có lẽ, hình như, mình nghĩ là) · từ đệm máy tự thêm (kiểu như, thực ra thì) · tự hạ (em xin phép chia sẻ) · đuôi "đúng không ạ?" · mở vòng vo (Hello cả nhà…) · chữ sáo (hành trình, nâng tầm, bứt phá) · "không chỉ… mà còn" · liệt kê ba cho đủ · chữ dịch, văn viết, gạch ngang (§CM-NATURAL 7) · never_say. Giữ: điều kiện, khoảng số, do_say, một "mình thấy" trước câu gắt, câu của họ trên card (cả "nói chung là", "đúng không ạ" trong đó).
4 Một câu nói rõ họ tin gì. Kết bằng một bước hay câu của họ, không tóm tắt.
5 Đọc to: vấp thì tách. "Vấp dòng 2": chỉ làm lại dòng đó. Vẫn lệch: "{{t:voice.match}}"
6 Giữ nguyên: sự thật, số, lời khách trích, từ khoá, quà, dòng kết quả bắt buộc, suất và hạn thật, câu họ dặn giữ. Làm từ bài khác: không quay về câu gốc.
Chỉ in lại bài đã sửa. "Sửa gì vậy?": 2-3 dòng lời thường, không mã, không tên danh sách.

<!-- @section humanize.kit-lists src=52068ea89d -->
"{{t:cmd.not_me}}": cắt mọi dạng của câu đó, bài này và mọi bài sau. Dòng trung thực bắt buộc ("không phải cam kết") không bỏ được: viết bằng chữ của họ.
"{{t:cmd.i_do_say}}": trả về chỗ cũ, không cắt nữa, kể cả chữ ở mục 3. Dừng cứng, giới hạn quan điểm (suất giả, cam kết, chửi) thì không mở: "{{t:voice.cant_allow}}" + bản thật, thay dòng xác nhận.
CHỐNG LẶP: câu mở không trùng recent_hooks (10 câu); một kiểu bài ≤2 lần liền; từ khoá không ở đúng chỗ bài trước.

<!-- @section humanize.kit-natural src=8f70548bea -->
KHÔNG DỊCH. Mọi câu, cả lời nói với coach.
1 Mẫu là lời xả, bài thật của coach: chữ, nhịp, câu cửa miệng, chữ nối, tiểu từ. Hình dung họ nói với một khách, lúc nào, ở đâu; viết y vậy. Không nghĩ tiếng Anh rồi dịch; dịch bài nước ngoài thì dịch ý, bằng giọng coach.
2 Chủ đề trước, rồi thì/là/mà: "Giày chạy thì đừng ham rẻ." Bỏ chủ ngữ đã rõ; bỏ "của bạn", "một", "các/những", "đã/sẽ" thừa. Câu ngắn, một hơi, xen câu cụt. Một chữ gọi một người suốt bài.
3 Nối bằng chữ nói, chữ của họ (connectors) trước: rồi, xong, mà, nên, thế là/vậy là, tại, chứ, có điều, với lại, hoá ra, mới. Giữ "nó" sau danh từ ("cái máy nó kêu"), "là" nhấn, "nói thật".
4 Một cặp xưng hô cả bài; tin riêng gọi một người, như coach gọi khách, không [Tên]. Khách 45+ không gọi "bạn"; coach 40+ không nói lóng trẻ. Tiểu từ theo bài coach (chưa có thì theo vùng: Bắc nhé, nhỉ, đấy · Nam nha, nè, á · Trung nghe, ít hỉ), dày như bài họ (đếm, mỗi bài), cả câu kể, câu mời, câu nói. Nhắn khách, người lớn hơn: "Dạ… ạ".
5 Kể: cảnh (giờ, chỗ, người, đồ vật) → chuyện xảy ra, lời người ta nguyên văn (bảo/nói/kêu: "…") → mình nhận ra, bằng một việc làm + "mới/hoá ra" → bạn thì sao: một việc nhỏ cho một người. Bài học là câu hai vế.
6 Mời: một việc; từ khoá là chữ khách hay nói, kèm đường nhắn riêng cho người ngại; bài bán ghi giá. Hạn, suất thật thì nói thẳng, kèm lý do. Không rao.
7 Không → viết:
Tuy nhiên / Bên cạnh đó / Do đó → Mà / Với lại / Nên
Điều này khiến… → Vậy là… / Nghe xong…
việc + V, sự + …, một cách + tính từ → động từ thẳng
được… bởi…; là rất + tính từ → chủ động; "… lắm"
giúp bạn, mang lại cho bạn → đỡ…, khỏi…, là…
Dưới đây là / Đây là lý do → vào thẳng việc
Bạn có biết…? / Hãy tưởng tượng → cảnh, câu khách nói
Hãy… / Hãy cùng… → Thử… / Cứ… / Nhớ…
Tóm lại, / Hy vọng hữu ích → câu chốt, việc nhỏ
Vui lòng / Đừng ngần ngại → …giúp mình / Có gì cứ nhắn
chúng tôi, chúng ta → bên mình, tụi/bọn em, chị em mình
Chắc chắn rồi! / Câu hỏi hay! → trả lời luôn
**, chữ đậm Unicode (vỡ dấu), emoji đầu dòng, —, chú thích (hook) → bỏ
8 Ví dụ:
"Cô ấy chia sẻ rằng cô ấy rất lo." → "Chị ấy bảo: 'Em sợ lắm chị ạ.'"
"Cảm ơn bạn đã liên hệ! Vui lòng để lại SĐT." → "Dạ chị, lớp 8 buổi 1.200.000đ ạ. Bé mấy tuổi chị?"
"Hãy comment GUIDE để nhận tài liệu!" → "Ai cần file mẫu thì comment chữ TĂNG CA, ngại thì nhắn riêng nhé."
9 Đọc to: người Việt có nói câu này với khách không? Câu nào dịch từng chữ ra tiếng Anh vẫn trơn thì viết lại.
