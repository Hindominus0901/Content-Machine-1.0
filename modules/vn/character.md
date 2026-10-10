Bản VN của modules/en/character.md, cho §CM-CHARACTER-LITE (character.kit-*): tính cách lấy từ lời xả, bài tính cách hằng tuần, quan điểm, độ nóng, thứ "mượn" để hút khách, 3 buổi nói chuyện sâu.
Nguồn: wf6-character-design A1 (luật phỏng vấn, 12 câu hỏi), A2, A4 (độ nóng, ghi chú VN 1-11: nhận trước đứng vững sau, thử thể diện, vùng miền, chính trị), §6 (lật lại); wf6-character-polarity mục 10;
arch-final-spec §5.2; wf11-ux-spec §3.3 (3 × 20 phút); DECISIONS. Nghiệm thu: evals/cases/character.vn.toml, router.vn.
Không lặp ở đây: trường trên card (§CM-CARD), chấm quan điểm và lật lại (§CM-EDGE), điểm dừng cứng (§CM-GUARDRAILS), sửa giọng (§CM-HUMANIZE). Tên độ nóng, 3D, bậc tin tưởng chỉ ở bên trong.
Thêm so với EN: nhận trước, đứng vững sau; thử thể diện; nhóm nhạy cảm VN (vùng miền, giới, tuổi; chính trị, nhà nước, tôn giáo là giới hạn cứng); mẹo micro bàn phím cho Claude (nay nằm ở start-block bước 2). Bỏ 6/10: "thu nhập dễ thành khoe: bỏ số hoặc nói khoảng" (lệch §CM-GUARDRAILS "khoe số làm bằng chứng"; §CM-EDGE MƯỢN đã lo). Người nhà không nêu tên = §CM-SETUP 1; người thường không nêu tên kể cả khi được nhờ = §CM-GUARDRAILS.

<!-- @section character.kit-core src=765f5031c2 -->
NGÀY 0: không hỏi về tính cách. Nét riêng (một cảnh + ai thấy không hợp), cách cũ họ chống, nguyên tắc, câu cửa miệng: chỉ từ lời xả, thiếu thì [CHƯA CÓ].
Mỗi tuần ≥1 bài tính cách: quan điểm · chuyện nguyên tắc và cái giá · "việc mình không bao giờ làm" · thói quen, lựa chọn + vì sao.
QUAN ĐIỂM chỉ từ card, thử thầm: người cùng nghề có thể cãi · họ bảo vệ được trong 2 câu · chuyện của họ chứng minh. Trượt: bỏ, không làm mềm. Nhận sai trước, đứng vững sau. "Gắt", "viral": viết luôn quan điểm về cách cũ; không bịa quan điểm sốc, không hỏi "chủ đề gì?".
NÓNG với ý, cách làm. Nhóm người (tuổi, vùng miền, giới, khách của họ) → cách làm, giữ độ nóng. Chính trị, nhà nước, tôn giáo: không đụng. Người thường: kể cảnh, không tên. "Gắt nữa": sắc hơn với cách làm, không chửi, không chê thứ họ bán. Công kích nhóm: vẫn dừng sau "{{t:cmd.post_anyway}}".
MƯỢN (§CM-EDGE): bằng cấp, số năm → những năm đó dạy họ bỏ gì. Bài quà dưới {{micro_threshold}} tiếng: bản của họ + bản "vì sao", giữ từ khoá. "Nghiên cứu nói" → bỏ.

<!-- @section character.kit-talks src=e4b4908277 -->
### 3 buổi nói chuyện về tính cách ("giống mình hơn", "có" khi được mời)
"Giống mình hơn" hay "có" khi được mời: "{{t:character.talk_start}}" Mỗi tin một câu, nói thay vì gõ ("{{t:character.voice_first}}"), hỏi cảnh, không hỏi tính từ, gặng ≤2 lần; rào đón → "{{t:character.bet}}"; mỗi câu trả lời: một dòng trung tính + câu kế. "Không dám nói công khai": ghi riêng, không viết thành bài.
Buổi 1: vì sao bắt đầu · nguyên tắc từng làm mất tiền · việc có tiền vẫn từ chối · điều không chịu nổi. 2: nghề mình sai ở đâu · lời khuyên muốn cấm · nét bị chê "hơi quá" · thói quen, cách tiêu tiền. 3: những năm làm sai · trả lời thành tiếng "thử đủ cách rồi" · khách 10 năm nữa · vì sao khách chọn họ (lời khách).
Rồi card: 3 nét riêng kèm bằng chứng, họ chọn một; giá trị chưa có chuyện trả giá: chưa chứng minh; ghi chỗ trống; bản ngắn ≤220 tiếng.

<!-- @section character.grow-dig src=11b501e1ae -->
### Đào sâu tính cách ("giống mình hơn nữa", "trên mạng mình là ai"; sau 3 buổi nói chuyện ở trên, hoặc thay luôn)
1 Đích: 6 dòng trên card, người lạ đọc là nhận ra họ. Hỏi theo luật các buổi ở trên.
2 Chỉ hỏi cái card còn thiếu, theo thứ tự:
- NÉT RIÊNG: "Kể mình nghe 3 lý do khách nể {xưng hô}, mà trong nghề không ai có đủ cả ba." → chọn MỘT nét đẩy lên hết cỡ; bản 10/10 là một cảnh; ai sẽ thấy không hợp.
- NGUYÊN TẮC: "Việc gì {xưng hô} luôn làm, hay không bao giờ làm, dù bị thiệt?" → 3-5 dòng "luôn/không bao giờ … vì …".
- GIÁ TRỊ: mỗi cái cần một chuyện kèm cái giá (tiền, một khách, thời gian); không có → "chưa chứng minh", không in như lời khẳng định.
- TẦM NHÌN: "10 năm nữa, nghề mình sẽ ngượng vì từng làm gì?" → một dòng + "người như mình thì {làm X}".
- PHÂN CỰC: cách cũ họ chống + một điều người cùng nghề sẽ cãi ("Nhiều người nghĩ X; thật ra là Y"), qua đủ 3 phép thử QUAN ĐIỂM (§CM-CHARACTER-LITE).
- CHỖ TỪNG DỞ: 2 lần sai, cái giá, giờ làm khác ra sao; một mâu thuẫn ("khó tính, mà lễ tốt nghiệp nào cũng khóc") và giá trị phía sau.
3 Một màn hình, mỗi phần trên một dòng (3 nguyên tắc, 1 giá trị kèm cái giá, 2 lần sai). "OK hay sửa một dòng?" Lần in card tới lưu vào trait, enemy, principles, stories.
4 Thêm vào NÓNG (§CM-CHARACTER-LITE): người cùng nghề, thói quen khách, nền tảng, chính họ ngày trước → nói về cách làm, không giễu; chuyện đau buồn, hứa sức khoẻ, tiền bạc → không. Độ nóng ≤3; khách lớn tuổi, B2B: hạ chủ đề một nấc, lời vẫn dứt khoát.
5 Chưa có cảnh: [CẦN {XƯNG HÔ}: một lần {xưng hô} …], không bịa.

<!-- @section character.grow-scenes src=17d3ebe9a2 -->
### Cho thấy, đừng tự khen (biến tính cách thành bài)
1 Không bao giờ "mình rất tâm huyết", "mình thật lòng": để một cảnh nói thay. Mỗi nét riêng, nguyên tắc, giá trị có 2 cảnh quay được, từ đời họ: thói quen (7 giờ sáng thứ Hai nào cũng…), lần từ chối (khách không nhận, vì sao), cái giá (giữ nguyên tắc đã mất gì), lựa chọn (chịu chi gì, không chi gì), cột mốc (ngày đầu làm được: ở đâu, kể với ai; không lấy tiền làm hook), công việc thật (soạn buổi với khách, trả lời khách; khách chưa đồng ý không lên hình).
2 Quan điểm: nháp ở độ nóng 1 ("Mình bỏ X rồi."), 2 ("Đừng X nữa. Làm Y.") và 3 ("X làm bạn mất thời gian, cả nghề ai cũng biết mà."); hỏi "Câu nào {xưng hô} hơi run khi đăng?", đề xuất đúng câu đó nếu qua §CM-CHARACTER-LITE. Dáng câu: "Đừng {cách cũ} nữa. Làm {cách mới}. {nguyên tắc}." · "Mình không bao giờ {X}, kể cả khi mất {cái giá}." · "Mình từng {cách cũ} suốt {N} năm. Mất {X}. Giờ mình {Y}." · "Mình là {vai} {nét riêng} nhất bạn từng gặp. Muốn {ngược lại} thì tìm người khác."
3 Mỗi tháng một nét đẩy hết cỡ: tuần nào cũng ≥1 bài cho thấy nó, mỗi lần một dạng. Bài kể cái sai chỉ đến khi tay nghề đã lộ (tuần 2-3 của mùa, §CM-SEASON), không ở tuần đầu.
4 Nhận trước, đứng vững sau: "Mình từng giảm giá suốt 2 năm. Nên giờ mình nói thẳng: …". Thử thể diện: nói thẳng câu này trước mặt một anh chị đi trước mình nể được không? Không thì hạ độ nóng. Lối ra đàng hoàng: "Bạn thích kiểu {khác} thì chắc mình không hợp rồi, vậy cũng không sao."
5 Nói đi nói lại vài quan điểm thấm hơn một lần nói gắt: 3 quan điểm quay lại mỗi mùa, mỗi lần chuyện mới.
