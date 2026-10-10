# Retest VG3 + G4: grader fixes G27–G30, the founder's long-dictation rule, protocol P10

Regression: scratch copies of the 5 run folders (`evals/runs/vg3-*`, `evals/runs/g4-*`; the originals untouched),
graded with `evals/run.py grade` before (HEAD `1f78fcc` graders) and after the fixes. Strings are the current ones
(kit fixes `f22d32e`) in both. The kit fixes for the real defects are not in these runs, so those must still fail.

## What changed

| Item | Where | Change |
|---|---|---|
| G27 | `check_day0_shape` "Shorter", `card_parts` (`top_at`), `acceptance.toml [day0]` | The Brand Card's top lines (`card.title` / `card.visible.*` to `card.machine.heading`) are left out of the talk after "Shorter". Cap per edition: `shorter_max_words_vn = 120` (tiếng), else `shorter_max_words` 90. VN evidence says "tiếng". |
| G28 | `i8_numbers`, `PAGE_LABEL_RE` | A page label at a line's start ("Trang 11:", "Slide 11:", "Page 11 ·", "**Trang 12:**") is not a claim. The numbers after it, and "trang 11" mid-line, still are. |
| G29 | `i11_injection`, `I11_CARD_FIELDS` | The card's `not_now` items are left out, like `never_say` / `principles`. The same claim in another field or a piece still fails. |
| G30 | `check_day0_shape`, `film_today_piece` | New item "FILM TODAY carries YOUR WORD outside its ask": the film piece's script plus its caption (the box under "Caption…", an unboxed caption paragraph, or a box opening "Caption:"), read past a blank line before the label. The gift box and the lines under the caption are not read. |
| Founder (6 Oct) | `dump_cut` (`over_threshold`), `check_day0` | Film-ready over 20 is a **warning** when the first cut answered the send that crossed 1,200, and that send's talk past 1,200 (its minutes, pro rata) covers the overrun: "the cut came on time; the coach's send it answered (turn N) ran W past 1200: +M min". It combines with "kept talking" minutes. No cut, a late cut, or minutes the coach's talk does not cover (machine questions, re-asks) stay a failure. Evidence strings are unchanged. |
| P10 | `evals/run.py` COACH.md step 2 | "A chunk over about 400 words (VN tiếng) goes in two sends, split at a paragraph, as the dump prompt asks." "One coach turn each" becomes "one coach turn per send". |

## Before → after, failed checks per run

| Run | Before | After |
|---|---|---|
| EN coldstart (Dan) | pass | pass |
| VN Hạnh | day0_shape (long post), vn_natural; timing warn (+5.4) | day0_shape (long post + **FILM TODAY caption, new: G30**), vn_natural; timing warn (+5.4, unchanged) |
| VN Tuấn | **I11**, day0_shape (FB long post), vn_natural | day0_shape (FB long post), vn_natural |
| VN coldstart | **day0_shape: "Shorter" 170 > 90** | **pass**: 75 tiếng without the card top (cap 120) |
| VN consultant | **I8 "11"**, **day0_timing 20.3**, day0_shape (carousel) | day0_shape (carousel); day0_timing **warn**: turn 5 ran 496 tiếng past 1,200, +4.0 min (20.3 − 4.0 = 16.3) |

Failed checks: 9 before → 5 after. All 5 are real: the keyword only in the ask ×3 (K37/VK-26) and particle density
×2 (VK-27). False positives: 2 → 0. Hạnh's FILM TODAY caption, a review grader miss, is now caught.

## Review §4, row by row

| # | Run · check | Verdict | After |
|---|---|---|---|
| 1, 4, 9 | Hạnh, Tuấn, consultant · day0_shape (keyword only in the ask) | R(kit) | still fail |
| 2, 5 | Hạnh, Tuấn · vn_natural (17%, 15%) | R | still fail |
| 3 | Tuấn · I11 "cam kết" in `not_now` | FP | **gone** (G29) |
| 6 | coldstart · "Shorter" 170 > 90 | R(kit conflict) | **pass** (G27; the kit now says the same, K38/VK-30) |
| 7 | consultant · I8 "Trang 11" | FP | **gone** (G28) |
| 8 | consultant · day0_timing 20.3 | R(pace) | **warn**, per the founder's 6 Oct rule |
| miss | Hạnh · FILM TODAY caption | grader miss | **caught** (G30) |

## Other runs (the 32 G1–G3 / VG1–VG2 folders, scratch copies, graded the same way)

- G30 flags FILM TODAY in 10 older runs: g1 coldstart floor, g1 service-biz S0, g2 proof S0, g3 consultant, vg1
  consultant, vg1 Hạnh S0 and S1, vg1 service-biz, vg2 Hạnh, vg2 Tuấn. In 9 the keyword is only in the ask. In g1
  service-biz S0 it is "nowhere", because YOUR WORD ≠ the CTA there, which is already a failure. I read 4 of them,
  and all 4 are real. Only vg1 Hạnh S1 gains a failing check.
- G27: the g1 and g2 EN coldstart "Shorter" failures (137, 164 words) pass now (75 and 77 without the card top).
  The g2 reply still printed Week 1 and the card together (1,930 words), which "the card on the next message" rules
  out. No grader item checks that.
- Founder rule: vg2 coldstart and vg2 consultant (21.4 each) become warnings (+1.8, +3.6 min past 1,200). vg2
  coldstart also had an avoidable second guess (about 1 min of machine turns). The coach's 1.8 min covers the
  1.4 min overrun, so it reads as a warning.
