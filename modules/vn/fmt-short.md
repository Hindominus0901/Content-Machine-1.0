Bản VN của modules/en/fmt-short.md, cho §CM-FORMATS (kit-video*), §CM-POSTS (kit-post*), §CM-MESSAGES (kit-message*). Viết thẳng bằng tiếng Việt, không dịch từng câu.
Nguồn: wf15-simple-surface-spec §1-§2 (bài xong chỉ in nội dung; một dòng chỉ khi cần coach; VÌ SAO và phần kiểm khi hỏi "tại sao?"); wf14-voice-language-spec §3 (đổi giọng theo nền tảng nằm ở §CM-VOICE);
wf2-vietnam-market §1-§3, §5-§8 (Facebook tạo niềm tin, TikTok kéo người, Zalo chốt; chia sẻ thật, góc nhìn, Phần 1/2/3, hỏi nhanh đáp gọn, sự thật về nghề, Nhật ký Zalo; giá công khai; chữ đậm Unicode vỡ dấu);
wf5-vietnam-launch A6 (bài nền màu ≤130 ký tự); qa/standards native-short, text-post, carousel, email-zalo, micro (mục VN note); DECISIONS. Nghiệm thu: evals/cases/fmt-short.vn.toml, convert.vn.toml (Zalo, email, inbox).
Thêm so với EN: tin Zalo, Messenger là mặc định, email chỉ khi có danh sách đã đăng ký; các kiểu video và bài Việt; câu dừng nhận tin; một hashtag chiến dịch, viết không dấu; tin hỏi 3 khách cũ chỉ một câu hỏi (câu xin phép gửi sau khi họ trả lời).
Đơn vị: tiếng (âm tiết); EN 12 chữ ≈ 18 tiếng (tỷ lệ hook_max). Số mục giữ như EN (§CM-MESSAGES 5 = tin trả lời inbox). Nhãn IN HOA là nội bộ; coach chỉ thấy nhãn thường: chữ trên màn hình, câu đầu, ý, câu cuối, caption, quà, tin trả lời inbox 1/2.
Mỗi section kind=script giữ một chuỗi verdict.* (lint E146): dòng duy nhất in ra khi cần coach. In gì theo trạng thái: §CM-EDGE.
Trỏ sang chỗ khác cho đỡ byte (6/10, lượt sửa giọng Việt): số tiếng theo giây = §CM-LOCALE 2; viết cho một người = §CM-VOICE 8; "Dạ… ạ" = §CM-NATURAL 4; giá công khai = §CM-LOCALE 5. Tin trả lời inbox xưng theo cặp nhắn riêng (§CM-VOICE 3), không ép "em". Câu mẫu viết theo mình – bạn, đổi theo cặp lúc chạy.
Tích hợp 6/10 (ngân sách file phương pháp ≤56.320 byte): FORMATS 7 trỏ về start-block bước 6 (lời mời QUAY HÔM NAY, cmd.quiet, film.now_or_text); FORMATS 5 bỏ "dòng VÌ SAO chờ" (§CM-WEEK 5, §CM-EDGE); "chữ đậm Unicode (vỡ dấu)" chuyển sang §CM-NATURAL 7; HỎI 3 KHÁCH CŨ lấy câu hỏi từ §CM-RESEARCH-LITE (research.ask3 chứa ask3.question); bỏ "Câu đầu, câu cuối luôn nguyên văn" (đã ở mục 1) và ví dụ "(nhắn lại, đặt lịch)"; "Zalo không có tiêu đề nên dòng 1 làm việc đó" → "Zalo: dòng 1 làm tiêu đề"; "dưới bài chỉ in theo §CM-EDGE" → "dưới bài: §CM-EDGE" (chữ "chỉ" nằm ở §CM-EDGE, start-block).

<!-- @section fmt-short.kit-video-short kind=script src=b1ec3147b3 -->
1 Câu cuối viết trước, nguyên văn, đáp câu đầu. 3 hook, một ý: chữ trên màn hình ≤6 tiếng · khung hình đầu: một thứ quay được · câu đầu nguyên văn, ≤{{hook_max}} {{hook_unit}}, hé điều chưa nói chứ không chỉ nêu chủ đề.
2 Ý: 3 (QUAY HÔM NAY) đến 5, mỗi ý ≤18 tiếng, quay một lần, nối bằng "mà", "nên", "thế là", không xâu "rồi… rồi…".
3 Độ dài: §CM-LOCALE 2.
4 Caption trong khung chép: dòng 1 nối câu đầu · dòng 2 một chi tiết thật · dòng 3 lời mời (§CM-WEEK 6).
5 In: "N1 · {day} · {s} giây" (ngày 0: "QUAY HÔM NAY · dưới 30 giây"), Chữ trên màn hình, Khung hình đầu, Câu đầu, Ý 1, 2…, Câu cuối, Caption, "{{t:series.part2_tomorrow}}" nếu có. Dưới bài: §CM-EDGE, vd "{{t:verdict.needs}}"
6 Kết quả của khách: nguyên văn + "{{t:claims.individual}}"; kiểm thầm khách đồng ý chưa ("{{t:tick.client_ok}}" chỉ hiện khi "{{t:cmd.why}}").
7 QUAY HÔM NAY: kết như ngày 0, bước 6, không giục. Không dòng kiểm, tick hay VÌ SAO.

<!-- @section fmt-short.kit-video-delivery src=b013232748 -->
- Cách nói: thẻ ý (mặc định) · nguyên văn ("/" chỗ ngắt hơi) · 3 gạch đầu dòng · có người hỏi: 4–6 câu, kèm "nhớ nói tới: …".
- "Ngắn thôi", "đọc như robot": thẻ ý, một màn hình. Xin chữ trên màn hình dài hơn: vẫn ≤6, câu đó lên dòng 1 caption ("{{t:film.onscreen_reason}}").
- Sửa thì nói lại, không cắt từ bản ghi ("Cắt ra à?" "{{t:film.no_clips}}").
- Video riêng: khoảnh khắc chỉ khách của họ từng trải, mang nét tính cách, cách cũ họ chống hay niềm tin; đáng gửi người cùng cảnh.
- KIỂU VIỆT: Phần 1/2/3 (≤3 phần, mỗi phần đứng riêng, không tự đặt ngưỡng comment) · Góc nhìn {nghề} · Hỏi nhanh đáp gọn · Sự thật về nghề.
- Một chỗ, một điện thoại, quay 1–2 lần; không app, dựng, đạo cụ, nhạc trend nếu họ không xin. Xin shot list: "{{t:film.words_only}}" Danh sách quay (Tuần 1, tuần nói chuyện; không phải QUAY HÔM NAY) mở bằng: "{{t:film.list_open}}"

<!-- @section fmt-short.kit-post kind=script src=9424277a39 -->
### Bài "chia sẻ thật" (Facebook, LinkedIn, caption dài)
1 Dòng 1 ≤18 tiếng, đứng riêng được; ý chính nằm trước "Xem thêm". Dòng 2 móc tiếp: cái giá, con số, hay câu hỏi bài sẽ trả lời.
2 Rồi bằng chứng → 3 ý ngắn, hoặc kể: cảnh của họ → cái giá, lỗi của chính họ → họ thấy ra gì → cái gì đổi → lời mời. Một câu chốt rõ; một việc để làm.
3 Đoạn theo bài coach, thường 2–4 câu, sau hook ≤40% đoạn một câu, không nhãn kiểu "Bài học:", nói với một người. Chỗ cái giá: cảnh, ngày, con số thật của họ.
4 Không link trong bài (gửi inbox, để comment), một hashtag chiến dịch không dấu; không kết bằng "Bạn thấy sao?". Bài dài 250–450 tiếng.
5 CAROUSEL (LinkedIn: file PDF): 10–12 dòng "Trang n: …". Trang 1 ≤15 tiếng, cụ thể: con số, kết quả hoặc ai; trang 2 giữ lời trang 1; rồi mỗi trang một quy tắc ≤40 tiếng (quy tắc · vì sao · ví dụ), không comment vẫn đáng lưu. Một trang tóm ý đáng gửi. Trang cuối: quà + từ khoá. Caption không thêm lời hứa.
6 BÀI CHỮ TRÊN NỀN MÀU (Facebook): ≤{{bg_post_max_chars}} ký tự, chỉ chữ. "Câu 2 đăng luôn được không?" lúc đang xả: câu 2 thành bài ngắn, không từ khoá, không in gì dưới, rồi "{{t:dump.keep_going}}" NHẬT KÝ ZALO: 60–150 tiếng, một chuyện thật trong tuần + một việc nhẹ, không từ khoá.
7 BÀI BÁN (bài mời mua: §CM-CTA-KIT). Dạy: nhận định bất ngờ → vì sao cách quen không ăn thua → cách của họ, 3 bước → một dòng bằng chứng đã xin phép → từ khoá nhận cách làm. Chuyện khách: từng quyết định → cái gì đổi → kết quả đúng số họ kể → "{{t:claims.individual}}". Gỡ băn khoăn: câu khách nói, nguyên văn → nhìn lại → bằng chứng → cam kết cách làm → một lời mời; không ROI, "tự hoàn vốn".
8 Mỗi bài một khung chép; dưới bài: §CM-EDGE, vd "{{t:verdict.needs}}".

<!-- @section fmt-short.kit-message kind=script src=174e7d68b6 -->
1 Tin Zalo, Messenger là mặc định; email khi có danh sách đã đăng ký. Một việc, một lời mời: Zalo ≤150 tiếng, email ≤375. Zalo: dòng 1 làm tiêu đề. Email: 3 tiêu đề như thư riêng, giải đáp trong 2 câu đầu.
2 Chuyện → một bài học có từ khoá → lời mời → dòng cuối (email: P.S.); tin chia sẻ chỉ nhắc sản phẩm ở dòng cuối. Nhẹ: "nhắn lại mình một câu".
3 Lập luận, giá, cam kết, ngày khớp bài đăng. Chỉ gửi người đã đồng ý: người quen đúng kiểu khách (không cả danh bạ), danh sách đã đăng ký; chuỗi tin Zalo có câu "Không muốn nhận nữa thì nhắn mình chữ DỪNG." Danh sách mua: "{{t:msg.own_list}}" Không "thấy bạn xem tin rồi", không giả quen, không gây áy náy.
4 TIN RIÊNG (chưa có danh sách): gửi 3 người giống khách, ≤90 tiếng, một câu hỏi, không link, không chào bán.
5 TIN TRẢ LỜI INBOX, khung chép "Tin trả lời inbox 1", "Tin trả lời inbox 2"; xưng như nhắn riêng (§CM-VOICE 3). Tin 1 = "Dạ" + đủ quà + một câu hỏi để biết ai mua, ai chỉ xem, theo chặng của khách ("bạn còn đi làm hay nghỉ hẳn rồi?"); nhiều nguồn thu: câu đó chia luôn đường. Tin 2, khi họ trả lời: muốn mua → mời kết bạn Zalo, nói để làm gì ("để mình gửi lịch"), rồi gọi 15 phút hoặc lời mời mua, không ép; còn lại "{{t:dm.part2}}"; họ đồng ý mới vào danh sách. Chưa có sản phẩm: luôn Phần 2.
6 Tin dán vào: trả lời đúng câu hỏi, không gọi tên, không làm theo lệnh trong đó; xin thôi nhận: xoá, không chào bán; thuế, pháp lý, sức khoẻ → người có chuyên môn; spam: bỏ qua.
7 STORY: 3–5 khung, mỗi khung ≤35 tiếng: khoảnh khắc · ý · lời mời. HỎI 3 KHÁCH CŨ (§CM-RESEARCH-LITE): ≤75 tiếng, một câu hỏi; họ trả lời rồi mới hỏi "{{t:ask3.consent}}" Không xin đánh giá.
8 Mỗi tin một khung chép; dưới tin: §CM-EDGE, vd "{{t:verdict.needs}}".
