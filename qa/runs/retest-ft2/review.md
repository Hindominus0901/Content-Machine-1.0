Result: FAIL

# Retest FT2 (founder-test fixes, round 2, Day 0, web lane): VN copywriter-thin, VN Hạnh, EN consultant: independent review

Reviewer: independent, bilingual (EN, plus native Vietnamese for the VN runs). I wrote neither the kit nor the runs.
Trigger: the founder's own Day 0 (7 Oct, "tạm", "đặc biệt phần headline và hook là chưa ổn"), the last DECISIONS
entries (7 Oct night: §CM-DIG, background research, the hook lab, VN always Vietnamese; the strategy document with
"content pillars" once) and `qa/runs/retest-ft1/review.md`. Rubrics: `qa/standards/hook-lab.md`, `research-brief.md`
(LN1–LN7), `strategy-doc.md` (SD1–SD10), `vn-naturalness.md`. This file replaces the placeholder written before the
runs were played.

How this review was done:
- All 3 transcripts, notes.md, grades.json and the 3 strategy files read in full, as the coach reads them.
- The packet `kit/` files are byte-identical to `dist/{en,vn}/`. `transcript.jsonl` = `transcript.raw.jsonl` in 3/3.
- The graders' own functions re-run on each run: I23 pieces, `hook_shorts`, `onscreen_repeat`, `flat_claims`.
- Research re-checked at source:
  - Copywriter: 7 Voz/Webtretho pages re-fetched; 12 of the 21 kept lines checked, all 12 found.
  - EN: 21 Hats page re-fetched (4/4 lines found, 2 trimmed without "…"). Capterra and Trustpilot block curl, so 5 lines
    were checked through WebFetch.
- Scored every hook and headline on HL1–HL9 + HG1–HG3, and every strategy file on SD1–SD10. Uncertain = 0.

## Scorecard vs retest-ft1

| Area | retest-ft1 | retest-ft2 | Change |
|---|---|---|---|
| Runs valid / edited | 2 of 3 (copywriter `pace`) / 0 | **3 of 3** / 0 | better |
| Grade pass | 0 of 3 | 1 of 3 (EN) | better |
| (1) Extraction: dig fires thin, stays out rich | PASS (4 asks thin; 0 and 1 rich) | **PASS** (3 asks thin; 1 and 1 rich) | same, one ask fewer |
| (2) Research LN1–LN7 | FAIL: 10 · 12 · 12 /14 | **FAIL**: 11 (LN1 1, LN3 1) · 12 PASS · 10 (LN3 0, LN4 1, LN6 1) | Hạnh now passes; EN fails on its first KEEP |
| (2) Pages opened · lines kept · KEEP | 8/10 · 9, 5, 5 · 0 KEEP | 10 · 8 · 17 pages; 21 · 0 · 13 lines; 2 KEEP, both stretched | deeper, not truer |
| (2) Research changed the Map | 0 of 3 | 1 of 3 nominal (EN topic 1), **not creditable** (§2) | — |
| (3) Hooks passing, FILM TODAY + Week 1 | 7 of 16 | **8 of 15** | slightly better |
| (3) FILM TODAY alone | 3 of 3 | 2 of 3 (Nhi: on-screen re-says line 1 in other words) | worse |
| (3) On-screen = first line, VN Week-1 shorts | 4 of 6 | 1 of 6 (Nhi N2) | much better |
| (3) Strategy-file hooks (new ones) | — | 3 of 10 pass; 4 flat claims on screen | new gap |
| (3) Founder's "Đó không phải research." / "Khách phải tin bạn." | first survived on screen; second in the early win | both gone as hooks; a flat label ("Nghiên cứu có hai lớp") and flat "phải tin" lines remain | partly fixed |
| Strategy document SD1–SD10 | not produced | **1 of 3 pass**: Nhi 16 FAIL (SD3) · Hạnh 17 PASS · EN 16 FAIL (SD3) | new, mostly sound |
| VN pieces 100% Vietnamese | PASS | PASS | same |
| VN particles (`vn_natural`) | FAIL both (7% vs 20%; 16% vs 54%) | Nhi pass; Hạnh FAIL (24% vs 54%) | better |
| VN her phrases (I23) | Nhi FAIL 22% | FAIL both (22%, 22%) | worse for Hạnh |
| ≤1 question per reply | PASS | PASS | same |
| Keyword specific, buyer words, tagged right | PASS | PASS | same |
| Week 1 only after OK | PASS | PASS | same |
| Quiet option beside the keyword ask | (FP in FT1) | Nhi missing, Hạnh and EN present | 1 real miss |
| Grader fails: real / FP | 6 real + 1 simulator · 4 FP classes | **5 real · 0 FP** · 7 misses (§7) | better precision, weak recall |

**Why FAIL, in one line each:**
- **Research:** 2 of 3 runs fail LN1–LN7. Both KEEP patterns count to 2 places only by stretching what the lines say.
  The one Map change (EN topic 1) rests on that stretch, and it echoes a line from the persona's undictated answer bank.
- **Hooks:** 8 of 15 pass. The copywriter run passes only 1 of 5. Flat claims moved from the pieces into the strategy
  files' hooks ("The bank app isn't a forecast.", "Không cần chiến dịch lớn").
- **Strategy document:** 2 of 3 fail SD3. Nhi's file invents a client fact in a hook. EN's prints a "held" pattern
  that only one review page backs.
- **VN voice:** I23 fails in both VN runs: only 2 of 9 pieces carry one of the coach's phrases. Hạnh's particle rate
  is under half of hers.

**What clearly improved:**
- All 3 runs are valid, and EN passes the grade.
- On-screen text no longer copies the spoken line: 1 of 6 VN Week-1 shorts, down from 4 of 6.
- The founder's "Đó không phải research." is gone. Its topic now opens on a scene ("Nhiều người bảo đã nghiên cứu khách:
  đọc vài bài, hỏi AI ít từ khoá.").
- Hạnh's and EN's FILM TODAY and long posts are strong.
- Research is deeper (21 verified lines for the copywriter, 13 lines in 3 places for EN), and Hạnh's run is honest
  about finding 0 lines.
- All 3 strategy files exist, with the 7 parts in order and the 3 Map topics as the big ideas. The gaps are marked.
- No grader false positive this round.

## 1. Extraction (§CM-DIG): PASS

| Slot | Nhi (thin, English dump) | Hạnh (rich) | EN Erin (rich) |
|---|---|---|---|
| Buyer | from the story answer: a coach, personal finance for office workers | spa owners, 1 shop, 2–5 KTV, 28–40 | agencies $1–5M, 8–35 people |
| Client's exact words | dig → "Bài nào em đăng cũng có người thả tim, mà không ai nhắn hỏi giá hết." + "Em bán được cho người quen thôi, người lạ coi xong là lướt." | Thảo: "Chị ơi em ngại chào lắm, cứ mở miệng chào thẻ là em thấy mình như đi lừa người ta" | Marcus: "Record year. Empty account. Make it make sense." · Dee |
| Story | dig (same answer) | 2018 scare script, Thảo | stairwell 2019, Marcus |
| Offer + price | dig → 3 tuần, 9.500.000đ, 2 đợt | soft-cut question → 6 tuần, 6.500.000đ | soft-cut question → Margin Sprint, $7,500 |
| Proof + OK | dig → 180 / 7 / 2 / 1, "no name" | Thảo 2→5 of 10, name OK, no spa name, no ads | Marcus all; Dee no amounts |
| Stance | dump: why before how; "That is not research" | dọa da scripts, 99k ads | top line theater |

- **Thin dump: the dig fired as designed.** Three questions, one per reply, after "Done.":
  - "Bạn nghĩ tới người khách bạn giúp được nhiều nhất nhé. Tuần đầu tìm tới bạn, họ đang kẹt chuyện gì?"
  - "Làm với bạn xong, chị ấy khác đi thế nào?"
  - "Khách gật đầu làm với bạn thì họ nhận được gì, trả bao nhiêu?"
  The 6 slots were full at 12.4 minutes. The `dig.proof` fix landed: the question asks for the result only, and the
  client's OK came unasked.
- **Rich dumps: it stayed out of the way.**
  - Hạnh got slot-aimed nudges with no question mark ("Chuyện kế, chị kể một em chủ spa chị từng kèm: lúc mới tìm đến
    chị, em ấy nói gì…"), then one question on the cut, then the §CM-SETUP 6 income guess ("Đúng không chị?").
  - EN got "Next, if it helps: …" nudges, then one question riding the soft cut.
  - In both runs the nudges cost no turn.

## 2. Research (Day-0 listening pass): FAIL

| | Nhi (copywriter) | Hạnh | EN |
|---|---|---|---|
| Queries | 20, Vietnamese | 17, Vietnamese | 24 web + 5 HN API |
| Aimed at the buyer? | 4 of 20 name coaches. 12 aim at neighbours (freelancer, gia sư, PT gym, mở lớp, bán khoá học), which the kit forbids: "cụm nào cũng có vai của khách … để không trôi sang nhóm bên cạnh" | yes: "ngại chào", "để về suy nghĩ rồi mất hút", "sợ khách nghĩ chặt chém", "không đủ trả lương thợ" | mostly. One uses the coach's category ("fractional CFO"); q6 is an admitted slip from undictated chunk 3 |
| Pages opened · places | 10 · Voz (8), Webtretho, Substack | 8 · Voz, Webtretho, Foody, 4 seller blogs | 17 · Capterra, Trustpilot, 21 Hats, HN, others |
| Lines kept | 21, all buyer-adjacent, none from a coach | 0, honest | 13 from 9 people |
| KEEP | "khách chủ yếu qua người quen, người lạ chưa tin" (3 people · 2 places) | none | "owners want to see which clients make money" (6 · 2) |
| Map line 1 + keyword | client's words, KHÔNG AI NHẮN "(mình đoán)" | Thảo + "bao nhiêu em nói y hệt", NGẠI CHÀO | Marcus + "all of them say", RECORD YEAR |
| LN1·LN2·LN3·LN4·LN5·LN6·LN7 | 1·2·1·2·2·1·2 = **11** | 2·1·2·2·2·1·2 = **12** | 2·2·0·1·2·1·2 = **10** |
| Verdict | FAIL (LN1, LN3) | **PASS** | FAIL (LN3, LN4) |

**Re-checked at source:**

- **Nhi's KEEP is stretched (LN3 1).**
  - K1 "nhưng đa số quen biết giới thiệu" and K4 "Khoảng đầu thật sự là không ai học vì học viên không tin tưởng" are
    in the same Voz thread, so they count as one place.
  - The second place is K8, "Để làm freelance a cần 1 lượng khách quen". "Khách quen" means regular clients; it does
    not say clients come through acquaintances.
  - The "người lạ chưa tin" half has one person.
  - The pattern changed nothing on the Map, but CHIEN-LUOC-NOI-DUNG.md prints it as GIỮ ("3 người · 2 nơi").
- **EN's KEEP is stretched (LN3 0), and it is the run's one Map change.**
  - Only lines 1–3 say "which clients", and all three come from one Capterra page (Productive, page 3). Reviews under
    one product page are one place.
  - The Trustpilot backers say something else:
    - line 9: "real visibility on performance and profitability", general, not per client;
    - line 8 on the page reads "…allowing us to make informed financial decsions": no clients and no profit.
  - Line 8 was also silently corrected to "decisions". Lines 12–13 ("Our revenue grew year over year.", "The bottom line
    never quite scaled the same way.") drop "And yes," and "But" with no "…". That is LN4 1. The meaning holds, but the
    strategy file prints two of these as held buyer lines.
- **EN's research change cannot be credited.**
  - Topic 1 became "Which clients lose you money".
  - The words that found its backers were "which clients" in queries 6, 10 and 11.
  - Query 6 is the admitted slip from undictated chunk 3. "Which clients actually make us money?" is in the persona's
    undictated answer bank (`evals/personas/en/consultant/answers.md` lines 88, 112) and in expected.toml's big idea 1.
  - The leak check uses a 5-word window, so it cannot see a 2-word echo in a query.
- **EN "Line 1 from: your client + 1 agency owner like it"**: no line in the notes backs the "+ 1 agency owner" (LN6 1).
- **Research timing is modelled, not real.**
  - Nhi's "phase 1 (dump only)" queries use "thả tim", "hỏi giá" and "người quen / người lạ", which she first said at
    turn 8.
  - Hạnh's T3 queries use "ngại chào" and "để về suy nghĩ", first said at turns 5–6.
  - All of these came before the Map, so no fact leaked into a machine turn. But the log's "ran after turn N" cannot be
    trusted (§8 item 4).
- **Hạnh passes on honesty.** 0 lines, no invented pattern, line 1's source named by role, exact paste steps.
  - Two flaws in the block: its "tháng 10/2026" is the date of reading, not of any line, and it lists "blog người bán"
    as a place where it "listened to clients".
  - The founder would still say the research found nothing.
- **LN2 / LN6 counting (Nhi).** "21 câu, 7 nơi" counts 6 Voz threads as 6 places. The block shows "Voz (20, ở 6 chủ
  đề)", so the reader can see it. In practice this is 2 sites, and 20 of 21 lines come from one of them. Line 1's
  source is not named in the block (LN6 1).

## 3. Hooks and headlines (hook-lab)

| Run · piece | Hook (on-screen / frame / first line → last line) | Fails | Verdict |
|---|---|---|---|
| Nhi · QUAY HÔM NAY | "Tim nhiều, hộp tin nhắn trống" / a post full of hearts, then the empty inbox / "Bài nào em đăng cũng có người thả tim, mà không ai nhắn hỏi giá hết." → "Người lạ chỉ nhắn khi đọc thấy đúng câu của chính họ." | HL8: on-screen, frame and line say one fact three times (grader: 33% word overlap, passes) | FAIL (close) |
| Nhi · N1 | "Đăng đều mà không ai nhắn" / full posting calendar / "Ai cũng hỏi mình viết bài sao. Mình chỉ hỏi lại: tại sao người ta phải đọc." → "Trả lời được câu tại sao rồi, viết sao mới có nghĩa." · caption 1 "Viết sao thì để sau, tại sao phải có trước." | HL3 (the last line restates), HL4 ("start with why": nobody disagrees), HL7 (caption line 1 is a maxim) | FAIL |
| Nhi · N2 | "Người quen mua, người lạ lướt" / a finger scrolling past / "Em bán được cho người quen thôi, người lạ coi xong là lướt." → "Người ta coi xong mà không biết gì về bạn, thì không ai nhắn đâu." · caption 1 "Người quen mua vì đã biết bạn. Người lạ thì chưa." | HL8 (80% same words), HL7 (caption) | FAIL |
| Nhi · N3 | "Nghiên cứu có hai lớp" / handwritten notebook beside the phone / "Nhiều người bảo đã nghiên cứu khách: đọc vài bài, hỏi AI ít từ khoá." → "Hiểu tới mức thấy được cái họ thấy, lúc vừa thức dậy đã gặp chuyện đó." | HL2/HL7 (a label in the coach's own frame on screen), HL3 (vague, translated close) | FAIL |
| Nhi · bài dài | "Đăng đều, tim nhiều, mà không ai nhắn." → "Hoá ra người lạ chỉ cần đọc thấy đúng câu của chính họ." | none. But HG1: "Chị tưởng phải đăng nhiều hơn." gives the client a thought nobody reported | PASS (flag) |
| Hạnh · QUAY HÔM NAY | "27 trên 41 thẻ bỏ dở" / chị lật sổ ở quầy / "Năm 2018 spa chị cũng dọa khách đấy, 3 tháng bán được 41 cái thẻ." → "Giờ chị không bán thẻ, chị bán buổi hẹn sau." | none | PASS (best of the round) |
| Hạnh · bài dài | "Năm 2024 có một em hỏi trong nhóm chủ spa: sao em chào thẻ khách toàn từ chối?" → "Ngại thì không sai đâu các em ạ. Sai là tưởng chào thì phải dọa." | none ("câu nào cũng dọa da" stretches her one scare line) | PASS |
| Hạnh · N1 | "Giường trống lúc 3 giờ chiều" / an empty bed / "Thảo bảo chị: khách khen tay em nhẹ mà cứ "để chị về suy nghĩ" rồi mất hút." → "Chị dạy Thảo chào buổi hẹn sau, chứ không chào thẻ 30 buổi." | none (the on-screen text partly captions the frame) | PASS |
| Hạnh · N2 | "Chào liệu trình bằng cái gương" / chị đưa gương về phía máy / "Chào liệu trình mà không dọa da câu nào thì chào thế nào?" → "Chị gọi là cầm gương nói thật, đơn giản lắm." | HL3 (the last line names the method instead of landing it; the screen gives the answer first) | FAIL (close) |
| Hạnh · N3 | "Ngại chào vì sợ chặt chém?" / bảng giá / "Em sợ khách nghĩ mình chặt chém." Các em nói câu này nhiều lắm. → "Chị thì để giá trên bảng, không giảm sốc gì hết." | HL3, HL4 (the fear is never answered; her own flip line is missing) | FAIL |
| EN · FILM TODAY | "22 million. Out of cash." / desk, legal pad / "Our best year ever, and I'm asking the bank for payroll." → "Your biggest client is not your best client until you've done the math." | none; FT1's text-version miss is fixed (caption line 1 "Record year, empty account…") | PASS |
| EN · email | subject 1 "How are you out of cash in your best year?" (+2, exempt) | none | PASS (FT1 "The Monday Number: minus 6" fixed) |
| EN · Wed post | "6 in the morning, from a hockey rink parking lot." → "Your biggest client is not your best client until you've done the math." | none | PASS |
| EN · PDF slide 1 | "Your biggest client might be underwater. Here's how to check." | HL9 (61 characters, cap 60), HL6 ("might" hedges), HL2 ("underwater" is her word) | FAIL |
| EN · Fri post | "New logos, an award, the "we doubled revenue" post." → "Margin before more. Before more clients, before more people, before more anything." | none; FT1's "If your margin's broken…" moved into the body | PASS |

**Totals:** Nhi 1 of 5, Hạnh 3 of 5, EN 4 of 5: **8 of 15** (FT1 7 of 16). DMs, Zalo asks and inbox replies open in the
coach's own words ("Chị ơi, em là Nhi nè.", "Em ơi, chị Hạnh đây.", "Quick favor: …") and are not counted.

**Strategy-file hooks** (the 10 not reused from the pieces): **3 pass.**
- Pass:
  - EN: "Minus 6 percent." / "6 in the morning…"
  - EN: "He repriced his biggest client." / "They said yes to a new scope after a long weekend."
  - Hạnh: "Bước các em hay bỏ nhất" / "Sau 3 ngày chị nhắn thoại cho khách…"
- Fail, flat claims or labels on screen (the founder-test shape):
  - EN: "The bank app isn't a forecast." (the grader's own flat-claim example), "That's a rearview mirror.", "Fix it or fire
    it."
  - Nhi: "Câu đúng nằm ở khách cũ", "Không cần chiến dịch lớn"
- Fail, invented fact: Nhi's "1 email, 180 người" / "Chị ấy không đăng thêm bài nào, chỉ gửi đúng một email.". The
  coach never said the client stopped posting.
- Fail, on-screen label repeats the line and gives the result at once: Hạnh's "Sổ hẹn của Thảo tháng 7" / "Thảo đếm lại
  sổ hẹn, 10 khách mới thì khoảng 5 khách hẹn buổi sau."
- The PLAYBOOK says these hooks follow §CM-HOOKS, but its SOÁT THẦM / silent check never tests them.

**Founder test → FT1 → FT2**

| Founder test (7 Oct) | FT1 | FT2 | Status |
|---|---|---|---|
| On-screen "Đó không phải research." | "Vậy chưa phải nghiên cứu" | Gone. The topic opens on a scene. On screen is now the label "Nghiên cứu có hai lớp", and the file's hook is "Câu đúng nằm ở khách cũ" | the claim is fixed; a flat label took its place |
| On-screen "Khách phải tin bạn." + "Muốn người ta thành khách, họ cần tin bạn." | not a hook; the early win kept "…phải tin bạn" | Not a hook. The early win still lists "Người ta mua khi đã tin bạn. Mà tin là vì đã coi bạn đủ nhiều." and "Muốn ai đó thành khách, họ phải biết bạn có ở đó…". Captions N1/N2 end on maxims | fixed in hooks; the flat claims live on in the early win and captions |
| On-screen = spoken line | 4 of 6 VN shorts | 1 of 6 (Nhi N2), plus 1 paraphrase (Nhi FILM TODAY) | mostly fixed |
| English in a VN piece | none | none | fixed |
| Guessed client line in a public piece | 1 translated "quote" | none quoted; 2 small invented client facts ("Chị tưởng phải đăng nhiều hơn.", "câu nào cũng dọa da") | mostly fixed |

**The 3 weakest, with stronger rewrites (facts only from the transcripts):**

1. **Nhi N3**, the descendant of "Đó không phải research.": a label on screen, the coach's "two layers" frame, a
   translated close.
   - Chữ trên màn hình: "AI đâu có gọi khách cũ" (6 tiếng: it adds the contrast the first line holds back)
   - Khung hình đầu: cuốn sổ ghi tay đúng câu khách nói, cạnh điện thoại đang mở khung chat AI
   - Câu đầu (giữ): "Nhiều người bảo đã nghiên cứu khách: đọc vài bài, hỏi AI ít từ khoá."
   - Ý: Trước khi viết cho chị coach tài chính, mình gọi 3 khách cũ của chị, mỗi người 30 phút · Hỏi xong thì im, để
     họ kể bằng chữ của họ · Ghi đúng chữ họ nói, không sửa.
   - Câu cuối: "Câu làm người lạ nhắn tin là câu khách cũ nói ra, AI đoán không ra đâu." (16 tiếng, her Southern "đâu")
2. **Nhi N1**, a "start with why" maxim at both ends.
   - Chữ: "Đăng kín lịch, không ai nhắn" (6: the frame shows the full calendar, the text adds the silence)
   - Câu đầu: "Hỏi mình viết bài sao, mình hỏi lại đúng một chữ: tại sao?" (her early-win line)
   - Ý: Tại sao người lạ phải dừng lại, tại sao mua của bạn mà không mua người khác · Câu trả lời nằm trong lời người đã
     trả tiền cho bạn · Hỏi 3 khách cũ: sao bạn nhắn mình mà không nhắn người khác?
   - Câu cuối: "Câu họ trả lời, bạn đưa lên làm câu đầu bài kế tiếp nha." (a concrete step, which pays off "tại sao")
   - Caption dòng 1: "Khách hay hỏi mình: viết bài sao, làm sao có thêm người theo dõi." (her clients' question, not a
     maxim)
3. **Hạnh N3**, a loop the last line never closes.
   - Keep the on-screen text, the frame (bảng giá) and the first line.
   - Ý: Các em thương khách, thợ lên làm chủ, không có máu buôn · Năm 2018 spa chị ký thẻ trong ngày thì giảm sốc, 41
     thẻ mà 27 thẻ khách bỏ dở · Giờ giá chị để trên bảng, không giảm sốc, chỉ hẹn buổi sau.
   - Câu cuối: "Các em ạ, khách không sợ giá đâu, khách sợ bị dọa." It is her phrase and her opener, it answers the fear,
     and it ends on her particle. It would also lift I23 and `vn_natural`.

Quick fixes for the rest:
- Nhi FILM TODAY on-screen → "Người quen mua, người lạ lướt" (her client's second line, a new contrast). N2's
  on-screen then becomes "Một bài thì chưa ai tin" (her phrase).
- Hạnh N2 last line → "Khách tự nhìn thấy rồi, mình đâu cần dọa câu nào nữa."
- EN slide 1 → "Which client is losing you money? A 6-step check" (48 characters; "losing money" is from her dump).
- EN file hook "The bank app isn't a forecast." → on-screen "Bank app beat Instagram" (Dee's screen time, as dictated).

## 4. The content strategy document (SD1–SD10)

| ID | Nhi CHIEN-LUOC-NOI-DUNG.md | Hạnh CHIEN-LUOC-NOI-DUNG.md | EN CONTENT-STRATEGY.md |
|---|---|---|---|
| SD1 complete, in order | 2 (7 parts, rubric headings, gaps marked) | 2 (headings in the "Chị" pair, as DECISIONS says: "the VN 'bạn' follows the coach's pair") | 2 |
| SD2 their words | 2 | 2 | 2 |
| SD3 nothing invented | **1**: hook "Chị ấy không đăng thêm bài nào, chỉ gửi đúng một email." | 2 | **0**: "Their words that held (2+ people, 2+ places): agency owners want to see which clients make money" (1 page backs it; "make informed financial decisions" doesn't say it) |
| SD4 big ideas distinct, on the Map | 2 (all 3 "new ways" end in "đúng câu khách"; the beliefs differ) | 2 (Ý1 and Ý3 adjacent) | 2 |
| SD5 things to post + hooks | 1 (hooks fail: §3) | 1 (N2, N3, "Sổ hẹn…") | 1 (3 flat on-screen hooks) |
| SD6 stages | 1 (stage 5 has no line; stage 3 holds a problem line) | 1 (stage 1's "Các em hay nói: "để chị về suy nghĩ" là khách bảo vậy thôi." is no reported line; held lines are coach-reported, no place or month) | 2 |
| SD7 system | 2 (Lean ≤60, board and nudges "chưa") | 2 (Facebook, TikTok reposts, group) | 2 |
| SD8 asks + mix | 1 (no "≥3 gives per ask") | 1 (same) | 1 (same) |
| SD9 first 30 days | 2 | 2 (week 4 [CẦN CHỊ: ngày khai giảng]) | 2 |
| SD10 plain, natural | 2 | 2 | 2 |
| Total | 16, **FAIL** (SD3) | **17, PASS** | 16, **FAIL** (SD3) |

- **All 7 parts:** yes, in all 3 files, in order. "(content pillars)" appears once, in part 3's heading, as DECISIONS
  allows. The FT2 placeholder found that `strategy-doc.md` still fails that heading (line 45 and the runtime check);
  that is still open.
- **Pillars grounded:** the big ideas are the Map's 3 topics, each with old → new, a belief, 6–8 things to post and an
  ask. NOT NOW comes with reasons and a return rule.
  - Hạnh's 7 / 8 / 6 things to post are all from her dump.
  - EN's 8 / 8 / 7 likewise. Only EN's topic-1 name rests on the stretched research.
- **Polished wording:** the VN files read as spoken Vietnamese in the coach's pair. Two lines still read translated:
  - Nhi "Hiểu tới mức thấy cái họ thấy lúc vừa thức dậy."
  - Nhi "cho người lạ thấy bạn có ở đó vì họ".
- **Delivery:** one line above NEXT in 3/3. EN on Claude Free and Hạnh on ChatGPT Free Android both assume the app can
  create files. That is unverified per plan; Hạnh is a no-download persona, so the kit's "say 'chiến lược'" fallback
  would suit her better.

## 5. VN wording: lines that still read translated

| # | Line (where) | Why | Fix |
|---|---|---|---|
| 1 | "Hiểu tới mức thấy được cái họ thấy, lúc vừa thức dậy đã gặp chuyện đó." (Nhi N3 câu cuối; also in the strategy file) | "at a visceral level, you feel what they feel when they wake up with this problem", word for word | "Hiểu tới mức biết sáng ra mở mắt là họ lo chuyện gì." |
| 2 | "Người lạ thì chưa biết chị có ở đó vì họ." (Nhi long post; the same calque in N2 Ý2 "chưa biết mình có ở đó vì họ", the early win "biết bạn có ở đó, và biết bạn có đúng thứ cho họ", and the file's Ý1) | "you're there for them", "you have this stuff for them" | "Người lạ thì đâu biết chị giúp được gì cho họ." |
| 3 | "Lớp sau mới là gom bối cảnh, con số, thị trường, rồi phân tích." (Nhi N3 Ý2) | her English list calqued; a Hán-Việt stack in a spoken script | "Rồi mới tới coi số liệu, coi thị trường." |
| 4 | "Chị ơi, nhờ chị một chút: em đang viết lại cách giới thiệu công việc của em, muốn lấy đúng câu của chị." (`research.ask3`; Hạnh: "…chị đang viết lại cách giới thiệu lớp kèm, muốn lấy đúng câu của em.") | "rewriting how I describe my work, want your words": stiff, and "lấy câu" sounds like taking. Flagged by the FT2 placeholder, not fixed | "Chị ơi, cho em nhờ chút xíu: em đang sửa lại phần giới thiệu, muốn dùng đúng lời chị nói." |
| 5 | "Bạn nghĩ tới người khách bạn giúp được nhiều nhất nhé. Tuần đầu tìm tới bạn, họ đang kẹt chuyện gì?" (`dig.story`, printed at turn 7); runner-up `dig.proof` "…khác đi thế nào?" | "Think of one client… the week they first came to you"; "what changed" | "Bạn nhớ lại người khách bạn giúp được nhiều nhất. Hồi mới tìm tới bạn, họ đang kẹt chuyện gì?" · "Làm với bạn xong, giờ chị ấy ra sao rồi?" |

Hạnh's Vietnamese is otherwise natural Northern speech ("Ngại thì không sai đâu các em ạ. Sai là tưởng chào thì phải
dọa."). Her gap is density: beats such as "Spa em ấy 4 kỹ thuật viên mà 3 giờ chiều giường trống trơn." end flat where
she would say "…trống trơn em ạ". Four of her captions open with the same "Em nào … thì nghe chị…" frame in one week.

## 6. Rules

- **At most 1 question per reply:** held in 3/3. Questions inside copy boxes (the 3-question gift, the inbox replies)
  are content, not asks to the coach.
- **Keyword:** specific, 2–3 words, from buyer words, and tagged by the current rule in 3/3.
  - KHÔNG AI NHẮN carries "(mình đoán)": one client, once.
  - NGẠI CHÀO and RECORD YEAR are untagged: one client plus "they all say it".
- **Week 1 only after OK:** "ok", "ok em", and "next" after the modelled Claude Free limit (DECISIONS: "OK, next, go").
  3/3.
- **Quiet option:** Hạnh ("Chị ngại xin comment thì gõ 'nhẹ'.") and EN ("(quieter: say 'quiet')") printed it. Nhi did
  not. Her persona dislikes "comment to get" endings, so that was the one run where it mattered.
- **Guesses named once above Week 1:** 3/3 (talk day; Nhi's list "chưa có", which is wrong for her; she can fix it with
  one word).

## 7. Grader failures: real or false positive, and what they missed

| Run | Check | Verdict | Why |
|---|---|---|---|
| Nhi | `day0_shape` (no quiet option) | real | see §6 |
| Nhi | `hook_lab` (N2 on-screen = line 1) | real | 80% of the on-screen words come back |
| Nhi | I23 (2 of 9) | real | the denominator counts the TikTok paste-steps box ("Lúc nào rảnh 15 phút: 1 Mở TikTok…"), which is not a piece; at 2 of 8 it still fails |
| Hạnh | I23 (2 of 9) | real | N1–N3 and the Zalo asks carry none of "khách không sợ giá đâu, khách sợ bị dọa", "chị nói thật nhé" |
| Hạnh | `vn_natural` (24% vs 54%) | real | flat beat endings (§5) |
| Hạnh, EN | `leaks` warnings (Hạnh 25, EN 19) | not failures | spot-checked: all compressions of dictated facts ("tự cầm, tự nhìn. Chỉ đúng một chỗ" ← turn 7; "30-minute fit call" ← turn 7) |

0 false positives (FT1 had 4 FP classes). **Missed by the graders** (each is a real fail found by hand):
1. Nhi's FILM TODAY on-screen paraphrases line 1 and the frame (33% word overlap passes).
2. The caption line-1 maxims "Viết sao thì để sau, tại sao phải có trước." and "Người quen mua vì đã biết bạn. Người lạ thì
   chưa." are not in the `flat_claims` families.
3. The on-screen label "Nghiên cứu có hai lớp".
4. Hạnh's captions parse as empty: they sit in their own copy box with no "Caption:" label, so the caption check never ran.
5. EN slide 1: 61 characters plus "might". `hook_lab` reads shorts only, not slides, titles or subjects.
6. Neither strategy file is graded: "The bank app isn't a forecast." on screen and the stretched GIỮ / "held" lines pass
   unseen.
7. The research log is not graded: stretched KEEP counts, a typo silently fixed, and a 2-word undictated echo in queries.

## 8. Prioritised fix list

1. **Run the hook lab on every hook, the strategy file's included.**
   - `modules/vn/fmt-short.md` §CM-FORMATS 1 and `core/vn/ship-check.md`, with the EN mirrors:
     - on-screen text never re-says line 1 in other words and never just captions the frame;
     - the last line lands the answer, never a name ("Chị gọi là cầm gương nói thật");
     - caption line 1 is never a maxim.
   - `modules/{en,vn}/strategy-doc.md` SOÁT THẦM: "the 2 hooks per idea pass §CM-HOOKS; no flat claim on screen".
   - `modules/en/packaging.md`: slide 1 and titles ≤60 characters, no "might".
   - Budget: PLAYBOOK has room (7 KB of 30 KB). The VN method file has 52 B, so pay for the core line with a cut.
2. **Nothing invented in the file or the pieces** (`modules/{en,vn}/strategy-doc.md` item 2/4, `modules/vn/humanize.md`).
   - Never give a client an action or thought the coach did not report: "Chị ấy không đăng thêm bài nào", "Chị tưởng
     phải đăng nhiều hơn", "câu nào cũng dọa da".
   - Held lines print only lines that say the pattern in their own words, exactly as on the page (typos "(sic)", trims
     "…").
3. **KEEP recount** (`modules/{en,vn}/research.md` rule 5 and §CM-LISTEN, RESEARCH level-ups):
   - reviews under one product page are one place;
   - a line backs a pattern only in its own words;
   - a two-part pattern needs both parts backed;
   - "{n} nơi" counts sites, with threads shown apart.
   - A KEEP that renames a Map topic is recounted by the reviewer helper first.
4. **Make the research test clean** (`evals/run.py` MACHINE.md web-lane text, `evals/graders.py` protocol `leaks`).
   - Run the research pass as a separate agent that sees only the transcript up to that turn, never the persona files.
   - Log the turn each query really ran after.
   - Add a leak check on the research log (answer-bank-only runs of 2+ content words in queries, e.g. "which clients").
   - Re-run EN to see whether topic 1 still changes.
5. **VN voice** (`modules/vn/humanize.md` §CM-NATURAL 4, `core/vn/ship-check.md`).
   - Each short's last line or caption carries one card phrase where it fits.
   - A high-particle coach's dặn / rủ beats end on her particles.
   - `evals/graders.py` I23: leave the paste-steps box out of the pieces.
6. **Quiet option as a fixed line** after every Day-0 keyword ask (`core/vn/start-block.md` step 6, `strings/vn.toml`
   `cmd.quiet`). Nhi's run dropped it.
7. **VN strings** (`strings/vn.toml` `dig.story`, `dig.proof`, `research.ask3`, per §5; still unchanged from the FT2
   placeholder). Add the "có ở đó vì họ / có đúng thứ cho họ" calque to `locales/vn/banned-tells.txt` or the
   humanize table.
8. **Graders** (`evals/graders.py`).
   - `check_hook_lab`: on-screen words all inside line 1 ∪ frame; label families ("… có hai lớp", "Không cần …",
     "Câu đúng nằm ở …"); a caption in its own box; text-post line 1, slide 1 and subjects (HL9 length, hedges).
   - A new `strategy_doc` check on CONTENT-STRATEGY.md / CHIEN-LUOC-NOI-DUNG.md: 7 headings in the card's pair,
     `flat_claims` on its hooks, each held line verbatim among the notes' kept lines.
   - A `research_log` check: each KEEP backed from ≥2 distinct pages and hosts.
   - `qa/standards/strategy-doc.md`: exempt "(content pillars)" in part 3's heading (still open from the placeholder).
9. **Browser lane for the VN personas** (`evals/run.py`): still 0 buyer lines for Hạnh from 8 public pages. Without
   Facebook groups and TikTok comments, LN2 stays at 1 and the Map stays unchanged.
