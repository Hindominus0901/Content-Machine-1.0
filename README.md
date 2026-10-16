# Gói Hook + Giọng và Chiến lược (Content Machine v14.5)

Nhánh này chỉ chứa phần hook và phần giọng, chiến lược của Content Machine, để đọc riêng hoặc đưa người khác đọc. Hệ thống build, test và bộ cài nằm ở nhánh làm việc chính.

Độ dài đang áp dụng (bản 1.4.5):
- video ngắn 250–400 chữ;
- bài dài 400–500 chữ;
- video dài 1.000–1.500 chữ.

Bản tiếng Việt dùng cùng các con số, đếm theo tiếng.

## Đọc theo thứ tự này

### 1. Hook và CTA (`1-hook/`)
| File | Nội dung |
|---|---|
| `HOOK-FRAMEWORK.md` | **Đọc đầu tiên.** Khung hook + CTA đầy đủ: nguyên tắc, các khung câu, quy trình 4 bước có bảng chấm, hook theo từng chỗ (video, ảnh bìa, slide 1, tiêu đề email, bài dài), CTA kèm cặp sai → đúng, lỗi hay gặp, bảng tự kiểm, 16 ví dụ đã duyệt |
| `PRINCIPLES.md` | Luật hook/CTA bạn đã duyệt và 16 ví dụ gốc. Máy kiểm hook theo file này |
| `nghien-cuu/` | Nghiên cứu nền về hook/CTA và nguồn |
| `trong-may/HOOKS-*.md` | Phần hook máy đang dùng (thư viện khung, cách chấm) |
| `trong-may/COPY-*.md` | Khung viết, kể chuyện, thuyết phục, CTA, dùng lại một ý cho nhiều bài |
| `trong-may/BANKS-*.md` | Kho CTA, quà (lead magnet), bảng từ khoá |

### 2. Giọng và chiến lược (`2-giong-va-chien-luoc/`)
| File | Nội dung |
|---|---|
| `GIONG-VA-CHIEN-LUOC.md` | **Đọc đầu tiên.** Phần A là chiến lược (thông điệp, trụ, tuyến, tỷ lệ 40/40/20, tuần 7 bài), có ví dụ coach "Vy". Phần B là giọng (đo tiểu từ, câu cửa miệng, xưng hô, bảng tự kiểm 16 dòng) |
| `trong-may/STRATEGY-*.md` | Phần chiến lược máy đang dùng |
| `trong-may/PLAYBOOK-*.md` | Cách máy dựng chiến lược và ví dụ tuần |
| `agents/cm-writer.md` | Luật người viết: viết đúng giọng coach, không thêm chi tiết, không kéo dài |
| `agents/cm-reviewer.md` | Luật người duyệt: kiểm hook, CTA, giọng, thông tin có nguồn |

`*-VN.md` là bản tiếng Việt, `*-EN.md` là bản tiếng Anh. Các file trong `trong-may/` và `agents/` là đúng chữ máy đọc, nên có ký hiệu kỹ thuật (§CM-…). Hai file "Đọc đầu tiên" viết cho người đọc.

## Ghi chú
- Lấy từ bản 1.4.5 (commit f110502 trên `claude/relaxed-einstein-h9m241`).
- Khi sửa luật hook hay giọng thì sửa ở nhánh chính, rồi cập nhật lại nhánh này.
