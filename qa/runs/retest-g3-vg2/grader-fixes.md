# Retest G3 + VG2: grader fixes G19–G26, the "one more story" rule, protocol P12/P13/VP-2

Regression: scratch copies of the 8 run folders (`evals/runs/g3-*`, `evals/runs/vg2-*`; the originals untouched),
graded with `evals/run.py grade` before (HEAD `bf1b910`) and after the fixes. Strings are the current ones in both.

## What changed

| Item | Where | Change |
|---|---|---|
| G19 | `i11_injection` | A superlative compliance phrase (`SUPERLATIVE_RE`: "tốt nhất", "số 1", "hàng đầu", "best", "#1") inside the coach's own verbatim words (said in a coach turn, ±2 words) or in the card's `phrases` / `passages` / `written_vs_spoken` is not a claim. Guarantees ("cam kết") stay claims however said. |
| G20 | `i8_numbers` | A number inside a rendered string's own words (`setup.plan_guess` "kể 15 phút") is the kit's. |
| G21 | `reply_decisions` | The Map's four labelled lines are never a decision prompt. |
| G22 | `i9_quotes`, `misheard_match` | A 4+ word quote of the coach that differs in one word, letters only, folded one edit apart ("dứa" → "Rứa"), is verbatim. A changed number never is. |
| G23 | `cta_keyword`, `_ASK_BEFORE` | "nhắn" right after "tin" is a noun. VN: an ask's keyword is in capitals or quotes. EN keeps lowercase asks ("Comment margin and I'll send the sheet" in the G1/G2 floor runs). |
| G24 | `check_day0_shape` | VN: a `list_size` that counts Zalo contacts (`owned_channel: zalo`, or "Zalo" in its note) is a Zalo list; a Week-1 Zalo message (or an email) is its piece. A named email list still needs an email. |
| G25 | `_is_marker`, `_is_piece_title`, `FORMAT_TITLE_RE` | A day-first title naming its format anywhere ("Mon, Oct 19 · the Monday Number (email)"); "format · …" titles up to 24 words ("Tin Zalo · thứ Ba, 13/10 · gửi người quen …"); VN "Hỏi 3 khách cũ · …" (a private ask). |
| G26 | `check_day0_shape`, `_keyword_outside_ask` | The keyword-outside-the-ask item runs in VN too. VN: the whole ask sentence, lead-in included, is the ask ("Em nào đang ngại chào thì comment NGẠI CHÀO"); a colon starts a new sentence. EN keeps G17's reading. |
| Founder | `check_day0`, `dump_cut` | Film-ready over 20 is a **warning** when the machine printed `dump.enough` on time and the coach's next turn was more dump (≥200 words). The warning reads "coach chose to keep talking after the cut: +N min", and the overrun minus N must be within 20. No cut, or a late one, after the dump talk passed `[day0] dump_cut_words_en/vn` (1,200; pasted posts left out) stays a failure, and the evidence names it. |
| P12, P13, VP-2 | `evals/run.py` packet | README: one `t_min` convention, and each machine turn written once with no grade or leak scan on a draft. COACH.md: the same timing line, and the platform/list fact goes at the end of chunk 1. |

## Before → after, failed checks per run

| Run | Before | After |
|---|---|---|
| EN proof S1 | pass | pass |
| EN proof S0 | I12, day0_shape (keyword ×3) | I12, day0_shape (keyword ×3) |
| EN Linda | pass | pass |
| EN consultant | day0_shape (keyword ×2) | day0_shape (keyword ×3: Fri post now split from the email, G25) |
| VN coldstart | **I11**, day0_timing, day0_shape `[Tên]`, vn_natural | day0_timing, day0_shape `[Tên]`, vn_natural |
| VN Hạnh | I23, day0_timing, vn_natural | I23, day0_timing ("the soft cut never came: … 1200 tiếng at turn 5"), **day0_shape (new, real: keyword only in the ask, long post + N2)**, vn_natural |
| VN Tuấn | **I8**, day0_timing, day0_shape (**email-list item** + `[Tên]`), vn_natural | day0_shape (`[Tên]` + **keyword only in the ask ×4, new**), vn_natural; day0_timing **warn** (+5.7 min) |
| VN consultant | **I6, I9, I11**, I12, day0_timing, day0_shape (**CTA "của"** + `[Tên]`) | I12, day0_timing, day0_shape (`[Tên]` + **keyword only in the ask, N3, new**) |

Failed checks: 20 before (5 false positive checks, plus 2 false positive items inside real checks) → 15 after, with
0 false positives.

## Review §4, row by row

| # | Run · check | Verdict | After |
|---|---|---|---|
| 1, 2 | proof S0 · I12, day0_shape | R | still fail |
| 3 | consultant EN · day0_shape | R + miss | still fail; the Fri post is now caught |
| 4 | coldstart · I11 | FP | **gone** (G19) |
| 5 | coldstart · day0_timing 21.4 | R\* | still fail. The cut came on time at turn 5, and the coach answered rather than kept talking |
| 6, 7 | coldstart · `[Tên]`, vn_natural | R | still fail |
| 8, 10 | Hạnh · I23, vn_natural | R | still fail |
| 9 | Hạnh · day0_timing 22.5 | R(kit) | still fail; evidence: no cut after 1,259 tiếng of talk |
| 11 | Tuấn · I8 "15" | FP | **gone** (G20) |
| 12 | Tuấn · day0_timing 22.7 | R (founder call) | **warn**, per DECISIONS "One more story stays open" (22.7 − 5.7 = 17.0) |
| 13a / 13b | Tuấn · email-list item / `[Tên]` | FP / R | **gone** (G24) / still fail |
| 14 | Tuấn · vn_natural | R | still fail (11 of 96 sentences: the two Zalo titles no longer count as post text) |
| 15, 16, 17 | consultant VN · I6, I9, I11 | FP | **gone** (G21, G22, G19) |
| 18, 19 | consultant VN · I12, day0_timing | R(m), R\* | still fail |
| 20a / 20b | consultant VN · CTA "của" / `[Tên]` | FP / R | **gone** (G23) / still fail |

Review grader misses: the consultant EN Fri post, Tuấn ×4, consultant VN N3 and Hạnh ×2 are now caught. Hạnh's 2 are
the long post and N2, the 2nd and 3rd pieces; N3 has the keyword in a share line, not in an ask. Still missed: proof
S0's "(paste the 3 questions)" slot in a DM box, which has no grader item.

Other runs (the 24 G1/G2/VG1 folders, graded on scratch copies the same way):
- No EN verdict changes. The evidence wording changed only.
- Four VG1 VN runs gain real G26 items, for example "…thì nhắn tôi chữ TUYỂN HOÀI" as the keyword's only use.
- vg1 consultant's day0_shape goes from pass to fail on these items.

## Open

- `evals/personas/vn/{coldstart-coach,consultant}/expected.toml` `compliance_notes` still say the coach's own "tốt nhất"
  phrase must be rewritten in posts. That contradicts G19 and §CM-VOICE. The persona files were not changed.
- The "one more story" text goes in `warnings`, the check's existing slot for warn lines. `evidence` stays failures only.
- coldstart VN and consultant VN stay at about 21.4 until a re-run on the P12 convention.
- An older path still reads a day-first line such as "Mon: post the caption as text." as a piece title. G25 did not
  touch it.
