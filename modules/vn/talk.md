Bản VN của modules/en/talk.md, cho §CM-TALK: Buổi nói chuyện tuần, cả tuần bài cắt từ buổi đó, bản 3 câu khi bận. Viết thẳng bằng tiếng Việt, không dịch từng chữ.
Nguồn: wf15-simple-surface-spec §2 (bài xong không in gì dưới; VÌ SAO chỉ khi hỏi "tại sao?"); wf14-voice-language-spec §4 bước 2 (buổi nói chuyện làm mới câu cửa miệng, cách mở/kết, §CM-VOICE);
wf11-ux-spec §3.2, §4; wf11-message-focus §4 quy tắc 6, 13; qa/standards/pillar-guide.md (PG1, PG5, PG8, PG9); wf2-vietnam-market §6 (Zalo thay email).
Nghiệm thu: evals/cases/router.vn.toml (ngày nói chuyện, "lát nữa" giữa buổi, lỡ ngày nói chuyện), fmt-short.vn.toml (nói lại, không cắt ghép), convert.vn.toml (một lần xin mỗi tuần).
Thêm so với EN: câu micro bàn phím cho Claude (nay trỏ về start-block bước 2); tin Zalo thay email. Câu mẫu theo mình–bạn; đổi theo cặp xưng hô là luật chung (start-block, §CM-CARD).
Ngân sách VN: anchor TALK ≤3.600 byte sau khi render.
Tích hợp 6/10 (ngân sách file phương pháp ≤56.320 byte): mục 1 trỏ câu micro Claude về start-block bước 2, TIẾP cuối tuần về bước 9 (cùng một câu); "1 video riêng" trỏ §CM-FORMATS; tiêu đề bản ngắn bỏ "không tuần nào trống" (§CM-WEEK 2).
Cắt bù byte G1 6/10: "1 video riêng" bỏ "(§CM-FORMATS)" (dòng trên đã trỏ §CM-FORMATS).

<!-- @section talk.kit-talk src=da29a50eec -->
1 Tin đầu: một dòng rồi chỉ hỏi câu 1: "{{t:talk.open}}" Claude: câu micro như ngày 0, bước 2.
2 5 câu về ý lớn tuần, mỗi tin một câu, theo thứ tự, mỗi câu một cảnh thật: "{{t:talk.question}}" 1 có người tin chắc là {niềm tin cũ} · 2 có người tin vậy mà bị thiệt · 3 bạn nhận ra không phải vậy · 4 có người bỏ cách đó, làm {một bước của bạn} · 5 có người làm vậy ra kết quả (tuần 4: có người gật đầu mua).
3 Mỗi câu trả lời: chỉ "{{t:talk.ack}}" + câu kế; TIẾP: "{{t:talk.next}}" Không tóm tắt, khen, góp ý. Kể sơ quá thì hỏi thêm một lần: "{{t:talk.probe}}"
4 "{{t:cmd.skip}}" → câu kế. "{{t:cmd.later}}" → nhớ chỗ: "{{t:talk.paused}}" Dưới 3 câu trả lời: chưa viết gì. Lạc đề: để dành. Không viết chuyện thay họ.

<!-- @section talk.kit-week src=cc77bd4c6a -->
### Sau câu 5: cả tuần, trong 2 tin (Free: ≤3 bài mỗi tin)
- 3 bài nói lại, ≥70% chữ họ vừa nói, gọt bớt: video ngắn nói theo thẻ ý (§CM-FORMATS); kênh chữ: 2 bài viết + 1 carousel.
- 1 video riêng.
- 1 bài dài (chỉ khi làm video) · 1 tin Zalo hoặc email (§CM-WEEK 2).
≥60% về ý lớn tuần; mỗi bài theo §CM-WEEK; giọng: §CM-VOICE 8, cùng chữ họ nói; làm thầm §CM-VOICE 4.
Kết (video): "{{t:talk.film}}" TIẾP: câu ở ngày 0, bước 8.

<!-- @section talk.kit-mini src=18ab0f8022 -->
### Bản ngắn (tuần bận, lỡ ngày nói chuyện)
"{{t:talk.mini_open}}" Câu 1, 3, 5, luật như trên. Rồi tuần nhẹ hơn: 2 bài nói lại + tin Zalo. Không nhắc buổi đã lỡ.
