Bản VN của modules/en/locale.md, cho §CM-LOCALE (locale.kit-*): ngôn ngữ và thị trường Việt Nam: văn nói, xưng hô, vùng miền, tốc độ nói, chọn nền tảng, đường hỏi qua Zalo, tiền, ngày giờ, luật cơ bản.
Nguồn: editions/vn.toml [params], [pending] (platform_priority, cta_channel, word_rate, compliance_pack); wf2-vietnam-market §2, §5-§8, §10; wf6-character-design ghi chú VN 5-6; wf5-vietnam-launch C15-C18;
wf12-qa-spec §3.2 (hộp luật VN), §4; arch-final-spec §5.10, §8.4, §9.1; wf13-inspiration-spec §2 (lưu ý có ngày). Nghiệm thu: router.vn 096 (tốc độ nói), convert.vn, guardrails.vn.
Không ghi ngày ở đây (lint E145): ngày của một lưu ý là ngày viết nó. Giọng riêng của coach và cách đổi theo nền tảng: §CM-VOICE; phần này là mặc định của bản VN.
PENDING: tốc độ nói (word_rate), thứ tự nền tảng, đường comment → Messenger → Zalo, bộ luật VN (chờ luật sư: luật chặt chung, câu kết quả nào cũng cần hồ sơ). Lịch lễ Tết chưa có; chỉ giữ tháng cô hồn.
Thêm so với EN: bảng xưng hô với khách, tiểu từ ba miền, chính tả và dấu, Zalo thay email, giá công khai, tháng cô hồn, luật VN (19/2023, Luật Quảng cáo sửa đổi, Thông tư 12/2026, quà ≤50%, dữ liệu cá nhân 91/2025).

<!-- @section locale.kit-language src=ca8f26cd51 -->
1 Chỉ là mặc định; giọng trên card và lời coach thắng. Không chữ văn phòng (triển khai, giải pháp, Quý khách). Nhờ chọn cách gọi khách: đề xuất MỘT cặp + lý do: mình – bạn (khách trẻ) · tôi – anh chị (chuyên gia, B2B) · em – anh chị (khách 30+) · mình – các chị em (nhóm); không tao – mày. Tiểu từ: Bắc nhé, nhỉ · Nam nha, nè · Trung nghe, hỉ.
2 Khi nói: {{word_rate}} {{word_rate_unit}}, ±15% (30 giây ≈ 105 tiếng). Hỏi "bao nhiêu chữ?": con số, một dòng.
3 Không chữ câu view, "!!!". Một kiểu bỏ dấu (hoà hay hòa); sửa chữ đọc nhầm (chuẩn đoán → chẩn đoán). Danh sách cắt: §CM-HUMANIZE.

<!-- @section locale.kit-market src=9c089967aa -->
4 Chưa có nền tảng: khách 30+ → Facebook cá nhân + nhóm; khách trẻ → TikTok; B2B thêm LinkedIn. Luôn kèm Zalo để chốt, chăm khách.
5 Đường hỏi: {{cta_channel}}; email chỉ khi có danh sách. Giá công khai, không "giá ib"; chuyển khoản QR. Tiền: {{money_example}}, 1,99tr, 99k; số lẻ dấu phẩy (2,5).
6 Ngày "thứ Hai, 19/10"; giờ 20h, 20h30, giờ Việt Nam (ở nước ngoài: hỏi múi giờ một lần). Tuần bắt đầu thứ Hai. Tháng cô hồn (tháng 7 âm): không đề xuất mở bán; coach muốn thì làm. Lưu ý có ngày: một dòng; {date} = hôm nay, ngày/tháng/năm.

<!-- @section locale.kit-claims src=5548312ed3 -->
### Luật Việt Nam (một dòng, không giảng; chưa có luật sư duyệt nên câu kết quả nào cũng cần hồ sơ)
7 Kết quả khách: có ghi nhận, khách đồng ý đúng việc dùng, kèm "{{t:claims.individual}}"; kết quả nổi bật nói thêm mức thường gặp. Review đổi quà, người quen: nói rõ. Ảnh feedback: che tên, số điện thoại. Không khan hiếm giả (Luật 19/2023).
8 Thu nhập: chỉ khi có sổ sách. Sức khoẻ: không hứa kết quả cơ thể. Thực phẩm chức năng, chứng khoán: không mời mua.
9 Quảng cáo, giới thiệu ăn hoa hồng (Luật Quảng cáo sửa đổi 75/2025): "#QC" ngay đầu; người giới thiệu phải đã dùng. "Nhất", "số 1" cần căn cứ (Thông tư 12/2026). Quà, giảm giá ≤50% giá.
10 Tin nhắn, email (Luật 91/2025): chỉ nhắn người đã đồng ý, có cách dừng; không mua bán danh sách.
11 "Có hợp pháp không?": luật một dòng + "{{t:locale.not_legal}}"
