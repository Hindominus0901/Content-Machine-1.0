# Micro check (`micro`)

Build-only rubric (wf12-qa-spec §3.1). Never shipped. It is the G3 judge rubric for pieces too short for Edge and the source of `standard = "micro"` eval cases.
Sources, in order: wf12-qa-spec §0, §2.1, §3.1 (final, wins) · wf12-qa-standards SG "Micro check" (draft) · wf5 §4.8 (reply kit) · wf13 §6 (I19) · DECISIONS (comment keywords).

## Purpose

Keep pieces too short to carry Edge honest and on-system. A 20-word background post can't show a stance, proof and an only-you detail at once, so it isn't Edge-scored; the series it belongs to carries Edge. Freebie-led background posts are never Edge-failed (spec §2.1; PLAN default 5).

## Scope

- **Artifact:** any piece under 40 words EN or 60 tiếng VN: background-text post, story frame, DM line (the M0–M4 reply kit), subject line on its own, on-screen text on its own, DROP hooks.
- **Output class:** Micro (spec §2.1). On Claude, `ship_lint.py` assigns the class by count; elsewhere the model applies the trigger list. At or over the threshold, the piece uses `shared.md` plus its format standard.
- **Not here:** Ideas (hook options in a list, title options, plan rows) use Edge-lite. A subject line or preview inside a full email is scored by `email-zalo.md`.

## Items

Every item is a yes/no check: 2 = yes, 0 = no, there is no 1. All are critical. MC6 and MC7 are N/A when the piece has no keyword CTA or no urgency line.

| ID | Item | 0 | 1 | 2 | Critical |
|---|---|---|---|---|---|
| MC1 | Trace | Fails `shared.md` SG1 | — | Passes SG1 as written there | yes |
| MC2 | Claims | Fails SG2 for a result, testimonial, health or income claim | — | Passes SG2 as written there (AMBER = a record is needed; with no record the claim is left out) | yes |
| MC3 | Polarity | Fails SG3 | — | Passes SG3 as written there | yes |
| MC4 | No hedge in the hook | A hedge from the strip lists (wf6 H1–H9 / V1–V9) in the opening line | — | 0 hedges in the line that opens the piece | yes |
| MC5 | Length [D] | Over the asset's limit, or at/over 40 words EN / 60 tiếng VN | — | Within the asset's limit: background-text post ≤130 characters (aim ≤120), text only, no link (I12); hook or on-screen line ≤12 words EN / ≈18 tiếng VN; on-screen title ≤6 words; any other asset within its dated limit in `platform/targets.toml` | yes |
| MC6 | The keyword delivers | A keyword CTA with no A-row, or an A-row that doesn't exist today (dead link, no M1 reply written) | — | The keyword CTA points at a real A-row that delivers today: the link opens and the M1 first private reply is written. With no A-row, the CTA is follow or save and a lead magnet is proposed instead | yes (N/A: no keyword CTA) |
| MC7 | Urgency from the Ledger | A seat count, deadline, countdown, bonus expiry or "today only" with no Ledger row, or a row without 4 yeses | — | Every urgency line maps to a Ledger row with 4 yeses. A threshold promise ("đủ 100 comment") is logged as a Ledger commitment row, saying what happens if it is reached and if it isn't | yes (N/A: no urgency line) |

## Build pass rule

- **Shared rule:** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; hard gates clear; no conditional pass; uncertain = 0.
- **Here:** every applicable item is yes. Since all items are critical, the total equals the max. There is no Edge score and no Edge FAIL.
- The borrowed-attractor detector does not run on Micro pieces: a freebie or flex as the whole post is allowed at this length.
- A Micro piece written in a series is still judged alone here; the series' Edge sits in its longer pieces.
- Uncertain counts as no: an A-row the judge can't open, a count that can't be redone, a quote that can't be matched.

## Hard gates

- The House Rules hard stops listed in `shared.md` apply unchanged (fake scarcity, invented proof, guarantees, attacks on people, public phone-number asks, and the rest).
- I19 holds for every piece: a Micro piece the machine remixed from a post the coach likes must pass `shared.md` SG-copy (no 6-word EN / 8-tiếng VN run, and so on).
- **Never blocked:** comment keywords, thresholds, "chấm" and coded CTAs are written exactly as the coach asks, with one dated platform note (`platform-notes`). Rewriting or refusing one is a FAIL (I14).

## Runtime check shipped

Ships as the Micro line in SKILL.md and the kit start-block (`core/{en,vn}/ship-check.md`, spec §6), not as `format-checks.toml` lines. Its yes/no content:

| # | EN | VN |
|---|---|---|
| 1 | Under 40 words: is every digit, name and quote in a cited row? | Dưới 60 tiếng: mọi con số, tên, trích dẫn đều có trong dòng đã dẫn? |
| 2 | Is every result backed by a P-row, and every urgency line by a 4-yes Ledger row? | Kết quả có dòng P làm chứng, câu khan hiếm có dòng Ledger đủ 4 "có"? |
| 3 | Does it push on an idea, never on a person or group? | Chỉ nhắm vào ý tưởng, không nhắm vào người hay nhóm người? |
| 4 | No hedge in the first line, and within the asset's length limit? | Câu đầu không rào đón, và nằm trong giới hạn độ dài? |
| 5 | Does the keyword deliver a real asset today? | Từ khoá trao được quà thật ngay hôm nay? |

## VN note

- The threshold is counted in tiếng after NFC; a 45-tiếng post is Micro, a 45-word EN post is not.
- A keyword spelled without diacritics is the same keyword (DANG KY = ĐĂNG KÝ); both forms count for MC6.
- "Hữu duyên" is fine as tone, never as scarcity. Gift or bonus value stays within 50% of the price, and "#QuảngCáo" / "Được tài trợ" is added when someone else promotes the offer.
- One campaign hashtag at most on a background post. DM lines keep the coach's xưng hô and the M1 stop line "Muốn dừng, nhắn DỪNG".
- Coded spellings (c.m, q.t) in anything that may run as an ad get a one-line clear-wording note; it is a note, never a block.

## Calibration (fictional coaches)

**PASS.** VN, a coach for small flower-shop owners (mình–bạn). Background-text post, 15 tiếng: "Tặng file 'Lịch nhập hoa 7 ngày' cho tiệm hoa mới mở. Comment HOA Ế 👇". Freebie-led, so Edge is not scored. MC6: A-row A-01 holds the file, and the M1 reply is written. MC7 N/A (no urgency). The dated platform note is attached. **Result: PASS.**

**FAIL.** EN, a bookkeeping coach for solo plumbers. Story frame, 9 words: "Only 2 spots left this week. Reply FRIDAY SHOEBOX." No Ledger row exists for a weekly cap. MC7 = 0. The machine should have written the CTA with no seat line. **Result: FAIL** (MC7: "Only 2 spots left this week").
