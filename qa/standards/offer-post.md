# Offer post standard (`offer-post`)

Build-only rubric (wf12-qa-spec §3.1, new; from the agency's C4). Never shipped. It is the G3 judge rubric for direct-response offer posts and client decision breakdowns, and the source of `standard = "offer-post"` eval cases.
Sources, in order: wf12-qa-spec §2.1 (claims class), §3.1 (final, wins) · agency copy quality page, Part C row C4 ("the offer is unmistakable") · arch-final-spec §5.7 (offer post, client decision breakdown) · wf5 §4.3(b), §5.2, §6.1, §6.3 (offer skeleton, downgrades, Ledger, claims) · wf11 §2.2 test 6 (claims-safe; VN no cam kết) · DECISIONS (F1; comment keywords).

## Purpose

Make one clear, complete offer that a buyer can say yes or no to after one read, without being misled.

What good means: after one read the buyer knows what they get, what it costs, what they risk, how to leave, and the one next step. It says who it is for and who it is not for. The guarantee covers the process. Every cap, deadline and bonus is real and sits in the Ledger. Proof appears only within its consent; with no consented proof, it is a founding offer.

## Scope

- **Artifact:** the direct-response offer post (Trustable; the W4 slot; the launch P5 pinned post). Skeleton: headline (offer + cohort + cap) → promise with conditions → who it's for → 3 steps tied to deliverables → what's inside → price + real next price or date → real bonus + cap reason → why N seats → not for you if → process guarantee → one CTA. Also the **client decision breakdown**: each decision A → B → result → typical-results line, ending at the offer.
- **Output class:** Script, claims (a price is always present; spec §2.1).
- **Also applies:** `shared.md` (gates, Edge ≥8 with no 0), never restated here, and the carrier's own standard (`text-post.md`, `carousel.md`, `email-zalo.md`, or `micro.md` for a background post). In a launch the post is also a P5 asset under `launch-assets.md`.
- **Line with SG2:** SG2 decides whether a single claim may print. OP4 and OP5 decide whether this post may make a hard offer at all, and in which framing.

## Items

All five items are critical, so a 1 anywhere fails the post.

| ID | Item | 0 | 1 | 2 | Critical |
|---|---|---|---|---|---|
| OP1 | Offer unmistakable (C4) | Two or more of the five missing (what you get, price, risk, how to leave, next step), or the price hidden ("DM for price", "giá ib") | One of the five missing or vague ("flexible support"), or more than one next step | After one read the buyer knows what they get (name, deliverables, format, length, start), what it costs (a public price in the edition's currency, and the payment plan if any), what they risk, how to leave (refund window, cancel, stop line) and the one next step. The promise is an outcome with conditions. Decision breakdown: every decision A → B → result → typical-results line, then the offer | yes |
| OP2 | Not-for line | None | Generic ("not for people who aren't serious") | ≥1 specific "not for you if…" line naming a real situation the offer doesn't serve (time, stage or expectation), from the Launch Brief's `who_not_for` or the Map's not-for line | yes |
| OP3 | Process guarantee only | An outcome guarantee ("results or your money back", "cam kết tăng doanh thu"), or a guarantee the Brief doesn't hold | A process guarantee with a term missing (what the buyer must do, the window, or what they get back) | The risk reversal is a process guarantee with all its terms (do X for Y; not a fit → Z back), taken from the Brief's guarantee field, and it says it covers the process, not the result. No guarantee at all is fine when the risk line says so plainly | yes |
| OP4 | Urgency only from the Ledger (N/A: no urgency line) | A cap, deadline, bonus expiry or next price with no 4-yes Ledger row, or different from it | Matches its row, but the cap's real reason or the time zone is missing | Every cap, deadline, bonus expiry and next price reads exactly as its 4-yes Ledger row (number, date, time zone, what turns off), and the cap's real reason is in the post ("why N seats"). A real cap is written plainly, never stripped | yes |
| OP5 | Proof gate | A hard offer with testimonials, results or a case while proof_gate is locked; proof used outside its consented uses | Founding framing used, but never explained ("founding" with no cohort, price or co-creation line) | Gate open: proof only from P-rows whose consent covers this use, with context and the individual-result line. Gate locked: founding framing ("cohort 1, founding price, you help shape it") or process proof, and no testimonial, "students achieved" line or case | yes |

**AMBER = a record is needed:** a result claim with no P-row is left out and the post is written as a founding or process offer. It becomes a Draft only when the post is about that result (for example, a decision breakdown with no consented client).

## Build pass rule

- **Shared rule:** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; hard gates clear; no conditional pass; uncertain = 0.
- **Here:** all five items are critical, so a pass is every applicable item at 2: 10/10, or 8/8 when OP4 is N/A. The spec's "≥8/10" is the shared 0.8 rule, met by construction.
- The judge reads OP4 against the Ledger rows and OP5 against the P-rows' consent fields at source, never against the post's own wording.
- An honest founding offer with no proof can score 10/10. Edge Authority is then capped and the ceiling is named in the verdict (`shared.md`).

## Hard gates

- Fake scarcity: a cap with no real reason, a counter that never moves, a "last chance" with no hard close, a routine reopening.
- An outcome guarantee on income, health or results; a cure or treat claim.
- An invented testimonial, or one used outside its consented uses.
- **Never blocked:** a real cap or deadline with a 4-yes row (stripping or softening it is a false block); the coach's comment keyword, threshold or "chấm" as the next step, written as asked with one dated note; a named comparison on the coach's explicit request, with the dated `liked.compare_note` and a logged Override (F1).

## Runtime check shipped

`core/format-checks.toml`:

```toml
[format.offer-post]
checks = [
  "After one read, does the buyer know what they get, the price, the risk, how to leave and the one next step?",
  "Is there a specific not-for line?",
  "Does the guarantee cover the process only, with its terms, and never an outcome?",
  "Is every cap, deadline, bonus and next price exactly as its 4-yes Ledger row?",
  "Proof gate locked: founding or process framing, with no testimonial or result line?",
]
checks_vn = [
  "Đọc một lần, khách biết rõ nhận được gì, giá bao nhiêu, rủi ro gì, rút lui thế nào và bước tiếp theo duy nhất?",
  "Có một câu 'không dành cho bạn nếu…' cụ thể?",
  "Cam kết chỉ cho quy trình, ghi rõ điều kiện, không bao giờ cam kết kết quả?",
  "Mọi số suất, hạn chót, quà và giá sau đều đúng như dòng Ledger đủ 4 'có'?",
  "Chưa mở cổng bằng chứng: viết dạng founding hoặc quy trình, không feedback, không kết quả?",
]
```

## VN note

- The price is public and written with dots (1.990.000đ, 1,99tr or 99k), never "giá ib".
- "Cam kết" covers only the process ("Mình cam kết quy trình, không cam kết doanh thu thay bạn"); never "cam kết hiệu quả" or "cam kết không phát sinh".
- No nhất, duy nhất or số 1 without a survey or award (Circular 12/2026). Gift or bonus value ≤50% of the price; discounts ≤50%.
- "#QuảngCáo" / "Được tài trợ" when someone else promotes the offer. Results carry "kết quả cá nhân, không phải cam kết".
- "Không dành cho bạn nếu…" is the not-for form. "Hữu duyên" is tone, never scarcity. One xưng hô, one campaign hashtag.

## Calibration (fictional coaches)

**PASS.** EN, a bookkeeping coach for solo plumbers, founding offer (proof gate locked). "FRIDAY SHOEBOX, cohort 1 (12 seats): tax-ready books by April, if you give it 15 minutes every Friday. 6 weekly calls, the shoebox sheet, one review of your books. Founding price $490 (cohort 2 will be $590), and you help shape the program. Why 12: I review every member's shoebox myself. Not for you if you invoice twice a year or want me to do your books. Guarantee: do the first 2 Fridays; not a fit, full refund. I guarantee the process, not your tax bill. Closes Wed 21 Oct, 11:59pm ET. DM SHOEBOX for the link." Cap, price rise and close match Ledger rows L-01 to L-03. OP1–OP5 all 2 = 10/10. **Result: PASS.**

**FAIL.** VN, a coach for small flower-shop owners (mình–bạn). The guarantee line reads "Cam kết tiệm bạn tăng 30% khách quay lại sau 60 ngày, không thì hoàn tiền 100%". That is an outcome guarantee (also RED under `shared.md` SG2). OP3 = 0. **Result: FAIL** (OP3: "Cam kết tiệm bạn tăng 30% khách quay lại sau 60 ngày, không thì hoàn tiền 100%").
