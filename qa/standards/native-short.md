# Native short script standard (`native-short`)

Build-only rubric (wf12-qa-spec §3.1). Never shipped. It is the G3 judge rubric for native short scripts and the source of `standard = "native-short"` eval cases.
Sources, in order: DECISIONS (lengths in words, never seconds, 7 Oct; short video 500–800 words, kept 11 Oct; ATTRACT / TRUST / CONVERT) · core/en/start-block.md DAY 0 steps 5 and LENGTHS · evals/acceptance.toml [lengths] · wf12-qa-spec §0, §3.1 · wf12-qa-standards §8 (draft) · wf6 §A3 (character formats F1–F14) · wf5 §4.8 (reply kit). Updated 11 Oct 2026 (audit a3 H7): length in words, ATTRACT / TRUST / CONVERT labels.

## Purpose

A short video script of 500–800 spoken words (founder, 7 Oct; kept 11 Oct; lengths are in words, never seconds, because people speak at different speeds): a POV, relatable, "I made it", stance or story piece on ONE idea, in 3–5 beats filmed one a take, ready to film today on a phone.

What good means: three aligned hooks; a lock-in, then beats joined by "but" or "therefore"; a final line, written first, that pays off the hook; one idea and one belief; a caption that carries the piece forward; filmable in one place, and it sounds like the coach when read aloud.

## Scope

- **Format:** native short-form video script (Reels, TikTok, Shorts, Facebook Reels), including character formats F1–F14 when filmed. Output is the script only: spoken lines, on-screen hook text, caption and CTA. No shot lists or editor briefs (DECISIONS).
- **Output class:** Script, normal or Script, claims.
- **Scored on top of `shared.md`,** which must pass first. This file never restates SG items: truth, claims, polarity, hook length, hedges, the keyword and the CTA rung live there.
- **Not here:** clips cut from the pillar (`cut-kit.md`); on-screen text alone (`micro.md`).

## Items

| ID | Item | 0 | 1 | 2 | Critical |
|---|---|---|---|---|---|
| NS1 | Hooks aligned [D lengths] | A hook missing, or the hooks point at different ideas | Aligned, but the verbal hook only names the topic (no loop) | The title hook (on-screen, ≤6 words), the visual hook (one filmable first frame) and the verbal hook (verbatim first line) point at one idea; the verbal hook opens a loop beyond the topic | yes |
| NS2 | Beats | No lock-in; or beats joined by "and then"; or fewer than 3 or more than 5 beats | A lock-in, but beats loosely joined, or the final line not verbatim or not paying off the hook | A verbatim lock-in of one or two spoken sentences; 3–5 beats, one per take, joined by "but" or "therefore"; a verbatim final line, written first, that pays off the hook | no |
| NS3 | Length [D] | The spoken script (first line, beats, last line; not the on-screen text, the first frame, the caption or the ask) is outside 500–800 words ±10% (VN: tiếng); or the piece states a length in seconds | — | 500–800 spoken words, within ±10% (acceptance [lengths] short_words_min / _max, tolerance); no length in seconds anywhere | no |
| NS4 | Buyer Filter (ATTRACT pieces and character or entertainment pieces only; otherwise N/A) | Generic humour, or a moment anyone has lived | A moment from the buyer's world that meets 1 of the 3 tests | A moment from the buyer's world (an R-ID) that meets ≥2 of 3: the ideal client would send it to a peer; you need the problem to get the joke; it names the next domino | yes, where it applies |
| NS5 | Delivery mode | No delivery mode, or one that overrides the mode the coach chose | A mode set but incomplete (e.g. beat cards without the verbatim hook and final line) | Mode B by default: beat cards with a verbatim hook and final line. Mode A: 4–6 off-camera questions, each with what the answer should hit. Mode C: word for word with pause marks, the default for compliance-sensitive pieces | no |
| NS6 | Caption | No caption, or a caption that makes a claim the video doesn't | A caption that repeats the hook instead of extending it | Line 1 continues the hook, line 2 extends it, line 3 is the send prompt or the CTA. A keyword CTA carries the M0/M1/M2 reply kit | no |
| NS7 | Film-ready | Needs props, edits, a second person or a change of place; or a shot list instead of a script | One dependency (a prop, or a cut that carries meaning) | One location, a phone, no props or editing dependencies | no |

## Build pass rule

- **Shared rule:** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; hard gates clear; no conditional pass; uncertain = 0.
- **Here:** `shared.md` passes; NS1 scores 2 (and NS4, where it applies); total ≥12/14, or ≥10/12 when NS4 is N/A.
- NS4 applies only to pieces typed ATTRACT and to character or entertainment pieces; it is never N/A on those. (The old trust-rung labels Admirable, Likable, Credible, Trustable are deny-listed in coach text; the types are ATTRACT, TRUST, CONVERT.)
- NS3 counts words, never seconds: 500–800 spoken words ±10%, EN words, VN tiếng (what a word counter shows). The count runs in code (evals/graders.py `lengths`, acceptance [lengths]); a length in seconds on a title or in talk fails there (`seconds_budget_fails`).

## Hard gates

- Every gate in `shared.md` (SG1, SG2, SG3, SG-copy, SG4, SG7) is scored there and must be clear.
- No format-specific hard stop. An AI avatar or voice clone of the coach needs the platform's AI label and a caption note; anyone else's likeness or voice is a House Rules hard stop.

## Runtime check shipped

`core/format-checks.toml`:

```toml
[format.native-short]
checks = [
  "Do all 3 hooks (on-screen, first frame, first line) point at one idea?",
  "Does the final line pay off the hook?",
  "Is it one beat per take, joined by \"but\" or \"therefore\", never \"and then\"?",
  "Can it be filmed in one place on a phone, with no props or edits?",
]
checks_vn = [
  "3 hook (chữ trên màn hình, khung hình đầu, câu đầu) cùng chỉ về một ý?",
  "Câu chốt trả lời đúng điều hook đã mở?",
  "Mỗi lần quay một ý, nối bằng \"nhưng\" hoặc \"nên\", không dùng \"rồi thì\"?",
  "Quay được ở một chỗ bằng điện thoại, không cần đạo cụ hay dựng phim?",
]
```

## VN note

- The verbal hook is ≈18 tiếng (SG4 counts it); the on-screen title is short VN, even when the coach mixes in English.
- Localised moment hooks ("con nhà người ta", Tết questions, the boss messaging at 11pm, "Ai từng ___ sẽ hiểu") come only from the R-bank.
- Native VN formats: TikTok góc nhìn, hỏi nhanh đáp gọn, sự thật về nghề, một ngày làm. Series marker: "Phần N".
- Beats join with "nhưng" / "nên", never "rồi thì". Particles and the coach's dialect stay.
- NS3: VN counts tiếng, 500–800 like EN (no word rate, no seconds; the old provisional `word_rate` reading is retired, 11 Oct 2026).

## Calibration (fictional coaches)

**PASS.** EN, a bookkeeping coach for solo plumbers. TRUST, 620 spoken words in 4 beats. On-screen: "Receipts aren't April's job." First frame: a shoebox on a van seat. First line: "I watched a plumber lose a weekend to a shoebox of receipts." (a receipt frame, one spoken sentence). Beats: the April dump, *but* 15 minutes on Friday, *therefore* a boring April, *but* the one receipt that still goes missing. Final line: "Fifteen minutes on Friday. April gets boring." Caption line 1 continues the hook. NS4 N/A (TRUST). NS1 2 · NS2 2 · NS3 2 · NS5 2 · NS6 1 (line 3 missing) · NS7 2 = 11/12, with `shared.md` passed. **Result: PASS.**

**FAIL (length).** The same script cut to "35 seconds" (about 90 words, 2 beats). NS3 = 0 (outside 500–800 words, and a length in seconds), NS2 = 0 (2 beats). **Result: FAIL** (NS3: "35 seconds").

**FAIL.** VN, a coach for small flower-shop owners. ATTRACT piece. Its "buyer moment" is "Ai đi làm cũng từng mệt vào sáng thứ Hai 😅". Anyone has lived it, no flower-shop owner would send it to a peer, and you don't need the problem to get it. NS4 = 0 (critical where it applies). **Result: FAIL** (NS4: "Ai đi làm cũng từng mệt vào sáng thứ Hai").
