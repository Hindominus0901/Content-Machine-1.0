Bản VN của modules/en/edge-rubric.md, cho §CM-EDGE (edge-rubric.kit-*): kiểm tra trước khi giao chạy thế nào và mỗi trạng thái bài in ra gì (thẻ kiểm tra nằm ở core/vn/ship-check.md, không lặp lại ở đây).
Nguồn: wf15-simple-surface-spec §2-§3 (Sẵn sàng không in gì; lý do, phần kiểm, hồ sơ chỉ khi hỏi "tại sao?"); wf12-qa-spec §0-§2.6; wf6-character-design §B5-§B6 (cổng, mượn, lật lại; câu đầu khoảng 18 tiếng; VN strip list V1-V9), ghi chú VN 1-13;
PLAN reconciliations 2-3, 8; DECISIONS (6/10: ngoài đơn giản, trong chặt). Nghiệm thu: evals/cases/edge-rubric.vn.toml, router.vn.
K V A Au C, tên cổng, "edge" là nhãn nội bộ: không bao giờ in ra, kể cả khi hỏi "tại sao?" (v13.4: chỉ in dòng VÌ SAO và bài dựng thế nào). Lời hứa → §CM-GUARDRAILS. Giọng → §CM-VOICE.
Đơn vị VN là tiếng (âm tiết): EN 15 chữ ≈ 20-24 tiếng, 25 chữ ≈ 38-40 tiếng, 5 chữ ≈ 8 tiếng.
Trỏ sang chỗ khác (6/10): dòng in đổi theo cặp xưng hô = start-block XƯNG HÔ ("Cần chị"); khung MY CONTENT MACHINE = §CM-CARD 7.
Thêm so với EN: dòng in theo cặp xưng hô đã chọn (nay nằm ở start-block); rào đón VN trỏ về §CM-HUMANIZE 3; khung MY CONTENT MACHINE trong Zalo "Cloud của tôi" khi chat chưa có card.
Tích hợp 6/10 (ngân sách file phương pháp ≤56.320 byte): dòng Dừng cứng (verdict.hardstop) chỉ in ở §CM-GUARDRAILS; dòng Cần bạn bỏ "(thông tin, lựa chọn chỉ họ có)" vì SẴN SÀNG đã nói.
Cắt bù byte G1 6/10 (không bỏ luật): tiêu đề IN DƯỚI BÀI bỏ "chỉ khi cần coach; còn lại để dành cho "tại sao?"" (start-block MỖI LẦN TRẢ LỜI và dòng IN của thẻ kiểm tra nói y vậy; các gạch đầu dòng dưới vẫn liệt kê); "bản nháp thì sửa thầm" bỏ (SẴN SÀNG: "Chưa đạt → sửa thầm một lần").

<!-- @section edge-rubric.kit-run src=333d85cb5e -->
LOẠI: Ý tưởng (phương án, dòng kế hoạch): ý yếu bỏ thầm. Bài ngắn (dưới {{micro_threshold}} tiếng): không chấm điểm, mở bằng quà được; chỉ kiểm sự thật, lời hứa, quan điểm, độ dài, quà thật. Có lời hứa (kết quả, tiền, giá, lời khách, gấp gáp): + §CM-GUARDRAILS.
ĐIỂM 0-2: K từ khoá, chữ khách ở câu đầu, câu chốt · V ý chính trong 2 dòng đầu, làm được hôm nay · A bằng chứng cạnh mỗi lời hứa · Au chi tiết chỉ họ có · C quan điểm nhắm cách cũ, câu "không hợp với ai"; "cách nào cũng được" = 1. Dạng quan điểm (cũ – mới, sự thật ít ai nói, không hợp với ai) cần C 2. Chưa có card: Au, C ≤1; xin dán card một lần (§CM-CARD 7).
CỔNG. Quan điểm: nóng với cách làm, không với người ("coach lùa gà" → "khoá học bỏ bước X"). Sự thật: số lệch hồ sơ → số thật. Giọng: câu đầu ≤{{hook_max}} {{hook_unit}}; câu đầu, câu hứa không rào đón (§CM-HUMANIZE 3); câu ~20 tiếng, tối đa 38, có câu ≤8; hỏi tu từ thì đáp liền (hook hỏi: câu cuối đáp). Sửa, không từ chối.
MƯỢN: tiền, quà, lý lịch làm cả câu đầu, tới dòng 3 chưa có "vì sao" → C 0, Bản nháp. Lật lại: mở bằng lựa chọn hay chuyện; món kia làm bằng chứng hay lời mời.
SẴN SÀNG: qua cổng, ≥8, không mục 0, không [CẦN …]; không "Sẵn sàng sau khi…". Chưa đạt → sửa thầm một lần, chỉ lỗi đã gọi tên (≤5; quan điểm; mượn → ý khác). Vẫn chưa → dòng Cần (thông tin, lựa chọn sửa được), không thì hạ bậc. "{{t:cmd.fix}} N2", "{{t:cmd.try_again}}": chỉ N2, in lại riêng.

<!-- @section edge-rubric.kit-verdict src=b418e8a557 -->
IN DƯỚI BÀI (≤1 dòng):
- Sẵn sàng (cả bản hạ bậc), Bản nháp: không in gì.
- Cần: {{t:verdict.needs}} Mỗi lần một câu, bài gần nhất trước; bài khác chạy bản hạ bậc.
- Dừng cứng: dòng ở §CM-GUARDRAILS.
- Override ("{{t:cmd.post_anyway}}"): {{t:verdict.override}} Một lần, không nhắc lại; dừng cứng vẫn giữ.
- Chép, dịch, so sánh, ngưỡng comment, gửi tay: một lưu ý có ngày; Override chỉ ghi.
"{{t:cmd.why}}" → bài gần nhất, một câu: dòng VÌ SAO ({{t:why.prefix}}: niềm tin cũ → mới, bằng chứng của họ) + cách viết bằng lời thường ("kể chuyện một khách rồi rút bài học"), không tên khung. Không in điểm, chữ cái, cổng, tick, hồ sơ kiểm. Bằng chứng: câu, cảnh, khách của họ; không tính từ.
BÀI HỌ VIẾT nhờ xem: một dòng Sẵn sàng hoặc "{{t:verdict.draft_fixable}}". Hỏi điểm: trạng thái bằng lời + "{{t:qa.why_hint}}", không con số.
