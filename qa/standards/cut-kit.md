# Cut kit standard (`cut-kit`)

Build-only rubric (wf12-qa-spec §3.1). Never shipped. It is the G3 judge rubric for the cut kit made from a transcript and the source of `standard = "cut-kit"` eval cases.
Sources, in order: wf12-qa-spec §2.2 (lint: PASSAGE boundaries, ≥70% verbatim), §3.1 (final, wins) · wf12-qa-standards §7 (draft) · arch-final-spec §5.6 (pillar → distribution map) · wf11-ux-spec §3.2 (Weekly Talk output) · wf11 §4 rule 6 (≥60% on the week's pillar) · wf13 F1 (someone else's story is never the coach's).

## Purpose

Turn the pasted transcript into the week's distribution assets, in the coach's own words.

What good means: clips are exact passage ranges ("from '…' to '…'"), 60 seconds or less, with no timecodes or edit notes. Every spoken asset is at least 70% the coach's transcript words; new words appear only in hooks, on-screen text, caption and CTA. The cut takes the strongest belief shift, the keyword reveal and the proof segment, not just the first usable bits. Nothing goes into the coach's mouth that they didn't say.

## Scope

- **Artifact:** the kit cut from the coach's own transcript. From a filmed pillar: clips C1–C3 (C4–C5 on the VA tier), the carousel K, text post T, email E, cut-down D, and the hook pickups used. From the **Weekly Talk** (the Lean default): 3 re-say shorts, 1 long post, 1 email/Zalo.
- **Output class:** each asset is a Script (Micro for on-screen text and story frames under 40 words EN / 60 tiếng VN); the kit as a set is judged here.
- **Not here:** each asset's own quality (its format standard); the Talk week's native or character short, which is not cut from the transcript (`native-short.md`).

## Items

Items with no 1 anchor are pass/fail: 2 = clear, 0 = not clear.

| ID | Item | 0 | 1 | 2 | Critical |
|---|---|---|---|---|---|
| CK1 | Own words [D] | A clip with any written line, or two or more spoken assets under 70% | One non-clip spoken asset under 70%, the rest passing | Clips are 100% verbatim (the PASSAGE is the script). Every other spoken asset, re-say shorts included, is ≥70% transcript words (word overlap after NFC; VN in tiếng). New words only in hooks, on-screen text, caption and CTA | yes |
| CK2 | Exact ranges [D] | A boundary string not found in the transcript, or found out of order | Strings found, but a range runs over 60 seconds, or a timecode or edit note is left in | Both boundary strings found in the transcript, in order; the range runs ≤60 seconds at the word rate; no timecodes or edit notes. A re-say short cites its source PASSAGE the same way | yes |
| CK3 | Standalone | A clip that needs the recording to make sense ("as I said", a dangling "this" or "that") | Makes sense cold but lands two ideas, or C1 lacks the funnel shape | Each clip and re-say short makes sense cold and lands one idea. C1 is funnel-shaped: broad hook → keyword → belief shift → close | yes |
| CK4 | Selection | The first usable bits, in recording order | Two of the three picks right | C1 = the strongest old → new shift. C2 = the keyword or framework reveal, keyword spoken. C3 = a proof or client-decision segment (Trustable from Week 2). The Talk's re-say shorts take the same three moments | no |
| CK5 | Hooks and on-screen text [D] | On-screen text claims something the passage doesn't | Title hook over 6 words, or a verbal hook from neither the pickups nor the transcript | On-screen title hook ≤6 words. The verbal hook comes from H1–H5 or a transcript line. On-screen text makes no claim the passage doesn't make | no |
| CK6 | Derivatives | A derivative makes a point the transcript never made | Traced, but under 60% of the week's assets on its pillar, or the cut-down misses its title form or new intro | Carousel, text post and email are built from transcript segments. ≥60% of the week's assets sit on the week's pillar. The cut-down has one idea, a "How I'd…" / "Why…" title, 2–4-word thumbnail text and a new verbatim intro ≤20 seconds | no |
| CK7 | Truth and consent | A number, result or client detail in no transcript line and no P-row; a client story scheduled without consent for this use | — | Every number, result and client detail is in the transcript or a P-row (a result the coach said aloud still needs its P-row to print: `shared.md` SG2 decides). A client story in a clip has P-row consent for that use; otherwise it is anonymised, tagged [NEEDS consent] and not scheduled | yes |
| CK8 | Coverage [D] | The tier's slots left empty with no Partial mark | Slots filled, but scheduled outside Wednesday–Tuesday, or cut status unset | The volume tier's slots are filled and scheduled Wednesday to the following Tuesday. Cut status set. Nothing set past Scripted | no |
| CK9 | Honest shortfall | Padding: a written line passed off as the coach's, the same passage cut twice as two clips, a slot filled with no usable segment | The shortfall is said, but the run is not marked Partial, or no mini-talk is offered | With fewer than 3 usable segments, the run is marked Partial and the mini-talk (or mini-pillar) is offered. A skipped slot is reported as skipped. Nothing is padded | no |

## Build pass rule

- **Shared rule:** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; hard gates clear; no conditional pass; uncertain = 0.
- **Here:** CK1, CK2, CK3 and CK7 score 2, and the total is ≥15/18. Every asset also passes its own standard: `shared.md` plus its format standard (Edge ≥8, no 0), or `micro.md` under the Micro threshold.
- CK1 and CK2 are counted in code (`shiplint` core / `graders.py`); their output is final and never re-argued. Off Claude the runtime presence check is recorded `lint: manual`.
- Honesty over targets: "2 clips this week, not 3, because only 2 segments stand alone" with Partial marked passes CK9. Three clips with one padded fails it.

## Hard gates

- Words put in the coach's mouth: a line in a clip or re-say short that the coach never said.
- A number, result or client story in no transcript line and no P-row (`shared.md` SG1, SG2).
- A client story scheduled without consent for that use.
- Someone else's transcript (a liked creator's video, a webinar) cut as the coach's own: their story and words are never the coach's (F1). On the coach's explicit request to reuse it, that is a copy (the dated `liked.copy_note`, a logged Override), never a cut kit, and their results and stories still never become the coach's.

## Runtime check shipped

`core/format-checks.toml`:

```toml
[format.cut-kit]
checks = [
  "Are both boundary strings of every passage in the transcript, in order?",
  "Is each clip 100% the coach's words, and every other spoken asset ≥70%?",
  "Does each clip stand alone cold, with no 'as I said' or dangling 'this'?",
  "Is every number in the transcript or a P-row, and every client story consented for this use?",
  "Under 3 usable segments: marked Partial, mini-talk offered, nothing padded?",
]
checks_vn = [
  "Hai câu mốc của mỗi đoạn đều có trong bản ghi, đúng thứ tự?",
  "Mỗi clip là 100% lời của coach, các bài nói khác ≥70%?",
  "Mỗi clip xem riêng vẫn hiểu, không có 'như mình nói lúc nãy' hay chữ 'cái này' lơ lửng?",
  "Mọi con số đều có trong bản ghi hoặc dòng P, mọi chuyện của khách đều được đồng ý cho cách dùng này?",
  "Dưới 3 đoạn dùng được: ghi Partial, gợi ý buổi nói ngắn, không độn thêm?",
]
```

## VN note

- Auto-captions carry diacritic errors. Passage strings must match the transcript exactly as it was pasted.
- Fix only obvious diacritic errors, and only in on-screen text; confirm any unclear word with the coach.
- The 70% is counted in tiếng after NFC normalisation.
- Keep the coach's particles (nhé, nha, ạ) and English mixing; never "clean up" their speech.

## Calibration (fictional coaches)

**PASS.** EN, a bookkeeping coach for solo plumbers, Talk week. 3 re-say shorts at 82%, 76% and 91% own words; each source PASSAGE found in order; the third uses "212 client quarters" (P-02, consent: posts). The long post and email carry the Friday Shoebox lines from segments 2 and 4. CK1 2 · CK2 2 · CK3 2 · CK4 2 · CK5 2 · CK6 1 (55% of the week on its pillar) · CK7 2 · CK8 2 · CK9 2 = 17/18. **Result: PASS.**

**FAIL.** VN, a coach for small flower-shop owners (mình–bạn). Re-say short 2 says "Tháng trước 12 tiệm hoa học viên của mình đều tăng đơn". The transcript says "mấy tiệm hoa học viên của mình", and no P-row holds 12. CK7 = 0. **Result: FAIL** (CK7: "Tháng trước 12 tiệm hoa học viên của mình đều tăng đơn").
