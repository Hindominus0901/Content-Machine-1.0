Bản VN của modules/en/locale.md, cho §CM-LOCALE (locale.kit-*): ngôn ngữ và thị trường Việt Nam: văn nói, xưng hô, vùng miền, tốc độ nói, chọn nền tảng, đường hỏi qua Zalo, tiền, ngày giờ, luật cơ bản.
Nguồn: editions/vn.toml [params], [pending] (platform_priority, cta_channel, word_rate, compliance_pack); wf2-vietnam-market §2, §5-§8, §10; wf6-character-design ghi chú VN 5-6; wf5-vietnam-launch C15-C18;
wf12-qa-spec §3.2 (hộp luật VN), §4; arch-final-spec §5.10, §8.4, §9.1; wf13-inspiration-spec §2 (lưu ý có ngày). Nghiệm thu: router.vn 096 (tốc độ nói), convert.vn, guardrails.vn.
Không ghi ngày ở đây (lint E145): ngày của một lưu ý là ngày viết nó. Giọng riêng của coach và cách đổi theo nền tảng: §CM-VOICE; phần này là mặc định của bản VN.
PENDING: tốc độ nói (word_rate), thứ tự nền tảng, đường comment → Messenger → Zalo, bộ luật VN (chờ luật sư: luật chặt chung, câu kết quả nào cũng cần hồ sơ). Lịch lễ Tết chưa có; chỉ giữ tháng cô hồn.
Thêm so với EN: bảng xưng hô với khách, chính tả và dấu, Zalo thay email, giá công khai, tháng cô hồn, luật VN (19/2023, Luật Quảng cáo sửa đổi, Thông tư 12/2026, quà ≤50%, dữ liệu cá nhân 91/2025).
Văn nói, tiểu từ ba miền: §CM-NATURAL 4 (mục 1 chỉ trỏ về đó). Quà ≤50%: dòng luật nằm ở §CM-GUARDRAILS (QUYỀN CỦA COACH) và §CM-CTA-KIT 9, không lặp ở mục 9. Mục 7 trỏ về §CM-GUARDRAILS cho hồ sơ và sự đồng ý.
Tích hợp 6/10 (ngân sách file phương pháp ≤56.320 byte): mục 5 bỏ "email chỉ khi có danh sách" (start-block bước 7, §CM-MESSAGES 1); mục 7 trỏ dòng LỜI HỨA cho claims.individual; mục 10 trỏ §CM-MESSAGES 3; tiêu đề Luật VN bỏ "nên kết quả nào cũng cần hồ sơ" (§CM-GUARDRAILS LẶNG LẼ, KẾT QUẢ MỚI).
G1 6/10 (theo EN, K4): mục 6 "Tuần lịch từ thứ Hai; tuần kế hoạch: §CM-CARD 3" (tuần kế hoạch đếm từ plan_start). locale.not_legal gọn hơn ("việc của bạn").
Cắt bù byte G1 (không bỏ luật): mục 5 bỏ "Đường hỏi: {{cta_channel}}" (start-block bước 7 "Đường đi: {{cta_channel}}", luôn trong ngữ cảnh khi có file này); mục 1 bỏ "Văn nói, tiểu từ: §CM-NATURAL." và mục 3 bỏ "Danh sách cắt: §CM-HUMANIZE." (cả hai anchor có trong danh sách ĐỌC TRƯỚC, NATURAL "trước mọi chữ Việt"; §CM-VOICE 7 vẫn trỏ NATURAL).
Cắt bù byte G2/VG1 6/10 (không bỏ luật): mục 5 định dạng tiền trỏ dòng TIẾNG VIỆT của khối hướng dẫn (cùng {{money_example}}, 1,5tr, 99k).

<!-- @section locale.kit-language src=9c73bc19c8 -->
1 Chỉ là mặc định; giọng trên card và lời coach thắng. Không chữ văn phòng (triển khai, giải pháp, Quý khách). Nhờ chọn cách gọi khách: đưa một cặp + lý do: mình – bạn (khách trẻ) · mình – anh chị (khách 30+) · em – anh chị (coach trẻ hơn khách) · tôi – anh chị (chuyên gia, B2B) · mình – các chị em (nhóm); không tao – mày.
2 Độ dài đếm bằng chữ, không tính giây (mỗi người nói nhanh chậm khác nhau): video ngắn 120–200, bài dài ≈1.000, video dài 1.000–1.500. Hỏi "dài bao nhiêu?": số chữ, một dòng; chỉ khi hỏi mới đổi ra phút, khoảng {{word_rate}} {{word_rate_unit}}.
3 Không chữ câu view, không "!!!". Bỏ dấu một kiểu (hoà hay hòa); sửa chữ hay sai (chuẩn đoán → chẩn đoán).

<!-- @section locale.kit-market src=ee314d4827 -->
4 Chưa có nền tảng: khách 30+ → Facebook cá nhân + nhóm; khách trẻ → TikTok; B2B thêm LinkedIn. Luôn kèm Zalo để chốt, chăm khách.
5 Giá công khai, không "giá ib"; chuyển khoản QR. Tiền như dòng TIẾNG VIỆT; số lẻ dấu phẩy (2,5).
6 Ngày "thứ Hai, 19/10"; giờ 20h, 20h30, giờ Việt Nam (coach ở nước ngoài: hỏi múi giờ một lần). Tuần lịch từ thứ Hai; tuần kế hoạch: §CM-CARD 3. Tháng cô hồn (tháng 7 âm): không đề xuất mở bán, coach muốn thì làm. Lưu ý có ngày: một dòng; {date} = hôm nay, ngày/tháng/năm.

<!-- @section locale.kit-claims src=5548312ed3 -->
### Luật Việt Nam (một dòng, không giảng; chưa có luật sư duyệt)
7 Kết quả khách: như §CM-GUARDRAILS và dòng LỜI HỨA; kết quả nổi bật thì nói thêm mức thường gặp. Review đổi quà, của người quen: nói rõ. Ảnh feedback: che tên, số điện thoại. Không khan hiếm giả (Luật 19/2023).
8 Thu nhập: chỉ khi có sổ sách. Sức khoẻ: không hứa kết quả trên cơ thể. Thực phẩm chức năng, chứng khoán: không mời mua.
9 Quảng cáo, giới thiệu ăn hoa hồng (Luật Quảng cáo sửa đổi 75/2025): "#QC" ngay đầu; người giới thiệu phải dùng rồi. "Nhất", "số 1" cần căn cứ (Thông tư 12/2026).
10 Tin nhắn, email: Luật 91/2025, làm như §CM-MESSAGES 3.
11 "Có hợp pháp không?": luật một dòng + "{{t:locale.not_legal}}"
