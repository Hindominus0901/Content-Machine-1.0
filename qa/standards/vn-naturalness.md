# Vietnamese naturalness standard (`vn-naturalness`)

Build-only rubric. Never shipped: lint E153 keeps `qa/` out of every zip. It is the G3 judge rubric and the native-reviewer sheet for **every Vietnamese piece** the machine writes (posts, scripts, captions, Zalo and inbox messages, comment replies, offer lines) and for the machine's own Vietnamese to the coach. It answers the founder's ask: the Vietnamese must read like a Vietnamese person talking or posting, not like a translation from English.
Sources, in order: `docs/research/vn-language-guide.md` (source of truth; §2 catalogue, §3 story linking, §4 register, §5 selling, §9 tests) · `docs/research/vn-language-anchor-draft.md` (what the model is told) · `shared.md` SG4, SG8 · `email-zalo.md` EM3, EM7 · wf14 §5 (sounds like the coach).

## Purpose

One question: **would a Vietnamese reader believe this coach typed or said every line, to them, in Vietnamese?** Word choice, sentence order, connectors and story flow, xưng hô, particles, no translationese, this coach's own voice, and a CTA that asks the Vietnamese way.

## Scope

- **Applies to:** every VN piece of 15 tiếng or more, on top of its format standard, which must pass first (`shared.md` → format standard → this file). Under 15 tiếng: VN4, VN5, VN6 only.
- **Also applies to:** the machine's prose to the coach (VN4 uses the machine–coach pair, `pronouns`; VN7 and VN8 are N/A).
- **Not here:** truth, claims, polarity, copy distance, Edge (`shared.md`); length and format items (format standards). A banned tell is also a `shared.md` SG4 lint fail; this file scores the rest of the language.
- **Evidence the judge must have:** the piece; the coach's dump and any pasted posts (`answers.md` / Bank V-rows); the Brand Card voice fields (`audience_address` public and 1:1, `dialect`, `phrases`, `openers_closers`, `code_mix`, `never_say`, `do_say`); the lint and grader output (E141 / I23 and the density counts in guide §9.3).

## Items

| ID | Item | 0 | 1 | 2 | Critical |
|---|---|---|---|---|---|
| VN1 | Word choice | ≥3 book or translated words where speech has its own (rất / vô cùng before adjectives, cảm thấy, khách hàng, sở hữu, trải nghiệm, giải pháp, thực hiện, Hán Việt in a script: nhằm, gia tăng, tiếp cận, cải thiện), or English the coach does not use | 1–2 such words | The coach's everyday words: lắm / quá / thiệt after the adjective, thấy, khách, "cái" + noun; English only from `code_mix`; emotion in plain words (sợ, ngại, mừng, quê) | no |
| VN2 | Sentence order | Most sentences use the English subject–predicate frame: a long subordinate clause first (Mặc dù…, Sau khi…, Để…,), "việc / sự" as subject, passive "được… thiết kế", a stacked modifier block, or any sentence ≥40 tiếng in a script | 1–2 such sentences | Topic first, then thì / là / mà where it fits; subjects dropped once clear; one breath per sentence; long and short mixed with ≥1 short line | no |
| VN3 | Connectors and story flow | An essay connector (Tuy nhiên, Do đó, Vì vậy, Bên cạnh đó, Ngoài ra, Hơn nữa) in a script or message; a turn told as "Đó là lúc tôi nhận ra / Khoảnh khắc ấy / chợt nhận ra rằng" with no action or object at the turn; or essay logic (claim → "Đây là lý do" → Thứ nhất, Thứ hai → Tóm lại) in a story, script or message | Spoken connectors, but the story drops one link: no time or place, someone's words reported ("chia sẻ rằng") instead of quoted, the lesson preached ("Bài học là…", "Hãy luôn nhớ"), or the end is not a small step for one person | Spoken connectors of the coach's region (rồi, xong, mà, nên, thế là / vậy là, tại, chứ, có điều, hóa ra, mới); a story runs cảnh → chuyện xảy ra (words quoted verbatim) → mình nhận ra (an action or object + mới / hóa ra) → bạn thì sao; the lesson is one two-part line or in someone else's mouth. No story in the piece: connectors alone decide | yes |
| VN4 | Xưng hô | The pair differs from the Card (`audience_address`; the 1:1 pair in DMs); the self pronoun drifts (mình → tôi → chúng tôi); "bạn" to a 45+ reader or to a commenter who called the coach "c" / "a"; tao – mày; the machine uses the audience pair to the coach | One slip ("các bạn" once in an "anh chị" piece), or plural address ("các chị em") in a 1:1 message | One pair from first line to last, matching the Card; 1:1 messages singular; quoted speech keeps its speaker's own pronouns | yes |
| VN5 | Particles | A wrong-region particle the coach's own dump and posts never use (nha / nè / hông in a Bắc voice; nhé / đấy / nhỉ in a Nam voice; a young Bắc coach whose posts say "nha" keeps it); a message to an older person or a customer with neither "Dạ" nor "ạ"; or the same particle on 3 sentences in a row | Below half the coach's own end-particle rate (no posts yet: below 1/3 of sentences in captions and messages); more than one "ạ" per sentence on average; or particles on price, terms or refund lines in a public post | The coach's region and rate; particles sit where the relationship is (dặn, rủ, làm thân, gỡ căng), fact lines plain; "Dạ… ạ" once per message to an older reader or a customer | no |
| VN6 | No translationese | Any banned tell (`locales/vn/banned-tells.txt`) not on the coach's `do_say`; or ≥3 judge-level patterns from guide §2 (marked Judge); or two density flags (guide §9.3); or `**`, `#` headings or Unicode bold in a Facebook, Zalo or TikTok piece | 1–2 judge-level patterns, or one density flag | 0 banned tells, 0 judge-level patterns, no density flag; back-translation: 3 sentences of the judge's choice each stumble when put word for word into English | yes |
| VN7 | Sounds like this coach | Fails the swap test (any coach could have posted it); none of their phrases, openers or rhythm; a `never_say` hit; tone, emoji, humour or English they do not use | Their pair and region but generic: no phrase or opener of theirs where one fits naturally, or the rhythm departs from their samples (every line split for a coach who writes paragraphs, or the reverse) | Reads like their dump and posts: one of their phrases or openers / closers where it fits (never forced, not the same one two pieces running), their rhythm (written voice for posts, spoken for scripts), their humour and code-mix; someone who read the dump would believe the coach wrote it | yes |
| VN8 | CTA, the Vietnamese way | A translated or pushy ask the machine chose (Bạn đã sẵn sàng… chưa?, Đừng bỏ lỡ, Hành động ngay, Nhanh tay); a real deadline or slot count said plainly with its reason is not pushy (DECISIONS: launches); hiding a fixed price (giá ib; a bare "check ib" under a price question); pressure in DMs ("em thấy chị đã xem…", three messages in a row); an English keyword the machine chose (GUIDE, FREE) | One ask but no quiet DM route beside a comment keyword; two asks; or a vague ask ("liên hệ để biết thêm") | One small, specific action in the coach's voice; a Vietnamese keyword or a plain DM; a quiet route for people who feel "ngại"; the price where it is a sale; an exit line in a follow-up ("chưa phải lúc thì cứ để đó") | no |

**Never scored down:** a keyword, "chấm", "ib" or threshold the coach chose themselves (DECISIONS; `shared.md` "Never blocked"); a word on the coach's `do_say`; natural forms the guide lists in §2.7 ("nó" after a noun, emphatic "là", "là" meaning "that" after thấy / nói / khen ("khách khen là rất ngon"), "tóm lại là" mid-story, "nói thật", "anh ấy" in a Bắc voice, "không những… mà còn" once, a real well-wish ("Chúc anh chị thành công nha!" before an opening), literal "chìa khóa", "hành trang", "chợt nhận ra quên…", the coach's own abbreviations to people they know).

## Build pass rule

- **Shared rule:** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; no conditional pass; uncertain = 0.
- **Here:** VN3, VN4, VN6 and VN7 score 2; total ≥13/16 (the 4-out-of-5 bar). With VN8 N/A: ≥12/14. Machine prose to the coach (VN7, VN8 N/A; the story half of VN3 N/A): VN3, VN4 and VN6 at 2, ≥10/12.
- **N/A:** VN8 when the piece has no ask; VN7 only when the run holds no dump, no pasted post and no voice sample (the verdict then says "giọng chung" and the piece is capped at Draft for G3); the story half of VN3 when there is no story (connectors still scored).
- **Code side:** a banned tell is decided by the lint / I23 output, never re-argued; the judge only checks whether the hit is on the coach's `do_say` or inside quoted speech.
- **Release bar (G3):** every VN persona's pieces average ≥14/16 with no critical below 2, and each region present in the eval set has had one native-reviewer pass (below).

## How to judge (in this order)

1. **Read aloud** as the coach, to one customer. Mark every line a Vietnamese person would not say aloud.
2. **Back-translate** three sentences word for word into English (guide §9.2). Smooth English = translated Vietnamese.
3. **Check the chain** in any story: scene, what happened with a verbatim line, the turn shown by an action, a small step for one person (guide §3.1).
4. **Check the pair and particles** against the Card, the channel (public or 1:1) and who is reading.
5. **Hold it next to the dump:** does it sound like the coach's own lines, or like any coach?
6. Score; every score below 2 quotes the offending line and names the guide row (e.g. "VN6 = 1: 'Điều này khiến khách…' (C7)").

## Native reviewer pass

- **Who:** one native speaker per region present in the eval set (Bắc, Nam, and for Trung both Huế–Quảng and Nghệ Tĩnh when a Trung persona is in the run). Not the person who wrote the module.
- **What:** for each piece, mark each line ✓ natural · S stiff · D translated · R wrong region · X wrong pair, and write the line as they would say it. Then score VN1–VN5 for their region.
- **Weight:** on VN1–VN5 for their own region, the native reviewer's score replaces the judge's; disagreements of 2 points go to `qa/rubric-proposals.md` with both lines quoted. VN6 stays with the lint and the judge; VN7 with whoever has read the dump.
- **Sample:** every Day-0 piece of each VN persona plus 10 random weekly pieces per release; all Zalo and inbox replies in the run.
- **Feed back:** any line marked D or R that no banned-tells entry or guide row covers becomes a proposed guide row (and, if mechanically detectable with no hit on the persona corpus, a banned-tells entry).

## Runtime check shipped

VN edition only. Appended to every VN format's `checks_vn` in `core/format-checks.toml` (the EN edition has no counterpart). Yes means pass.

```toml
[format.vn-naturalness]
checks_vn = [
  "Đọc to lên, người Việt có nói đúng những câu này với khách không?",
  "Không còn câu nào dịch từng chữ ra tiếng Anh mà vẫn trơn (Tuy nhiên, Điều này, một cách, được… bởi, Dưới đây là)?",
  "Một cặp xưng hô từ đầu tới cuối, tiểu từ đúng giọng của coach (theo bài họ viết, chưa có thì theo vùng) và đặt ở chỗ dặn, rủ, làm thân?",
  "Chuyện có cảnh, có câu người ta nói nguyên văn, nối bằng chữ nói (rồi, xong, thế là, mà)?",
  "Lời mời là một việc nhỏ, từ khóa là chữ khách hay nói, có đường nhắn riêng, không rao, không giấu giá (hạn, suất thật thì nói thẳng)?",
]
```

## Calibration (fictional coaches)

**PASS.** Khang, 31, running coach for office workers in Sài Gòn, "mình – mấy bạn", Nam; his dump has "Nói thiệt nha" and "chậm tới mức vừa chạy vừa nói chuyện được". TikTok script, 100 tiếng:
"Bữa trước có bạn nhắn mình: 'Anh ơi em chạy được ba bữa là đau gối, chắc em hông hợp chạy bộ.' Nói thiệt nha, hồi đầu mình cũng y chang vậy. Ra công viên là chạy hết sức, chạy cho bằng người ta, xong ba bữa nằm nhà. Tới chừng chạy chậm lại, chậm tới mức vừa chạy vừa nói chuyện được, thì gối hết kêu. Mấy bạn hông phải hông hợp đâu, mấy bạn chạy nhanh quá đó. Sáng mai thử chạy chậm hai chục phút thôi, đau nhói thì nghỉ, đi khám nha. Rồi kể mình nghe."
VN1 2 · VN2 1 (the "Tới chừng…" sentence runs 18 tiếng with a clause inside; fine spoken, one breath too long for a 3-second cut) · VN3 2 (quoted line, "xong", "Tới chừng… thì…", a small step) · VN4 2 · VN5 2 (nha, đó, thôi at the dặn lines) · VN6 2 (0 lint; back-translation stumbles) · VN7 2 (his opener and his phrase) · VN8 2 ("Sáng mai thử…", "Rồi kể mình nghe") = 15/16, criticals at 2. **Result: PASS.**

**FAIL.** cô Nga, 52, home baking classes in Nam Định, "mình – các chị", Bắc. Facebook opener the machine wrote:
"Bạn có biết rằng việc định giá bánh một cách chính xác là vô cùng quan trọng? Là một người đã làm bánh hơn 20 năm, tôi hiểu rõ điều này. Tuy nhiên, nhiều chị em vẫn đang gặp khó khăn trong việc tính giá. Hãy cùng mình khám phá 3 bước đơn giản nhé! Đừng bỏ lỡ!"
VN1 0 (vô cùng, khám phá) · VN2 0 ("việc định giá…" as subject, "Là một…," clause first) · VN3 0 ("Tuy nhiên" in a post opener; claim → steps logic) · VN4 0 (bạn → tôi → mình → chị em) · VN5 1 (one "nhé" for five sentences) · VN6 0 (lint: "Bạn có biết rằng", "một cách chính xác", "là vô cùng quan trọng", "Là một người…,", "gặp khó khăn trong việc", "Hãy cùng… khám phá") · VN7 0 (swap test fails; her "các chị" pair and her kitchen are missing) · VN8 0 ("Đừng bỏ lỡ!") = 1/16. **Result: FAIL** (VN3: "Tuy nhiên, nhiều chị em…"; VN4: "Bạn có biết" then "tôi hiểu rõ"; VN6: six lint hits; VN7: generic). A passing rewrite opens with a customer's message and her kitchen: "Tuần trước có chị nhắn mình: 'Cô ơi em bán cả tháng mà vẫn còn nợ tiền bơ tiền trứng.' Mình nhìn bảng giá của chị ấy là hiểu ngay." (guide §8 A1).
