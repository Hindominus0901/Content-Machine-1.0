VN twin of core/en/ship-check.md (docs/research/wf12-qa-spec.md §2.3; wf15 §3 PRINT line; wf14 §5 VOICE step).
One source, included with {{>ship.…}}:
- ship.kit   → the instruction block and Phone Starter. Fully Vietnamese: the Phone Starter is pasted into the chat, so no
               English label ("SHIP CHECK" is deny-listed coach jargon) and no § sign.
- ship.card  → SKILL.md and the L3 skill. Hub and Bank identifiers stay as the schemas name them (Bank, P, Ledger,
               Substantiated, Consent, scripts/ship_lint.py); [CẦN …] is the VN open-fact tag (tools/cmcore/checks.py).
- ship.task  → standalone task text (VA tier); recent_hook_stems is a hub field name.
Budgets (platform/targets.toml): card ≤1,000 VN, task ≤1,000 VN, NFC characters.
Units: VN counts tiếng (syllables). EN "one idea ≤15 words" → ≤20 tiếng (editions/vn.toml quote/hook ratios).
The cards hold no string tags on purpose: lint renders them through an Edition built without a root, so the lint fixture
repos read these real files against their own tiny strings tables (tools/lint.py card_markers, load_editions).

<!-- @section ship.kit src=5be8ead996 -->
KIỂM TRA TRƯỚC KHI GIAO · âm thầm · mọi bài · không chắc → cắt hoặc hạ bậc · không khen
0 TRỌNG TÂM: một ý lớn trên bản đồ · ý chính ≤20 tiếng · một niềm tin ("bạn nghĩ X → thật ra Y") · không phải chủ đề để dành
1 VIẾT chỉ từ điều coach kể. Thiếu thông tin → hạ bậc (kể quy trình, nhóm đầu, bỏ số suất) hoặc hỏi
2 SỰ THẬT: số, tên, câu trích là của coach, trích nguyên văn; kết quả của khách chỉ khi khách đồng ý; gấp chỉ khi gấp thật
3 KHÁC BIỆT, mỗi mục 0–2, cần ≥8, không mục 0: từ khoá 1 lần + chi tiết cụ thể · một ý, một niềm tin · bằng chứng hiện ra · chi tiết chỉ coach có · quan điểm có người phản đối. Câu mở đầu không rào đón
4 GIỌNG + NGƯỜI MUA: giọng, nhịp, câu hay nói, cách gọi khách của coach, không chữ cấm; người mua lướt điện thoại dừng lại, tin trong 5 giây. Sửa một lần
IN: bài xong → chỉ nội dung. Thiếu thông tin → một dòng "Cần bạn · <câu hỏi>". Lý do, phần kiểm: chỉ khi hỏi "tại sao?"

<!-- @section ship.card src=79de1a30da -->
KIỂM TRA TRƯỚC KHI GIAO · âm thầm · một lần mỗi đợt · không chắc → cắt hoặc hạ bậc · không khen
0 TRƯỚC: có dòng slot + chất liệu Bank? Không → HẠ BẬC (kể quy trình, nhóm đầu, bỏ số suất); chỉ hỏi khi bài dựa vào thông tin thiếu
1 VIẾT từ ID trong Bank; từ chối điểm dừng cứng
2 SOÁT (Claude: scripts/ship_lint.py, chạy cuối): số, tên, câu trích có trong dòng được dẫn, trích nguyên văn · kết quả = dòng P có Substantiated + Consent · gấp theo Ledger · từ khoá ×1 · gốc câu mở đầu mới · mở đầu không rào đón · 0 [CẦN …]
3 KIỂM khi viết xong, đọc lại dòng đã dẫn. Cổng: quan điểm, sự thật, giọng. Khác biệt 0–2: K từ khoá + chi tiết · V một ý, một niềm tin · A bằng chứng hiện ra · Au chi tiết chỉ coach có · C quan điểm. Kiểm định dạng. Không chắc = trượt: lướt 5 giây, nghe đúng Card, người mua tin
4 SỬA lỗi đã gọi tên, một lần. Sẵn sàng = qua cổng, khác biệt ≥8, không mục 0, đúng định dạng
IN dưới mỗi bài: Sẵn sàng <động từ> · Mình sẽ đăng: <dữ kiện Bank> | Cần bạn: <1 câu hỏi/trả lời>

<!-- @section ship.task src=a40952396a -->
KIỂM TRA (tác vụ) · âm thầm · không chắc → cắt hoặc hạ bậc · không đoán, không khen
1 Chỉ viết từ ID trong Brief; từ chối khan hiếm giả, bằng chứng bịa, lời cam kết, công kích người khác
2 Mọi con số, tên, câu trích nằm trong một dòng Brief được dẫn; trích đúng nguyên văn; kết quả chỉ từ dòng P có Substantiated + Consent, không thì kể quy trình; gấp chỉ theo Ledger
3 Từ khoá đúng 1 lần · gốc câu mở đầu không có trong recent_hook_stems · câu mở đầu không rào đón · không mục khác biệt nào 0: từ khoá + chi tiết, một ý, bằng chứng hiện ra, chi tiết chỉ coach có, một quan điểm
4 Thiếu thông tin → [CẦN BẠN: một câu hỏi] và bài là Bản nháp. Không bao giờ hỏi trong tác vụ; báo cáo lượt chạy mang 1 câu hỏi
IN dưới mỗi bài: Sẵn sàng <động từ> · Mình sẽ đăng: <dữ kiện Brief> | Bản nháp · cần: <câu hỏi>
