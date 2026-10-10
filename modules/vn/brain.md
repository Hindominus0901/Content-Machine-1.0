Bản VN của modules/en/brain.md, cho §CM-CARD (file phương pháp): cách in Brand Card, tên trường, phiên bản, cách lưu, sửa lỗi ở đoạn chat mới.
Nguồn: wf15-simple-surface-spec §0 S3-S4, §1.7 (phần trên ngắn, một dòng lưu, không điểm dừng); wf14-voice-language-spec §1-§3
(NÓI GÌ / NÓI THẾ NÀO, các trường Hồ sơ giọng); schemas/brand-card.toml (trường, giới hạn, trim_order, liked; connectors, address_1to1 từ 06/10/2026);
wf11-ux-spec §1.4, §3.2, §6; wf13-inspiration-spec §4; wf2-vietnam-market §5 (xưng hô, giọng vùng, định dạng giá), §10 mục 13 (tài khoản dùng chung).
Câu chữ soát theo docs/research/vn-language-guide.md §2, §4.5 (06/10/2026). Nghiệm thu: evals/cases/brain.vn.toml.
Tên trường giống hệt bản EN và schema; phần trên không bao giờ hiện tên trường. Cách điền từng trường giọng: §CM-VOICE 1-3, 9.
Thêm so với EN: pronouns (cặp máy–coach, quy tắc xưng hô cho mọi trả lời), dialect, connectors, address_1to1, owned_channel=zalo,
định dạng giá. Zalo "Cloud của tôi" nằm ở core/vn/start-block.md (dòng Lưu, phone.save), không lặp ở mục 7. (Bản EN của dòng giọng chưa có connectors, address_1to1: src giữ nguyên vì thân EN không đổi.)
Tích hợp 6/10 (ngân sách file phương pháp ≤56.320 byte): mục 1 trỏ dòng lưu (card.save_line) về start-block bước 8.
G1 6/10 (theo EN): mục 3 K4 "plan_start = hôm sau ngày 0, tuần n = mỗi 7 ngày từ đó"; K8 tier=lean|standard (bỏ va như EN), delivery thêm beat-cards (= "thẻ ý"), timezone=ask|{zone} (VN: giờ Việt Nam mặc định, §CM-LOCALE 6). Mục 7: dòng LUÔN LUÔN đã bỏ khỏi start-block (K21) → "dòng "Luôn…"" (dòng hợp đồng đầu, cuối); src brain.kit-box giữ nguyên vì thân EN không đổi.
Cắt bù byte G1 (không bỏ luật): mục 1 bỏ "; không chặn gì" (start-block bước 8: "Chưa lưu vẫn làm tiếp"); mục 3 card.machine.heading → "dòng cho máy như BRAND CARD" (start-block BRAND CARD in đúng chuỗi đó).
G2/VG1 6/10: mục 3 list_size=ask|{n} (schema đổi sang text; thay VK-20), VK-13 "proof: … (không thì not_now)". Trả bằng month.save_card bỏ ", chạm 2 cái là xong" (cắt VK-16 đã nêu). Chưa theo EN: K28 (7/7 lượt VG1 đã in dự phòng Zalo: start-block "Dự phòng"); K29 thứ tự cắt (cần ~38 byte; file phương pháp đang 56.318/56.320).

<!-- @section brain.kit-print src=1d3242aee9 -->
1 KHI NÀO: ngày 0, "tiếp" sau QUAY HÔM NAY (§CM-SETUP 9); in lại: mục 4.
2 PHẦN TRÊN, ≤500 ký tự, 3 dòng: "{{t:card.title}}" · "{{t:card.visible.what}} {thông điệp} · {trụ cột} · "{từ khoá}"" · "{{t:card.visible.how}} {giọng} · {nhịp} · "{câu}", "{câu}" · {{t:card.visible.to_them}} "{xưng hô}"", có "{{t:cmd.not_me}}" thì thêm · {{t:card.visible.never}} "{chữ}". Quá 500: rút thông điệp, giữ dòng giọng.
3 Rồi dòng cho máy như BRAND CARD + một khung code, mỗi dòng `tên: giá trị`, " | " giữa mục, [n] tối đa, ? = không có thì bỏ, không để trống:
version date=YYYY-MM-DD edition=vn pack_version=1.0.0 progress
who their_words[2] promise method old_way pillars[5] mix=a/t/c% offer bio_line keyword_alternates[2] idea_shifts[3] key_belief why_this_one side_door? trial_ends offer_status=live|founding|none proof_ready=yes|no not_now[7]
tone rhythm phrases[5] openers_closers?[3] audience_address address_1to1? connectors?[5] pronouns dialect=vùng·tiểu từ ~n%·3 tiểu từ code_mix humour=none|dry|playful|self-roast written_vs_spoken? never_say?[10] do_say?[10]
trait(một nét + người nó đẩy ra) enemy(một cách làm) principles[3] passages[5] client_words[8] stories[5] proof?[5]
plan_start season=1 talk_day=Mon..Sun week tier=lean|standard platform=chữ thường owned_channel=zalo|email|both|none list_size=ask|{n} cta_style=keyword|quiet delivery=beat-cards|interview|bullets|word-for-word timezone=ask|{zone} mode=always-on hub=none automations=none|reminders recent_hooks?[10] liked?[8]
plan_start = hôm sau ngày 0, tuần n = mỗi 7 ngày từ đó; trial_ends = plan_start + 25 ngày. offer kèm giá (§CM-LOCALE 5). proof: đếm được, đúng việc khách cho; chưa rõ: hỏi 1 lần trước khi đăng, không cho: not_now. passages ≤60 tiếng, nguyên văn. Nhóm giọng: §CM-VOICE; pronouns: cặp chọn ở trả lời 1. liked: mới trước, ≤90 ký tự. Quá 6.600: cắt liked trước, nhóm giọng sau cùng.

<!-- @section brain.kit-keep src=67b215f2a1 -->
4 In lại khi lên kế hoạch tháng, thứ Sáu có thêm bài họ thích hay kết quả, đổi giá, sản phẩm; + "{{t:month.save_card}}" Câu, cách mở mới từ buổi nói chuyện vào bản in sau.

<!-- @section brain.kit-fix src=dd0e7e84d5 -->
5 Claude, cách lưu: "{{t:save.claude_plain}}"
6 ĐOẠN CHAT MỚI: v cao nhất thắng; bản cũ, bản thừa: "{{t:card.remove_old}}" Không hỏi. Card ở chat cũ: dùng luôn. Không có card, coach không mới: "{{t:card.fix_missing}}" Không chạy lại ngày 0. Dán nhầm hướng dẫn vào chat: vẫn làm + "{{t:card.fix_pasted_block}}" "Bắt đầu" kèm card, khung: in lại, làm tiếp.

<!-- @section brain.kit-box src=cb6dcdffbe -->
7 Khung điện thoại "MY CONTENT MACHINE" = dòng "Luôn…", MỖI LẦN TRẢ LỜI, LỜI HỨA + card.
