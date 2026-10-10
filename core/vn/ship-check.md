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
G2 6 Oct (EN merge): ship.kit drops "· không khen" (MỖI LẦN TRẢ LỜI says it) and its IN line takes the block's old bullet: "Thiếu thông tin, điều cấm → một dòng ("Cần bạn · <câu hỏi>")". Block budget: ship.kit 4 "phải dừng lại" → "dừng lại". ship.kit is 923 of 1,000 chars.
Retest FT1 7/10 (qa/runs/retest-ft1/review.md §7 items 1, 7): ship.kit 3 thêm "chữ trên màn hình ≠ câu đầu"; 4 "tiểu từ cuối câu dày như họ (đếm)"; 2 bỏ "kết quả của khách chỉ khi họ đồng ý; giục gấp chỉ khi gấp thật" (dòng LỜI HỨA ngay sau card nói đúng hai luật đó). ship.kit 944 of 1,000 chars.
Retest FT2 7/10 (qa/runs/retest-ft2/review.md §8 items 1, 2, 5): ship.kit 1 "cả khách làm gì, nghĩ gì"; 3 "Hook, dòng 1 caption: không rào đón, phán suông, châm ngôn; chữ trên màn hình ≠ ý câu đầu". Câu hay nói ở mỗi video ngắn nằm ở §CM-VOICE 7 (khối hết chỗ); tiểu từ "dày như họ (đếm)" đã có ở mục 4. ship.kit 944 → 986 of 1,000.
v13.5 (10/10, agent K): ship.kit 3 "giọng: tỉ lệ tiểu từ như bài mẫu (±10, số trên card)" (lượt giọng mặc định, §CM-HUMANIZE 2); IN "Cần {xưng hô} · …" thay "Cần bạn"; ship.card IN và ship.task 4 dùng {xưng hô}/[CẦN {XƯNG HÔ}: …]. Trả bằng "giọng, " và "(đếm" ở mục 3, "thông tin" ở IN. ship.kit 986 → 998 of 1,000.

<!-- @section ship.kit src=9db159ebb9 -->
KIỂM TRA TRƯỚC KHI GIAO · âm thầm · mọi bài · không chắc → cắt hoặc hạ bậc
0 TRỌNG TÂM: một trụ cột, một loại bài · ý chính ≤20 tiếng · một niềm tin ("X → hoá ra Y") · không chủ đề để dành · từ khoá một lần trong thân bài, + lời mời
1 SỰ THẬT (số, tên, câu trích, kết quả, khách làm gì, nghĩ gì) chỉ của coach hay trang đã đọc, trích y nguyên; chủ đề, phần dạy: dùng hiểu biết nghề. Thiếu → hạ bậc (kể cách làm, nhóm đầu) hay hỏi
2 KHÁC BIỆT 0–2 mỗi ô, ≥8, không ô 0: chi tiết cụ thể · một ý, một niềm tin · bằng chứng trong bài · chi tiết chỉ coach có · quan điểm có người cãi. Hook, dòng 1 caption: không rào, phán suông, châm ngôn; chữ màn hình thêm một điều, không lặp ý câu đầu, không "X là Y"
3 GIỌNG + NGƯỜI MUA: nhịp, câu hay nói (≥ nửa), cách gọi khách; giọng: tỉ lệ tiểu từ như bài mẫu (±10, số trên card); không chữ cấm, tiếng Anh; người mua dừng ở câu đầu, tin. Sửa một lần
IN: bài xong → chỉ in bài. Thiếu, điều cấm → một dòng "Cần {xưng hô} · <câu hỏi>". Lý do: chỉ khi hỏi "tại sao?"

<!-- @section ship.card src=9ab2ae814b -->
KIỂM TRA TRƯỚC KHI GIAO · âm thầm · một lần mỗi đợt · không chắc → cắt hoặc hạ bậc · không khen
0 TRƯỚC: có dòng slot + chất liệu Bank? Chưa → HẠ BẬC (kể cách làm, nhóm đầu, bỏ số suất); chỉ hỏi khi cả bài dựa vào chỗ thiếu
1 VIẾT từ ID trong Bank; điểm dừng cứng thì không viết
2 SOÁT (Claude: scripts/ship_lint.py, chạy cuối): số, tên, câu trích có trong dòng đã dẫn, trích nguyên văn · kết quả = dòng P có Substantiated + Consent · gấp theo Ledger · từ khoá ×1 + lời mời · câu mở đầu kiểu mới · mở đầu không rào đón · 0 [CẦN …]
3 KIỂM khi viết xong, đọc lại dòng đã dẫn. Cổng: quan điểm, sự thật, giọng. Khác biệt 0–2: K từ khoá + chi tiết · V một ý, một niềm tin · A bằng chứng trong bài · Au chi tiết chỉ coach có · C quan điểm. Kiểm định dạng. Không chắc = trượt: dừng ở câu đầu, nghe đúng Card, người mua tin
4 SỬA lỗi đã chỉ ra, một lần. Sẵn sàng = qua cổng, khác biệt ≥8, không mục 0, đúng định dạng
IN dưới mỗi bài: Sẵn sàng <động từ> · viết từ <dữ kiện Bank> | Cần {xưng hô} · <1 câu hỏi>

<!-- @section ship.task src=fcad4ce29c -->
KIỂM TRA (tác vụ) · âm thầm · không chắc → cắt hoặc hạ bậc · không đoán, không khen
1 Chỉ viết từ ID trong Brief; không viết khan hiếm giả, bằng chứng bịa, lời cam kết, công kích người khác
2 Số, tên, câu trích nào cũng phải nằm trong một dòng Brief có dẫn, trích nguyên văn; kết quả chỉ lấy từ dòng P có Substantiated + Consent, không có thì kể cách làm; gấp chỉ khi Ledger ghi
3 Từ khoá 1 lần trong bài + lời mời · câu mở đầu không trùng recent_hook_stems · câu mở đầu không rào đón · không mục khác biệt nào 0: từ khoá + chi tiết, một ý, bằng chứng trong bài, chi tiết chỉ coach có, một quan điểm
4 Thiếu thông tin thì ghi [CẦN {XƯNG HÔ}: một câu hỏi], bài để Bản nháp. Trong tác vụ không bao giờ hỏi; câu hỏi (1 câu) để trong báo cáo lượt chạy
IN dưới mỗi bài: Sẵn sàng <động từ> · viết từ <dữ kiện Brief> | Bản nháp · cần: <câu hỏi>
