# Thử Content Machine trên tài khoản thật (khoảng 100 phút)

**Để làm gì.** Bạn đóng vai coach mới, cài plugin rồi dùng thử từ đầu đến cuối trên Claude và ChatGPT thật. Mỗi bước: làm gì, phải thấy gì, chụp gì; đánh dấu ☐ Đạt hay ☐ Không. Bước nào "Không": chụp màn hình, ghi một dòng, làm bước kế.

**Tên menu** theo tài liệu dự án, ngày 10/10/2026; app hay đổi giao diện. **Nếu menu khác, chụp màn hình gửi mình.**

---

## 0. Chuẩn bị (5 phút)

- ☐ Tài khoản **Claude Pro**, đăng nhập trên máy tính, có cài **app Claude cho máy tính** (Mac/Windows).
- ☐ Tài khoản **ChatGPT Plus**, đăng nhập trên máy tính.
- ☐ Điện thoại có app Claude và app ChatGPT, cùng tài khoản.
- ☐ File **`content-machine-plugin.zip`** để trong thư mục Tải về. **Không giải nén.**
- ☐ Một tài khoản Notion (bản miễn phí là đủ) và một tài khoản Google.
- ☐ Đồng hồ bấm giờ và giấy ghi số phút.

**Chuyện coach giả để kể.** Dùng chuyện này, đừng dùng chuyện khách thật. Đọc to vào micro hoặc dán vào:

> Mình là Lan, coach dinh dưỡng cho mẹ bỉm sau sinh ở Hà Nội, làm được 4 năm. Khách hay than "ăn ít mà vẫn không xuống cân, lại mất sữa". Câu mình bị hỏi hoài là "sau sinh mấy tháng thì được ăn kiêng?". Có chị khách 32 tuổi, sinh bé thứ hai, trước ăn mỗi ngày một bữa cho nhanh gầy, mệt rã rời. Theo mình 8 tuần, chị ăn đủ ba bữa, sữa vẫn đều, chị nói thấy nhẹ người hơn. Điều mình ngứa mắt nhất là mấy trà giảm cân quảng cáo "giảm 5 ký 7 ngày". Gói của mình là 8 tuần kèm 1-1 qua Zalo, giá 3,5tr. Mình đăng chủ yếu trên TikTok và Facebook.

Máy hỏi thêm thì cứ bịa cho hợp với chuyện Lan.

---

## 1. Cài plugin trên Claude (10 phút)

| Làm gì | Phải thấy gì | Kết quả | Chụp |
|---|---|---|---|
| 1. Vào claude.ai trên máy tính → **Customize** → **Plugins** → **Add** → **Upload plugin** → chọn file zip. | Plugin "content-machine" hiện trong danh sách, đang bật. | ☐ Đạt ☐ Không | Danh sách plugin |
| 2. Nếu Claude báo cần Code execution: **Settings → Capabilities** → bật lên. | Không còn báo lỗi. | ☐ Đạt ☐ Không ☐ Không bị hỏi | Thông báo nếu có |
| 3. Bấm vào plugin, xem bên trong. | Có 2 skill chính (content-machine-vn, content-machine-en) và khoảng 18 skill đồng hành (tên bắt đầu bằng cm-…). | ☐ Đạt ☐ Không | Danh sách skill |
| 4. Tạo **Project** tên "Lan test" (Projects → New project). | Project trống, mở được. | ☐ Đạt ☐ Không | — |

## 2. Cài plugin trên ChatGPT (10 phút)

Phần chưa chắc nhất: tài liệu ghi ChatGPT nhận plugin của Claude, nhưng chưa ai thử trên tài khoản thật.

| Làm gì | Phải thấy gì | Kết quả | Chụp |
|---|---|---|---|
| 1. chatgpt.com → **Settings** → **Security and login** → bật **Developer mode**. | Công tắc bật. | ☐ Đạt ☐ Không | Trang Settings |
| 2. Tìm mục **Plugins** (có thể nằm dưới **Apps**) → tải file zip lên. | ChatGPT nhận file, không báo lỗi định dạng. | ☐ Đạt ☐ Không | Màn hình sau khi tải |
| 3. Nếu không có chỗ tải: ghi lại các menu bạn thấy. | — | ☐ Không có chỗ tải | Mọi menu trong Settings |
| 4. Tạo **Project** tên "Lan test". | Project mở được. | ☐ Đạt ☐ Không | — |

Bước 2 không được: dùng file dự phòng `CONTENT-MACHINE-VN-1-FILE.md` (trong zip bản VN), đính kèm vào chat, gõ `Bắt đầu`, và ghi lại là đã dùng cách này.

---

## 3. Buổi đầu, tới lúc có video quay hôm nay (35 phút, làm trên Claude)

**Bấm giờ khi gửi tin đầu, dừng khi thấy "QUAY HÔM NAY".** Ghi số phút: ______ (mục tiêu: khoảng 35 phút với coach thật, khi kể nhanh thì ít hơn).

| Làm gì | Phải thấy gì | Kết quả | Chụp |
|---|---|---|---|
| 1. Trong project "Lan test", mở chat mới, gõ `Bắt đầu`. | Dòng đầu: **"◆ Content Machine · Kiểm tra cài đặt: ✓ hướng dẫn ✓ file phương pháp · Brand Card: hôm nay mình làm"**. | ☐ Đạt ☐ Không | Tin trả lời đầu |
| | **Lỗi cần báo ngay:** thấy "✗ file phương pháp (chế độ gọn)". | ☐ Có lỗi này | |
| 2. Cũng trong tin đầu đó. | Máy nói hôm nay khoảng 35 phút và hỏi **"gọi bạn là anh, chị hay bạn?"**. Máy xưng mình–bạn. | ☐ Đạt ☐ Không | (cùng ảnh) |
| 3. Gõ `chị`. | Từ đây máy xưng **em**, gọi **chị** ("Dạ, em chào chị."). Máy mời kể bằng **micro bàn phím điện thoại** vì micro của Claude chưa nghe được tiếng Việt. | ☐ Đạt ☐ Không | Tin trả lời 2 |
| 4. Dán chuyện của Lan. | "Nhận rồi. 3 câu đáng tiền chị vừa nói:" và một câu kiểu "em đang tìm hiểu …". | ☐ Đạt ☐ Không | |
| 5. Trả lời các câu hỏi thêm (tối đa khoảng 6 câu, **mỗi tin một câu**). Đến câu hỏi về kênh, máy có thể hỏi **một lần** chị có Claude in Chrome hay muốn dán comment (A/B/C). Chọn A. | Không bao giờ có 2 câu hỏi trong một tin. Câu hỏi về trình duyệt chỉ xuất hiện một lần. | ☐ Đạt ☐ Không | Tin có câu hỏi trình duyệt |
| 6. Trả lời câu hỏi cuối (máy tự dừng hỏi); muốn dừng sớm thì gõ `đủ rồi`. | Chiến lược gửi trong **tối đa 3 tin**, mỗi tin ngắn, có lựa chọn A/B/C, một lựa chọn ghi "(máy khuyên)". Máy không kết bằng "Bạn có muốn…không?". | ☐ Đạt ☐ Không | Cả 3 tin |
| 7. Gõ `OK` ở mỗi tin. | Một tin riêng **"QUAY HÔM NAY · …"**: kịch bản đủ câu nằm trong khung chép, caption nằm ở khung riêng, có dòng "Ngại xin comment thì gõ 'nhẹ'.". | ☐ Đạt ☐ Không | Tin QUAY HÔM NAY |
| 8. Đọc kịch bản. | Viết toàn tiếng Việt, không hứa "giảm X ký Y ngày", không bịa số liệu. | ☐ Đạt ☐ Không | |
| 9. Xem dưới kịch bản. | Nếu máy tự thêm phần dạy hay ví dụ: một dòng **"Máy tự thêm: đoạn N"** ghi theo số đoạn (bao nhiêu đoạn cũng được). Không có câu nào máy thêm mà thiếu trên dòng đó. | ☐ Đạt ☐ Không ☐ Không có gì máy thêm | Kịch bản + dòng dưới |
| 10. Đọc dòng "Cần". | Chỉ **một** dòng "Cần", hỏi **một điều**, ≤20 chữ (kiểu "có sẵn quà chưa?"). | ☐ Đạt ☐ Không | (cùng ảnh) |
| 11. Đọc câu đầu và cả kịch bản. | Kịch bản xoay quanh **một ý** (ý khác để cho tuần). Câu đầu theo một khung hook (ví dụ "Nếu…", câu hỏi gọi đúng người, "Cho mình N phút…", "Từ … lên …"), một câu nói vừa phải. | ☐ Đạt ☐ Không | |
| 12. Xem Lan xưng gì trong kịch bản. | Lan xưng **mình/tôi** như bài của Lan, **không** xưng "chị" (chị–em chỉ dùng trong chat). | ☐ Đạt ☐ Không | |
| 13. Xem chỗ dùng chuyện chị khách 32 tuổi. | Trước khi đưa kết quả hay chi tiết của chị khách vào bài, máy hỏi **một lần** chị khách đã cho kể chưa (hỏi ở dòng "Cần" hay lúc hỏi thêm); chưa rõ thì chưa dùng. Không hỏi lại lần hai. | ☐ Đạt ☐ Không | Tin có câu hỏi này |
| 14. Quay xong (hay giả như đã quay), gõ `tiếp`. | Brand Card, dòng lưu, bảng **Tuần 1**: số bài khớp **số giờ chị chọn ở chiến lược** (khoảng 2,5 giờ: 3 video ngắn + 1 bài dài + 1 tin Zalo hay email; khoảng 3,5 giờ: thêm 1 video ngắn, 1 carousel; dưới 2 giờ: 3 bài), có cột **Ý, hook**, không hai bài cùng một ý. Bài CHUYỂN ĐỔI của tuần 1 là tin xin khách trả lời, **chưa chào bán, chưa có giá**. Chưa có câu hỏi hub. Máy lưu **HUB.md** cuối ngày 0. | ☐ Đạt ☐ Không | Card + bảng + HUB.md |

Làm lại bước 1–3 trên ChatGPT (chỉ đến tin trả lời 2, khoảng 5 phút). ☐ Đạt ☐ Không.

## 4. Chat mới, gõ "tiếp": máy có nhớ không (5 phút)

| Làm gì | Phải thấy gì | Kết quả | Chụp |
|---|---|---|---|
| 1. Claude: làm theo dòng lưu (chép card → project → **Add text content**). Mở **chat mới** trong project, gõ `tiếp`. | "Kiểm tra cài đặt: … · Brand Card v1 ✓" rồi một dòng **"Lần trước: … · đang dở bước …"** (hoặc "Mình nhớ: …"), sau đó làm tiếp đúng chỗ. Vì đây là lần "tiếp" đầu khi chưa có hub, cùng tin đó có **một** dòng hỏi hub: A) Notion B) Google Sheet C) Để sau, chỉ HUB.md, có "(máy khuyên)": chưa kết nối Notion thì máy khuyên B hay C, không khuyên A. Vẫn xưng em–chị. | ☐ Đạt ☐ Không | Tin đầu |
| 2. Mở chat mới **ngoài** project, gõ `tiếp`. | Máy **không đoán**, không nói "mình nhớ". Máy nhờ dán HUB.md hay Brand Card. | ☐ Đạt ☐ Không | Tin đầu |
| 3. Làm lại bước 1 trên ChatGPT. | Như bước 1. | ☐ Đạt ☐ Không | Tin đầu |

## 5. Hub: Notion, Google Sheet, HUB.md (15 phút)

| Làm gì | Phải thấy gì | Kết quả | Chụp |
|---|---|---|---|
| 1. Trả lời câu hỏi hub đã có ở bước 4.1 (không cần gõ thêm `tiếp`). | Câu hỏi hub chỉ xuất hiện **một lần** (ở bước 4.1), không lặp lại ở tin sau. | ☐ Đạt ☐ Không | Tin hỏi hub |
| 2. Chọn A khi **chưa** kết nối Notion. | Một bước duy nhất: Claude: **Settings → Connectors → Notion → Connect**. | ☐ Đạt ☐ Không | |
| 3. Kết nối Notion, nhắn `xong`. | Máy dựng trang **"Content Machine · Lan"** có Bắt đầu ở đây, Chiến lược, HUB, sáu bảng (Nội dung, Chiến dịch, Tuyến nội dung, Ngân hàng, Tìm hiểu, Số liệu). Báo "Hub của chị xong rồi: {link}". Ghi số phút: ______ | ☐ Đạt ☐ Không | Trang Notion + view Lịch |
| 4. Mở Notion, xem các trang khác của bạn. | Máy **không đụng** tới trang nào ngoài "Content Machine · Lan". | ☐ Đạt ☐ Không | |
| 5. Chat mới, gõ `dùng Google Sheet`. | 3 bước: sheets.new → File → Import → Upload 5 file CSV trong `Level-ups/Board` (hoặc máy in sẵn dòng tiêu đề để dán). Sau khi viết một bài, máy in **dòng để dán** (khung tsv, ≤6 cột). | ☐ Đạt ☐ Không | Sheet sau khi dán |
| 6. Gõ `lưu hub`. | HUB.md có 8 phần (Chiến lược trong 5 dòng, Lịch tuần này, Đang chờ chị chọn, …). Claude: một file + "Add to project". ChatGPT: file tải về, hoặc khung chép. | ☐ Đạt ☐ Không | HUB.md trong project |

## 6. Việc tự chạy (15 phút)

**Claude (chỉ app trên máy tính, không có trên web hay điện thoại):**

| Làm gì | Phải thấy gì | Kết quả | Chụp |
|---|---|---|---|
| 1. Trong chat, gõ `cài tác vụ`. | Một tin: các bước + khung lời nhắc để chép. | ☐ Đạt ☐ Không | |
| 2. App Claude máy tính → thanh bên **Scheduled → New task → Set up manually**. Tên "Content Machine", dán khung, chọn **Weekdays 7:07**, không chọn thư mục → **Schedule** → **Run now**. | Chạy xong không đứng lại chờ bạn bấm duyệt (nếu có hỏi duyệt thì ghi lại mình đã chọn chế độ nào). Ra bài hoặc nhắc đúng việc của hôm nay, kết bằng "TIẾP →". | ☐ Đạt ☐ Không | Kết quả lần chạy + hộp duyệt nếu có |
| 2b. Tạo thêm **tác vụ thứ hai**: dán đúng khung đó, tên "Content Machine · thứ Sáu", chọn **Weekly, thứ Sáu, 15:07** → Schedule → Run now. | Lần chạy hỏi số liệu tuần (Số liệu thứ Sáu), không ra bài mới. Danh sách Scheduled có **2** tác vụ. | ☐ Đạt ☐ Không | Danh sách tác vụ + kết quả |
| 3. Mở Notion. | Tác vụ chỉ ghi vào trong trang hub, không ghi gì hai lần. | ☐ Đạt ☐ Không | |

**ChatGPT (Plus):**

| Làm gì | Phải thấy gì | Kết quả | Chụp |
|---|---|---|---|
| 4. Trong project, gõ `cài tác vụ`. Máy in **4 khung**; mỗi khung dán vào một chat mới rồi gửi. | ChatGPT tạo đủ 4 tác vụ, xem ở **Scheduled** (hoặc **Tasks**): "Bài tuần này" thứ Hai 7:07 · "Một việc hôm nay" thứ Ba tới thứ Năm 6:37 · "Số liệu thứ Sáu" thứ Sáu 15:07 · "Làm mới hằng tháng" thứ Tư đầu tháng 11:07. (ChatGPT Free/Go chỉ có 3: không có tác vụ hằng tháng, nó thành TIẾP của thứ Sáu cuối tháng.) | ☐ Đạt ☐ Không | Danh sách tác vụ |
| 5. Nếu ChatGPT chỉ trả lời mà không hẹn giờ: Scheduled → **New**, dán khung. | Tác vụ có trong danh sách. | ☐ Đạt ☐ Không | |

Xong thì **xoá** tác vụ thử cho khỏi tốn lượt.

## 7. Claude in Chrome đọc bình luận (5 phút)

Chỉ đọc. **Không** bình luận, thả tim, theo dõi hay vào nhóm. Không chép tên hay nick người bình luận vào ghi chú.

| Làm gì | Phải thấy gì | Kết quả | Chụp |
|---|---|---|---|
| 1. Cài tiện ích **Claude in Chrome**, đăng nhập Claude Pro. | Biểu tượng Claude có trên Chrome. | ☐ Đạt ☐ Không | |
| 2. Trong chat Content Machine, gõ: `đọc giúp 10 comment đầu của video này` + link một video TikTok công khai về giảm cân sau sinh. | Máy dùng Chrome của bạn, chép lời khách, **gọi người theo vai** (ví dụ "một mẹ bỉm"), không ghi tên. | ☐ Đạt ☐ Không | Kết quả |
| 3. Làm lại với một bài đăng Facebook công khai. | Như trên. | ☐ Đạt ☐ Không | Kết quả |

## 8. Dùng trên điện thoại (5 phút)

| Làm gì | Phải thấy gì | Kết quả | Chụp |
|---|---|---|---|
| 1. App Claude trên điện thoại → project "Lan test" → chat mới → `tiếp`. | Nhớ đúng chỗ dở, xưng em–chị, mỗi tin vừa một màn hình. | ☐ Đạt ☐ Không | Màn hình điện thoại |
| 2. Bấm micro **bàn phím** (không phải nút sóng âm), nói 1 phút tiếng Việt. | Chữ ra đủ, không bị cắt. | ☐ Đạt ☐ Không | |
| 3. Làm lại bước 1 trên app ChatGPT. | Như bước 1. | ☐ Đạt ☐ Không | |
| 4. Bấm nút chép ở khung kịch bản. | Chép được trọn khung. | ☐ Đạt ☐ Không | |

---

## 9. Gửi lại cho mình

Gửi qua Zalo hay Drive, một thư mục tên `test-<ngày>`:

1. **Ảnh chụp** của mọi ô "Chụp", đặt tên theo số bước (ví dụ `3-7.png`), nhất là các bước bị ☐ Không.
2. **Bản chép chat** của buổi đầu (phần 3) và chat "tiếp" (phần 4), cả Claude lẫn ChatGPT:
   - Claude: bấm ⋯ / **Share** ở chat → tạo link chia sẻ, gửi link. Không được thì chọn hết nội dung (Ctrl/Cmd+A), chép, dán vào file .txt.
   - ChatGPT: **Share** ở góc trên → Copy link. Hoặc **Settings → Data controls → Export data** (file gửi qua email, có thể mất vài giờ).
3. **Bảng này** đã đánh dấu, cùng số phút ở phần 3 và phần 5.
4. Link trang Notion "Content Machine · Lan" (Share → cho mình quyền xem).
5. Một dòng cảm nhận: chỗ nào chán, rối hay chờ lâu.

---

> **Lỗi hay gặp**
> - **"✗ file phương pháp (chế độ gọn)"**: plugin chưa bật, hoặc chat mở trước khi cài xong. Mở chat mới. Vẫn lỗi thì chụp gửi mình.
> - **Máy nói tiếng Anh, hoặc vẫn xưng "bạn" sau khi chọn "chị"**: chụp tin đó. Đây là lỗi cần sửa.
> - **Micro Claude không ra chữ tiếng Việt**: đúng như dự kiến. Dùng micro bàn phím điện thoại.
> - **Hết lượt dùng giữa chừng**: ghi giờ và bước đang làm, chờ rồi làm tiếp.
> - **Không thấy Scheduled**: chỉ có trong app Claude trên máy tính, không có trên web.
> - **Notion báo không có quyền**: kết nối lại, cho phép sửa trang.
> - **Menu khác với tài liệu này**: chụp màn hình gửi mình, rồi đi tiếp bằng cách bạn tìm được.
