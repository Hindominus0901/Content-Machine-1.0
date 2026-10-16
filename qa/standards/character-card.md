# Character Card standard (`character-card`)

Build-only rubric (wf12-qa-spec §3.1). Never shipped. It is the G3 judge rubric for the Character Card and the source of `standard = "character-card"` eval cases.
Sources, in order: wf12-qa-spec §2.6, §3.1, §6 (final, wins) · wf12-qa-standards §3 (draft) · wf6 §A2 (Card template and field rules), §A4 (polarity guide, 3D test, VN calibration) · wf11 §2.3 (cold-start pillars) · `schemas/brand-card.toml` (compact character fields).

## Purpose

Turn the coach's character into a usable, polarizing anchor. Edge Au and C (`shared.md` SG5) are scored against it, so a weak Card caps every script.

What good means: it reads like the coach talking, not a brand sheet. ONE extreme trait, shown as a scene, plus who it repels. Principles in the form "always/never … because …"; values that each have a real cost story. The enemy is a named old way; 3 hills pass the 3D test; the hard limits are intact; the voice phrases are verbatim. It is a living document, refreshed every 90 days.

## Scope

- **Artifact:** the Character Card (wf6 A2 one-page Card), the compact Card generated from it (≤150 words), and the character and voice fields of the Brand Card at Day 0 (`trait`, `enemy`, `principles`, `phrases`, `pronouns`, `never_say`, `do_say`).
- **Versions:** Day-0 v0 (from the brain-dump) and the full Card (after the deep-character talks). Each refresh is re-scored.
- **Output class:** Structured artifact (spec §2.1).

## Items

| ID | Item | 0 | 1 | 2 | Critical |
|---|---|---|---|---|---|
| CC1 | One extreme trait | None; a list of adjectives; or a trait the coach never showed | One trait, but given as an adjective, or with no "repels" line | Exactly one. Its 10/10 version is a scene from the coach's answers, not an adjective. Says who it repels. Matches the Buyer Mirror when one exists | yes |
| CC2 | Principles [D form] | None, or platitudes | Fewer than 3, or "because" missing | 3–5, each "I always/never X because Y", each heard in an answer (Day-0 Brand Card holds up to 3) | no |
| CC3 | Values with cost | Values with no story at all | Some values marked `[UNPROVEN]` (no real story or cost) | 3 values, each with a real story and a real cost (money, a client, time) | no |
| CC4 | Enemy | A person, brand, competitor, KOL or group; or no enemy | A practice, but unnamed, or with no one it hurts | A named old way (a practice or system) → the new way, and who the old way hurts | yes |
| CC5 | Stances | No contrarian truth; a hill that fails 3D; heat above 3; anything from the red zone | Hills that are generic (AI contrarian, no Card anchor), or one hill that can't be demonstrated | A contrarian truth plus 3 hills (a cold start may show 2 plus "proof hill coming", wf11 §2.3). Each passes 3D: a sensible peer could Disagree, the coach can Defend it in 2 sentences and Demonstrate it with Card proof or a story. Heat ≤3 | yes |
| CC6 | Vision and tribe | None | A vision without the client's future identity, or no tribe line | Names the client's future identity, plus a "People like us …" line | no |
| CC7 | Texture | None | Fewer than 3 items, no contradiction pair, or "where I look bad" without a cost | 3–5 tastes, quirks or rituals, each with the value behind it; one contradiction pair; ≥2 "where I look bad" entries, each with its cost | no |
| CC8 | Voice [D] | Phrases AI-polished, or not in the coach's answers | Fewer than 5 verbatim phrases, or no words-used / words-banned | 5 phrases found verbatim in the coach's answers or samples; words used and words banned, including the personal banned list (`never_say`) and allowlist (`do_say`); VN: the xưng hô pair is set | yes |
| CC9 | Hard limits [D] | A default red-list entry removed | Red list present, but limits the coach named are missing | The default red list is present (wf6 A4 red zone); the coach may add to it, never remove from it; hard stops never sit on the allowlist | no |
| CC10 | Honest and current | Any invented trait, story, cost or phrase; a quiet truth placed in public content | A field neither traced nor marked `[GAP]`; or the refresh date has passed | Every field cites an answer or Bank ID, or is marked `[GAP]` / `[UNPROVEN]`. Quiet truths are flagged `[QT]` and never auto-published. Refresh date within 90 days. Compact Card ≤150 words [D] | yes |

**3D test (CC5):** Disagree (a sensible peer could) · Defend (in 2 sentences) · Demonstrate (Card proof or a story). A stance that fails any D is dropped, not softened.

## Build pass rule

- **Shared rule:** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; hard gates clear; no conditional pass; uncertain = 0.
- **Full Card:** CC1, CC4, CC5, CC8 and CC10 score 2, and the total is ≥16/20.
- **Day-0 v0** (a recorded lower bar, spec §3.1): the same five critical items score 2, and the total is ≥14/20. `[GAP]` or `[UNPROVEN]` is allowed in CC3, CC6 and CC7 (each scores 1).
- Gaps become optional homework, reminded in the weekly loop, never extra setup probes: the draft's "≤2 probes per gap" is removed (spec §6).
- The judge checks every verbatim phrase against `answers.md` / `voice-samples.md` at source; a phrase that is close but not exact scores CC8 = 0.

## Hard gates

- **Never invent** a trait, story, cost or phrase. A missing field is `[GAP]`, never filled. The machine improves a Card only by asking, in context.
- **The enemy and every hill target an idea, practice or system,** never a person, brand, KOL or group (`shared.md` SG3).
- **The red list never shrinks.** A coach's "I do say …" can never allowlist a hard stop or a polarity limit.
- **`[QT]` quiet truths are never auto-published.**
- **Privacy:** no client names, handles or phone numbers in the Card; clients appear by role or a C-ID.

## Runtime check shipped

`core/format-checks.toml`:

```toml
[format.character-card]
checks = [
  "Is every field traced to the coach's answer or a Bank ID, or marked [GAP]?",
  "Is the compact Card 150 words or fewer?",
  "Is nothing invented: no trait, story, cost or phrase the coach didn't say?",
  "Are gaps offered as optional homework, with no extra setup questions?",
  "Is the enemy a practice or old way, never a person or group?",
]
checks_vn = [
  "Mọi mục đều dẫn về câu trả lời của coach hoặc ID, hoặc gắn [GAP]?",
  "Bản Card rút gọn không quá 150 từ?",
  "Không bịa gì: không có nét tính cách, câu chuyện, cái giá hay câu nói nào coach chưa nói?",
  "Chỗ còn thiếu chỉ là bài tập tuỳ chọn, không hỏi thêm lúc cài đặt?",
  "Kẻ thù là một cách làm hay lối cũ, không phải một người hay một nhóm người?",
]
```

## VN note

- The xưng hô pair is chosen once: mình–bạn by default, tôi–anh chị for B2B. "tôi–các bạn" can read as lecturing.
- "Nhận trước, đứng vững sau": admit your own mistake first, then hold the stance firmly. Face test: would you say it to an anh/chị đi trước?
- Heat goes one notch lower for B2B and older audiences; the wording stays definitive.
- The red list adds politics and the state, regions (Bắc/Nam) and family-duty framing. Attack "cách làm" or "lối cũ", never "người".
- Income reads as "khoe" easily, so a flipped-paycheck entry uses a range or no number.
- The 150-word compact cap is a whitespace count, so in VN it is 150 tiếng. Dialect (north, central, south) is set in `dialect`.

## Calibration (fictional coaches)

**PASS.** EN, a bookkeeping coach for solo plumbers, full Card. Trait: "over-labels everything"; 10/10 scene: "colour-coded 41 receipt envelopes on a van dashboard" (answer Q7); repels "shoebox-in-April people". Enemy: "the year-end dump" → "the 3-Envelope Method"; hurts first-year plumbers who overpay their accountant. 3 hills pass 3D. 5 verbatim phrases from the samples; `never_say` holds "crush your numbers". CC1 2 · CC2 2 · CC3 1 (one value `[UNPROVEN]`) · CC4 2 · CC5 2 · CC6 2 · CC7 1 · CC8 2 · CC9 2 · CC10 2 = 18/20. **Result: PASS.**

**FAIL.** VN, a coach for small flower-shop owners, Day-0 v0. Enemy: "mấy shop hoa online phá giá" ("those online flower shops that undercut prices"). That targets a group of businesses, not a practice; the repair is "đua giá" (racing on price) as the old way. CC4 = 0, and the total of 15/20 does not matter. **Result: FAIL** (CC4: "mấy shop hoa online phá giá").
