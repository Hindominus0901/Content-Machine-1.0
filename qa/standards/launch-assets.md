# Launch assets standard (`launch-assets`)

Build-only rubric (wf12-qa-spec §3.1). Never shipped. It is the G3 judge rubric for a launch's asset set (P0–P9) and the source of `standard = "launch-assets"` eval cases.
Sources, in order: wf12-qa-spec §2.1, §3.1, §4 "Before a launch" (final, wins) · wf12-qa-critique #48–#49 (calendar by construction, math by code) · wf12-qa-standards §14 and reconciliation 6 (draft) · wf12-qa-runtime #45 (launch assets checked as one set) · wf5 §1–§8 · DECISIONS (comment keywords, thresholds and "chấm" are on by default).

## Purpose

Run a launch like a direct-response campaign, mostly organic, that closes on time with trust intact.

What good means: the Scarcity Ledger comes first, and every seat cap, deadline, bonus and price rise in any asset maps to an enforced row. Each asset does its phase's job, P0 to P9; belief-shift posts reuse the chain (vehicle → internal → external). Proof is consented and in context; with no proof, the launch uses founding framing. Keyword CTAs follow the coach, and each keyword delivers something real. The calendar holds, closes on time, and keeps give:ask at ≥3:1 across runway and launch.

## Scope

- **Artifact:** one launch's set (types A–D; 7-, 14- or 21-day calendars): the Launch Brief, the Scarcity Ledger, the launch math, the filled calendar and every asset P0–P9 (background posts, long posts, reels, carousels, story sequences, the live outline, the M0–M5 DM flow, email/Zalo, retargeting ads).
- **Output class:** the Brief, Ledger, math and calendar are structured artifacts (calendars shipped per type; math in code on Claude). Each asset is a Script (claims for P1 with seats, P4 and P5–P8) or Micro (under 40 words EN / 60 tiếng VN).
- **Not here:** each asset's own quality. That is its format standard, never restated here.

## Items

| ID | Item | 0 | 1 | 2 | Critical |
|---|---|---|---|---|---|
| LA1 | Scarcity Ledger [D] | An urgency line with no row, a row without 4 yeses, or a number or date that differs from its row; a countdown with no hard close | Every line maps, but a row lacks its owner, update times or what happens after | The Ledger is filled before any urgency line. Every row has constraint, real reason, number, public update times, what happens after, owner, and 4 yeses (cap enforced; the deadline turns off the link or changes the price; no reopening; numbers updated truthfully). Every urgency line in the set maps to its row with the same number and date; counter updates sit in the calendar at the stated times. A technical failure allows one public, stated extension | yes |
| LA2 | Proof and claims | A result or income number without the context block or consent for this use; a result promise with no condition; testimonials or a case series in a no-proof launch | Numbers carry context and consent, but the set has no variance case | Income or result numbers only with the context block (audience size and years, ad spend, price, buyers, refunds, team), a consent date and allowed use, "individual result, not a promise", and ≥1 variance case. Result promises are conditional ("if 1 h/day") and substantiated. No consented proof: type A founding framing, process proof, no testimonials or case series | yes |
| LA3 | Phase job | Assets that don't match their phase (an offer in P2, a belief post in P7) | One asset misses its phase's job | Each asset does its phase's job (list below) | no |
| LA4 | Keyword CTAs (founder override) [D] | A coach's keyword, threshold or "chấm" CTA rewritten, softened or refused; or a keyword with no A-row and none proposed | Written as asked, but the reply kit, the dated note or a threshold's commitment row is missing | Written exactly as the coach asks, with one dated platform note, and every condition below met. It never scores below 2 for using bait | yes |
| LA5 | Platform mechanics [D] | A link in a background post; a promotional DM outside the 24-hour window; automation planned on a personal profile | A background post over 130 characters | Background posts ≤130 characters (aim ≤120), text only, no link. Private reply: 1 message per comment, within 7 days. Promotional DMs only inside the 24-hour window, so cart-open goes by email or Zalo plus a fresh keyword post. DM automation only on Pages and Instagram professional accounts, else "reply by hand or VA". Each fact dated in `platform-notes` | no |
| LA6 | Consent and capture | A public phone-number ask; messages to people who didn't opt in; a testimonial outside its consented uses | M1 lacks its purpose or its stop word | M1 states purpose, consent and a stop word. Never asks for phone numbers in public comments. Zalo and email only to opt-ins. Testimonials only for consented uses. Buyers are left out of the next "buy now" message | yes |
| LA7 | Calendar integrity [D] | A day of the shipped calendar left empty, or phases out of order | Retargeting not run as a layer P1–P7, or under 6 always-on weeks since the last launch | The shipped calendar for the type is filled day by day, phase order intact. Retargeting runs as a layer P1–P7. Give:ask ≥3:1 over any 8 weeks, runway included. ≥6 always-on weeks since the last launch. No launch in a blocked VN period when the overlay is active | no |
| LA8 | Launch math shown [D] | No math, or a seat goal above capacity | Math shown, but a rate not labelled as an assumption, or the 3× rule ignored | seats = min(goal ÷ price, capacity); warm leads ≈ seats ÷ 2%; if what's needed is over 3 × the warm pool, downgrade the type or add runway. Every rate labelled as an assumption. Code on Claude; elsewhere the formula with its numbers | no |
| LA9 | Trust signals | None | Some missing (no refund terms anywhere in the set) | Who it's not for, refund terms, honest counters, closing on time, keeping and answering critical comments. The live says up front there is an offer at the end. Real seeding only: students with disclosure, the coach's own comments | no |
| LA10 | Set continuity | Two assets give different prices, caps, dates or guarantee terms | Terms match, but the xưng hô or the keyword's spelling shifts between assets | Price, next price, cap, close date and time zone, bonus and its deadline, and guarantee read identically in every asset and match the Launch Brief and Ledger. One xưng hô and one keyword set for the launch | no |

**LA3 phase jobs:** P0 ask a real question · P1 bait plus a real asset · P2 one false belief per asset, in chain order · P3 a quick win they can use · P4 a consented case or proof · P5 the complete offer (`offer-post.md`) · P6 retarget warm people only · P7 Ledger updates only · P8 close on time, plus a waitlist · P9 onboarding, proof capture, downsell, lessons.

**LA4 scores 2 when:** the keyword delivers a real A-row, or one is proposed · the reply kit (M0 public replies, M1 first private reply, M2 capture) is attached · the post has value on its own (Value ≥1) · "personal profile: reply by hand or VA" is noted where it applies · any threshold promise ("đủ 100 comment") is logged as a Ledger commitment row saying what happens if it is reached and if it isn't. wf5's bait-meter "L4 rewrite" rule is superseded by the founder.

## Build pass rule

- **Shared rule:** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; hard gates clear; no conditional pass; uncertain = 0.
- **Here:** LA1, LA2, LA4 and LA6 score 2, and the total is ≥16/20. Every asset also passes its own standard: `shared.md` plus its format (`offer-post.md` for P5, `ad-script.md` for retargeting ads, `email-zalo.md`, `text-post.md`, `carousel.md`, `native-short.md`), or `micro.md` for background posts, story frames and DM lines.
- Second read required at build on the Ledger and on every P5–P8 asset; the lower score stands.
- The calendar and the math are proven by construction and code at G1; the judge scores the fill and re-runs the math from the Launch Brief.
- A downgrade is a pass when it is honest: no proof → founding; no real cap reason → no seat line; no hard close → no countdown, a rolling cohort instead (wf5 §5.2).

## Hard gates

- Fake scarcity: fake counters, resetting timers, routine reopenings, "today only" every day, "first 99" with no enforcement.
- Fabricated or AI-generated testimonials; clone-account seeding; impersonating people or brands.
- Guaranteed income or health outcomes; asking people to post phone numbers publicly.
- **Never blocked:** comment keywords, thresholds ("đủ 100 comment"), "chấm" and coded CTAs, written as asked with one dated note; a real cap or deadline with a 4-yes row (stripping it is a false block).

## Runtime check shipped

`core/format-checks.toml`:

```toml
[format.launch-assets]
checks = [
  "Does this asset do its phase's job?",
  "Does every urgency line map to a 4-yes Ledger row, with the same number and date?",
  "Is the keyword CTA exactly as the coach wrote it, with its A-row, the reply kit and one dated note?",
  "Does every result carry the context block, consent for this use and 'individual result, not a promise'?",
  "Does M1 state purpose, consent and a stop word, with no public phone-number ask?",
]
checks_vn = [
  "Bài này làm đúng việc của giai đoạn launch chưa?",
  "Mọi câu khan hiếm đều khớp dòng Ledger đủ 4 'có', cùng con số và ngày?",
  "CTA từ khoá giữ nguyên như coach viết, có quà thật (dòng A), bộ tin trả lời và 1 ghi chú có ngày?",
  "Mọi kết quả đều kèm bối cảnh, được đồng ý cho cách dùng này, và 'kết quả cá nhân, không phải cam kết'?",
  "Tin M1 nêu mục đích, xin đồng ý, có từ dừng, và không xin số điện thoại công khai?",
]
```

## VN note

- Law 19/2023 Art. 10 treats false scarcity as misleading. Gift or bonus value ≤50% of the price; discounts ≤50%. Affiliates and students who promote add "#QuảngCáo" or "Được tài trợ". No clone seeding (Decree 147/2024).
- Results carry "kết quả cá nhân, không phải cam kết" and "kết quả tùy mỗi người". No "giá ib". "Hữu duyên" is tone, never scarcity.
- One xưng hô per launch. Keyword variants without diacritics are accepted (DANG KY = ĐĂNG KÝ). Full VND amounts with dots. One campaign hashtag. M1's stop line: "Muốn dừng, nhắn DỪNG".
- No launch in tháng cô hồn once the seasonal overlay is active. All of this is PENDING VN counsel; the strict rules apply until sign-off.

## Calibration (fictional coaches)

**PASS.** EN, a bookkeeping coach for solo plumbers, no client proof yet, so type A (founding), 7 days. Ledger: L-01 12 seats (he reviews every shoebox), updated 12:00 and 20:00 ET; L-02 a bonus for the first 5 or until Tue 20 Oct, 11:59pm ET; L-03 close Wed 21 Oct, 11:59pm ET, the link goes off, cohort 2 at $590. P1 background post: "Free, not for sale: the Friday Shoebox sheet. DM SHOEBOX", with M0–M2 and a dated note. P7 frame: "12:00 update: 4 of 12 seats left. Next update 20:00." Process proof only; no testimonials. LA1 2 · LA2 2 · LA3 2 · LA4 2 · LA5 2 · LA6 2 · LA7 2 · LA8 1 (the 2% rate not labelled an assumption) · LA9 2 · LA10 2 = 19/20. **Result: PASS.**

**FAIL.** VN, a coach for small flower-shop owners (mình–bạn). The D12 and D13 story frames both read "Chỉ còn 3 suất cuối cùng!" while Ledger row L-01 shows 9 of 20 seats left. LA1 = 0, and the fake-scarcity hard gate is hit. **Result: FAIL** (LA1: "Chỉ còn 3 suất cuối cùng!").
