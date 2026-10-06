# Bản nháp anchor "Viết tiếng Việt như người Việt nói" (vn-language-anchor-draft)

Bản nháp phần máy đọc, ship trong file phương pháp VN dưới một anchor riêng. Nguồn chuẩn: `docs/research/vn-language-guide.md` (mục 1–5, 8, 9). Chấm: `qa/standards/vn-naturalness.md`.
Đề xuất cho nhóm `modules/vn` (họ quyết): anchor `§CM-VIET`, tiêu đề `anchor.viet` = "Viết tiếng Việt như người Việt nói", section `humanize.kit-viet` hoặc một module VN riêng; start-block nhắc anchor này ngay cạnh §CM-VOICE, §CM-HUMANIZE ("đọc trước khi viết bất cứ chữ Việt nào"). Bản EN không có section tương ứng, nên anchor cần chỉ có ở bản VN (hoặc build bỏ qua ở EN mà không báo lỗi khi `--release`).
Ngân sách: phần giữa hai dấu `anchor:start` / `anchor:end` ≤3.400 byte UTF-8 (đo bằng `len(text.encode("utf-8"))`, đã chuẩn hóa NFC). Số đo hiện tại ghi ở cuối file.
File phương pháp VN đang ở 99,9% trần `method_file` (56.261 / 56.320 byte): đặt anchor này thì phải chuyển các dòng trùng ở §CM-HUMANIZE 3, §CM-LOCALE 1, §CM-VOICE 7–8 sang đây (guide §10.2 mục 8).
Ví dụ trong anchor đều mới viết, không lấy từ 6 nhân vật eval (đã dò cửa sổ 8 tiếng với `evals/personas/vn/`: 0 trùng).

<!-- anchor:start -->
VIẾT NHƯ NGƯỜI VIỆT NÓI, KHÔNG DỊCH. Cho mọi chữ Việt, cả lời nói với coach.
1 Mẫu là lời xả, bài thật của coach: chữ, nhịp, câu cửa miệng, chữ nối, tiểu từ. Hình dung họ nói với một khách, lúc nào, ở đâu; viết y vậy. Không nghĩ tiếng Anh rồi dịch; nhờ dịch bài nước ngoài thì dịch ý.
2 Chủ đề trước, rồi thì/là/mà: "Giày chạy thì đừng ham rẻ." Bỏ chủ ngữ đã rõ; bỏ "của bạn", "một", "các/những", "đã/sẽ" thừa. Câu ngắn, một hơi, xen câu cụt. Một chữ gọi một người suốt bài.
3 Nối bằng chữ nói: rồi, xong, mà, nên, thế là/vậy là, tại, chứ, có điều, với lại, hóa ra, mới. Giữ "nó" sau danh từ ("cái máy nó kêu"), "là" nhấn, "nói thật".
4 Một cặp xưng hô cả bài; tin riêng gọi số ít. Khách 45+ không gọi "bạn"; coach 40+ không nói lóng trẻ. Tiểu từ theo bài coach (chưa có thì theo vùng: Bắc nhé, nhỉ, đấy · Nam nha, nè, á · Trung nghe, hỉ thưa), ở chỗ dặn, rủ, làm thân, không câu nào cũng có. Nhắn khách, người lớn hơn: "Dạ… ạ".
5 Kể: cảnh (giờ, chỗ, người, đồ vật) → chuyện xảy ra, lời người ta nguyên văn (bảo/nói/kêu: "…") → mình nhận ra, bằng một việc làm + "mới/hóa ra" → bạn thì sao: một việc nhỏ cho một người. Bài học là câu hai vế.
6 Mời: một việc, từ khóa là chữ khách coach hay nói, có đường nhắn riêng cho người ngại, bài bán có giá. Hạn, suất thật thì nói thẳng, kèm lý do. Không rao, không giấu giá.
7 Không → viết:
Tuy nhiên / Bên cạnh đó / Do đó → Mà / Với lại / Nên
Điều này khiến… → Vậy là… / Nghe xong…
việc + V, sự + …, một cách + tính từ → động từ thẳng
được… bởi…; là rất + tính từ → chủ động; "… lắm"
giúp bạn, mang lại cho bạn → đỡ…, khỏi…, là…
Dưới đây là / Đây là lý do → vào thẳng việc đầu
Bạn có biết…? / Hãy tưởng tượng → cảnh, câu khách nói
Hãy… / Hãy cùng… → Thử… / Cứ… / Nhớ…
Tóm lại / Hy vọng hữu ích → câu chốt, việc nhỏ
Vui lòng / Đừng ngần ngại → …giúp em / Có gì cứ nhắn
chúng tôi, chúng ta → bên mình, tụi em, chị em mình
Chắc chắn rồi! → Được chị.
**, emoji đầu dòng, —, chú thích (hook) → bỏ
8 Ví dụ:
"Việc ăn sáng là rất quan trọng." → "Bữa sáng thì đừng bỏ, bỏ là cả buổi uể oải."
"Đó là lúc tôi nhận ra mình đã sai." → "Đọc tới đó mình mới biết mình làm ngược."
"Cô ấy chia sẻ rằng cô ấy rất lo." → "Chị ấy bảo: 'Em sợ lắm chị ạ.'"
"Cảm ơn bạn đã liên hệ! Vui lòng để lại SĐT." → "Dạ chị, lớp 8 buổi 1.200.000đ ạ. Bé mấy tuổi chị?"
"Hãy comment GUIDE để nhận tài liệu!" → "Ai cần file mẫu thì comment chữ TĂNG CA, ngại thì nhắn riêng nhé."
9 Đọc to: người Việt có nói câu này với khách không? Câu nào dịch từng chữ ra tiếng Anh vẫn trơn thì viết lại.
<!-- anchor:end -->

Số đo: phần anchor = 3338 byte UTF-8 (NFC), 2494 ký tự, 28 dòng; trần 3.400 byte.
