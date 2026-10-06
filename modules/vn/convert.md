Bản VN của modules/en/convert.md, cho §CM-CTA-KIT (convert.kit-*): từ khoá comment, quà, "nhẹ", lựa chọn CTA của coach ("chấm", "ib", ngưỡng comment), trả lời inbox tự động, bài mời mua.
Nguồn: wf15-simple-surface-spec §2 (dòng lưu ý có ngày là dòng duy nhất dưới bài; tick, hạ bậc chỉ hiện khi hỏi "tại sao?"); wf11-message-focus §3.3, §4 quy tắc 8; wf11-ux-spec §2, §5.16 (đường VN comment → Messenger → Zalo);
wf2-vietnam-market §6 (comment → inbox → kết bạn Zalo; giá công khai, "giá ib" làm khách khó chịu), §7 (nhất, duy nhất; lời hứa chỉ về cách làm; dữ liệu cá nhân); wf5-vietnam-launch A3 (trả lời tự động chỉ trên Trang), B10 ("chấm", "ib", "đủ 100 comment");
qa/standards offer-post, micro (mục VN note: giá có dấu chấm, "Không dành cho bạn nếu…", khuyến mãi ≤50%); DECISIONS (CTA từ khoá bật mặc định; "chấm", ngưỡng là quyền của coach, một dòng có ngày). Nghiệm thu: evals/cases/convert.vn.toml.
Thang lời mời ở §CM-WEEK 6; lời tin trả lời inbox ở §CM-MESSAGES. Số mục giữ như EN (§CM-CTA-KIT 5 = "nhẹ").
Trỏ sang chỗ khác (6/10): quà, giảm giá ≤50% = §CM-GUARDRAILS; đường comment → Messenger → Zalo, QR = §CM-LOCALE 5.
Thêm so với EN: từ khoá nhận cả dạng không dấu; "tin nhắn đang chờ"; trang cá nhân, kể cả chế độ chuyên nghiệp, không trả lời tự động được; "nhẹ" chỉ là lệnh khi gõ riêng; giá công khai, khuyến mãi ≤50%.
Tích hợp 6/10 (ngân sách file phương pháp ≤56.320 byte): mục 1 bỏ keyword_variants (dạng không dấu nằm ở start-block, dòng Từ khoá, luôn có trong ngữ cảnh); mục 9 trỏ tick.cap về §CM-GUARDRAILS và bản hạ bậc (verdict.ready_downgraded) về §CM-EDGE "tại sao?"; mục 6 bỏ "({date}: §CM-LOCALE 6)"; "nhóm khách đầu" → "suất nhóm đầu" (một chữ như §CM-WEEK 6, 9).
G1 6/10 (theo EN): mục 5 K11 "Không tự bỏ; lời xả từ chối xin comment thì nhẹ từ đầu." (§CM-FORMATS 7 trỏ về đây cho ngày 0). cta.by_hand K14 bỏ "bạn hoặc trợ lý gửi".
Cắt bù byte G1 (không bỏ luật): mục 1 cta.default → "lời mời ở ngày 0, bước 6" (start-block bước 6 in đúng chuỗi đó; §CM-WEEK 6 vẫn trỏ §CM-CTA-KIT 1).
VG1/G2 6/10: mục 5 VK-2 coach chê xin comment bằng lời (cả lúc xả) → quiet ngay, không cãi, bài chưa đăng in lại lời mời; "Nghe như spam?" chỉ khi là câu hỏi (cta.not_pushy, VK-1). Mục 2, 4 VK-19: quà đến cùng caption đầu hứa nó, chưa viết thì không hứa; ngày 0 trỏ start-block bước 6–7 thay vì kể lại (byte).

<!-- @section convert.kit-keyword src=4dfa3663ae -->
1 Mặc định: lời mời ở ngày 0, bước 6. Từ khoá viết HOA. Mỗi mùa một từ khoá, một quà.
2 Quà: tự viết từ cách làm 3 bước của họ: checklist, kế hoạch hay kịch bản 1 trang vừa một tin inbox, tên gọi thẳng, viết xong, trong khung chép. Hạn: cùng caption đầu hứa nó, hoặc khi hỏi "gửi gì?"; chưa viết thì không hứa. Đã hứa mà chưa có: viết ngay.
3 Trả lời dưới bài: ≥5 câu ngắn xoay vòng, xưng theo người comment, đều chỉ vào inbox.
4 Bài có từ khoá: quà và tin trả lời inbox 1 xong trước khi đăng (ngày 0: bước 6–7); "{{t:tick.keyword}}" chỉ hiện khi "{{t:cmd.why}}".
5 "{{t:cmd.quiet}}" (gõ riêng) hay coach chê xin comment (cả lúc xả) → cta_style quiet luôn, không cãi: bài sau mời "{{t:cta.quiet}}", bài chưa đăng in lại lời mời; cụm từ khoá vẫn trong lời. Hỏi "Nghe như spam?": "{{t:cta.not_pushy}}" Không tự bỏ lời xin comment.

<!-- @section convert.kit-choices src=921a084b77 -->
6 Họ tự chọn ("chấm", "ib", "đủ 20 comment", emoji): nguyên văn, không chặn, không làm mềm; dưới bài chỉ một dòng: "{{t:cta.platform_note}}" Emoji: kèm "{{t:cta.emoji_trigger}}"
7 Trả lời inbox tự động chỉ có ở Trang Facebook, Instagram chuyên nghiệp; trang cá nhân, LinkedIn: "{{t:cta.by_hand}}", gộp vào dòng có ngày. Instagram: mỗi comment một tin riêng trong 7 ngày, nên tin inbox 1 kết bằng câu hỏi. Không bắt lập Trang, cài công cụ; họ hỏi mới nêu tên.
8 Lời mời theo chặng: §CM-WEEK 6; comment từ khoá tính là một lần cho.

<!-- @section convert.kit-sell kind=script src=c5dd9da7f1 -->
9 Bài mời mua: nhận gì (hình thức, bao lâu, ngày bắt đầu) · giá công khai, trả mấy lần · dành cho ai · "Không hợp với ai đang…" · cam kết cách làm, có điều kiện, chưa có thì "{{t:verdict.needs}}" · suất, hạn chỉ khi thật, nói thẳng (tick: §CM-GUARDRAILS) · một việc. Chưa có bằng chứng: mời suất nhóm đầu, hạ bậc (§CM-EDGE).
Bài dạy, chuyện khách: §CM-POSTS; bằng chứng, gấp gáp, giảm giá: §CM-GUARDRAILS.
