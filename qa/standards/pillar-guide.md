# Pillar recording guide standard (`pillar-guide`)

Build-only rubric (wf12-qa-spec §3.1). Never shipped. It is the G3 judge rubric for the pillar recording guide and the Weekly Talk question set, and the source of `standard = "pillar-guide"` eval cases.
Sources, in order: wf12-qa-spec §3.1 (final, wins) · wf12-qa-standards §6 (draft) · arch-final-spec §5.5–§5.6 (guide template, pillar → distribution map) · wf11 §4 rule 13 (one pillar per recording) · wf11-ux-spec §3.2 (Weekly Talk, mini-talk) · DECISIONS (default pillar = the Weekly Talk; the filmed pillar is opt-in).

## Purpose

Make a 20–40 minute recording easy to do and easy to cut into a week of assets.

What good means: one belief shift plus one Trustable segment. 3 titles and 3 thumbnail texts. A verbatim open of ≤40 seconds: contrarian line → proof → promise with an open loop → plan → objection remover. 4–6 segments, each standing alone, with an old → new claim, a "tell the time when…" prompt tied to a story or proof ID, one how-step and a verbatim CLIP LINE. A mid CTA at about 65%. A close that pays off the loop. 5 hook pickups. All in the coach's delivery mode.

## Scope

- **Artifact:** the pillar recording guide for the opt-in filmed pillar (guided interview, whiteboard/method, live consult, client decision breakdown, "How I'd…"), or for a podcast, livestream or long "chia sẻ" post used as the anchor. Also the **Weekly Talk** question set, the Lean default (5 audio questions, one per message), and its busy-week mini-talk (3 questions, 5 minutes).
- **Output class:** Script, normal (claims when a segment rests on a result or client story). The spoken lines (open, CLIP LINEs, pickups, close) are also scored on `shared.md`, which this file never restates. Titles and thumbnail texts are scored by `longform-packaging.md`.
- **Not here:** the cut kit made from the recording (`cut-kit.md`).

## Items

| ID | Item | 0 | 1 | 2 | Critical |
|---|---|---|---|---|---|
| PG1 | One idea, one belief | Two beliefs or a topic tour; a NOT NOW topic as the main idea | One belief, but no Trustable segment, or one segment drifts to another pillar | One B-ID and one pillar for the whole recording (a topic parked mid-recording becomes an X-row, not a segment). A Credible core plus one Trustable segment | yes |
| PG2 | Clip-ready segments [D] | Under 4 or over 6 segments; segments that need the one before; no CLIP LINEs | 4–6 segments, but one lacks a prompt tied to an S/P-ID or [NEEDS], has a CLIP LINE over 20 words, or repeats the one before | 4–6 segments, each standing alone: claim old → new, a "tell the time when…" prompt tied to an S or P ID or [NEEDS], one how-step, a verbatim CLIP LINE ≤20 words. Each adds something the previous one didn't | yes |
| PG3 | The open [D] | No verbatim open; over 40 seconds; or proof, promise or plan missing | All three within 40 seconds, but the open loop is never closed, or no objection remover | Verbatim, ≤40 seconds at the coach's word rate: contrarian line → Proof → Promise (an open loop) → Plan → objection remover. The loop is paid off in the close | yes |
| PG4 | Packaging attached | No titles or thumbnail texts | Fewer than 3 titles × 3 thumbnail texts, or they fail `longform-packaging.md` | 3 titles × 3 thumbnail texts attached, passing `longform-packaging.md` | no |
| PG5 | Delivery mode | No mode, or modes mixed | Mode set, but questions ask for opinions rather than scenes, or beat cards lack a verbatim hook or final line | Mode A: 10–12 interviewer questions in belief order, each asking for a scene. Mode B: beat cards with a verbatim hook and final line. Mode C: word for word, with pause marks. Weekly Talk: 5 questions, one per message, in belief order for the week's pillar, each a "tell me the time when…" | no |
| PG6 | Hook pickups [D] | None | Fewer than one per planned clip, or two share a stem | H1–H5, one per planned clip, each a different stem, each within the shared hook limit (SG4) | no |
| PG7 | Keyword and CTA [D] | Keyword absent or spoken more than 3 times; no CTA | Mid CTA far from 65%, or the close skips the next domino | Keyword spoken 1–3 times. A one-line mid CTA at about 65%. Close: takeaway → close the loop → next domino → soft keyword CTA | no |
| PG8 | Honest | A prompt that scripts a story, result or number the Bank doesn't hold; a client story without consent for this use; proof the coach doesn't have | Prompts honest, but a missing proof is left blank instead of shown as [NEEDS] | Every story prompt asks for a real time it happened, never a story written for the coach. Numbers only from P-rows. Client stories only with consent for this use. Missing proof shows as [NEEDS] | yes |
| PG9 | Doable | Over 40 minutes or heavy prep, with no fallback | Fits, but no mini version attached | Fits 20–40 minutes with ≤10 minutes of prep; a mini-pillar (3 questions, 10 minutes) attached. Weekly Talk: ≤15 minutes, audio only, one device, with the mini-talk for a busy week | no |

## Build pass rule

- **Shared rule:** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; hard gates clear; no conditional pass; uncertain = 0.
- **Filmed or long-form guide:** PG1, PG2, PG3 and PG8 score 2, and the total is ≥15/18. The spoken lines also clear `shared.md`.
- **Weekly Talk / mini-talk:** PG1, PG5, PG8 and PG9 apply; PG2, PG3, PG4, PG6 and PG7 are N/A (the Talk has no open, segments, titles or pickups; the cut kit builds those from its transcript). Max 8: PG1 and PG8 score 2, and the total is ≥7/8.
- The open is timed at the edition's `word_rate` (`editions/*.toml`); the judge recounts the words, never estimates them.

## Hard gates

- A prompt that writes the coach's story or a client's result for them, or plans a number with no P-row (invented proof).
- A client story planned without consent for that use. It is anonymised and tagged [NEEDS consent], or dropped.
- Codes in coach text: the guide the coach reads carries no B-IDs, rung names or rubric codes outside paste blocks (I4).
- **Never blocked:** a "park that" said mid-recording. It becomes an X-row, and the recording carries on.

## Runtime check shipped

`core/format-checks.toml`:

```toml
[format.pillar-guide]
checks = [
  "Is the open verbatim, ≤40 seconds, with proof, promise and plan, and its loop closed at the end?",
  "Are there 4–6 segments, each with a CLIP LINE and an S/P-ID or [NEEDS]?",
  "Is there a one-line mid CTA at about 65%?",
  "Does every story prompt ask for a real time it happened, with numbers only from P-rows?",
  "Is the mini-pillar (3 questions, 10 minutes) attached?",
]
checks_vn = [
  "Phần mở đầu viết nguyên văn, ≤40 giây, có bằng chứng, lời hứa, lộ trình, và vòng mở được khép ở cuối?",
  "Có 4–6 phần, mỗi phần có câu CLIP và ID S/P hoặc [CẦN BẠN]?",
  "Có 1 câu CTA giữa bài ở khoảng 65%?",
  "Mọi câu gợi chuyện đều hỏi về một lần có thật, con số chỉ lấy từ dòng P?",
  "Đã kèm bản mini (3 câu hỏi, 10 phút)?",
]
```

## VN note

- The anchor may be a livestream or a long "chia sẻ" post; then `text-post.md` also applies to the post.
- Mode A and Weekly Talk ("Buổi nói chuyện tuần") questions use the coach's xưng hô. The series marker is "Phần N".
- The open is timed at the VN word rate (3.5 tiếng a second, PENDING in `editions/vn.toml`); until it is measured, the timing carries a verify flag.

## Calibration (fictional coaches)

**PASS.** EN, a bookkeeping coach for solo plumbers. Opt-in filmed pillar, Mode A, B-3, P2 "Why the shoebox beats the app". Open (34 seconds at his rate): "Your accountant isn't slow. Your shoebox is." → proof "212 client quarters" (P-02) → promise with a loop ("the one receipt that costs you most, at the end") → plan "3 Friday moves" → "even if you hate spreadsheets". 5 segments, each with a CLIP LINE and an S/P-ID; one shows [NEEDS] where no client story exists yet. PG1 2 · PG2 2 · PG3 2 · PG4 2 · PG5 2 · PG6 1 (two pickups share "Most plumbers…") · PG7 2 · PG8 2 · PG9 2 = 17/18. **Result: PASS.**

**FAIL.** VN, a coach for small flower-shop owners (mình–bạn). Segment 3's prompt reads "Kể chuyện chị Thu tăng 40% đơn hoa cưới sau 2 tháng dùng Lịch nhập hoa". No P-row holds 40% or chị Thu. PG8 = 0. **Result: FAIL** (PG8: "Kể chuyện chị Thu tăng 40% đơn hoa cưới sau 2 tháng dùng Lịch nhập hoa").
