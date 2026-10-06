# Simple on the outside, rigorous on the inside: spec (EN + VN)

**Founder, 6 Oct 2026:** delivery must be very simple. The coach puts the file into the AI; it sets everything up, researches and deploys right away. Brand Card, scoring and the other artifacts are fine, but coaches won't look at them. They are for the AI to navigate and validate with.

**Principle:** every artifact, score and check stays and keeps running. **The coach-facing surface shrinks to: talk → one short OK → content to post → one next step.**

This spec overrides `wf11-ux-spec.md` §2 and `wf12-qa-spec.md` §2.4 / §2.7 wherever they differ.

## 0. Decisions (founder answers, 6 Oct 2026)

| # | Question | Answer |
|---|---|---|
| S1 | What the coach sees under each piece | **Nothing when it is Ready.** One short line only when the coach is needed: a missing fact ("Needs you · …"), a hard stop, or an override. The WHY line, the checks and the record show only on "why?" |
| S2 | Day-0 confirmations | **Short Map only.** No 7-line check screen. The machine asks only the 1–3 facts it could not hear, one per message. Then a **4-line Map** and "OK?". NOT NOW, "why this one" and the scoring stay internal |
| S3 | Brand Card | **Keep a short visible top:** 3–4 lines (the message, 3 topics, the keyword, the voice line). Then the machine block, labelled "for the machine, no need to read". One-line save instruction |
| S4 | After "OK" | **Today's video, then the whole Week 1 automatically** in the next reply, then the save line. The coach can stop at any time |
| S5 | Research (founder's "it researches") | Silent, during the dump: search where the app can (buyer words, root cause); the coach's own pasted posts and own page link are read to fill gaps instead of asking. Never a question about research on Day 0 |

## 1. Day 0, new shape (≤10 coach turns, film-ready ≤20 min)

> **Amended 6 Oct 2026 (founder, golden round G1 item K2):** step 5 FILM TODAY prints in the same reply as the step 4 Map, under "OK, or change a line." A changed line reprints both; the next coach message brings Week 1 (step 6). See `docs/DECISIONS.md`.

1. **Start.**
   - Setup check line + the 3-line promise + the mic tip.
   - The dump prompt, with two optional extras: "paste 2–3 posts you've written" (wf14) and "or send a link to your page".
2. **Dump.**
   - After chunk 1: the early win (3 lines worth money). Later chunks get "Got it." plus one jogger.
   - Research runs silently.
3. **Missing facts only.** At most 3, one per message, each with a default and "skip". Typically: their exact client words, the best result, the offer.
4. **Map, 4 lines + "OK?":**
   - **Known for:** the one message, in one breath.
   - **3 things you'll talk about:** the 3 big ideas, plain.
   - **Your word:** the keyword.
   - **Your voice:** tone · rhythm · a phrase · how you talk to them (wf14).
   - Then: "We'll run this for 4 weeks. OK, or change a line." This is the one decision.
5. **Film today.** The script only: on-screen text, first line, 3 beats, last line, the caption in a copy box, a CTA with the quiet option. Then one line: "Film it now or post the caption as text."
6. **Week 1 arrives automatically** in the next reply, in its platform mix: 3 shorts, a long post, an email or message, the gift, DM replies, the "ask 3 past clients" message.
7. **Save line + Brand Card.**
   - "Save this so I remember you (30 s): ⋯ → Save to project."
   - The card's visible top is 3–4 lines; below it, the machine block.
8. **NEXT:** "Film today's video. Tomorrow: open Content Machine, newest chat, say 'next'."

## 2. Per-piece output rule (replaces the verdict-under-every-piece rule)

| Piece state | What the coach sees |
|---|---|
| Ready | The content only |
| Ready, downgraded (e.g. founding framing) | The content only. The downgrade shows on "why?" |
| Needs you | One line: "Needs you · {question} (or say 'skip')." At most one per reply |
| Draft, fixable | Nothing. The machine fixes it once, silently. If still not Ready, it becomes "Needs you" |
| Hard stop | One line: "Not writing "{line}": {reason}. …" |
| Override ("post anyway") | One line: "Posted on your call · noted." |
| F1 copy / translate / compare | The one dated note (unchanged) |
| Comment keyword / "chấm" / threshold | The one dated note (unchanged) |

**"why?"** prints, for the last piece:
- the WHY line (old belief → new belief, next step);
- the checks it passed;
- what it was written from.

## 3. QA changes

**Ship Check kit card, PRINT line:**

> "Ready → print only the content. Missing fact → one 'Needs you' line. Hard stop / override → one line. WHY and checks only on 'why?'."

**Invariants:**

| Id | Change |
|---|---|
| **I3 (new wording)** | "At most one coach-facing status line per piece, and only for Needs you / hard stop / override / required notes. A Ready piece prints none." The grader checks that Ready pieces carry no verdict or WHY or ✓ Checked line unless "why?" was asked |
| I4 | Unchanged (no scores or codes; allowed after "why?") |
| I18 | "Ready" text never appears with an open bracket. Moot when Ready prints nothing; kept for "why?" output |

**Acceptance:**
- `[week] why_line_rate` becomes "WHY available on 'why?'": 100% of pieces store one.
- `[day0]`: Map ≤6 turns EN / ≤7 VN; film-ready ≤20 min; session ≤10 turns.
- G6/G8: the "words before anything usable" trigger stays at 300.

**Cases:** every EN/VN case that asserts a visible WHY line, a "✓ Checked" line, a Ready verdict line or the 7-line check screen is rewritten to the new rule. Hidden checks are asserted through "why?" cases instead.

## 4. Build changes

| Area | Change |
|---|---|
| `core/{en,vn}/start-block.md` | Day 0 per §1 (no 7-line screen; missing facts; 4-line Map; Week 1 automatic; save line); per-piece rule; silent research; the coach's own link. Budget kit ≤6,500 / ≤7,500 |
| `core/{en,vn}/ship-check.md` | `ship.kit` PRINT line per §3; `ship.card` and `ship.task` keep the record lines for hub/tasks (L3 writes Quality to the hub; the coach still sees nothing unless needed) |
| `schemas/brand-card.toml` | Visible top = 3–4 lines (message, 3 topics, keyword, voice), ≤500 chars; the rest machine block |
| `modules/*` | `setup.kit-*` (missing facts instead of the check; silent research; own link), `message.kit-*` (4-line Map), `brain.kit-*` (short top), `fmt-short` / `plan` / `talk` / `levelup` / `edge-rubric` (per-piece rule; "why?"; Week 1 automatic) |
| `evals` | Graders I3; acceptance; case rewrite pass (EN + VN) |
| `docs` | DECISIONS, PLAN reconciliation; UX spec §2 and QA spec §2.4 marked superseded by this file |
