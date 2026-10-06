# Ad script standard (`ad-script`)

Build-only rubric (wf12-qa-spec §3.1). Never shipped. It is the G3 judge rubric for ads and the source of `standard = "ad-script"` eval cases.
Sources, in order: wf12-qa-spec §2.1, §3.1 (final, wins) · wf12-qa-standards §13 (draft) · arch-final-spec §5.7 (ads: 5 hooks × 2 bodies, talking-head timing) · wf5 §4.10, §6.2–§6.4 (retargeting ad, platform rules, claims, VN law) · DECISIONS + wf13 F1 (comment keywords never blocked; comparison on request).

## Purpose

Amplify proven content to qualified strangers or warm retargeting audiences, behind the proof gate.

What good means: it hooks the pain, not the person, within 0–3 seconds, and reads with the sound off. One idea per ad. Talking head: problem and mechanism → proof → offer → CTA; short VSL: a small CTA at about 65%. Every claim is substantiated; no result numbers, no guarantees, no personal-attribute phrasing. The hook's promise continues on the destination it sends people to.

## Scope

- **Artifact:** ads written on request: talking head (30–60 seconds), short VSL (90–180 seconds), static (headline, primary text, CTA), and retargeting ads (click-to-Messenger or click-to-Zalo, launch P5–P7).
- **Output class:** Script, claims (always).
- **Also applies:** `shared.md` (gates, Edge ≥8 with no 0), never restated here. SG2 already fails every guarantee, cure and unbacked claim; AD6 adds what ads forbid even when it is true.
- **Not here:** the organic post an ad boosts (its own standard); the launch calendar (`launch-assets.md`).

## Items

Items with no 1 anchor are pass/fail: 2 = clear, 0 = not clear.

| ID | Item | 0 | 1 | 2 | Critical |
|---|---|---|---|---|---|
| AD1 | Proof gate [D] | A testimonial, client story or result whose P-row consent doesn't include ads; or a hard offer ad with the gate locked and no founding or process framing | — | proof_gate is open with a P-row whose consented uses include ads, or the ad uses founding or process framing | yes |
| AD2 | Pain, not person | "Are you [attribute]?", a health-condition question, or no pain in the first 3 seconds | Pain named, but only by voice (no on-screen hook), or after 3 seconds | 0–3 seconds name the pain and the key message. On-screen text carries the hook, so it reads with the sound off. No personal-attribute phrasing | yes |
| AD3 | One idea | Several competing claims | One idea plus a second claim slipped into the CTA | One claim per static; one idea per video | no |
| AD4 | Structure and timing [D] | No structure | One section missing or out of order | Talking head: 0–3 / 3–15 / 15–35 / 35–50 / 50–60 seconds (pain → problem + mechanism → proof → offer → CTA). Short VSL: 90–180 seconds, a small CTA at about 65%. Static: headline, primary text, CTA | no |
| AD5 | Copy limits [D] | The lead sits below the visible primary text | Headline over its dated limit | The lead sits inside the first visible primary-text characters; the headline is within the dated limits in `platform/targets.toml` | no |
| AD6 | Ad compliance | Earnings language, or an income or case-study number (even one with a P-row); a before-and-after; a weight or body-change claim; an undisclosed endorser; an unlabelled AI avatar or voice clone; a named competitor on the default path | — | None of these. Endorsers are disclosed. Any AI likeness of the coach is labelled. A named comparison appears only on the coach's explicit request, with the dated `liked.compare_note` and a logged Override (F1) | yes |
| AD7 | Message match | No destination named, or the destination changes the promise | Destination named, but its first screen or message doesn't continue the hook | The destination (DM flow, landing page, Zalo) is named and continues the hook verbatim or near it | yes |
| AD8 | Variation [D] | One version | Variants differ by more than one variable, or are unlabelled | 5 hooks × 2 bodies; variants differ by one variable and are labelled | no |
| AD9 | Retargeting fit (N/A unless retargeting) | Hotter than the organic posts it follows, or buyers not excluded | Milder, but the button isn't "Send message" and no reason is given | Milder than the organic posts; a "Send message" button; a one-line instruction that buyers are excluded | no |

## Build pass rule

- **Shared rule:** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; hard gates clear; no conditional pass; uncertain = 0.
- **Here:** AD1, AD2, AD6 and AD7 score 2, and the total is ≥15/18 (≥13/16 when AD9 is N/A).
- Second read required at build (G5): a fresh reader re-scores every item and re-opens the P-rows' consent fields; the lower score stands.
- AD1 is read against the P-row's `allowed_uses` at source. Consent for posts is not consent for ads.
- Each of the 5 × 2 variants is scored; each item takes its lowest score.

## Hard gates

- Income or health guarantees; cure or treat claims; unsubstantiated income or health claims (House Rules).
- Invented or AI-generated testimonials or reviews; an AI likeness or voice of anyone else.
- Attacks on protected groups or private individuals.
- **Never blocked:** a comment keyword or "chấm" in ad copy, written as asked with one dated platform note (ads with comment CTAs are often rejected); VN coded spellings (c.m, q.t), which get a one-line clear-wording note; a named comparison on the coach's explicit request (F1).

## Runtime check shipped

`core/format-checks.toml`:

```toml
[format.ad-script]
checks = [
  "Is the proof gate open for ads (consent covers ads), or is it founding or process framing?",
  "Do the first 3 seconds name the pain, not the person, and read with the sound off?",
  "Is it free of guarantees, earnings language, income numbers, before-and-after, cure claims and named competitors?",
  "Is the destination named, and does it continue the hook?",
]
checks_vn = [
  "Cổng bằng chứng đã mở cho quảng cáo (khách đồng ý cho dùng trong quảng cáo), hoặc viết dạng founding hay quy trình?",
  "3 giây đầu gọi đúng nỗi đau, không nhắm vào con người, và tắt tiếng vẫn đọc được?",
  "Không cam kết, không nói chuyện thu nhập, không con số kết quả, không trước-sau, không chữa bệnh, không nêu tên đối thủ?",
  "Có nêu nơi khách đến tiếp theo, và nơi đó nối đúng câu hook?",
]
```

## VN note

- Ads must be in clear, correct Vietnamese. Coded spellings (c.m, q.t) and slang get a one-line legal note (the Advertising Law's clear-wording rule; Decree 87/2026 fines). It is a note, never a block.
- Superlatives (nhất, duy nhất, số 1, tốt nhất) need a survey or award (Circular 12/2026).
- "#QuảngCáo", "#QC" or "Được tài trợ" when someone else promotes the offer (Advertising Law as amended by 75/2025, Decree 342/2025).
- Prices use dots (4.990.000đ). The retargeting button is "Gửi tin nhắn"; click-to-Zalo is the other destination.

## Calibration (fictional coaches)

**PASS.** EN, a bookkeeping coach for solo plumbers. Retargeting talking head, 25 seconds, founding framing. 0–3 seconds, on screen and spoken: "April receipts panic? Fix it on Fridays." Body: the Friday rule shown on his own shoebox (process proof), "12 seats, because I review every shoebox" (Ledger L-01). CTA: "Tap Send message and I'll send the cohort schedule"; the DM flow's first message repeats the Friday line. Buyers excluded. AD1 2 · AD2 2 · AD3 2 · AD4 2 · AD5 1 (headline over its limit) · AD6 2 · AD7 2 · AD8 1 (bodies differ in two variables) · AD9 2 = 16/18. **Result: PASS.**

**FAIL.** VN, a coach for small flower-shop owners (mình–bạn). The ad opens: "Bạn là chủ tiệm hoa đang lỗ mà không biết vì sao?". It asserts the reader's financial state (a personal attribute) instead of naming the pain. AD2 = 0. **Result: FAIL** (AD2: "Bạn là chủ tiệm hoa đang lỗ mà không biết vì sao?").
