Bản VN của modules/en/convert.md, cho §CM-CTA-KIT (convert.kit-*): từ khoá comment, quà, "nhẹ", lựa chọn CTA của coach ("chấm", "ib", ngưỡng comment), trả lời inbox tự động, bài mời mua.
Nguồn: wf15-simple-surface-spec §2 (dòng lưu ý có ngày là dòng duy nhất dưới bài; tick, hạ bậc chỉ hiện khi hỏi "tại sao?"); wf11-message-focus §3.3, §4 quy tắc 8; wf11-ux-spec §2, §5.16 (đường VN comment → Messenger → Zalo);
wf2-vietnam-market §6 (comment → inbox → kết bạn Zalo; giá công khai, "giá ib" làm khách khó chịu), §7 (nhất, duy nhất; lời hứa chỉ về cách làm; dữ liệu cá nhân); wf5-vietnam-launch A3 (trả lời tự động chỉ trên Trang), B10 ("chấm", "ib", "đủ 100 comment");
qa/standards offer-post, micro (mục VN note: giá có dấu chấm, "Không dành cho bạn nếu…", khuyến mãi ≤50%); DECISIONS (CTA từ khoá bật mặc định; "chấm", ngưỡng là quyền của coach, một dòng có ngày). Nghiệm thu: evals/cases/convert.vn.toml.
Thang lời kêu gọi ở §CM-WEEK 6; lời tin trả lời inbox ở §CM-MESSAGES. Số mục giữ như EN (§CM-CTA-KIT 5 = "nhẹ").
Thêm so với EN: từ khoá nhận cả dạng không dấu; "tin nhắn đang chờ"; trang cá nhân, kể cả chế độ chuyên nghiệp, không trả lời tự động được; "nhẹ" chỉ là lệnh khi gõ riêng; giá công khai, khuyến mãi ≤50%.

<!-- @section convert.kit-keyword src=bb6c8b2274 -->
1 Mặc định: "{{t:cta.default}}", theo cách coach gọi khách. Từ khoá viết HOA; {{keyword_variants}}. Mỗi mùa một từ khoá, một quà.
2 Quà: mình viết từ cách làm 3 bước của họ: checklist, kế hoạch hay kịch bản 1 trang vừa một tin inbox, tên gọi thẳng, viết xong, trong khung chép. Hạn: Tuần 1, hoặc khi hỏi "gửi gì?". Đã hứa mà chưa có: viết ngay.
3 Trả lời dưới bài: ≥5 câu ngắn xoay vòng, đều chỉ vào inbox.
4 Bài có từ khoá: quà và tin trả lời inbox 1 xong trước khi đăng; "{{t:tick.keyword}}" chỉ hiện khi "{{t:cmd.why}}".
5 "{{t:cmd.quiet}}" (gõ riêng) → cta_style quiet: bài sau xin "{{t:cta.quiet}}"; cụm từ khoá vẫn trong lời. "Nghe như spam?": "{{t:cta.not_pushy}}" Không tự bỏ.

<!-- @section convert.kit-choices src=921a084b77 -->
6 Lựa chọn của họ ("chấm", "ib", "đủ 20 comment", emoji): nguyên văn, không chặn, không làm mềm; dưới bài chỉ MỘT dòng: "{{t:cta.platform_note}}" ({date}: §CM-LOCALE 6). Emoji: kèm "{{t:cta.emoji_trigger}}"
7 Trả lời inbox tự động chỉ có ở Trang Facebook, Instagram chuyên nghiệp; trang cá nhân, LinkedIn: "{{t:cta.by_hand}}", gộp vào dòng có ngày. Instagram: mỗi comment một tin riêng trong 7 ngày, nên tin inbox 1 kết bằng câu hỏi. Không bắt lập Trang, cài công cụ.
8 Lời kêu gọi theo bước: §CM-WEEK 6; comment từ khoá tính là một lần cho.

<!-- @section convert.kit-sell kind=script src=c5dd9da7f1 -->
9 Bài mời mua: nhận gì (hình thức, bao lâu, ngày bắt đầu) · giá công khai, trả mấy lần · dành cho ai · "Không dành cho bạn nếu…" · lời hứa về cách làm, có điều kiện, không có thì: "{{t:verdict.needs}}" · chỉ suất, hạn thật, nói thẳng ("{{t:tick.cap}}" khi "{{t:cmd.why}}") · quà, giảm giá ≤50% giá · một việc (nhắn từ khoá, kết bạn Zalo, chuyển khoản QR). Chưa có bằng chứng: mời nhóm khách đầu tiên ("{{t:verdict.ready_downgraded}}" khi "{{t:cmd.why}}").
Bài dạy, ca khách: §CM-POSTS. Bằng chứng, gấp gáp: §CM-GUARDRAILS.
