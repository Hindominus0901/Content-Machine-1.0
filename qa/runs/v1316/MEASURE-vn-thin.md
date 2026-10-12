# MEASURE · v13.16 founder rule "một ý là đủ, máy mở rộng từ nền đã có" · vn/copywriter-thin

Lengths are counted in tiếng separated by whitespace. For a video, the count runs from Câu đầu to Câu cuối; for a long post, it covers the whole box.

| # | Check | Day-0 (T17, video) | N2 (T19, long post) | N3 (T20, video) |
|---|---|---|---|---|
| 1 | Length floor | 516 ≥ 500 ✓ | 974 ≥ 950 ✓ | 516 ≥ 500 ✓ |
| 2 | Anchor | chunk 2: "why before how", "send one email to one person… is marketing"; T10 August result; T9 method | chunk 3: two layers of research, "understand the client from their point of view"; T9 delivery; T8 "she never listened to her own clients" | W1: "Khách không đến từ bài đăng…"; chunk 1: "trust you, know you're there"; T11: 9 coaches, mostly referrals; T14: the goal "I read your post" |
| 3 | Untraceable facts | 0 | 0 hard, 1 borderline: in para 11, the example quote "làm hoài mà không xong việc", marked "Ví dụ thôi" and listed | 0 hard, 1 borderline: in Ý1, "câu trả lời ít khi nằm ở bài hôm nay", a generalisation stretched from W1 |
| 4 | "Máy tự thêm" | đoạn 9 (the do-today step and its example) ✓. Ý1–4 are grounded and correctly not listed | 10, 11, 13, 14, 16, 18 ✓ (how-to, self-test, consequence, examples, the "phía bạn" contrast, gift usage). Paras 5, 9, 12, 15 hold grounded glue and are correctly not listed | đoạn 8 (the exercise + example) ✓. Gap: Ý5 "Bạn bè thì đã tin sẵn rồi" is the machine's own assumption, and it is not listed |

5. **Story ask:** none. No slot lacked an anchor, so no "Cần" line asked for a story. The only nudge was the kit's topic hint during the dump at T3 ("một khách cụ thể bạn từng giúp"), which does not ask for a story for a slot. The 6 interview questions left no turn for the client-words question in §CM-DIG.
6. **Quality read:** mostly her teaching. Some examples are generic filler.
   - Reads as hers (N2 ¶5): "Đọc vài bài là đọc chữ của người khác viết về khách. Nhờ AI tìm từ khoá là đọc lại chữ đó lần nữa, gọn hơn." This develops her own line "I read a few posts and ask the AI for keywords. That is not research."
   - Generic filler (N3 Ý4): "Ví dụ, thứ Hai bạn nói về cách viết tiêu đề, thứ Ba về một chuyến đi chơi, thứ Tư về một công cụ mới." Any content coach could have written it. N2 ¶11's "nâng cao hiệu suất" example is in the same tier.
   - Pattern: the floors were met mostly with *listed* machine paragraphs. N2 has 6 of 20 paragraphs listed, and they total ~350 of its 974 tiếng. The first drafts ran 455/653/348 tiếng; the floor, not the coach's material, drove the expansion.
7. **"Why this one" / research:** no VÌ SAO line is printed under any post. The card's machine block has a `why_this_one:` field, which the card spec requires, so it is not in the visible text. The research "nothing read" line at T16 reads "Chưa đọc được trang nào… (mình đoán cả mục này)", so it carries the guess tag ✓.
8. **Minutes to the Day-0 piece:** 26.7 (active; no `away_min` before it).

## Grader fails: real vs misread
- **Real:**
  - deny_list: bare "Trụ cột" at T14.
  - style: the "Cần" line is 25 tiếng, over the limit of 20.
  - day0_shape: `{tên}` placeholders left in the gift and inbox reply.
  - hook_lab: the gift email's subject is not a hook frame.
  - week_dedupe #1: the Day-0 hook is repeated in N2 ¶8.
  - I23: own phrases appear in 17% of pieces, against a minimum of 50%.
  - day0_timing: the strategy finishes at 25.2 against a limit of 25. That is 0.2 over, partly from how the sim models time.
- **Misread or arguable:**
  - day0_shape "CTA HỎI GIÁ vs YOUR WORD": §CM-CTA-KIT 1 gives QUAY HÔM NAY a comment word taken from the hook, not the season keyword.
  - week_dedupe #2: a "Phần 2 mai lên: ba câu vì sao" teaser shares words with Day-0 Ý2 by design.
  - week1_plan: "Người lạ nhắn khi đã tin" and "Gốc là gói" are different ideas that share the THU HÚT/video label.
  - I9: "không ai hỏi giá" is the machine's own guess at the keyword (tagged "(mình đoán)" at T16), not a quote. The card spec's quoted `"{từ khoá}"` slot makes it look like one. Half real: the card should drop the quotes or keep the guess tag.
