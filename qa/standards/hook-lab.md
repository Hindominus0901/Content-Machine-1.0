# Hook lab standard (`hook-lab`)

Build-only rubric (wf12-qa-spec §3.1 shape). Never shipped. It is the G3 judge rubric for every hook and headline the machine prints, and the source of `standard = "hook-lab"` eval cases.
Sources, in order: the founder's own Day 0 run (7 Oct 2026, VN edition: "đặc biệt phần headline và hook là chưa ổn"; defects: flat claims, on-screen text = spoken line, no open loop, no buyer words, nothing concrete, English sentences in VN pieces, a guessed client line in a public piece) · founder decisions 7 Oct (VN pieces always Vietnamese; Soo Wei Goh and Matt Gray are the two strategy references, Matt Gray's framework names never in coach text) · docs/research/founder-sources.md (Goh: three hooks per short, a hook wide for the sharer and specific for the buyer, loops beyond the topic; Matt Gray: title shapes, thumbnail words that add, packaging before production) · docs/research/wf8-mattgray-playbook.md §0-§4 · docs/research/vn-language-guide.md §3.5 (VN openers by platform, openers to avoid) · modules/{en,vn}/packaging.md §CM-HOOKS, §CM-PACKAGING · kit §CM-FORMATS 1 and the Ship Check hook line.

## Purpose

Every hook and headline is the winner of a silent lab: ≥12 drafts in ≥6 shapes, picked by six checks, never a flat claim. The reviewer sees only the winner, so this rubric scores the winner and the reply around it, not the drafts.

What good means: a stranger stops because they see something (a scene, an object, the coach's number), hears their own words, and wants the answer the last line gives; the buyer knows it is about them; nothing is invented, inflated or bait.

## Scope

- **Artifacts:** a short's three hooks (on-screen text, first frame, first spoken line); the first line of a text post or long Facebook post; carousel slide 1; email subject and Zalo first line; long-video title and thumbnail words; FILM TODAY on Day 0.
- **Scored on top of** `shared.md` (truth, claims, polarity, hook length, hedges) and the piece's format standard (`native-short`, `text-post`, `carousel`, `email-zalo`, `longform-packaging`, `micro`). This file adds what those don't check: the six lab checks, the flat-claim fail and the reply discipline.
- **Not here:** the Map's line 1 and keyword (`message-map`, `signature-keyword`); the body of the piece.

## The six checks (yes/no; 2 = yes, 0 = no; all critical)

Uncertain = 0. Each line quotes the hook. Examples come from one topic pair (fictional coach: a consultant who teaches coaches to research buyers and to earn trust before selling; built from the founder's test, person removed).

| ID | Check | PASS (2) | FAIL (0) |
|---|---|---|---|
| HL1 | Concrete: a scene, an object or the coach's own number | EN "An AI chat open, 'keywords for coaches' typed in." · VN "Khung chat AI gõ dở 'từ khoá cho coach'." · a number only from the coach's facts ("I've read {N} intake forms…") | EN "Research is the most important part of marketing." · VN "Nghiên cứu là phần quan trọng nhất của marketing." (nothing seen or counted; adjectives like "real", "huge" don't count) |
| HL2 | The buyer's words, not the coach's terms | EN "nobody messages me" (a buyer line from the dump or research, source kept) · VN "đăng hoài chẳng ai nhắn" | EN "low conversion", "persuasion comes from consumption", "ICP" · VN "tỉ lệ chuyển đổi thấp", "chân dung khách hàng", "thuyết phục đến từ tiêu thụ" |
| HL3 | Opens a loop past the topic that the last line pays off | EN first line "A few posts read, one AI prompt, and you call that knowing your buyer?" → last line "Research starts when a buyer says a sentence you'd never have guessed." · VN "Đọc vài bài, hỏi AI một câu, rồi gọi đó là hiểu khách?" → "Hiểu khách là nghe họ kể, tới lúc họ nói ra câu bạn không đoán được." | EN "3 research tips for coaches." (no question) · a loop the piece never answers (bait) · VN "Chia sẻ 3 mẹo nghiên cứu khách." |
| HL4 | A belief shifts (A before, doubt after) | EN "Nobody buys from your sales post. They buy from the posts they read before it." · VN "Không ai mua vì bài chốt đơn. Người ta mua vì những bài đã đọc trước đó." | EN "Trust matters in business." · VN "Niềm tin rất quan trọng." (everyone already agrees; nothing moves) |
| HL5 | Wide enough for a friend to share, specific enough that the buyer knows it's them | EN "Posting every day and nobody messages?" (any small-business owner gets it; a coach feels named) · VN "Đăng bán mà không ai hỏi?" | Too wide: EN "Want more success?" · VN "Muốn thành công hơn?" Too narrow: EN "If your intake funnel lacks a VoC layer…" · VN "Nếu phễu của bạn thiếu lớp insight…" (only insiders get it; nobody shares) |
| HL6 | Clean: no hype, hedge or bait; the piece keeps the promise | EN "Who picked your keywords?" (the piece answers it) · VN "AI đâu có gặp khách bạn" | EN "You won't believe what AI does to your research" · "Research is dead" · "Maybe you're researching wrong" (hedge) · a freebie or money flex as the whole hook · VN "Bạn sẽ không tin đâu…", "Nghiên cứu chết rồi", "Có lẽ bạn đang làm sai" |

## Format and gate items

| ID | Item | PASS | FAIL | Critical |
|---|---|---|---|---|
| HL7 | Not a flat claim: a bare "X is Y" that states the ending fails even when true; rewritten as a scene, a flip or the buyer's words | the PASS lines above | EN "That's not research." · "Clients must trust you." · VN "Đó không phải research." · "Khách phải tin bạn." (these were the founder test's on-screen texts) | yes |
| HL8 | A short's 3 hooks add up (N/A when not a short): on-screen ≠ first spoken line ≠ first frame; one idea | EN on-screen "Who picked your keywords?" · frame: an AI chat, "keywords for coaches" typed · line: "A few posts read, one AI prompt…" · VN chữ "AI đâu có gặp khách bạn" · khung đầu: khung chat AI gõ dở · câu đầu "Đọc vài bài, hỏi AI một câu…" | EN on-screen "That's not research." and the first line ends "That's not research." · VN chữ "Khách phải tin bạn." + câu đầu "Muốn người ta thành khách, họ cần tin bạn." (same claim twice, no frame) | yes |
| HL9 | Headline packaging (titles, subjects, slide 1): a title shape in plain words, the viewer's result, ≤60 characters EN / ≤70 VN; thumbnail words add, never repeat | EN "you don't need more leads (you need people who trust you)" + thumbnail "the posts before the pitch" · VN "Không thiếu khách, chỉ thiếu người tin bạn (cách sửa đây)" + "bán từ bài trước" | EN "The importance of customer research" (topic label, no result) · VN "Tầm quan trọng của việc nghiên cứu khách hàng" · thumbnail repeating a title word | yes (N/A: no title) |

**Gates (pass/fail, scored here, on top of `shared.md`):**
- **HG1 Truth.** A client's words open a piece only if the coach reported them. A research line is the viewer's own thought or "a line I keep seeing", never a client quote. Numbers, years and results are the coach's; results OK'd. FAIL: the founder test's "Coach nào cũng hay than: 'Em đăng bài đều mà không có khách.'" (guessed, quoted as clients). PASS: research found the line (source logged) and the hook asks it: "Đăng đều mỗi ngày mà inbox vẫn im?"; or, with no line yet, "Cần bạn · Khách hay hỏi bạn câu gì, đúng chữ họ?"
- **HG2 VN language.** A VN piece has no English sentence; brand and platform names only. English dictation becomes a natural Vietnamese idea, the early win too. FAIL: "Bạn đọc vài bài post, nhờ AI tìm keyword. That is not research." · early win "Client acquisition come from persuasion…". PASS: "Muốn người ta mua, phải để người ta xem bạn đủ lâu trước đã."
- **HG3 Reply discipline.** Only the winner prints (no "Option 1/2/3" unless asked); "another hook" / "hook khác" gives exactly 2, each a new shape; no shape or check is named to the coach; one question at most in the reply.
  - **Exempt, by the kit's own design:** an email prints 3 subject lines (EN §CM-MESSAGES, Email: "3 subject lines"; VN §CM-MESSAGES: "3 tiêu đề"), and a long video prints 3 title options with thumbnail words that the coach picks from (§CM-PACKAGING). Three subjects or three titles is never an HG3 fail (the 7 Oct review scored it as a kit/rubric clash, not a defect). Score the first subject (or the title the reply recommends) on HL9, and the other two as drafts of it: each still free of hype, hedge and bait (HL6). Everything else in HG3 still holds: no "Option 1/2/3" label, no shape or check named, one question at most.
  - **Not exempt:** a short's on-screen text, first line or first frame, a text post's line 1, slide 1 and a Zalo first line: one winner each, never a list of alternatives.

## Build pass rule

- **Shared rule:** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; hard gates clear; no conditional pass; uncertain = 0.
- **Here:** `shared.md` and the format standard pass first; HL1-HL9 all 2 (N/A where marked); HG1-HG3 clear. The lab is all-or-nothing on purpose: one failed check means the winner was the wrong draft.

## Runtime check shipped

Not a format-checks footer: the lab ships in the kit. EN §CM-FORMATS 1 carries the drafts, shapes, the six checks, the flat-claim fail, "another hook" → 2 more; the Ship Check carries "Hook: no hedge or flat claim". VN: §CM-FORMATS 1 ("nháp thầm ≥12 câu, ≥6 dáng … Câu phán suông ("Khách phải tin bạn.") trượt") and "Câu mở không rào đón, không phán suông". Depth: STRATEGY level-up §CM-HOOKS, §CM-PACKAGING. Exact lines: the hook-lab kit-lines file of 7 Oct (applied by the kit editor).

Proposed yes/no lines if a footer is wanted (≤5):
- EN: "Is the hook concrete (a scene, an object or their number) and in the buyer's words?" · "Does it open a loop the last line pays off?" · "Is it free of a flat claim, a hedge and bait?" · "On a short, do on-screen text, first frame and first line each add something?"
- VN: "Hook có cụ thể (cảnh, đồ vật, số của coach) và đúng chữ khách không?" · "Hook hé một điều mà câu cuối trả lời không?" · "Không phán suông, không rào đón, không câu mồi?" · "Video ngắn: chữ trên màn hình, khung đầu, câu đầu, mỗi cái nói thêm một điều?"

## VN note

- VN openers that pass are spoken, not read (vn-language-guide §3.5): a scene with a time and an object ("Tối qua gần mười một giờ…"), a call-out of the buyer's situation ("Anh chị nào đang… thì nghe cái này đã"), a buyer line word for word when the coach reported it.
- Always FAIL in VN (translated hooks): "Bạn đã bao giờ…", "Hãy tưởng tượng…", "Bạn có biết rằng…", "Trong thời đại…", "Xin chào các bạn, hôm nay mình…" on TikTok or Reels.
- On-screen text ≤6 tiếng, first line ≤18 tiếng (SG4). Title ≤70 characters. "Phán suông" is the VN name of the flat claim in the kit; keep the term the same in kit and level-up.

## Calibration (fictional coaches)

**PASS.** EN, the research coach, a short. On-screen "Who picked your keywords?" · frame: an AI chat, "keywords for coaches" typed · first line "A few posts read, one AI prompt, and you call that knowing your buyer?" · last line "Research starts when a buyer says a sentence you'd never have guessed." HL1 2 (the chat on screen) · HL2 2 ("knowing your buyer", no jargon) · HL3 2 (paid off by the last line) · HL4 2 (posts + AI = research → doubt) · HL5 2 · HL6 2 · HL7 2 · HL8 2 (three different jobs) · HL9 N/A. Gates clear. **PASS.**

**FAIL.** VN, the same coach, the founder test's VIDEO 3. Chữ trên màn hình "Khách phải tin bạn." · câu đầu "Muốn người ta thành khách, họ cần tin bạn." · câu cuối "It's all about human relationship." HL7 0 (flat claim) · HL8 0 (on-screen = first line, no frame) · HL3 0 (no loop) · HL4 0 (no one disagrees) · HG2 fail (English last line). **Result: FAIL** (HL7: "Khách phải tin bạn."). The rewrite that passes: chữ "Đăng bán mà không ai hỏi?" · khung đầu: lướt ngược trang cá nhân, dừng ở một bài cũ · câu đầu "Không ai mua vì bài chốt đơn. Người ta mua vì những bài đã đọc trước đó." · câu cuối "Bài bán chỉ là lời mời. Người ta quyết từ mấy bài trước."
