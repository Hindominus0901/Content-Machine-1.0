Result: PASS

# VN naturalness judge: VN edition as built on 6 Oct 2026

Independent native-reader pass. Yardstick: `qa/standards/vn-naturalness.md` (VN1–VN8) and `docs/research/vn-language-guide.md` §1, §2 (incl. §2.7), §3, §4, §9. Build: `python3 tools/build.py --edition vn` (build 1.0.0, sha256 f4fc0691…; 1-INSTRUCTIONS 9,543 B, CONTENT-MACHINE-VN 56,246 B, PHONE-STARTER 9,292 B). Every value in `strings/vn.toml`, both instruction files line by line, and all 21 method anchors were read in full (SETUP, CARD, TODAY, TALK, WEEK, FORMATS, POSTS, MESSAGES, NUMBERS, MONTH, MAP, CTA-KIT, CHARACTER-LITE, RESEARCH-LITE, EDGE, VOICE, HUMANIZE, NATURAL, GUARDRAILS, LIKED, LOCALE). Findings are mine; guide examples are cited by section, not copied.

## Scores

| Area | Score | Findings | Of which over-corrections | Verdict |
|---|---|---|---|---|
| A. Coach-facing lines (strings/vn.toml + word-for-word lines in 1-INSTRUCTIONS / PHONE-STARTER) | **4** | 33 | 0 | Natural dialogue; the stiff spots sit in labels and two Day-0 templates. A low 4: the Map screen is the one Day-0 screen a native reader would call translated. |
| B. 1-INSTRUCTIONS.txt as language the model imitates | **4** | 5 | 2 | Plain, spoken, imperative Vietnamese; quoted lines are natural. Gaps are rules, not wording. |
| C. CONTENT-MACHINE-VN.md (sample lines + instruction prose) | **4** | 16 | 4 | Prose is clean (no essay connectors, no "việc/sự/điều này" chains outside the "don't" table); sample lines natural. The risk is four rules carried over from EN that push output away from spoken Vietnamese. |

Total: 54 findings (6 over-corrections). Severity: High 5 · Med 21 · Low 28.

What changed since the earlier draft (git diff, read for over-corrections): the rewrite of `strings/vn.toml`, `core/vn/*` and `modules/vn/*` is a real improvement. Lines like "Không vội đâu. Quay lại thì nhắn 'ok rồi' nhé.", "Phải cược 1 triệu thì bạn chọn cái nào?", "Hôm nay xong rồi. Có tấm card này mình mới nhớ được bạn." read like a person. None of the rewrites I checked replaced natural Vietnamese with something worse.

Fix first (High): A1–A4 and O1. Next, O2 and O3, which change what the model writes in every post. Then A7, A12, A22, A23, C1–C3, C7, C9 and O5.

---

## A. Coach-facing lines: score 4, 33 findings

| # | Sev | Source | Line (exact) | Problem | Natural fix (same meaning, not longer) |
|---|---|---|---|---|---|
| A1 | High | core/vn/start-block.md:34 (step 5, Map line 1 template; shipped in both files) | `"{coach tự xưng} giúp {ai} đang "{lời khách}" {kết quả, nói theo khoảng}, bằng {cách làm}, chứ không {cách cũ}."` | The EN bio formula ("I help {who} who… {promise} with {method}, instead of {old way}") put into Vietnamese word for word: "giúp" (T1) + "bằng {cách làm}" (C11). "đang" + a quoted complaint breaks when the client's words are not a verb phrase. This is the centre of Day 0. | `"{ai} hay than "{lời khách}" thì tìm {coach tự xưng}: {cách làm}, không {cách cũ}, {kết quả, nói theo khoảng}."` |
| A2 | High | strings/vn.toml:240 `map.known` (rendered into start-block step 5, §CM-MAP) | `ĐƯỢC BIẾT ĐẾN VÌ:` | Passive calque of "KNOWN FOR:" (C4 "được"). First label on the Map. | `ĐIỀU KHÁCH NHỚ:` |
| A3 | High | strings/vn.toml:253 `setup.multi_income` | `Mình đoán: MỘT kiểu khách mua được hơn một thứ là {buyer}. Đúng không?` | English relative clause ("the ONE buyer who could buy more than one is…") plus capital-letter emphasis. A native reader has to parse it twice. | `Mình đoán {buyer} là kiểu khách mua được nhiều món nhất. Đúng không?` |
| A4 | High | strings/vn.toml:21 `verdict.ready` (quoted in core/vn/ship-check.md:30, :38 and §CM-EDGE) | `Sẵn sàng {verb} · Là mình thì đăng luôn: {evidence}` | "I'd post it" mistranslated as "if it were me I'd post right away". With the colon, the evidence reads as the thing to post. "đăng" is hard-coded while {verb} can be "quay"/"gửi" ("Sẵn sàng quay · … đăng luôn"). "Sẵn sàng + V" is the "Ready to" calque. | `Ổn rồi, {verb} được · viết từ {evidence}` |
| A5 | Med | strings/vn.toml:223 `liked.evidence` | `Sẵn sàng {verb} · Là mình thì đăng luôn: khung của họ, {fact} của bạn, không chép câu nào.` | Same defect as A4. | `Ổn rồi, {verb} được · khung của họ, {fact} của bạn, không chép câu nào.` |
| A6 | Low | strings/vn.toml:22 `verdict.ready_downgraded` | `Sẵn sàng {verb} · viết thành {evidence}` | "Sẵn sàng + V" calque; keep it in line with A4. | `Ổn rồi, {verb} được · viết thành {evidence}` |
| A7 | Med | strings/vn.toml:163 `claims.individual` (printed in public posts) | `kết quả cá nhân, không phải cam kết` | Calque of "individual result". Vietnamese disclaimers say results vary by person. | `kết quả tuỳ người, không phải cam kết` |
| A8 | Med | strings/vn.toml:191 `message.label.side_door` (+ modules/vn/message.md:16 "CỬA PHỤ", modules/vn/setup.md:17 "cửa phụ") | `Cửa phụ` | Literal "Side door". A coach sees it as a post label and doesn't know what it means. | `Bán kèm` |
| A9 | Med | strings/vn.toml:229 `review.labels`, :232 `review.best_label` | `Người giơ tay` · `nhiều người giơ tay nhất` | Marketing "hand-raisers" carried over. Native coaches count people who ask. | `Khách hỏi` · `nhiều người hỏi nhất` |
| A10 | Med | strings/vn.toml:122 `task.week.name` | `Tuần của bạn` | "Your week" app copy; also freezes "bạn" in a reminder title. | `Bài tuần này` |
| A11 | Low | strings/vn.toml:124 `task.numbers.name` | `Ngày số liệu` | "Numbers day" calque. | `Thứ Sáu xem số` |
| A12 | Med | strings/vn.toml:171 `msg.own_list` | `Mình chỉ viết cho danh sách của chính bạn, những người đã đồng ý nhận tin.` | "your own list, the people who…": "của chính" plus an English apposition. | `Mình chỉ viết cho danh sách bạn tự gom, người đã đồng ý nhận tin.` |
| A13 | Med | strings/vn.toml:221 `liked.no_watch` | `Mình không theo dõi kênh nào được, cũng không giả vờ là có.` | "and won't pretend to": a translated honesty disclaimer. A person wouldn't talk about "pretending". | `Mình không tự theo dõi kênh nào được đâu.` (rest unchanged) |
| A14 | Med | strings/vn.toml:252 `setup.guess_no_result` | `Mình đoán: chưa có kết quả của khách để kể, nên mình lấy chuyện của chính bạn. Đúng không?` | "Đúng không?" asks the coach to confirm the machine's own decision; "của chính bạn" calque. | `Chắc chưa có kết quả của khách để kể, đúng không? Vậy mình lấy chuyện của bạn.` |
| A15 | Med | strings/vn.toml:187 `message.drift.park` | `Chủ đề này quay lại {trigger}. … Viết thì tính là 1 bài ngoài bản đồ trong 10 bài.` | "comes back {trigger}" and "1 off-map post in 10" are both English frames. | `Khi {trigger} thì mình viết chủ đề này. … Viết thì tính là bài ngoài bản đồ, 10 bài chỉ được 1.` |
| A16 | Med | strings/vn.toml:186 `message.drift.bridge`, :188 `message.save.on_map` | `…xoay về ý lớn {n} là hợp bản đồ…` · `Đúng bản đồ: ý lớn {n}.` | The coach never saw "ý lớn": the Map says "3 CHỦ ĐỀ". "ý lớn 2" is internal jargon reaching the coach. | `…xoay về chủ đề {n} trên Bản đồ là hợp…` · `Đúng bản đồ: chủ đề {n}.` |
| A17 | Med | strings/vn.toml:196 `message.reason.tool` (shown as "Để dành: {lý do}") | `công cụ, không phải thông điệp` | "a tool, not a message": opaque calque. | `chỉ là công cụ, chưa phải ý chính` |
| A18 | Low | strings/vn.toml:198 `message.reason.risky` | `lời hứa rủi ro` | "risky claim" noun calque. | `dễ thành hứa quá lời` |
| A19 | Low | strings/vn.toml:199 `message.reason.too_early` | `đúng người, nhưng ở giai đoạn sau` | "right person, but at a later stage" stage-model phrasing. | `đúng khách, mà để sau mới hợp` |
| A20 | Low | strings/vn.toml:150 `angle.labels` (read by evals/graders.py via strings) | `AI CŨNG NÓI · CHƯA AI NÓI · BẠN NÓI ĐƯỢC` | In capitals inside an AI product, "AI CŨNG NÓI" reads first as "AI also says". | `KÊNH NÀO CŨNG NÓI · CHƯA AI NÓI · BẠN NÓI ĐƯỢC` |
| A21 | Low | strings/vn.toml:242 `map.word`, :243 `map.voice`, :229 `review.labels` ("Thông điệp của bạn"), :216 `liked.saved` ("Bài bạn thích") | `TỪ KHOÁ CỦA BẠN:` · `GIỌNG CỦA BẠN:` · `Thông điệp của bạn` · `Bài bạn thích` | "bạn" frozen in labels, while the machine calls the coach chị/anh from reply 2 (VN4 drift). The "(Cần chị)" example in XƯNG HÔ covers it only by inference. | Drop the pronoun: `TỪ KHOÁ:` · `GIỌNG:` · `Thông điệp` · `Bài đã lưu`. Or add "nhãn cũng đổi theo cặp" to XƯNG HÔ. |
| A22 | Med | strings/vn.toml:180 `proof.intake` (§CM-GUARDRAILS) | `Kết quả này có lưu lại không, khách có đồng ý bằng văn bản cho dùng trong bài đăng, quảng cáo hay case study không?` | Two questions fused into one form sentence, in legal register. | `Kết quả này có lưu lại không? Khách nhắn đồng ý cho đăng bài, quảng cáo, case study chưa?` |
| A23 | Med | strings/vn.toml:154 `cta.default` (printed in every FILM TODAY caption, §CM-CTA-KIT 1) | `Comment {KEYWORD}, mình gửi bạn {gift} qua inbox.` | No quiet route for people who feel "ngại". By the standard's own VN8 row this scores 1, and it contradicts §CM-NATURAL 6 and its example. | `Comment {KEYWORD} hay nhắn riêng, mình gửi {gift}.` |
| A24 | Low | strings/vn.toml:157 `cta.platform_note` | `Lưu ý nền tảng (tính đến {date}):` | "Platform note (as of {date})" calque; every other dated note says `Lưu ý ({date}):`. | `Lưu ý ({date}):` |
| A25 | Low | strings/vn.toml:156 `cta.not_pushy` | `Comment từ khoá là người xem nhận được thứ có ích thật, đâu có ép ai.` | The "là" chain switches subject mid-sentence. | `Người xem comment là nhận được thứ có ích thật, đâu có ép ai.` |
| A26 | Low | strings/vn.toml:182 `liked.copy_note` | `Nền tảng có thể giảm hiển thị bài na ná bài khác, mà chữ cũng là của họ.` | "The platform may…" as agent subject. | `Bài na ná bài khác dễ bị giảm hiển thị, mà chữ cũng là của họ.` |
| A27 | Low | strings/vn.toml:127 `levelup.offer_nudges` | `Bạn đi trọn một tuần rồi đó.` | "đi trọn" is an odd verb for "kept it up a full week". | `Bạn theo đủ một tuần rồi đó.` |
| A28 | Low | strings/vn.toml:205 `research.later` | `Để sau: một bước 10 phút trong Tuần 1.` | "a 10-minute step in Week 1" noun-phrase calque. | `Để Tuần 1 làm, 10 phút thôi.` |
| A29 | Low | core/vn/start-block.md:30 (reply 1, said word for word) | `2) Mình tìm ra MỘT điều để khách nhớ bạn.` | Capitals as English "ONE" emphasis; Vietnamese stresses with "đúng". | `2) Mình tìm ra đúng một điều để khách nhớ bạn.` |
| A30 | Low | strings/vn.toml:227 `review.ask` | `(bài đăng từ 2 ngày)` | Ambiguous: from day 2, within 2 days, or 2+ days old? | `(bài đăng được 2 ngày)` |
| A31 | Low | strings/vn.toml:239 `setup.dump_posts` (rendered into reply 2) | `Có bài hay tin nhắn bạn từng viết thì dán 2–3 cái luôn…` | "bài hay" first reads as "good posts". | `Có bài đăng hoặc tin nhắn bạn từng viết thì dán 2–3 cái luôn…` |
| A32 | Low | strings/vn.toml:209 `research.paste_steps` | `Chép 10-20 bài hay comment ở 3 chỗ khách bạn hay trò chuyện mà không ai bán hàng.` | Three different "hay" in one line ("or", "good", "often"), plus a trailing relative clause. | `Chép 10–20 bài đăng hoặc comment ở 3 chỗ khách bạn hay vào nói chuyện, chỗ không ai bán hàng.` |
| A33 | Low | strings/vn.toml:71 `anchor.research-lite` (+ modules/vn/research.md:9 "LẮNG NGHE NHANH") | `Lắng nghe nhanh` | "Quick Listen" calque; reaches the coach if the model names the step. | `Nghe khách nói gì` |

Lines checked and natural (no finding): all `talk.*`, `card.stop_lines`, `card.save_line`, `card.fix_*`, `verdict.needs`, `verdict.draft_*`, `verdict.hardstop`, `verdict.override`, `check.bet`, `character.bet`, `resume.brb`, `setup.cut_off`, `setup.link_unread`, `setup.no_setup`, `dump.keep_going`, `month.*`, `angle.offer`, `film.*`, `tick.*`, `ask3.*`, `research.ask3*`, `research.drip`, `signature.*`, `voice.*`, `liked.*` (except A5, A13, A26), `levelup.*` (except A27), `mic.*`, `ics.*`, `starthere.*`, `phone.opening`, `phone.save`, `map.ok`, the XƯNG HÔ question, and replies 2, 3 and 9 of Day 0.

## B. Instruction block as language the model imitates: score 4, 5 findings

The block reads like a Vietnamese team lead's notes: short, imperative, spoken ("làm luôn trong chat, viết xong rồi mới giao", "Coach chọn gì theo nấy, không theo chữ lọt trong câu", "giục gấp chỉ khi gấp thật", "quan điểm có người cãi"). It has no essay connectors and no nominalised chains. The quoted lines the model copies are natural. The Map template (A1) is the one translated pattern the model will reproduce for every coach; it is counted in A.

| # | Sev | Source | Line (exact) | Problem | Natural fix |
|---|---|---|---|---|---|
| B1 | Low | core/vn/start-block.md:24 | `chị → em–chị (lễ phép, có "Dạ")` | No dose. The model will put "Dạ… ạ" on every message, which is the page-staff voice guide §4.5 warns about. | `chị → em–chị ("Dạ" khi đáp, không câu nào cũng "ạ")` |
| B2 | Low | core/vn/start-block.md:31, 32, 34, 38 (+ `mic.claude_vn`) | `Bạn cứ xả hết ra nhé` · `kể thêm nhé` · `Mình chạy thử 4 tuần nhé` · `Quay video hôm nay nhé` | Five quoted lines hard-code Bắc "nhé" and nothing tells the machine to say "nha" to a Nam coach, so it sounds Northern to everyone. | Add to XƯNG HÔ: `tiểu từ theo giọng coach (Nam: nha)`. |
| B3 | Low | core/vn/start-block.md:29, 33 (also §CM-MESSAGES 5, §CM-NUMBERS 6, §CM-MONTH 2) | `MỘT quyết định` · `chọn MỘT kiểu khách` · `MỘT câu hỏi` · `MỘT chỗ gãy` · `chỉnh MỘT dòng` | Capitals as English "ONE" emphasis. The model carries it into coach lines (A3, A29). | `đúng một` / `chỉ một`. |
| O5 | Med | core/vn/start-block.md:48 (TIẾNG VIỆT line; the only particle rule in phone and compact mode) | `tiểu từ đúng vùng coach (Bắc: nhé, nhỉ · Nam: nha, nè), không trộn` | Over-correction. Region beats the coach's own posts: a young Bắc coach whose posts say "nha" gets "nhé" (VN5 says keep "nha"). There is no Trung row, so a Huế or Đà Nẵng coach gets Bắc or Nam. | `tiểu từ theo bài coach, chưa có thì theo vùng (Bắc nhé · Nam nha · Trung nghe), không trộn` |
| O6 | Low | core/vn/start-block.md:46 (LỜI HỨA) | `không "cam kết", "đảm bảo", "chắc chắn"` | Over-correction. A bare-word ban also removes playful spoken uses that promise nothing (the guide §4.2 mình–bạn row uses "đảm bảo" as a joke). The legal target is a promised result. | `không "cam kết / đảm bảo / chắc chắn" + kết quả` |

## C. Method file: score 4, 16 findings

Sample lines are natural: §CM-NATURAL 8's three pairs, "bạn còn đi làm hay nghỉ hẳn rồi?", "để mình gửi lịch", "nhắn lại mình một câu", the TALK question, the month check, "Phần 2 mai lên", the hard-stop line, the "coach lùa gà" polarity example, "Tháng cô hồn", "NHẬT KÝ ZALO", 'ý chính nằm trước "Xem thêm"'. Instruction prose has no Tuy nhiên / Do đó / Điều này outside the "don't" table. The 18 "việc" and 26 "được" hits are concrete nouns and "can", not nominalisations or passives. The problems are rules carried over from EN, plus a few labels.

| # | Sev | Source | Line (exact) | Problem | Natural fix |
|---|---|---|---|---|---|
| C1 | Med | modules/vn/review.md:22 (§CM-NUMBERS 6) | `không xem hết → cắt dạo đầu` | "dạo đầu" alone carries the "màn dạo đầu" sense. The model will echo it in "Chỗ chưa ổn". | `không xem hết → cắt đoạn mở vòng vo` |
| C2 | Med | modules/vn/convert.md:23 (§CM-CTA-KIT 9) | `"Không dành cho bạn nếu…"` | "Not for you if…" sales calque, and it locks "bạn" (wrong for a 45+ audience). | `"Lớp này không hợp với ai đang…"` |
| C3 | Med | modules/vn/fmt-short.md:44 (§CM-MESSAGES 5) | `Tin 1 = cảm ơn + đủ quà + MỘT câu hỏi` | Thanks-first is the customer-service opener (guide X7). Vietnamese inbox replies open with "Dạ" and send the thing. | `Tin 1 = "Dạ" + gửi quà đủ + một câu hỏi` |
| C4 | Low | modules/vn/fmt-short.md:25 (§CM-FORMATS, KIỂU VIỆT) | `Góc nhìn của một {nghề}` | "POV of a {job}" with the translated article "một" (C12). | `Góc nhìn {nghề}` |
| C5 | Low | modules/vn/humanize.md:44 (§CM-NATURAL 7) | `chúng tôi, chúng ta → bên mình, tụi em, chị em mình` | "tụi em" is Nam/Trung; a Bắc coach would say "bọn em". | `bên mình, tụi em / bọn em (Bắc), chị em mình` |
| C6 | Low | modules/vn/humanize.md:30 (§CM-NATURAL 4) | `Trung nghe, hỉ` | No dose. Dense "hỉ" reads as mockery of the accent (guide §4.6). | `Trung nghe (hỉ thì một lần)` |
| C7 | Med | modules/vn/locale.md:11 (§CM-LOCALE 1) | `em – anh chị (khách 30+)` | Ties self-"em" to the client's age, not the coach's. Drops "mình – anh chị", the safe default for owners 35+ (guide §4.1, §4.4.6). A 45-year-old coach would be told to call himself "em". | `mình – anh chị (chủ quán, chủ shop 30+) · em – anh chị (coach nhỏ tuổi hơn khách)` |
| C8 | Low | modules/vn/fmt-short.md:42 (§CM-MESSAGES 3) | `"Muốn dừng nhận tin, nhắn DỪNG."` | SMS-gateway tone inside a coach's personal Zalo. | `"Không muốn nhận nữa thì nhắn mình chữ DỪNG."` |
| C9 | Med | modules/vn/talk.md:11 (§CM-TALK 2, slotted into `talk.question`) | `5 làm vậy có kết quả, người ta nói gì (tuần 4: có người gật đầu mua, vì sao họ gật)` | Slotted in, it gives "Kể mình nghe lần làm vậy có kết quả, người ta nói gì. Lúc đó ra sao?": no subject and two questions. Week 4 has the same problem. | `5 có người làm vậy ra kết quả (tuần 4: có người gật đầu mua)`. "Lúc đó ra sao?" already asks what they said and why. |
| C10 | Low | modules/vn/review.md:13, 17 (§CM-NUMBERS 2–3, hard-coded, not the string) | `Người giơ tay: {n} comment {KEYWORD} · …` · `Người giơ tay trước, lượt xem phụ.` | Same calque as A9, but hard-coded here, so it needs its own fix. | `Khách hỏi: {n} comment {KEYWORD} · …` · `Khách hỏi trước, lượt xem phụ.` |
| C11 | Low | modules/vn/fmt-short.md:36 (§CM-POSTS 7) | `Ca khách:` | "client case" calque. | `Chuyện khách:` |
| C12 | Low | modules/vn/guardrails.md:12 (§CM-GUARDRAILS) | `LẶNG LẼ:` | Literary word for "silently"; the rest of the file says "thầm". | `SỬA THẦM:` |
| O1 | High | modules/vn/edge-rubric.md:13 (§CM-EDGE CỔNG, Giọng) | `câu hỏi chỉ ở lời mời` | Over-correction, from EN "questions only in the CTA". It bans the Vietnamese questions the guide recommends: hooks that call out a group with a question (§3.5 F), real narrow questions (§3.6), mid-story check-ins (§3.10), and quoting an objection then answering it (§3.8 #6, K4). The model will flatten hooks into statements. | `câu hỏi tu từ thì trả lời liền; không mở bằng "Bạn có biết…?"` |
| O2 | Med | modules/vn/fmt-short.md:13 (§CM-FORMATS 2) | `nối bằng "nhưng", "nên", không "rồi thì"` | Over-correction, from EN "but / therefore, never and then". It prefers the written "nhưng" over spoken "mà", and sidelines "rồi, xong, thế là", which §CM-NATURAL 3 asks for. The two anchors conflict. | `nối bằng "mà", "nên", "thế là", không xâu "rồi… rồi…" mà không có ngoặt` |
| O3 | Med | modules/vn/humanize.md:14 (§CM-HUMANIZE 3) | `rào đón (có lẽ, hình như, mình nghĩ là) · từ đệm (kiểu như, thực ra thì)` | Over-correction. "mình thấy / mình nghĩ là / theo em" is how Vietnamese soften a hot take (guide §4.3, §4.7; the em–anh chị pair needs it), and "kiểu như" is a common spoken connector (§3.3). Only stacked hedges and filler the machine adds itself should go. | `rào chồng (có lẽ, hình như, có thể… xếp chồng) · từ đệm máy tự thêm; giữ một "mình thấy / theo em" trước câu gắt` |
| O4 | Low | modules/vn/fmt-short.md:32 (§CM-POSTS 3) | `Đoạn 2–3 câu` | Over-correction, from EN "paragraphs of 2–3 sentences". It gives every coach the same rhythm. Guide §3.12: 40+ coaches write 3–5-sentence paragraphs; don't make every paragraph alike (VN7 rhythm). | `Đoạn dài ngắn theo bài coach, thường 2–4 câu` |

## Notes (not counted)

- **Gap, VN4:** §CM-CTA-KIT 3 ("Trả lời dưới bài: ≥5 câu ngắn xoay vòng") gives no pair rule for comment replies. A commenter who writes "c ơi" should get "em" back, not "bạn" (guide §4.4 #5; VN4 = 0 in the standard).
- **Gap, exemplars:** the method file holds almost no complete Vietnamese post, script beat or Zalo message, only §CM-NATURAL 8's three pairs. Wherever the coach has no dump or posts yet, the model falls back on its default Vietnamese. One short annotated script and one Zalo reply would teach the model more than another rule.
- **Process:** §CM-NATURAL 2 and 3 ship two guide examples taken from §1 and §2.7. Guide §0 says pack examples come only from §3 and §8 and must pass the I19 copy check. This is not a naturalness defect, but it is worth re-running the copy check.
- Nothing in the build trips the mechanical markers in a way that matters. "Tuy nhiên / Do đó / Bên cạnh đó / Điều này / một cách / rằng / chúng tôi" appear only inside the §CM-NATURAL "don't → write" table and the "bad" half of its examples.

---

## Fix round

Applied 6 Oct 2026 to the VN sources (`strings/vn.toml`, `core/vn/start-block.md`, `core/vn/ship-check.md`, `modules/vn/*.md`). Every key, section id, `src` hash, `{{t:}}` tag, `{slot}` and param is unchanged. Yardstick: guide §2.7 (don't over-correct). Not committed.

**Tally (54):** 47 applied (some as a variant, reason given) · 5 applied in part (the rest declined, reason given) · 2 declined. Of the 3 uncounted notes, 1 was applied, 1 was checked and found clean, and 1 is still open.

### A. Coach-facing lines

| # | Outcome | What changed / why not |
|---|---|---|
| A1 | applied (variant) | Map line 1 → `"{ai} hay than "{lời khách}" thì tìm {coach tự xưng}: {cách làm} chứ không {cách cũ}, {kết quả, nói theo khoảng}."` Kept "chứ không" because it's the native contrast (guide N3). |
| A2 | applied | `map.known` → `ĐIỀU KHÁCH NHỚ:` |
| A3 | applied | `setup.multi_income` → `Mình đoán {buyer} là kiểu khách mua được nhiều món nhất. Đúng không?` |
| A4 | part | Fixed the mistranslation and the hard-coded "đăng": `verdict.ready` → `Sẵn sàng {verb} · viết từ {evidence}`; the ship.card and ship.task PRINT lines now match. Declined "Sẵn sàng" → "Ổn rồi": "sẵn sàng + V" is native Vietnamese (§2.7), and "Sẵn sàng" is the Ready key in `tools/cmcore/checks.py` READY_PREFIXES / `_CONDITIONAL_READY`, the edge rule "không 'Sẵn sàng sau khi…'" and the eval not_regexes. |
| A5 | part | `liked.evidence` → `Sẵn sàng {verb} · khung của họ, {fact} của bạn, không chép câu nào.` Kept "Sẵn sàng" (reason as A4). |
| A6 | declined | `verdict.ready_downgraded` already reads "Sẵn sàng {verb} · viết thành …", which matches A4's kept prefix. Same reason as A4. |
| A7 | applied | `claims.individual` → `kết quả tuỳ người, không phải cam kết` (kit LỜI HỨA, §CM-FORMATS 6, §CM-POSTS 7). |
| A8 | applied | `Cửa phụ` → `Bán kèm`; also message.md "CỬA PHỤ" → "BÁN KÈM" and setup.md "cửa phụ" → "bán kèm". |
| A9 | applied | `review.labels` "Khách hỏi"; `review.best_label` "nhiều người hỏi nhất". |
| A10 | applied | `task.week.name` → `Bài tuần này`. |
| A11 | applied (variant) | → `Số liệu thứ Sáu`, not "Thứ Sáu xem số", because "xem số" can read as lottery or fortune-telling. This also matches `ics.friday.summary`. |
| A12 | applied (variant) | `msg.own_list` → `Mình chỉ viết cho danh sách bạn tự gom, ai đồng ý nhận tin rồi mới gửi.` This removes the apposition too. |
| A13 | applied | `liked.no_watch` → `Mình không tự theo dõi kênh nào được đâu.` (rest unchanged). |
| A14 | applied | `setup.guess_no_result` → `Chắc chưa có kết quả của khách để kể, đúng không? Vậy mình lấy chuyện của bạn.` |
| A15 | applied (variant) | `message.drift.park` → `… Chờ {trigger} rồi mình viết. … Viết thì tính là bài ngoài bản đồ, 10 bài chỉ được 1.` "Khi {trigger} thì" breaks on the trigger "mùa sau"; "Chờ … rồi" fits every trigger. |
| A16 | applied | `message.drift.bridge` → `Bài này xoay về chủ đề {n} là hợp bản đồ…`; `message.save.on_map` → `chủ đề {n}`. Also changed review.md "Tuần sau: chủ đề {n}" (the same coach-facing name). |
| A17 | applied | `message.reason.tool` → `chỉ là công cụ, chưa phải ý chính`. |
| A18 | applied | `message.reason.risky` → `dễ thành hứa quá lời`. |
| A19 | applied | `message.reason.too_early` → `đúng khách, mà để sau mới hợp`. |
| A20 | declined | `angle.labels` kept. "AI CŨNG NÓI" always sits next to "CHƯA AI NÓI", and the pair reads as "ai" (who). Changing it would rewrite about 25 regexes in liked.vn.toml for a Low finding. Left for the native reviewer. |
| A21 | part | Dropped the pronoun: `TỪ KHOÁ:`, `GIỌNG:`, review label "Thông điệp" (and the hard-coded line in review.md). Kept "Bài bạn thích": it's the name of the saved list in start-block and §CM-LIKED, it already flips with the pair ("Bài chị thích", tested in liked.vn), and "Đã lưu vào Bài đã lưu" reads worse. |
| A22 | part | `proof.intake` → `Kết quả này có lưu lại không, khách đã nhắn đồng ý cho đăng bài, quảng cáo, case study chưa?` This drops the legal register ("bằng văn bản", "cho dùng trong"). Declined splitting it into two questions: the reply limit is ≤1 question, and grader I5 counts every "?". |
| A23 | applied | `cta.default` → `Comment {KEYWORD} hay nhắn riêng, mình gửi {gift}.` (quiet DM route, VN8). |
| A24 | part | Dropped "tính đến": `Lưu ý nền tảng ({date}):`. Kept "nền tảng": evals/graders.py recognises the required platform note by its fixed opening before `{date}` (≥8 chars). "Lưu ý (" alone is too short and would match every other dated note. |
| A25 | applied | `cta.not_pushy` → `Người xem comment là nhận được thứ có ích thật, đâu có ép ai.` |
| A26 | applied | `liked.copy_note` 2nd sentence → `Bài na ná bài khác dễ bị giảm hiển thị, mà chữ cũng là của họ.` The copy-note marker (first sentence) is unchanged. |
| A27 | applied | `Bạn theo đủ một tuần rồi đó.` |
| A28 | applied | `research.later` → `Để Tuần 1 làm, 10 phút thôi.` |
| A29 | applied | Reply 1 → `Mình tìm ra đúng một điều để khách nhớ bạn.` |
| A30 | applied (variant) | `(bài đăng đủ 2 ngày)`, which matches review.md "bài chưa đủ 2 ngày". |
| A31 | applied (variant) | `Có bài đăng, tin nhắn bạn từng viết…`. A comma instead of "hoặc" fixes the same misread and costs 4 fewer characters, which matters with the kit at 7,499/7,500. |
| A32 | applied | `Chép 10–20 bài đăng hoặc comment ở 3 chỗ khách bạn hay vào nói chuyện, chỗ không ai bán hàng.` |
| A33 | applied | `anchor.research-lite` → `Nghe khách nói gì`; research.md heading "NGHE KHÁCH NÓI GÌ"; setup.md step 3. |

### B. Instruction block

| # | Outcome | What changed / why not |
|---|---|---|
| B1 | applied (variant) | `chị → em–chị ("Dạ" khi đáp, không rải "ạ")`, shorter than the proposal to fit the kit budget. |
| B2 | applied (variant) | Folded into the O5 line as "…, cả câu mẫu, không trộn" instead of a separate XƯNG HÔ clause, so particles in quoted lines follow the coach too. |
| B3 | applied | Every "MỘT" in VN sources is now "một" (start-block, §CM-FORMATS 1, §CM-MESSAGES 5, §CM-NUMBERS 6, §CM-MONTH 2, §CM-CTA-KIT 6, §CM-LIKED 8, §CM-LOCALE 1). Reply 1 uses "đúng một"; the step-5 "Quyết định duy nhất" already carries the emphasis. |
| O5 | applied | `tiểu từ theo bài coach, không thì theo vùng (Bắc nhé · Nam nha · Trung nghe), cả câu mẫu, không trộn` (kit and phone). |
| O6 | applied | `không "cam kết, đảm bảo, chắc chắn" + kết quả, …`. This also removes the conflict with "cam kết cách làm" in §CM-CTA-KIT 9 and §CM-POSTS 7. |

### C. Method file

| # | Outcome | What changed / why not |
|---|---|---|
| C1 | applied (variant) | `không xem hết → cắt bớt đoạn mở` (8 B cheaper than "đoạn mở vòng vo"). |
| C2 | applied (variant) | `"Không hợp với ai đang…"`, without "Lớp này" because the offer isn't always a class. §CM-EDGE "không dành cho (bạn)" changed to "không hợp với ai" to match. |
| C3 | applied | `Tin 1 = "Dạ" + đủ quà + một câu hỏi`. |
| C4 | applied | `Góc nhìn {nghề}`. |
| C5 | applied (variant) | `bên mình, tụi/bọn em, chị em mình`. |
| C6 | applied (variant) | `Trung nghe, ít hỉ`. The same line already doses every particle ("không câu nào cũng có"), so a short cap was enough. |
| C7 | applied | §CM-LOCALE 1 now offers `mình – anh chị (khách 30+) · em – anh chị (coach trẻ hơn khách)` next to the other pairs. |
| C8 | applied | `"Không muốn nhận nữa thì nhắn mình chữ DỪNG."` |
| C9 | applied | TALK question 5 → `có người làm vậy ra kết quả (tuần 4: có người gật đầu mua)`. |
| C10 | applied | review.md "Khách hỏi:" ×3 ("cái kéo khách hỏi", "không ai hỏi →"). |
| C11 | applied | `Chuyện khách:`; convert.md "chuyện khách" to match. |
| C12 | applied | `SỬA THẦM:`. |
| O1 | applied (variant) | `câu hỏi chỉ ở lời mời` → `hỏi tu từ thì đáp liền`. The "Bạn có biết…?" opener ban already sits in §CM-NATURAL 7, so it isn't repeated here (bytes). |
| O2 | applied | `nối bằng "mà", "nên", "thế là", không xâu "rồi… rồi…"`. |
| O3 | applied (variant) | Cut list is now `rào chồng, rào trước điều họ biết chắc (…) · từ đệm máy tự thêm (…)`, and Giữ gains `một "mình thấy" trước câu gắt`. Hedges before a known fact are still cut, so edge-rubric.vn.010 holds. |
| O4 | applied | `Đoạn theo bài coach, thường 2–4 câu`. |

### Notes (uncounted)

- **Comment-reply pair (VN4):** applied. §CM-CTA-KIT 3 now has "xưng theo người comment".
- **I19 copy check:** re-run on the rendered dist/vn files against all of evals/personas/vn/ (8-tiếng window, `copy_tokens`). §CM-NATURAL 2–3 examples: 0 runs. The only shared runs (4) are product lines that persona expected and answers files quote back (mic tips, the Zalo ask-3 line, `liked.cant_open`), so no contamination. The guide §0 "only §3/§8" process rule is still the guide owner's call.
- **Exemplars gap:** open. There is no byte room left (see sizes).

### Eval cases kept in step (VN only; no EN case, evals/runs or g1 file touched)

Regexes that quoted changed strings now accept the new wording: guardrails.vn (claims line), message.vn (`kiểu khách mua được nhiều món`; `chủ đề|ý lớn n`; "10 bài chỉ được 1"; `cửa phụ|bán kèm`; new park reasons), brain.vn (`chủ đề|ý lớn n`), liked.vn and router.vn (`không (tự) theo dõi kênh … được`), liked.vn and humanize.vn (`liked.evidence`), edge-rubric.vn and fmt-short.vn (Ready-line not_regexes now also catch "· viết từ"). Several of these were already stale from the earlier rewrite ("Mình sẽ đăng", "kênh của ai"). Header comments that cite the old "Mình sẽ đăng → Em sẽ đăng" pair-swap example are unchanged; the example no longer applies because `verdict.ready` has no pronoun now.

### Final sizes (python3 tools/build.py --edition all)

| Artifact | Before | After | Budget |
|---|---|---|---|
| vn/1-INSTRUCTIONS.txt | 7,481 ch | **7,499 ch** (9,564 B) | 7,500 ch |
| vn/PHONE-STARTER.txt | 7,239 ch | **7,257 ch** (9,313 B) | 7,500 ch |
| vn/CONTENT-MACHINE-VN.md | 56,246 B | **56,304 B** | 56,320 B |
| largest anchors | MAP 3,385 B | MAP 3,360 · NATURAL 3,208 · SETUP 3,202 · CARD 3,181 · EDGE 3,172 B | 3,600 B each |
| Ship cards | | ship.kit 915 · ship.card 980 · ship.task 816 ch | 1,000 ch |

The kit is 1 character under budget and the method file 16 bytes under, so any further VN addition needs a cut first. Step 7 lost "nhắn qua Zalo, Messenger" (the `{{cta_channel}}` line already names both) to make room.

Checks: `python3 tools/lint.py` gives 0 errors and 30 warnings (W201 budget-near, W202 unused EN keys, as before). `python3 -m unittest discover -s tools/tests` ran 336 tests: OK.

### Open (for the founder's human native reviewer)

1. A1: "hay than" fits a complaint. Check niches where the client's words are a wish ("muốn tự quay video"); "hay nói" would be the fallback.
2. A4/A6: keep "Sẵn sàng {verb}" or switch to "Ổn rồi, {verb} được". Switching also means updating READY_PREFIXES and `_CONDITIONAL_READY` in tools/cmcore/checks.py, the edge rule and the eval not_regexes.
3. A20: "AI CŨNG NÓI" ambiguity. If it changes, about 25 regexes in liked.vn.toml must follow.
4. A8: does a coach read "Bán kèm" as "the other thing you still sell"?
5. Legal and native: "kết quả tuỳ người, không phải cam kết" and `proof.intake` "nhắn đồng ý" (instead of "bằng văn bản") need the compliance_pack lawyer (editions/vn.toml PENDING).
6. C3: "Dạ" opening inbox Tin 1 for mình–bạn coaches with young audiences.
7. Regional rows: Trung "nghe, ít hỉ", "tụi/bọn em", and particles in quoted lines (guide §10.5).
8. qa/standards/offer-post.md (lines 62, 75) still names "Không dành cho bạn nếu…" as the not-for form. The standard's owner should align it with C2.
9. The exemplars gap needs a budget decision (raise the 56,320 B cap or move exemplars out of the method file).
