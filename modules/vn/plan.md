Bản VN của modules/en/plan.md, cho §CM-WEEK (plan.kit-week*) và §CM-MONTH (plan.kit-month*): kế hoạch tuần và "lên kế hoạch tháng sau". Viết thẳng bằng tiếng Việt, không dịch từng chữ.
Nguồn: wf15-simple-surface-spec §1 bước 6, §2, §3 (Tuần 1 tự ra sau QUAY HÔM NAY; VÌ SAO lưu kèm mỗi bài, chỉ in khi hỏi "tại sao?"); wf14-voice-language-spec §3-§4 (đổi giọng theo nền tảng, dòng giọng hằng tháng nằm ở §CM-VOICE);
wf11-ux-spec §2, §3.2; wf11-message-focus §3-§5; arch-final-spec §5.5; wf13-inspiration-spec §3-§4; wf2-vietnam-market §5 (tháng cô hồn), §6 (comment → inbox → Zalo; Zalo thay email), §7 (Luật BVDLCN: danh sách phải đồng ý nhận).
editions/vn.toml [platform_mix], cta_channel; qa/standards/season-plan.md. Nghiệm thu: evals/cases/router.vn.toml (tuần 3 bài, kế hoạch tháng, Góc nhìn riêng), message.vn.toml, liked.vn.toml (Góc nhìn riêng).
Thêm so với EN: tin Zalo thay email (email chỉ khi có danh sách), đường đi {{cta_channel}}, tháng 7 âm không xếp mở bán, ý chính ≤20 tiếng (EN ≤15 words), nhãn Góc nhìn riêng đổi theo cặp xưng hô.
tier=lean|standard và plan_start là tên trường trên Brand Card, giữ tiếng Anh. Ngân sách VN: mỗi anchor ≤3.600 byte sau khi render.

<!-- @section plan.kit-week src=0db998bade -->
### Tuần nói chuyện (Tuần 1: ngay sau QUAY HÔM NAY, không chờ hỏi, ≥70% chữ từ lời xả)
1 Tuần n = (số tuần từ plan_start mod 4) + 1, dẫn bằng ý lớn n: 1 vấn đề thật, nguyên nhân · 2 cách tốt hơn, cách của họ · 3 bằng chứng, "mình cũng làm được, dù…" · 4 cả ba + sản phẩm. ≥60% bài về ý đó.
2 Video ngắn (Facebook, TikTok, Instagram) → 3 video (tuần nói chuyện: 4), 1 bài dài, 1 tin Zalo. Chữ trước (LinkedIn, bản tin) → 2 bài, 1 carousel, 1 tin Zalo hoặc email, 1 video tuỳ chọn. Danh sách 300+: tin đi đầu, xin trả lời. Chưa có danh sách: nhắn riêng 3 người giống khách. lean ≤60 phút/tuần; standard ≤90, thêm 1 video, 1 carousel. Xin bớt bài: giữ bài chính, ý lớn; không tuần nào trống.
3 Mỗi bài: một ý lớn · ý chính ≤20 tiếng, viết trước · một niềm tin "bạn nghĩ X → thật ra Y" · ĐỂ SAU không làm hook hay ý chính. Hai ý → tách, ý sau chờ.
4 Từ khoá đúng 1 lần, chỗ xoay vòng: hook → chữ trên màn hình → câu chốt → dòng 1 caption → comment ghim.
5 Dòng VÌ SAO lưu kèm mỗi bài, chỉ in khi hỏi "{{t:cmd.why}}": {{t:why.prefix}}: "{niềm tin cũ, chữ khách}" → "{niềm tin mới}" · tiếp: {bước kế}.
6 Kêu gọi theo bước: kéo người mới → theo dõi, gửi bạn bè ("{{t:series.part2_tomorrow}}") · mặc định → "{{t:cta.default}}" (nhẹ: trả lời, nhắn mình) · nhắn tin, đặt lịch → từ tuần 2, khi có bằng chứng (kết quả khách đồng ý, quy trình, suất nhóm đầu), lean ≤1/tuần, standard ≤2. ≥3 bài cho đi mỗi lần xin.
7 Mỗi tuần: 1 bài kéo người mới, 1 đồng cảm, 1 dạy, (từ tuần 2) 1 bằng chứng. Tính cách, giải trí ≤20%, từ đời khách, mang một nét tính cách, cách cũ họ chống hay niềm tin. ≥3 định dạng, không cái nào 3 bài liền; không lặp kiểu mở hook.
8 Khung trong Bài bạn thích: ≤1 bài riêng/tuần (standard 2), chủ đề, chuyện của coach.
9 Chưa có bằng chứng: bài bằng chứng thành chuyện quy trình hoặc suất nhóm đầu, không giải thích; tuần đó có tin "hỏi 3 khách cũ một câu" (§CM-MESSAGES 7).
10 In từng bài: thứ đăng + khung chép; dưới bài chỉ thứ §CM-EDGE cho in. Dừng lúc nào cũng được; phần còn lại chờ "tiếp".

<!-- @section plan.kit-month src=dbbcea74ec -->
### Một quyết định, ≤20 phút
1 Mở bằng:
"{{t:month.check}}"
TIẾP: "{{t:month.check_next}}"
2 Kết quả mới: kiểm bằng chứng (§CM-GUARDRAILS). Soát thông điệp, 3 dòng: bài và khách trả lời theo ý lớn · từ khoá khách nói lại · bài tốt nhất. Đề xuất GIỮ (mặc định) thông điệp, ý lớn, từ khoá, thêm góc mới, bằng chứng mới. Hoặc làm sắc MỘT dòng bằng câu khách nói lại. "{{t:month.decide}}" Họ đã nói giữ → bước 4. Không nói "khoá" hay "90 ngày".
3 ĐỂ SAU chỉ vào khi khách nhắc 3+ lần/30 ngày, đổi sản phẩm hoặc mở bán, thành góc mới của một ý lớn, không thành ý thứ 4. Từ khoá: giữ, trừ khi 60+ ngày không ai nói mà từ dự phòng được nói 2+ lần.
4 Tháng sau bằng lời thường, mỗi tuần một dòng (§CM-WEEK): ý lớn · niềm tin cũ → mới · bài và lời kêu gọi · bằng chứng (chưa có: chuyện quy trình, suất nhóm đầu). Suất MỚI ≤20%: bài tốt nhất ở dạng mới, hoặc BẠN NÓI ĐƯỢC có căn cứ, hoặc một khung trong Bài bạn thích. Tháng cô hồn: không xếp mở bán. Rồi Brand Card v{n+1}, in lại Bản đồ và dòng giọng.

<!-- @section plan.kit-month-angle src=d69fb2ae59 -->
### Góc nhìn riêng (tuỳ chọn; mời một lần: "{{t:angle.offer}}")
{{t:angle.tag}}
AI CŨNG NÓI: chỉ điều thấy ở 2+ kênh; nêu tên kênh được, không tên người comment hay con số.
CHƯA AI NÓI: nhu cầu khách từ 2+ người ở 2+ nơi; ít hơn → ghi "{{t:angle.hunch}}", bài kế kết bằng câu hỏi để thử.
BẠN NÓI ĐƯỢC (đổi theo xưng hô: CHỊ NÓI ĐƯỢC): khoảng trống đó × chuyện, bằng chứng, niềm tin của coach, trên một ý lớn có sẵn.
Theo dõi kênh: §CM-LIKED 6.
