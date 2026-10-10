# Message Map standard (`message-map`)

Build-only rubric (wf12-qa-spec §3.1). Never shipped. It is the G3 judge rubric for the Message Map and the source of `standard = "message-map"` eval cases.
Sources, in order: wf12-qa-spec §2.1, §3.1 (final, wins) · wf12-qa-standards §2 (draft) · wf11-message-focus §1.6, §2.1–§2.4 (the Map template, the 6 core-message tests, pillars, NOT NOW) · wf7 §4.7, §7.1 (traces into the Brief).

## Purpose

Stop dilution. From everything the coach knows, choose ONE message that every piece maps to: one buyer, one problem in their words, one promise, one named method, one enemy, and the offer it leads to; at most 3 pillars, plus a NOT NOW list.

What good means: a stranger reads it in 60 seconds and can say who it is for, the problem (in buyer words), what changes, how, against what, and what to buy next. The Big Domino sentence and B1–B7 come from research and Bank rows, not from the model's idea of the niche. The coach can say the positioning aloud without notes, and everything they know but aren't saying this Season sits on NOT NOW.

## Scope

- **Artifact:** the Message Map (wf11 §2.1 one-screen template): core message, bio line, WHO, THEIR WORDS, PROMISE, METHOD, OLD WAY, OFFER, KEYWORD line, 3 pillars, NOT NOW. Plus the hidden layer stored in the Brain: Big Domino sentence, B1–B7, Focus Scores, the root-cause chain.
- **Output class:** Structured artifact (spec §2.1). Season 1 v1 onward; re-checked at the quarterly re-map or an offer change.
- **Not here:** the keyword pick itself is scored by `signature-keyword.md`; the pocket version is a view of this Map and is not scored apart.

## Items

| ID | Item | 0 | 1 | 2 | Critical |
|---|---|---|---|---|---|
| MM1 | One buyer | "Anyone", or two buyers in one Map | Role only; or a stage with no moment; or no "not for" line | Role + stage + the moment they find you, with the pains of the stage they're in now; one "not for" line; the dream follower marked `[AI inference]` until the coach ticks it (Map test 3, Narrow) | yes |
| MM2 | Problem in their words [D] | Expert jargon the buyers don't use, or a buyer phrase nobody said | One V-ID, one person, or a paraphrase | The #1 problem is a quoted V-phrase backed by ≥2 V-IDs from ≥2 people (Map test 2, Their words) | yes |
| MM3 | Promise | A guarantee; or an outcome with no backing and no label | No timeframe or condition, or backing unclear | X → Y in Z as a range or with conditions; backed by P-rows or marked Founding / NEEDS PROOF (Map test 6, Claims-safe) | no |
| MM4 | Method and mechanisms | No named method | Method named but steps vague; a mechanism missing; or more than 5 coined terms | A named method with 3–5 steps; a problem mechanism (why what they tried failed) and a solution mechanism; ≤5 coined terms; the core message carries the method or old-way name (Map test 4, Swap) | no |
| MM5 | Enemy | A person, brand, group or KOL; or no enemy | An old way named, but not who it hurts, or no new way | A named old way (belief or practice) → the new way, and who the old way hurts; it passes `shared.md` SG3 | no |
| MM6 | Big Domino and chain | No Big Domino sentence, or beliefs invented | Chain incomplete, untyped, or a belief with no V/O trace | One Big Domino sentence ("If they believe {P2 new belief}, every other objection goes away"). B1–B7 each "Most [buyer] believe __; truth __ because [S/P/V-ID]", each typed vehicle, internal or external; each false belief traces to a V or O row; each has proof planned or is marked NEEDS PROOF | yes |
| MM7 | Focus [D] | More than 3 pillars, a second offer, or no NOT NOW list | Pillars that are topics rather than beliefs; or NOT NOW items with no reason or return trigger | Exactly 3 pillars (a cold start may show 2 plus "proof pillar coming"), each a hill of ≤6 words that passes 3D, with old belief → new belief, tied to an I-ID or a Card hill; NOT NOW holds ≥3 topics, each with a reason code and a return trigger (≤7 shown, the rest archived as X-rows); one offer | yes |
| MM8 | Offer link | No offer, or the price hidden ("giá ib") | Offer named with no price or CTA ladder, or the wrong proof gate | The offer (a Founding pilot or Offer v0 counts) with its price in the edition's currency, the CTA ladder, and the right proof gate (locked when no consented P-row exists); the core message ends at something sold (Map test 5, Money) | no |
| MM9 | Sayable positioning | The core message takes 2+ breaths, or reads as a brochure | Sayable but over the one-breath limit, or a bio line over 12 words | Core message in one breath: ≤35 words EN / ≤50 âm tiết VN (Map test 1). Bio line ≤12 words. A 60-second statement (who you are 5 years ahead of, what people already come to you for, what you are quietly intolerant of) the coach can say without notes | no |
| MM10 | Traceable | Any invented buyer phrase, client, number or result | One element untraced and unlabelled | Every element cites I, V or Bank IDs, or is marked `[AI inference]` or `[guess]` | yes |

**The 6 core-message tests** (wf11 §2.2; the machine rewrites before showing) are scored inside the items above, and a failed test caps its item at 1:
1. One breath → MM9. 2. Their words → MM2. 3. Narrow → MM1. 4. Swap test → MM4. 5. Money → MM8. 6. Claims-safe → MM3.

**NOT NOW reason codes** (wf11 §2.4): DIFF-BUYER · DIFF-PROBLEM · NO-OFFER · TOOL · GENERIC · RISKY · TOO-EARLY. Return triggers: ≥3 buyer mentions in 30 days, the offer changes, a launch needs it, Season N, or never (RISKY).

## Build pass rule

- **Shared rule:** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; hard gates clear; no conditional pass; uncertain = 0.
- **Here:** MM1, MM2, MM6, MM7 and MM10 score 2, and the total is ≥16/20.
- The judge reads the Map and the hidden layer together, and recounts MM2's V-IDs and people at source.
- A cold-start Map with 2 pillars plus "proof pillar coming" can score MM7 = 2; it still needs MM2 from real V-rows (the coach's own clients count, coach recall does not).

## Hard gates

- **Nothing invented** (MM10): an invented buyer phrase, client, number or result fails the Map whatever the total.
- **No guaranteed outcome** in the promise or core message (RED, `shared.md` SG2). VN: no nhất / duy nhất / cam kết.
- **The enemy is never a person, brand or group** (SG3). VN adds politics and the state, regions and family duty.
- **The coach sees one screen, in plain words:** no Big Domino label, B-IDs, Focus Scores, rubric codes or IDs in coach text (I4). A Map that shows them fails.
- **Never a 4th pillar:** character pieces are how a pillar gets said, not a pillar.

## Runtime check shipped

`core/format-checks.toml`:

```toml
[format.message-map]
checks = [
  "Is every field traced to an answer or ID, or marked [guess]?",
  "Are there 3 pillars or fewer, each an old belief → new belief?",
  "Does a NOT NOW list exist, each topic with a reason?",
  "Is there exactly one offer, and does the core message end at it?",
  "Is the core message one breath (≤35 words), with the problem in their words?",
]
checks_vn = [
  "Mọi mục đều dẫn về câu trả lời hoặc ID, hoặc gắn [guess]?",
  "Tối đa 3 trụ, mỗi trụ là niềm tin cũ → niềm tin mới?",
  "Có danh sách ĐỂ SAU, mỗi chủ đề kèm lý do?",
  "Chỉ đúng một offer, và thông điệp chính dẫn tới offer đó?",
  "Thông điệp chính nói trong một hơi (≤50 âm tiết), vấn đề dùng đúng lời của khách?",
]
```

## VN note

- The problem is in the buyer's own register, including any English they really use ("content", "chốt sale") when the V-rows show it.
- Strip calques and buzzwords: nâng tầm, bứt phá, hành trình, chìa khóa, chinh phục.
- Prices are written 1.990.000đ, 1,99tr or 99k, and are public: never "giá ib".
- Xưng hô matches the Voice Card. VN labels follow the wf11 template ([AI], [LỜI CỦA HỌ], [3 TRỤ], [ĐỂ SAU]); IDs stay in English.

## Calibration (fictional coaches)

**PASS.** EN, a bookkeeping coach for solo plumbers. Core message (33 words): "I help solo plumbers in their first 3 years who say 'I'll sort the receipts in April' get tax-ready in 15 minutes a week with the 3-Envelope Method, instead of the year-end dump." WHO names the stage and the moment (the first letter from the tax office). THEIR WORDS: V-04, V-09 (2 people, a forum and DMs). 3 pillars as old → new beliefs; NOT NOW holds 4 topics with codes; one offer, the 3-Envelope Method itself as a 6-week program at a public price; B1–B7 typed and traced. MM1 2 · MM2 2 · MM3 2 · MM4 2 · MM5 2 · MM6 2 · MM7 2 · MM8 2 · MM9 1 (bio line 14 words) · MM10 2 = 19/20. **Result: PASS.**

**FAIL.** VN, a coach for small flower-shop owners. THEIR WORDS reads "khách hàng thiếu trung thành với thương hiệu": no V-row holds it, and no buyer talks like that. MM2 = 0 and MM10 = 1. The total of 16/20 does not matter. **Result: FAIL** (MM2: "khách hàng thiếu trung thành với thương hiệu").
