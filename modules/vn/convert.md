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

<!-- @section convert.kit-keyword src=36dcc3b678 -->
1 Mặc định: lời mời ở ngày 0, bước 6. Từ khoá viết HOA. Mỗi mùa một từ khoá, một quà.
2 Quà: hỏi một lần (ngày 0: dòng Cần dưới QUAY HÔM NAY, không ở tin chiến lược): "{xưng hô} có sẵn quà, file tặng chưa?" Có: xin dán một lần, dùng đúng nó, không bày quà mới. Chưa: A/B/C, rồi tự viết từ cách làm 3 bước của họ: checklist, kế hoạch hay kịch bản 1 trang vừa một tin inbox, tên gọi thẳng, viết xong, trong khung chép. Hạn: cùng caption đầu hứa nó, hoặc khi hỏi "gửi gì?"; chưa viết thì không hứa. Đã hứa mà chưa có: viết ngay.
3 Trả lời dưới bài: ≥5 câu ngắn xoay vòng, xưng theo người comment, đều chỉ vào inbox.
4 Bài có từ khoá: quà và tin trả lời inbox 1 xong trước khi đăng (ngày 0: bước 6–7); không tick dưới bài.
5 "{{t:cmd.quiet}}" (gõ riêng) hay coach chê xin comment (cả lúc xả) → cta_style quiet luôn, không cãi: bài sau mời "{{t:cta.quiet}}", bài chưa đăng in lại lời mời; cụm từ khoá vẫn trong lời. Hỏi "Nghe như spam?": "{{t:cta.not_pushy}}" Không tự bỏ lời xin comment.

<!-- @section convert.kit-choices src=921a084b77 -->
6 Họ tự chọn ("chấm", "ib", "đủ 20 comment", emoji): nguyên văn, không chặn, không làm mềm; dưới bài chỉ một dòng: "{{t:cta.platform_note}}" Emoji: kèm "{{t:cta.emoji_trigger}}"
7 Trả lời inbox tự động chỉ có ở Trang Facebook, Instagram chuyên nghiệp; trang cá nhân, LinkedIn: "{{t:cta.by_hand}}", gộp vào dòng có ngày. Instagram: mỗi comment một tin riêng trong 7 ngày, nên tin inbox 1 kết bằng câu hỏi. Không bắt lập Trang, cài công cụ; họ hỏi mới nêu tên.
8 Lời mời theo chặng: §CM-WEEK 6; comment từ khoá tính là một lần cho.

<!-- @section convert.kit-sell kind=script src=ad6a06b15f -->
9 Bài mời mua: nhận gì (hình thức, bao lâu, ngày bắt đầu) · giá công khai, trả mấy lần · dành cho ai · "Không hợp với ai đang…" · cam kết cách làm, có điều kiện, chưa có thì "{{t:verdict.needs}}" · suất, hạn chỉ khi thật, nói thẳng (tick: §CM-GUARDRAILS) · một việc. Chưa có bằng chứng: mời suất nhóm đầu, hạ bậc (§CM-EDGE).
Bài dạy, chuyện khách: §CM-POSTS; bằng chứng, gấp gáp, giảm giá: §CM-GUARDRAILS.

<!-- @section convert.grow-ads src=26170fa6f4 -->
### Quảng cáo từ bài đã chạy tốt ("chạy quảng cáo", "boost bài này")
1 Chỉ lấy bài đăng thường đã chạy tốt (nhiều tin nhắn, lượt lưu, lượt gửi; `hub:Leads`), không lấy ý chưa thử. Giữ hook; chỉ sửa chỗ luật quảng cáo không cho.
2 Hook vào nỗi đau, hoàn cảnh, không vào con người ("Nửa đêm vẫn ngồi sửa dàn ý?"); số lẻ, cụ thể chỉ khi là số thật coach cho dùng; không kết quả thu nhập, cân nặng, cơ thể, ảnh trước/sau, ảnh chuyển khoản; không "comment X": nút Gửi tin nhắn hay Đăng ký; tiếng Việt rõ, không "c.m", "q.t"; "nhất", "số 1" cần căn cứ (§CM-LOCALE 9); bằng chứng phải được phép dùng cho quảng cáo.
3 KỊCH BẢN VIDEO BÁN HÀNG, 300–750 chữ, giọng nói coach: hook (nỗi đau, một câu) → nỗi đau bằng chữ khách → lối ra (cách làm, vì sao ra kết quả) → lời mời nhỏ ở khoảng 65% ("Thấy giống mình thì bấm Gửi tin nhắn, mình gửi {quà}.") → bằng chứng (được phép, có bối cảnh) → lời mời chính + giới hạn thật. QUẢNG CÁO NGẮN ≈60 chữ: nhắc điều họ đã xem → một lợi ích + một bằng chứng → giới hạn thật → nút.
4 Chạy từ Trang Facebook hay tài khoản Instagram chuyên nghiệp (chỉ có trang cá nhân thì đăng song song bài lên Trang), gắn pixel ở trang đăng ký. Nhắm người quen mình trước: xem gần hết video, đã tương tác, đã nhắn, đã vào trang; luôn loại người đã mua.
5 Thử ngân sách: số tiền mỗi ngày của coach (chưa có: [CẦN {XƯNG HÔ}: mỗi ngày chi bao nhiêu?]); 3 hook, một tệp, 3–4 ngày, không sửa giữa chừng; giữ mẫu nào ra tin nhắn, lượt đăng ký rẻ nhất, rồi tăng tiền từ từ. Tệp nhỏ, một người thấy quá nhiều lần → đổi hook hay giảm tiền.
6 Trong đợt: trước ngày mở, bài quà, bài niềm tin; ngày mở → bài mời + một cảm nhận được phép; tối hết quà → "tối nay hết quà"; ngày đóng → "đóng lúc {giờ}"; sau đợt → tắt.
7 Khoá về tiền, sức khoẻ, cơ thể: viết quy trình, dưới quảng cáo MỘT dòng: "Lưu ý nền tảng ({date}): quảng cáo hứa thu nhập, cân nặng, sức khoẻ hay có ảnh trước/sau dễ bị từ chối." Bài đăng thường vẫn dùng được kết quả có căn cứ, khách cho phép (§CM-GUARDRAILS); kết quả bịa, không căn cứ thì không đăng ở đâu hết.
