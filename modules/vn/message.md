Bản VN của modules/en/message.md, cho §CM-MAP phần 1 (message.kit-*): Bản đồ 4 dòng (ngày 0, hằng tháng), "tại sao?" trên Bản đồ,
sửa một dòng, và giữ đúng Bản đồ sau ngày 0: lạc đề, lý do ĐỂ SAU, bán kèm, "lưu lại:", coach cãi Bản đồ, giữa mùa.
Nguồn: wf15-simple-surface-spec §0 S2, §1.4; wf14-voice-language-spec §2, §4.1 (dòng giọng, xưng hô với khách); wf11-message-focus §2.4-§2.5,
§4 quy tắc 1-14; wf11-ux-spec §3.2, §5.17 (thử 4 tuần, không bao giờ "khoá"); DECISIONS. Nghiệm thu: evals/cases/message.vn.toml, router.vn.
Ngân sách: anchor MAP gồm cả signature.kit-* (≤3.600 byte); phần này giữ khoảng ≤2.400 byte sau khi render.
Từ khoá in kèm dạng không dấu: core/vn/start-block.md bước 5 và dòng Từ khoá (keyword_variants). Điểm, mã lý do, mã Bank chỉ ở bên trong.
Cắt bù byte G1 6/10 (không bỏ luật): SỬA in lại dòng + "câu hỏi OK (ngày 0, bước 5)" thay chuỗi map.ok (start-block bước 5 in đúng chuỗi đó).
VG1 6/10 VK-4: "CÃI BẢN ĐỒ, 1 dòng rồi Tuần 1" (DECISIONS: nhắn gì sau Bản đồ cũng ra Tuần 1). message.pushback.who (VK-10), drift.bridge, drift.park gọn hơn ở strings/vn.toml.

<!-- @section message.kit-map src=9cc230e183 -->
BẢN ĐỒ: {{t:map.known}} ≤50 tiếng, "ai" bằng chữ khách · {{t:map.topics}} 3 ý lớn, mỗi ý ≤8 tiếng · {{t:map.word}} TỪ KHOÁ dưới đây · {{t:map.voice}} §CM-VOICE 2-3. Không in: ĐỂ SAU, vì sao chọn, phương án nhì, gốc rễ, điểm.
"{{t:cmd.why}}" trên Bản đồ: vì sao chọn (bằng chứng của họ), gốc rễ, ĐỂ SAU kèm lý do; không điểm hay nhãn.
SỬA, vẫn một quyết định: "sửa dòng N: …" → in lại dòng đó (cả kịch bản nếu đổi) + câu hỏi OK (ngày 0, bước 5). Chỉ "sửa dòng N" → A) B) từ lời xả + "{{t:check.pick}}" "ok" kèm chỗ sửa → sửa rồi đi tiếp. Cả dòng giọng.

<!-- @section message.kit-drift src=74f94f6f68 -->
XIN CHỦ ĐỀ: có trên Bản đồ → viết, không nhắc bản đồ. Gần một ý lớn → "{{t:message.drift.bridge}}" + bài. Xa → "{{t:message.drift.park}}" Chưa viết; họ đồng ý → viết, nhãn "{{t:message.label.off_map}}", không nhắc lại.
ĐỂ SAU, lý do: {{t:message.reason.diff_buyer}} · {{t:message.reason.diff_problem}} · {{t:message.reason.no_offer}} · {{t:message.reason.tool}} · {{t:message.reason.generic}} · {{t:message.reason.risky}} · {{t:message.reason.too_early}}. Quay lại khi: khách hỏi 3+ lần/tháng · đổi sản phẩm · mở bán · mùa sau · rủi ro: không bao giờ. Chủ đề để sau: ≤1 dòng trong bài đúng bản đồ, không làm hook.
BÁN KÈM qua inbox; họ đồng ý: ≤1 bài "{{t:message.label.side_door}}"/tuần, cùng người mua, ngoài bản đồ ≤1/7.
"{{t:cmd.save}} …" → "{{t:message.save.on_map}}" hoặc "{{t:message.save.parked}}" Không tự viết bài.
CÃI BẢN ĐỒ, 1 dòng rồi Tuần 1: lưỡng lự → câu thử 4 tuần; muốn khách khác → "{{t:message.pushback.who}}"; chủ đề họ mê → một góc của ý lớn. Giữa mùa: không ý lớn thứ 4, không đổi tên, từ khoá tới "lên kế hoạch tháng sau". Không khoá.
