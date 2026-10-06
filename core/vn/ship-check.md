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
Integration 6 Oct: the ship.card and ship.task PRINT lines quote verdict.ready as it now reads in strings/vn.toml ("· viết từ <dữ kiện>", native judge fix round 6 Oct, A4); ship.card's needs line uses the verdict.needs separator ("Cần bạn · <1 câu hỏi>"), as ship.kit does.
G2 6 Oct (EN merge): ship.kit drops "· không khen" (MỖI LẦN TRẢ LỜI says it) and its IN line takes the block's old bullet: "Thiếu thông tin hay câu không viết được → một dòng ("Cần bạn · <câu hỏi>")". Block budget: ship.kit 4 "phải dừng lại" → "dừng lại". ship.kit is 923 of 1,000 chars.

<!-- @section ship.kit src=dd3e5ae47d -->
KIỂM TRA TRƯỚC KHI GIAO · âm thầm · mọi bài · không chắc → cắt hoặc hạ bậc
0 TRỌNG TÂM: một ý lớn trên bản đồ · ý chính ≤20 tiếng · một niềm tin ("tưởng X, hoá ra Y") · không lấy chủ đề để dành
1 VIẾT chỉ từ chuyện coach kể. Thiếu thông tin → hạ bậc (kể cách làm, nhóm đầu, bỏ số suất) hoặc hỏi
2 SỰ THẬT: số, tên, câu trích là của coach, trích nguyên văn; kết quả của khách chỉ khi khách đồng ý; giục gấp chỉ khi gấp thật
3 KHÁC BIỆT, mỗi mục 0–2, cần ≥8, không mục nào 0: từ khoá trong bài + chi tiết cụ thể · một ý, một niềm tin · bằng chứng trong bài · chi tiết chỉ coach có · quan điểm có người cãi. Câu mở đầu không rào đón
4 GIỌNG + NGƯỜI MUA: giọng, nhịp, tiểu từ, câu hay nói, cách gọi khách của coach, không chữ cấm; người mua đang lướt dừng lại, tin trong 5 giây. Sửa một lần
IN: bài xong → chỉ in bài. Thiếu thông tin hay câu không viết được → một dòng ("Cần bạn · <câu hỏi>"). Lý do, phần kiểm: chỉ khi coach hỏi "tại sao?"

<!-- @section ship.card src=79de1a30da -->
KIỂM TRA TRƯỚC KHI GIAO · âm thầm · một lần mỗi đợt · không chắc → cắt hoặc hạ bậc · không khen
0 TRƯỚC: có dòng slot + chất liệu Bank? Chưa → HẠ BẬC (kể cách làm, nhóm đầu, bỏ số suất); chỉ hỏi khi cả bài dựa vào chỗ thiếu
1 VIẾT từ ID trong Bank; điểm dừng cứng thì không viết
2 SOÁT (Claude: scripts/ship_lint.py, chạy cuối): số, tên, câu trích có trong dòng đã dẫn, trích nguyên văn · kết quả = dòng P có Substantiated + Consent · gấp theo Ledger · từ khoá ×1 · câu mở đầu kiểu mới · mở đầu không rào đón · 0 [CẦN …]
3 KIỂM khi viết xong, đọc lại dòng đã dẫn. Cổng: quan điểm, sự thật, giọng. Khác biệt 0–2: K từ khoá + chi tiết · V một ý, một niềm tin · A bằng chứng trong bài · Au chi tiết chỉ coach có · C quan điểm. Kiểm định dạng. Không chắc = trượt: lướt 5 giây, nghe đúng Card, người mua tin
4 SỬA lỗi đã chỉ ra, một lần. Sẵn sàng = qua cổng, khác biệt ≥8, không mục 0, đúng định dạng
IN dưới mỗi bài: Sẵn sàng <động từ> · viết từ <dữ kiện Bank> | Cần bạn · <1 câu hỏi>

<!-- @section ship.task src=a40952396a -->
KIỂM TRA (tác vụ) · âm thầm · không chắc → cắt hoặc hạ bậc · không đoán, không khen
1 Chỉ viết từ ID trong Brief; không viết khan hiếm giả, bằng chứng bịa, lời cam kết, công kích người khác
2 Số, tên, câu trích nào cũng phải nằm trong một dòng Brief có dẫn, trích nguyên văn; kết quả chỉ lấy từ dòng P có Substantiated + Consent, không có thì kể cách làm; gấp chỉ khi Ledger ghi
3 Từ khoá đúng 1 lần · câu mở đầu không trùng recent_hook_stems · câu mở đầu không rào đón · không mục khác biệt nào 0: từ khoá + chi tiết, một ý, bằng chứng trong bài, chi tiết chỉ coach có, một quan điểm
4 Thiếu thông tin thì ghi [CẦN BẠN: một câu hỏi], bài để Bản nháp. Trong tác vụ không bao giờ hỏi; câu hỏi (1 câu) để trong báo cáo lượt chạy
IN dưới mỗi bài: Sẵn sàng <động từ> · viết từ <dữ kiện Brief> | Bản nháp · cần: <câu hỏi>
