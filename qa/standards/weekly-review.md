# Weekly review standard (`weekly-review`)

Build-only rubric (wf12-qa-spec §3.1). Never shipped. It is the G3 judge rubric for the Friday review and the source of `standard = "weekly-review"` eval cases.
Sources, in order: wf12-qa-spec §2.5, §2.8, §3.1, §4 "Weekly review" (final, wins) · wf12-qa-critique #49 (math by code) · wf12-qa-standards §15 (draft) · wf11-ux-spec §3.1–§3.2 and §5 item 10 (5-line Friday, spoken numbers, the 2× rule only with a board) · wf11 §4 rules 11, 12, 14 · wf13 §3 (remixes in REVIEW).

## Purpose

One screen that tells the coach the truth about the week and sets the next 3 bets.

What good means: every number came from where it says it came from; blanks say why; nothing is borrowed. Buyer signals lead (keyword comments, DMs, calls, people who named a piece before booking); views are diagnostics, and reach is judged over 90 days. Winner and weakest are called by the 2× trailing-10-median rule within each content type, and only once a board exists. The break point is diagnosed only when its trigger is met. At most 3 bets, each tracing to a number. One NEXT line. No hype, no blame.

## Scope

- **Artifact:** the Friday review ("my numbers" / "số liệu tuần này", or the scheduled Numbers-day task): the 5 lines (posted · hands up: keyword comments, DMs, calls · your message: on-map count, keyword said and said back · best post + why · next week's pillar), ≤3 bets and one NEXT line. With a board (L2+), the per-post scoreboard behind it.
- **Output class:** Structured artifact (spec §2.1). Math runs in code on Claude; elsewhere the formula is shown with its numbers and labelled "rough".
- **Not here:** the monthly re-plan (`season-plan.md`); the stats checklist the coach answers (spec §4, strings tier).

## Items

| ID | Item | 0 | 1 | 2 | Critical |
|---|---|---|---|---|---|
| WR1 | Traced [D] | A number with neither a source nor "unverified"; a derived figure that doesn't recompute | Every number sourced, but one derived figure shown off Claude without its formula | Each number cites its source: a Content row's stats, a screenshot, the coach's reply, a date. Derived figures (per-1k rates, medians, ratios) are recomputed in code on Claude, or shown as the formula with its numbers and labelled "rough" elsewhere | yes |
| WR2 | Blank is not zero [D] | A missing stat shown as 0; a skipped review; a silent week counted as zero | Blanks marked, but with no reason; or posts under 48 hours counted | Missing stats read "not supplied (reason)", never 0. Posts younger than 48 hours roll to next week. If over 50% of rows lack stats, the run is Partial and adds a 3-question qualitative review. The review is never skipped | yes |
| WR3 | Right metric | Views lead the review | Buyer signals present but after views, or a rate used on the wrong type | Buyer signals first (keyword comments, DMs and Zalo adds, calls, sales, "how did you find me?" answers). With a board: Entertain = sends per 1k views, Educate = saves per 1k, Convert = leads. Reach judged over 90 days | no |
| WR4 | Honest calls [D] | A "winner" below 2× the trailing-10 median of its type, with under 10 rows of that type, or with no board; a trend from under 3 points; a winner named off Claude with no code | No false call, but "too early to call" or "rough" is missing where it applies | A winner only at ≥2× the trailing-10 median of the same type; under 10 rows of a type → "too early to call"; no trend on under 3 points. With spoken numbers only, "best post" is the coach's pick or the most hands up, labelled as such, never a winner. Off Claude with no code: "rough", no winner named | yes |
| WR5 | Break point gated [D] | A diagnosis before its trigger, or a stricter bar announced | Triggered correctly, but more than one break point, or "not closed" blamed on content | Only after 2 flat weeks and ≥10 posts. One break point. "Not closed" is marked as outside content. The fix changes the next 2 weeks' slots, never the bar | no |
| WR6 | Bets | More than 3, or bets tied to no number | ≤3, but one has no number, or New over 20% or off-map | ≤3 bets (More / Better / New; New ≤20% and on-map), each tracing to a number, filed as Idea rows. The default line: "I'll run these 3 unless you change one" | no |
| WR7 | Edge and system | None of these | Some of these | Keyword said and said back (echo); belief exposures against 3-in-30-days; on-map count and any off-map piece; character and Trustable pieces; proof gaps; BATCH and DROP status; times said vs times likely heard when the coach wants to change the message | no |
| WR8 | Unsoftened, one screen [D] | Hype, praise or blame; a flat week called good; codes, scores or "Edge" in coach text | Honest, but over one phone screen, or more than one NEXT line | The words match the numbers (a flat week is called flat). The 5 lines, ≤3 bets and one NEXT line fit one phone screen, in plain words: simple words with rhythm, nothing unnecessary, one person, "you". Homework is optional and ≤10 minutes | no |
| WR9 | No borrowed numbers | A benchmark, average or another account's number shown as the coach's | A benchmark beside the coach's number without the "typical, not yours" label | No benchmark or average shown as the coach's; any benchmark labelled "typical, not yours"; assumptions labelled. A liked post's counts never enter the coach's numbers | no |

## Build pass rule

- **Shared rule:** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; hard gates clear; no conditional pass; uncertain = 0.
- **Here:** WR1, WR2 and WR4 score 2, and the total is ≥15/18.
- The judge recomputes every derived figure from the persona's stats files and `expected.toml`; review math must match exactly.
- Honesty over targets: "views not supplied; 6 keyword comments, 2 DMs" passes. A week rounded up ("strong week") with flat numbers fails WR8, and a guessed view count fails WR1.
- A remix of a liked post counts as the coach's winner only by the same 2× rule (wf13 §3); "proven" is never said.

## Hard gates

- An invented number: a stat the coach never supplied, or a figure that matches no source (I8).
- Someone else's numbers (a benchmark, a liked post's counts, another coach's result) presented as the coach's own (F1).
- Codes in coach text: no score, "Edge", rubric code or ID outside paste blocks or `why?` (I4).

## Runtime check shipped

`core/format-checks.toml`:

```toml
[format.weekly-review]
checks = [
  "Does every number cite its source (row, screenshot, your reply, date)?",
  "Do missing stats read 'not supplied', never 0?",
  "Is a winner named only at ≥2× the trailing-10 median of its type, else 'too early' (no code: 'rough', no winner)?",
  "Are there ≤3 bets, each tied to a number?",
  "Do the words match the numbers: a flat week called flat?",
]
checks_vn = [
  "Mọi con số đều ghi nguồn (dòng, ảnh chụp, câu trả lời của bạn, ngày)?",
  "Số liệu thiếu ghi 'không có số', không bao giờ ghi 0?",
  "Chỉ gọi bài thắng khi ≥2 lần trung vị 10 bài gần nhất cùng loại, nếu chưa thì 'còn sớm' (không chạy code: 'ước lượng', không gọi bài thắng)?",
  "Tối đa 3 việc cho tuần tới, mỗi việc gắn với một con số?",
  "Lời khớp với số: tuần đứng yên thì nói là đứng yên?",
]
```

## VN note

- Numbers are written 4.210; dates dd/mm. The view is named "Báo cáo".
- Plain Vietnamese, no English outside the loanword allowlist. Buyer-signal labels come from `strings/vn.toml`; "không có số" replaces "not supplied", "còn sớm" replaces "too early".
- Zalo adds and inbox messages count as hands up; keyword comments without diacritics count as the keyword.
- Xưng hô follows the Card. No praise words ("tuyệt vời", "xuất sắc") in machine text (I17).

## Calibration (fictional coaches)

**PASS.** EN, a bookkeeping coach for solo plumbers, Week 3, spoken numbers, no board. "Posted 4 of 5 (the Thursday short rolls to next week). Hands up: 6 FRIDAY SHOEBOX comments, 2 DMs, 1 call (your reply, Fri 16 Oct). Your message: 4 of 4 on the map; keyword said 4 times, said back once. Best post: the receipts short (your pick). Views: not supplied. Next week: Pillar 2." Three bets, each tied to the comments or the call. WR1 2 · WR2 2 · WR3 2 · WR4 2 · WR5 2 · WR6 2 · WR7 1 · WR8 2 · WR9 2 = 17/18. **Result: PASS.**

**FAIL.** VN, a coach for small flower-shop owners (mình–bạn), no board. The review says "Video hoa cưới là bài thắng tuần này, lượt xem tăng 35%". There are 4 rows of that type, no screenshot, and the coach gave no view count. WR4 = 0 (and WR1 = 0). **Result: FAIL** (WR4: "Video hoa cưới là bài thắng tuần này, lượt xem tăng 35%").
