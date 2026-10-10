# Voice & Language as a first-class pillar: spec (EN + VN)

**Founder, 6 Oct 2026:** "2 cái quan trọng khi làm content: Voice and Languages (how to say), Content Strategy (what to say)."

## 0. Decisions (founder answers, 6 Oct 2026)

| # | Question | Answer |
|---|---|---|
| V1 | Show "your voice" on Day 0? | **One line on the Map screen.** It can be changed inside the same one decision ("change line N"). The Brand Card shows 2 voice lines. No extra turn |
| V2 | What "Languages" means | **Wording and style** (word choice, rhythm, register, dialect, how much English is mixed into VN, platform shifts). Not multilingual output: one language per edition |
| V3 | Getting the coach's *written* voice | **Ask on Day 0.** The dump prompt invites "paste 2–3 posts or messages you've written". It is part of the dump: optional, no extra turn, never a gate |
| V4 | VN: how the coach addresses the AUDIENCE | **Inferred from the dump** (and the pasted posts), shown on the Map, correctable there. It is kept separate from how the machine addresses the coach (asked in reply 1) |

## 1. The two pillars, coach-facing

| Pillar | Founder's words | Coach sees | Built from | Checked by |
|---|---|---|---|---|
| **What to say** | Content Strategy | **"Your Map"** / **"Bản đồ"**: the one message, 3 big ideas, keyword, offer, NOT NOW, this week's big idea | Dump, 7-line check, Quick Listen, research, liked posts, Friday numbers | Ship Check step 0 FOCUS (on the Map, one idea, one belief, not a NOT NOW topic) |
| **How to say it** | Voice & Language | **"Your voice"** / **"Giọng của bạn"**: one line on the Map, two on the Brand Card | Dump (spoken), 2–3 pasted posts (written), Weekly Talk transcripts, "not me:", "I do say", "make it sound like me" | Ship Check VOICE step (below) + the humanize pass |

**The Brand Card's visible part is split under two plain headers:**
- EN: **WHAT YOU SAY** / **HOW YOU SAY IT**.
- VN: **NÓI GÌ** / **NÓI THẾ NÀO**.

The coach still never sees framework names, scores or codes.

## 2. Coach-facing lines

| Where | EN | VN |
|---|---|---|
| Day-0 dump prompt (added clause) | Got posts or messages you've written? Paste 2–3 too, so I learn how you write. | Có bài hay tin nhắn bạn từng viết thì dán 2–3 cái luôn, để mình bắt giọng viết của bạn. |
| Map screen (one line) | YOUR VOICE: {tone, 3 words} · {rhythm} · you say "{phrase}" · you talk to them as "{address}" | GIỌNG CỦA BẠN: {3 chữ} · {nhịp câu} · hay nói "{câu}" · nói với khách là "{xưng hô}" |
| Brand Card visible (2 lines) | HOW YOU SAY IT: {tone} · {rhythm} · "{phrase}", "{phrase}" / to them: "{address}" · never: "{word}" | NÓI THẾ NÀO: {3 chữ} · {nhịp} · "{câu}", "{câu}" / với khách: "{xưng hô}" · không bao giờ: "{chữ}" |
| After "not me:" / "I do say" | Got it: "{line}" is out of your voice from now on. / Got it: you do say "{word}". | Rồi: từ giờ bỏ "{câu}" khỏi giọng của bạn. / Rồi: bạn có nói "{chữ}". |

**Examples of how `{address}` renders:**
- EN: you / "y'all" / "friend".
- VN: "mình – các chị em", "em – anh chị", "tôi – các bạn".
- VN also gives the coach's own pronoun when they speak to the audience.

## 3. The Voice Card (hidden, in the Brand Card machine block)

| Field | What | Source | Cap |
|---|---|---|---|
| `tone` | 3 plain words (e.g. direct · warm · dry) | dump + posts | 40 |
| `rhythm` | sentence style: short / mixed / long; fragments OK?; questions?; lists? | dump (spoken) + posts (written) | 60 |
| `phrases` | 5 verbatim phrases (exists) | dump, Talks | 5 × 60/70 |
| `openers_closers` | ≤3 ways they usually open or close | posts, Talks | 3 × 50 |
| `audience_address` | how they address the audience (VN pronoun pair; EN "you" style) | inferred from dump/posts; shown on the Map | 40 |
| `pronouns` | how the machine addresses the coach (exists, VN) | asked in reply 1 | 30 |
| `dialect` | VN north/central/south + particles they use (nha, nè, á, ạ, nhé…) | dump | 40 |
| `code_mix` | the English words they really mix in (VN) / jargon level (EN) | dump + posts | 60 |
| `humour` | none / dry / playful / self-roast | dump | 20 |
| `written_vs_spoken` | one line on how their writing differs from their talk | posts vs dump | 80 |
| `never_say` / `do_say` | exist ("not me:", "I do say") | coach | exist |

**Platform shifts** are rules, not fields (§CM-VOICE):
- Video scripts follow the spoken voice.
- Posts follow the written voice (or the spoken voice tidied if no posts were pasted).
- LinkedIn is plainer and fewer emoji.
- TikTok/Reels are shorter, with a hook in 3 seconds.
- Email/Zalo is one-to-one ("you" / the audience address in the singular).

**Budgets:**
- The Brand Card whole stays ≤5,700 EN / ≤6,600 VN (the new fields ≈ +300).
- The visible part stays ≤900 by rebalancing the visible field caps (message and NOT NOW names give up characters to the 2 voice lines).

**Trim order:** voice fields are trimmed last after `phrases`. Voice is core.

## 4. Building and refreshing the voice

1. **Day 0:**
   - Extract voice silently from the dump and any pasted posts.
   - Infer `audience_address`.
   - Show the one Map line.
   - Corrections are part of "change line N" (still the one decision).
2. **Every Weekly Talk:** refresh `phrases` / `openers_closers` from the transcript. Keep the newest real phrases; never invent.
3. **"make it sound like me":** rewrite using the Voice Card plus a read-aloud pass. If the coach says what's off, store it as `never_say` / `do_say` and print the one-line confirmation.
4. **Monthly plan:** the Voice line is reprinted with the Map. "Anything that didn't sound like you?" is already tick 3 of the weekly review.
5. **No written samples ever pasted:** posts use the spoken voice, tidied (contractions, rhythm kept, filler removed).

## 5. QA

**Ship Check kit card:** step 4 becomes concrete:

> "VOICE: their tone and rhythm, one of their phrases where natural, their way of addressing the audience, none of their never-words"

The card stays ≤900, so another line is trimmed to fit.

**Graders:**
- **I15** is extended: the VN audience address stays consistent within a piece and across a week, and separate from the coach-machine pair.
- **New I23 voice:**
  - 0 `never_say` hits;
  - pieces of 60+ words use ≥1 coach phrase or opener/closer in ≥50% of a week's pieces (proxy);
  - no banned tells.

**Standards:** `shared.md` SG4 (voice) points to the Voice Card fields. The judge's "sounds like the Card" lens reads `tone` / `rhythm` / `phrases` / `address`.

**Cases:** `voice.{en,vn}.toml`, ≥20 each:
- Map voice line present and plain;
- audience address inferred and shown, and kept separate from the machine–coach pair (VN);
- pasted posts change `rhythm` / `written_vs_spoken`;
- "not me:" / "I do say" persist into later pieces;
- platform shifts;
- no-samples path;
- dialect particles (VN);
- code-mix limits (no English the coach doesn't use);
- the Talk refreshes phrases;
- `never_say` never appears.

**Persona fixtures:** each persona gets `written-posts.md` (2–3 posts or messages they wrote, in their written voice, some with typos and emoji). `expected.toml [voice]` gains `tone`, `rhythm`, `audience_address`, `code_mix`, `written_vs_spoken`.

## 6. Build changes

| Area | Change |
|---|---|
| `schemas/brand-card.toml` | Voice fields above; visible "HOW YOU SAY IT" 2 lines; caps rebalanced (visible ≤900); trim order |
| `core/en/start-block.md` (+ VN) | Dump-prompt clause; Map voice line; Brand Card visible headers; router `§CM-VOICE`. Kit stays ≤6,500 EN / ≤7,500 VN by moving the three setup-check prefixes into one sentence |
| `core/*/ship-check.md` | `ship.kit` step 4 → VOICE line (≤900) |
| `core/method.toml` | New anchor **VOICE** (`voice.kit-*`): building and refreshing the voice, platform shifts, code-mix rules, audience address. HUMANIZE keeps the rewrite pass |
| `modules/en/voice.md` (+ VN) | `voice.kit-*` sections |
| `strings` | `card.visible.what`, `card.visible.how`, `voice.map_line`, `voice.not_me_ok`, `voice.do_say_ok`, `setup.dump_posts`, `anchor.voice` (EN + VN) |
| `evals` | `voice.{en,vn}.toml`; `written-posts.md` fixtures; graders I15 extension + I23; acceptance `[voice]` |
| `qa/standards/shared.md` | SG4 references the Voice Card |
