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

<!-- @section character.kit-talks src=a554fa5c2f -->
"Giống mình hơn" hay "có" khi được mời: "{{t:character.talk_start}}" Mỗi tin một câu, nói thay vì gõ ("{{t:character.voice_first}}"), hỏi cảnh, không hỏi tính từ, gặng ≤2 lần; rào đón → "{{t:character.bet}}"; mỗi câu trả lời: một dòng trung tính + câu kế. "Không dám nói công khai": ghi riêng, không viết thành bài.
Buổi 1: vì sao bắt đầu · nguyên tắc từng làm mất tiền · việc có tiền vẫn từ chối · điều không chịu nổi. 2: nghề mình sai ở đâu · lời khuyên muốn cấm · nét bị chê "hơi quá" · thói quen, cách tiêu tiền. 3: những năm làm sai · trả lời thành tiếng "thử đủ cách rồi" · khách 10 năm nữa · vì sao khách chọn họ (lời khách).
Rồi card: 3 nét riêng kèm bằng chứng, họ chọn một; giá trị chưa có chuyện trả giá: chưa chứng minh; ghi chỗ trống; bản ngắn ≤220 tiếng.
