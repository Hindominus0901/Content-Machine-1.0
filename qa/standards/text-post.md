# Text post standard (`text-post`)

Build-only rubric (wf12-qa-spec §3.1). Never shipped. It is the G3 judge rubric for long text posts and the source of `standard = "text-post"` eval cases.
Sources, in order: wf12-qa-spec §3.1 and its dedupe rules (final, wins) · wf12-qa-standards §10 (draft) · wf6 §B strip lists (V8) · DECISIONS (formats).

## Purpose

A Likable, character or Credible post that gets read in the feed, not scrolled past.

What good means: line 1 stands alone and the claim lands before "See more" / "Xem thêm". Then a re-hook, a proof or context line, a 3-beat body or the 5-line story (Mirror, Friction, Realization, Shift, Invitation), one bold takeaway, and a CTA that closes the loop the story opened. Prose with rhythm: short paragraphs that flow, not a stack of one-liners. A real scene, date or number from the Bank.

## Scope

- **Format:** long text post: Facebook profile or Page "chia sẻ" post, LinkedIn post, Facebook Group post.
- **Output class:** Script, normal or Script, claims.
- **Scored on top of `shared.md`,** which must pass first. This file never restates SG items: truth, claims, polarity, hook length, hedges, AI tells, the keyword and the CTA rung live there.
- **Not here:** background-text posts and anything under 40 words EN / 60 tiếng VN (`micro.md`); the offer post (`offer-post.md`).

## Items

| ID | Item | 0 | 1 | 2 | Critical |
|---|---|---|---|---|---|
| TP1 | Above the fold [D] | The claim, or the scene that carries it, starts after the fold | It lands by the fold, but line 1 doesn't stand alone | Line 1 stands alone, and the claim (or the scene that carries it) lands within the platform's fold length (`platform/targets.toml`, dated) | yes |
| TP2 | Re-hook | Line 2 restates line 1, or is filler | Line 2 continues but adds no pull | Line 2 re-hooks: it raises a stake, a number or a question the post goes on to answer | no |
| TP3 | Structure | No recognisable flow | The flow is there with one step missing (e.g. no takeaway) | Re-hook → proof or context line → 3-beat body or the 5-line story → one bold takeaway → CTA | no |
| TP4 | Rhythm [D+J] | A stack of one-liners, labelled fragments ("The lesson:"), or padding | Mostly prose, but over 40% single-sentence paragraphs after the hook, or one of the three rules slips | The three rules hold: simple words with rhythm (no stacked fragments); nothing unnecessary; one person, "you". At most 40% of paragraphs after the hook are single sentences. No labelled fragments | yes |
| TP5 | Specifics in the body | No Bank detail beyond the hook | One detail, but generic, or only in the hook | The body carries a real scene, date or number from an S, P, V or C row at the friction or proof beat | no |
| TP6 | The CTA closes the loop | A generic "follow for more", or a CTA unrelated to the story | Tied to the topic but not to the loop the story opened, or two actions | One action that closes the loop the story opened | yes |
| TP7 | Platform fit [D] | A link in the body | More than 3 hashtags (VN: more than one campaign hashtag) | No link in the body: it goes by DM or comment, as the dated platform note says; ≤3 hashtags (VN: one campaign hashtag) | no |
| TP8 | Length [D] | Outside the format's dated default | — | Within the format's dated default in `platform/targets.toml` | no |

**The three inline rules (TP4)** replace every "Part A 6/6" reference (spec §3.1 dedupe):
1. **Simple words with rhythm:** mixed sentence lengths that flow; no stacked fragments.
2. **Nothing unnecessary:** every line earns its place; no wind-up, no restating.
3. **One person, "you":** written to one reader, never "everyone" or "you guys".

## Build pass rule

- **Shared rule:** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; hard gates clear; no conditional pass; uncertain = 0.
- **Here:** `shared.md` passes; TP1, TP4 and TP6 score 2; total ≥13/16.
- TP1 and TP8 read their limits from `platform/targets.toml`; a missing or stale key means the check was "not run", which counts as FAIL at build. The judge never guesses a fold.
- A story's cost or flaw is scored in `shared.md` (Au), not here; the runtime line below still asks for it, because it ships as one footer.

## Hard gates

- Every gate in `shared.md` (SG1, SG2, SG3, SG-copy, SG4, SG7) is scored there and must be clear.
- No format-specific hard stop. A client story needs consent for this use (SG1); a stranger's comment is paraphrased, never screenshotted.

## Runtime check shipped

`core/format-checks.toml`:

```toml
[format.text-post]
checks = [
  "Does the claim land before \"See more\"?",
  "Is it prose with rhythm, not a stack of one-liners?",
  "If it's a story, does it include a cost or a flaw?",
  "Does the CTA close the loop the story opened, with one action?",
]
checks_vn = [
  "Ý chính nằm trước chữ \"Xem thêm\"?",
  "Văn xuôi có nhịp, không phải chuỗi câu một dòng xếp chồng?",
  "Nếu là câu chuyện, có cái giá phải trả hoặc một điểm yếu thật?",
  "CTA khép lại đúng vòng mà câu chuyện đã mở, chỉ một hành động?",
]
```

## VN note

- The register is "chia sẻ thật" (a genuine share). The hook lands before "Xem thêm". The xưng hô stays consistent.
- Emoji are used sparingly, following the Brand Card style.
- TP4 in VN: long Western-style sentences and chains of "mà", "trong đó", "nhằm" break the rhythm (wf6 V8); split them, one idea per sentence. VN AI tells are stripped by SG4 lint (`locales/vn/banned-tells.txt`) and are not re-scored here.
- If the offer is mentioned, the price is public, never "giá ib". One campaign hashtag.

## Calibration (fictional coaches)

**PASS.** EN, a bookkeeping coach for solo plumbers. LinkedIn post. Line 1: "I lost a client over a shoebox." The claim (the Friday rule saves the April panic) lands by line 3, inside the fold. The body is 5 short paragraphs of prose; the friction beat names "41 envelopes on the van dashboard, March 2025" (S-06). Takeaway in bold. CTA: "Comment FRIDAY SHOEBOX and I'll send the sheet I gave him", which closes the lost-client loop. TP1 2 · TP2 1 · TP3 2 · TP4 2 · TP5 2 · TP6 2 · TP7 2 · TP8 2 = 15/16, with `shared.md` passed. **Result: PASS.**

**FAIL.** VN, a coach for small flower-shop owners. Facebook "chia sẻ" post. After the hook, five one-line paragraphs: "Mở tiệm. / Nhập hoa. / Hoa ế. / Bài học: / Đừng nhập theo cảm tính." That is a stack of one-liners and a labelled fragment, so TP4 = 0. The total of 13/16 does not matter. **Result: FAIL** (TP4: "Mở tiệm. / Nhập hoa. / Hoa ế. / Bài học:").
