Result: FAIL

# Retest FT1 (founder-test fixes, Day 0): VN copywriter-thin, VN Hạnh, EN consultant: independent review

Reviewer: independent, bilingual (EN, plus native Vietnamese for the VN runs). I wrote neither the kit nor the runs.
Trigger: the founder's own Day 0 (7 Oct, VN edition), verdict "tạm", "đặc biệt phần headline và hook là chưa ổn"
(`scratchpad/founder-test/transcript.md`). Rubrics: `qa/standards/hook-lab.md`, `research-brief.md` (LN1–LN7),
`vn-naturalness.md`; founder decisions: the last bullets of `docs/DECISIONS.md` (7 Oct, night).

How this review was done:
- All 3 transcripts read in full, as the coach reads them on a phone; notes.md and grades.json read in full.
- Each packet's `kit/` is byte-identical to `dist/{en,vn}/` (method file + instructions). Scratch copies re-graded with
  the current `evals/run.py grade`: the same failed lists in 3/3. `transcript.jsonl` = `transcript.raw.jsonl` in 3/3.
- Research re-checked at source: 12 kept lines re-fetched (voz ×3, VnExpress, Warrior Forum, HN Algolia API). All 12
  strings are on the pages; two problems found (§2).
- Every hook and headline in FILM TODAY and Week 1 scored on HL1–HL9 + HG1–HG3 (uncertain = 0).

## Scorecard

| Area | VN copywriter (thin dump) | VN Hạnh (rich dump) | EN consultant (rich dump) | Verdict |
|---|---|---|---|---|
| Run validity | **invalid** (protocol `pace`, simulator's timing) | valid, 0 edits | valid, 0 edits | 2/3 valid |
| (1) Extraction: dig fires when thin, stays out when rich | fired: 4 one-question asks → 6/6 slots | 0 extra questions → 6/6 | 1 question on the cut → 6/6 | **PASS** |
| (2) Research, Day-0 LN1–LN7 (pass: LN1/3/4/5 at 2, ≥12/14) | 10/14, LN1 1 · LN3 1 · LN4 1: **FAIL** | 12/14, LN4 1: **FAIL** | 12/14: PASS | **FAIL** |
| (2) Did research change the Map? | no | no | no | 0/3 |
| (3) Hooks passing hook-lab (FILM TODAY + Week 1) | 2/5 | 2/5 | 3/6 | **FAIL** (7/16) |
| (3) FILM TODAY hook alone | PASS | PASS | PASS | PASS (3/3) |
| (3) Founder's two flat lines gone? | "Đó không phải research." survives as on-screen "Vậy chưa phải nghiên cứu" | n/a | n/a | **not fixed** |
| (4) VN pieces 100% Vietnamese (early win too) | yes | yes | n/a | PASS |
| (5) ≤1 question per reply | yes (`dig.proof` is 2 asks under 1 "?") | yes | yes | PASS (minor) |
| (5) Keyword specific, from buyer words | KHÔNG AI NHẮN, "(mình đoán)" (1 client) ✓ | NGẠI CHÀO, untagged (Thảo + "bao nhiêu em nói y hệt") ✓ | RECORD YEAR, untagged (Marcus + "all of them say") ✓ | PASS |
| (5) Week 1 only after OK | after "ok" | after "ok em" | after "next" (limit reset; DECISIONS allows) | PASS |
| (6) Grader fails: real / clash / FP | 8 + `pace`: 4 real · 1 clash · 3 FP (`day0_shape`: both items FP); `pace` real (simulator) | 2: 1 real · 1 FP | 1: 1 real | 6 real + 1 simulator |
| VN naturalness (`vn_natural`) | 7% end particles vs her 20% | 16% vs her 54% | n/a | **FAIL** (both) |

**Why FAIL, in one line each:**
- Hooks: the founder's exact defect survives in Week 1. A flat claim is on screen again ("Vậy chưa phải nghiên cứu"), and
  in 4 of the 6 VN Week-1 shorts the on-screen text repeats the first spoken line. Only 7 of 16 hooks pass.
- Research: honest and silent now, in buyer language, nothing invented in a piece. But it changed the Map in 0 of 3 runs
  and found 0 KEEP patterns. Two VN slips at source: a seller line cut so its meaning flips, and a reporter's paraphrase
  kept as an owner's words.
- VN voice: particle density is far below the coach's own in both VN runs. It is the hooks' "doesn't sound like her" problem.

**What clearly improved vs the founder test:** the dig (a concrete client, her verbatim words, offer, price, proof with OK,
all before the Map); FILM TODAY hooks 3/3 concrete and paid off; no English in VN pieces, the early win included; a
specific keyword instead of "KHÁCH"; one question per reply; Week 1 only after OK; queries in Vietnamese buyer words.

## 1. Extraction (§CM-DIG)

| Slot | Copywriter (thin) | Hạnh (rich) | EN consultant (rich) |
|---|---|---|---|
| Buyer | from the story: 1-1 coach, posts daily, "many hearts, zero messages" | small new spa owners, 2–5 KTV, 28–40 | agency founders, $1–5M, record year, no cash |
| Client's exact words | asked → "Bài nào em đăng cũng có người thả tim, mà không ai nhắn hỏi giá hết." | Thảo: "Chị ơi em ngại chào lắm, cứ mở miệng chào thẻ là em thấy mình như đi lừa người ta" | Marcus: "Record year. Empty account. Make it make sense." · Dee |
| One real client story | asked → Bình Thạnh café, 3 old clients × 30 min | Thảo; 2018 cô giáo | 2019 stairwell; Marcus |
| Offer + price | asked → 3 tuần, 9.500.000đ, 2 đợt | in the cut answer: 6 tuần, 6.500.000đ | asked on the cut: Margin Sprint, $7,500 |
| Proof + client's OK | asked → 180 / 7 / 2 / 1, "no name" | Thảo 2/10 → 5/10, name OK, no spa name, no ads | Marcus all, Dee no amounts |
| What the field gets wrong | dump: "That is not research", jump to posts | dọa da scripts, 99k, ads | "top line theater" |

- **Thin dump: the dig fired as designed.** After "Done." the machine asked, one per reply, in the kit's order (kit
  strings adapted to the client she had just named):
  - "Bạn nghĩ tới một khách bạn giúp được nhiều nhất nhé. Tuần đầu tìm tới bạn, họ đang kẹt chuyện gì?"
  - "Lúc mới tìm tới bạn, chị coach đó nói gì? Nhớ được nguyên văn thì càng hay."
  - "Khách gật đầu làm với bạn thì họ nhận được gì, trả bao nhiêu?"
  - "Làm với bạn xong, chị coach tài chính đó khác đi thế nào, và chị có chịu cho bạn kể lại không?"
  The founder test asked none of these and guessed all of them. Cost: the Map came after 10 coach turns (budget 7), but
  at 12.7 minutes. The 7-turn budget predates the 7 Oct dig decision (§6).
- **Rich dumps: it stayed out of the way.** Hạnh got only mid-dump hints ("Gợi ý: các em chủ spa lúc mới tìm đến chị
  hay nói câu gì…") and one question riding the soft cut: "Chị đang có 2 nguồn thu… Đúng không?". EN got one: "That's
  plenty for today. If you have one more story, tell it now. If not: when someone says yes to you, what exactly do they
  get, and what do they pay?"
- Residual: `dig.proof` (strings/vn.toml, strings/en.toml) carries two asks under one question mark ("khác đi thế nào,
  và … có chịu cho bạn kể lại không?"). The coach answered both. It is still the one place a reply asks two things.

## 2. Research (Day-0 listening pass)

| | Copywriter | Hạnh | EN |
|---|---|---|---|
| Queries | 23, Vietnamese | 21 Vietnamese (19 returned) | 27 web + 11 HN API |
| Buyer language? | yes, but 11/23 aim at online-shop selling ("bán hàng online", "không ra đơn"), only 6 at coaches or course sellers | yes: "ngại chào", "để chị về suy nghĩ", "sợ khách nghĩ … chặt chém", "giường trống" | mostly; 2 worded from undictated persona lines (logged) |
| Places with kept lines | voz, Dân trí, (webtretho, blog: 0 kept) | voz, VnExpress, webtretho (baophapluat, eva/vietnamnet: 0) | Hacker News, Warrior Forum |
| Pages read | 8 of 10 | 8 of 13 | ~14 read of 26 fetched (the summary's "26 opened" counts fetches) |
| Verbatim lines | 9 from 7 people, **all not the buyer** | 5, 2007–6/2025, none says "ngại chào" | 5, 2011–2018 |
| KEEP / WATCH | 0 KEEP | 0 KEEP, 5 WATCH | 0 KEEP; "make payroll" WATCH |
| Map line 1 + keyword from | her client, one person → "(mình đoán)" | Thảo + "bao nhiêu em nói y hệt" | Marcus + "all of them say it" |
| Unverified line in a public piece | none from research (but see I9, §3) | none | none |
| LN1–LN7 | 1·1·1·1·2·2·2 = 10 | 2·1·2·1·2·2·2 = 12 | 2·1·2·2·2·1·2 = 12 |

- **Process: the founder's defects are fixed.** The pass ran silently from the first send. Queries were in Vietnamese
  buyer words, not the coach's complaint. Nothing was said before the Map. Places, counts and months show under the Map.
  The Map honestly says where line 1 came from, and the Week-1 paste step is exact ("mở 3 video TikTok nhiều view nhất khi
  tìm 'chủ spa ngại chào thẻ', mỗi video chép 20 comment…").
- **Yield: still not research the coach can see.** In 3/3 runs the notes say the research changed nothing on the Map.
  The founder would say what the copywriter persona says: "That is not research." The cause is mostly the harness
  (WebSearch's US index, no browser, Facebook groups / TikTok / LinkedIn unreadable). Part of it is the packet: it does
  not ship `Level-ups/RESEARCH-{EN,VN}.md`, so §CM-LISTEN never loaded, though the founder's own Cowork folder had it.
- **Re-checked at source (all 12 strings found), with two VN slips:**
  - Copywriter Map: "Câu gần nhất: '…tương tác rất nhiều nhưng đơn thì giảm rất mạnh' (người bán online, voz, 8/2025)".
    The page reads "Tỷ lệ tin nhắn, tương tác rất nhiều nhưng đơn thì giảm rất mạnh". The cut drops "tin nhắn": this
    seller gets *many* messages. The cut line now seems to back the Map's "không ai nhắn". It is a cut quote and a
    non-buyer, printed on the decision screen (LN3 1, LN4 1).
  - Hạnh notes: "…dịch vụ này được mở ra quá nhiều, dẫn đến cạnh tranh nên giá cũng giảm mạnh" is kept as a spa owner's
    line (VnExpress, 2007). On the page it is the reporter's indirect speech ("Bà … cho biết …"), not her words. It is a
    report used as buyer voice. Notes only, not printed (LN4 1).
  - EN: the "Where I listened" line reads 'Line 1: "managing cash flow so that I could actually make payroll all the time"
    (agency owner, Hacker News)'. Map line 1 came from Marcus. The kit's EN template ("Line 1: "{line}" ({role}, {place})")
    invites this; VN says "nguồn dòng 1 theo vai" and both VN runs got it right (LN6 1).
- Copywriter LN1 = 1: the queries drifted to a neighbour group, mostly one kind (symptom). LN2 = 1 in all three: under 12
  lines, unread places named.

## 3. Hooks and headlines (hook-lab)

| Run · piece | Hook as printed (on-screen / frame / first line → last line) | Fails | Verdict |
|---|---|---|---|
| VN Nhi · QUAY HÔM NAY | "Một chị coach than với mình" / phone, a post full of hearts / "Bài nào em đăng cũng có người thả tim, mà không ai nhắn hỏi giá hết." → "Muốn người lạ nhắn thì hỏi khách cũ trước, rồi mới viết." | none (on-screen is a label, weak) | PASS |
| VN Nhi · bài dài | "Chị ấy mở Facebook cho mình coi: bài nào cũng nhiều tim, mà không ai nhắn. / Mình hỏi chị đúng một câu. Chị không trả lời được." | none | PASS |
| VN Nhi · N2 | "Không ai nhắn? Hỏi vì sao" / laptop, a draft / "Hỏi mình cách viết bài, mình hỏi lại: vì sao người ta mua của bạn?" → "Chưa có vì sao thì cách nào cũng chỉ là tiếng ồn." | HL1 (nothing seen), HL3 (last line restates, pays nothing), HL4 ("start with why": nobody disagrees) | FAIL |
| VN Nhi · N3 | "Vậy chưa phải nghiên cứu" / scrolling posts / "Em nghiên cứu rồi." Mình hỏi làm gì. "Đọc vài bài, nhờ AI tìm từ khoá." | HL7 (on-screen = the founder test's "Đó không phải research."), HG1 / I9 (an English report put in quote marks as a verbatim line) | FAIL |
| VN Nhi · N4 | "Một email, 180 người" / inbox / "Một email gửi 180 người: 7 người trả lời, 1 người mua." | HL8 (on-screen repeats the first line) | FAIL |
| VN Hạnh · QUAY HÔM NAY | "41 thẻ, 27 thẻ bỏ dở" / chị ở quầy, nhìn vào máy / "3 tháng spa chị bán được 41 cái thẻ, chị khao cả spa đi ăn lẩu." → "Bán được thẻ chứ mình có giữ được người đâu." | none (frame weak: the card book is the object) | PASS |
| VN Hạnh · N1 | "Khen tay nhẹ rồi mất hút" / quầy, điện thoại / "Khách khen tay em nhẹ mà cứ để chị về suy nghĩ rồi mất hút." → "Mà làm xong để khách về thì cuối tháng lấy gì trả lương thợ." | HL8 (same words), HL3 (no payoff), HL4 (pain only, no shift) | FAIL |
| VN Hạnh · N2 | "Sợ khách nghĩ mình chặt chém" / cầm gương / "Em sợ khách nghĩ mình chặt chém." → "Mà khách không sợ giá đâu, khách sợ bị dọa." | HL8 (on-screen = first line) | FAIL |
| VN Hạnh · N3 | "40 triệu, toàn khách săn 99k" / cửa spa / "40 triệu tiền quảng cáo, chị ra toàn khách săn 99k." | HL8 (on-screen = first line) | FAIL |
| VN Hạnh · bài dài | "'Em tin chị mà chị.' Câu đấy chị nhớ đến tận bây giờ." | none | PASS |
| EN · FILM TODAY | "Record year. Still no cash." / desk, Marcus's sticky note / "Best year ever. I'm in a stairwell, asking the bank for payroll." → "Your biggest client is not your best client until you've done the math." | none (text version: keyword only in the ask, "that call" has no referent) | PASS |
| EN · email | "The Monday Number: minus 6" (+ "Or:" ×2, the kit's 3 subjects) | HL9 (a series label, no reader result); 3 subjects vs HG3 is a kit/rubric clash | FAIL (weak) |
| EN · Wed post | "If your margin's broken, growing just makes the hole bigger, faster." | HL1, HL2 ("margin's broken" is her term), HL3, HL7 (maxim states the ending) | FAIL |
| EN · slides | slide 1 "Record year. Empty account. Start here." | HL9 (a label), HL3, HL4 | FAIL |
| EN · Fri post | "I check the bank app like it's a heart monitor." | none | PASS |
| EN · N1 | "The client you love, by margin" / legal pad, client list / "Usually one client is underwater. Usually it's the one you love." → "You can keep a client you love on purpose…" | none (on-screen phrasing clumsy) | PASS |

DMs, Zalo asks and inbox replies open in the coach's own words ("Chị ơi, em là Nhi nè.", "Em ơi, nhờ em một chút…",
"Quick favor: …"). They pass and are not counted above.

**Founder test vs this round**

| Founder test (7 Oct) | This round | Status |
|---|---|---|
| VIDEO 2 on-screen "Đó không phải research." + "…That is not research." | Nhi N3 on-screen "Vậy chưa phải nghiên cứu"; caption "…mà đó chưa phải nghiên cứu." | **Not fixed**: the same flat claim, now in Vietnamese. The counter-example lives only in STRATEGY-VN §CM-HOOKS 4, which the packet doesn't ship |
| VIDEO 3 on-screen "Khách phải tin bạn." + first line "Muốn người ta thành khách, họ cần tin bạn." | No trust hook. The idea closes the long post in her own posted words ("Khách không đến từ bài đăng. Khách đến từ chuyện họ tin bạn đủ để nhắn một tin."). The early win still lists "Muốn ai đó thành khách thì họ phải tin bạn…" as a line worth money | Fixed as a hook; the early win's 2nd line is still flat |
| On-screen text = spoken line | VN Week 1: 4 of 6 shorts (Nhi N4; Hạnh N1, N2, N3). EN: 0 of 2 (the EN kit says "on-screen ≠ first line", the VN kit only "không lặp nhau") | **Not fixed in VN** |
| English sentence in a VN piece; early win in English | none; early win "Khách đến từ chỗ bạn thuyết phục được người ta. Mà thuyết phục được là nhờ người ta đã coi bạn đủ nhiều." | Fixed |
| Guessed client line in a public piece | none guessed; one translated "quote" (N3, I9) | Mostly fixed |

**The 3 weakest, with a stronger rewrite (facts only from the transcripts):**

1. **VN Nhi N3.** Chữ "Vậy chưa phải nghiên cứu" · câu đầu: "Em nghiên cứu rồi." Mình hỏi làm gì. "Đọc vài bài, nhờ AI tìm từ khoá."
   - Fails HL7 (it is the founder's flat line) and HG1 (an English report in quote marks).
   - Rewrite:
     - Chữ trên màn hình: "AI đâu có gọi khách cũ" (6 tiếng)
     - Khung hình đầu: màn hình điện thoại, khung chat AI gõ dở "từ khoá cho coach tài chính"
     - Câu đầu: "Đọc vài bài, nhờ AI kiếm từ khoá, vậy là hiểu khách rồi hả?" (14)
     - Ý: Chị coach tài chính đăng gần như mỗi ngày, tim nhiều, không ai nhắn · Mình gọi 3 khách cũ của chị, mỗi người 30 phút · Có một câu khách nói ra, mình đặt ngay giữa trang của chị.
     - Câu cuối: "Câu làm người lạ nhắn tin là câu khách cũ nói ra, AI không đoán được đâu." (17)
   - Why it is stronger: the scene is visible, the loop is paid off, the on-screen text adds something the first line
     doesn't say, nothing sits in quote marks that she did not say in Vietnamese, and her "nha/đâu" register fits.
2. **VN Hạnh N1.** Chữ "Khen tay nhẹ rồi mất hút" + the same words as the first line; last line adds pain, no answer.
   - Rewrite:
     - Chữ trên màn hình: "10 khách, 2 người hẹn lại" (6)
     - Khung hình đầu: chị lật cuốn sổ hẹn ở quầy
     - Câu đầu (Thảo, nguyên văn): "Khách khen tay em nhẹ mà cứ để chị về suy nghĩ rồi mất hút."
     - Ý: Thảo ngại chào, làm xong là để khách về · Chị bảo Thảo đưa gương cho khách cầm, chỉ đúng một chỗ, hẹn buổi sau · 6 tuần sau Thảo đếm sổ: 10 khách thì khoảng 5 người hẹn lại.
     - Câu cuối: "Chị không bán thẻ đâu các em, chị bán buổi hẹn sau." (her phrase, her "các em" pair, with a particle)
     - Caption keeps "kết quả tuỳ người, không phải cam kết". Thảo's name is cleared; no spa name, no ads.
3. **EN Wednesday post.** "If your margin's broken, growing just makes the hole bigger, faster." is a maxim with no
   scene, in her term, stating the ending.
   - Rewrite: line 1 "\"Record year, and I put payroll on my personal card.\"" (a client line she reports many saying,
     10 words). Line 2: "I hear some version of that every month."
   - Last line: "Before you add a client, find the one you're paying to keep."
   - Same body. Slide 1 by the same lab: "Find the client you're paying to keep (5 steps)".

## 4. VN pieces 100% Vietnamese

Both VN runs: no English sentence in any piece, the early win included. Loanwords only (coach, email, Facebook, Zalo,
AI, inbox, comment, TikTok; Hạnh's own "phây", "serum", "sale"). Two words are outside Nhi's `code_mix`: "podcast"
(she says it in her dump) and "laptop" (a frame direction, not a spoken line). **PASS.**

## 5. Rules

- One question per reply: held in 3/3. The two-ask `dig.proof` string is the only soft spot (§1).
- Keyword: specific, 2–3 words, buyer words, and tagged by the current rule in all 3:
  - KHÔNG AI NHẮN is one client once, so it carries "(mình đoán)";
  - NGẠI CHÀO and RECORD YEAR are "one client + they all say it", so no tag (the founder's "trust the coach").
  - The founder test's "KHÁCH" is gone.
- Week 1 only after OK: 3/3.
- One more check, from the Map template: "{ai} nào hay than '{lời khách thật}'". On a one-client keyword this prints
  "Coach nào hay than…", the founder-test shape, but only on the decision screen and with the guess tag. Acceptable.

## 6. Grader failures: real or false positive

| Run | Check | Real / FP | Why |
|---|---|---|---|
| Copywriter | `pace` (protocol) | real, simulator | 2 posts pasted in 0.6 min (needs 1.0); invalidates the run |
| Copywriter | I9 | real, machine | "Em nghiên cứu rồi." is her English report in quote marks; the kit has no rule for English-dictated reported speech in VN pieces |
| Copywriter | I15 | **FP** | third-person "chị" ("chị coach đó"); she is still addressed as "bạn" |
| Copywriter | I23 | real | 2 of 9 pieces (22%) use her phrases (min 50%) |
| Copywriter | `quit_triggers` | real | 349 words before the first copy box: the FILM TODAY script is not boxed (Hạnh's is), and the research block runs 4 lines |
| Copywriter | `day0_timing` | design clash | 4 dump sends + 4 dig answers; `map_max_turns_vn = 7` predates §CM-DIG; film-ready at 12.7 min |
| Copywriter, Hạnh | `day0_shape`: "xem nghiên cứu" read as the CTA | **FP** | the kit's own closing line; not in `cmd.*` strings, so `cta_keyword` takes it |
| Copywriter, Hạnh | `day0_shape`: "[TikTok · 10/2026]" unfilled | **FP** | the kit's literal "[{place} · {month}]" header, filled |
| Copywriter | `vn_natural` | real | 7% end particles vs her 20% |
| Copywriter | `vn_messages` "Dạ" | **FP** | in inbox reply 2 Nhi is "em", the reader "chị": "Dạ" is right |
| Hạnh | `vn_natural` | real | 16% vs her 54%; scripts end flat ("…giường trống trơn.") |
| EN | `day0_shape`: text version | real, machine | RECORD YEAR only in the ask (§CM-FORMATS 7) |

No grader checks what hurt most this round: on-screen text = first line, and a flat claim on screen.

## 7. Prioritised fix list

1. **VN hook trio in the core kit** (`modules/vn/fmt-short.md` §CM-FORMATS 1, `core/vn/ship-check.md`).
   - Say it as the EN kit does: "chữ trên màn hình ≠ câu đầu: nói một điều câu đầu chưa nói (số, đối lập, câu hỏi)".
   - Move the TRƠN/HAY pair from STRATEGY-VN §CM-HOOKS 4 into the core. Name "Đó/Vậy không phải…" and "…phải tin bạn"
     as phán suông that fail on screen and in caption line 1 too.
   - Ship Check: "Chữ trên màn hình có lặp câu đầu không?"
   - The VN method file is at 56,252 / 56,320 B, so pay for this with a VN cut.
2. **Grader + cases for the two hook defects** (`evals/graders.py`, `evals/cases/` with `standard = "hook-lab"`).
   - Fail when most of the on-screen content words reappear in the first line.
   - Fail a flat-claim on-screen pattern.
   - Seed cases from Nhi N3/N4 and Hạnh N1–N3.
3. **EN text-post and slide hooks** (`modules/en/edge-rubric.md` GATES, `modules/en/fmt-short.md` §CM-POSTS 1,
   `modules/en/packaging.md`).
   - "questions only in the CTA" contradicts hook-lab HL3's own PASS example and the VN gate ("hỏi tu từ thì đáp
     liền"). Allow a hook question the last line answers, and a real person's quoted question (the banker's line).
   - Line 1 and slide 1 are a scene, a buyer line or their number, never an "If X, Y" maxim. Slide 1 is result-shaped.
4. **Quotes from English dictation** (`modules/vn/humanize.md` or `fmt-short.md`). Speech the coach reports in English
   is told without quote marks, or the Vietnamese original is asked for with `dig.words`. Quote marks only for words
   given in Vietnamese (I9).
5. **Make the research testable** (`evals/run.py`).
   - Ship `Level-ups/RESEARCH-*.md` and `STRATEGY-*.md` in the packet: the founder's Cowork folder had them, and this
     round neither §CM-LISTEN nor §CM-HOOKS loaded.
   - Replace MACHINE.md's "Searching the web is not possible" (line 250) for research lanes.
   - Add a browser lane (Claude in Chrome) for both VN personas. Without one, 3/3 runs ended with 0 KEEP and an unchanged Map.
6. **Research kit text** (`modules/vn/research.md`, `modules/en/research.md`, `core/en/start-block.md`).
   - Every query carries the buyer's role or place. The copywriter run drifted to shop sellers (11 of 23 queries).
   - The heard-where block never quotes a non-buyer line or a cut line.
   - A reporter's indirect speech ("cho biết") is not a buyer line.
   - The EN template "Line 1: "{line}"" becomes "Line 1 from: {role}", matching VN "nguồn dòng 1 theo vai".
7. **VN particles and phrases before printing** (`modules/vn/humanize.md` §CM-NATURAL 4, `core/vn/ship-check.md`).
   - Count end particles per piece against the coach's own rate.
   - At least half of the 60+ word pieces carry one of their phrases or openers.
   - Add one worked hook that ends on her particle.
8. **Map reply wall** (`core/vn/start-block.md` step 6). Put the FILM TODAY script in a copy box. When research changed
   nothing, the heard-where block is 1–2 lines.
9. **Grader false positives.**
   - `strings/{en,vn}.toml`: add `cmd.show_research` ("show the research" / "xem nghiên cứu"), which `cta_keyword`
     already skips as a command.
   - `evals/graders.py` `unfilled_placeholders`: accept a filled "[X · Y]" from the kit header.
   - I15: allow a third-person "chị/anh + noun/đó/ấy".
   - `vn_messages` "Dạ": read the coach's 1:1 self-pronoun from `address_1to1`.
10. **Budget after the dig decision** (`evals/acceptance.toml` `map_max_turns_{en,vn}`). Allow up to 4 dig answers on
    top; `map_max_minutes = 20` stays the real guard.
11. **Rubric/kit clash** (`qa/standards/hook-lab.md` HG3). Exempt email subjects: the kit prints 3 by design
    (EN "3 subject lines", VN "3 tiêu đề").
12. **`dig.proof`** (`strings/{en,vn}.toml`). Ask the result alone; move the OK to the Week-1 ask-3 message.
13. **Re-run** `ft1-day0-vn-copywriter-thin-S1` as r2 (r1 invalid: `pace`) after 1–4 and 7–9, with a browser lane per 5.
