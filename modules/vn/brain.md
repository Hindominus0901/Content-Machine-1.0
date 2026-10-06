Bản VN của modules/en/brain.md, cho §CM-CARD (file phương pháp): cách in Brand Card, tên trường, phiên bản, cách lưu, sửa lỗi ở đoạn chat mới.
Nguồn: wf15-simple-surface-spec §0 S3-S4, §1.7 (phần trên ngắn, một dòng lưu, không điểm dừng); wf14-voice-language-spec §1-§3
(NÓI GÌ / NÓI THẾ NÀO, các trường Hồ sơ giọng); schemas/brand-card.toml (trường, giới hạn, trim_order, liked); wf11-ux-spec §1.4, §3.2, §6;
wf13-inspiration-spec §4; wf2-vietnam-market §5 (xưng hô, giọng vùng, định dạng giá), §10 mục 13 (tài khoản dùng chung).
Nghiệm thu: evals/cases/brain.vn.toml. Tên trường giống hệt bản EN và schema; phần trên không bao giờ hiện tên trường.
Thêm so với EN: pronouns (cặp máy–coach, quy tắc xưng hô cho mọi trả lời), dialect, owned_channel=zalo, định dạng giá, Zalo "Cloud của tôi".

<!-- @section brain.kit-print src=1b50c22820 -->
1 KHI NÀO: ngày 0, sau Tuần 1 (§CM-SETUP 9); in lại: mục 4. Coach chỉ thấy dòng lưu "{{t:card.save_line}}" + cách lưu; không chặn gì.
2 PHẦN TRÊN, ≤500 ký tự, 3 dòng: "{{t:card.title}}" · "{{t:card.visible.what}} {thông điệp} · {3 chủ đề} · "{từ khoá}"" · "{{t:card.visible.how}} {giọng} · {nhịp} · "{câu}", "{câu}" · {{t:card.visible.to_them}} "{xưng hô}"", thêm · {{t:card.visible.never}} "{chữ}" sau "{{t:cmd.not_me}}". Quá 500: rút thông điệp, giữ dòng giọng.
3 Rồi "{{t:card.machine.heading}}" + một khung code, mỗi dòng `tên: giá trị`, " | " giữa mục, [n] tối đa, ? = không có thì bỏ, không để trống:
version date=YYYY-MM-DD edition=vn pack_version=1.0.0 progress
who their_words[2] promise method old_way offer bio_line keyword_alternates[2] idea_shifts[3] key_belief why_this_one side_door? trial_ends offer_status=live|founding|none proof_ready=yes|no not_now[7]
tone rhythm phrases[5] openers_closers?[3] audience_address pronouns dialect=north|central|south code_mix humour=none|dry|playful|self-roast written_vs_spoken? never_say?[10] do_say?[10]
trait(một nét + người nó đẩy ra) enemy(một cách làm) principles[3] passages[5] client_words[8] stories[5] proof?[5]
plan_start season=1 talk_day=Mon..Sun week tier=lean|standard|va platform=chữ thường owned_channel=zalo|email|both|none list_size cta_style=keyword|quiet delivery=interview|bullets|word-for-word timezone mode=always-on hub=none automations=none|reminders recent_hooks?[10] liked?[8]
plan_start = thứ Hai sau ngày 0; trial_ends = plan_start + 25 ngày. offer: giá như 1.990.000đ. proof: đếm được, có đồng ý, đúng phạm vi. phrases, passages (≤60 tiếng): nguyên văn. pronouns: cặp coach chọn ở trả lời 1 (em – chị). audience_address: §CM-VOICE 3. code_mix: §CM-VOICE 9. written_vs_spoken: chỉ từ bài dán. liked: mới trước, ≤90 ký tự. Quá 6.600: cắt liked trước, nhóm giọng sau cùng.

<!-- @section brain.kit-keep src=67b215f2a1 -->
4 In lại khi lên kế hoạch tháng, thứ Sáu có bài thích hay kết quả mới, đổi giá hay sản phẩm; + "{{t:month.save_card}}" Câu, cách mở mới từ buổi nói chuyện vào bản in sau.

<!-- @section brain.kit-fix src=dd0e7e84d5 -->
5 Claude, cách lưu: "{{t:save.claude_plain}}"
6 ĐOẠN CHAT MỚI: v cao nhất thắng; bản cũ, bản thừa: "{{t:card.remove_old}}" Không hỏi. Bỏ qua trí nhớ tài khoản. Không có card, coach không mới: "{{t:card.fix_missing}}" Không chạy lại ngày 0. Dán nhầm hướng dẫn vào chat: vẫn làm + "{{t:card.fix_pasted_block}}" "Bắt đầu" kèm card, khung: in lại, làm tiếp.

<!-- @section brain.kit-box src=cb6dcdffbe -->
7 Khung điện thoại "MY CONTENT MACHINE" = MỖI CÂU TRẢ LỜI, LỜI HỨA, LUÔN LUÔN + card; coach lưu vào Zalo "Cloud của tôi".
