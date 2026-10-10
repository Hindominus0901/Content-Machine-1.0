Bản VN của modules/en/plan.md, cho §CM-WEEK (plan.kit-week*) và §CM-MONTH (plan.kit-month*): kế hoạch tuần và "lên kế hoạch tháng sau". Viết thẳng bằng tiếng Việt, không dịch từng chữ.
Nguồn: wf15-simple-surface-spec §1 bước 6, §2, §3 (Tuần 1 tự ra sau QUAY HÔM NAY; VÌ SAO lưu kèm mỗi bài, chỉ in khi hỏi "tại sao?"); wf14-voice-language-spec §3-§4 (đổi giọng theo nền tảng, dòng giọng hằng tháng nằm ở §CM-VOICE);
wf11-ux-spec §2, §3.2; wf11-message-focus §3-§5; arch-final-spec §5.5; wf13-inspiration-spec §3-§4; wf2-vietnam-market §5 (tháng cô hồn), §6 (comment → inbox → Zalo; Zalo thay email), §7 (Luật BVDLCN: danh sách phải đồng ý nhận).
editions/vn.toml [platform_mix], cta_channel; qa/standards/season-plan.md. Nghiệm thu: evals/cases/router.vn.toml (tuần 3 bài, kế hoạch tháng, Góc nhìn riêng), message.vn.toml, liked.vn.toml (Góc nhìn riêng).
Thêm so với EN: tin Zalo thay email (email chỉ khi có danh sách), đường đi {{cta_channel}}, tháng 7 âm không xếp mở bán, ý chính ≤20 tiếng (EN ≤15 words), nhãn Góc nhìn riêng đổi theo cặp xưng hô.
tier=lean|standard và plan_start là tên trường trên Brand Card, giữ tiếng Anh. Ngân sách VN: mỗi anchor ≤3.600 byte sau khi render.
Tích hợp 6/10 (ngân sách file phương pháp ≤56.320 byte): WEEK 6 lời mời mặc định trỏ §CM-CTA-KIT 1 (cta.default); WEEK 7 tính cách, giải trí trỏ video riêng §CM-FORMATS, chống lặp định dạng và kiểu mở trỏ §CM-HUMANIZE (CHỐNG LẶP).
G1 6/10 (theo EN): WEEK 2 K10 "lean (mặc định)", "standard, chỉ khi xin"; WEEK 4 K9 "Từ khoá 1 lần + lời mời"; WEEK 10 K3 "ngày 0 chỉ một dòng trên mỗi khung".
Cắt bù byte G1 (không bỏ luật): WEEK 3 trỏ mục 0 TRỌNG TÂM của KIỂM TRA TRƯỚC KHI GIAO (luôn trong khối hướng dẫn: một ý lớn, ý chính ≤20 tiếng, một niềm tin, không lấy chủ đề để dành), giữ "ý chính viết trước", "ĐỂ SAU không làm hook", tách hai ý; MONTH 3 điều kiện ĐỂ SAU vào lại trỏ §CM-MAP (Quay lại khi); MONTH 4 tháng cô hồn trỏ §CM-LOCALE 6; month.check bỏ dòng cuối "Trả lời 'không có gì thay đổi' là đủ." (TIẾP month.check_next nói y vậy trong cùng tin).
G2 6/10: WEEK 2 "chưa có (nói hay đoán)". K33 không cần ở VN: FORMATS đã ghi danh sách quay "(Tuần 1, …) mở bằng" film.list_open, và WEEK 10 không có vế "không thêm lời" để vướng.

<!-- @section plan.kit-week src=28fb623f17 -->
### Tuần nói chuyện (Tuần 1: sau QUAY HÔM NAY, mỗi "tiếp" một bài; chủ đề: trụ cột + hiểu biết nghề, sự thật chỉ của coach)
1 Tuần n = (số tuần từ plan_start mod 4) + 1, đi đầu là bước n: 1 vấn đề thật, nguyên nhân · 2 cách tốt hơn, cách của họ · 3 bằng chứng, "mình cũng làm được, dù…" · 4 cả ba + sản phẩm. Trụ cột xoay vòng.
2 Video ngắn (FB, TikTok, IG): 3 video (tuần nói chuyện: 4), 1 bài dài, 1 tin Zalo. Kênh chữ (LinkedIn, bản tin): 2 bài, 1 carousel, 1 tin Zalo/email, 1 video tuỳ chọn. Danh sách 300+: tin gửi trước, xin trả lời; chưa có (nói hay đoán): tin riêng (§CM-MESSAGES 4). Số giờ mỗi tuần quyết định: lean (≤1 tiếng, mặc định) hay standard (2–3 tiếng, thêm 1 video, 1 carousel). Xin bớt bài: giữ bài chính; không tuần nào trống.
3 Mỗi bài một trụ cột, một loại, qua mục 0 TRỌNG TÂM (KIỂM TRA TRƯỚC KHI GIAO); ý chính viết trước; một khung viết hợp loại bài, định dạng (§CM-COPY); ≥1 món trong kho: lời mời, quà, chuyện hay bằng chứng (§CM-BANKS); ĐỂ SAU không làm hook. Hai ý thì tách, ý sau để dành.
4 Từ khoá 1 lần trong thân mọi bài, cả bài mời gửi bạn, + lời mời; xoay vòng: hook → chữ trên màn hình → câu chốt → dòng 1 caption → mở đầu bài dài, carousel.
5 Dòng VÌ SAO lưu kèm mỗi bài, chỉ in khi hỏi "{{t:cmd.why}}": {{t:why.prefix}}: "{niềm tin cũ, chữ khách}" → "{niềm tin mới}" · dẫn tới: {bước kế}.
6 Lời mời theo chặng: kéo người mới → theo dõi, gửi bạn bè ("{{t:series.part2_tomorrow}}") · mặc định → từ khoá (§CM-CTA-KIT 1; nhẹ: trả lời, nhắn mình) · nhắn tin, đặt lịch → từ tuần 2, khi có bằng chứng (kết quả khách cho dùng, quy trình, suất nhóm đầu), lean ≤1/tuần, standard ≤2. Cho ≥3 lần mới xin 1 lần.
7 Theo tỷ lệ (mặc định 40/40/20): THU HÚT = kéo người mới + đồng cảm (rộng, dễ chia sẻ), NIỀM TIN = dạy + bằng chứng, CHUYỂN ĐỔI = sản phẩm, băn khoăn, quyết định của khách, lời mời. Tính cách, giải trí ≤20%, như video riêng (§CM-FORMATS). ≥3 định dạng (kiểu Việt: Phần 1/2/3, ≤3 phần, mỗi phần đứng riêng, không tự đặt ngưỡng comment · Góc nhìn {nghề} · Hỏi nhanh đáp gọn · Sự thật về nghề); chống lặp: §CM-HUMANIZE.
8 Khung trong Bài {xưng hô} thích: ≤1 video riêng/tuần (standard 2), chủ đề, chuyện của coach.
9 Chưa có bằng chứng: bài bằng chứng thành chuyện quy trình hoặc suất nhóm đầu, không giải thích; tuần đó có tin hỏi 3 khách cũ (§CM-MESSAGES 7).
10 In từng bài dưới dòng "N{n} · {thứ} · {dạng} · THU HÚT|NIỀM TIN|CHUYỂN ĐỔI · {n} chữ" + khung chép; ngày 0 chỉ một dòng trên mỗi khung. Họ dừng lúc nào cũng được; phần còn lại chờ "tiếp". Loại bài trong tên bài (cả QUAY HÔM NAY): đủ chữ, không mã, không viết tắt. Bảng trong chat ≤4 cột: Ngày · Dạng · Hook · Lời mời; bảng đủ cột vào file, hub (§CM-CALENDAR).

<!-- @section plan.kit-month src=dbbcea74ec -->
### Một quyết định, ≤20 phút
1 Mở bằng:
"{{t:month.check}}"
TIẾP: "{{t:month.check_next}}"
2 Kết quả mới: kiểm bằng chứng (§CM-GUARDRAILS). Soát thông điệp, 3 dòng: bài và khách trả lời theo ý lớn · từ khoá khách nói lại · bài tốt nhất. Đề xuất GIỮ (mặc định) thông điệp, ý lớn, từ khoá; thêm góc mới, bằng chứng mới. Hoặc chỉnh một dòng bằng câu khách nói lại. "{{t:month.decide}}" Họ đã bảo giữ → bước 4. Không nói "khoá" hay "90 ngày".
3 ĐỂ SAU vào lại như §CM-MAP (Quay lại khi), thành góc mới của một ý lớn, không thành ý thứ 4. Từ khoá: giữ, trừ khi 60+ ngày không ai nói mà từ dự phòng khách nói 2+ lần.
4 Tháng sau bằng lời thường, mỗi tuần một dòng (§CM-WEEK): ý lớn · niềm tin cũ → mới · bài và lời mời · bằng chứng (chưa có: như mục 9 §CM-WEEK). Phần MỚI ≤20%: bài tốt nhất của họ ở dạng mới; không có thì BẠN NÓI ĐƯỢC có căn cứ; không nữa thì một khung trong Bài {xưng hô} thích. Tháng cô hồn: §CM-LOCALE 6. Rồi Brand Card v{n+1}, in lại Bản đồ và dòng giọng.

<!-- @section plan.kit-month-angle src=d69fb2ae59 -->
### Góc nhìn riêng (tuỳ chọn; mời một lần: "{{t:angle.offer}}")
{{t:angle.tag}}
AI CŨNG NÓI: chỉ điều thấy ở 2+ kênh; nêu tên kênh được, không tên người comment hay con số.
CHƯA AI NÓI: nhu cầu khách từ 2+ người ở 2+ nơi; ít hơn thì ghi "{{t:angle.hunch}}", bài kế kết bằng câu hỏi để thử.
{XƯNG HÔ} NÓI ĐƯỢC: khoảng trống đó × chuyện, bằng chứng, niềm tin của coach, trên một ý lớn có sẵn.
Theo dõi kênh: §CM-LIKED 6.
