# Hướng dẫn tiếng Việt cho Content Machine (vn-language-guide)

**Vai trò:** nguồn chuẩn (source of truth) về ngôn ngữ cho bản VN. Ai viết, sửa module VN, chuỗi chữ `strings/vn.toml`, ví dụ `locales/vn/examples.md`, danh sách `locales/vn/banned-tells.txt`, chuẩn chấm `qa/standards/vn-naturalness.md` hay ca eval `*.vn.toml` thì đọc file này trước.
**Không ship.** Phần máy đọc lúc chạy là bản rút gọn ở `docs/research/vn-language-anchor-draft.md` (một anchor riêng trong file phương pháp VN, ≤3.400 byte).
**Ngày viết:** 06/10/2026. **Cần duyệt:** một người bản ngữ mỗi vùng (Bắc, Trung, Nam) đọc lại các câu có ghi vùng; giọng Trung cần cả người Huế–Quảng lẫn người Nghệ Tĩnh.

> **Founder (nguyên văn):** "đặc biệt là ngôn từ và cách nối chuyện cách giao tiếp trong tiếng việt, t nghĩ m sẽ cần xem cái đó kĩ đấy, AI hay làm theo kiểu dịch từ anh sang việt nên câu cú từ ngữ cấn lắm"

Tóm một câu: máy phải viết như một người Việt đang nói chuyện, đang đăng bài, đang nhắn tin; không như một bản dịch từ tiếng Anh, không như bài văn mẫu, không như tổng đài.

---

## Mục lục

0. Đọc file này thế nào
1. Mười lăm nguyên tắc gốc
2. Văn dịch: danh mục mẫu, vì sao cấn, sửa thế nào
3. Nối chuyện: mở, nối, ngoặt, rút ý, kết (phần founder dặn kỹ)
4. Xưng hô, tiểu từ, độ thẳng, chữ tiếng Anh, emoji
5. Bán hàng, lời mời, tin nhắn, bình luận
6. Khác nhau theo nền tảng
7. Vùng miền và lứa tuổi
8. 39 cặp trước / sau, thêm 6 cặp ngắn
9. Phép thử: đọc to, dịch ngược, đếm mật độ
10. Cho maintainer: lint, chuẩn chấm, đề xuất sửa, câu hỏi mở, nguồn

---

## 0. Đọc file này thế nào

**Ba lớp kiểm, ba mức xử lý.** Mỗi mẫu ở mục 2 có một mức:

| Mức | Nghĩa | Ai bắt | Ở đâu |
|---|---|---|---|
| **Lint** | Gần như không bao giờ đúng trong chữ của coach hay chữ máy nói với coach. Gặp là viết lại | Máy (regex) | `locales/vn/banned-tells.txt` (lint E141 trên chuỗi và ví dụ ship; grader I23 trên chữ máy viết trong eval) |
| **Judge** | Thường là văn dịch nhưng có lúc đúng. Người chấm đọc ngữ cảnh rồi quyết | Giám khảo, người duyệt bản ngữ | `qa/standards/vn-naturalness.md` mục VN6 |
| **Đếm** | Từng lần thì không sai, nhiều quá mới sai | Grader đếm, giám khảo xem lại | Bảng ngưỡng ở mục 9.3 |

**Ví dụ trong file này đều mới viết, nhân vật hư cấu.** Không có câu nào lấy từ 6 nhân vật eval trong `evals/personas/vn/` (chị Thu, chị Hạnh, Minh Anh, anh Khoa, anh Đức, anh Tuấn), để bài kiểm tra chép câu (I19) không bị bẩn. Lời của 6 nhân vật chỉ được dùng làm kho dò bắt nhầm và để đếm chữ (mục 1, 2.7). Ai lấy ví dụ từ file này vào gói thì chỉ lấy ở mục 8 và mục 3, và chạy lại kiểm tra chép (mục 10.4).

**Các coach hư cấu dùng trong ví dụ** (khác ngách với 6 nhân vật eval):

| Tên | Tuổi, nơi | Nghề | Xưng hô | Giọng |
|---|---|---|---|---|
| Vy | 30, Hà Nội | Dạy Excel, báo cáo cho dân văn phòng | mình – bạn | Bắc |
| Phát | 33, Sài Gòn | Dạy chủ quán ăn tự quay TikTok | mình – anh chị | Nam |
| thầy Tùng | 38, Đà Nẵng | Dạy bơi trẻ 5–10 tuổi | thầy – các con; thầy – anh chị (phụ huynh) | Trung, viết gần trung tính |
| Quân | 26, Hà Nội | Chụp ảnh sản phẩm cho shop | em – anh chị | Bắc |
| Trâm | 29, Thủ Đức | Chủ tiệm nail | em, tiệm – chị, mấy chị | Nam |
| Khang | 31, Sài Gòn | Coach chạy bộ cho dân văn phòng | mình – mấy bạn | Nam |
| anh Phong | 45, Huế | Tư vấn mở quán cà phê nhỏ | anh – em; tôi – anh chị | Trung |
| chị Diễm | 36, Cần Thơ | Coach ăn dặm cho mẹ bỉm | chị – các mẹ, em | Nam |
| Ngọc | 23, Hà Nội | Dạy nói tiếng Anh cho sinh viên | mình – mọi người | Bắc, Gen Z |
| Hiếu | 33, Đà Nẵng | Thợ vệ sinh, sửa máy lạnh | Hiếu – anh chị | Trung |
| chị Hồng | 41, Biên Hòa | Dạy cắm hoa mở tiệm | chị – em | Nam |
| cô Lan | 46, Hà Nội | Luyện thi vào lớp 10 | mình – anh chị phụ huynh; cô – các con | Bắc |
| Hoàng | 34, Hà Nội | Dạy nói trước đám đông | mình – bạn | Bắc |
| chị Mai | 50, Gò Vấp | Dạy nghề nấu cơm tấm bán sáng | chị – mọi người | Nam |
| cô Nga | 52, Nam Định | Dạy làm bánh tại nhà | cô – các cháu; mình – các chị | Bắc |

**Bằng chứng dùng ở file này:**
- Kho lời nói của 6 nhân vật eval (khoảng 37.000 chữ lời xả, bài viết, kịch bản nói; Bắc, Trung, Nam; 29–45 tuổi). Đây là giọng **đích** mà bộ eval đang đòi, viết cho giống lời thật, không phải ngữ liệu cào từ mạng. Số đếm chỉ để định hướng.
- Mẫu trả lời của AI chưa có pack (`evals/baselines/vn-*`): khoảng 3.800 chữ.
- Tài liệu trong repo: `wf2-vietnam-market.md` §5, §8; `wf9-pov-vietnam.md` §3; `wf5-vietnam-launch.md` F8, F10; `wf14-voice-language-spec.md`.
- Nguồn ngoài ở mục 10.6. Phần lớn bảng vùng miền, bảng chữ nối, khung kể là **phán đoán của người bản ngữ**, ghi rõ ở từng chỗ, cần người mỗi vùng duyệt.

---

## 1. Mười lăm nguyên tắc gốc

1. **Lời xả của coach là mẫu, không phải tư liệu.** Chữ, nhịp, câu cửa miệng, chữ nối, tiểu từ của họ là thứ máy bắt chước trước tiên. Có 2–3 bài thật của coach thì đưa vào mọi lần viết (wf14 V3). Một bài thật dạy máy nhiều hơn mười luật cấm.
2. **Hình dung, đừng dịch.** Cao Xuân Hạo: dịch sát từng chữ là cách tốt nhất để dịch sai. Trước khi viết, hình dung coach đang nói với **một** người khách: lúc mấy giờ, ở đâu, người đó vừa nói gì. Rồi viết lại y như vậy. Lệnh đúng là "viết như chị Hồng đang nhắn cho một em học viên lúc 9 giờ tối", không phải "viết bài về cắm hoa bằng tiếng Việt tự nhiên". Coach nhờ dịch một bài nước ngoài để đăng lại (DECISIONS: được, kèm một dòng lưu ý) thì cũng dịch **ý**, kể lại bằng giọng coach, không dịch từng chữ.
3. **Đề trước, thuyết sau.** Tiếng Việt là ngôn ngữ đề–thuyết: nói cái đang bàn tới trước, rồi "thì / là / mà", rồi mới nhận xét. "Giày chạy thì đừng ham rẻ." "Máy lạnh không mát thì coi cái lưới lọc trước." AI dựng câu chủ–vị kiểu Anh nên thừa chủ ngữ, thừa "của bạn", thừa "đã / sẽ", thừa "được… bởi".
4. **Câu ngắn, nói một hơi.** Mỗi câu một ý, đọc lên không phải lấy hơi giữa chừng. Câu dài thì là câu kể nối bằng dấu phẩy và "rồi, xong, mà". Xen một câu cụt 2–5 chữ: "Thế thôi." "Run thật." "Bảy tháng thì đóng."
5. **Nối bằng chữ nói.** *thì, mà, rồi, xong, nên, thế là / vậy là, tại, chứ, có điều, với lại, hóa ra, thế mà / vậy mà, mới*. Trong kho lời nói: "thì" 456 lần, "mà" 384, "rồi" 352, "xong" 92; còn *tuy nhiên, bên cạnh đó, ngoài ra, vì vậy, điều này, không chỉ… mà còn, một cách* đều 0.
6. **Kể theo cảnh, ý đến sau.** Chuyện mở bằng giờ, chỗ, người, đồ vật; có câu người ta nói nguyên văn; ngoặt bằng một việc làm cụ thể; bài học là một câu ngắn ở cuối. Không mở bằng luận điểm rồi "Đây là lý do".
7. **Lời người khác để nguyên văn.** Dẫn bằng *bảo, nói, kêu, nhắn, hỏi đúng một câu*, rồi hai chấm và ngoặc kép. Không "chia sẻ rằng", không "cho biết rằng". Đừng chuốt câu khách cho đúng ngữ pháp.
8. **Bài học là một câu hai vế, hoặc nằm trong miệng người khác.** "Rẻ lúc học, đắt lúc đền." "Má dạy: tiền nào của nấy." Không "Bài học rút ra là…", không "Hãy luôn nhớ rằng…".
9. **Kết bằng một việc nhỏ cho một người, hoặc một câu hỏi thật.** "Ai đang… thì tối nay thử…" Không "Hy vọng bài viết hữu ích", không "Đừng quên like, share".
10. **Một cặp xưng hô, một vùng, đúng tuổi.** Cặp xưng hô là quyết định đầu tiên, không phải chi tiết. Mặc định giọng Bắc không "nha, nè", giọng Nam không "nhé, đấy"; nhưng bài thật của coach thắng mặc định (người Bắc dưới 30 viết "nha" trên mạng là thường, coach Bắc 40+ thì không). Khách 45+ không gọi là "bạn".
11. **Tiểu từ là giọng, đặt đúng chỗ.** Ở chỗ dặn, rủ, làm thân, gỡ căng. Thiếu thì như bản dịch; rắc đều câu nào cũng có thì như diễn. Liều dùng lấy theo bài thật của chính coach.
12. **Chữ thường ngày thay chữ sách.** *lắm, quá, ghê, thiệt* thay *rất, vô cùng*; *thấy* thay *cảm thấy*; *khách* thay *khách hàng*; *cái sổ, cái máy* (có "cái") thay danh từ trần. Kho lời nói: "cái" 508, "lắm" 73, "rất" 3, "cảm thấy" 0, "khách" 320, "khách hàng" 4.
13. **Cảm xúc mộc, kể bằng việc làm.** *sợ, ngại, thương, tức, mừng, quê, nản*. Không *hạnh phúc vỡ òa, biết ơn sâu sắc, trân quý, chữa lành*. Kho lời nói: "sợ" 82, "ngại" 24, "thương" 21; "hạnh phúc", "biết ơn", "cảm động" đều 0.
14. **Mời nhẹ mà rõ, giá nói thẳng.** Một việc, từ khóa tiếng Việt, luôn có đường nhắn riêng cho người ngại, có giá nếu là bài bán. Không giục, không giấu giá, không nổ.
15. **Đừng sửa quá tay.** "Nó" sau danh từ ("cái máy nó kêu"), "là" nhấn ("mệt là mệt thiệt"), "thì" nhiều trong lời nói, "nói thật / nói thiệt", "tóm lại là" giữa lời kể, chữ Anh coach thật sự dùng: đều là tiếng Việt thật. Cắt sạch thì câu lại trơ, lại giống văn dịch (mục 2.7).

**Phép thử chung:** đọc to lên, hỏi "người Việt có nói câu này với khách không?". Rồi chọn ba câu, dịch từng chữ ra tiếng Anh: câu nào dịch ra trơn tru, câu đó là câu Tây (dịch giả Trần Tiễn Cao Đăng nhận xét bản dịch kém có "cấu trúc ngữ pháp giống hệt như trong tiếng Anh").

---

## 2. Văn dịch: danh mục mẫu, vì sao cấn, sửa thế nào

Văn AI tiếng Việt lệch theo **ba hướng cùng lúc**:

| Nguồn lệch | Nghe như | Dấu hiệu | Ví dụ AI | Người thật nói |
|---|---|---|---|---|
| **A. Dịch từ tiếng Anh** | Sách hướng dẫn dịch | Câu chủ–vị kiểu Anh, thì động từ, danh từ hóa, bị động, hook kiểu Mỹ | "Đó là lúc tôi nhận ra rằng tôi đã sai." | "Lúc đấy mình mới biết là mình làm ngược." |
| **B. Văn mẫu nhà trường, văn PR** | Bài nghị luận, thông cáo | Mở–thân–kết, "Như chúng ta đã biết", "đóng vai trò quan trọng", "Tóm lại" | "Có thể nói, sự kiên trì đóng vai trò vô cùng quan trọng." | "Ngày nào cũng làm một ít, vẫn hơn cả tuần dồn vào một bữa." |
| **C. Tổng đài, trợ lý ảo, banner** | Nhân viên trực page, ChatGPT, tờ rơi | "Cảm ơn bạn đã liên hệ", "Chắc chắn rồi!", "Dưới đây là", "Nhanh tay kẻo lỡ!" | "Chắc chắn rồi! Dưới đây là 5 mẫu caption tuyệt vời dành cho bạn:" | "5 bản đây chị, chị chọn nha:" |

Cả ba có chung một lỗi: **không có ai cụ thể đang nói với một người cụ thể.** Không tên, không vai (em, chị, mình), không giờ, không giá, không câu hỏi thật.

Danh mục dưới đây chia năm tầng: từ vựng, cấu trúc câu, nối ý và mở kết, xưng hô và giọng, trình bày và con số. Cột **Mức** theo mục 0. Câu sai là kiểu AI hay viết; câu sửa có ghi vùng khi dùng tiểu từ.

### 2.1 Từ vựng: chữ dịch, chữ sáo

| # | Mẫu (gốc tiếng Anh) | Vì sao cấn | Sửa | Ví dụ: sai → đúng | Mức |
|---|---|---|---|---|---|
| T1 | "giúp bạn…", "cho phép bạn…" (help you, allow you) | Đồ vật, khóa học làm chủ ngữ rồi "giúp bạn": tờ rơi dịch | Nói người ta được gì, đỡ gì: "đỡ", "khỏi", "là… liền" | "Ứng dụng này cho phép bạn đặt lịch dễ dàng." → "Đặt lịch trong app luôn, khỏi gọi điện." | Judge; ≥2 lần một bài thì viết lại |
| T2 | "mang lại / mang đến / đem lại" (bring, deliver) | Động từ dịch, hay đi kèm danh từ hóa ("mang lại sự tự tin") | Tả kết quả thấy được | "Lớp bơi mang lại cho bé sự tự tin dưới nước." → "Học xong là bé dám úp mặt xuống nước, hết khóc." | Judge (nghĩa đen "mang tới tận nhà" thì giữ) |
| T3 | Từ thổi phồng: nâng tầm, bứt phá, đột phá, đẳng cấp, vượt trội, thần tốc, giải pháp toàn diện, bùng nổ doanh số (elevate, breakthrough, premium) | Đọc là biết quảng cáo, mất tin ngay | Nói số và việc cụ thể | "Bứt phá doanh số cùng khóa TikTok đột phá." → "Học 3 buổi, về đứng bếp tự quay luôn, điện thoại cũ cũng được." | Lint |
| T4 | Ẩn dụ sáo: hành trình, chìa khóa (nghĩa bóng), khám phá, mở khóa tiềm năng, khai phá, hành trang, giải mã, đánh thức tiềm năng (journey, key, unlock) | Coach Việt không gọi lớp 8 buổi là "hành trình" | Nói lớp mấy buổi, làm gì, ra cái gì | "Hành trình 8 tuần trang bị hành trang vững chắc." → "8 tuần, tuần nào cũng ngồi sửa file của từng bạn." | Lint (nghĩa đen "mở khóa cửa", "đánh thức con dậy", "chìa khóa để trên bàn", "chuẩn bị hành trang đi biển" thì giữ; "hành trình" nghĩa đen hiện vẫn bị bắt, xem 10.2) |
| T5 | "giải pháp", "tối ưu (hóa)" (solution, optimize) | Chữ tài liệu doanh nghiệp; khách không mua "giải pháp" | Nói việc mình làm | "Giải pháp tối ưu cho ảnh sản phẩm." → "Điện thoại cũng chụp đủ sáng, miễn đặt đèn đúng chỗ." | Judge |
| T6 | "trải nghiệm" làm danh từ (experience) | Chữ marketing, không tả được gì | Tả khách thấy gì, làm gì | "Mang đến trải nghiệm thư giãn tuyệt vời." → "Khách ngồi một lúc là quên luôn cái điện thoại." | Judge (động từ "làm thử, học thử" thì được) |
| T7 | Động từ rỗng "thực hiện, tiến hành" (perform, conduct) | Thêm một động từ trước động từ thật | Dùng động từ thật | "Chúng ta sẽ tiến hành kiểm tra máy." → "Hiếu tháo cái lưới lọc ra coi trước." | Lint ("tiến hành"); Judge ("thực hiện") |
| T8 | Hán Việt trang trọng trong lời nói: nhằm, bởi lẽ, gia tăng, sở hữu, tiếp cận, cải thiện, duy trì, đáng kể, thúc đẩy | Kịch bản nói nghe như bản tin | để, vì, tăng, có, tới được, đỡ hơn, giữ, nhiều | "Nhằm gia tăng tỷ lệ khách quay lại…" → "Muốn khách quay lại nhiều hơn thì…" | Đếm (kịch bản nói: từ 2 chữ thì sửa) |
| T9 | Khung danh từ dịch: tầm quan trọng của việc, sức mạnh của, nghệ thuật của, ngành công nghiệp làm đẹp, mang tính…, đầy cảm hứng, cá nhân hóa | Dịch "the importance of, the power of, -al, inspiring, personalized"; "công nghiệp" là nhà máy | Nói thẳng bằng động từ; "nghề nail", "ngành làm đẹp" | "Tầm quan trọng của việc chăm sóc khách cũ trong ngành công nghiệp làm đẹp." → "Làm nail mà bỏ bê khách cũ là tự đuổi khách đi." | Lint (2 cụm đầu); Judge |
| T10 | Cụm nhấn kiểu Anh: hơn bao giờ hết, không thể bỏ lỡ, bạn không thể bỏ qua, bất kể bạn là ai, bất kỳ | Khuôn tựa SEO dịch | Nói lý do thật, bỏ cụm nhấn | "5 sai lầm mà bạn không thể bỏ qua." → "5 cái lỗi hồi mới mở tiệm, em dính đủ cả năm." | Lint (3 cụm đầu); Đếm ("bất kỳ" ≥2) |
| T11 | Thành ngữ dịch sát: ở cuối ngày, đi thêm một dặm, phá vỡ băng, con voi trong phòng, đặt mình vào đôi giày của, tư duy ngoài chiếc hộp, thay đổi cuộc chơi | Người nghe phải dịch ngược ra tiếng Anh mới hiểu | Dùng câu Việt có sẵn: nói cho cùng, làm hơn người ta một chút, mở lời làm quen, chuyện ai cũng biết mà không ai nói, đặt mình vào hoàn cảnh người ta | "Hãy đặt mình vào đôi giày của khách." → "Thử nghĩ coi, mình là khách thì mình ngại chỗ nào." | Lint ("phá băng", "bước ra khỏi vùng an toàn" đã quen: Judge) |
| T12 | Câu an ủi dịch từ sách self-help: bạn không đơn độc, bạn xứng đáng, phiên bản tốt nhất của chính mình, tôi đã từng ở vị trí của bạn | Dịch "You're not alone / You deserve / best version of yourself / I've been in your shoes" | An ủi bằng chuyện chung: "không phải mỗi mình chị đâu", "mình cũng từng y chang" | "Bạn không đơn độc. Bạn xứng đáng được nghỉ ngơi." → "Mệt thì nghỉ một bữa đi chị, đâu phải mỗi mình chị vậy." (Nam) | Lint (chỉ khung self-help: "bạn xứng đáng được nghỉ ngơi / hạnh phúc"; khen người thắng "giải này bạn xứng đáng mà" thì giữ) |
| T13 | Chữ sến: vỡ òa, biết ơn vũ trụ, chữa lành, trân quý, thanh xuân, năng lượng tích cực, lan tỏa giá trị, truyền cảm hứng | Cảm xúc dán nhãn, không kể việc | Một chữ mộc + một việc làm (mục 3.14) | "Tôi hạnh phúc vỡ òa." → "Em mừng quá, khao cả tiệm trà sữa." (Nam) | Lint (vỡ òa, biết ơn vũ trụ, lan tỏa giá trị); Judge (còn lại, trừ khi coach tự nói) |
| T14 | Chú thích tiếng Anh trong ngoặc, chữ nghề marketing: "câu mở đầu (hook)", "(CTA)", "nỗi đau (pain point) của khách hàng" | Giáo trình dịch; người đọc của coach không cần chữ nghề | Bỏ ngoặc; nói khách khổ chỗ nào, bằng câu khách nói | "Hãy xác định nỗi đau (pain point) của khách hàng mục tiêu." → "Khách khổ nhất chỗ nào? Ghi đúng câu họ than." | Lint |
| T15 | "rất / thực sự / vô cùng / hoàn toàn" đặt trước tính từ (very, really, truly) | Tiếng Việt nhấn ở cuối: lắm, quá, ghê, thiệt, dữ lắm; hoặc từ láy | Dời nhấn ra sau, hoặc tả | "Câu chuyện thực sự rất ý nghĩa." → "Nghe xong ngồi im luôn." | Đếm ("rất" >2/100 chữ); "vô cùng" trong lời nói: sửa |
| T16 | "cảm thấy" (feel) | Lời nói dùng "thấy" | "thấy", hoặc bỏ | "Tôi cảm thấy rất lo lắng." → "Lo lắm." | Đếm (≥2 lần một bài thì đổi) |

### 2.2 Cấu trúc câu

| # | Mẫu (gốc tiếng Anh) | Vì sao cấn | Sửa | Ví dụ: sai → đúng | Mức |
|---|---|---|---|---|---|
| C1 | "một cách + tính từ" (effectively, easily) | Dịch trạng từ đuôi -ly, kéo câu dài như công văn | Tính từ đứng sau động từ; "cho kỹ", "lắm"; hoặc tả kết quả | "Cắm hoa một cách chuyên nghiệp và tinh tế." → "Cắm xong để ba ngày hoa vẫn tươi." | Lint ("có một cách đơn giản để…", "nói một cách dễ hiểu" thì giữ) |
| C2 | "việc + động từ" làm chủ ngữ (V-ing) | Danh từ hóa kiểu Anh | Cho động từ đứng đầu, hoặc "Muốn… thì…" | "Việc chạy chậm giúp bạn chạy được lâu hơn." → "Chạy chậm thì chạy được lâu." | Đếm (≥2 một bài; lời nói 1 là sửa) |
| C3 | "sự + động/tính từ", "với sự…" (change, confidence, with confidence) | Danh từ trừu tượng | Nói bằng động từ, tính từ, việc | "Đứng trước đám đông với sự tự tin." → "Lên nói mà giọng không run." | Judge ("với sự" thì sửa); "sự thật, sự việc, sự cố" là danh từ gốc |
| C4 | Bị động "được / bị + động từ" dịch passive: được thiết kế, được tạo ra, được ghi nhận | Tiếng Việt chủ yếu nói chủ động; "được" khi có lợi, "bị" khi có hại | Đưa người làm lên đầu câu | "Khóa học được thiết kế dành riêng cho chủ quán." → "Lớp này mình soạn cho chủ quán ăn nhỏ." | Judge (≥2 lần một bài thì viết lại) |
| C5 | "được / bị … bởi …", "bởi đội ngũ / chuyên gia" (by) | GS Nguyễn Văn Khang chỉ ra lối "làm bởi (ai)" thay cho "do ai làm"; lời nói gần như không ai dùng | "do… làm", hoặc chủ động | "Giáo trình được biên soạn bởi đội ngũ chuyên gia." → "Giáo trình này thầy tự soạn, dạy bơi mười năm mới viết ra được." | Lint ("bởi vì, bởi lẽ" không tính) |
| C6 | "là + rất / vô cùng / hoàn toàn + tính từ" (is very…) | Tính từ tiếng Việt tự làm vị ngữ | Bỏ "là"; nhấn ở cuối | "Việc khởi động là rất quan trọng." → "Khởi động kỹ, cái này quan trọng lắm." | Lint ("là" nhấn kiểu nói "mệt là mệt thiệt", "cái máy là cũ lắm rồi" thì giữ; "là" dẫn ý sau thấy, nói, bảo, khen: "khách khen là rất ngon" cũng giữ); Judge ("là cực kỳ" trong lời nói video) |
| C7 | "Điều này / Điều đó" + khiến, cho thấy, có nghĩa là, giúp, dẫn đến (This means / This makes) | Một chữ "điều này" thay cả câu trước | "Vậy là", "nghĩa là", "nên", "chuyện đó", "vụ đó"; hoặc gộp hai câu | "Nhiều quán giảm giá 50%. Điều này khiến khách quen mất lòng." → "Giảm 50% thì khách mới tới, mà khách quen thấy mình hớ." | Lint |
| C8 | "Điều quan trọng là…", "Điều mà… là…", "Sự thật là…", "Trên thực tế," (The important thing is / What… is / In fact) | Câu chẻ kiểu Anh | Nói thẳng ý; "nói thật", "có điều" | "Điều mà tôi muốn nói với bạn là…" → "Mình nói cái này thôi:" | Judge ("cái mà… là…" trong lời nói thì là tiếng Việt thật) |
| C9 | "rằng" sau nghĩ, nói, biết, tin (that-clause) | Lời nói bỏ "rằng" hoặc dùng "là" | Bỏ "rằng", hoặc "là" | "Tôi tin rằng ai cũng có thể bơi." → "Ai cũng bơi được, thầy thấy tận mắt rồi." | Đếm (kịch bản nói: 1 lần là sửa) |
| C10 | Chuỗi "của… của…" (of… of…) | Lồng sở hữu kiểu Anh | Ghép thẳng, bỏ "của" khi đã rõ | "Sự hài lòng của khách hàng của tiệm là thước đo của chúng tôi." → "Khách có quay lại không, nhìn vậy là biết tiệm làm tốt hay chưa." | Judge |
| C11 | "bằng cách + động từ", "thông qua việc…" (by doing) | Việc trước, kết quả sau mới là thứ tự Việt | "Muốn… thì…", "… là…" | "Bạn có thể giữ khách bằng cách nhắn hỏi thăm sau 3 ngày." → "Muốn khách quay lại thì 3 ngày sau nhắn hỏi thăm một câu." | Judge ("bằng cách nào?" và "kiếm khách bằng cách phát tờ rơi" khi kể thì giữ) |
| C12 | "một" và "những / các" thừa (a / -s) | Tiếng Việt dùng danh từ trần khi nói chung | Bỏ; hoặc "mấy", "ai cũng", "nào cũng" | "Tôi là một huấn luyện viên và tôi giúp những người mới chạy." → "Mình dạy người mới chạy." | Đếm |
| C13 | "đã / sẽ" gắn vào mọi động từ; "sẽ có thể", "đã và đang" | Tiếng Việt không bắt đánh dấu thì; "hồi đó, mai, giờ" là đủ | Bỏ "đã/sẽ" khi mốc thời gian đã rõ | "Sau khóa học, bạn sẽ có thể tự quay video." → "Học xong là tự quay được." | Lint ("sẽ có thể", "đã và đang"); Đếm (đã/sẽ >3/100 chữ) |
| C14 | "Nó" đầu câu chỉ ý tưởng, sản phẩm (It…) | Dịch "It" | Lặp danh từ, "cái này", "vụ này", hoặc bỏ chủ ngữ | "Phương pháp này rất đơn giản. Nó giúp bạn tiết kiệm thời gian." → "Cách này dễ, làm 5 phút là xong." | Judge ("nó" sau danh từ cụ thể trong lời nói thì giữ: "cái máy nó kêu") |
| C15 | Mệnh đề phụ dài đặt trước ý chính: "Mặc dù…, Sau khi…, Để…," (Although…, After…) | Người xem video quên mất đầu câu | Ý chính trước, nối thêm bằng "mà, rồi, thì, nên"; tách câu | "Sau khi hoàn thành buổi học đầu tiên và được tư vấn kỹ về kỹ thuật thở, học viên sẽ được xếp lớp." → "Học xong buổi đầu, thầy coi con thở ra sao. Rồi mới xếp lớp." | Judge (+ câu ≥40 tiếng thì tách) |
| C16 | "Với hơn X năm kinh nghiệm,…", "Là một…,", "Với tư cách là…" (With over X years…, As a…) | Dịch phần giới thiệu tiếng Anh | Nói thẳng: "Tôi làm nghề này 10 năm", "Mình cũng làm mẹ nên…" | "Là một người mẹ, tôi hiểu nỗi lo con biếng ăn." → "Chị cũng có đứa con biếng ăn, chị hiểu." | Lint ("Là một…,", "Với tư cách"); Judge ("Với X năm,") |
| C17 | "Để…, bạn cần (phải)…", "Nếu bạn muốn…, hãy…" (To…, you need to / If you want…, do…) | Khuôn hướng dẫn dịch | "Muốn… thì…", bỏ chủ ngữ, bỏ "cần phải" | "Để có thể bán được trên TikTok, bạn cần phải xây dựng lòng tin." → "Muốn bán được trên TikTok thì người ta phải tin mình trước đã." | Judge |
| C18 | Khung động từ dịch: "khiến… cảm thấy", "trở nên", "có xu hướng", "hãy đảm bảo rằng" (make you feel, become, tend to, make sure) | Dịch khung câu | "làm mình thấy", "thấy", "hay", "nhớ… nha / nhé" | "Hãy đảm bảo rằng bé đã ăn nhẹ trước khi bơi." → "Nhớ cho con ăn nhẹ trước 4 giờ nha." (Nam) | Lint (2 cụm); Judge |
| C19 | Dồn định ngữ thành một cục dài sau danh từ; "đến từ" (come from) | Tiếng Anh dồn tính từ trước danh từ, AI dời cả cục ra sau một hơi | Tách thành câu ngắn; "ở", "quê" | "Chương trình huấn luyện cá nhân hóa 1 kèm 1 chuyên sâu dành riêng cho người mới bắt đầu chạy bộ." → "Mình kèm riêng từng người, cho ai mới tập chạy, kiểu chạy ba bữa là đau gối á." (Nam) | Judge |
| C20 | "trong khi" để đối lập (while / whereas) | Dịch "while" | "còn", "mà", "… mà đã…" | "Nhiều người chạy 10 cây số cuối tuần, trong khi họ không khởi động." → "Cuối tuần chạy 10 cây mà không khởi động thì gối nó khóc." | Judge ("trong khi chờ" chỉ thời gian thì giữ) |
| C21 | Gọi người kiểu báo dịch: "một người phụ nữ 40 tuổi", "một khách hàng nam" | Người Việt gọi nhau bằng chữ họ hàng và một nét đời | "một chị tầm bốn mươi", "ông chú bên Sơn Trà", "em sinh viên năm hai" | "Một khách hàng nữ 50 tuổi liên hệ với tôi." → "Có một cô tầm năm chục gọi mình." | Judge |

### 2.3 Nối ý, mở bài, kết bài

| # | Mẫu (gốc tiếng Anh) | Vì sao cấn | Sửa | Ví dụ: sai → đúng | Mức |
|---|---|---|---|---|---|
| N1 | Liên từ văn viết đầu câu: Tuy nhiên, Do đó, Vì vậy, Ngoài ra, Bên cạnh đó, Hơn nữa, Thêm vào đó, Mặt khác (However, Therefore, Moreover) | Chữ của bài luận | "mà, nhưng mà, có điều, nên, thế nên / vậy nên, với lại, chưa kể, còn, rồi, xong" | "Chạy chậm giúp đỡ đau gối. Bên cạnh đó, nó còn giúp bạn thở đều hơn." → "Chạy chậm thì gối đỡ đau, thở cũng đều hơn. Mà khỏi cần mua giày xịn nha." (Nam) | Lint ("Bên cạnh đó,", "Thêm vào đó,"); Judge (kịch bản nói, tin nhắn: 0; bài dài: tối đa 1) |
| N2 | "không chỉ / không những… mà còn…" (not only… but also) | Khung AI dùng nhiều nhất | "vừa… vừa…", "đã… lại còn…", "chưa kể", hoặc tách hai câu | "Lớp không chỉ dạy bơi mà còn dạy con tự tin." → "Học xong con vừa bơi được, vừa dám tự xuống nước, khỏi cần ba mẹ đứng kè kè." | Lint ("không chỉ… mà còn"); Judge ("không những… mà còn" là cặp quan hệ từ Việt có sẵn, người lớn tuổi nói thật: một lần thì được, thành khung lặp mới sửa) |
| N3 | "Không phải X, mà là Y" lặp mỗi đoạn; châm ngôn dịch "Khách không mua X, họ mua Y" | Dịch "It's not X, it's Y"; người Việt cũng nói, nhưng một lần, và hay nói ý chính trước rồi "chứ không phải" | Ý chính trước, "chứ đâu phải / chứ không phải" | "Khách không mua hoa. Họ mua cảm xúc." → "Khách quay lại là vì hoa để được lâu, chứ đâu phải vì rẻ." | Đếm (>1 lần một bài); Judge (châm ngôn dịch thì sửa) |
| N4 | Bộ ba tu từ đều nhau; "Không X. Không Y. Chỉ Z." (rule of three) | Nhịp copywriting Mỹ, đoạn nào cũng ba | Một bài tối đa một bộ ba | "Đơn giản. Hiệu quả. Bền vững." → "Một trang giấy, làm thử một buổi. Vậy thôi." | Judge |
| N5 | Tự hỏi tự đáp + hai chấm "bật mí": "Kết quả?", "Lý do rất đơn giản:", "Và đây là điều thú vị:" (The result? / Here's the thing:) | Nhịp copywriting Mỹ lặp mỗi đoạn | Kể thẳng: "Ba tuần sau, con bơi được 10 mét." | "Kết quả? Doanh thu tăng gấp đôi." → "Ba tháng sau, trưa thứ Bảy quán kín bàn." | Judge (tối đa một lần một bài) |
| N6 | Chuyển cảnh kể chuyện dịch: Đó là lúc tôi nhận ra, Khoảnh khắc ấy, chợt nhận ra, Và đó là lúc, Tua nhanh 3 năm sau, Và rồi, Mọi thứ thay đổi khi, Ít ai biết rằng (That's when I realized / Fast forward / Little did I know) | Người Việt nối chuyện bằng mốc thời gian và chữ ngắn | "Bữa đó", "Hồi đó", "Rồi", "Xong", "Thế là", "Ai dè", "Hóa ra", "Mãi sau mới", "Từ hồi đó", "Ba năm sau" | "Khoảnh khắc ấy, tôi chợt nhận ra rằng mình đã sai." → "Đọc tới đó chị mới biết, ba năm nay chị làm ngược." | Lint ("Đó là lúc tôi nhận ra", "Khoảnh khắc ấy,", "chợt nhận ra rằng / một điều", "Và đó là lúc", "Tua nhanh"); Judge (còn lại; "chợt nhận ra" trơn là chữ Việt, "đang chạy thì chợt nhận ra quên khóa cửa" vẫn đúng, chỉ sửa khi nó làm công tắc ngoặt) |
| N7 | "Khi nói đến…", "Đối với…", "Về mặt…", "Liên quan đến…" để mở chủ đề (When it comes to / Regarding) | Tiếng Việt đặt chủ đề lên đầu rồi "thì" | "Nói tới X thì…", "X thì…" | "Khi nói đến việc chọn giày chạy, nhiều người mắc sai lầm." → "Giày chạy thì người mới hay sai đúng một chỗ." | Judge |
| N8 | Đếm ý "Đầu tiên,… Thứ hai,… Cuối cùng,…" trong lời nói (First, Second, Finally) | Dịch dàn ý | "Một là… Hai là… Ba là…", "Cái thứ nhất…, còn nữa…", hoặc kể theo thứ tự việc | "Đầu tiên, hãy chọn hoa. Thứ hai, cắt gốc. Cuối cùng, cắm." → "Một là chọn hoa còn búp. Hai là cắt xéo gốc trong nước. Xong mới cắm." | Judge (bài dạng danh sách thì được) |
| N9 | Mở bài "Bạn có biết (rằng)…?", "Bạn đã bao giờ tự hỏi…?", "Đã bao giờ bạn…", "Hãy tưởng tượng…", "Bạn đang gặp khó khăn trong việc…?", "Bạn có đang…?" (Did you know / Have you ever wondered / Imagine / Are you struggling with) | Hook dịch; hook Việt đi thẳng vào cảnh, con số, câu khách nói | Mở bằng cảnh, người, câu khách nói (mục 3.5) | "Bạn có biết rằng 70% người mới chạy bị đau gối?" → "Bữa trước có bạn nhắn: 'Anh ơi em chạy được ba bữa là đau gối.'" | Lint ("Bạn đã bao giờ… chưa?" đúng ngữ pháp Việt, chỉ sáo khi làm câu mở: Judge) |
| N10 | Mở bài "Trong thế giới / cuộc sống hiện đại…", "Trong thời đại / kỷ nguyên số…", "Ngày nay,", "Như chúng ta đã biết", "Chúng ta đều biết", "Không thể phủ nhận" (In today's world / As we all know) | Câu mở rỗng, văn nghị luận | Vào thẳng cảnh hoặc con số | "Trong cuộc sống hiện đại bận rộn, nhiều mẹ bỏ quên bữa sáng của con." → "Sáu giờ rưỡi, con còn ngái ngủ, mẹ thì cầm hộp sữa đứng chờ ở cửa." | Lint |
| N11 | "Dưới đây là… / Sau đây là… / Đây là lý do tại sao… / Đó là lý do vì sao… / Câu chuyện dưới đây" (Here are / Here's why) | Câu mặc định của ChatGPT tiếng Việt, cả khi máy nói với coach | "Có 3 việc", "Mình làm vầy nè", hoặc vào thẳng việc thứ nhất | "Dưới đây là 5 bước giúp bạn chụp ảnh đẹp." → "Ảnh sản phẩm em chụp theo 5 bước, bước đầu dễ ợt." | Lint ("Đây là cái sổ mình ghi" khi chỉ vào vật trong video thì giữ; "Đây là cách…": Judge) |
| N12 | "Hãy…", "Hãy cùng…", "Hãy để tôi…", "Hãy cho tôi biết…" (Let's / Let me / Make sure) | Chữ của khẩu hiệu, sách giáo khoa | "thử… đi", "cứ…", "nhớ… nha / nhé", "… đi chị", "Để mình kể" | "Hãy để tôi chia sẻ 3 bí quyết giữ hoa tươi." → "Giữ hoa tươi lâu, chị làm 3 việc." | Lint ("hãy cùng nhau / tìm hiểu", "hãy để tôi chia sẻ / kể / giải thích", "hãy cho tôi biết"); Đếm ("hãy" >1 lần một bài; "hãy để em lo" không tính) |
| N13 | Kết kiểu luận văn: Tóm lại, Kết luận:, Cuối cùng nhưng không kém phần quan trọng, Đầu tiên và quan trọng nhất, Chúc bạn thành công!, Hy vọng bài viết hữu ích, Bài học rút ra là, Hãy luôn nhớ (In conclusion / Last but not least / Good luck) | Bài mạng xã hội Việt kết bằng một câu chốt, một việc nhỏ, hoặc bỏ lửng | Câu chốt hai vế; "Ai đang… thì…"; "Thế thôi." | "Tóm lại, khởi động là chìa khóa. Chúc các bạn thành công!" → "Vậy thôi. Sáng mai khởi động đủ năm phút rồi mới chạy, chạy xong kể mình nghe nha." (Nam) | Lint ("Tóm lại," đầu câu, "Kết luận:", "Cuối cùng nhưng không kém phần quan trọng", "Chúc bạn thành công trên / trong / với…", "Hy vọng bài viết hữu ích", "Bài học rút ra", "Hãy luôn nhớ"); Judge ("tóm lại là" giữa lời kể là văn nói thật; "Chúc anh chị thành công nha!" trước một việc thật như khai trương, đi thi là lời chúc Việt bình thường, chỉ sáo khi làm câu kết mọi bài) |
| N14 | Mở video kiểu YouTube dịch: "Xin chào các bạn, hôm nay mình muốn chia sẻ…", "Trong video này, tôi sẽ…", "đừng quên like, share và đăng ký" | TikTok, Reels Việt vào cảnh ngay giây đầu; lời chào chỉ hợp livestream | Câu đầu là cảnh hoặc câu nói thẳng vào người xem | "Xin chào các bạn, hôm nay mình sẽ hướng dẫn cách rửa máy lạnh." → "Máy lạnh chạy cả đêm mà không mát? Khoan gọi thợ, coi cái này đã." | Judge (video ngắn: sửa ở 3 giây đầu; video dài, live: được một lần) |
| N15 | CTA dịch: "Bạn đã sẵn sàng… chưa?", "Đừng bỏ lỡ", "Hành động ngay hôm nay", "Hãy để lại bình luận" (Are you ready? / Don't miss out) | Lời giục kiểu Mỹ, sang tiếng Việt nghe như rao hàng | Ai cần thì làm gì, cụ thể và nhẹ (mục 5.1) | "Bạn đã sẵn sàng thay đổi chưa? Đăng ký ngay hôm nay!" → "Ai muốn vô lớp tháng này thì nhắn mình, lớp nhỏ thôi." | Lint (2 cụm); Judge ("Đừng bỏ lỡ" đã quen trong quảng cáo, nhưng lệch giọng coach) |

### 2.4 Xưng hô, tiểu từ, giọng tổng đài và trợ lý

| # | Mẫu | Vì sao cấn | Sửa | Ví dụ: sai → đúng | Mức |
|---|---|---|---|---|---|
| X1 | "Bạn" làm chủ ngữ câu nào cũng có (you) | Câu tiếng Anh phải có chủ ngữ; "bạn" còn sai vai khi người nghe lớn tuổi | Bỏ chủ ngữ; gọi đúng nhóm ("mấy bạn văn phòng", "anh chị phụ huynh"); "ai", "người ta" | "Bạn có thấy mệt không? Bạn có biết bạn đang chạy sai không?" → "Mệt chưa? Chạy kiểu đó ba bữa là gối nó khóc đó." (Nam) | Đếm (>3/100 chữ hoặc 3 câu liền mở bằng "Bạn"); sai cặp xưng hô: Judge |
| X2 | "của bạn" gắn vào mọi danh từ (your) | Tiếng Việt bỏ khi đã rõ, hoặc dùng "mình" | "nhà mình", "tiệm mình", hoặc bỏ | "Hãy kiểm tra máy lạnh của bạn trước khi gọi thợ của bạn." → "Khoan gọi thợ, coi lại cái máy nhà mình cái đã." | Đếm (bài dưới 150 chữ: ≥2 lần) |
| X3 | Thiếu tiểu từ cuối câu | Câu trần đọc lên như thông báo; nhắn người lớn hơn mà thiếu "Dạ… ạ" là cộc | Thêm ở chỗ dặn, rủ, làm thân (mục 4.7) | "Em đã nhận được ảnh. Em sẽ gửi báo giá vào thứ Bảy." → "Dạ em nhận ảnh rồi ạ, sáng thứ Bảy em gửi báo giá anh nha." (Nam) | Đếm (so với bài thật của chính coach) |
| X4 | Rắc tiểu từ đều mọi câu; tiểu từ sai vùng | Nghe như diễn, như giễu nhại giọng vùng | Một vùng một bài; không ba câu liền cùng một chữ | "Bạn đăng ký nha. Khóa học hay nha. Giá rẻ nha." → "Lớp 8 buổi, 1.890.000đ. Ai cần thì nhắn mình nha." | Judge |
| X5 | "Chúng ta" trong bài bán; "chúng tôi" của người làm một mình; "Tại [Tên], chúng tôi tin rằng…" (We all know / At X, we believe) | Nghe như diễn văn, như công ty | Đúng cặp của coach; "bên mình, tụi em, bọn mình, chị em mình, nhà mình" | "Tại tiệm Trâm, chúng tôi tin rằng mỗi bộ móng đều xứng đáng được chăm chút." → "Tiệm em sơn xong là chụp cho chị coi, chưa ưng thì làm lại." (Nam) | Lint ("chúng tôi tin rằng", "chúng ta đều biết"); Judge |
| X6 | "anh ấy / cô ấy nói rằng…" và lời kể gián tiếp (he / she said that) | Lời kể Việt gọi theo vai và tên, trích nguyên câu | "anh chủ quán", "em Vy", Nam: "ảnh, chỉ, ổng, bả"; dẫn bằng "bảo / nói:" | "Cô ấy nói rằng cô ấy không biết bắt đầu từ đâu." → "Em ấy nhắn: 'Chị ơi em không biết bắt đầu từ đâu luôn.'" | Đếm (giọng Nam, Trung: ≥2 lần); "chia sẻ rằng": Lint ("anh ấy" trong giọng Bắc là tự nhiên) |
| X7 | Giọng tổng đài: "Cảm ơn bạn đã liên hệ / đã quan tâm đến dịch vụ", "Rất vui được hỗ trợ", "Đừng ngần ngại liên hệ", "Nếu bạn có bất kỳ câu hỏi nào", "trong thời gian sớm nhất", "Xin lỗi vì sự bất tiện này", "Vui lòng để lại số điện thoại", "Chúng tôi luôn lắng nghe và tiếp thu" | Dịch email CSKH tiếng Anh; là khuôn mẫu tin hàng loạt | Mở "Dạ" + tên, vào việc ngay, hẹn một bước cụ thể, kết "ạ / nghe / nha / nhé" | "Cảm ơn bạn đã liên hệ! Nhân viên sẽ phản hồi trong thời gian sớm nhất." → "Dạ chị, sơn gel bên em 150k nha. Chị tính ghé bữa nào để em xếp thợ?" (Nam) | Lint |
| X8 | Văn công văn: "Kính gửi", "Quý khách", "Quý phụ huynh", "Kính đề nghị", "Trân trọng" trên mạng xã hội và Zalo | Tiếng Việt chuẩn của công văn, nhưng trên Facebook, Zalo một-một thì như tờ rơi | Gọi tên, "anh chị", "phụ huynh" | "Kính đề nghị Quý phụ huynh nhắc nhở các em mang đầy đủ dụng cụ." → "Anh chị cho con mang kính bơi giúp thầy nghe." (Trung) | Judge (email trang trọng với doanh nghiệp thì "Kính gửi" vẫn đúng) |
| X9 | Giọng trợ lý dịch khi máy nói với coach: "Chắc chắn rồi!", "Tuyệt vời!", "Câu hỏi hay!", "Dưới đây là…", "Hy vọng điều này hữu ích", "Bạn có muốn tôi…?", nhãn "Lưu ý:", "Kết luận:" | Dịch "Sure! / Great question! / Here are… / Hope this helps / Would you like me to…" | "Được chị.", "5 bản đây chị:", "Có cần em làm thêm bản TikTok không ạ?" | "Chắc chắn rồi! Dưới đây là 5 mẫu caption tuyệt vời dành cho bạn:" → "Em viết 5 bản, chị chọn nha:" | Lint ("Câu hỏi hay!", "Dưới đây là", "Kết luận:"); Judge |
| X10 | "anh/chị" có gạch chéo trong tin gửi một người | Dấu hiệu tin mẫu gửi hàng loạt | Nhìn tên, ảnh, cách họ viết mà chọn "anh" hoặc "chị" | "Chào anh/chị, cảm ơn anh/chị đã quan tâm." → "Dạ chào chị Hoa," | Judge (chuỗi chữ trong repo dùng `[anh/chị]` làm chỗ trống, không phải lỗi) |

### 2.5 Trình bày, dấu câu, con số

| # | Mẫu | Vì sao cấn | Sửa | Ví dụ: sai → đúng | Mức |
|---|---|---|---|---|---|
| P1 | Markdown trong bài mạng xã hội: `**in đậm**`, `###`, dòng "Nhãn: nội dung" | Facebook, Zalo, TikTok hiện nguyên dấu sao; bài người thật không chia đề mục như báo cáo | Xuống dòng thường, câu nói | "**Bước 1: Chọn hoa**" → "Trước hết phải chọn hoa còn búp đã." | Judge; chạy lúc runtime: bài Facebook, Zalo, TikTok có `**` là trượt |
| P2 | Chữ in đậm Unicode (𝐁𝐎𝐋𝐃) | Vỡ dấu tiếng Việt | Bỏ | | Judge |
| P3 | Emoji đầu dòng kiểu AI: 🚀 💡 ✨ 🎯 🌟 mỗi dòng một cái | Mùi bài bán hàng loạt; người Việt viết tay dùng :)) =)) hihi 😅 ❤️ ở chỗ có cảm xúc | Chỉ emoji coach dùng, đặt ở chỗ có cảm xúc | "🚀 Ảnh đẹp ✨ Bán chạy 💡 Bứt phá" → "Ảnh đẹp mà sai màu thì khách cũng trả hàng thôi 😅" | Judge (coach không dùng emoji: không thêm cái nào) |
| P4 | Gạch dài (—), chấm phẩy (;), dấu phẩy trước "và" ở mục cuối | Bàn phím điện thoại Việt không có sẵn "—"; chấm phẩy hiếm trên mạng; tiếng Việt không có Oxford comma | Dấu phẩy, hai chấm, "...", xuống dòng | "Mang kính bơi, khăn tắm, và dép — thiếu là không xuống nước." → "Mang kính bơi, khăn tắm, dép nghe... thiếu cái nào là con ngồi trên bờ." (Trung) | Judge |
| P5 | Viết Hoa Mọi Chữ Trong Tiêu Đề (Title Case) | Chính tả Việt chỉ hoa chữ đầu câu và tên riêng | Viết thường | "5 Bí Quyết Giữ Hoa Tươi Lâu" → "5 cách chị giữ hoa tươi được năm ngày" | Judge (VIẾT HOA CẢ CÂU để gây chú ý "CHỊ EM ƠI" là thói quen Việt thật, khác lỗi này) |
| P6 | Số, tiền, ngày giờ kiểu Anh: $199, 4,990,000 VND, 2.5 triệu, 8:00 PM, October 15, 6M | Việt dùng chấm ngăn nghìn, phẩy thập phân, ngày dd/mm | 4.990.000đ · 1,99tr · 99k · 2,5 triệu · 20h / 8 giờ tối · 15/10 · trong lời nói "hai triệu rưỡi", "mười lăm nghìn" | "Khóa học chỉ $199, khai giảng October 15 lúc 8:00 PM." → "Khóa 4.990.000đ, khai giảng tối 15/10, 8 giờ." | Judge (runtime check); Gen Z viết "8pm" thì là giọng của họ |
| P7 | Hashtag tiếng Anh chung chung, có dấu | Không ai tìm | 1–3 hashtag không dấu, đúng ngách (#quanan #catmayhoa) | "#marketing #success #motivation" → "#quanan #quayvideo" | Judge |

### 2.6 Đếm mật độ: những gì từng lần không sai

Các mẫu mức **Đếm** chỉ sai khi dày. Ngưỡng cho grader và giám khảo ở mục 9.3. Lý do không đưa vào lint: "bạn", "của bạn", "việc", "sự", "rất", "hãy", "rằng", "đã", "sẽ", "một", "những" đều có cách dùng tự nhiên; chặn từng chữ sẽ chặn cả tiếng Việt thật.

### 2.7 Đừng sửa quá tay: trông như văn dịch mà là tiếng Việt thật

Khi chạy các mẫu trên kho lời nói của 6 nhân vật eval, những chỗ dưới đây trông giống văn dịch nhưng là cách nói thật. Lint phải nhắm vào **dạng dịch**, không nhắm vào **chữ**; người sửa cũng vậy. Ví dụ ở cột giữa là câu mới viết, cùng kiểu với câu trong kho.

| Trông giống | Nhưng là tiếng Việt thật | Ghi chú |
|---|---|---|
| "nó" (C14) | "Cái máy nó kêu rè rè." "Cái gối nó cao quá nên cổ mới mỏi." "Cái cây nó héo là tại nó thiếu nước." | "Nó" đứng **sau** một danh từ cụ thể là đặc trưng lời nói (kho lời nói: 92 lần). Bỏ hết thì câu lại thành văn viết |
| "cái mà… là…" (C8) | "Cái mà chị sợ nhất hồi mới mở tiệm là khách chê màu." | Chỉ "điều mà… là…" mới là câu chẻ dịch |
| "Không phải X, mà Y" (N3) | "Không phải hoa dở, mà cắm sai giờ." | Một lần trong bài là bình thường; lặp mỗi đoạn mới là khung dịch |
| "bằng cách" (C11) | "Hồi đó tiệm kiếm khách bằng cách phát tờ rơi ở chợ." | Khi kể việc đã làm thì tự nhiên |
| "anh ấy" (X6) | "Anh ấy gọi lại cho chị lúc nửa đêm." (Bắc) | Giọng Bắc dùng "anh ấy, chị ấy" tự nhiên; giọng Nam nói "ảnh, chỉ" |
| "được" (C4) | "Uống thuốc được mấy hôm là lại đâu vào đấy." "Con bơi được rồi nè." | "Được" nghĩa là làm được, có được, kéo dài được là tiếng Việt gốc |
| "là" nhấn (C6) | "Mệt là mệt thiệt." "Cái máy là cũ lắm rồi." | Dạng dịch là "là rất / là vô cùng / là hoàn toàn + tính từ" |
| "Tóm lại là", "Nói chung là" giữa lời kể (N13) | "Tóm lại là tháng đó lỗ, mà học được nhiều." | Chỉ "Tóm lại," đầu đoạn kết là văn mẫu; lint giờ chỉ bắt dạng đó |
| "chìa khóa" nghĩa đen (T4) | "Mẹ đưa chị cái chìa khóa xe máy." "Chìa khóa để trên bàn đó em." | Chỉ nghĩa bóng ("chìa khóa thành công", "là chìa khóa để…") mới sáo; lint giờ chỉ bắt nghĩa bóng |
| "có thể nói" nghĩa đen | "Chuyện giày chạy thì mình có thể nói tới sáng." | Chỉ "Có thể nói," mở câu kiểu nghị luận mới sáo; lint giờ chỉ bắt dạng đó |
| "là" dẫn ý + "rất" (C6) | "Khách khen là rất ngon." "Ai cũng bảo là rất dễ, làm mới biết." | Sau thấy, nói, bảo, khen, tưởng thì "là" nghĩa là "rằng", không phải "is"; lint bỏ qua |
| "không những… mà còn" (N2) | "Con không những bơi được mà còn dám xuống nước một mình." | Cặp quan hệ từ Việt có sẵn; chỉ "không chỉ… mà còn" lặp làm khung mới là mùi AI |
| "chợt nhận ra" (N6) | "Đang chạy thì chợt nhận ra quên khóa cửa." | Chữ Việt thường; chỉ "chợt nhận ra rằng / một điều" làm chỗ ngoặt chuyện mới là văn AI |
| "Chúc… thành công" (N13) | "Mai khai trương hả chị? Chúc anh chị thành công nha!" | Lời chúc thật trước một việc thật; chỉ "Chúc bạn thành công trên hành trình…" cuối mọi bài mới sáo |
| "hành trang" nghĩa đen (T4) | "Hành trang đi biển của con: kính bơi, phao tay." | Chỉ "hành trang vững chắc / vào đời" mới sáo |
| "một cách" khi là danh từ | "Có một cách đơn giản để biết hoa còn tươi." "Nói một cách dễ hiểu là vầy." | Dạng dịch là "một cách + tính từ" làm trạng từ sau động từ |
| Chữ nghề của chính coach | "tối ưu ảnh", "chạy ads", "feedback", "content" | Coach thật sự nói thì giữ (code_mix) |
| "Đây là…" khi chỉ vào vật | "Đây là cái lưới lọc sau hai tháng không rửa." | Trong video thì tự nhiên |
| "phá băng" | Trò phá băng đầu buổi | Đã thành chữ quen; chỉ "phá vỡ băng" mới là dịch |
| Rào đón, câu mở "nói thật" | "Nói thật nghe anh chị", "Nói thiệt nha", "Chị nói thật nhé" | Là giọng, là cách giữ lòng nhau. Đừng cắt khi đó là câu mở của chính coach |
| Viết tắt, mặt cười khi nhắn người quen | "c xem rồi nhé", "ko", "dc", ":))" | Chỉ dùng khi coach dùng, với người đã quen, không trong tin đầu với khách mới |
| "Dạ", "ạ" | "Dạ em gửi rồi ạ." | Không phải khách sáo; thiếu mới là thô (với người lớn hơn, với khách) |
| Lặp chữ | "khách… khách… khách", "đăng, đăng, đăng ầm ầm" | AI được dạy "tránh lặp từ" nên đổi chữ liên tục ("khách hàng / người mua / đối tượng"). Người Việt kể thì cứ một chữ gọi một người suốt bài |

**Hệ quả cho danh sách cắt (wf6 V4 từ đệm, V6 đuôi xin xác nhận):** giữ nguyên "nói chung là", "thật ra là", "đúng không ạ" khi chúng nằm trong câu cửa miệng hay cách mở của chính coach (Voice Card `phrases`, `openers_closers`). Chỉ cắt khi máy tự thêm vào.

---

## 3. Nối chuyện: mở, nối, ngoặt, rút ý, kết

Regex chỉ bắt được chữ và khung câu. Cái làm bài AI "cấn" nhiều nhất là **cách nối**: câu này sang câu kia, cảnh này sang cảnh kia, chuyện sang lời mời. Đây là phần hướng dẫn cho bước viết; chấm ở `vn-naturalness.md` mục VN3.

### 3.1 Chuỗi bốn nhịp: cảnh → chuyện xảy ra → mình nhận ra → bạn thì sao

Đây là chuỗi mặc định cho bài kể, video kể, cả tin nhắn dài. Anchor cho máy dùng đúng bốn chữ này.

| Nhịp | Làm gì | Chữ hay dùng | Tránh |
|---|---|---|---|
| **1. Cảnh** | Mốc thời gian gần và cụ thể, chỗ, một người, một đồ vật nhìn thấy được. Câu đầu hoặc câu hai | "Tối qua gần mười một giờ", "Hè ni", "Hồi mới mở tiệm, có bữa", "Sáng thứ Bảy", "cái túi", "cái lưới lọc" | "Vào một ngày nọ", "Trong cuộc sống", "Bạn có biết", câu luận điểm |
| **2. Chuyện xảy ra** | Việc nối việc, có câu người ta nói **nguyên văn** | "rồi", "xong", "xong rồi", "đang… thì…", "tự nhiên", "có bữa"; dẫn lời "bảo / nói / kêu / nhắn: '…'" | "Sau đó," mở mọi câu, "Tiếp theo,", "chia sẻ rằng", "anh ấy nói rằng" |
| **3. Mình nhận ra** | Ngoặt bằng một việc làm hoặc đồ vật, rồi chữ "mới / hóa ra / thế mà / ai dè". Bài học là một câu ngắn hai vế, hoặc nằm trong miệng người khác | "Lúc đó mình mới biết", "Hóa ra", "Thế mà", "Ai dè", "Phải đến… thì… mới…", "chứ có… đâu" | "Đó là lúc tôi nhận ra", "Khoảnh khắc ấy", "chợt nhận ra", "Bài học rút ra là" |
| **4. Bạn thì sao** | Quay sang **một** người đọc: một việc nhỏ làm được ngay, hoặc một câu hỏi thật, hẹp | "Ai đang… thì…", "Tối nay thử…", "Rồi kể mình nghe nha", "Có ai bị y vậy không hay mỗi mình?" | "Hy vọng bài viết hữu ích", "Bạn nghĩ sao?", "Đừng quên like, share" |

**Ví dụ đủ bốn nhịp (Hiếu, thợ máy lạnh, Đà Nẵng, xưng Hiếu – anh chị):**

> Hè ni có ông chú bên Sơn Trà gọi Hiếu, nói máy lạnh chạy cả đêm mà không mát, chắc hư rồi, thay cái mới cho chú. *(cảnh)*
> Hiếu tới, tháo cái lưới lọc ra, bụi đóng dày như miếng bánh tráng. Rửa xong, bật lên, mười phút là mát rượi. Chú cười, nói: "Rứa mà chú tính bỏ gần chục triệu mua cái mới." *(chuyện xảy ra, có lời nguyên văn)*
> Nhiều cái máy không hư chi hết, nó chỉ bị nghẹt thôi. *(mình nhận ra: đề–thuyết + "nó")*
> Hai tháng anh chị tự tháo lưới ra rửa một lần, có năm phút thôi à. *(bạn thì sao: một việc nhỏ)*

**Khung sáu bước** (chi tiết hơn, cho bài Facebook "chia sẻ thật" 120–250 chữ):
1. Mốc thời gian và chỗ ở câu đầu hoặc câu hai.
2. Một chi tiết nhìn thấy được (đồ vật, cử chỉ, con số).
3. Câu người ta nói, trích nguyên văn.
4. Nối bằng chữ ngắn: rồi, xong, từ bữa đó, thế là.
5. Bài học nói bằng câu cửa miệng của coach, một câu.
6. Rủ một việc nhỏ, đúng người: "Ai đang… thì…".

### 3.2 Chữ nối: tiếng Anh → AI dịch → người Việt nói

| Tiếng Anh | AI hay dịch | Người Việt nói (chọn theo giọng coach) |
|---|---|---|
| Then / After that | Sau đó, · Tiếp theo, | Rồi · Xong · Xong rồi · Được mấy bữa thì |
| However / But | Tuy nhiên, | Mà · Nhưng mà · Có điều · Khổ cái là · Khổ nỗi |
| So / Therefore / As a result | Do đó, · Vì vậy, · Kết quả là | Thế là (Bắc) · Vậy là · Nên · Thế nên · Thành ra (Nam) · Rứa là (Trung) |
| Because | Bởi vì · Bởi lẽ | Vì · Tại · Tại vì · Do |
| Even though | Mặc dù… nhưng… | Dù… · … mà vẫn … · … vậy mà … |
| Moreover / In addition | Hơn nữa, · Ngoài ra, · Bên cạnh đó, · Thêm vào đó, | Với lại · Mà còn · Chưa kể · Còn nữa · Đã thế lại còn (Bắc) |
| Meanwhile / While | Trong khi đó · trong khi | Còn · Mà |
| Suddenly | Đột nhiên | Tự nhiên · Đang… thì… · Đùng một cái |
| One day | Một ngày nọ · Vào một buổi chiều | Có bữa (Nam, Trung) · Có hôm (Bắc) · Hôm đó · Tối đó |
| At first | Ban đầu | Mới đầu · Lúc đầu · Hồi đầu |
| Little did I know | Tôi đâu biết rằng | Ai dè · Nào ngờ · Đâu có ngờ |
| It turned out | Hóa ra là | Hóa ra (giữ; đây là chữ Việt) |
| That's when I realized | Đó là lúc tôi nhận ra rằng | Lúc đó mới vỡ lẽ · Tới lúc đó mới hiểu · Lúc đó mình mới biết |
| Fast forward 3 years | Tua nhanh 3 năm sau | Ba năm sau · Tới giờ |
| Since then | Kể từ đó | Từ hồi đó · Từ đấy (Bắc) · Từ bữa đó (Nam, Trung) |
| To this day | Cho đến ngày nay | Tới giờ · Tới chừ (Trung) · Giờ vẫn nhớ hoài |
| Eventually / In the end | Cuối cùng, | Rốt cuộc · Mãi sau mới · Cuối cùng thì |
| Honestly | Thành thật mà nói | Nói thật · Nói thiệt (Nam) · Nói thật nghe (Trung) · Nói thật nhé (Bắc) |
| In other words | Nói cách khác · Điều này có nghĩa là | Tức là · Nghĩa là · Kiểu là · Nói nôm na là |
| Anyway | Dù sao đi nữa | Thôi · Nói chung là · Đại khái là |
| The thing is | Vấn đề là · Điều quan trọng là | Cái là · Có điều · Khổ nỗi |
| First, second, finally | Đầu tiên, thứ hai, cuối cùng | Một là, hai là, ba là · Cái thứ nhất… còn nữa… |
| No wonder | Không có gì ngạc nhiên khi | Thảo nào · Bảo sao (Bắc) · Hèn chi · Hèn gì (Nam) |
| You know what? | Bạn biết không? | Biết sao không? · Mà biết gì không |
| In the case that | Trong trường hợp… | Lỡ… thì… · Mà… thì… |
| Looking back | Nhìn lại, | Giờ nghĩ lại · Bây giờ nhớ lại |
| I learned that | Tôi đã học được rằng | Từ bữa đó mình biết · Sau vụ đó mình mới hiểu |
| That made me | Điều đó khiến tôi | Nghe xong mình… · Đọc tới đó mình… |

"Sau đó" tự nó không sai, lời nói vẫn dùng ("sau đó mình mới gọi lại"); cấn là khi "Sau đó," mở câu nào cũng có trong một chuỗi việc.

### 3.3 Chữ nối theo chức năng và vùng

Cột "Chung" dùng được cả nước. Cột vùng chỉ dùng khi coach đúng vùng đó. Cột cuối là chữ văn viết hoặc văn dịch: **không dùng trong bài kể, video, tin nhắn.** Bảng này là phán đoán người bản ngữ; cần người mỗi vùng duyệt.

| Chức năng | Chung | Bắc | Nam | Trung | Không dùng khi kể |
|---|---|---|---|---|---|
| Rồi tiếp theo | rồi, xong, xong rồi, sau đó | thế là, xong thì | rồi vậy là, xong cái | rồi rứa là | tiếp theo đó, kế đến, sau khi… thì |
| Nguyên nhân | vì, tại, tại vì, do | tại, vì | tại, tại vì | tại | bởi lẽ, bởi vì lý do, nguyên nhân là do |
| Kết quả | nên, nên là, vậy là | thế nên, thế là | thành ra, vậy nên | rứa nên | do đó, vì vậy, chính vì thế, kết quả là |
| Ngoặt | mà, nhưng mà, có điều, khổ nỗi | thế mà, cơ mà (trẻ), được cái… mỗi tội… | vậy mà, mà hổng ngờ, ai dè | rứa mà | tuy nhiên, mặc dù vậy, trái lại, ấy vậy mà (văn báo, dùng thưa) |
| Thêm ý | với lại, còn nữa, chưa kể | đã thế lại còn, lại còn | rồi còn, với lại còn | | bên cạnh đó, ngoài ra, thêm vào đó, không chỉ… mà còn |
| Giải thích lại | tức là, nghĩa là, kiểu, kiểu như, ý là | tức là | kiểu, kiểu như là | nghĩa là | nói cách khác, điều này có nghĩa là |
| Điều kiện | … thì …, nếu … thì, lỡ … thì, mà … thì | | lỡ mà… | | trong trường hợp, giả sử rằng |
| Phủ định để nhấn | chứ không phải, đâu phải, có phải… đâu | chứ có… đâu, chả phải | hổng phải… đâu, đâu có | không phải… mô | không phải là… mà là… (một lần thôi) |
| Quay lại sau khi lạc đề | à mà, quay lại chuyện…, thôi chuyện đó để sau | nãy nói đến đâu nhỉ | nãy nói tới đâu rồi ta | | quay trở lại vấn đề chính |
| Gom lại khi nói | nói chung là, đại khái là, thế thôi, vậy thôi | thế thôi, chung quy là | vậy thôi á, đơn giản vậy thôi | rứa thôi | tóm lại, nhìn chung, có thể nói |
| Nhấn đúng | đúng một câu, đúng một chỗ, có mỗi, y như | y hệt, đến giờ vẫn | y chang, tới giờ | tới chừ | duy nhất, hoàn toàn, tuyệt đối |

**Ghi chú dùng:**
- **"thì"** là chữ nối số một của lời nói: tách đề với thuyết ("Shop nhỏ thì…"), nối điều kiện, mở câu khi kể ("Thì hôm đó…"). Lời nói có hai, ba chữ "thì" một câu là bình thường; bài viết bớt còn một.
- **"mà"** vừa là "nhưng", vừa nối lý do ("mà ai dạy đâu"), vừa nhấn cuối câu ("có ai cười đâu mà ngại"). Viết "nhưng" mãi nghe cứng.
- **"rồi… rồi… rồi…"** liệt kê việc liên tiếp một hơi, chỉ cách bằng dấu phẩy: "rồi thuê thêm thợ, rồi mở thêm ca tối, rồi in tờ rơi, nói chung là tiệm đông hẳn". AI chặt mỗi việc thành một câu có "Sau đó,".
- **"xong"** là "and then" thật của người Việt: "Xong cuối tháng ngồi tính lại…". Video và tin nhắn dùng thoải mái; bài viết 1–2 lần.
- **"thế là / vậy là"** báo hệ quả, hay mở câu kết một đoạn chuyện: "Thế là từ hôm đấy…".
- **"chứ"** gắn phủ định với khẳng định: "Học được câu chứ có nói được đâu." Đây là cách nói bài học rất Việt.
- **"ấy vậy mà", "cơ mà":** kho lời nói 0 lần. "Ấy vậy mà" là chữ văn báo, AI dùng như công tắc "plot twist": tối đa một lần trong bài dài, không dùng trong video. "Cơ mà" là giọng Bắc trẻ, hơi đùa; hợp coach Bắc dưới 35.

### 3.4 Đề–thuyết: đưa "cái đang nói" lên đầu

Ranh giới đề và thuyết đánh dấu bằng "thì, là, mà" (Cao Xuân Hạo; xem ngonngu.net và Tạp chí ĐHSP TP.HCM ở mục 10.6).

| Câu chủ–vị kiểu dịch | Câu đề–thuyết kiểu nói |
|---|---|
| "Việc bánh nở đẹp không có nghĩa là bánh ngon." | "Bánh nở đẹp *là* một chuyện, ăn ngon *là* chuyện khác." |
| "Máy lạnh của bạn không bị hỏng." | "Cái máy *nó* có hư chi đâu." (Trung) |
| "Tôi đã ngừng nhận lớp buổi trưa từ lâu." | "Lớp buổi trưa á, chị bỏ lâu rồi." |
| "Doanh thu chỉ để trình diễn, lợi nhuận mới để chi tiêu." | "Doanh thu *là* để khoe, tiền lời *mới là* tiền bỏ túi." |
| "Người mới thường bỏ cuộc trong tuần đầu tiên." | "Người mới *mà* bỏ *thì* bỏ từ tuần đầu rồi." |

Ba công cụ lời nói hay dùng:
- **"cái" + danh từ** để chỉ cụ thể: "cái sổ", "cái câu đó", "cái lưới lọc" (kho lời nói: 508 lần).
- **"nó" lặp lại sau đề:** "Cái máy nó…", "cái tiền nó chảy đi…" (92 lần). AI gần như không làm vậy.
- **"á / ấy / thì" sau đề:** "Cái phòng làm kho ấy, …", "Lớp buổi trưa á, …", "Còn chuyện giá thì…".

### 3.5 Mở chuyện: bảy kiểu người Việt hay mở

**A. Mốc thời gian + chỗ + người (mở bằng cảnh).** Phổ biến nhất trên Facebook "chia sẻ thật" và video kể.
- "Tối qua gần mười một giờ, có em nhắn mình…" · "Sáng thứ Bảy, đang ngồi cà phê thì…" · "Hồi mới ra trường, có bữa…" (Nam) / "…có hôm…" (Bắc) / "…có bữa ni…" (Trung) · "Tết năm ngoái…" · "28 Tết…"
- Mốc nên gần và cụ thể. Không "Vào một ngày nọ" (giọng cổ tích, văn mẫu).

**B. Mở bằng người.** "Có một cô bán bún đầu chợ…", "Có ông chú bên Sơn Trà…", "Hôm qua có em sinh viên hỏi…". Gọi bằng chữ họ hàng và một nét đời; không "một người phụ nữ", "một khách hàng".

**C. Mở bằng câu khách nói, nguyên văn.** Mạnh cả trong bài lẫn video.
- "'Anh ơi em chạy ba bữa là đau gối, chắc em hông hợp chạy bộ.' Tin nhắn hồi tối."
- Câu khách phải là chữ khách thật dùng; không chuốt cho hay.

**D. Thú nhận.** Người Việt tin người tự nhận mình từng sai.
- "Nói thật là năm đầu chị cũng làm y như vậy." · "Kể cái chuyện quê nhất của mình năm đó." · "Mình dạy cái này sáu năm rồi mà tuần trước vẫn dính."

**E. Câu chốt đứng riêng dòng đầu,** rồi mới kể, cuối bài nhắc lại bằng chữ khác. Câu phải ngắn, hai vế, nghe như tục ngữ nhà làm, không như khẩu hiệu ("Thành công bắt đầu từ…").
- "Rẻ lúc học, đắt lúc đền." → chuyện → nhắc lại.

**F. Gọi đúng nhóm người, hỏi đúng tình huống.**
- "Mấy bạn văn phòng ơi, 3 giờ chiều rồi đó, mắt cay chưa?" (Nam) · "Bố mẹ nào sắp cho con đi biển thì đọc cái này nhé." (Bắc) · "Anh chị nào tính mở quán trước Tết thì nghe tôi nói cái ni đã." (Trung; gọi "anh chị" thì xưng "tôi", không xưng "anh")

**G. Con số trần, không trang trí.** "Bốn chục dĩa, chưa tới tám giờ." "Năm phút rửa lưới, ba năm đỡ tốn tiền thợ." Số phải thật, của coach (§CM-GUARDRAILS); số bịa là rủi ro pháp lý.

**Theo nền tảng:**
- **TikTok, Reels:** 3 giây đầu là một câu nói thẳng vào mặt người xem, giọng nói chứ không giọng đọc: "Khoan, đừng mua giày vội." "Bỏ điện thoại xuống năm giây đã." Kiểu C và F chạy tốt nhất; kiểu A được khi câu đầu có xung đột ngay ("Có cô dâu gọi em lúc 5 giờ sáng, khóc vì gãy móng").
- **Livestream:** chào và chờ người vào, thật, lộn xộn, có tên người: "Rồi, chào cả nhà, mọi người vô từ từ nha." "Chị Lan vô rồi nè, chào chị Lan." Câu kể đầu tiên hay bắt từ một bình luận: "Có bạn hỏi là…".
- **Zalo, inbox:** dòng đầu là gọi tên + xưng mình là ai + lý do nhắn: "Dạ chị, em Quân đây ạ." "Chào em, anh Phong đây." Không "Kính gửi Quý khách", không "Xin chào bạn, mình là X đến từ Y".

**Câu mở cần tránh:** "Bạn đã bao giờ…", "Đã bao giờ bạn…", "Hãy tưởng tượng…", "Hôm nay mình muốn chia sẻ với các bạn về…", "Trong cuộc sống, ai cũng từng…", "Câu chuyện dưới đây sẽ…", "Có một sự thật là…", "Xin chào các bạn, mình là… và hôm nay…" (chậm trên TikTok; được trên YouTube dài).

### 3.6 Câu hỏi người thật hỏi, khác câu hỏi AI

| Câu hỏi AI | Câu hỏi người thật |
|---|---|
| "Bạn đã sẵn sàng thay đổi cuộc sống chưa?" | "Một tuần nấu cho con được mấy bữa sáng?" |
| "Bạn có bao giờ cảm thấy mất động lực?" | "Có ai giống mình không, mở laptop ra là muốn ngủ?" |
| "Điều gì đang ngăn cản bạn thành công?" | "Tháng trước cái lò nướng ngốn hết bao nhiêu tiền điện? Không nhớ à?" |
| "Bạn nghĩ sao về vấn đề này?" | "Mọi người có bị vậy không hay mỗi mình?" |
| "Bạn có muốn biết bí quyết?" | "Biết sao không?" (rồi trả lời liền) |

Câu hỏi thật thì **cụ thể, có số, có đồ vật, hỏi đúng một chuyện**, hay dùng "không, chưa, à, hả, hông". Câu hỏi tu từ chỉ dùng khi trả lời liền: "Tiệm nhỏ cần gì tính toán à? Tiệm càng nhỏ càng phải tính kỹ."

### 3.7 Chuyển ngoặt: báo cái "à, ra thế"

Người Việt báo ngoặt bằng **thứ tự thời gian + chữ "mới"**, không bằng tuyên bố "tôi nhận ra".

| Mẫu | Ví dụ | Ghi chú |
|---|---|---|
| Phải đến … thì … mới … | "Phải đến lần con sặc nước thì chị mới chịu cho con học bơi." | Mẫu ngoặt mạnh nhất |
| Lúc đấy / lúc đó … mới … | "Lúc đó mình mới biết là mình học thuộc câu chứ không học nói." | |
| Hóa ra … | "Hóa ra con không sợ nước, con sợ nước vô kính." | Hay đặt trong miệng khách |
| Thế mà / vậy mà / rứa mà | "Thế mà cầm mic lên, tay vẫn run." | Ngoặt ngược kỳ vọng |
| Ai dè … | "Ai dè bé bốc ăn ngon lành." | Bắc, Nam đều dùng |
| Đùng một cái / tự nhiên | "Đang bán ngon thì đùng một cái chợ dời đi chỗ khác." | |
| Xong cuối tháng ngồi tính lại thì … | "Xong cuối tháng ngồi tính lại, tiền công có 4 triệu." | Ngoặt bằng con số |
| Tới chừng (Nam) / đến lúc (Bắc) | "Tới chừng chạy chậm lại thì gối hết kêu." | |
| Câu cụt đứng một mình | "Mười phút." "Mỗi chị." "Run thật." | Ngoặt bằng nhịp; lặp lại một chữ của khách |

**Ngoặt bằng chi tiết, không bằng chữ cảm xúc.** Người thật kể *mình đã làm gì* lúc nhận ra: "mở lại từng tấm ảnh ra coi", "đọc tin đó ba lần", "ngồi ngoài hiên tới khuya, ly trà nguội ngắt", "gỡ tấm bảng giá xuống". AI kể *mình cảm thấy gì*: "Khoảnh khắc ấy, tôi chợt nhận ra…", "Một cảm giác bừng tỉnh…". Luật cho máy: **ở chỗ ngoặt có ít nhất một việc làm hoặc đồ vật cụ thể; không "khoảnh khắc ấy", "chợt nhận ra", "bừng tỉnh".**

### 3.8 Rút bài học mà không giảng đạo

Người Việt ghét bị "dạy đời" trên mạng, nhất là từ người bán khóa học. Coach đáng tin rút bài học theo sáu cách:

1. **Câu hai vế đối, ngắn như tục ngữ nhà làm.** "Rẻ lúc học, đắt lúc đền." "Chạy nhanh ba bữa, nằm nhà ba tuần." Mẫu: *X là để A, Y mới là để B* · *A thì B* · *A chứ không phải B* · *Càng A càng B* · *A một lần, B cả đời*.
2. **Đặt vào miệng người khác:** mẹ, ba, chồng, khách, thầy cũ. "Má dạy: tiền nào của nấy." "Má hỏi đúng một câu: 'Bán cả ngày vậy rồi con ăn gì?'" Người đọc tự rút ra; coach khỏi nói.
3. **Mình cũng từng sai:** "hồi mới làm mình cũng sai y vậy". Bài học như nói với chính mình, không chỉ tay vào người đọc.
4. **"Mình" gộp cả người nghe** thay cho "bạn phải": "Nhà mình đâu có ai tính tiền chợ bằng chữ 'chắc đủ'." (Không "chúng ta cần".)
5. **Thu nhỏ thành một việc làm thử:** "Tối nay lấy 10 tấm ảnh gần nhất ra coi lại màu." "Thử với một khách thôi."
6. **Nhại câu cãi rồi trả lời liền:** "Không có máy xịn à? Điện thoại cũ cũng quay được." "Bận quá à? Năm phút thôi mà." AI thì viết kiểu dịch "Bạn có thể nghĩ rằng… Nhưng thực tế…".

**Không dùng:** "Bài học rút ra là…", "Hãy luôn nhớ rằng…", "Thành công không đến từ…", "Đừng bao giờ từ bỏ…", "Mỗi chúng ta đều…", "Cuộc sống mà,…", "Hãy là phiên bản tốt hơn của chính mình", "Hạnh phúc là…".

### 3.9 Kết bài

| Kiểu kết | Ví dụ | Hợp với |
|---|---|---|
| "Ai đang … thì …" + việc nhỏ | "Ai đang nhét hóa đơn chung một túi thì tối nay chia ra theo tháng trước đã." | Bài Facebook, caption |
| Giao việc thử + mời kể lại | "Chiều nay làm thử, xong nhắn mình coi ra sao nha." | Video, bài |
| Mời nhắn, giọng thấp | "Ai đang ngại hỏi thì cứ nhắn riêng, chị trả lời từng người." | Bài có lời mời ngầm |
| Dừng cụt | "Thế thôi." / "Rứa thôi." / "Vậy thôi á." | Bài kể ngắn, câu chốt mạnh |
| Câu hỏi thật, hẹp | "Có ai bị y vậy không hay mỗi mình?" | Bài kéo bình luận (nhẹ tay; luật mồi tương tác của Meta, wf5 F8) |
| P/s cho lời mời | "P/s: Lớp tháng 11 còn 3 chỗ, ai cần thì nhắn mình." | Bài có bán, đặt lời mời xuống cuối |
| Livestream: trả lượt | "Còn ai hỏi gì nữa hông, chị đọc tiếp nè." | Live |
| Zalo: gỡ áp lực | "Em cứ coi lịch đã nha, chưa cần quyết liền đâu." / "Có gì anh nhắn tôi." | Tin một-một |

**Không dùng:** "Hy vọng bài viết hữu ích", "Cảm ơn bạn đã đọc đến đây", "Hãy để lại bình luận bên dưới", "Đừng quên like, share và theo dõi", "Chúc bạn thành công trên hành trình…". Lời mời comment từ khóa bật mặc định (DECISIONS); ngưỡng ("đủ 100 comment") và "chấm" là quyền của coach: máy viết y như coach chọn, thêm đúng một dòng lưu ý nền tảng có ngày, không chặn, không viết lại (§CM-CTA-KIT). Kiểu "comment 'có' nếu đồng ý" mà không kèm việc gì thì máy không tự đề xuất.

### 3.10 Giữ người nghe, trả lượt (video, live, tin nhắn)

- **Hỏi lửng giữa chuyện:** "Buồn cười không?", "Em biết không?", "Biết sao không?", "Thấy chưa?", "Đúng hông?", "phải hông mấy bạn".
- **Báo sắp vào ý chính:** "Rồi, giờ tới cái quan trọng nè." "Nghe nè." "Khoan, nghe cái này trước đã."
- **Đọc tên người bình luận (live):** "Chị Lan hỏi là…", "Bạn Minh nói đúng nè", "Ai ở Bình Dương vô rồi nè".
- **Xác nhận ngắn:** "Đó." "Thấy chưa." "Vậy đó." "Thế đấy."
- **Tin nhắn:** gửi lựa chọn nhẹ cho người kia: "anh xem có tiện không", "chị coi giúp em", "em đợi tin chị ạ", "chỗ nào chưa rõ chị nhắn em".
- **Tự sửa giữa chừng (chỉ video, live):** "à không, ba buổi chứ", "nói nhầm, mười lăm chứ không phải năm mươi". Để nguyên cho thật, nhưng không cố chèn.

### 3.11 Sáu khung kể kiểu Việt (cho máy chọn)

| Khung | Trình tự | Khi dùng |
|---|---|---|
| **K1. Cảnh – lời – chuyện – ngoặt – chốt – việc nhỏ** | Mốc giờ, chỗ → một người nói một câu nguyên văn → rồi / xong → thế mà / hóa ra / mới → câu chốt hai vế → "Ai đang… thì…" | Mặc định cho bài Facebook, video kể |
| **K2. Chốt trước** | Câu chốt một dòng → chuyện chứng minh → nhắc lại câu chốt bằng chữ khác → việc nhỏ | Coach có câu cửa miệng mạnh; caption ngắn |
| **K3. Hồi đó – bây giờ** | "Ngày xưa mình cũng…" → cái giá phải trả → "Bây giờ mình…" → một việc người đọc làm được | Bài niềm tin, bài kể vì sao làm nghề |
| **K4. Nhại câu cãi** | Câu khách hay cãi + "à?" → trả lời một câu → chuyện nhỏ chứng minh → việc thử | Gỡ phản đối, bài về giá |
| **K5. Hỏi đúng một câu** | Khách kể rối → mình hỏi đúng một câu → câu trả lời của khách → bài học | Bài chuyên môn, video tư vấn |
| **K6. Lạc đề rồi quay lại** | Đang kể → "À mà nói tới…" → một chi tiết bên lề → "Thôi quay lại…" | Chỉ live và video dài; không dùng trong bài viết |

**So với logic bài luận tiếng Anh** mà AI hay bê sang (luận điểm → "Đây là lý do" → Thứ nhất, Thứ hai, Thứ ba → Tóm lại): khung đó hợp carousel hướng dẫn hay LinkedIn liệt kê ("4 bước mình chụp một món hàng"), **không hợp bài kể, video nói, tin nhắn**. Ngay cả bài liệt kê, người Việt cũng mở bằng một chuyện hay một con số, và các ý viết bằng câu nói, không bằng danh từ trừu tượng.

### 3.12 Nhịp câu

**Dài ngắn xen nhau.**
- Câu kể dài một hơi, nối bằng dấu phẩy và "rồi, xong, mà": "Hồi mới chạy, mình ra công viên là chạy hết sức, chạy cho bằng người ta, xong ba bữa nằm nhà." Ghép nhiều mệnh đề bằng dấu phẩy là bình thường trong văn nói Việt.
- Câu cụt đứng riêng sau câu dài: "Run thật." "Mười phút." "Thế thôi."
- Bài Facebook 150–250 chữ: 1–2 câu cụt dưới 5 chữ, ít nhất một câu dài trên 25 chữ, còn lại lộn xộn. Không đoạn nào cũng 3 câu, không bài nào cũng 3 ý. AI hay viết câu nào cũng 15–20 chữ, đều như kẻ chỉ.

**Lặp để nhấn** (người Việt lặp nhiều, AI tránh lặp):
- Lặp chữ của khách: "Con bé bảo 'cả lớp có mỗi con chưa dám xuống nước'. Có mỗi con."
- Lặp ba lần giễu: "chụp, chụp, chụp, chụp ầm ầm".
- Lặp số: "Chạy nhanh ba bữa, nằm nhà ba tuần."
- "X ơi là X": "dài ơi là dài", "đông ơi là đông".
- Từ láy: nhỏ xíu, trống trơn, run run, lặt vặt, te tua, nắn nót. AI rất ít dùng; dùng đúng là văn có hồn hơn, miễn đừng nhồi.
- Nhấn bằng "đúng": "hỏi đúng một câu", "sai đúng một chỗ".
- Lặp chủ ngữ kiểu nói (Bắc): "Chị ngồi chị xé tờ giấy." Video, live thì được; bài viết một lần là đủ.
- **Một chữ gọi một người suốt bài.** Không đổi "khách hàng / người mua / đối tượng / họ" cho đỡ lặp.

**Dẫn lời.**
- Động từ dẫn: **bảo** (Bắc), **nói** (cả nước), **kêu** (Nam, nghĩa "bảo"), **nhắn**, **hỏi đúng một câu**, **than**. Không "chia sẻ rằng", "cho biết", "bày tỏ", "tâm sự rằng" ("tâm sự" người 40+ có dùng, nhưng không kèm "rằng").
- Hai chấm + ngoặc kép, không cần "rằng": Chị ấy bảo: "Em sợ cuối tháng lắm."
- Lời kể gián tiếp kiểu nói: "Chị ấy bảo là em ấy ngại lắm, cứ đọc giá cho khách là run." (có "là", giữ chữ của người nói).
- Báo đúng nguyên văn: "chị nhớ nguyên văn", "em ấy nói đúng câu này". Câu khách là vàng; đừng sửa cho đúng ngữ pháp.
- Tin nhắn trích lại thì giữ viết tắt, emoji của người gửi khi được phép: Khách nhắn: "c ơi e làm xong r nè 😭".

**Xuống dòng, dấu câu, số.**
- Facebook: dòng đầu đứng riêng. Bài ngắn một hai câu một dòng. Bài "chia sẻ thật" của người 40+ hay viết đoạn liền 3–5 câu; **đừng chặt mọi bài thành từng dòng một** (cũng là mùi "content thuê").
- "..." để bỏ lửng chỗ không muốn nói: "cuối tháng nhìn hóa đơn tiền điện thì... thôi khỏi nói."
- Mặt cười Việt: ":))", "=)))", "hihi", "huhu"; chỉ khi coach dùng.
- Không gạch dài "—" trong văn VN của coach: dùng phẩy, hai chấm, xuống dòng.
- Số trong video đọc bằng chữ ("mười lăm phút", "một tỷ hai"); bài viết: "15 phút", "1 tỷ 2", "40 triệu", "99k".

### 3.13 Mười thói quen làm câu nghe Việt

1. Chủ đề trước, rồi "thì / là / mà": "Hoa hồng thì cắt gốc trong nước."
2. Bỏ chủ ngữ khi đã rõ: "Mới 26 tuổi á." "Đứng dậy cái đã."
3. Lặp danh từ, hoặc "cái này / vụ đó / chuyện đó", thay cho "nó / điều này" chỉ ý.
4. Loại từ và "đó / ấy" sau danh từ: "cái máy", "cái tối đó", "con số", "tờ giấy".
5. "Nó" sau danh từ trong lời nói: "cái máy nó kêu", "cái tường nó ẩm".
6. Nhấn ở cuối câu: "mệt thiệt", "quan trọng lắm", "đau dữ lắm", "sợ ghê".
7. Tiểu từ đúng vùng, đúng người; "Dạ… ạ" với người lớn hơn. Liều theo bài thật của coach (có người 2/3 số câu có tiểu từ, có người chỉ 1/7).
8. Câu ngắn xen câu dài, có câu cụt.
9. Số nói như người ta đọc: "mười lăm phút", "hai chục năm", "hai triệu rưỡi", "gần nửa đêm".
10. Trích nguyên câu người ta nói, có cả "ơi", "ạ", lỗi gõ của tin nhắn: "con xin nghỉ nha chú".

### 3.14 Chữ cảm xúc: mộc hay sến

| Cảm xúc | Chữ người thật nói | Chữ sến, chữ AI | Cho thấy bằng chi tiết |
|---|---|---|---|
| Vui | sướng, mừng, vui ghê, mừng hết biết (Nam), sướng rơn | hạnh phúc vỡ òa, niềm vui vô bờ, lâng lâng hạnh phúc | "khao cả tiệm đi ăn lẩu" |
| Buồn | buồn, tủi, chán, nản, nghẹn, buồn thiu | trái tim tan vỡ, nỗi buồn sâu thẳm | "ngồi bệt dưới sàn", "tắt mic im một lúc" |
| Thương | thương, nghe mà thương, khổ thân (Bắc), tội ghê (Nam) | đồng cảm sâu sắc, thấu hiểu, trân quý | "vừa dỗ con vừa nói chuyện với chị" |
| Biết ơn | cảm ơn, quý lắm, nhớ hoài | biết ơn vũ trụ, lòng biết ơn sâu sắc | "giờ ghé tiệm còn mang ổi cho cả thợ" |
| Sợ, lo | sợ, lo, run, hú hồn, hết hồn, mất ngủ | nỗi sợ hãi bao trùm, lo âu tột độ | "đọc đi đọc lại tin nhắn" |
| Xấu hổ | ngại, quê (Nam), muối mặt (trẻ), ê mặt | cảm giác tự ti, tổn thương lòng tự trọng | "đứng hình đúng câu đầu" |
| Tức | tức, cay, bực, điên | phẫn nộ, bức xúc tột cùng | "đập tay xuống bàn" |
| Mệt | đuối, gồng không nổi, nản, kiệt | kiệt quệ về tinh thần | "ba tháng không về quê" |
| Nhẹ người | nhẹ cả người, thở phào, nhẹ re (Nam) | bình yên trong tâm hồn, được chữa lành | "cười, dúi cho bó rau" |
| Xúc động | rưng rưng (một lần), nổi da gà, nghẹn họng | xúc động nghẹn ngào, nước mắt lăn dài | "đứng trong nhà vệ sinh khóc mười phút" |

**Luật:**
1. Cảm xúc mạnh nhất kể bằng việc làm và đồ vật. Tính từ cảm xúc tối đa 1–2 chữ mỗi bài, và phải mộc.
2. Không chồng chữ: "rưng rưng, nghẹn ngào, vỡ òa" một đoạn là sến. Một chữ, đúng chỗ, hay đi với "cũng… theo", "nghe mà…": "Chị nghe mà cũng rưng rưng theo."
3. Chữ sến mặc định tránh (trừ khi coach tự dùng, lưu ở do_say): chữa lành, hành trình, thanh xuân, tổn thương (nghĩa tâm lý), năng lượng tích cực, phiên bản tốt hơn của chính mình, yêu thương bản thân, bình yên (làm danh từ trừu tượng), đánh thức, vỡ òa, trân quý, biết ơn vũ trụ, lan tỏa, truyền cảm hứng, giá trị, ý nghĩa cuộc sống, tỏa sáng. Trên mạng "chữa lành" còn bị chế giễu (Tuổi Trẻ, 2024).
4. Tự trào được tin hơn bi lụy. "Buồn cười không, con bà bán tạp hóa mà không biết tính lời" hay hơn "Tôi đã từng thất bại thảm hại".
5. Kể chuyện vui thì cân lại cho khỏi "nổ": thêm một câu thật về cái khó ("Nghề này không giàu nhanh được đâu, cực lắm").

### 3.15 Sáu bài mẫu có chú thích (hư cấu, mới viết)

**Bài Facebook "chia sẻ thật" · Bắc · 40+ · chị Vân, 47, Hải Phòng, làm sổ sách thuế cho hộ kinh doanh · mình – anh chị**

> Chiều qua có cô bán bún đầu chợ cầm cái túi nilon đựng hóa đơn sang nhờ mình xem. Cô bảo: "Cô sợ cái thuế này lắm, cứ có số lạ gọi là run." Mình ngồi xếp ra từng tờ, xong cộng lại. Hóa ra cô nộp thiếu có hơn ba trăm nghìn, chứ không phải mấy chục triệu như cô tưởng. Cô thở phào, còn dúi cho mình bó rau.
>
> Thuế không đáng sợ bằng cái túi hóa đơn không ai dám mở ra.
>
> Anh chị nào đang dồn hóa đơn một túi như cô thì tối nay cứ mở ra, xếp theo tháng đã.

Mở bằng giờ + người + đồ vật ("cái túi nilon") · lời nguyên văn ("số lạ gọi là run") · nối "xong" · ngoặt "Hóa ra… chứ không phải…" · cảm xúc bằng việc làm ("dúi cho bó rau") · câu chốt hai vế đứng riêng · kết "Anh chị nào… thì…" + "cứ… đã" (làm đúng một việc nhỏ này trước, chưa cần gì to).

**Kịch bản TikTok · Nam · 25–39 · Khang, 31, coach chạy bộ · mình – mấy bạn**

> Bữa trước có bạn nhắn mình: "Anh ơi em chạy được ba bữa là đau gối, chắc em hông hợp chạy bộ." Nói thiệt nha, hồi đầu mình cũng y chang vậy. Ra công viên là chạy hết sức, chạy cho bằng người ta, xong ba bữa nằm nhà. Tới chừng chạy chậm lại, chậm tới mức vừa chạy vừa nói chuyện được, thì gối hết kêu. Mấy bạn hông phải hông hợp đâu, mấy bạn chạy nhanh quá đó. Sáng mai thử chạy chậm hai chục phút thôi, đau nhói thì nghỉ, đi khám nha. Rồi kể mình nghe.

3 giây đầu là lời khách · thú nhận "Nói thiệt nha" · chuỗi việc một hơi, bỏ chủ ngữ · ngoặt Nam "Tới chừng… thì…" · chốt bằng phủ định "hông phải… đâu, … quá đó" · rào sức khỏe giọng đời ("đau nhói thì nghỉ, đi khám nha"), không giọng pháp lý.

**Tin Zalo trả lời người hỏi · Trung (Huế) · 40+ · anh Phong, 45, tư vấn mở quán cà phê · anh – em**

> Chào em, anh Phong đây. Anh đọc tin em hồi tối rồi. Nói thiệt, năm 2016 anh cũng mở quán y như em đang tính: thuê mặt bằng đẹp trước, rồi mới ngồi tính một ly bán bao nhiêu. Được bảy tháng thì đóng. Chừ ai hỏi anh cũng khuyên làm ngược lại: tính giá một ly trước, đủ sống rồi mới đi coi mặt bằng. Em gửi anh ba con số: tiền thuê, giá một ly, một ngày bán chừng mấy ly. Sáng thứ Bảy anh ngồi với em được, em coi có tiện không nghe.

Tên + "đây" + đã đọc tin · kể mình từng sai thay vì chê kế hoạch của người ta · câu cụt "Được bảy tháng thì đóng." · đổi thứ tự là bài học · xin đúng ba con số · kết mềm "em coi có tiện không nghe" · chỉ hai chữ địa phương ("chừ", "nghe") để người vùng khác vẫn đọc trôi.

**Đoạn livestream · Nam · 30–39 · chị Diễm, 36, coach ăn dặm · chị – các mẹ, em**

> Rồi, Thảo Vy hỏi là bé nhà em mười tháng mà ăn cháo cứ ngậm hoài, phải hông. Nghe quen ghê. Bé nhà chị hồi đó cũng vậy á, một chén cháo đút từ trưa tới gần hai giờ, chị ngồi muốn khóc luôn. Xong có bữa chị lười, hấp miếng bí, cắt thanh dài để đó cho bé tự cầm. Ai dè bé bốc ăn ngon lành. Hóa ra hông phải bé biếng ăn đâu, bé muốn tự làm. Thảo Vy thử bữa tối nay nha, rồi lên đây kể chị nghe. Còn ai hỏi gì nữa hông, chị đọc tiếp nè.

Đọc tên người bình luận · đồng cảm ba chữ "Nghe quen ghê" (không "Chị rất thấu hiểu cảm giác của em") · chi tiết giờ giấc · cảm xúc mộc "muốn khóc luôn" · ngoặt đôi "Ai dè… Hóa ra hông phải… đâu" · giao việc + hẹn kể lại · trả lượt.

**Kịch bản Reels · Bắc · 25–39 · Hoàng, 34, dạy nói trước đám đông · mình – bạn**

> Chuyện là tuần trước mình đi đám cưới thằng bạn thân, bị gọi lên phát biểu. Mình dạy nói trước đám đông sáu năm rồi đấy nhé. Thế mà cầm mic lên, tay vẫn run. Run thật. Cơ mà không ai biết, vì mình làm đúng một việc: câu đầu tiên nói chậm gấp đôi bình thường. Nói chậm thì thở sâu được, thở sâu thì giọng hết run. Bạn nào sắp phải lên nói gì đấy thì nhớ, run là bình thường, chỉ cần câu đầu chậm lại thôi.

"Chuyện là" vào cảnh ngay · tự hạ mình · câu cụt lặp "Run thật." · "Cơ mà" (Bắc trẻ) · "đúng một việc" · chuỗi "thì" nối vòng thay cho "điều này giúp…" · bình thường hóa nỗi sợ rồi mới giao việc.

**Bài Facebook · Nam · 50 · chị Mai, dạy nghề nấu cơm tấm bán sáng · chị – mọi người**

> Sáng nay sáu giờ, em Thắm học viên khóa trước gọi chị, vừa alo là khóc. Chị hết hồn, tưởng có chuyện gì. Ai dè em nói: "Chị ơi em bán hết sạch rồi, bốn chục dĩa, chưa tới tám giờ." Năm ngoái em bị cho nghỉ ở xưởng may, bốn mươi lăm tuổi, đi xin chỗ nào cũng chê lớn tuổi. Chị nghe mà cũng rưng rưng theo. Nghề này hổng giàu nhanh được đâu, cực lắm. Mà được cái mình đứng bếp nhà mình, hổng ai cho mình nghỉ. Ai đang tính học nghề làm lại từ đầu thì nhắn chị, chị kể thiệt cho nghe cực cỡ nào.

Mở bằng giờ + cuộc gọi + việc bất ngờ · ngoặt giả rồi ngoặt thật ("hết hồn… Ai dè") · lời nguyên văn có số, giọng Nam ("dĩa") · lùi thời gian cho thấy cái giá · một chữ cảm xúc có "cũng… theo" · cân lại cho khỏi nổ ("hổng giàu nhanh… Mà được cái…") · mời nhắn, hứa nói thật về cái cực. (Chuyện kết quả của học viên chỉ đăng khi học viên đồng ý: §CM-GUARDRAILS.)

---

## 4. Xưng hô, tiểu từ, độ thẳng, chữ tiếng Anh, emoji

### 4.1 Cặp xưng hô: coach tự xưng – gọi khách

Cặp xưng hô định ra tuổi, vị thế, độ thân. Chọn sai là cả bài lệch, dù chữ nào cũng đúng. Cột "kéo theo" quan trọng ngang cột cặp: đổi cặp là đổi cả cách bảo, cách rào, tiểu từ, độ đùa.

| Cặp | Nghe ra sao | Hợp với ai, ở đâu | Kéo theo | Rủi ro |
|---|---|---|---|---|
| **mình – bạn** | Ngang hàng, thân mà giữ lễ, không lộ tuổi | Mặc định cho coach 25–40 nói với dân văn phòng, người trẻ; TikTok, Reels, Threads, Facebook | "thử / cứ / … nhé (nha)"; tự trào, đùa được | Gọi khách 45+ là "bạn" nghe trống, thiếu lễ |
| **mình – mấy bạn** (Nam) / **mình – các bạn** | "Mấy bạn" thân; "các bạn" trung tính, hơi đứng lớp | Video nói, bài gọi một nhóm | Đi lại giữa "mấy bạn" (gọi nhóm) và "bạn" (một người) | "Các bạn" lặp nhiều như MC |
| **mình – mọi người / mn** | Rộng, ấm; "mn" là cách viết của người trẻ | Bài kể đời thường, live, caption | Câu kể, câu hỏi chung | Mơ hồ khi cần dặn một người |
| **mình – cả nhà** | Thân như trong nhóm quen | Nhóm Facebook riêng, nhóm Zalo lớp, live với người xem quen | "Cả nhà ơi", hỏi han | Với người lạ trên bài công khai thì sến; "cả nhà iu" là giọng shop online |
| **mình – các chị em / chị em mình** | Phụ nữ cùng cảnh, cùng phe | Coach nữ nói với mẹ bỉm, chủ shop, phụ nữ đi làm | "Chị em mình" kéo người đọc về cùng phía | Đàn ông đọc thấy bị gạt ra; "các mom", "nàng ơi" là giọng bán mỹ phẩm |
| **mình – anh chị** | Coach trẻ hoặc ngang tuổi nói với chủ doanh nghiệp 30+ | Facebook chuyên nghiệp, nhóm chủ quán | Lời bảo mềm hơn "mình – bạn" | "Anh chị em" như MC sự kiện |
| **tôi – anh chị** | Chuyên gia, chắc, có khoảng cách, đáng tin với người 40+ | Tư vấn 40+, B2B; Facebook dài, LinkedIn | Ít tiểu từ, câu đủ, có số; bảo thẳng được | Trên video ngắn, với khán giả trẻ thì lạnh, kẻ cả |
| **tôi – các bạn** | Giảng viên trên bục | Bài dài kiểu chuyên mục, podcast | Câu khẳng định, ít đùa | Rất dễ thành giọng lên lớp; tránh làm mặc định |
| **em – anh chị** (+ "Dạ… ạ") | Người trẻ hơn, lễ phép, làm dịch vụ | Dịch vụ, môi giới, bảo hiểm, chụp ảnh, thợ; inbox, Zalo; cả bài công khai nếu coach trẻ | "giúp em", "em thấy", "theo em"; lời bảo thành lời nhờ; "ạ" | Hạ vị thế chuyên gia; lạm dụng "ạ" thành giọng nhân viên trực page |
| **chị / anh – em, chị – các em** | Người đi trước kèm người đi sau; thương mà thẳng | Kèm nghề, nhóm học viên, Zalo học viên | Bảo thẳng được ("bỏ câu đó đi em"); "không sao đâu em" | Gọi khách trưởng thành ngang tuổi là "các em" nghe kẻ cả |
| **cô / thầy – các con** | Giáo viên với học trò | Lớp học thêm, lớp kỹ năng trẻ em, nhóm Zalo lớp | Với phụ huynh vẫn xưng "cô / thầy" (phụ huynh gọi theo con), gọi phụ huynh là "anh chị" | Dùng "các con" với người lớn là lố |
| **Tên riêng – anh chị** ("Hiếu", "Trâm") | Thân mà khiêm, kiểu chủ tiệm, thợ, người trẻ | Trang của tiệm, TikTok | Xen "tụi em", "bên em" cho đỡ lặp tên | Xưng tên năm câu liền nghe như kể về người thứ ba |
| **tui – mấy bạn / bà con** | Nam, đời, rất thật | Facebook cá nhân, TikTok giải trí | "thiệt", "hổng", "luôn á" | Với khách Bắc, khách sang, bài nghiêm thì suồng sã |
| **mình – anh em / ae** | Nam, dân kinh doanh | Nhóm kinh doanh nam | Giọng hô hào | Đi kèm "hữu duyên", "chiến binh" thành giọng hội làm giàu; chỉ khi coach tự nói vậy |
| **tớ – cậu** | Học trò | Gen Z với Gen Z | | Coach bán dịch vụ dùng thì non |
| **chúng tôi – quý khách** | Công văn, hợp đồng | Hóa đơn, điều khoản, thông báo chính thức | | Trên mạng xã hội như tờ rơi, như ngân hàng; không dùng trong bài và tin nhắn |
| **tao – mày** | Bạn rất thân hoặc gây sự | Chỉ trong lời thoại nhân vật của một tiểu phẩm | | Xúc phạm; không bao giờ |

**Chữ thay "chúng tôi" cho coach hay tiệm nhỏ:** *bên mình, bên em, tụi mình / tụi em* (Nam, Trung), *bọn mình / bọn em* (Bắc), *nhà mình, tiệm em, xưởng tụi em, lớp mình*. "Mình" còn gộp được người nghe ("chị em mình", "lớp mình"), nên gần như không cần "chúng ta" (kho lời nói: "chúng ta" 0 lần).

### 4.2 Một câu, năm cặp xưng hô

Cùng một lời dặn: *ghi âm 1 phút kể về ngày hôm nay, rồi nghe lại.*

| Cặp, vùng | Câu | Đổi gì |
|---|---|---|
| mình – bạn, Bắc | "Tối nay bạn thử ghi âm 1 phút kể chuyện hôm nay, xong nghe lại xem nhé. Đảm bảo giật mình đấy." | "thử … xem nhé": rủ ngang hàng; "đảm bảo… đấy": đùa nhẹ, nhấn ở cuối (không "Mình cá là bạn sẽ…", dịch "I bet you'll…") |
| mình – mấy bạn, Nam | "Tối nay mấy bạn ghi âm 1 phút kể chuyện hôm nay coi, rồi mở ra nghe lại. Bất ngờ lắm á." | "coi", "á": giọng Nam; câu cụt |
| tôi – anh chị, trung tính | "Tối nay anh chị ghi âm 1 phút, kể lại chuyện trong ngày, rồi nghe lại. Nghe mới thấy mình 'ờ', 'à' nhiều đến mức nào." | Không tiểu từ; câu đủ; bảo thẳng vì có vị thế |
| em – anh chị | "Tối nay anh chị thử giúp em một việc nhỏ ạ: ghi âm 1 phút kể chuyện hôm nay rồi nghe lại. Nghe xong thấy sao anh chị nhắn em với nhé." | Lời bảo thành lời nhờ; "ạ" một lần; "với nhé" mềm |
| chị – các em, Bắc | "Tối nay các em ghi âm 1 phút kể chuyện hôm nay, xong nghe lại. Nghe là biết ngay mình hay vấp ở đâu. Làm đi rồi nhắn chị." | Bảo thẳng, không rào; thân, có trách nhiệm kèm |

### 4.3 Đổi cặp là đổi những chữ này

| | mình – bạn | tôi – anh chị | em – anh chị | chị – em, cô – các con |
|---|---|---|---|---|
| **Lời bảo** | "thử…", "cứ…", "… nhé / nha" | Câu đủ, thẳng: "Anh chị làm thử một món thôi." | Lời nhờ: "anh chị … giúp em", "anh chị thử … xem ạ". Không "Hãy…", không mệnh lệnh trơn | Thẳng: "bỏ câu đó đi em", "làm đi rồi nhắn chị" |
| **Rào** | "mình thấy", "theo mình" | Ít rào; thay bằng số và kinh nghiệm: "10 năm mở quán, tôi thấy…" | "em thấy", "theo em", "em nghĩ là" | Ít; "chị nói thật nhé" |
| **Tiểu từ** | nhé / nha, á, nè, đó | "nghe", "nhé", "ạ" rất thưa; LinkedIn gần như không | "Dạ" mở, "ạ" kết; "nha ạ", "nhé ạ" | nhé, nhỉ, đấy, chứ (Bắc); nha, nè (Nam) |
| **Đùa** | Tự trào thoải mái | Đùa khô, ít | Không trêu người lớn hơn | Trêu thương được ("khổ thân em") |
| **Chữ cảm xúc** | "quê", "nản", "sướng" | Ít; nói qua việc | "em hiểu cảm giác đó ạ" | "thương", "không sao đâu em", "ối giời" (Bắc) |

### 4.4 Giữ cặp: chống "trôi xưng hô"

1. **Chữ tự xưng cố định cả bài.** Không "mình" đoạn đầu, "tôi" đoạn giữa, "chúng tôi" ở dòng giá. Đây là lỗi AI hay mắc nhất khi bài có phần bán.
2. **Chữ gọi khách đi lại trong một họ:** "mấy bạn ↔ bạn", "các chị em ↔ chị em mình", "anh chị ↔ anh / chị" (khi nói với một người). Không nhảy họ: "bạn" → "anh chị" → "các em".
3. **Lời thoại trong chuyện giữ xưng hô của người nói.** Bài "mình – bạn" vẫn trích được khách nói "Chị ơi em sợ lắm". Đó là lời khách, không phải trôi cặp.
4. **Công khai một cặp, nhắn riêng có thể là cặp khác.** Bài đăng "mình – các chị em", sang Zalo với một học viên thì "chị – em". Bài trên Trang "Hiếu / tụi em – anh chị", sang tin nhắn với khách lớn tuổi thì "Dạ, em – anh". Máy giữ cả hai cặp, không trộn; tin riêng gọi số ít.
5. **Người kia đặt quan hệ trước thì đi theo, nếu hợp với coach.** Người bình luận gọi coach là "c" (chị) thì đáp "em" là tự nhiên; đáp "bạn" nghe như đẩy người ta ra xa. Coach vẫn có thể giữ "mình", nhưng đừng gọi lại người ta bằng chữ thấp hơn hay cao hơn chữ họ vừa tự nhận.
6. **Không chắc thì chọn cặp ít rủi ro:** khán giả trẻ hoặc trộn tuổi → "mình – bạn"; chủ doanh nghiệp 35+ → "mình – anh chị"; tin riêng với người chưa rõ tuổi → "Dạ" + gọi "anh / chị" theo ảnh đại diện và cách họ viết, không "bạn".

**Gọi tên:** tên kèm vai ("chị Lan", "anh Hùng", "Hà"); không "chị Nguyễn", "Mr. Hùng", "bạn Nguyễn Thị Lan". Một lần mỗi tin là đủ; lặp tên câu nào cũng có là kiểu tin tự động. Miền Nam, người lớn tuổi đôi khi tự giới thiệu theo thứ ("cô Ba", "chú Sáu"): chỉ gọi vậy khi họ tự xưng. Coach trả lời bằng chính mình ("mình", "Vy", "em Quân"), không "Ad gửi bạn nhé".

### 4.5 Máy nói với coach: cặp thứ hai, tách hẳn

Cặp máy – coach hỏi ở trả lời 1, lưu ở `pronouns`, tách khỏi `audience_address` (wf14 V4, §CM-VOICE 3).

| Coach viết cho máy kiểu | Máy làm |
|---|---|
| "em xem cái này", "em coi cái ni" (coi máy là "em") | Xưng "em", gọi "chị / anh" (+ tên nếu biết); "Dạ" khi trả lời câu hỏi, không câu nào cũng "ạ" |
| "bạn viết giúp mình…" | "mình – bạn" |
| "t / m" (tao – mày), kiểu bạn thân, như tin của founder | **Không** đáp tao – mày. Giữ năng lượng thân: ngắn, thẳng, bỏ khách sáo, không "Dạ… ạ". Xưng "mình" hoặc bớt xưng |
| "tôi cần…", viết trang trọng | "mình – bạn", hoặc "em – anh / chị" nếu biết người lớn tuổi; tránh "tôi – bạn" (giọng máy mặc định, lạnh) |
| Coach mở bằng "Dạ" với máy | Coach lễ phép, có thể lớn tuổi: "em – anh / chị" an toàn |

**Giọng trợ lý dịch cần bỏ:**

| Trợ lý dịch (gốc Anh) | Nói như người |
|---|---|
| "Chắc chắn rồi!" (Sure!) / "Tuyệt vời!" (Great!) | "Được chị." / "Rồi, em làm luôn." |
| "Câu hỏi rất hay!" (Great question!) | Bỏ, trả lời luôn |
| "Dưới đây là 5 mẫu caption dành cho bạn:" (Here are…) | "5 bản đây chị:" / "Em viết 5 bản, chị chọn:" |
| "Tôi hiểu rồi." (I understand) | "Dạ em hiểu rồi." / "Rồi." |
| "Hy vọng điều này hữu ích!" (Hope this helps) | Bỏ |
| "Hãy cho tôi biết nếu bạn cần thêm hỗ trợ." (Let me know if…) | "Chỗ nào chưa giống giọng chị thì chị chỉ em nha." |
| "Bạn có muốn tôi viết thêm phiên bản cho TikTok không?" (Would you like me to…) | "Có cần em làm thêm bản ngắn cho TikTok không ạ?" |
| "Tôi rất sẵn lòng hỗ trợ bạn." | Bỏ |
| "Lưu ý:", "Kết luận:", "Tổng kết:" làm tiêu đề | Bỏ tiêu đề; "À, có một chỗ chị để ý:" |

### 4.6 Tiểu từ: khi nào thật, khi nào giả

| Tiểu từ | Vùng | Làm gì | Tự nhiên khi | Nghe giả khi |
|---|---|---|---|---|
| **Dạ** (đầu câu) | Cả nước; Nam dùng rộng hơn, cả thay "vâng" | Nhận lời, mở lời đáp người lớn hơn hoặc khách | Đầu tin trả lời khách, phụ huynh, học viên lớn tuổi | Câu nào cũng "Dạ"; "Dạ" trong bài công khai của người lớn tuổi hơn khán giả |
| **ạ** (cuối câu) | Cả nước | Kính, mềm | Cuối câu hỏi, câu cảm ơn, câu báo tin với người lớn hơn | Sau mọi câu; "Hãy đăng ký ngay ạ"; coach 45+ viết "ạ" với khán giả 25 tuổi |
| **vâng** | Bắc | Đồng ý | "Vâng ạ", "Dạ vâng" | Coach giọng Nam |
| **nhé** | Bắc (trung tính trên báo) | Dặn, rủ, hẹn | "Tối nay thử nhé." | Coach giọng Nam (người Nam nói "nha"); sau lời trách nghe kẻ cả: "Lần sau đọc kỹ nhé." (Trung viết dùng cả "nhé" lẫn "nha"; chữ vùng là "nghe") |
| **nha** | Nam; lan ra cả nước trên mạng, nhất là người trẻ | Dặn nhẹ, thân | Caption, tin nhắn, video giọng Nam; coach Bắc trẻ khi bài thật của họ có | Coach Bắc 40+; "Hãy … nha" (trang trọng + thân = giả thân); ba câu liền "nha" |
| **nè** | Nam | Chỉ, đưa, gọi chú ý | "Em gửi chị file nè.", "Thử cái này nè." | Tin đầu với khách lớn tuổi; câu nghiêm (giá, cam kết, xin lỗi) |
| **á** | Nam, trẻ | Nhấn, kể | "Hay lắm á.", "Tầm 4 giờ á." | Dày đặc thành giọng teen; coach 45+ |
| **hen / hén** | Nam | Rủ, chốt nhẹ như người quen | "Vậy thứ Bảy gặp hen." | Với người lạ, khách sang |
| **nghen** | Nam (miền Tây) | Dặn thân, hơi quê | Coach gốc miền Tây nói thật | Coach Sài Gòn trẻ dùng thì như diễn |
| **nghe** | Trung; Nam lớn tuổi | Dặn, nhấn | "Nói thật nghe anh chị…" | Rắc cho có màu |
| **hỉ** | Trung | Rủ đồng tình | Một chữ mỗi bài | Rắc dày: giễu nhại giọng Trung, người Trung đọc sẽ phật ý |
| **nhỉ, đấy, thế, cơ** | Bắc | Rủ đồng tình, nhấn, nũng nhẹ | Giọng Bắc thật | Coach Nam, Trung |
| **đó** | Nam, Trung; Bắc cũng hiểu | Nhấn nhẹ | Chữ an toàn nhất toàn quốc | |
| **chứ** | Cả nước | Khẳng định | "Được chứ." | "…chứ ạ" với khách nghe như cãi |
| **mà** | Cả nước | Giải thích, nài | "Có ai cười đâu mà ngại." | "Em nói rồi mà." với khách nghe như trách |
| **luôn** | Nam, lan rộng | Ngay, trọn | "Em gửi luôn." "Làm luôn." | |
| **thôi** | Cả nước | Giới hạn, gỡ áp lực | "Một câu thôi." "Thế thôi." | |
| **đi** | Cả nước | Giục nhẹ | "Thử đi." (ngang hàng, chị – em) | Với khách lớn tuổi nghe như sai bảo |
| **nha ạ / nhé ạ** | Người trẻ nói với nhiều người | Vừa thân vừa lễ | Coach 20–30 nói với đám đông trộn tuổi | Coach 40+ dùng thì non |

**Liều lượng** (phán đoán; mốc thật lấy từ bài của chính coach):
- Bài Facebook, caption: khoảng một tiểu từ cuối câu cho mỗi 2–4 câu. Câu kể sự việc để trơn; tiểu từ đặt ở câu dặn, câu rủ, câu kết.
- Tin nhắn, Zalo: dày hơn; hầu hết câu dặn, câu hỏi có tiểu từ.
- Video nói: theo giọng thật của coach (thường dày hơn bài viết).
- LinkedIn: 0–2 cả bài.
- Không ba câu liền cùng một tiểu từ.
- Dòng giá, điều khoản, hoàn tiền trong **bài đăng** để trơn ("Học phí 1.890.000đ."). Trong **tin nhắn** thì "1.890.000đ nha chị" vẫn tự nhiên.
- Trong kho bài viết của 6 nhân vật eval, 36% số câu kết bằng tiểu từ, dao động 14% đến 67% tùy người; câu trả lời của AI chưa có pack chỉ 11%. Nên luật đếm phải so với bài thật **của chính coach**, không theo một con số chung.

**Cái bẫy hay gặp:** máy thấy luật "dùng tiểu từ" là rắc đều: "Bạn đăng ký nha. Khóa học hay nha. Giá cũng rẻ nha." Người thật dùng tiểu từ ở **chỗ có quan hệ**: chỗ dặn, chỗ rủ, chỗ làm thân, chỗ gỡ căng.

### 4.7 Độ thẳng: nói ngược ý mà không thô

Ý muốn nói: *quán ăn giảm giá 50% trên TikTok để kéo khách là kéo nhầm người.* Coach: Phát, Sài Gòn, "mình – anh chị".

| Mức | Câu | Nhận xét |
|---|---|---|
| 1. Mềm tới mức không nói gì | "Giảm giá cũng là một cách hay, nhưng anh chị cũng có thể cân nhắc thêm nhiều phương án khác nữa ạ." | Vô hại mà vô vị. AI hay dừng ở đây |
| 2. Mềm có ý | "Giảm giá thì khách tới thật, mà toàn khách tới vì giá. Hết giảm là vắng." | Được với coach hiền, khán giả dễ tự ái |
| 3. **Thẳng ấm (mặc định)** | "Nói thiệt nha anh chị, giảm 50% là kéo người ham rẻ chứ hổng kéo khách quen. Hồi mới làm mình cũng xúi quán giảm, tháng sau vắng hơn tháng trước." | Thẳng về **cách làm**; tự nhận từng sai; có hậu quả cụ thể |
| 4. Thẳng gắt (chỉ khi giọng coach vậy) | "Giảm 50% trên TikTok là bỏ tiền mời người lạ ăn một bữa rồi đi luôn. Dừng đi." | Gọn, gắt. Chỉ khi Hồ sơ giọng ghi coach nói thẳng như thế |
| 5. Quá đà (không bao giờ) | "Quán nào còn giảm 50% là quán sắp dẹp, chủ quán không có não kinh doanh." | Chửi người, quơ đũa cả nắm, có thể thành khủng hoảng |

**Phản bác mà giữ lòng nhau:**

| Dùng | Tránh |
|---|---|
| "Nói thật nha / nhé, …" · "Nói ra chắc mất lòng vài người, mà…" | "Sự thật mà không ai dám nói với bạn" (khuôn câu nhử) |
| "Nhiều người khuyên X. Mình thì làm ngược lại, vì…" | "Ai nói X là sai bét." |
| "Không phải X sai. Mà X chưa đủ." | "Bạn đang làm sai hoàn toàn." |
| "Đúng là X. Có điều…" (nhận phần đúng rồi mới ngoặt) | "Sai lầm chết người mà 99% mọi người mắc phải" |
| "Ngày xưa mình cũng làm y vậy." (tự gộp mình vào) | Đứng trên cao chỉ xuống: "Người thành công họ không bao giờ…" |
| "Nghe ngược đúng không?" · "Sự thật hơi khó nghe:" | "Tư duy người nghèo", "đầu óc", "não cá vàng" |
| Chỉ vào **một cách làm** cụ thể: "giảm 50% ngay tuần đầu mở quán" | Chỉ vào **một nhóm người** ("mấy ông chủ quán"), **một đối thủ** dù không nêu tên ("bên kia chặt chém") |

- **Rào nhiều quá cũng là giọng AI.** "Có thể", "có lẽ", "trong một số trường hợp", "tùy thuộc vào nhiều yếu tố" xếp chồng làm câu nhũn. Coach Việt rào bằng **chính mình** ("theo mình thấy", "ở lớp mình thì") rồi nói thẳng.
- **Chê đối thủ:** mặc định máy không nêu tên, không ám chỉ, không so sánh trực tiếp; muốn nói khác biệt thì nói **mình làm gì**: "Giá ghi trên bảng là giá chốt." Coach yêu cầu rõ một so sánh có tên thì máy viết, kèm đúng một dòng lưu ý có ngày (DECISIONS: không chặn; Luật Quảng cáo hạn chế so sánh trực tiếp trong quảng cáo, nên dòng lưu ý nói điều đó). Chê **cách làm**, không chê **người**.

### 4.8 Chêm tiếng Anh

| Mức | Chữ | Khi nào |
|---|---|---|
| **Bình thường** với dân thành thị, dân bán hàng online | content, sale, deal, feedback, team, deadline, KPI, booking, order, ship, livestream / live, review, check, inbox / ib, link, file, online, offline, group, page, follow, like, share, comment, clip, app, ok / oke, tips, trend, viral, workshop, CV | Được, nếu coach cũng nói vậy |
| **Tùy nghề, tùy người** | insight, mindset, case study, upsell, funnel, lead, branding, storytelling, mentor, coaching 1:1, JD, onboarding, target, dashboard, VBA | Chỉ khi coach dùng **và** khán giả cùng nghề (dân nhân sự hiểu "JD", chủ quán thì nói "việc phải làm") |
| **Nghe làm màu** với khách bình dân, 40+, tỉnh | handle, discuss, sure, actually, basically, problem, impact, value, solution, journey, empower, align, skill set, growth mindset, pain point, talent | Không dùng, trừ khi đó là giọng thật của coach |

- Báo chí Việt từ lâu chê kiểu "Với problem này, chúng ta nên discuss lại" là làm màu (Báo Quốc tế, 2008). Sinh viên chêm tiếng Anh trong caption TikTok như chơi chữ là giọng của họ (ĐH Thái Nguyên).
- **Chữ Anh đã Việt hóa cách viết**: "oke", "sốp" (shop), "phây": chỉ dùng khi coach tự viết vậy.
- **Ngữ pháp vẫn là tiếng Việt:** "đi check", "chốt sale", "feedback của học viên". Không bê ngữ pháp Anh: "các bạn mà không sure".
- **Đừng dịch ngược chữ ai cũng nói:** "tiếp thị nội dung" thay "content", "người có sức ảnh hưởng" thay "KOL", "trang đích" thay "landing page", "lời kêu gọi hành động" thay "CTA". Với dân văn phòng, dịch cứng còn lạ hơn để nguyên. Với khách bình dân thì nói bằng việc: "trang đăng ký", "câu mời".
- **Luật cho máy:** dùng đúng danh sách `code_mix` của coach; không có trong danh sách thì nói tiếng Việt thường ngày; không bao giờ thêm chữ Anh coach không dùng.

### 4.9 Emoji và mặt cười

| Ký hiệu | Người Việt thường đọc là | Dùng thế nào |
|---|---|---|
| **:))** **:)))** | Cười thân, vui | An toàn với 25–45. AI gần như không bao giờ viết ra, dù rất Việt |
| **=)))** | Cười to, trẻ hơn | Người trẻ |
| **:)** (một ngoặc) | Có thể là cười nhạt | Tránh trong tin trả lời khách |
| **🙂** | Với nhiều người trẻ: cười mỉa, cạn lời, bực mà không nói (nguồn chỉ đọc qua tóm tắt) | Không dùng khi trả lời khách; khi người khác gửi "🙂" dưới bài, thường là mỉa |
| **😅** | Ngại, tự trào | Hợp khi kể lỗi của mình |
| **😄** | Vui, mộc | Hợp 40+ |
| **🙏** | Cảm ơn, nhờ | Thợ, chủ tiệm, 40+ |
| **❤️** | Ấm | Kết bài, cảm ơn; một cái là đủ |
| **😭** | Gen Z: cười quá, bất lực vì buồn cười | Theo tuổi khán giả |
| **👍** | 40+: ok, đồng ý. Người trẻ có thể đọc một 👍 trơn là lạnh | Kèm chữ |
| **💀** | Gen Z: chết cười. Người lớn: đầu lâu | Tránh với khách lớn |
| **👉 ✅ 📌 👇** | Gạch đầu dòng của bài bán | Vừa phải trong bài bán; không trong bài kể |
| **🚀 ✨ 💡 🎯 📈 🔥** đầu mỗi dòng | Mùi AI, mùi bài bán hàng loạt | Không |
| **hihi / hehe / haha** | Dễ thương / ranh mãnh / cười | "hihi" trong chuyện căng nghe coi thường; "hehe" mơ hồ thì lạnh |
| Sticker Zalo | Người 40+ dùng nhiều | Một cái để kết, không mở đầu |

Theo tuổi: Gen Z dày, đổi nhanh; 25–39 vừa phải; 40+ thưa, chữ đủ. Theo nền tảng: Facebook cá nhân 0–3 mỗi bài; caption TikTok 1–3; Zalo theo độ thân; LinkedIn 0–1. Coach không dùng emoji thì không thêm cái nào.

---

## 5. Bán hàng, lời mời, tin nhắn, bình luận

### 5.1 Chữ mời người Việt thật sự dùng

Thang an toàn với luật mồi tương tác của Meta, TikTok ở wf5 F8. Bảng này nói về **giọng**.

| Hành động | Nghe như người | Nghe như máy, như rao |
|---|---|---|
| Nhắn riêng | "Ai cần thì nhắn riêng mình." · "Nhắn mình chữ X, mình gửi." · "Có gì cứ nhắn em." | "Liên hệ ngay với chúng tôi để được hỗ trợ!" · "Inbox ngay!" |
| Comment từ khóa | "Ai cần thì comment chữ TĂNG CA, mình gửi qua tin nhắn." | "Comment 'GUIDE' ngay bên dưới để nhận tài liệu độc quyền hoàn toàn miễn phí!" |
| Đường lặng cho người ngại | "Ngại comment thì nhắn riêng mình chữ đó cũng được nha." | (AI gần như không bao giờ thêm câu này) |
| "ib", "inbox" | "ib" là chữ chat, hợp bình luận giữa người ngang tuổi; "inbox mình" phổ biến, hơi mùi bán | "Check ib" trơn làm câu trả lời cho người hỏi giá: cụt, giấu giá |
| "chấm", ngưỡng comment | Coach tự chọn thì là giọng của họ: "Chấm mình gửi file nha 👇", "Đủ 100 comment mình làm phần 2". Máy viết y vậy, thêm đúng một dòng lưu ý nền tảng có ngày, không chặn, không làm mềm (DECISIONS; §CM-CTA-KIT). Người comment "." để theo dõi bài là chuyện của họ | Máy **tự** đặt "chấm", tự đặt ngưỡng khi coach chưa chọn; "Comment CHẤM ngay để nhận tài liệu độc quyền!!!" |
| Zalo | "Anh chị kết bạn Zalo số ở ảnh bìa giúp em, em gửi bản vẽ qua đó cho rõ ạ." · "Em add chị vô nhóm lớp nha." | "Để lại số điện thoại để được tư vấn" (dưới bình luận công khai: không bao giờ) |
| TikTok | "Phần 2 mai lên." · "Link nhóm Zalo ở bio nha." | "Theo dõi để không bỏ lỡ những nội dung hữu ích tiếp theo!" |
| Đăng ký | "Nhắn mình chữ ĐĂNG KÝ, mình gửi lịch và học phí." · "Form có 2 câu, link mình gửi qua tin nhắn." | "Đăng ký ngay!" · "Nhanh tay!" · "Số lượng có hạn!" · "Đừng bỏ lỡ cơ hội!" |
| Mời mềm | "Cứ coi lịch đã nha, chưa cần quyết liền." · "Chưa phải lúc thì cứ bỏ qua tin này." | "Bạn sẽ hối hận nếu bỏ lỡ!" |

Lời giục kiểu Mỹ dịch sang tiếng Việt nghe như rao hàng; người Việt chuộng lời mời **có chừa đường lui** (văn hóa giữ thể diện, nói giảm nói tránh).

### 5.2 Chữ từ khóa

- **Chữ của chính tệp khách coach, 1–2 chữ, viết hoa, gọi đúng nỗi khổ hoặc món quà:** TĂNG CA, ẢNH TỐI, BIỂN, NGẠI CHÀO (DECISIONS: từ khóa là chữ gắn với coach và là chữ khách của họ hay nói). Thường là tiếng Việt; chữ Anh chỉ khi đúng là chữ khách nói hằng ngày (dân IT nói "CV"). Không GUIDE, FREE, INFO, EBOOK do máy tự chọn.
- Chính các coach trong bộ eval, khi thấy bài người khác bảo "comment GUIDE", đều chê: không hiểu chữ đó, thấy "hơi bán hàng", không ưa (bằng chứng ở `liked-paste.md`; không trích vào gói).
- **Luôn kèm đường nhắn riêng** cho người ngại để tên mình dưới bài. "Ngại" là một cảm xúc riêng của người Việt: ngần ngừ vì nghĩ cho người kia, không phải nhút nhát. Viết trúng chữ "ngại" là chạm đúng chỗ; dịch thành "e ngại, rụt rè, thiếu tự tin" là trật.
- Bài có từ khóa phải **cho đủ giá trị ngay trong bài**; món quà là phần đầy đủ, không phải phần bị giấu.
- Từ khóa coach đã tự chọn (cả "chấm", "ib", emoji) thì giữ nguyên, không đổi, không làm mềm (DECISIONS; §CM-CTA-KIT).

### 5.3 Nói giá

| Việc | Tự nhiên | Lệch |
|---|---|---|
| Bài bán | "Học phí 1.890.000đ." Đặt cùng chỗ với số buổi, lịch, số người | "Giá ib", "Inbox để nhận báo giá chi tiết" |
| Người hỏi giá dưới bình luận | Trả lời bằng con số, rồi "chi tiết mình nhắn riêng" | "Check ib nha" trơn |
| Tin nhắn | Giá ở câu đầu hoặc câu hai | Hỏi số điện thoại trước khi cho giá |
| Định dạng | Bài viết: 1.890.000đ hoặc 1,89 triệu. Tin nhắn: "1tr890", "1.890k" (Nam, trẻ, bán online), "1 triệu 890". Nói: "một triệu tám trăm chín mươi nghìn" (Bắc) / "chín chục ngàn" (Nam). "150k" quen với người trẻ; khách 50+ thì "150 nghìn / ngàn" | "1,890,000 VND", "$", "VNĐ 1.890.000" |
| Chữ đi kèm giá | "Số đó gồm 8 buổi, buổi nào cũng sửa bài từng người." | "Chỉ với 1.890.000đ" (calque "for only"), "giá cực sốc", "ưu đãi đặc biệt dành riêng cho bạn" (calque "just for you"), "khoản đầu tư cho bản thân mà bạn sẽ không bao giờ hối tiếc" |
| Thanh toán | "Chị chuyển khoản theo mã QR ở trên, nội dung ghi tên + 4 số cuối điện thoại giúp em ạ." · "Chia 2 lần được nha." · "Học 2 buổi đầu thấy không hợp thì nhắn mình, mình hoàn đủ." | "Vui lòng thực hiện thanh toán theo thông tin bên dưới." |

Vì sao không "giá ib": khách khó chịu và tự hỏi giá có đổi theo người hỏi không (LuatVietnam; Sapo). Thông tư 47/2014/TT-BCT đòi người bán qua mạng cung cấp thông tin giá. Chuẩn trong repo: giá công khai, không "giá ib" (`email-zalo.md`, §CM-LOCALE 5). Riêng dịch vụ báo giá theo công trình, theo khảo sát thì "nhắn em để em qua coi rồi báo giá" là đúng; cái sai là giấu giá của món có giá cố định. Gọi học phí là "khoản đầu tư" là chữ quen của các khóa làm giàu, làm người đọc cảnh giác: cứ gọi "học phí", "giá", "phí".

### 5.4 Hạn chót và số chỗ

- **Số chỗ đi kèm lý do thật:** "20 bạn, vì buổi nào mình cũng mở file từng người ra sửa." Không có lý do thì như chiêu.
- **Hạn có ngày giờ, nói luôn sau hạn thì sao:** "Đóng 23h59 thứ Sáu. Khóa sau chắc tầm tháng 3." Nói khóa sau là gỡ nỗi sợ bị bỏ lại.
- **Không:** "chỉ còn 3 suất" ngày nào cũng đăng, "giá tăng gấp đôi lúc 0h" khi không tăng thật, đồng hồ đếm ngược giả, mở lại ngay sau khi "đóng". Hạn và suất **thật** thì nói thẳng, kể cả trong đợt mở bán (DECISIONS: gấp gáp, khan hiếm thật là một bước của launch); chỉ cái giả mới bị chặn. Hạn và suất phải có trong Ledger (shared.md SG2).

### 5.5 Nổ, lùa, hứa quá, dí: chữ nào làm mất tin

Các khóa "dạy làm giàu" bị báo chí bóc nhiều năm; "lùa gà" và "coach dạy làm giàu" đã thành chữ chê (SGGP 2020; wf2 §1). Viết giống những khuôn đó, dù thật thà, vẫn bị xếp chung.

| Chữ, câu | Người đọc nghe ra | Viết lại |
|---|---|---|
| "x2 x3 doanh thu", "Thu nhập 100 triệu/tháng sau 3 tháng", "bùng nổ doanh số", "ra đơn ầm ầm" | Lùa gà; còn phạm luật quảng cáo | Một ca thật, có xin phép, có bối cảnh và chi phí, kèm "đây là kết quả của bạn ấy, không phải lời hứa" |
| "Đổi đời", "tự do tài chính", "thu nhập thụ động", "làm giàu" | Hội thảo làm giàu | Nói đúng cái thay đổi nhỏ, đo được |
| "Bí kíp", "bí mật không ai nói", "công thức độc quyền", "Hệ … 4.0™" | Đóng gói chữ cho kêu để bán khóa | "Cách mình làm", "3 bước mình dùng" |
| "Chuyên gia hàng đầu", "số 1", "duy nhất", "tốt nhất", "bậc thầy" | Nổ; "nhất, số 1" không có bằng chứng thì bị cấm | "Mình làm nghề này 7 năm." |
| "Cam kết 100%", "đảm bảo thành công", "hết đau", "trắng bật tông" | Hứa thay kết quả; sức khỏe, làm đẹp còn rủi ro pháp lý | Cam kết **cách làm**: "Mình cam kết buổi nào cũng sửa bài từng người. Kết quả thì do bạn làm, mình không hứa thay được." |
| "Hữu duyên", "chỉ dành cho người thật sự nghiêm túc", "người được chọn" | Chọn lọc giả, ép tâm lý | Nói thẳng ai **không** nên mua: "Không dành cho bạn nếu…" |
| "Xin vía", ảnh chuyển khoản, ảnh bill, khoe xe làm cả cái mồi | Khoe để câu khách | Số thật chỉ làm **bằng chứng**, đặt sau chuyện, có bối cảnh (DECISIONS: khoe chỉ làm bằng chứng, lời mời hay kiểu lật ngược, không làm cả hook); còn lại kể việc học viên làm được |
| "Đánh thức", "khai phá", "kích hoạt", "thức tỉnh", "sức mạnh tiềm thức", "năng lượng" | Giọng hội thảo cảm xúc | Chữ việc: "tập", "sửa", "làm thử" |
| "Thực chiến" lặp mọi bài | Chữ quảng cáo khóa học đã mòn | Nói học bằng việc gì: "cầm điện thoại quay ngay tại quán" |
| "Nếu không đầu tư cho bản thân, bạn sẽ mãi nghèo" | Dọa, làm nhục | Bỏ |
| "Cơ hội vàng", "siêu phẩm", "căn cuối cùng", "suất nội bộ" | Giọng rao, gây nghi | Con số thật |
| **Dí trong tin nhắn:** "Sao chị seen mà không rep em?", "Em thấy chị đã xem tin nhắn rồi…", gọi ngay sau khi người ta comment, ba tin liền, nhắn 11 giờ đêm | Bị theo dõi, bị ép; hay dẫn tới chặn Zalo | Nhắc **một lần**, có đường lui (5.7) |

Chữ lóng máy cần hiểu khi coach nói tới: *nổ, chém gió* (khoe quá sự thật), *lố* (quá đà), *lùa gà*, *phông bạt* (khoe mẽ, chữ người trẻ), *sống ảo*, *seeding* (nick ảo vào khen).

**Cái gì làm người Việt tin:** giá công khai, hạn thật, hoàn tiền nói rõ điều kiện; "Không dành cho bạn nếu…" và chỉ chỗ khác khi mình không hợp; nói được cái mình **không làm được** ("Móng bị nấm thì tiệm em không nhận, chị đi khám trước nha"); nói thẳng chuyện tiền của **mình** ("Link máy này mình có ăn hoa hồng, nói trước cho rõ nha"); số nhỏ, cụ thể, có bối cảnh, kể cả ca không thành; tự trào về lần mình sai; người thật đồng ý cho hỏi trực tiếp.

### 5.6 Nối từ chuyện sang lời mời

| Cầu nối AI | Cầu nối người |
|---|---|
| "Và đó chính là lý do tôi tạo ra khóa học X." (And that's why I created…) | "Từ hồi đó lớp mình mới dạy theo kiểu…" · "Nên lớp này mình làm khác:" |
| "Nếu bạn cũng đang gặp vấn đề tương tự, khóa học này dành cho bạn." | "Ai đang y vậy thì…" · "Bạn nào đang kẹt đúng chỗ này thì nhắn mình." |
| "Ngoài ra, bên em còn có các gói dịch vụ khác như…" (trong tin nhắn) | Hỏi một câu để biết người ta cần gì rồi mới nói gói hợp |
| "Đừng để X cản trở bạn thêm nữa!" | Bỏ. Kết bằng một việc nhỏ hoặc lời mời có đường lui |

### 5.7 Tin nhắn riêng: inbox, Messenger, Zalo

**Khung bốn nhịp:**
1. **Gọi + "Dạ"** (nếu người lớn hơn hoặc là khách): "Dạ chị Hoa," / "Chào Hà,". Gọi tên một lần.
2. **Trả lời đúng câu họ hỏi, trước tiên.** Hỏi giá thì câu đầu là giá. Hỏi lịch thì câu đầu là lịch.
3. **Một câu hỏi lại** để hiểu họ (một câu, không phải bảng khảo sát).
4. **Bước tiếp, cụ thể, nhẹ:** "Chị muốn em giữ chỗ không ạ?" / "Chị cứ coi lịch đã nha." / "Tối nay 8 giờ em gọi chị được không ạ?"

**Độ dài:** 2–5 câu; tin đầu với người lạ nên dưới khoảng 60 chữ (phán đoán). Không dán nguyên bài đăng vào tin nhắn. Có ảnh, link thì tách tin riêng, kèm một dòng nói ảnh đó là gì ("em khoanh đỏ chỗ bị ố ở ảnh trên ạ"). Tin đầu tiên sau khi người ta hỏi về khóa phải đủ: lịch, học phí, ưu đãi đến bao giờ, số chỗ, rồi một câu hỏi.

**Điểm chung của tin nhắn người thật** (đọc từ tin mẫu của các coach trong bộ eval): tự giới thiệu bằng tên ("em Quân đây", "anh Phong đây"), nói việc đã làm ("em xem ảnh rồi", "anh đọc tin em rồi"), có chi tiết thật, một bước tiếp có giờ ("tối nay", "sáng thứ Bảy 9 giờ"), **không một chữ khách sáo**. Không ai viết "Cảm ơn anh đã tin tưởng".

**Zalo:**
- **Ghi âm:** với khách 40+, một tin thoại 30–60 giây ấm hơn một đoạn chữ dài. Máy có thể viết **ý cho tin thoại** để coach nói, không viết thành văn đọc.
- **Sticker:** một cái để cảm ơn hay kết chuyện là tự nhiên, nhất là 40+. Không mở tin đầu với khách bằng sticker.
- **Ảnh thật kèm một dòng:** ảnh công trình, ảnh file, có khoanh đỏ. Bằng chứng gọn nhất.
- **Giờ nhắn** (phán đoán): tin bán hàng trong khoảng 7h–21h; trả lời người vừa nhắn thì giờ nào cũng được. Nghị định 91/2020 có quy định giờ cho tin nhắn, cuộc gọi quảng cáo qua viễn thông (SMS, cuộc gọi; cần luật sư kiểm có áp cho chat không), nên dùng làm phép lịch sự.
- **"Seen" mà không trả lời:** chuyện thường, không trách. Nhắc lại **một lần**, có đường lui: "Mình nhắn lần này nữa thôi nha: … Chưa phải lúc thì cứ bỏ qua tin này."
- **Dòng dừng:** chuỗi tin Zalo có "Muốn dừng nhận tin, nhắn DỪNG"; tin xin thông tin nói rõ dùng để làm gì (`email-zalo.md` EM6; Luật 91/2025).
- **Nhóm Zalo:** "Cả nhà ơi", "Cả lớp ơi"; ghim tin quan trọng (lịch, link, nội quy); @Tất cả chỉ khi nhắc lịch; câu hỏi riêng thì trả lời riêng; không bán trong nhóm học viên khi chưa nói trước.
- **Nhật ký Zalo:** ít bài bán; đăng bán liên tục thì bạn bè hủy kết bạn hoặc chặn xem nhật ký (tỉ lệ hay được khuyên: khoảng 80% đời sống, giá trị, 20% bán).
- **Viết tắt:** "c, e, ko, dc" chỉ khi coach thật sự dùng, với người đã quen, không bao giờ trong tin đầu với khách mới.
- **"anh/chị" có gạch chéo** trong tin gửi một người là dấu hiệu tin mẫu. Nhìn tên, ảnh, cách họ viết mà chọn.

**Tin cụt, tin dồn:**

| Cụt, lạnh | Ấm mà vẫn ngắn |
|---|---|
| "Ok" · "Ừ" · "Biết rồi" · 👍 trơn | "Dạ em nhận rồi ạ." · "Ok chị, mai em gửi nha." · "Rồi nha em." |
| "Đã nhận." | "Em nhận được tiền rồi ạ, cảm ơn chị. Thứ Hai em thêm chị vô nhóm lớp nha." |
| Ba tin liền: "Chị ơi" / "Chị còn đó không" / "Chị ơi???" | Một tin đủ ý |
| Trả lời muộn mà không nói gì | "Em xin lỗi trả lời chị muộn, hôm nay em đứng lớp cả ngày ạ." |

### 5.8 Trả lời bình luận

| Tình huống | Làm | Đừng |
|---|---|---|
| **Hỏi giá** | Trả lời bằng con số công khai, rồi "lịch học mình nhắn riêng rồi nha" | "Check ib", "ib", "Bạn vui lòng kiểm tra tin nhắn" |
| **Comment từ khóa** | "Mình gửi rồi nha, chưa kết bạn thì tin hay nằm ở mục tin nhắn chờ, bạn xem giúp mình." | "Đã gửi! Vui lòng kiểm tra hộp thư đến 📩" |
| **Chê có lý** | Nhận phần đúng, nói đã đổi gì, mời nhắn riêng nếu cần thông tin cá nhân | "Cảm ơn bạn đã góp ý! Chúng tôi luôn lắng nghe và tiếp thu…" |
| **Nghi "lùa gà"** | Không tự ái. Đưa thứ kiểm được: giá công khai, hoàn tiền, người thật đồng ý cho hỏi | Phản công, khoe "hàng nghìn học viên", bảo người ta "thiếu thiện chí" |
| **Kể chuyện của họ** | Đáp đúng chi tiết họ kể, hỏi một câu, có thể làm nội dung tiếp (không nêu tên nếu chưa xin) | "Cảm ơn bạn đã chia sẻ câu chuyện vô cùng truyền cảm hứng! ❤️❤️❤️" |
| **Khen** | Cảm ơn ngắn, bằng chữ của coach, kèm một chi tiết | "Cảm ơn bạn rất nhiều! Chúc bạn một ngày tốt lành! 🥰" lặp y nhau dưới mọi lời khen |
| **Troll, mỉa** | Một câu bình thản, hoặc để đó | Đôi co nhiều lượt |
| **Để lộ số điện thoại** | Ẩn bình luận, nhắn riêng: "Mình ẩn bình luận có số của chị cho an toàn nha, mình gọi chị rồi." | Để nguyên; xin số công khai |
| **Quảng cáo của người bán khác** | Ẩn, không đáp | Cãi |
| **Chửi tục** | Ẩn hoặc xóa | Đáp cùng giọng |

Gọi tên, kèm "ơi" khi thân ("Hà ơi, …"). Bài "em – anh chị" thì "Dạ chị ơi, …" ngay cả ở bình luận công khai cũng tự nhiên (tiệm, thợ, dịch vụ). Giữ cặp của bài, chuyển sang số ít. Đừng xóa bình luận chê trừ khi chửi tục: người khác đang nhìn cách mình xử lý. Không seeding, không dùng nick khác vào khen (Nghị định 147/2024). Câu hỏi hay của người bình luận là nguồn cho bài tiếp.

### 5.9 Giọng tổng đài, trợ lý, rao hàng: bảng thay chữ

| Tránh (gốc) | Dùng |
|---|---|
| "Cảm ơn anh/chị đã quan tâm đến sản phẩm/dịch vụ của chúng tôi" | "Dạ chào chị," rồi trả lời luôn |
| "Để được tư vấn chi tiết, vui lòng để lại số điện thoại" | (trong tin nhắn, sau khi đã nói giá) "Dạ học phí 1.890.000đ ạ. Chị cho em xin số Zalo, em gửi lịch học qua đó cho dễ coi." |
| "Nhân viên sẽ liên hệ lại trong thời gian sớm nhất" | "Tối nay 8 giờ em gọi chị được không ạ?" |
| "Xin lỗi vì sự bất tiện này" (Sorry for the inconvenience) | "Em xin lỗi chị, lỗi bên em để chị chờ." |
| "Đừng ngần ngại liên hệ" (Don't hesitate) | "Có gì chị cứ nhắn em." |
| "Vui lòng …" (Please) | "… giúp em / giúp mình", "… nha" |
| "Chúc bạn một ngày tốt lành!" cuối mọi tin | Bỏ; hoặc câu thật: "Chị ngủ ngon nha." khi đúng là tối khuya |
| "Rất hân hạnh được phục vụ" | Bỏ |
| "Chúng tôi luôn lắng nghe và tiếp thu ý kiến" | Nói đã sửa gì |
| "Kính gửi", "Quý khách", "Quý phụ huynh", "Trân trọng" (trên mạng xã hội, tin nhắn) | Gọi bằng tên, "anh chị", "phụ huynh" |
| "anh/chị" có gạch chéo trong tin gửi một người | Chọn "anh" hoặc "chị" |
| "Bạn đang gặp khó khăn trong việc …?" (Are you struggling with…) | Tả cảnh. (Câu hỏi đoán đặc điểm cá nhân còn bị Meta cấm trong quảng cáo) |
| "Giải pháp toàn diện cho …" | Nói mình làm việc gì |
| "Đồng hành cùng bạn" | "Mình kèm bạn 6 tuần." |
| "Trải nghiệm" (experience) | "học thử", "làm thử", "dùng thử", "ghé" |
| "Sở hữu" (own) | "có", "mua" |
| "Mang đến cho bạn …" (bring you) | Nói kết quả, bỏ chủ ngữ: "Học xong là …" |
| "Chỉ với 1.890.000đ" (for only) | "1.890.000đ" |
| "Dành riêng cho bạn" (just for you) | Bỏ, hoặc nói thật: "cho người đã dự buổi thử" |
| "Trở thành phiên bản tốt nhất của chính mình" | Nói cái làm được: "chủ trì được một buổi họp 15 phút" |
| "Đã đến lúc …" (It's time to …) | Bỏ, vào việc luôn |
| "Theo dõi để không bỏ lỡ những nội dung hữu ích" | "Phần 2 mai lên." |
| "Like, share và đăng ký kênh để ủng hộ mình" | Một việc cụ thể gắn với video |

---

## 6. Khác nhau theo nền tảng

| Nền tảng | Xưng hô hay gặp | Độ dài, nhịp | Tiểu từ, emoji | Lời mời tự nhiên | Lạc giọng khi |
|---|---|---|---|---|---|
| **Facebook cá nhân** (bật chế độ chuyên nghiệp) | mình – bạn / các chị em / anh chị; tôi – anh chị (chuyên gia 40+) | Dòng đầu đứng riêng; đoạn ngắn; kể dài được (500–1.500 chữ) nếu 3 dòng đầu giữ được người đọc trước "Xem thêm" | Vừa; :)) được | "Ai cần thì comment chữ X / nhắn riêng mình"; link ở bình luận đầu | Viết như thông cáo; "Kính gửi"; quá nhiều emoji gạch đầu dòng |
| **Nhóm Facebook** | Theo nhóm: "cả nhà", "các chị em", "anh em" | Hỏi, chia sẻ, bài tập | Thân hơn trang cá nhân | "Tài liệu mình để ở mục File của nhóm" | Vào nhóm người khác mà đăng bán ngay |
| **Trang Facebook** | Tên tiệm / tên mình, "tụi em", "bên mình" – anh chị | Gọn hơn | Ít | Nút Gửi tin nhắn | Giọng "chúng tôi" tập đoàn |
| **Messenger, inbox** | Số ít; "Dạ… ạ" với khách lớn tuổi hơn | 2–5 câu | Dày hơn bài | Bước tiếp có giờ | Kịch bản tổng đài |
| **TikTok, Reels (lời nói)** | mình – bạn / mấy bạn / mọi người; em – anh chị (người trẻ làm dịch vụ) | Hook 3 giây; câu cụt; "Phần 1, 2, 3" | Theo giọng nói thật | "Phần 2 mai lên", "link nhóm Zalo ở bio", nhắn chữ X | Đọc văn viết; "Xin chào các bạn, hôm nay mình sẽ chia sẻ…" |
| **Caption, bình luận TikTok** | Như video | 1–3 dòng; chữ thường được | Emoji làm dấu câu 😭😂🫶 (theo tuổi) | Lời mời trong caption, không trong hook | Bài bán hàng trơn |
| **Zalo một-một** | Như ngoài đời: em – chị, chị – em, tôi – anh | Ngắn; tin thoại; ảnh | "Dạ… ạ"; viết tắt nếu thân | Hẹn giờ cụ thể; QR chuyển khoản | Tin mẫu "anh/chị"; dồn tin; nhắn khuya |
| **Nhóm Zalo (lớp, học viên)** | "Cả nhà / cả lớp" – mình / thầy / cô / chị | Thông báo ngắn, ghim | Ấm, gọn | Nhắc lịch, bài tập | Văn công văn "Kính đề nghị quý phụ huynh"; bán liên tục |
| **Nhật ký Zalo** | Như Facebook cá nhân, đời hơn | Ngắn, ảnh thật | Mộc | Rất ít | Đăng bán mỗi ngày |
| **LinkedIn** | tôi – anh chị / bạn; mình – bạn (người trẻ) | Gọn, danh sách số được; ký tên được | Gần như không tiểu từ; 0–1 emoji | "Ai cần mẫu thì bình luận hoặc nhắn tôi." | "nha, nè"; bài kiểu Facebook; calque "Tôi rất vinh dự và tự hào thông báo rằng…" (Humbled and honored to announce) → "Tuần này tôi vừa xong…" |
| **Threads** | mình – mọi người; chữ thường | Một ý, ngắn, thú nhận | Như chat | Gần như không bán | Bài bán, bài dài |
| **Livestream** | mình / chị – cả nhà, mọi người; gọi tên người xem | Chào và chờ; đọc bình luận; lạc đề rồi quay lại (K6) | Theo giọng nói | "Còn ai hỏi gì nữa hông", nhắc link ở bình luận ghim | Đọc kịch bản; không gọi tên ai |
| **Email** | Như Zalo, đủ câu hơn; với doanh nghiệp: "Kính gửi anh Hùng" vẫn đúng | ≤375 tiếng; tiêu đề như thư riêng | Ít | Một việc | Tiêu đề kiểu khuyến mãi; "Re:" giả |

**Viết khác nói:** bài viết dùng giọng viết của coach; chưa từng dán bài thì giọng nói làm gọn (bỏ ờ, à, câu vấp; giữ nhịp, tiểu từ, câu cửa miệng) (§CM-VOICE 8). Kịch bản video giữ đúng giọng nói. Người Trung viết bài thường bớt tiếng địa phương, giữ 1–3 chữ; video thì để nguyên giọng.

---

## 7. Vùng miền và lứa tuổi

### 7.1 Ba giọng vùng

| | **Bắc** (Hà Nội, đồng bằng) | **Trung** (Huế, Đà Nẵng, Quảng, Nghệ Tĩnh) | **Nam** (Sài Gòn, miền Tây) |
|---|---|---|---|
| Tiểu từ cuối câu | nhé, nhỉ, đấy, thế, cơ, ạ, chứ, à, hả, ấy | nghe, hỉ, hè, rứa, tề, nờ (Nghệ), ạ | nha, nè, á, hen, nghen, ha, hông, đó, luôn, ạ |
| Hỏi | sao, thế nào, à, hả, không | răng, mô, chi, rứa, hả | sao, hông, hả, vậy, ta |
| Chỉ trỏ | thế, thế này, này, kia, ấy | rứa, ri, ni, tê, nớ, chừ (bây giờ) | vậy, nè, đó, bữa, giờ |
| Chữ thường ngày | bảo, xem, vào, ngã, cốc, bát, hôm | nói, coi, vô, chén, ly, bữa | kêu, coi, vô, té, ly, chén, bữa, ổng, bả, chỉ (chị ấy) |
| Chữ nối đặc trưng | thế là, thế nên, thế mà, cơ mà, đã thế lại còn | rứa là, rứa mà, răng mà | vậy là, thành ra, vậy mà, ai dè, tới chừng |
| Nhấn, khen | lắm, quá, ghê, cực, ối giời | lắm, quá, dễ sợ | dữ lắm, quá trời, dễ sợ, thiệt, hết sảy |
| Thán từ | ối giời ơi, khổ thân, chết thật, thôi chết | trời đất ơi, mạ ơi | trời ơi, má ơi, thấy mồ, mèn ơi |
| Tự xưng (thân) | mình, tớ (trẻ), chị, anh | tui, mình | tui, mình, tụi mình |

**Luật cho máy:**
1. **Một vùng một bài.** Không "đấy" trong bài giọng Nam; không "hông" trong bài giọng Bắc; không vừa "nhé" vừa "nha" trừ khi bài thật của coach trộn như vậy (người Bắc trẻ hay trộn). Đổi vùng là đổi cả **chữ nối** ("thế là" ↔ "vậy là", "rứa là") và chữ thường ngày ("bố mẹ" ↔ "ba mẹ", "bát" ↔ "chén", "nghìn" ↔ "ngàn"), không chỉ tiểu từ.
2. **Giọng Trung khi viết:** bớt tiếng địa phương, giữ 1–3 chữ ("rứa", "chừ", "nghe", "hỉ") để người vùng khác vẫn đọc trôi. Video thì để nguyên giọng nói.
3. **Giọng Nam khi viết:** "hông", "thiệt", "vô", "nè" giữ được; chính tả nói ("dzậy", "hông dám đâu") chỉ khi coach tự viết vậy.
4. **Không đoán vùng khi không có bằng chứng.** Không rõ thì viết trung tính: chữ chung cả nước ("đó", "thôi", "luôn", "nhé" thưa ở câu dặn; "nhé" là chữ trên báo, người Nam đọc vẫn quen), không "nè, hông, nhỉ, đấy, rứa". Đừng bỏ hết tiểu từ: câu trơn không tiểu từ nào lại nghe như bản dịch (X3).
5. **Tiếng địa phương không phải trò cười.** Không rắc "rứa, mô, tê" dày đặc cho có màu: đó là giễu nhại, người miền Trung đọc sẽ phật ý.

### 7.2 Lứa tuổi

| | **40+** | **25–39** (văn phòng, chủ shop trẻ) | **Gen Z** (dưới 25) |
|---|---|---|---|
| Câu | Đủ chữ, ít viết tắt, đoạn dài hơn | Ngắn, xuống dòng nhiều | Rất ngắn, chữ thường đầu câu, có khi không dấu câu |
| Xưng hô | anh chị, cô chú, các chị em, em – anh chị; "Dạ… ạ" khi nhắn | mình – bạn, mình – mấy bạn | mình – mn, tui – mấy bà (nữ, đùa), tớ – cậu |
| Chữ Anh | Ít; chữ đã Việt hóa: sale, ship, online | content, deadline, booking, feedback, KPI | flex, red flag, slay, vibe |
| Thành ngữ, tục ngữ | Dùng tự nhiên: "mất bò mới lo làm chuồng", "tiền nào của nấy", "thợ may ăn giẻ" | Thỉnh thoảng, hay đùa ngược | Gần như không, trừ khi chế lại |
| Emoji | Thưa: 🙏 😄 ❤️ | 😅 ❤️ 👉 vừa phải, :)) | 😭 🫶 💀 ✨, =))) |
| Tiếng lóng | Không | Nhẹ, đã phổ biến: "toang", "cạn lời", "xỉu" | "khum", "j z tr", "u là trời", "đỉnh nóc kịch trần" (đi rất nhanh) |
| Cảm xúc | Nói qua việc làm | "quê", "đứng hình", "cạn lời", "nản" | "xỉu ngang", "muối mặt", "khóc thét" |

**Luật cho máy:** tiếng lóng chỉ dùng khi (a) coach tự dùng trong lời xả hay bài dán **và** (b) khách cùng tuổi đó. Tối đa một chữ lóng mỗi bài. Không bao giờ cho coach 40+ nói giọng Gen Z để "bắt trend". Tiếng lóng của AI thường lỗi thời nhiều năm (wf2 §5). Gọi khách 40+ là "bạn" là lỗi văn hóa hay gặp; dùng anh chị, cô chú.

**Lệch tuổi giữa coach và khách:**
- **Coach 40+, khách trẻ hơn:** giữ giọng của coach, đừng "trẻ hóa": "chị – các em", "cô – các con", "anh – em", hoặc "mình – các bạn"; câu đủ chữ, ít lóng, emoji thưa. Không "ạ" với khán giả nhỏ tuổi hơn. Tự trào về tuổi thì được ("chị già rồi, nói chậm, các em chịu khó").
- **Coach trẻ, khách 40+:** "em – anh chị", "Dạ… ạ" khi nhắn; không "mn", không lóng, không "bạn"; chữ Anh chỉ chữ đã quen (sale, ship, online).
- **Khách trộn tuổi** (nhóm Facebook, live): "mình – mọi người" hoặc "mình – anh chị"; câu trả lời riêng thì đổi theo người hỏi.

### 7.3 Giao tiếp kiểu Việt: tế nhị, giữ thể diện, ghét nổ

- **Tế nhị, nói giảm nói tránh.** Văn hóa ngữ cảnh cao, giữ thể diện cho nhau. Vì vậy lời mời tiếng Việt mềm hơn tiếng Anh: "ai cần thì nhắn", "cứ coi lịch đã", "chưa cần quyết liền".
- **"Ngại"** là cảm xúc riêng: ngần ngừ vì nghĩ cho người kia. Khách "ngại hỏi giá", coach "ngại chào". Viết trúng chữ này là chạm đúng chỗ.
- **Khiêm, ghét khoe.** Thành tích đặt vào khách ("Thắm làm đều nhất nên bán hết sớm nhất"), kèm chữ giảm nhẹ ("cũng được", "tạm ổn", "may là"). Khoe doanh thu, ảnh chuyển khoản làm cả bài là "nổ"; một con số thật đặt sau chuyện để làm bằng chứng thì được.
- **Nói thẳng chuyện tiền thì được tin,** nếu là thẳng về *mình*. Thẳng kiểu ép người khác thì mất tin.
- **"Dạ"** mở đầu khi trả lời người lớn hơn hoặc khách; "ạ" cuối câu. Một "Dạ" và một "ạ" mỗi tin là đủ; "Dạ vâng ạ" (Bắc), "Dạ, dạ" (Nam). Thiếu "Dạ… ạ" khi nhắn khách là thô.

---

## 8. Ba mươi chín cặp trước / sau

Nhân vật hư cấu (bảng ở mục 0). Số, chính sách (hoàn tiền, chụp lại, số chỗ) trong ví dụ là bịa; khi máy viết cho coach thật, chỉ dùng điều coach đã nói là thật. Mỗi cặp ghi: chỗ dùng · coach · cặp xưng hô · vùng. Dòng "Sửa gì" là lý do, để người viết học cách nghĩ, không phải để chép.

### A. Mở bài, hook

**A1 · Câu mở bài Facebook · cô Nga · mình – các chị · Bắc**
- Trước: "Bạn có biết rằng 80% người làm bánh tại nhà đang định giá sai sản phẩm của mình? Hãy cùng mình khám phá nguyên nhân nhé!"
- Sau: "Tuần trước có chị nhắn mình: 'Cô ơi em bán cả tháng mà vẫn còn nợ tiền bơ tiền trứng.' Mình nhìn bảng giá của chị ấy là hiểu ngay."
- Sửa gì: bỏ "Bạn có biết rằng" và con số không nguồn; mở bằng câu khách nhắn nguyên văn (khách gọi "cô", cô vẫn xưng "mình" với các chị đọc bài: lời trích giữ xưng hô của người nói); "Hãy cùng khám phá" thành một câu kể có người, có giờ.

**A2 · Hook TikTok 3 giây · Hiếu · Hiếu – anh chị · Trung**
- Trước: "Xin chào các bạn, hôm nay mình sẽ hướng dẫn các bạn cách vệ sinh máy lạnh tại nhà một cách đơn giản và hiệu quả."
- Sau: "Máy lạnh chạy cả đêm mà không mát? Khoan gọi thợ, anh chị coi cái này đã."
- Sửa gì: video ngắn vào thẳng nỗi khổ; bỏ lời chào YouTube, bỏ "một cách đơn giản và hiệu quả"; xưng hô đúng kênh ("anh chị", không "các bạn").

**A3 · Câu mở bài · Khang · mình – mấy bạn · Nam**
- Trước: "Trong cuộc sống hiện đại bận rộn ngày nay, việc duy trì thói quen chạy bộ là vô cùng quan trọng đối với sức khỏe của chúng ta."
- Sau: "5 giờ sáng, công viên Gia Định đông nhất là mấy ông chú chạy chậm rì. Mà bền nhất cũng là mấy ổng."
- Sửa gì: bỏ mở bài nghị luận ("Trong cuộc sống hiện đại", "việc duy trì", "vô cùng quan trọng", "chúng ta"); mở bằng giờ, chỗ, người; "mấy ổng" giọng Nam.

**A4 · Câu mở bài · cô Lan · mình – anh chị phụ huynh · Bắc**
- Trước: "Là một giáo viên với hơn 20 năm kinh nghiệm, tôi hiểu rõ những áp lực mà các bậc phụ huynh đang phải đối mặt trong kỳ thi vào lớp 10."
- Sau: "Tối thứ Sáu, chín rưỡi, mẹ một bạn lớp 9 gọi cho mình, giọng run run: 'Cô ơi cháu làm đề lần nào cũng 6 điểm, em sốt ruột quá.'"
- Sửa gì: bỏ "Là một…, với hơn 20 năm kinh nghiệm" (dịch "As a teacher with over…"); bỏ "các bậc phụ huynh đang phải đối mặt"; mở bằng giờ + giọng nói + câu nguyên văn.

**A5 · Câu mở bài · Ngọc · mình – mọi người · Bắc, Gen Z**
- Trước: "Bạn đã bao giờ tự hỏi tại sao mình học tiếng Anh nhiều năm mà vẫn không thể giao tiếp một cách tự tin?"
- Sau: "Kể mọi người nghe pha muối mặt nhất hồi năm hai của mình."
- Sửa gì: bỏ hook dịch "Have you ever wondered"; thú nhận mở chuyện; một chữ lóng nhẹ, đúng tuổi ("muối mặt").

### B. Nối ý, chuyển ngoặt

**B1 · Nối hai ý · chị Diễm · chị – các mẹ · Nam**
- Trước: "Cho bé tự bốc giúp bé phát triển kỹ năng vận động. Bên cạnh đó, nó còn giúp bé hứng thú hơn với bữa ăn. Tuy nhiên, các mẹ cần chú ý an toàn."
- Sau: "Cho bé tự bốc thì tay bé khéo hơn, mà bé cũng ham ăn hơn. Có điều mẹ phải ngồi kế bên nha, đừng bỏ đi đâu."
- Sửa gì: "Bên cạnh đó", "Tuy nhiên" thành "mà", "có điều"; bỏ "giúp bé phát triển kỹ năng"; "nó" chỉ ý thì bỏ; tiểu từ ở câu dặn.

**B2 · Chỗ ngoặt · chị Hồng · chị – em · Nam**
- Trước: "Khoảnh khắc ấy, tôi chợt nhận ra rằng mình đã sai lầm khi chọn học khóa rẻ nhất."
- Sau: "Qua ngày thứ hai hoa héo rũ, chị phải đền nguyên giỏ. Lúc đó chị mới biết cái mắc nhất là hoa hư chứ hổng phải học phí."
- Sửa gì: ngoặt bằng việc xảy ra và đồ vật ("hoa héo rũ", "đền nguyên giỏ"), rồi "Lúc đó… mới biết… chứ hổng phải…"; bỏ "Khoảnh khắc ấy, chợt nhận ra rằng".

**B3 · Chuyển thời gian · Phát · mình – anh chị · Nam**
- Trước: "Tua nhanh đến 2 năm sau, tôi đã xây dựng thành công kênh TikTok với hàng chục nghìn người theo dõi."
- Sau: "Hai năm sau, kênh của quán có bốn chục ngàn người theo dõi. Má vẫn la mình cầm điện thoại trong bếp, mà la nhỏ hơn rồi."
- Sửa gì: "Tua nhanh" thành "Hai năm sau"; số cụ thể thay "hàng chục nghìn"; thêm một chi tiết đời để khỏi "nổ".

**B4 · Giải thích lại · Hoàng · mình – bạn · Bắc**
- Trước: "Nói chậm giúp bạn kiểm soát hơi thở. Điều này có nghĩa là giọng của bạn sẽ trở nên ổn định hơn."
- Sau: "Nói chậm thì thở sâu được, thở sâu thì giọng hết run."
- Sửa gì: "Điều này có nghĩa là", "giúp bạn", "sẽ trở nên", "của bạn" thành một chuỗi "thì" nối vòng.

**B5 · Đối lập · thầy Tùng · thầy – anh chị · Trung**
- Trước: "Nhiều phụ huynh cho con học bơi ở hồ, trong khi họ không biết rằng bơi ở biển hoàn toàn khác."
- Sau: "Nhiều nhà cho con học bơi ở hồ rồi yên tâm. Mà ra biển là chuyện khác, sóng rút dưới chân là con hoảng liền."
- Sửa gì: "trong khi họ không biết rằng" thành "mà"; "hoàn toàn khác" thành một chi tiết thấy được.

### C. Dẫn lời, bài học, kết bài

**C1 · Dẫn lời · Quân · em – anh chị · Bắc**
- Trước: "Chị chủ shop chia sẻ rằng chị ấy cảm thấy rất thất vọng vì khách phàn nàn về màu sắc sản phẩm."
- Sau: "Chị chủ shop nhắn em: 'Khách bảo túi ngoài đời nâu hơn trên ảnh, đòi trả hàng em ạ.'"
- Sửa gì: "chia sẻ rằng… cảm thấy rất thất vọng" thành dẫn lời nguyên văn bằng "nhắn"; giữ chữ của người nói.

**C2 · Bài học · Khang · mình – mấy bạn · Nam**
- Trước: "Bài học rút ra ở đây là: sự kiên trì chính là chìa khóa dẫn đến thành công trong chạy bộ."
- Sau: "Chạy nhanh ba bữa, nằm nhà ba tuần."
- Sửa gì: bài học thành một câu hai vế lặp số; bỏ "Bài học rút ra", "sự kiên trì", "chìa khóa dẫn đến thành công".

**C3 · Bài học trong miệng người khác · chị Mai · chị – mọi người · Nam**
- Trước: "Hãy luôn nhớ rằng thành công không đến từ may mắn mà đến từ sự chăm chỉ mỗi ngày."
- Sau: "Má chị hồi xưa bán xôi, hay nói: 'Dậy sớm hơn người ta một tiếng là bán hơn người ta một mâm.'"
- Sửa gì: bỏ giảng đạo ("Hãy luôn nhớ rằng", "thành công không đến từ… mà đến từ"); đặt bài học vào miệng má, có hình ảnh đời.

**C4 · Kết bài Facebook · cô Nga · mình – các chị · Bắc**
- Trước: "Hy vọng bài viết hữu ích với các bạn. Đừng quên để lại bình luận và chia sẻ cho những người cần nhé!"
- Sau: "Chị nào đang bán bánh mà chưa tính tiền điện chạy lò vào giá thì tối nay ngồi cộng thử nhé, cộng xong là biết."
- Sửa gì: kết bằng một việc nhỏ cho đúng người ("Chị nào… thì tối nay…"); bỏ câu kết rỗng và lời giục tương tác.

**C5 · Kết bài video · Ngọc · mình – mọi người · Bắc**
- Trước: "Tóm lại, để cải thiện khả năng nói tiếng Anh, bạn cần luyện tập thường xuyên. Chúc các bạn thành công!"
- Sau: "Ai sắp đi phỏng vấn thì tối nay thử nói to ba câu về mình thôi nhé, sai cũng cứ nói."
- Sửa gì: bỏ "Tóm lại", "Để…, bạn cần…", "Chúc các bạn thành công"; một việc nhỏ có số, có giờ.

### D. Kịch bản video nói

**D1 · Đoạn giữa video · Hiếu · Hiếu – anh chị · Trung**
- Trước: "Sau khi tiến hành tháo lưới lọc, chúng ta sẽ thực hiện việc vệ sinh bằng nước sạch. Điều này giúp máy hoạt động hiệu quả hơn."
- Sau: "Tháo cái lưới ra, xả nước cho sạch bụi, phơi khô rồi gắn lại. Mười phút là máy mát rượi."
- Sửa gì: bỏ "tiến hành", "thực hiện việc", "Điều này giúp", "chúng ta"; chuỗi việc một hơi nối bằng dấu phẩy; kết quả bằng con số và chữ nhấn ("mát rượi").

**D2 · Đoạn giữa video · Phát · mình – anh chị · Nam**
- Trước: "Để có thể quay được video đẹp trong bếp, bạn cần phải đặt điện thoại ở vị trí phù hợp và đảm bảo rằng ánh sáng đầy đủ."
- Sau: "Muốn quay trong bếp mà đẹp thì đứng quay mặt ra cửa sổ, để điện thoại ngang ngực. Vậy thôi, khỏi mua đèn."
- Sửa gì: "Để có thể…, bạn cần phải…" thành "Muốn… thì…"; "đảm bảo rằng ánh sáng đầy đủ" thành chỉ dẫn thấy được; câu cụt "Vậy thôi".

**D3 · Câu chốt video · Hoàng · mình – bạn · Bắc**
- Trước: "Nếu thấy video hữu ích, đừng quên like, share và đăng ký kênh để không bỏ lỡ những video tiếp theo nhé!"
- Sau: "Bạn nào sắp phải lên nói gì đấy thì nhớ, run là bình thường, chỉ cần câu đầu chậm lại thôi."
- Sửa gì: thay lời xin like bằng một câu cho đúng người đang sợ; "nhớ… thôi" là lời dặn kiểu Việt.

### E. Lời mời (CTA)

**E1 · Cuối bài Facebook · Vy · mình – bạn · Bắc**
- Trước: "Bạn đã sẵn sàng nâng cao kỹ năng Excel và tiết kiệm hàng giờ làm việc mỗi ngày chưa? 🚀 Hãy comment "GUIDE" ngay bên dưới để nhận bộ tài liệu độc quyền hoàn toàn miễn phí! ✨"
- Sau: "Mình có làm sẵn một file mẫu báo cáo tuần, mở ra điền số là xong. Ai cần thì comment chữ TĂNG CA, mình gửi qua tin nhắn. Ngại comment thì nhắn riêng mình chữ đó cũng được nhé."
- Sửa gì: bỏ "Bạn đã sẵn sàng… chưa?"; nói rõ quà là gì; từ khóa tiếng Việt gọi đúng nỗi khổ; thêm đường nhắn riêng; bỏ "độc quyền", "hoàn toàn miễn phí", 🚀✨; một "nhé" cuối, đúng giọng Bắc.

**E2 · Caption TikTok · Phát · mình – anh chị · Nam**
- Trước: "Theo dõi để không bỏ lỡ những mẹo marketing hữu ích tiếp theo! 💡🔥 #marketing #tiktok #kinhdoanh"
- Sau: "Quán hẻm, điện thoại cũ, quay vẫn ngon nha anh chị 😄 Phần 2 mình chỉ chỗ đặt điện thoại lúc đứng bếp, mai lên. #quanan #quayvideo"
- Sửa gì: nói phần 2 có gì và khi nào; gọi đúng người xem; một emoji mộc; hashtag không dấu, đúng ngách; bỏ chữ "marketing" chủ quán không nói.

**E3 · Lời mời buổi nói chuyện, nhóm Zalo phụ huynh · thầy Tùng · thầy – anh chị · Trung**
- Trước: "📢 THÔNG BÁO QUAN TRỌNG 📢 Kính mời Quý phụ huynh tham gia buổi hội thảo trực tuyến MIỄN PHÍ với chủ đề "An toàn dưới nước cho trẻ". Số lượng có hạn, đăng ký ngay để không bỏ lỡ cơ hội!"
- Sau: "Anh chị phụ huynh ơi, hè ni nhiều nhà cho con đi biển. Tối thứ Năm 8 giờ thầy nói chuyện qua Zalo 30 phút: con mới biết bơi thì ra biển cần dặn con mấy câu gì. Không thu phí. Anh chị nhắn thầy chữ BIỂN để thầy gửi link, ai bận thì thầy gửi bản ghi lại sau."
- Sửa gì: bỏ văn công văn, viết hoa cả câu; giờ, thời lượng, nội dung cụ thể; "Số lượng có hạn" giả thành thứ thật có ích (bản ghi); "thầy" với phụ huynh; một chữ Trung ("ni").

**E4 · Câu chốt video · Quân · em – anh chị · Bắc**
- Trước: "Nếu thấy video hữu ích, đừng quên like, share và follow kênh để ủng hộ mình nhé! Hẹn gặp lại các bạn trong những video tiếp theo!"
- Sau: "Anh chị nào đang bán mà ảnh chụp bằng điện thoại cứ bị tối thì nhắn em chữ ẢNH TỐI, em gửi cái sơ đồ đặt đèn một trang, đèn bàn ở nhà cũng làm được ạ."
- Sửa gì: một việc gắn đúng nỗi khổ; bản trước trôi xưng hô ("mình" rồi "các bạn" trong khi kênh xưng "em – anh chị"); món quà nhỏ, cụ thể; "ạ" một lần.

### F. Trả lời tin nhắn

**F1 · Hỏi giá qua inbox · Trâm · em – chị · Nam**
- Khách: "Giá sơn gel bn vậy shop"
- Trước: "Cảm ơn bạn đã quan tâm đến dịch vụ của chúng tôi! 😊 Để được tư vấn chi tiết về bảng giá và các chương trình ưu đãi, vui lòng để lại số điện thoại, nhân viên sẽ liên hệ lại trong thời gian sớm nhất."
- Sau: "Dạ chị, sơn gel bên em 150k, vẽ thêm thì từ 30k một ngón nha chị. Chị tính ghé bữa nào để em xếp thợ, cuối tuần tiệm hơi đông á."
- Sửa gì: giá ở câu đầu; "Dạ chị", "em" (không "chúng tôi – bạn"); không đòi số điện thoại khi người ta chỉ hỏi giá; một câu hỏi lại có ích cho cả hai; "á", "bữa" giọng Nam.

**F2 · "Lớp này có hợp với em không?" · Vy · mình – bạn · Bắc**
- Trước: "Chào bạn! Khóa học được thiết kế dành riêng cho những ai mong muốn nâng cao kỹ năng Excel một cách toàn diện. Với lộ trình bài bản cùng đội ngũ giảng viên giàu kinh nghiệm, chắc chắn bạn sẽ đạt được kết quả như mong đợi!"
- Sau: "Chào Hà, cho mình hỏi lại một chút nhé: mỗi tuần Hà hay phải làm báo cáo gì, mất khoảng bao lâu? Lớp mình tập đúng việc gom số từ mấy file về một bảng. Nếu Hà cần học VBA hay làm dashboard thì lớp này không hợp đâu, mình chỉ Hà chỗ khác."
- Sửa gì: hỏi trước khi bán; nói thật khi không hợp; bỏ "được thiết kế dành riêng", "một cách toàn diện", "chắc chắn"; Vy dạy một mình nên "đội ngũ giảng viên" là nói sai; "VBA, dashboard" là chữ dân văn phòng thật dùng.

**F3 · Khách nói "để chị suy nghĩ thêm" · Quân · em – chị · Bắc**
- Trước: "Dạ vâng ạ! Chị cứ thoải mái suy nghĩ nhé ạ. Tuy nhiên, chương trình ưu đãi chỉ áp dụng đến hết ngày hôm nay, chị nên nhanh chóng đưa ra quyết định để không bỏ lỡ cơ hội ạ!"
- Sau: "Dạ vâng, chị cứ thong thả ạ. Em gửi lại bảng giá một trang ở trên để chị xem lúc rảnh. Giá này em giữ đến hết tháng 11. Chị muốn xem em chụp đồ bên chị thế nào thì gửi em 1 món, em chụp thử 2 tấm, không lấy tiền."
- Sửa gì: bỏ "Tuy nhiên… nhanh chóng… không bỏ lỡ" (vừa dí vừa gấp giả); hạn có ngày thật; một bước nhỏ giảm rủi ro cho khách; "ạ" vừa đủ (bản trước có bốn "ạ").

**F4 · Nhắn lại khi khách đã xem mà chưa trả lời · Phát · em – anh (khách lớn tuổi hơn) · Nam**
- Trước: "Anh ơi, em thấy anh đã xem tin nhắn rồi mà sao chưa phản hồi em ạ? Anh còn quan tâm đến khóa học không ạ? Nếu anh không đăng ký thì cho em xin lý do để em cải thiện ạ."
- Sau: "Dạ anh, em nhắn lần này nữa thôi nha: lớp quay video tại quán khai giảng thứ Hai tuần sau, còn nhận thêm 2 quán. Giờ chưa tiện thì anh cứ để đó, mấy mẹo quay em vẫn đăng đều trên kênh, anh coi miễn phí ạ."
- Sửa gì: bỏ "em thấy anh đã xem" (bị theo dõi; `email-zalo.md` EM7); bỏ xin lý do; nói rõ đây là lần cuối; chừa đường lui. Phát xưng "mình" trên kênh, sang tin riêng với khách lớn tuổi thì đổi "em" (mục 4.4 luật 4).

**F5 · Khách chê đắt · Vy · mình – bạn · Bắc**
- Trước: "Dạ, học phí của chúng tôi hoàn toàn xứng đáng với chất lượng mà khóa học mang lại. Đây là một khoản đầu tư cho bản thân mà bạn sẽ không bao giờ hối tiếc!"
- Sau: "Đúng là 1.890.000đ không phải ít đâu Hà. Số đó là 8 buổi tối, buổi nào mình cũng mở file của từng bạn ra sửa, chứ không phải video quay sẵn. Nếu giờ chưa tiện thì Hà lấy file mẫu báo cáo tuần ở bài ghim dùng trước nhé, miễn phí."
- Sửa gì: nhận phần đúng của khách trước; nói giá mua được gì; cho một lối rẻ hơn; bỏ "khoản đầu tư… không bao giờ hối tiếc" và "chúng tôi".

### G. Tin Zalo

**G1 · Tin chào khi khách vừa kết bạn · Vy · mình – bạn · Bắc**
- Trước: "Xin chào! 🎉 Cảm ơn bạn đã kết bạn với Vy. Vy rất vui được đồng hành cùng bạn trên hành trình chinh phục Excel! Hãy cùng nhau khám phá những bí quyết giúp bạn làm việc hiệu quả hơn mỗi ngày nhé! 💪✨"
- Sau: "Chào Hà, Vy đây. File mẫu báo cáo tuần mình để ở dưới nhé, Hà mở sheet 'Tổng' trước, điền thử số tuần này vào xem. Mình hỏi một câu thôi: báo cáo của Hà đang gom từ mấy file? (Zalo này mình chỉ dùng để gửi tài liệu và nhắc lịch lớp. Muốn dừng nhận tin, nhắn DỪNG.)"
- Sửa gì: vào việc ngay, chỉ đúng chỗ mở; một câu hỏi; dòng mục đích và dòng dừng; bỏ "đồng hành", "hành trình", "khám phá", "bí quyết".

**G2 · Nhắc lịch trong nhóm Zalo lớp · thầy Tùng · thầy – anh chị · Trung**
- Trước: "THÔNG BÁO: Buổi học sẽ diễn ra vào lúc 17h00 ngày mai. Kính đề nghị Quý phụ huynh nhắc nhở các em mang đầy đủ dụng cụ và có mặt đúng giờ. Trân trọng cảm ơn!"
- Sau: "Anh chị ơi, mai 5 giờ chiều lớp mình học ở hồ như cũ. Mai các con tập úp mặt thổi bong bóng nên anh chị cho con mang kính bơi giúp thầy, con nào chưa có thì báo thầy, thầy cho mượn. Cho con ăn nhẹ trước 4 giờ thôi nghe."
- Sửa gì: bỏ văn công văn; nói lý do (mai tập gì); gỡ khó cho nhà chưa có kính; một chữ "nghe" giọng Trung ở cuối.

**G3 · Báo tin không vui · Quân · em – anh (chủ shop, khoảng 40) · Bắc**
- Trước: "Kính gửi anh, chúng tôi rất tiếc phải thông báo rằng do một số sự cố ngoài ý muốn, tiến độ giao ảnh sẽ bị chậm trễ. Rất mong anh thông cảm cho sự bất tiện này."
- Sau: "Dạ anh Hùng, em Quân đây ạ. Bộ ảnh túi da em hẹn giao chiều nay thì em phải lùi sang trưa mai anh ạ: 6 tấm nền trắng bị ám vàng, em chụp lại cho đều màu chứ không muốn gửi anh ảnh sửa tạm. 2 tấm xong rồi em gửi anh ở trên, anh cần gấp thì cứ lên bài trước. Em xin lỗi anh."
- Sửa gì: lý do thật, cụ thể; giờ mới rõ ràng; bù ngay bằng 2 tấm xong trước; "Em xin lỗi anh" thay "sự bất tiện này"; bỏ "Kính gửi", "chúng tôi".

### H. Trả lời bình luận

**H1 · Hỏi giá dưới bài · Vy**
- Bình luận: "Học phí bao nhiêu vậy c"
- Trước: "Bạn check inbox giúp mình nhé! 📩"
- Sau: "1.890.000đ cho 8 buổi nhé em, lịch học chị nhắn riêng cho em rồi đấy."
- Sửa gì: giá ngay chỗ người ta hỏi, ai đọc cũng thấy; người hỏi gọi Vy là "c" (chị) nên Vy đáp "chị – em" là tự nhiên, đáp "bạn" nghe như đẩy ra xa.

**H2 · Chê thẳng · Phát**
- Bình luận: "Học xong toàn lý thuyết, về quay vẫn dở"
- Trước: "Cảm ơn anh đã góp ý! Chúng tôi luôn lắng nghe và tiếp thu mọi ý kiến đóng góp của học viên để ngày càng hoàn thiện hơn ❤️"
- Sau: "Anh nói trúng một chỗ nè: buổi 2 khóa trước mình nói lý thuyết dài thiệt. Khóa này buổi đó mình cắt còn 15 phút, còn lại cầm điện thoại quay ngay tại quán. Anh học khóa nào, anh nhắn riêng mình, mình coi lại clip của anh rồi chỉ cụ thể."
- Sửa gì: nhận phần đúng, nói đã đổi gì; mời xem bài thật của người chê; bỏ câu tổng đài.

**H3 · Nghi "lùa gà" · Vy**
- Bình luận: "Lại lùa gà à 🙂"
- Trước: "Chúng tôi là đơn vị đào tạo uy tín với hàng nghìn học viên thành công. Mong bạn tìm hiểu kỹ trước khi đưa ra bình luận thiếu thiện chí."
- Sau: "Hỏi thế là phải, giờ khóa online kiểu đấy nhiều thật. Học phí mình để công khai ở bài ghim, học 2 buổi đầu thấy không hợp thì mình hoàn đủ. Có 3 bạn khóa trước đồng ý cho người hỏi nhắn trực tiếp, cần thì mình gửi tên."
- Sửa gì: không tự ái, không phản công; đưa ba thứ kiểm được; bỏ "uy tín", "hàng nghìn học viên" (không kiểm được). "🙂" ở đây là cười mỉa: đọc đúng mới đáp đúng.

**H4 · Phụ huynh kể chuyện · thầy Tùng**
- Bình luận: "Năm ngoái con em suýt đuối ở biển, giờ nhớ lại vẫn run"
- Trước: "Cảm ơn chị đã chia sẻ câu chuyện đáng nhớ này! Chúc chị và bé luôn bình an và hạnh phúc! ❤️❤️❤️"
- Sau: "Đọc mà thầy cũng thót tim. Lúc đó con mấy tuổi chị? Mấy bé nhỏ hay hoảng nhất lúc sóng rút dưới chân, tuần sau thầy quay riêng một clip chỗ ni cho phụ huynh coi."
- Sửa gì: đáp đúng cảm xúc bằng chữ mộc ("thót tim"); hỏi một câu; biến chuyện thành việc có ích, không nêu tên.

### I. Câu trong bài bán

**I1 · Câu mở bài bán · Vy · Bắc**
- Trước: "🚀 CHÍNH THỨC RA MẮT KHÓA HỌC EXCEL THỰC CHIẾN – BỨT PHÁ HIỆU SUẤT, LÀM CHỦ CÔNG VIỆC! 🔥 Chương trình đào tạo toàn diện giúp bạn trở thành phiên bản chuyên nghiệp nhất của chính mình!"
- Sau: "Mình mở lớp Báo Cáo Gọn khóa 4. 8 buổi tối thứ Ba và thứ Năm, 20 bạn. Học xong, báo cáo tuần gom từ mấy file về một bảng chỉ mất 15 phút, khỏi ngồi cả buổi chiều. Học phí 1.890.000đ."
- Sửa gì: bỏ viết hoa cả câu, tên lửa, "thực chiến", "bứt phá", "phiên bản… của chính mình"; bốn câu ngắn nói đủ: lớp gì, lịch, mấy người, học xong làm được gì, giá.

**I2 · Câu số chỗ · Vy · Bắc**
- Trước: "⚠️ CHỈ CÒN 3 SUẤT CUỐI CÙNG DÀNH CHO NGƯỜI HỮU DUYÊN! Giá sẽ tăng gấp đôi vào 0h đêm nay. Nhanh tay kẻo lỡ!"
- Sau: "Còn 3 chỗ. Lớp chỉ nhận 20 bạn vì buổi nào mình cũng mở file của từng người ra sửa. Đăng ký đóng 23h59 thứ Sáu này, khóa sau chắc tầm tháng 3."
- Sửa gì: giới hạn có lý do thật; hạn có ngày; nói khóa sau để gỡ sợ lỡ; bỏ "hữu duyên", "gấp đôi lúc 0h", "nhanh tay".

**I3 · Câu giá · Trâm · Nam**
- Trước: "Giá chỉ từ 99k – ưu đãi cực sốc dành riêng cho bạn! 💅 Inbox ngay để nhận báo giá chi tiết!"
- Sau: "Bảng giá ở ảnh 2 luôn nha mấy chị: sơn gel 150k, đắp bột 250k, tháo móng cũ 30k. Thứ Ba, thứ Tư tiệm vắng, ghé không cần hẹn. Cuối tuần thì nhắn tiệm trước giùm em."
- Sửa gì: giá công khai từng món; thêm một tin có ích (ngày vắng); bỏ "chỉ từ", "cực sốc", "dành riêng cho bạn", "inbox để nhận báo giá"; "giùm em", "mấy chị" giọng Nam.

### J. Máy nói với coach

**J1 · Máy trả lời khi coach nhờ viết caption · coach gọi máy là "em" · chị Hồng**
- Trước: "Chắc chắn rồi! Dưới đây là 3 mẫu caption tuyệt vời dành cho bạn. Hy vọng những gợi ý này sẽ hữu ích! Bạn có muốn tôi viết thêm phiên bản cho TikTok không?"
- Sau: "Dạ em viết 3 bản, chị chọn nha: … Cần bản ngắn cho TikTok thì chị nói em."
- Sửa gì: đúng cặp máy – coach ("em – chị"); bỏ "Chắc chắn rồi", "Dưới đây là", "Hy vọng… hữu ích", "Bạn có muốn tôi…"; ngắn, vào việc.

**J2 · Máy nhắc coach một chỗ lệch · coach gõ kiểu bạn thân "t/m"**
- Trước: "Lưu ý: Câu thứ 3 trong bài có thể chưa phù hợp với giọng văn của bạn. Bạn có thể cân nhắc chỉnh sửa để đảm bảo tính nhất quán."
- Sau: "Câu 3 chưa giống giọng lắm, chữ 'tối ưu' ngoài đời đâu có nói. Đổi thành 'làm cho gọn' nhé?"
- Sửa gì: bỏ nhãn "Lưu ý:", "có thể cân nhắc", "đảm bảo tính nhất quán"; nói đúng chữ nào lệch và đổi thành gì; không đáp tao – mày, không "Dạ… ạ", bớt xưng hô (không gọi lại "bạn" cho khỏi xa cách), giữ thân và thẳng.

### K. Sáu cặp ngắn (dùng làm few-shot)

| Chỗ | Văn AI | Văn người |
|---|---|---|
| Mở | "Bạn có bao giờ tự hỏi tại sao khách rời bỏ bạn sau buổi đầu tiên? Hôm nay hãy cùng mình khám phá nguyên nhân." | "Tuần rồi có ba khách làm xong buổi đầu là mất hút. Mình gọi lại hỏi từng người. Nghe xong hơi quê." |
| Ngoặt | "Khoảnh khắc đó, tôi chợt nhận ra rằng mình đã sai lầm trong suốt thời gian qua." | "Đọc tới đó chị mới biết, ba năm nay chị làm ngược." |
| Nối | "Tuy nhiên, bên cạnh những lợi ích đó, phương pháp này cũng tồn tại một số hạn chế nhất định." | "Có điều cách này cũng có cái dở: mất công lắm." |
| Dẫn lời | "Cô ấy chia sẻ rằng cô ấy cảm thấy rất lo lắng về tài chính gia đình." | "Chị ấy bảo: 'Em sợ cuối tháng lắm anh ạ.'" |
| Bài học | "Bài học rút ra ở đây là: sự kiên trì chính là chìa khóa dẫn đến thành công." | "Ngày nào tập mười phút, vẫn hơn tuần tập một bữa hai tiếng." |
| Kết | "Hy vọng bài viết hữu ích. Đừng quên để lại bình luận và chia sẻ cho những người cần nhé!" | "Ai đang bị y vậy thì tuần này thử đúng một việc đó thôi, xong kể mình nghe." |

Ví dụ "trước" nào được đưa vào `locales/vn/examples.md` thì dòng đó cần `<!-- lint-ok:E141 -->` (lint E141 quét file ví dụ).

---

## 9. Phép thử: đọc to, dịch ngược, đếm mật độ

### 9.1 Đọc to: mười lăm câu tự hỏi trước khi đưa bài

Dùng cho người viết, người duyệt và giám khảo. Bản rút gọn cho máy nằm trong anchor (mục 9 của anchor) và trong dòng kiểm lúc chạy (`vn-naturalness.md`).

**Phần kể**
1. Câu đầu có mốc thời gian, một người cụ thể, hoặc câu khách nói không? (bài kể, video)
2. Có chữ nào trong danh mục mục 2 mức Lint không? Có thì thay.
3. Có "đã / đang / sẽ", "của bạn", "một", "những / các" mà bỏ đi vẫn rõ nghĩa không? Bỏ.
4. Có "việc / sự / điều này / một cách" không? Viết lại bằng động từ.
5. Chữ nối có phải chữ nói của đúng vùng không (mục 3.3)?
6. Chỗ ngoặt có việc làm hoặc đồ vật cụ thể không? Có "chợt nhận ra / khoảnh khắc ấy" không?
7. Lời người khác có để nguyên văn, dẫn bằng bảo / nói / kêu / nhắn không?
8. Bài học là một câu ngắn hai vế, hay nằm trong miệng nhân vật, chứ không phải "Bài học là…"?
9. Kết có một việc nhỏ hoặc một câu hỏi hẹp, không "Hy vọng… / Đừng quên…"?
10. Câu dài câu ngắn có xen nhau, có ít nhất một câu cụt không?

**Phần giao tiếp, bán**
11. Tự xưng một kiểu từ đầu đến cuối? Gọi khách trong cùng một họ? Bài công khai hay tin riêng, đã đúng cặp chưa?
12. Người nhận lớn tuổi hơn hoặc là khách: có "Dạ… ạ" chưa, và có bị "ạ" câu nào cũng có không? Tiểu từ đúng vùng, đặt ở chỗ dặn, rủ, làm thân?
13. Lời mời: một hành động, từ khóa tiếng Việt, có đường nhắn riêng, có giá nếu là bài bán? Có chữ nào ở bảng 5.5 (nổ, lùa, hứa, gấp giả, dí) không?
14. Emoji, chữ tiếng Anh, viết tắt: có đúng là của coach không? Có `**`, chữ đậm Unicode, Viết Hoa Mỗi Chữ, gạch dài không?
15. **Đọc to như coach đang nói với một người khách quen.** Câu nào người Việt không nói thành tiếng với khách ("Khóa học được thiết kế dành riêng cho bạn" thì không ai nói qua điện thoại) thì viết lại.

### 9.2 Dịch ngược

Chọn ba câu bất kỳ, dịch từng chữ ra tiếng Anh. Câu nào dịch ra trơn tru là câu Tây.

| Câu | Dịch từng chữ | Kết luận |
|---|---|---|
| "Khóa học được thiết kế để giúp bạn tự tin hơn." | "The course is designed to help you be more confident." | Trơn tuột: câu Tây, viết lại |
| "Học xong là dám lên nói, hết run." | "Study finish is dare go-up speak, end shake." | Vấp: câu Việt |
| "Điều này khiến khách hàng cảm thấy không thoải mái." | "This makes customers feel uncomfortable." | Trơn: câu Tây |
| "Khách nghe vậy là ngại, lần sau né luôn." | "Customer hear so is shy, next time avoid always." | Vấp: câu Việt |

Phép thử này không dùng cho câu ngắn kiểu "Giá 150k." (câu nào cũng dịch được); dùng cho câu dài có khung.

### 9.3 Đếm mật độ (cho grader và giám khảo)

Các ngưỡng dưới đây là **gắn cờ**, không phải trượt tự động: grader ghi lại, giám khảo đọc ngữ cảnh rồi chấm ở VN6, VN5 (`vn-naturalness.md`). Ngưỡng là phán đoán; nên chỉnh lại sau khi chạy trên 30–50 bài AI thật chưa có pack và trên bài thật của coach.

| Kiểm tra | Áp cho | Ngưỡng gắn cờ |
|---|---|---|
| Tiểu từ cuối câu | Caption, tin nhắn | Thấp hơn một nửa tỉ lệ trong bài thật của chính coach; chưa có bài mẫu thì dưới 1/3 số câu |
| "Dạ" hoặc "ạ" | Tin của coach nhỏ tuổi hơn gửi anh / chị, hoặc gửi khách | Không có cái nào (trượt VN5); hoặc trung bình hơn một "ạ" mỗi câu |
| "bạn" làm chủ ngữ | Mọi bài | Hơn 3 lần mỗi 100 chữ, hoặc 3 câu liền mở bằng "Bạn"; hoặc sai cặp trên Brand Card (trượt VN4) |
| "của bạn" | Mọi bài | Từ 2 lần trong bài dưới 150 chữ; bài dài hơn 1 lần mỗi 100 chữ |
| "việc + động từ", "sự + …" | Mọi bài | Từ 2 lần; kịch bản nói thì 1 |
| "rất", "thực sự", "vô cùng" | Mọi bài | "rất" hơn 2 lần mỗi 100 chữ; "vô cùng" trong lời nói |
| "Hãy" | Mọi bài | Hơn 1 lần một bài |
| "rằng" | Kịch bản nói | Từ 1 lần |
| "cảm thấy" | Mọi bài | Từ 2 lần |
| "đã / sẽ" | Mọi bài | Hơn 3 lần mỗi 100 chữ |
| Liên từ văn viết (Tuy nhiên, Do đó, Vì vậy, Ngoài ra, Hơn nữa, Mặt khác) | Kịch bản nói, tin nhắn | Từ 1 lần; bài viết dài: hơn 1 |
| Hán Việt trang trọng (nhằm, bởi lẽ, gia tăng, sở hữu, tiếp cận, cải thiện, duy trì, đáng kể, thúc đẩy) | Kịch bản nói | Từ 2 chữ |
| "anh ấy / cô ấy" | Chuyện kể giọng Nam, Trung | Từ 2 lần |
| "Không phải X, mà là Y" | Mọi bài | Hơn 1 lần |
| Câu dài | Mọi bài | Từ 40 tiếng không có dấu chấm (luật V8) |
| Emoji | Mọi bài | Coach không dùng mà có emoji; hoặc từ 3 dòng mở bằng emoji; hoặc 🚀 💡 ✨ 🎯 🌟 |
| Markdown | Bài Facebook, Zalo, TikTok, tin nhắn | `**…**` hoặc `#` đầu dòng: trượt (runtime) |
| Số, tiền kiểu Anh | Bài cho khách Việt | `$` + số, phẩy ngăn nghìn (1,990,000), chấm thập phân trước "triệu" (2.5 triệu): gắn cờ |

**Chỉ số chữ nói / chữ sách** (cho giám khảo, không phải lint): trên 100 chữ, đếm (a) chữ nói: thì, mà, rồi, xong, cái, lắm, nên, chứ, tại, kiểu; (b) chữ sách: tuy nhiên, việc, sự, điều này, những, rất, một cách, cảm thấy, đã. Video và tin nhắn có (a) thấp hơn hẳn (b) là dấu hiệu văn dịch. Kho lời nói của 6 nhân vật: (a) rất cao, (b) gần 0.

**Số đo trong repo** (mẫu nhỏ, chỉ để định hướng): in đậm Markdown 19,4 lần mỗi 1.000 chữ ở mẫu AI chưa có pack, 0 trong khoảng 30.000 chữ lời thật; emoji đầu dòng 5,5 so với 0; chú thích tiếng Anh trong ngoặc 3,2 so với 0; câu kết bằng tiểu từ 11% so với 36%.

---

## 10. Cho maintainer

### 10.1 Cái gì nằm ở đâu

| Tài sản | Vai trò | Ghi chú |
|---|---|---|
| `docs/research/vn-language-guide.md` (file này) | Nguồn chuẩn cho người | Không ship |
| `docs/research/vn-language-anchor-draft.md` | Bản nháp anchor máy đọc, ≤3.400 byte | Đề xuất anchor riêng trong file phương pháp VN; nhóm viết `modules/vn` quyết chỗ đặt và tên section |
| `locales/vn/banned-tells.txt` | Lint E141 (chuỗi, ví dụ ship) và grader I23 (chữ máy viết trong eval) | 65 mục mới ở cuối file, mỗi mục một dòng chú thích; ba mục cũ đã thu hẹp (10.2 mục 1) |
| `qa/standards/vn-naturalness.md` | Chuẩn chấm cho giám khảo và người duyệt bản ngữ | VN1–VN8, dòng kiểm lúc chạy, hai ví dụ hiệu chỉnh |

**65 mục mới trong `banned-tells.txt`** (66 lúc viết; bản duyệt bỏ "không những… mà còn" và thu hẹp 8 mục bắt nhầm tiếng Việt thật: "là" dẫn ý + "rất", "chợt nhận ra", "Chúc… thành công", "hành trang", "hãy để…", "bạn xứng đáng", "hân hạnh được", "xỏ chân vào đôi giày", "ngành công nghiệp giải trí / thời trang / du lịch") chỉ gồm những mẫu đo được bằng máy mà gần như không có cách dùng tự nhiên trong bài coach. Mỗi mục nhắm vào **dạng dịch**, không vào chữ. Đã chạy trên lời nói, bài viết, kịch bản của 6 nhân vật eval (answers.md, voice-samples.md bỏ phần "không bao giờ dùng", written-posts.md, pillar-transcript.md): không trúng chỗ nào, trừ lúc coach nhắc tới chính chữ đó để chê ("đẳng cấp" trong danh sách chữ anh không bao giờ nói) và một quảng cáo đối thủ được dán vào làm tư liệu ("THẦN TỐC"). Đã chạy trên `strings/vn.toml`: 0. Đã chạy trên các câu "sửa" ở mục 2, 3, 8: 0. Những mẫu cố ý **không** đưa vào lint vì có cách dùng thật: "Tuy nhiên", "Do đó" (bài LinkedIn của tư vấn có thể dùng một lần), "bạn đã bao giờ… chưa", "vui lòng", "Kính gửi", "Trân trọng" (email trang trọng), "chỉ với + giá", "theo dõi để không bỏ lỡ" (đang nằm trong `stock-phrases.txt`), "$", AM/PM, tên tháng tiếng Anh (máy có thể nhắc "$10k" khi nói về một bài người khác; Gen Z viết "8pm"), "đổi đời", "thu nhập thụ động" (coach tài chính có thể bàn thật), "đến từ", "khoảnh khắc" (nhiếp ảnh gia nói "bắt khoảnh khắc"), "đánh thức" (đánh thức con dậy), "bùng nổ" (dịch bùng nổ), "toàn diện" (khám toàn diện), "vượt bậc" (con tiến bộ vượt bậc), "thêm vào đó" giữa câu (cho thêm vào đó ít muối), "tua nhanh" (tua nhanh video), "bên ngoài hộp", "trong đôi giày" (nghĩa đen).

### 10.2 Đề xuất chưa làm (cần người có quyền quyết)

1. **Ba mục cũ trong `banned-tells.txt` chặn nhầm tiếng Việt thật: đã sửa ở bản duyệt (06/10).** `chìa khóa` / `chìa khoá` giờ chỉ bắt nghĩa bóng ("chìa khóa thành công", "là chìa khóa để…"; "chìa khóa kho", "chìa khóa để trên bàn" qua); `tóm lại` chỉ bắt "Tóm lại," / "Nói tóm lại:" mở câu; `có thể nói` chỉ bắt "Có thể nói," / "Có thể nói rằng" mở câu. Kho lời nói chạy lại: hết trúng "chìa khóa kho" (consultant) và "có thể nói cả buổi" (coldstart-coach). **Còn mở:** `hành trình` (mục cũ, start-block cũng cấm đích danh) vẫn bắt nghĩa đen "hành trình từ Huế vô Sài Gòn"; nhóm module quyết có thu hẹp không.
2. **Danh sách cắt wf6 V4 (từ đệm) và V6 (đuôi xin xác nhận)** đang cắt "nói chung là, thật ra là, đúng không ạ". Cắt sạch thì câu Việt trơ hơn, giống văn dịch hơn. Đề xuất ghi rõ trong §CM-HUMANIZE: giữ khi chữ đó nằm trong câu cửa miệng, cách mở của chính coach; chỉ cắt khi máy tự thêm.
3. **Hồ sơ giọng (Voice Card):** thêm trường nhỏ "chữ nối hay dùng" (2–3 chữ lấy từ lời xả: "xong", "thế là", "nói chung là", "tại"); tiểu từ đã có, mà chữ nối mới làm nên cách nối chuyện. Lưu **cả hai** cặp xưng hô (công khai và nhắn riêng) như `persona.toml content_pronouns` đã làm; voice.kit-shift 8 mới nói tin riêng gọi số ít, chưa nói chữ **tự xưng** cũng có thể đổi. Gộp vào trường sẵn có nếu ngân sách card chật: emoji coach dùng (≤4) vào `code_mix`; viết tắt trong Zalo vào `written_vs_spoken`; độ thẳng (mềm / thẳng ấm / thẳng gắt) vào `tone`. `openers_closers` nên có câu mở tin nhắn riêng của coach khi họ dán, vì tin nhắn là chỗ máy trôi về giọng tổng đài nhiều nhất.
4. **Grader:** thêm các kiểm tra đếm ở 9.3, nhất là tiểu từ so với bài của chính coach, "Dạ / ạ" trong tin gửi khách, Markdown trong bài Facebook, Zalo, TikTok.
5. **Kiểm tra lúc chạy (chỉ trên output):** bài Facebook, Zalo, TikTok có `**`, `##` hoặc chữ đậm Unicode → trượt; Title Case → cảnh báo; gạch dài trong bài VN → cảnh báo; trả lời câu hỏi giá mà không có giá → trượt (`micro`, `email-zalo`); từ khóa CTA là chữ Anh ASCII (GUIDE, FREE) → trượt, không có đường nhắn riêng → cảnh báo; tin gửi người lớn tuổi hơn không có "Dạ" lẫn "ạ" → cảnh báo; 🙂 trong tin trả lời khách → cảnh báo; tiểu từ sai vùng (đã có ở voice.kit-shift 7) mở thêm "hen, nghen, hông, hổng" (Nam) và "cơ, đấy, nhỉ" (Bắc).
6. **Ca eval nên thêm** (`voice.vn.toml`, `micro`, `email-zalo`): hỏi giá dưới bình luận → có con số, không "check ib" trơn · CTA từ khóa → chữ Việt + đường nhắn riêng · coach "mình – các chị em" trên bài, "chị – em" trên Zalo, không trộn · người bình luận gọi "c" → không đáp "bạn" · "để chị suy nghĩ" → không hạn giả trong ngày, không "tuy nhiên… nhanh chóng" · nhắc sau khi "seen" → một tin, có lối ra, không "em thấy chị đã xem" · "lùa gà à 🙂" → không phản công, có ít nhất một thứ kiểm được · coach gõ "em xem cái này" → máy xưng "em", không giọng trợ lý · coach gõ "t/m" → máy không tao – mày, cũng không "Dạ… ạ" cứng · Zalo báo tin xấu → lý do thật, giờ mới, bù ngay, "Em xin lỗi anh" · coach Bắc 45+ → không "nha, nè, á", emoji ≤2, không lóng Gen Z · bài LinkedIn → không tiểu từ chat, ≤1 emoji · bài kể có câu khách → dẫn bằng bảo / nói, không "chia sẻ rằng" · bài kể → chỗ ngoặt có một việc làm cụ thể, không "khoảnh khắc ấy".
7. **Ví dụ trong gói:** `locales/vn/examples.md` phải do người Việt viết từ đầu theo giọng từng vùng, **không dịch từ bản EN**. Lấy từ mục 3.15 và mục 8 của file này; đưa cả cặp "trước → sau" (cặp đối chiếu dạy máy nhanh hơn danh sách cấm); dòng "trước" cần `<!-- lint-ok:E141 -->`.
8. **Ngân sách:** file phương pháp VN đang ở 56.261 / 56.320 byte (99,9%, lint W201 lúc viết file này). Anchor mới thêm khoảng 3,4 KB, nên nhóm module phải nhường chỗ khi đặt anchor: chuyển các dòng trùng ở §CM-HUMANIZE mục 3 (danh sách cắt chữ dịch), §CM-LOCALE 1 (tiểu từ vùng) và §CM-VOICE 7–8 (văn nói, tiểu từ) sang anchor mới, hoặc xin nâng trần `method_file` cho bản VN.

### 10.3 Phép thử đã chạy khi viết

- 66 mục mới: mỗi mục có câu sai phải trúng và câu gần đúng (tiếng Việt thật, dễ bắt nhầm) phải không trúng: 90 câu sai, 82 câu gần đúng, 0 lỗi.
- Bản duyệt (người bản ngữ, 06/10): thêm 50 câu sai và 105 câu tiếng Việt thật dễ bắt nhầm ("khen là rất ngon", "chìa khóa để trên bàn", "Chúc anh chị thành công nha!", "chuẩn bị hành trang đi Đà Lạt", "hân hạnh được làm quen", "con không những bơi được mà còn…"). Trước khi sửa: 32 câu thật bị bắt nhầm. Sau: 0, trừ "hành trình" nghĩa đen (giữ có chủ ý, 10.2 mục 1); 50/50 câu sai vẫn trúng.
- Kho lời nói 6 nhân vật eval (answers.md, voice-samples.md bỏ danh sách "không bao giờ dùng", written-posts.md, pillar-transcript.md, research-paste.md, paste-dump.md): 4 lần trúng, cả 4 là chỗ coach nhắc tới chữ đó để chê hoặc quảng cáo đối thủ dán vào làm tư liệu.
- `strings/vn.toml`: 0. `modules/vn/*.md`, `core/vn/*.md` (không thuộc phạm vi E141): chỉ trúng ở chỗ module **trích** chữ cấm làm lời dặn ("không 'giá ib'", "Hãy cùng khám phá", "tiến hành" trong danh sách cắt), không phải văn dịch.
- 120 câu "sửa" của bản nghiên cứu văn dịch, 33 câu người viết của hai bản nghiên cứu kể chuyện và xưng hô, 132 câu "sau" trong file này và trong anchor: 0 lần trúng. Chiều ngược lại, lint (mục cũ + mới) bắt 61/120 câu "trước" của file này; phần còn lại là mẫu mức Judge và Đếm, đúng thiết kế.
- `python3 tools/lint.py`: 0 lỗi (không mục mới nào gây E141 hay E161). `python3 -m unittest discover -s tools/tests`: 319 bài qua hết.

### 10.4 Kiểm tra chép (I19) trước khi đưa ví dụ vào gói

Ví dụ trong file này và trong anchor đã được dò với mọi file trong `evals/personas/vn/` bằng cửa sổ 8 tiếng (ngưỡng chép của `evals/acceptance.toml [copy]`): không có chuỗi 8 tiếng nào trùng. Ai thêm ví dụ mới thì chạy lại cùng phép dò (tách tiếng theo khoảng trắng, chuẩn hóa NFC, bỏ dấu câu, chữ thường), và tránh câu cửa miệng, chuyện, con số của 6 nhân vật dù ngắn hơn 8 tiếng.

### 10.5 Câu hỏi mở, cần người bản ngữ ở mỗi vùng

- Bảng chữ nối theo vùng (3.3), bảng tiểu từ (4.6), bảng vùng (7.1): phán đoán người viết; cần một người Bắc, một người Nam, một người Huế–Quảng và một người Nghệ Tĩnh duyệt.
- "nha" đã phổ biến với người Bắc dưới 30 trên mạng tới mức nào? Có cho coach Bắc trẻ dùng "nha" khi chính họ dùng? (hiện: theo bài thật của coach).
- Giáo viên xưng "cô / thầy" với phụ huynh: tự nhiên ở cả ba miền không?
- Nghĩa của 🙂 và 👍 theo tuổi: hai nguồn chỉ đọc được qua tóm tắt tìm kiếm; nên hỏi thử 10 người mỗi nhóm tuổi.
- Ngưỡng "tin đầu dưới khoảng 60 chữ", "7h–21h", liều tiểu từ: phán đoán; nên đo trên tin thật của vài coach.
- Điều khoản giờ gửi tin quảng cáo trong Nghị định 91/2020 cần luật sư kiểm.
- Thứ hạng "hay gặp" của các mẫu văn dịch là ước lượng biên tập; nên đo lại trên 30–50 bài AI thật (ChatGPT, Claude, chưa có pack) cho mỗi loại bài.

### 10.6 Nguồn

**Trong repo:** `docs/research/wf2-vietnam-market.md` §1, §3, §5–§8 · `wf9-pov-vietnam.md` §2.1, §3 · `wf5-vietnam-launch.md` insight 9–12, 15, 19; F8; F10 · `wf6-character-design.md` (danh sách cắt V1–V9) · `wf14-voice-language-spec.md` · `modules/vn/voice.md`, `humanize.md`, `locale.md` · `qa/standards/email-zalo.md`, `shared.md` · `evals/personas/vn/*` (chỉ làm kho dò và để đếm) · `evals/baselines/vn-*` (mẫu AI chưa có pack).

**Tiếng Việt, ngôn ngữ học và dịch thuật**
- Nguyễn Thảo, "Tiếng Việt đang bị dùng dễ dãi, thiếu chuẩn mực", VietnamNet, 06/11/2016 (GS Nguyễn Văn Khang về "làm bởi (ai)" và "đến từ"). https://vietnamnet.vn/vn/giao-duc/khoa-hoc/tieng-viet-dang-bi-dung-de-dai-thieu-chuan-muc-338087.html
- Nghĩa KB, "Tiếng Việt trên nhiều bài báo cũng đang khá 'lạ'", Tuổi Trẻ, 26/08/2010. https://tuoitre.vn/tieng-viet-tren-nhieu-bai-bao-cung-dang-kha-la-397288.htm
- Minh Tú, "Dịch giả trẻ nghèo vốn tiếng Việt…", báo Phụ Nữ, 05/11/2019 (Trần Tiễn Cao Đăng). https://tuoitre.vn/phunuonline/dich-gia-tre-ngheo-von-tieng-viet-tac-pham-dich-vang-thau-lan-lon-a1398109.html
- Nguyễn Đặng Tiến Nguyên, Trần Thị Kim Tuyến, "Chuyển dịch thể bị động tiếng Anh sang tiếng Việt qua For Whom the Bell Tolls", VJOL, 2026. https://vjol.info.vn/giaochuc/article/view/141239
- "Bàn về dịch thuật của Cao Xuân Hạo". https://dichthuatsaokimcuong.com/tin-tuc-dich-thuat/2/ban-ve-dich-thuat-cua-cao-xuan-hao.html · "Dịch giả Cao Xuân Hạo: 'Tiếng Việt đang lâm nạn'", Tuổi Trẻ. https://tuoitre.vn/dich-gia-cao-xuan-hao-tieng-viet-dang-lam-nan-7322.htm
- ngonngu.net, lịch sử nghiên cứu cú pháp tiếng Việt (đề–thuyết). https://ngonngu.net/cuphap_lichsu05/156 · Tạp chí Khoa học ĐHSP TP.HCM (ranh giới đề–thuyết "thì, là, mà"). https://journal.hcmue.edu.vn/index.php/hcmuejos/article/download/2116/2100
- VJOL, tiểu từ tình thái cuối phát ngôn Nam Bộ. https://vjol.info.vn/tudienhoc/article/view/130363 · https://vjol.info.vn/NNDS/article/download/11413/10392
- VJOL, chiến lược giữ thể diện (Anh–Việt). https://vjol.info.vn/upt/article/view/135400 · Luật Minh Khuê, nói giảm nói tránh. https://luatminhkhue.vn/noi-giam-noi-tranh.aspx
- Báo Văn hóa, chữ "ngại". https://baovanhoa.vn/doi-song/trong-tieng-viet-co-mot-tu-rat-kho-dich-sang-tieng-anh-vi-no-tuong-trung-cho-su-tinh-te-cua-nguoi-viet-200174.html
- FPT Shop, "Chừ là gì"; HoaTieu, "Rứa là gì" (phương ngữ Trung).
- Tiền Phong và Báo Văn hóa về tiếng lóng Gen Z; Tuổi Trẻ 2024 về "chữa lành" bị chế giễu. https://tuoitre.vn/len-mang-bay-to-mong-muon-chua-lanh-con-bi-hanh-them-20240408114318027.htm
- Báo Quốc tế, "Ngôn ngữ thời hiện đại!?", 25/12/2008 (chêm tiếng Anh, làm màu). https://baoquocte.vn/ngon-ngu-thoi-hien-dai-7094.html · Tạp chí KH&CN ĐH Thái Nguyên, caption TikTok của sinh viên. https://vjol.info.vn/tnu/article/view/103012

**"Mùi AI" trong content tiếng Việt**
- findskill.ai, "AI viết content tiếng Việt tự nhiên: 10 dấu hiệu 'mùi AI'". https://findskill.ai/vi/blog/ai-viet-content-tieng-viet-tu-nhien/
- Finhay, "Mẹo dùng ChatGPT không bị văn mẫu". https://www.finhay.com.vn/meo-dung-chatgpt-khong-bi-van-mau-robotic
- VnReview: "Bảy cách viết bằng ChatGPT mà không bị phát hiện"; "6 prompt bắt ChatGPT, Claude AI viết như người"; "Mẹo khiến người khác không bao giờ nhận ra bạn dùng AI để viết" (chính bài này khuyên đổi "Điều này giúp…" thành "Nó làm cho…", tức là vẫn văn dịch).
- 1StopAsia, "English to Vietnamese localization mistakes" (bản "đúng" họ đưa ra vẫn là văn dịch). https://www.1stopasia.com/blog/english-to-vietnamese-localization-mistakes/

**Giao tiếp, bán hàng**
- Zing, "Nhiều khách mua hàng online hỏi cộc lốc…", 04/06/2021. https://lifestyle.zingnews.vn/nhieu-khach-mua-hang-online-hoi-coc-loc-gia-bao-tien-inbox-post1222552.html
- CafeF, "4 kiểu nhắn tin tố cáo EQ thấp", 18/09/2025. https://cafef.vn/4-kieu-nhan-tin-to-cao-eq-thap-ban-co-dang-mac-phai-18825091813580294.chn
- Tuổi Trẻ / PLO, "5 nguyên tắc nhắn tin trong công việc", 04/03/2014. https://tuoitre.vn/plo/5-nguyen-tac-nhan-tin-trong-cong-viec-post267947.html
- MISA AMIS, chăm sóc khách qua Zalo (mẫu tin CSKH mà AI hay chép). https://amis.misa.vn/64134/cham-soc-khach-hang-qua-zalo/
- LuatVietnam, "Bán hàng online - Tại sao phải inbox giá?". https://luatvietnam.vn/tin-phap-luat/ban-hang-online-tai-sao-phai-inbox-gia-230-17198-article.html · Sapo, nên để giá công khai hay không (đọc qua tóm tắt).
- SGGP, "Ma trận học làm giàu - Bài 2", 18/08/2020. https://www.sggp.org.vn/ma-tran-hoc-lam-giau-bai-2-lam-giau-bang-cam-xuc-post565516.html
- Decision Lab, emoji và Gen Z Việt. https://www.decisionlab.co/blog/the-importance-of-emojis-for-brands-in-vietnam · Kaiwa, phản ứng chữ trên mạng (hihi, hehe). https://trykaiwa.com/blog/vietnamese-online-text-reactions-2026 · Advertising Vietnam về 🙂, 👍 (chỉ đọc qua tóm tắt; trang trả 403).

**Giới hạn:** công cụ tìm kiếm thiên về tiếng Anh, ít bài biên tập tiếng Việt về văn dịch; thảo luận trong nhóm Facebook, Threads không truy cập được. Phần lớn bảng là tổng hợp biên tập, kiểm lại bằng nguồn trên và bằng kho lời nói trong repo. Cần người bản ngữ mỗi vùng đọc lại trước khi coi là chuẩn.
