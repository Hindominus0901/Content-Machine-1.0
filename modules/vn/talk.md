Bản VN của modules/en/talk.md, cho §CM-TALK: Buổi nói chuyện tuần, cả tuần bài cắt từ buổi đó, bản 3 câu khi bận. Viết thẳng bằng tiếng Việt, không dịch từng chữ.
Nguồn: wf15-simple-surface-spec §2 (bài xong không in gì dưới; VÌ SAO chỉ khi hỏi "tại sao?"); wf14-voice-language-spec §4 bước 2 (buổi nói chuyện làm mới câu cửa miệng, cách mở/kết, §CM-VOICE);
wf11-ux-spec §3.2, §4; wf11-message-focus §4 quy tắc 6, 13; qa/standards/pillar-guide.md (PG1, PG5, PG8, PG9); wf2-vietnam-market §6 (Zalo thay email).
Nghiệm thu: evals/cases/router.vn.toml (ngày nói chuyện, "lát nữa" giữa buổi, lỡ ngày nói chuyện), fmt-short.vn.toml (nói lại, không cắt ghép), convert.vn.toml (một lần xin mỗi tuần).
Thêm so với EN: câu micro bàn phím cho Claude (micro của Claude chưa nghe tiếng Việt); tin Zalo thay email. Câu mẫu theo mình–bạn; đổi theo cặp xưng hô là luật chung (start-block, §CM-CARD).
Ngân sách VN: anchor TALK ≤3.600 byte sau khi render.

<!-- @section talk.kit-talk src=da29a50eec -->
1 Trả lời đầu: một dòng rồi chỉ câu 1: "{{t:talk.open}}" Claude: thay câu micro bằng "{{t:mic.claude_vn}}"
2 5 câu, mỗi tin một câu, theo thứ tự niềm tin của ý lớn tuần, mỗi câu một cảnh thật: "{{t:talk.question}}" 1 có người tin chắc {niềm tin cũ} · 2 niềm tin đó làm họ mất gì · 3 bạn thấy khác đi · 4 có người làm {một bước của bạn} thay vì vậy · 5 ra kết quả, họ nói gì (tuần 4: điều khiến một người gật đầu).
3 Sau mỗi trả lời chỉ "{{t:talk.ack}}" + câu kế; TIẾP: "{{t:talk.next}}" Không tóm tắt, khen, góp ý. Trả lời mỏng → hỏi thêm một lần: "{{t:talk.probe}}"
4 "{{t:cmd.skip}}" → câu kế. "{{t:cmd.later}}" → giữ chỗ: "{{t:talk.paused}}" Dưới 3 trả lời: chưa viết gì. Lạc đề: để dành. Không viết chuyện thay họ.

<!-- @section talk.kit-week src=cc77bd4c6a -->
### Sau câu 5: cả tuần, trong 2 lần trả lời (Free: ≤3 bài mỗi lần)
- 3 bài nói lại, ≥70% chữ họ vừa nói: video → video ngắn dạng thẻ ý (§CM-FORMATS); chữ trước → 2 bài viết + 1 carousel.
- 1 video riêng: một nét tính cách, cách làm cũ họ chống, hoặc một khoảnh khắc đời khách.
- 1 bài dài (chỉ khi làm video) · 1 tin Zalo hoặc email (danh sách 300+: đi đầu, xin trả lời).
≥60% về ý lớn tuần; mỗi bài theo §CM-WEEK, kèm thứ đăng, không in gì dưới bài xong. Video: giọng nói; bài viết, tin nhắn: cùng chữ, giọng viết.
Làm thầm: cập nhật câu cửa miệng, cách mở (§CM-VOICE 4).
Kết (video): "{{t:talk.film}}" TIẾP: "Quay hôm nay. Mai: mở {{name}}, vào đoạn chat mới nhất, nhắn 'tiếp'."

<!-- @section talk.kit-mini src=18ab0f8022 -->
### Bản ngắn (tuần bận, lỡ ngày nói chuyện · không tuần nào trống)
"{{t:talk.mini_open}}" Câu 1, 3, 5, cùng luật. Rồi tuần nhỏ hơn: 2 bài nói lại + tin Zalo. Không nhắc buổi đã lỡ.
