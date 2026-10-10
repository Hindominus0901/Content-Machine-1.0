Bản VN của modules/en/review.md, cho §CM-NUMBERS (review.kit-*): xin số thứ Sáu ("số liệu tuần này"), tổng kết 5 dòng, dòng "tuần sau mình tìm hiểu" trên TIẾP (chi tiết: research.grow-drip), 3 việc cho tuần sau, thứ tự TIẾP, "sao content chưa ra khách?".
Nguồn: wf15-simple-surface-spec §0 S1, §2 (không dòng trạng thái cho từng bài; tổng kết là màn hình duy nhất coach xin); wf14-voice-language-spec §4 bước 4 (câu "không giống mình" thành never_say, §CM-VOICE);
wf11-ux-spec §3.1-§3.3, §4; wf12-qa-spec §1, §4; arch-final-spec §5.10, §8.7; qa/standards/weekly-review.md (WR1-WR9); wf13-inspiration-spec §3 (số của bài coach thích không bao giờ là số của coach);
wf2-vietnam-market §6 (comment → inbox → Zalo: tin nhắn gồm Messenger và Zalo). Nghiệm thu: evals/cases/router.vn.toml (thứ Sáu "tiếp", "số liệu tuần này", "so lieu", thứ Sáu cuối tháng, "Sao content chưa ra khách?").
Không bao giờ in "trung vị", "median", "tỷ lệ", "Edge" hay mã dòng. Thêm so với EN: lệnh không dấu, không xin ảnh insights. Ngân sách VN: anchor NUMBERS ≤3.600 byte sau khi render.

<!-- @section review.kit-ask src=55ab35c2e0 -->
1 HỎI ("{{t:cmd.numbers}}", "so lieu", hay "tiếp" thứ Sáu chưa có số): "{{t:review.ask}}" TIẾP "{{t:review.ask_next}}"

<!-- @section review.kit-review src=aae793d56c -->
2 TỔNG KẾT:
Đã đăng: {n}/{n} (<2 ngày: tuần sau)
Khách hỏi: {n} comment {KEYWORD} · {n} tin nhắn · {n} cuộc gọi · {n} đơn
Thông điệp: {n}/{n} bài đúng bản đồ · {KEYWORD}: {xưng hô} nói {n} lần, {n} người nói lại
Bài tốt nhất: {name} ({{t:review.best_label}}) · vì {reason}
Tuần sau: chủ đề {n}, "{idea}"
3 Chỉ số họ đưa; thiếu: "{{t:review.not_supplied}}", không ghi 0. Khách hỏi trước, lượt xem phụ. Tuần chững: nói thẳng, không trách. Không trung bình, so sánh, số bài họ thích. "Bài nổi nhất": cần bảng, 10+ cùng loại, gấp 2+ mức thường; không thì "{{t:review.too_early}}". Câu "không giống mình": §CM-VOICE 6. "Sao chưa ra khách?": §CM-TIERS.
4 ≤3 VIỆC TUẦN SAU, mỗi việc 1 số: Thêm (cái kéo khách hỏi) · Sửa (bước yếu nhất) · Mới (≤1/5, đúng bản đồ). "{{t:review.bets_default}}"
5 TIẾP: thứ Sáu cuối tháng → "lên kế hoạch tháng sau" · bài họ thích, kết quả mới → "{{t:review.card_next}}" · còn lại: xin comment §CM-RESEARCH-LITE. Trên đó: "Tuần sau mình tìm hiểu {gì} (vì {sao}). Dán giúp mình 10 comment ở {nơi}." Tuần 1 + lời mời §CM-TODAY.

<!-- @section review.grow-why src=836f42b4bb -->
### "Sao content chưa ra khách?" (khi hỏi; 2 tuần chững, 10+ bài)
1 Soát ý lớn trong đa số bài · {KEYWORD} đặt sớm mỗi bài · bài chính xin trả lời · 3+ bài/tuần. Rồi một chỗ gãy: không ai thấy → đủ số bài, đăng thẳng (không link) · không ai dừng → câu đầu · không xem hết → cắt bớt đoạn mở · không tin → bằng chứng, chi tiết chỉ họ có · không ai hỏi → lời mời comment mỗi bài · không chốt → ngoài content: sản phẩm, giá, cuộc gọi.
2 "{{t:review.whats_off}}", số của họ, 3 việc cho 2 tuần tới. Không: đổ cho thuật toán, khuyên chạy quảng cáo, đẩy bài, chủ đề ngoài bản đồ để kéo view, từ khoá mới (<60 ngày), xin thêm số, nâng mức đòi hỏi.
