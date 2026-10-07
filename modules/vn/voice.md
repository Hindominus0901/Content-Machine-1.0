Bản VN của modules/en/voice.md, cho §CM-VOICE (voice.kit-*) = "nói thế nào": Hồ sơ giọng làm thầm, dòng giọng trên Bản đồ, xưng hô với khách
(công khai và nhắn riêng), làm mới sau mỗi Buổi nói chuyện tuần, "viết lại giọng mình", "không giống mình:" / "mình có nói", đổi giọng theo nền tảng,
chữ tiếng Anh, khi chưa có bài mẫu.
Nguồn: wf14-voice-language-spec §0 V1-V4, §2-§4; wf15-simple-surface-spec §0 S5, §1.1-§1.4; DECISIONS; schemas/brand-card.toml (nhóm "voice",
gồm connectors và address_1to1); docs/research/vn-language-guide.md §1, §3.2, §4.1-§4.4 (06/10/2026).
Không nhắc lại ở đây: chữ nối, tiểu từ theo vùng, "Dạ … ạ", tin riêng gọi số ít, văn dịch (§CM-NATURAL); viết lại, đọc to (§CM-HUMANIZE);
cách in card (§CM-CARD); Bản đồ và "sửa dòng N" (§CM-MAP).
Tên trường chỉ ở bên trong; coach chỉ nghe chữ thường. audience_address = coach xưng gì + gọi khách là gì ("mình – các chị em"),
không bao giờ là pronouns (cặp máy – coach, hỏi ở trả lời 1); address_1to1 = cặp khi nhắn riêng một khách, nếu khác cặp công khai;
connectors = chữ nối họ hay dùng khi kể; dialect = vùng + tiểu từ của họ; code_mix = chỉ chữ tiếng Anh họ thật sự chêm.
Tích hợp 6/10 (ngân sách file phương pháp ≤56.320 byte): mục 1 bỏ "code_mix · humour" và chú thích connectors (enum ở §CM-CARD 3, code_mix ở mục 9); mục 3 bỏ "Giữ y cả tuần" (start-block XƯNG HÔ: giữ y mọi bài).
Retest FT2 7/10 (qa/runs/retest-ft2/review.md §8 item 5): DÙNG 7 "video ngắn: câu cuối hay caption" (mỗi video ngắn mang một câu hay nói trên Card, chỗ nào hợp); "ít nhất nửa số bài có" → "nửa số bài trở lên".

<!-- @section voice.kit-build src=a8ac51f765 -->
1 DỰNG thầm ngày 0 (§CM-CARD 3): lời xả = giọng nói; bài, tin họ dán, trang mở được = giọng viết. tone 3 chữ thường · rhythm ngắn, xen hay dài, có câu cụt, câu hỏi? · phrases, openers_closers, connectors: nguyên văn · audience_address, address_1to1: mục 3 · dialect: vùng, tiểu từ · written_vs_spoken chỉ khi có bài. Không hỏi gì về giọng; không chắc thì đoán giản dị.
2 DÒNG TRÊN BẢN ĐỒ: giọng điệu bằng chữ họ tự nhận (thẳng · ấm · tưng tửng), không khen · nhịp ≤5 tiếng · câu họ lặp nhiều nhất, nguyên văn · xưng hô y như họ nói với khách. "sửa dòng 4": §CM-MAP.
3 XƯNG HÔ VỚI KHÁCH = coach tự xưng + gọi khách, như đã nghe ("mình – các chị em"); chưa rõ: "mình – bạn". Nhắn riêng mà đổi cặp ("em – chị") → address_1to1. Không lẫn với pronouns.

<!-- @section voice.kit-keep src=ecea69bdf0 -->
4 MỖI BUỔI NÓI CHUYỆN TUẦN: câu cửa miệng, cách mở, kết mới nhất thay cái cũ nhất (giữ 5 câu, 3 cách); chỉ lời thật, nguyên văn, không chuốt, không lấy từ bài họ thích. Giọng điệu, nhịp chỉ đổi khi 2 buổi cùng cho thấy.
5 "{{t:cmd.voice}}": viết lại theo card như mục 7, rồi đọc to (§CM-HUMANIZE 5). Họ chỉ chỗ lệch → lưu như mục 6.
6 "{{t:cmd.not_me}} {line}" → never_say: "{{t:voice.not_me_ok}}" "{{t:cmd.i_do_say}} {word}" → do_say: "{{t:voice.do_say_ok}}" Một dòng rồi làm việc; giữ cho mọi bài, tác vụ, card về sau. Cắt, trả lại: §CM-HUMANIZE.

<!-- @section voice.kit-shift src=6e7ad3c50c -->
7 DÙNG trong mọi bài: giọng điệu, nhịp, xưng hô, chữ nối của họ, không chữ never_say; một câu cửa miệng hay cách mở khi hợp (bài từ 60 tiếng: nửa số bài trở lên; video ngắn: câu cuối hay caption), không gượng, không lặp hai bài liền. Văn nói, tiểu từ: §CM-NATURAL.
8 Video: giọng nói, y như họ nói. Bài viết, carousel: giọng viết; chưa có bài nào thì giọng nói làm gọn (bỏ ờ, à, câu vấp; giữ nhịp, tiểu từ). LinkedIn: gọn, ít emoji. TikTok, Reels: ngắn hơn, hook ngay câu đầu. Zalo, inbox, email: viết cho một người (address_1to1 nếu có).
9 CHỮ TIẾNG ANH (code_mix): chỉ chữ họ thật chêm, đúng mức; chữ khác đổi ra chữ Việt họ hay nói, hoặc bỏ. Không thêm tiếng lóng, emoji, chửi thề, câu trend, kiểu đùa họ không dùng.
