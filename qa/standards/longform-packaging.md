# Long-form packaging standard (`longform-packaging`)

Build-only rubric (wf12-qa-spec §3.1). Never shipped. It is the G3 judge rubric for titles, thumbnail texts and intros of long-form pieces, and the source of `standard = "longform-packaging"` eval cases.
Sources, in order: wf12-qa-spec §2.1 (Idea class), §3.1 (final, wins) · wf12-qa-standards §11 (draft) · arch-final-spec §5.5–§5.6 (3 titles × 3 thumbnail texts; the cut-down) · wf13 §1, §4 (a liked post lends its packaging formula; DISTANCE) · PLAN (packaging library in the founder's words; no Matt Gray framework names).

## Purpose

Get the pillar or cut-down clicked by the right stranger, and keep the promise the click made.

What good means: the title says exactly what the video is, for a stranger, with a true specific (a number, role or timeframe). Thumbnail text is 2–4 words that add to the title and never repeat it. The intro gives Proof, Promise and Plan in the first 30–40 seconds, leading with the strongest (usually proof), then a one-line identity re-intro, an objection remover ("even if…") and an open loop that is paid off at the end.

## Scope

- **Artifact:** the package of a long-form piece (filmed pillar, YouTube video, podcast episode, livestream replay) and of each single-idea cut-down: titles, thumbnail texts and the intro.
- **Output class:** at runtime, title and thumbnail options are Ideas (Edge-lite plus the kill rule); the intro is part of the pillar script (Script, normal or claims). At build the package is judged here as a set.
- **Also applies:** `shared.md` SG1–SG3 to every title, thumbnail and intro line, and SG4 to the intro. A title shaped from a liked post keeps only its formula and must pass SG-copy (no 6-word EN / 8-tiếng VN run from the source title; its numbers and coined terms absent). This file never restates those items.
- **Not here:** the rest of the recording guide (`pillar-guide.md`); hooks of shorts (`native-short.md`).

## Items

Items with no 1 anchor are pass/fail: 2 = clear, 0 = not clear.

| ID | Item | 0 | 1 | 2 | Critical |
|---|---|---|---|---|---|
| LP1 | Clear title | A stranger can't tell what the video is: an inside joke, a coined term alone, a vague promise | Literal, but no true specific; or over the dated length limit | Specific and literal for a stranger, with a true specific (a number, role or timeframe). A pattern from the packaging library (`locales/<lang>/lib/titles.toml`), with a parenthetical payoff where natural. Within the dated length limit in `platform/targets.toml` [D] | yes |
| LP2 | Variants | One title or one thumbnail text | 3 × 3, but two share an angle | 3 titles × 3 thumbnail texts, each with a distinct angle | no |
| LP3 | Thumbnail adds [D] | Shares a content word with its title | No shared word, but over 4 words | 2–4 words that add to the title (a feeling, a stake, a contrast) and share no content word with it | yes |
| LP4 | Proof, Promise, Plan | Two or more missing from the first 40 seconds, or proof that is neither a P-ID nor process / say-do proof | All three present, but past 40 seconds, or not led by the strongest | All three within 40 seconds, led by the strongest (usually proof). The proof is a P-ID or process / say-do proof. The plan names the structure | yes |
| LP5 | Identity line | None | A résumé list, or more than one line | One line: who I am and why you should listen, for a viewer who knows nothing | no |
| LP6 | Objection remover | None | Generic ("anyone can do this") | An "even if…" line that names a real objection the buyers raise | no |
| LP7 | Message match and truth | A number in the title, thumbnail or intro with no P-row; a title the video doesn't pay off in full (bait) | — | Every number in the title, thumbnail or intro traces to a P-row. The video pays off the title's promise in full; no bait the content doesn't deliver. The intro's open loop is paid off at the end | yes |
| LP8 | Cut-down fit (N/A: no cut-down) | A cut-down titled like the full pillar, or carrying two ideas | Right form, but the thumbnail is a sentence, or the pillar's open is reused as its intro | A single-idea cut-down gets a plain "How I'd…" or "Why…" title, a 2–4-word concept thumbnail and a new verbatim intro ≤20 seconds | no |

## Build pass rule

- **Shared rule:** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; hard gates clear; no conditional pass; uncertain = 0.
- **Here:** LP1, LP3, LP4 and LP7 score 2, and the total is ≥13/16 (≥12/14 when LP8 is N/A).
- LP3's shared-word test and LP1's length run in code; the judge never re-argues them. Every title and thumbnail in the 3 × 3 is scored, and each item takes its lowest score.
- LP7 is judged against the transcript when one exists, otherwise against the recording guide's segments and close. A package judged before recording is judged again on the transcript.

## Hard gates

- A number or result in a title or thumbnail with no P-row (invented proof). Income figures appear only with the context block (`shared.md` SG2).
- A superlative (best, #1; VN nhất, duy nhất, số 1) with no survey or award behind it.
- A named person or brand in a title on the default path (`shared.md` SG3). On the coach's explicit request: the dated `liked.compare_note` and a logged Override (F1).
- Matt Gray framework names in any title or thumbnail (lint deny-list, G1).

## Runtime check shipped

`core/format-checks.toml`:

```toml
[format.longform-packaging]
checks = [
  "Would a stranger know exactly what the video is from the title alone?",
  "Is the thumbnail text 2–4 words, sharing no content word with the title?",
  "Does every number in the title, thumbnail or intro trace to a P-row?",
  "Does the intro give proof, promise and plan within 40 seconds?",
  "Does the video pay off what the title promises?",
]
checks_vn = [
  "Người lạ chỉ đọc tiêu đề có biết chính xác video nói gì không?",
  "Chữ trên thumbnail có 2–4 từ, không trùng từ nội dung nào với tiêu đề?",
  "Mọi con số ở tiêu đề, thumbnail hay phần mở đầu đều có dòng P?",
  "Phần mở đầu có bằng chứng, lời hứa, lộ trình trong 40 giây?",
  "Nội dung video có trả đúng điều tiêu đề hứa?",
]
```

## VN note

- Titles use casual VN forms. Thumbnail text is 2–4 words (about 6 tiếng or fewer).
- LP3's shared-word test runs on tiếng after NFC; function words (của, và, là, cho, với, để) are ignored.
- Amounts are written 571 triệu or 571.000.000đ, and only with the context block.
- No nhất, duy nhất or số 1 without a survey or award (Circular 12/2026).

## Calibration (fictional coaches)

**PASS.** EN, a bookkeeping coach for solo plumbers. Cut-down title: "Why I Tell Solo Plumbers to Keep a Shoebox (Not an App)". Thumbnail: "Fridays, not April". Intro (18 seconds): "212 client quarters taught me one thing" (P-02) → "you'll be tax-ready by April" → "three Friday moves" → "even if you hate spreadsheets". LP1 2 · LP2 1 (two titles share the shoebox-vs-app angle) · LP3 2 · LP4 2 · LP5 2 · LP6 1 · LP7 2 · LP8 2 = 14/16. **Result: PASS.**

**FAIL.** VN, a coach for small flower-shop owners (mình–bạn). Title: "Tiệm hoa nhỏ tăng gấp đôi khách quen trong 30 ngày". No P-row holds "gấp đôi" or "30 ngày", and the video is about reminder messages. LP7 = 0. **Result: FAIL** (LP7: "Tiệm hoa nhỏ tăng gấp đôi khách quen trong 30 ngày").
