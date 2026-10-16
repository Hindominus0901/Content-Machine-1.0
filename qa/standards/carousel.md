# Carousel standard (`carousel`)

Build-only rubric (wf12-qa-spec §3.1). Never shipped. It is the G3 judge rubric for carousel copy and the source of `standard = "carousel"` eval cases.
Sources, in order: wf12-qa-spec §3.1 and its dedupe rules (final, wins) · wf12-qa-standards §9 (draft) · wf5 §4.5 (6-slide P2 myths carousel) · DECISIONS (formats; comment keywords).

## Purpose

A top-of-funnel or Credible asset people save and send. The copy is written first; design comes later.

What good means: slide 1 is a big-type hook that is short and specific; slide 2 confirms the payoff; then one rule per slide (rule, why, example), each shareable on its own; a summary slide someone would send to a friend; a last slide whose lead magnet continues the topic. It is worth saving even if nobody comments.

## Scope

- **Format:** carousel copy (Instagram, Facebook, LinkedIn document post, TikTok photo mode): slide text plus caption. The launch myths carousel (P2) is a 6-slide variant.
- **Output class:** Script, normal or Script, claims.
- **Scored on top of `shared.md`,** which must pass first. This file never restates SG items: truth, claims, polarity, hedges, the keyword-once rule and the A-row behind a keyword CTA live there.
- **Not here:** visual design, fonts and image prompts (output is scripts only, DECISIONS).

## Items

| ID | Item | 0 | 1 | 2 | Critical |
|---|---|---|---|---|---|
| CA1 | Slide-1 hook [D length] | Over 10 words, or a vague teaser ("Things you need to know about…") | Within length but generic: no number, outcome or named reader | ≤10 words EN (≈15 tiếng VN) and specific: a number, an outcome or who it's for, in concrete words; the keyword where it fits naturally | yes |
| CA2 | Payoff | Slide 2 changes the subject | Slide 2 restates slide 1 | Slide 2 confirms the payoff slide 1 promised | no |
| CA3 | One rule per slide [D] | A slide mixes rules, depends on the slide before, or repeats another | One rule per slide, but some lack the why or the example, or run over 30 words | ≤30 words per slide (VN ≈40 tiếng); rule / why / example form (the myths carousel: myth / truth / do); each slide stands alone; no slide repeats another | yes |
| CA4 | Summary | None | A recap list nobody would send | A summary slide someone would send to a friend | no |
| CA5 | Last-slide CTA (N/A for a reflection carousel with no CTA) | The lead magnet has nothing to do with this carousel's topic, or the slide asks for two actions | The lead magnet is related but generic ("my free guide") | The lead magnet is the next step after the last rule, so a stranger sees why this carousel leads to it; one action; the keyword is on the slide | yes, when a keyword is used |
| CA6 | Count [D] | Outside the range | — | 10–12 slides (6 for the launch myths carousel) | no |
| CA7 | Caption | Makes a claim the slides don't make | Repeats slide 1 instead of adding context | Adds context and makes no new claim | no |
| CA8 | Worth saving | The value is held back for the DM ("comment to get the rest") | Useful, but thin without the lead magnet | The slides alone teach the rules; worth saving even with no comment | no |

## Build pass rule

- **Shared rule:** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; hard gates clear; no conditional pass; uncertain = 0.
- **Here:** `shared.md` passes; CA1 and CA3 score 2, and CA5 scores 2 when a keyword is used; total ≥13/16, or ≥12/14 when CA5 is N/A.
- CA5 with a CTA but no keyword is scored but not critical.
- Counts (CA1, CA3, CA6) run in code at build. Slides are counted as delivered; a "slide 7b" counts as a slide.

## Hard gates

- Every gate in `shared.md` (SG1, SG2, SG3, SG-copy, SG4, SG7) is scored there and must be clear.
- No format-specific hard stop. A carousel that holds its value hostage to a comment is not blocked; it scores CA8 = 0.

## Runtime check shipped

`core/format-checks.toml`:

```toml
[format.carousel]
checks = [
  "Is slide 1 10 words or fewer, and specific?",
  "Does each slide carry one rule that stands on its own?",
  "Does the last slide's lead magnet continue this topic, with a real asset behind the keyword?",
  "Is it worth saving even if nobody comments?",
]
checks_vn = [
  "Slide 1 khoảng 15 tiếng trở xuống, và cụ thể?",
  "Mỗi slide một quy tắc, tự đứng được một mình?",
  "Quà ở slide cuối nối tiếp đúng chủ đề, và có tài liệu thật đằng sau từ khoá?",
  "Không cần comment vẫn đáng lưu lại?",
]
```

## VN note

- Slide text in short VN lines, ≈40 tiếng or fewer per slide.
- Slide 1: about 15 tiếng. The spec gives 10 words EN only; 15 tiếng applies the 1.5× ratio the spec uses for hooks (12/18) and Micro (40/60). Calibrate on the P2 VN golden runs.
- The last slide shows the keyword and its no-diacritic variant (HOA Ế / HOA E).
- Numbers use dots (1.000); prices are public.

## Calibration (fictional coaches)

**PASS.** EN, a bookkeeping coach for solo plumbers. 11 slides. Slide 1: "5 Friday rules that end April panic for plumbers" (9 words). Slide 2: "15 minutes a week. Here's the order." Slides 3–7: one rule each, as rule / why / example ("Photograph the receipt before the coffee. Ink fades. The Tuesday fuel receipt was blank by April."). Slide 9 summary. Slide 11: "Comment FRIDAY SHOEBOX for the one-page weekly sheet", the next step after rule 5. CA1 2 · CA2 2 · CA3 2 · CA4 1 · CA5 2 · CA6 2 · CA7 2 · CA8 2 = 15/16, with `shared.md` passed. **Result: PASS.**

**FAIL.** VN, a coach for small flower-shop owners. Slide 1: "Những điều bạn cần biết khi kinh doanh tiệm hoa". It is short, but it names no number, outcome or reader stage. CA1 = 1 (critical). **Result: FAIL** (CA1: "Những điều bạn cần biết khi kinh doanh tiệm hoa").
