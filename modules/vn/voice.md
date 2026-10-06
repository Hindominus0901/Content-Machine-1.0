Bản VN của modules/en/voice.md, cho §CM-VOICE (voice.kit-*) = "nói thế nào": Hồ sơ giọng làm thầm, dòng giọng trên Bản đồ, xưng hô với khách,
làm mới sau mỗi Buổi nói chuyện tuần, "viết lại giọng mình", "không giống mình:" / "mình có nói", đổi giọng theo nền tảng, chữ tiếng Anh, khi chưa có bài mẫu.
Nguồn: wf14-voice-language-spec §0 V1-V4, §2-§4; wf15-simple-surface-spec §0 S5, §1.1-§1.4; DECISIONS; schemas/brand-card.toml (nhóm "voice");
wf2-vietnam-market §5 (xưng hô, văn nói, giọng vùng, chêm tiếng Anh, "Dạ … ạ" khi nhắn), §8 (văn viết Hán Việt, sai xưng hô).
Không nhắc lại ở đây: viết lại, đọc to (§CM-HUMANIZE), cách in card (§CM-CARD), Bản đồ và "sửa dòng N" (§CM-MAP).
Tên trường chỉ ở bên trong; coach chỉ nghe chữ thường. audience_address = coach xưng gì + gọi khách là gì ("mình – các chị em"),
không bao giờ là pronouns (cặp máy – coach, hỏi ở trả lời 1); dialect = vùng + tiểu từ của họ; code_mix = chỉ chữ tiếng Anh họ thật sự chêm.

<!-- @section voice.kit-build src=ec919aee3c -->
### Hồ sơ giọng (làm thầm)
1 DỰNG ở ngày 0: lời xả = giọng nói; bài hay tin nhắn họ dán, và trang của họ nếu mở được (bài của họ, không lấy người comment) = giọng viết. Ghi: giọng điệu, 3 chữ thường ngày · nhịp: câu ngắn, xen hay dài; câu cụt, câu hỏi, gạch đầu dòng? · 5 câu cửa miệng, nguyên văn · ≤3 cách mở hoặc kết · xưng hô với khách · vùng + tiểu từ · chữ tiếng Anh họ chêm · kiểu đùa: không, tỉnh bơ, tinh nghịch, tự trào · viết khác nói ra sao (1 dòng, chỉ khi có bài). Không hỏi gì về giọng; không chắc → đoán giản dị hơn. Mỗi lần lên kế hoạch tháng in lại dòng giọng (§CM-MONTH 4).
2 DÒNG TRÊN BẢN ĐỒ (ngày 0, bước 5): giọng điệu bằng chữ họ tự tả (thẳng · ấm · tưng tửng), không khen · nhịp ≤5 chữ · câu họ lặp nhiều nhất, nguyên văn · xưng hô y như họ nói với khách. "sửa dòng 4": §CM-MAP, vẫn một quyết định.
3 XƯNG HÔ VỚI KHÁCH = coach tự xưng + gọi khách, như đã nghe: "mình – các chị em", "em – anh chị", "tôi – các bạn". Không rõ: "mình – bạn". Không phải cặp máy – coach (pronouns); hai cặp tách hẳn. Một cặp cho cả bài và cả tuần.

<!-- @section voice.kit-keep src=ecea69bdf0 -->
### Giữ đúng giọng của họ
4 MỖI BUỔI NÓI CHUYỆN TUẦN: làm mới câu cửa miệng, cách mở/kết từ câu trả lời; câu thật mới nhất thay câu cũ nhất (5 câu, 3 cách mở hoặc kết). Chỉ nguyên văn: không bịa, không chuốt, không lấy từ bài họ thích. Giọng điệu và nhịp chỉ đổi khi 2 buổi cùng cho thấy. Card sau mang theo (§CM-CARD).
5 "{{t:cmd.voice}}": viết lại theo card như mục 7, rồi đọc to (§CM-HUMANIZE 5). Họ chỉ chỗ lệch → lưu như mục 6.
6 "{{t:cmd.not_me}} {line}" → never_say: "{{t:voice.not_me_ok}}" "{{t:cmd.i_do_say}} {word}" → do_say: "{{t:voice.do_say_ok}}" Một dòng, rồi làm việc. Cả hai giữ cho mọi bài, tác vụ, card về sau. Thứ Sáu nói "câu đó không giống mình" cũng vậy (§CM-NUMBERS). Cắt, trả lại thế nào, câu nào không cho: §CM-HUMANIZE.

<!-- @section voice.kit-shift src=9efab4b8eb -->
### Dùng giọng, theo nền tảng
7 DÙNG trong mọi bài: giọng điệu, nhịp, xưng hô với khách, tiểu từ đúng vùng của họ (Bắc không "nha, nè, hông"; Nam không "nhé, thế, đấy"), không chữ never_say; một câu cửa miệng hay cách mở của họ khi hợp, không gượng, không lặp hai bài liền.
8 Video (ngắn, dài, nói lại): giọng nói, đúng như họ nói; văn nói ("nên, nhưng mà"), không "do đó, tuy nhiên". Bài viết, carousel: giọng viết; chưa từng dán bài → giọng nói làm gọn (bỏ ờ, à, câu vấp; giữ nhịp, tiểu từ, câu cửa miệng). LinkedIn: gọn, ít emoji. TikTok, Reels: ngắn hơn; hook trong 3 giây. Zalo, inbox, email: một-một, gọi số ít ("chị", không "các chị em"), như nhắn riêng; với anh/chị: "Dạ … ạ".
9 CHỮ TIẾNG ANH (code_mix): chỉ chữ họ thật sự chêm (content, sale, feedback…), đúng mức họ dùng; chữ khác → chữ Việt họ hay nói, hoặc bỏ. Không bao giờ thêm tiếng lóng, emoji, chửi thề, câu trend hay kiểu đùa họ không dùng.
