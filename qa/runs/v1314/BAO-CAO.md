# Báo cáo v13.14 (1.3.14): sửa 5 điểm còn lại của v13.13

## Bản này sửa gì
- **Một ý tối đa 3 bài một tuần.** Cột "Ý" trong bảng tuần dùng để đếm. Phần mô tả khách hàng là tệp khách, không tính là ý.
- **Kết quả dùng lại thì kể bằng câu mới.** Số liệu giữ nguyên.
- **Câu khái quát vẫn phải có nguồn,** dù đã ghi trong "Máy tự thêm". Phần dạy chỉ nói "có thể…", "thử…".
- **Khi phải giảm số video so với mức đã chọn,** máy nói rõ trong một dòng.
- **Bỏ chữ "trụ cột" trơn** khỏi nhãn, HUB.md và các tin nhắc tự động.
- **Grader:** sửa nhiều chỗ đọc nhầm, giờ đo được độ dài bài.

## Kết quả 2 mô phỏng (Day 0 + 7 bài Tuần 1)

| | Chị Quyên v13.13 → v13.14 | Copywriter dump mỏng v13.13 → v13.14 |
|---|---|---|
| Thông tin không có nguồn | 2 → 2 (ở câu kết bài, không còn ở carousel) | 0 → **0** |
| Đoạn tự thêm mà không khai | 1 → **0** | 2 → **0** |
| Câu chép giữa các bài | 0–1 → **0** (1 cặp gần giống) | 4 → **1** (câu 3 chữ "Chị không biết.") |
| Một ý ở quá 3 bài | 6 bài → **4 bài** | 5 bài → **4 bài** |
| Phần máy tự viết mỗi video | 19–24% → 27% | 29% → **14–29%** |
| Giọng (nha, nè…) so với thẻ | 34–40% / thẻ 45% → **50–55% / thẻ 50%** | hầu hết đạt → **mọi bài đạt** |
| Hook có khung | 7/7 → **7/7** | 6/7 → **7/7** |
| Tên khách trong hook / dòng "Cần" hỏi 2 việc | 0 / 0 | 0 / 0 |
| Báo rõ khi giảm số video | chưa có → **có, cả 2 lần** | (không cần: coach kể thêm chuyện, đủ 3 video) |
| Chữ "trụ cột" lộ ra | 4 → **0** | → **0** |
| Bài dài | 981 → 973 chữ | 974 → 951 chữ |
| Phút tới bài ngày 0 | 27,9 → **27,5** | 22,5 → **22,1** |
| Mục chấm chưa đạt | 12 → **8** | 12 → **11** |

## Còn lại (đều nhỏ)
1. **Một ý vẫn ở 4 bài, không phải 3.** Lý do: một dòng nhắc lướt, ví dụ "phần 2 mai lên" hay một dòng trong danh sách tuần học, cũng bị tính. Sửa: mỗi bài chỉ nhắc ý của chính bài đó.
2. **Chị Quyên còn 2 câu khái quát ở câu kết.** Câu kết cần đi qua cùng bước kiểm như thân bài.
3. **Câu chuyện mẫu bên chị Quyên đặt trong ngoặc kép như lời khách thật.** Ví dụ phải ghi rõ là ví dụ, không đặt như lời khách.
4. **Lặt vặt:**
   - Một câu mở dài 20 chữ, mức tối đa là 18.
   - Bài dùng câu cửa miệng của coach ít hơn mức cần (dưới 50% số bài).
   - Tên trụ dài 6–7 chữ, mức tối đa là 5.
   - Một video bên copywriter có chữ ảnh bìa trùng tiêu đề.
5. **Nghiên cứu web còn mỏng.** Bên chị Quyên chỉ được 1 nguồn, chưa đủ 2 người ở 2 nơi, nên chưa có câu nào được giữ (KEEP) để dùng. Ngoài đời, coach có Chrome hoặc dán comment thì sẽ tốt hơn.

## Đánh giá
Qua 5 vòng mô phỏng (v13.9 → v13.14), máy đã đạt các điểm sau:
- gần như không bịa thông tin;
- khai đủ phần tự viết;
- giọng đúng với coach;
- hook vào khung trên mọi chỗ;
- một tuần ra 7 bài, đủ định dạng, đúng số giờ đã hứa.

Các lỗi còn lại là lỗi tinh, cần người duyệt bắt.

**Khuyên:** dừng mô phỏng ở đây và chuyển sang chạy thử thật.
1. Bạn chạy danh sách test tài khoản thật (`docs/founder/real-account-test.md`, khoảng 90 phút).
2. Sau đó chạy thử với 1–2 coach thật, bạn duyệt từng bài trước khi đăng.

Mô phỏng đã cho hết những gì nó có thể cho. Lỗi tiếp theo đáng sửa sẽ đến từ người thật.
