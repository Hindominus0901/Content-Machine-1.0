# Content calendar and strategy steps standard (`calendar`)

Build-only rubric (wf12-qa-spec §3.1 shape). Never shipped. It is the G3 judge rubric for the strategy engine's step cards (§CM-STRATEGY-ENGINE), the content lines (§CM-CONTENT-LINES) and the 4-week calendar (§CM-CALENDAR), all in `modules/<lang>/strategy-doc.md` (PLAYBOOK level-up), and the source of `standard = "calendar"` eval cases.
Sources, in order: the founder request (9 Oct, v13: people don't know what calendar to keep or which content both draws interest and converts; strictly in sequence, 2-3 options A/B/C with a one-line reason each, one marked recommended, never a vague "do you want…?" ending) · `modules/en/strategy-doc.md` · `docs/research/strategy-coverage.md` (Soo Wei Goh first, Matt Gray's ideas renamed) · `season-plan.md`, `strategy-doc.md` (the parts it reuses) · `vn-naturalness.md`.

## Purpose

The coach leaves with a strategy built one decision at a time and a calendar they can run from Monday: every piece placed on a day, a platform, a content pillar, a named line and a type, with its length in words, its hook family, its shape and its ask, and a month that adds up to the mix they chose and the hours they really have.

What good means: each step offered as 2-3 real alternatives with one pick backed by the coach's own words or the research; nothing skipped; the content lines give every pillar that holds 2+ lines something that draws people in and something that earns trust (the pillar holding the CONVERT line: trust + the offer); the calendar is complete, balanced and honest about time; it is saved where the next chat can pick it up.

## Scope

- **Artifact:** the step replies of the engine (steps 1-8, or the "ok all" reply), the content lines table, the 4 weekly calendar tables with their totals, and the save lines (strategy file, hub). Also a re-made calendar after "plan next month" and a reflowed one after a missed week. On Day 0 the chat prints week 1's table only, after FILM TODAY (founder, 9 Oct, retest v13): CL1 is scored on the strategy file's part 6 and the hub, which hold all 4 weeks; 4 tables printed before FILM TODAY fail CL1.
- **Output class:** Structured artifact filled at runtime from stored facts. The judge scores the fill against the transcript (dump, interview, research lines, Brand Card, earlier OKs).
- **Not here:** the pieces themselves (`shared.md` plus each format standard), the strategy document as a whole (`strategy-doc.md`), the season plan's beliefs (`season-plan.md`), hooks (`hook-lab.md`, `hook-library.md`).

## Items

| ID | Item | 0 | 1 | 2 | Critical |
|---|---|---|---|---|---|
| CL1 | Calendar complete [D] | Fewer than 4 weeks, or rows missing 3+ columns, or no totals | All 4 weeks, but 1-2 columns blank in some rows, or a week header without its trust step and belief, or the totals or hours line missing | 4 weekly tables; every row has Day · Platform · Content pillar · Line · Type · Format · Words · Hook · Shape · Ask · Status; each week headed "Week {n} · {what it shows} · belief: you think X → actually Y"; totals by type and hours a week under the 4 weeks | yes |
| CL2 | Lines per pillar | A pillar with no line; lines that are one-off topics, not series; no CONVERT line while an offer exists | More lines than the hours hold (e.g. 9 at 3 hours) with no merge or pause; a pillar with 2 lines lacks an ATTRACT or a TRUST line (the pillar holding the CONVERT line excepted: TRUST + CONVERT is right); CONVERT lines that skip a week; lines fixed before the hours are known (hours asked a reply later); or a line misses 2+ of its fields; or a CONVERT line not tied to the offer | Lines per pillar scale with hours (≤1 h: 1 each, ≤5 in all · ~3 h: 1-2 each, ≤8 in all · 5 h+: 2-3 each; merged or paused when pillars × lines exceed the month's slots, §CM-CONTENT-LINES 1); ATTRACT and TRUST lines follow the mix, a pillar with 2 lines has one of each, except the pillar holding a CONVERT line (TRUST + CONVERT, no ATTRACT needed); on Day 0 the hours are settled in the same reply as the lines (reply 2); 1-2 CONVERT lines tied to the offer (objection, a client's decision to buy, its price) that together run every week; each line has name in the coach's words, promise, format, length in words, how often, type, hook family, shape, ask; names they would say on camera | yes |
| CL3 | Steps with a recommendation | A step offered as an open question ("what do you want to focus on?"), or a reply ending "Do you want…?"; a step skipped without "ok all"; after Day 0, two steps in one reply; on Day 0, more than 3 strategy replies or one reply asking 2+ A/B/C | Options present but two are wordings of one idea, or a reason is missing, or the pick gives no evidence | In order 1→8. Day 0: grouped into ≤3 replies (1-2 positioning, pillars · hours, then 3-4 lines in a copy box, mix · 5-8 platforms, calendar, gift, asks), each one OK with ≤1 A/B/C, talk outside copy boxes ≤150 words (VN tiếng) in reply 2 and ≤200 EN / ≤250 VN in the others, the other steps pre-filled with the pick + reason; after Day 0 or on "details": one step a reply; 2-3 options that differ in kind, each with a one-line reason; exactly one pick with its evidence (a quote, "{n} people in {n} places", their hours); the last line invites A/B/C, an edit or "ok all"; a pre-filled step (rich dump) shows the pick + one alternative | yes |
| CL4 | Tier balance [D] | Totals off the OK'd mix by >10 points; a week with no TRUST or no ATTRACT; a DM, call or offer ask in week 1 | Totals off by 6-10 points; or a week without a CONVERT piece outside a launch flip; or 2 CONVERT in a row on one platform | Totals within 5 points of the mix; every week holds all three types; never 2 CONVERT in a row on one platform; direct asks from week 2 and only with proof; ≥3 gives per ask; launch window flipped as §CM-CALENDAR 8 | yes |
| CL5 | Word lengths [D] | Any length given in seconds or minutes of video; or a length 30%+ outside its format | 1-2 rows outside the range by up to 30%, or a row with no length | Every row's length in words within its format: short 500-800 · long post 850-1,150 · long video 1,000-1,500 · email or Zalo ≤250 · carousel 10-12 slides | yes |
| CL6 | Fits their hours [D] | More pieces than their hours hold (per §CM-CALENDAR 2) in any week; hours guessed up | The week fits, but the hours line is missing or doesn't add up | Pieces per week match their band; the hours line adds up with the per-piece minutes; spare time goes to replies, never extra pieces | yes |
| CL7 | Order and dates | Weeks out of trust order (proof before the stance week); a launch in tháng cô hồn (VN) | A dated item (launch, moment) placed but the weeks around it not flipped; or a moment that fails the buyer filter | Week 1 → 4 follow the trust steps; dated items keep their dates; a launch window flips the mix; VN moments from the buyer's year; a missed week slides without doubling up | no |
| CL8 | Hooks, shapes, asks in plain words | A framework name, code, score or stage label in a cell | Hook or Shape cells generic ("hook", "story") in 3+ rows; ask rungs out of order | Hook = a hook family in plain words; Shape = a copy shape's plain name; Ask = a rung (comment {KEYWORD} · follow · DM · call · offer); the month's asks about 6 in 10 the gift, 2 direct, 2 follow, share or none; one keyword or gift per line | no |
| CL9 | Saved and resumable | Nothing saved; a new chat starts the strategy over | Saved in one place only, or the open-step line missing mid-engine | Saved to the strategy file (part 6) and the hub (Notion rows, else HUB.md's month block); mid-engine the top line "Strategy: step {n} of 8 open"; a new chat opens at that step; status Idea/Scripted set by the machine, Filmed/Posted only on the coach's word | no |
| CL10 | Nothing invented, plain and natural | A number, result, client line or follower count not in the sources; a deny-list word in coach text; VN fails `vn-naturalness` VN3, VN4 or VN6 | A guess shown as fact once, without "(my guess)"; translated-sounding VN headers | Every fact traces to a source; guesses marked; gaps [NEEDS: …] / [CẦN BẠN: …]; coach text plain ("content pillars"/"trụ cột nội dung" allowed, never "pillar"/"trụ cột" alone); VN reads as spoken Vietnamese in the Card's address pair | yes |

## Build pass rule

- **Shared rule:** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; hard gates clear; no conditional pass; uncertain = 0.
- **Here:** CL1, CL2, CL3, CL4, CL5, CL6 and CL10 score 2, and the total is ≥16/20.
- A transcript that shows only the "ok all" path scores CL3 on the first card and the "ok all" reply (every pick printed, in order).
- A reflowed calendar (missed week) is scored the same way, plus CL7's slide rule; the re-made month 2 calendar also needs the review's calls behind each change.

## Hard gates

- Invented proof: a result, testimonial, client line, follower or view count the coach never gave.
- A direct ask (DM, call, offer) in week 1 with no proof, or a fake deadline anywhere.
- Any length in seconds.
- An engine step that ends on a vague question ("Do you want…?", "Shall I…?", "thoughts?") instead of A/B/C, or a step the machine skipped on its own.
- Coach-visible jargon: "pillar" or "trụ cột" alone, a stage label (Admirable…Trustable), "Buyer Filter", "Dream Follower", any Matt Gray framework name, a copy framework's name, a score, code or § id.
- **Never blocked:** the coach's comment keyword and their own ask wording; "chấm" or a comment threshold the coach chose (one dated platform note); a line or day the coach insisted on, shown as theirs.

## Runtime check shipped

For `core/format-checks.toml` (`[format.calendar]`):

```toml
[format.calendar]
checks = [
  "Is this one step only, with 2-3 different options, a one-line reason each, one pick with its evidence, and no 'do you want…?' ending?",
  "Does every content pillar with 2+ lines have an ATTRACT and a TRUST line (the CONVERT pillar: TRUST + CONVERT), and does each CONVERT line serve the offer?",
  "Does each week hold all three types, with totals within 5 points of the mix and no direct ask before week 2?",
  "Is every row complete, its length in words for its format, and does the week fit their real hours?",
]
checks_vn = [
  "Tin này đúng một bước, 2–3 phương án khác nhau, mỗi cái một dòng lý do, một lựa chọn có căn cứ, và không kết bằng 'bạn có muốn…?'?",
  "Trụ cột nội dung có 2+ tuyến thì có tuyến THU HÚT và tuyến NIỀM TIN (cụm giữ tuyến CHUYỂN ĐỔI: NIỀM TIN + CHUYỂN ĐỔI), tuyến CHUYỂN ĐỔI nào cũng phục vụ sản phẩm?",
  "Tuần nào cũng đủ ba loại, tổng lệch tỷ lệ không quá 5 điểm, và không mời inbox, gọi, mua trước tuần 2?",
  "Dòng nào cũng đủ cột, độ dài đếm bằng chữ đúng dạng bài, và tuần vừa số giờ thật của họ?",
]
```

## VN note

- Column headers: Ngày · Kênh · Trụ cột nội dung · Tuyến · Loại · Dạng · Số chữ · Hook · Cách viết · Lời mời · Trạng thái; types THU HÚT / NIỀM TIN / CHUYỂN ĐỔI; status Ý tưởng → Đã viết → Đã quay → Đã đăng.
- Step cards "Bước {n}/8 · {tên}"; the last line offers A/B/C, a change or "ok hết"; the pick reads "Mình chọn {option}, vì {reason}."
- Tin Zalo counts as the email; the ladder runs comment từ khoá → inbox → quà → Zalo or a call → the offer, price said plainly (never "giá ib").
- Moments from the Vietnamese buyer's year (Tết, 8/3, 20/10, 20/11, back to school); no launch in tháng cô hồn.

## Scenarios the eval set should hold

1. Rich dump, coach types "ok all" at step 2: steps 3-8 printed in order, a line each, then the calendar; nothing silently skipped.
2. Thin dump: step 1 opens with one §CM-STRATEGY question, then full cards.
3. Resume: a new chat after step 4 opens "We stopped at step 5 of 8" with the step-5 card; steps 1-4 not asked again.
4. Launch in week 3: weeks 1-2 TRUST-led, open days CONVERT-led, one ATTRACT a week kept, campaign day cards in those slots.
5. Missed week 2: the calendar slides; week 3's proof does not jump ahead; nothing doubles up; "Picking up at week 2."
6. 8 hours a week: one long video per week cut into 4 shorts, 1 long post, 1 carousel, 1 email or Zalo.

## Calibration (fictional coaches)

**PASS.** EN, a career coach for nurses moving into health tech, LinkedIn + email, about 3 hours a week, mix 40/40/20, keyword PIVOT. Step 2 offers A) by the buyer's worries, B) by the craft, C) B + their "bedside to backlog" method as a pillar; the pick is B, "your dump says 'nobody explains what a product job actually is' and 9 people in 3 places asked the same". Lines: 3 pillars × 2 lines + 1 CONVERT email ("Before you apply"). Calendar: 4 weeks × 5 rows, all columns, lengths in words (long posts 1,000, carousels 10 slides, emails 230), ATTRACT 8 · TRUST 8 · CONVERT 4; first call ask in week 2 after their process post; hours line "about 3 h ✓". Saved to the file and HUB.md. CL1 2 · CL2 2 · CL3 2 · CL4 2 · CL5 2 · CL6 2 · CL7 2 · CL8 1 (3 Shape cells say "story") · CL9 2 · CL10 2 = 19/20. **Result: PASS.**

**FAIL.** VN, a fitness coach for office women (chị–em pair). The reply after the interview prints positioning, pillars and the whole calendar at once and ends "Chị có muốn em làm thêm lịch tháng sau không?"; week 1 carries "Inbox em để đăng ký gói 1 kèm 1"; two shorts list "60 giây". Hard gates: a vague ending and skipped steps; a direct ask in week 1 with no proof; lengths in seconds. CL3 = 0, CL4 = 0, CL5 = 0. **Result: FAIL** ("Chị có muốn em làm thêm lịch tháng sau không?"; "60 giây").
