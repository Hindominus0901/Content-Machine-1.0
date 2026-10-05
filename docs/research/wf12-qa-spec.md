# Content Machine 1.0: QA system spec (final)

This spec merges drafts A (runtime and checklists), B (standards and house rules) and C (build QA), applying the critique. The rule throughout: **heavy rigor at build time, light and mechanical checks at runtime, and the coach sees one line per piece.** I checked it against the plan (#1 PRIORITY, the QA section), arch-final-spec §3.3, §5.7, §5.9 and §8, wf6 §B, wf7 §7 and the agency doctrine, run contract, copy quality page and house rules. No files were written.

## 0. Numbers settled here (lint and graders need one value each)

| Item | Settled value | What it replaces |
|---|---|---|
| Runtime "Ready" bar | All gates pass, Edge ≥8/10, no pillar at 0, format checks all yes, 0 open brackets. Stance formats also need C = 2 | arch §8.1/§8.2 "ship ≥7" (wf6 and the plan say ≥8) |
| Release judge bar | Per persona and edition, median of 3 runs: Edge average ≥8, no piece below 7, no pillar at 0 | Unchanged |
| Runtime rounds | 2 rounds: round 1 is the draft, round 2 is one fix aimed only at named defects. Then the coach decides. This is the run contract's own definition (§7). It is how I read the plan's "≤2 fix rounds", and the founder should confirm it | A had 2 fix rounds; wf6 had 2 passes |
| Questions to the coach | At most 1 per reply | A: ≤1 per piece and ≤3 per batch; arch §8.1: ≤2 [NEEDS] |
| Word-count tolerance | word_rate × seconds ±15% | NS3 said ±10% |
| Public quote cap | ≤15 words EN, ≤25 tiếng VN | arch §8.5 said 15 for both |
| AMBER | Means "this claim needs a record". P-row fields clear it. With no record, downgrade quietly. It becomes a Draft only when the piece is about that result | "AMBER ships with Needs:" (arch §8.1/§8.4, B SG2, House Rule 5) |
| Coach line | One line, ≤20 words. No score, no "Edge", no rubric codes | arch §5.7/§8.1 technical footer |
| Ship Check card | ≤900 characters EN, ≤1,000 VN (always loaded). Task variant ≤800 EN / ≤1,000 VN | about 900 |
| Micro threshold | Pieces under 40 words EN or 60 tiếng VN get the Micro check, not Edge | none |

---

## 1. QA principles (the founder's style)

1. **There is one question.** Would this embarrass the coach, or cost a buyer's trust, if it were posted as it is? Every other check serves that question.
2. **Nothing invented.** A missing fact becomes a visible `[NEEDS: one question]` (VN `[CẦN BẠN: …]`), never a guess. A coach with no results uses what they do have and never borrows someone else's. Blank is not zero, and unknown is not a guess.
3. **Cheapest first.** Deterministic checks come first, then the rubric, then the lenses, then the human. Judgment is never spent on a piece that failed a lint. A count the model guessed is never called "deterministic": counts run in code or at build, and everywhere else they are writing targets.
4. **Never claim a check that didn't run.** "Not run" is not "clean". Anything the machine cannot see becomes one coach tick, and every tick asks only about something the machine cannot see.
5. **Uncertain means fail.** At build, uncertain is a FAIL. At runtime, uncertain means cut the line or downgrade the piece. The machine asks only when the whole piece rests on the missing fact.
6. **No conditional pass and no praise.** Internally the first line is `Result: PASS` or `Result: FAIL`. The coach sees "Ready" or "Needs you", never "Ready after…". The machine's own text never uses praise words.
7. **Honesty over targets.** Three honest shorts beat five padded ones. A shortfall reported as a shortfall passes. A shortfall dressed up fails, and that covers a stretched label, a rounded-up count, "most" where the data says "some", and a cut-off quote.
8. **The reviewer is never the writer.** In a chat, the checker is labelled `same-context` and trusted only as far as build calibration proves. Real independence lives at build: a fresh judge, 3× blind generative tests, and a second read on every pass where the lower score stands.
9. **Two rounds, then the boss.** At runtime that means draft plus one fix, then the coach decides. At build it means two rounds, then the founder. The boss can override anything except a hard stop. The verdict stays attached to the work and is not raised again.
10. **Rigor at build, quiet at runtime.** The coach never fills in a template and never sees a score or a rubric code. They get one line per piece and at most one question per reply. When the machine turns out to be wrong, the rubric gets fixed, not the verdict defended.

---

## 2. Runtime QA (layer 1)

### 2.1 Output classes (assigned mechanically, never by judgment)

| Class | What triggers it | QA that runs |
|---|---|---|
| **Idea** | DROP idea, hook options, title options, plan rows, capture questions | Edge-lite ≥4/5 plus the kill rule. A failing idea is dropped silently |
| **Micro** | Under 40 words EN or 60 tiếng VN: background-text post, story frame, DM line, subject line, on-screen text, DROP hooks | Micro check: trace, claims, polarity, no hedge in the hook, length, the keyword delivers a real A-row, urgency comes from the Ledger. No Edge score; the series carries Edge. This settles B's founder decision (A): freebie-led background posts are never Edge-failed |
| **Script, normal** | Every other script | The full loop (§2.2) |
| **Script, claims** | Any of these: a digit next to a result, money or time word (clients, %, $, đ, triệu, tr, k, days, weeks, ×); a client story, quote or testimonial; a price; an urgency word (left, only, last, closes, deadline, today only, còn, chỉ còn, suất, hạn chót, đóng); health, body or income outcome words; nhất / duy nhất / số 1. Also any of these formats: offer post, client decision breakdown, ad, sales email, DM flow with a price, launch P1 with seats, P4, P5–P8 | The full loop, plus a mark on every claim, the before-posting ticks (§4), and eligibility for the flag-only second read on Claude Pro |
| **Structured artifact** | Brand Brain, Character Card, Message Map, keyword pick, Season plan, Research Brief, weekly review, launch plan | Required fields present, each traced to an answer or ID or tagged `[guess]` / `[GAP]`. Plans are correct by construction (shipped grids). Math runs in code on Claude; elsewhere the formula is shown with its numbers. The Research Brief runs wf7's self-check gates G1–G13 as written |

On Claude, `ship_lint.py` assigns the class. Everywhere else the model applies the trigger list, which is a presence check it can do reliably.

### 2.2 The loop (one Ship Check per batch)

**Step 0. PREFLIGHT (silent, per piece).**
- Check the slot row: rung, B-ID, a pillar from the Message Map that is not on the not-now list, the CTA for the rung, the keyword and the format.
- Check that the Bank holds material for this angle. If it doesn't, switch to the angle the Bank can prove (material-first drafting).
- Claims class also needs:
  - the proof gate;
  - a P-row with Substantiated = Y and Consent covering this use;
  - a Ledger row with 4 yeses for any urgency;
  - an A-row for every keyword CTA;
  - consent for any client story;
  - the transcript, for a cut.
- The outcome is one of three:
  - **GO.**
  - **DOWNGRADE** (the default; written in `guardrails.md`):

    | What's missing | What the machine writes instead |
    |---|---|
    | Consented proof | Founding framing or a process story; the Authority ceiling is named internally |
    | Ledger row | No seat line, no countdown |
    | Income context block | A process story |
    | Client consent | The coach's own side of the story, with no identifying client detail |
    | A-row | A follow or save CTA, plus a proposed lead magnet |
    | Transcript | The mini-pillar |
    | Voice samples | Generic mode (Au and C capped at 1) |

  - **NEEDS YOU**, only when the piece itself is the missing fact (for example, "write my testimonial post" with no testimonial).

**Step 1. WRITE.** Write from Bank IDs only. The writing rules (humanize, format template, calibration ladder) carry most of the quality. Hard stops are refused while writing, so a hard-stop line is never printed.

**Step 2. LINT.**
- **Claude:** `scripts/ship_lint.py` runs once per batch over the drafts and the cited rows fetched in one Notion query. It checks:
  - lengths, sentence averages and maximums, VN syllables;
  - word_rate ±15%;
  - PASSAGE boundaries and ≥70% verbatim;
  - every digit, name and quote found in a cited row, and every ID resolving;
  - the banned and hedge lists;
  - the keyword appearing exactly once;
  - the hook stem against the last 10;
  - leftover brackets;
  - the class.

  Its output is final and is never re-argued.
- **If the script can't run** (or on ChatGPT and Gemini): the model does presence checks only. These are: digit, name or quote in a cited row; the quote matches; a claim word maps to a P-row field; an urgency word maps to the Ledger; the keyword is present; the hook stem is not in `recent_hook_stems`; no hedge or tell in the hook; no brackets left. Counts are not claimed as checked, and the record says `lint: manual`.

**Step 3. CHECK** (after all drafts, never interleaved with writing; label `checker: same-context`).
- Re-read the card and the cited Bank rows.
- Score Edge K V A Au C (0–2 each).
- Gates: G1 polarity, G2 truth, G3 voice.
- The format checks, 3–5 yes/no items from the module's "CHECK BEFORE ANSWERING" footer (§3).
- Three lenses, each fail-only: 5-second phone read, sounds like the Card, would the buyer believe it.
  - Compliance is covered by the claims lint.
  - Message Map fit is fixed by the slot row in Step 0.
  - The DM/call lens lives in the launch reply kit.

**Step 4. FIX (round 2).** Fix only the named defects, in one shared order: truth and claims, then format criticals, then Edge (C, A, K, V, Au), then re-lint the whole piece.
- A score of ≤5, a polarity fail or a borrowed-attractor-only hook means re-ideate: take the next idea silently, once.

**Step 5. VERDICT.**
- **Ready:** everything in the §0 bar. A recorded ceiling (for example, Authority capped while the proof gate is locked) is named in the record and never waived.
- **Draft:** everything else.

**Step 6. RECORD.**
- **Claude:** the Quality properties go into the same upsert as the script, so there are 0 extra hub calls. The full record is written only for Draft or Override.
- **Sheets:** the same four columns go in the paste block.

**Step 7. PRINT.** One verdict line directly under each piece, and one NEXT line per reply. **A piece with no line under it was not checked.** START-HERE says so, and on Claude the Runs row is set to Partial.

**Per path:**
- **Claude connected:** draft all → lint script → check → fix once → upsert with Quality → print. If the usage cap hits mid-batch, every unwritten piece stays unwritten, the run is Partial, and "finish batch" resumes it.
- **ChatGPT / Gemini standalone:** a fixed piece is never reprinted.
  - When the model reasons, it checks and fixes before printing.
  - Otherwise the post-check only sets Ready or Draft. A Draft with no missing fact says `say "fix N2"`, which is an optional one-word reply.
- **Scheduled tasks:** use the task card. They never ask questions; the run report's NEXT line carries the one question.

### 2.3 The Ship Check card (always loaded)

EN measures **896 characters** after NFC. Rendered into SKILL.md, the ChatGPT instructions and the Claude task:

```
SHIP CHECK · silent · once per batch · unsure → cut or downgrade · no praise
0 PRE: slot row + Bank material? Else DOWNGRADE (process story, founding, no seat line); ask only if the piece rests on the missing fact
1 WRITE from Bank IDs; refuse hard stops
2 LINT (Claude: scripts/ship_lint.py, final): digits/names/quotes in cited rows · quotes exact · result claim = P-row Substantiated+consent · urgency from Ledger · keyword ×1 · new hook stem · no hedge in hook · 0 [NEEDS]
3 CHECK after all drafts, cited rows reread. Gates: polarity, truth, voice. Edge 0–2: K keyword+specific · V one idea, one belief · A proof shown · Au only-you detail · C a stance. Format checks. Unsure = fail: 5-sec phone, sounds like Card, buyer believes it
4 FIX named defects once. Ready = gates, Edge ≥8, no 0, format yes
PRINT under each: Ready to <verb> · I'd post it: <Bank fact> | Needs you: <1 question/reply>
```

**VN note.**
- The card stays in English: method prose is EN, and every rendered file carries the output contract.
- The VN edition appends one line through an `editions/vn.toml` param, for a total of **997 characters (≤1,000)**:

  `VN: one xưng hô pair · no EN outside allowlist · results carry "kết quả cá nhân, không phải cam kết"`
- The `PRINT` strings come from `strings/vn.toml`.
- These VN items live in `locales/vn/compliance.md`: the gift cap of 50% of the price, #QuảngCáo, superlatives, and the capture consent line.

**Task variant** (`automation/task-standalone.tmpl`): **721 characters EN**, about 822 VN with the VN line. It is within the ≤800 / ≤1,000 sub-budget.

```
SHIP CHECK (task) · silent · unsure → cut or downgrade · never guess or praise
1 Write only from Brief IDs; refuse fake scarcity, invented proof, guarantees, attacks on people
2 Every digit/name/quote sits in a cited Brief row; quotes exact; result claim only from a P-row marked Substantiated+consent, else the process story; urgency only from the Ledger
3 Keyword once · hook stem not in recent_hook_stems · no hedge in hook · Edge none at 0: keyword+specific, one idea, proof shown, only-you detail, a stance
4 Missing fact → [NEEDS: one question] and the piece is a Draft. Never ask in a task; the run report carries 1 question
PRINT under each: Ready to <verb> · I'd post it: <Brief fact> | Draft · needs: <question>
```

### 2.4 The one-line verdict (the coach sees nothing else)

- **Verbs:** film / post / send (VN: quay / đăng / gửi).
- **Evidence:** must name a Bank item (a keyword, scene, client or P-row), never an adjective.
- **Length:** ≤20 words.
- **Pronouns:** VN xưng hô follows the Card; the default is mình–bạn.

| State | EN | VN |
|---|---|---|
| Ready | `Ready to film · I'd post it: it uses your "<K>" and Lan's cancellation call.` | `Sẵn sàng quay · Mình sẽ đăng: có "<K>" và đúng cuộc gọi huỷ lịch của chị Lan.` |
| Ready, downgraded | `Ready to post · written as a founding offer (no client results yet).` | `Sẵn sàng đăng · viết dạng mời khách đầu tiên (chưa có kết quả khách).` |
| Needs you | `Needs you · What did she say, word for word? I won't make it up. (Or say "skip".)` | `Cần bạn · Hôm đó chị ấy nói nguyên văn câu gì? Mình không tự bịa phần này. (Hoặc nhắn "bỏ qua".)` |
| Draft (queued) | `Draft · waiting on one fact from you; I'll ask next.` | `Bản nháp · còn thiếu 1 thông tin, mình sẽ hỏi sau.` |
| Draft (fixable) | `Draft · the stance is soft. Say "fix N2" and I'll sharpen it.` | `Bản nháp · quan điểm còn mềm. Nhắn "sửa N2", mình làm sắc lại.` |
| Hard stop | `Not writing "3 seats left": there's no real cap yet. Give me the real number and I'll write it.` | `Câu "chỉ còn 3 suất" mình không viết: chưa có giới hạn thật. Bạn cho con số thật, mình viết ngay.` |
| Override | `Posted on your call · my concern: no clear stance · logged.` | `Đăng theo quyết định của bạn · mình lưu ý: chưa có quan điểm rõ · đã ghi lại.` |
| Second-read flag (Claude Pro) | `Heads-up on N2: one number doesn't match your proof. Say "fix N2" before posting.` | `Lưu ý N2: một con số chưa khớp với bằng chứng của bạn. Nhắn "sửa N2" trước khi đăng.` |

The command `why?` (VN `tại sao?`) prints the internal record for any piece. That is the only way QA detail ever reaches chat.

### 2.5 Round limits and "Needs you" handoffs

- **Round 1** is the draft and check. **Round 2** is one fix aimed only at named defects: automatic on Claude, or on standalone it is the reasoning step, the coach's answer, or "fix N2".
- A **round 3** happens only when the coach says "try again" (VN "làm lại").
- **"Post anyway"** (VN "cứ đăng") records an Override on everything except hard stops. It is logged once and never raised again.
- **At most one question per reply.** It goes to the Draft that blocks the soonest slot. The other Drafts keep their Needs and come up one at a time through the NEXT line or "What's next?".
- **The question's form:**
  - one fact, answerable in one line or a voice note;
  - names who can supply it (you, your client, your VA);
  - always offers the downgrade ("or say 'skip' and I'll write it as a process story").
- **The coach's answer** is filed first as an ID'd Bank row. Then only that piece re-runs, as round 2.
- **Unattended runs** never ask a question. Their Drafts carry Needs, and the run report's NEXT line carries one question.
- **Silence never zeroes a week.** DROP proposes the downgraded version.

### 2.6 What gets recorded

- **Content → Quality** (replaces Edge · Claims · Uses · Needs):
  - Result: Ready, Draft, Override or Pending;
  - Edge: 0–10, internal;
  - Uses: IDs;
  - Needs: text.
- **The full record** is written only on Draft or Override, in a "QA" toggle in the page body (Sheets: a Notes cell). Its first line is `Result: PASS/FAIL`, then the Edge pillars, the gates, failed format items, lens fails, the ceiling, `checker: same-context`, and `lint: script|manual`.
- **P-rows** gain a "Re-check by" field (default 90 days, or when the offer changes). A Claims view filters on it.
- **Character Card** gains a personal banned list and a personal allowlist.

### 2.7 Budget (free tiers)

- **Card:** about 230 tokens, always loaded.
- **Per piece:** ≤20 printed words.
- **Exception records only.**
- **Lint:** one script call per batch.
- **Hub:** 0 extra calls (Quality goes in the same upsert); stays within the ≤30 calls per run.
- **ChatGPT:** QA costs **0 extra messages**.
- **Second read:** Claude Pro only, flag-only, run inside DROP. At most 1 claims piece per run. Skipped when a catch-up runs. It never touches the body, so the state rule "never overwrite a Scripted body" stands unchanged.
- **Required runtime second reads:** none.

### 2.8 Feedback without labelling chores

- **Two commands:**
  - `not me: <line>` (VN `không giống mình: <câu>`) adds the line to the banned list.
  - `I do say <word>` (VN `mình có nói <từ>`) adds it to the allowlist. Hard stops and polarity limits can never be allowlisted.
- **Launch debrief asks one question:** "Did the link close, or the price rise, when you said?" A "no" blocks urgency lines in the next launch until the coach states an enforcement plan.
- **Monthly re-plan:**
  - a format at ≤0.5× its median for 4 weeks is offered for retirement, and the coach decides;
  - a keyword with 0 echo after 90 days is offered for retirement, and the coach decides;
  - a P-row retires when consent or the offer changes, or when its re-check date passes without confirmation.
- **Opt-in "send feedback"** (VN "gửi góp ý"): an anonymised paste the coach emails to the founder. It lands in `qa/inbox/` and becomes labelled eval cases. This is the only bridge from the human sample to build evals.
- **Cut from runtime:**
  - automatic edit diffing;
  - the four-way outcome labels;
  - hook-stem performance retirement;
  - capture-question rotation;
  - per-pillar score-vs-performance analysis in REVIEW;
  - the diagnostic's "temporary stricter bar" (the diagnostic changes the next 2 weeks' slots instead).

---

## 3. Standards (layer 4)

### 3.1 Standards files

- **Build-only rubrics** live in `qa/standards/<id>.md` and are never shipped. They are the G3 judge rubric and the source of the eval cases.
- **Runtime** ships only the right-hand column, as 3–5 yes/no lines in the matching module's generated "CHECK BEFORE ANSWERING" footer, from `core/format-checks.toml`. No scores, no totals, no per-standard fix orders.
- **Shared pass rule (build):**
  - every critical item scores 2;
  - the total is ≥ ceil(0.8 × max), with N/A items removed from the max;
  - all hard gates are clear;
  - there is no conditional pass;
  - uncertain = 0.

| File (`qa/standards/`) | Artifact | Critical items (must score 2 at build) | Build pass | Runtime check shipped (yes/no) |
|---|---|---|---|---|
| `shared.md` (SG + Edge v2) | Every script | SG1 trace, SG2 claims (AMBER = a record is needed), SG3 polarity: all hard gates. SG5 Edge (stance formats C = 2). SG6 ladder. SG4 voice and SG7 variation are code-checked | Gates clear, Edge ≥8, no 0 | The Ship Check card |
| `micro.md` | Under 40 words EN / 60 tiếng VN | Trace, claims, polarity, no hedge in the hook, length, the keyword delivers a real A-row, urgency from the Ledger | All yes | The Micro line in SKILL.md |
| `research-brief.md` | Research Brief | RB1 right people, RB3 depth, RB4 roots, RB8 swap test, RB9 honesty | ≥16/20, second read at build. Starter brief: RB1 and RB9 at 2, ≥14/20, Week 1 only | wf7 gates G1–G13. 3 links for the coach to re-open, asked inside the sign-off message, never as a separate step. Where the machine browsed, it re-fetches the quoted pages and drops misses itself |
| `message-map.md` | Message Map | MM1 one buyer, MM2 problem in their words, MM6 Big Domino and chain, MM7 focus, MM10 traceable | ≥16/20 | Every field traced or `[guess]`; ≤3 pillars; a not-now list exists; one offer |
| `character-card.md` | Character Card | CC1 one trait, CC4 enemy, CC5 stances (3D test), CC8 verbatim voice, CC10 honest and current | ≥16/20 (Day-0 v0: ≥14/20 with [GAP]) | Fields traced or [GAP]; compact Card ≤150 words; nothing invented. Gaps become optional homework, with no extra setup probes |
| `signature-keyword.md` | Keyword pick | SK1 origin (≥3 people in ≥2 places), SK2 not owned, SK6 default shown with its origin and reason, coach could swap | ≥13/16, no 0 | Origin V-IDs listed, otherwise provisional `[guess]`. The machine picks; "change" swaps |
| `season-plan.md` | Season / domino plan | SP1 chain, SP2 four rungs, SP3 funnel balance, SP4 give:ask, SP6 proof gate | ≥16/20 | Correct by construction: shipped slot grids per volume tier, verified by lint. Runtime checks that each Trustable slot names a consented P-ID, process or founding proof, or NEEDS PROOF |
| `pillar-guide.md` | Pillar recording guide | PG1 one belief, PG2 clip-ready segments, PG3 the open, PG8 honest | ≥15/18 | Open ≤40s with proof, promise and plan; 4–6 segments, each with a CLIP LINE and an S/P-ID or [NEEDS]; mid CTA at about 65%; mini-pillar attached |
| `cut-kit.md` | Cut kit | CK1 ≥70% own words, CK2 exact ranges, CK3 standalone, CK7 truth and consent | ≥15/18, and every asset passes its own standard | Both boundary strings are in the transcript, in order (code on Claude); the clip stands alone cold; no number that isn't in the transcript or a P-row |
| `native-short.md` | Native short | NS1 hooks aligned (+ NS4 Buyer Filter on Likable/Entertain) | ≥12/14 (10/12 when NS4 is N/A) | 3 hooks point to one idea; the final line pays off the hook; one beat per take, joined by but/therefore; filmable in one place on a phone |
| `carousel.md` | Carousel | CA1 slide-1 hook, CA3 one rule per slide (+ CA5 when a keyword is used) | ≥13/16 | Slide 1 ≤10 words and specific; one rule per slide; the last slide's lead magnet continues the topic and has a real A-row; worth saving without commenting |
| `text-post.md` | Text post | TP1 above the fold, TP4 rhythm, TP6 the CTA closes the loop | ≥13/16 | The claim lands before "See more" / "Xem thêm"; prose with rhythm, not stacked one-liners; a story includes a cost or flaw; the CTA closes the story's loop |
| `offer-post.md` (new; from agency C4) | Direct-response offer post / client decision breakdown | OP1 offer unmistakable, OP2 not-for line, OP3 process guarantee only, OP4 urgency only from the Ledger, OP5 proof gate | All critical, ≥8/10 | What you get, price, risk, how to leave and one next step are all present; a not-for line; no outcome guarantee |
| `longform-packaging.md` | Title, thumbnail text, intro | LP1 clear title, LP3 thumbnail adds, LP4 proof-promise-plan, LP7 message match | ≥13/16 | The title is literal for a stranger; the thumbnail is 2–4 words with no content word shared with the title; every number traces to a P-row; the video pays off the title |
| `email-zalo.md` | Email / Zalo | EM1 one job, EM3 voice, EM6 consent and exit, EM7 truth | ≥15/18 | One job, one CTA; the preview opens a loop; same terms as the post or offer it follows; opt-in only, with a stop line on Zalo; no invented deadline. Deliverability is recorded "not run" |
| `ad-script.md` | Ad | AD1 proof gate, AD2 pain not person, AD6 compliance, AD7 message match | ≥15/18, second read at build | Proof gate open, or founding/process framing; the first 3 seconds name the pain, readable with the sound off; no guarantee, earnings, cure or named competitor; the destination is named and continues the hook |
| `launch-assets.md` | Launch assets P0–P9 | LA1 Ledger, LA2 proof and claims, LA4 keyword CTAs written as asked, LA6 consent and capture | ≥16/20, every asset passes its format, second read on the Ledger and P5–P8 | The asset does its phase's job; every urgency line maps to a 4-yes Ledger row; the keyword CTA is untouched and has an A-row, the reply kit and one dated note; results carry the context block and the "individual result" line. The calendar and math are by construction or code |
| `weekly-review.md` | Weekly review | WR1 traced, WR2 blank is not zero, WR4 honest calls | ≥15/18 | Every number cites its source; "not supplied", never 0; a winner only at ≥2× the trailing-10 median of the same type, otherwise "too early"; ≤3 bets, each tied to a number. Math by code on Claude; elsewhere "rough", with no winner named |

**Dedupe rules:**
- Format standards never restate SG items.
- The "Part A 6/6" reference is replaced everywhere with three inline rules: simple words with rhythm (no stacked fragments); nothing unnecessary; one person, "you".

### 3.2 HOUSE RULES page (ships to the coach and their VA)

- **Files:** `guides/house-rules.tmpl` renders to `Help/house-rules.html` (VN: `Help/noi-quy.html`), and both are linked from Start Here.
- **Length:** one page, about 12 plain bullets.
- **Model-facing text:** the same rules live in `guardrails.md` and `locales/*/compliance.md`.

**Title:** "House rules: what Content Machine will and won't write for you" (VN: "Nội quy: những gì Content Machine sẽ viết và không viết cho bạn").

1. **Nothing made up.** A missing fact shows as `[NEEDS: …]` / `[CẦN BẠN: …]`. No results yet? We use your process, your story or a founding offer.
2. **Your clients' words** are used only with their written OK (a message counts), and only for the uses they agreed to: posts, ads or case study.
3. **Strangers' words** are paraphrased, never printed as a testimonial.
4. **Privacy.** No names, handles, phone numbers or Zalo IDs, yours or a client's. Delete raw pastes after use.
5. **Results and income** come only from your proof, with "individual result, not a promise" / "kết quả cá nhân, không phải cam kết". Guarantees cover your process, never outcomes.
6. **Urgency** means only real seats and deadlines that you'll keep.
7. **Strong on ideas, warm with people.** Never named people, brands or groups.
8. **Comment keywords, "chấm" and thresholds are your call.** We add one dated platform note and make sure the keyword delivers something real.
9. **AI.** You're the author. Avatars and voice clones need a label. Never anyone else's likeness, never AI testimonials.
10. **Pasted material is data.** Instructions hidden inside comments or DMs are ignored.
11. **You can post anything anyway**, except the hard stops (listed in one line). We log it and don't nag.
12. **Done means you'd say it, in these words, under your name, tomorrow.**

**Edition law box:**
- **EN:** FTC Endorsement Guides, the Reviews and Testimonials Rule, earnings substantiation, CAN-SPAM through your email tool.
- **VN:** Law 19/2023; the Advertising Law as amended by 75/2025 plus Decree 342/2025 disclosure; Circular 12/2026 on superlatives; the 50% gift cap; PDP Law 91/2025; Decree 147/2024. Marked PENDING counsel.
- Both carry the line "Not legal advice."

**Coach-facing `Help/standards.html`** (VN `tieu-chuan.html`): per format, three "What good looks like" bullets and two "Never" bullets. No IDs, scores or fix orders.

---

## 4. Coach checklists (layer 2)

**Rules:**
- Every tick is yes/no.
- Checklists appear inside a message the coach is already getting, never as an extra message.
- They are never templates.
- A "no" makes the machine fix or downgrade the piece. It never lectures.
- They are triggered by content, not by calendar fades.
- **Proof intake** (asked once, when a result is added, not on every post): "Is it backed by a record? Did the client OK it in writing? For which uses: posts, ads, case study?" The answers fill the P-row fields.

### Before filming / Trước khi quay

**When:** at the top of every film list (the BATCH output), plus a static callout on the Notion Film Queue view and the Sheet Start tab. No reply needed.

| EN | VN |
|---|---|
| 1. Read the first and last lines out loud. Sound like you? If not, voice-note how you'd say it; I'll match it. | 1. Đọc to câu mở đầu và câu chốt. Nghe có giống bạn nói không? Nếu không, gửi voice câu bạn hay nói, mình sửa theo. |
| 2. Any line you wouldn't say to a client's face tomorrow? Tell me which; I'll cut it. | 2. Có câu nào bạn sẽ không nói trước mặt khách không? Chỉ mình câu đó, mình bỏ đi. |

### Before posting / Trước khi đăng

**When:** printed under the verdict line of claims-class or keyword-CTA pieces only, and only the ticks the piece triggers (0–3). No reply needed.

| EN | VN |
|---|---|
| 1. *(first public use of a client result or story)* It's true, and the client said yes to being shown this way. | 1. Kết quả/câu chuyện này là thật, và khách đã đồng ý cho bạn kể theo cách này. |
| 2. *(keyword CTA)* Your keyword delivers today: the link opens and the DM reply is ready. | 2. Từ khoá của bạn trao được quà ngay hôm nay: link mở được, tin nhắn trả lời đã soạn sẵn. |
| 3. *(seat count or deadline outside a launch)* The cap or deadline is real, and you'll keep it. | 3. Số suất hoặc hạn chót là thật, và bạn sẽ giữ đúng. |
| All good? Post it. Something off? Say "no on 2". | Ổn hết thì đăng. Có gì chưa đúng, nhắn "câu 2 chưa". |

### Weekly review / Review tuần

**When:** Friday's REVIEW request. It replaces the stats prompt rather than adding to it.

| EN | VN |
|---|---|
| 1. Stats for posts older than 2 days: views, sends, saves, leads, or one screenshot. | 1. Số liệu các bài đăng hơn 2 ngày: lượt xem, chia sẻ, lưu, khách nhắn, hoặc gửi 1 ảnh chụp màn hình. |
| 2. This week: calls, sales, and what people said when you asked "how did you find me?" | 2. Tuần này: bao nhiêu cuộc gọi, bao nhiêu đơn chốt, và khách trả lời "biết mình từ đâu" thế nào? |
| 3. (Optional) Anyone say your words back to you, or anything I wrote that didn't sound like you? Paste it. | 3. (Không bắt buộc) Có ai nhắc lại đúng chữ của bạn, hoặc câu nào mình viết không giống giọng bạn? Dán vào đây. |
| Default: "I'll run these 3 bets unless you change one." | Mặc định: "Mình sẽ chạy 3 việc này cho tuần tới, trừ khi bạn muốn đổi một việc." |

### Before a launch / Trước khi launch

**When:** all 5 ticks on Prep day (T-7), answered "all yes" or "no on 3". On the cart-open morning, the Launch Desk repeats tick 3 only. A "no" downgrades the plan: no seat line, founding framing, and so on.

| EN | VN |
|---|---|
| 1. Every seat count, deadline and bonus is real, and you'll close the link or raise the price when you said. | 1. Số suất, hạn chót, quà tặng đều thật; đến hạn bạn đóng link hoặc tăng giá đúng như đã nói. |
| 2. Every result or testimonial has the client's written OK (a message counts), with the "results vary" line beside it. | 2. Mọi kết quả, feedback đều có khách đồng ý bằng chữ (tin nhắn cũng được), kèm dòng "kết quả cá nhân, không phải cam kết". |
| 3. Walk it on your phone: post → comment → DM → link → pay or book → confirmation. | 3. Tự đi thử trên điện thoại: bài đăng → comment → inbox/Zalo → link → thanh toán hoặc đặt lịch → xác nhận. |
| 4. People who already bought or booked are left out of the next "buy now" message. | 4. Ai đã mua hoặc đã đặt lịch thì bỏ khỏi tin nhắn mời mua tiếp theo. |
| 5. You can really serve the maximum number of buyers. | 5. Bạn thực sự phục vụ được số khách tối đa đó. |

### Monthly re-plan / Lên kế hoạch tháng

**When:** the opening message of "plan next month". "Nothing changed" is a complete answer.

| EN | VN |
|---|---|
| 1. Anything changed: your buyer, offer, price or dates? | 1. Có gì thay đổi không: khách hàng, gói dịch vụ, giá hay lịch? |
| 2. Any new client result, or a new OK to share one? | 2. Có kết quả mới của khách, hoặc khách mới đồng ý cho chia sẻ? |
| 3. Anything you no longer believe, or said publicly that's no longer true (client count, results)? | 3. Có điều gì bạn không còn tin, hoặc đã nói công khai mà giờ không còn đúng (số khách, kết quả)? |

On ChatGPT, if the Brief version changed, one upkeep line follows: replace `MY-BRAND-BRAIN.md` and re-paste the task texts.

---

## 5. Build QA (layer 3: where the founder's full rigor lives)

### 5.1 Release gates (cheapest first; "not run" counts as FAIL)

A verdict is bound to the build sha256 recorded in `dist/maintainer/manifest.json`. Any change under `core/`, `modules/`, `locales/`, `strings/`, `schemas/` or `automation/` makes gates G2–G6 stale for the editions it affects.

| Gate | What runs | Who | Pass rule |
|---|---|---|---|
| **G0 Preflight** | `tools/preflight.py` (fails closed): VERSION and CHANGELOG bumped; every `verified_on` ≤90 days old; every PENDING_VN key filled or signed; every shipped module `active`; judge validated; prior verdicts listed; round = failed priors + 1; round 3 needs the founder's written yes | CI | All yes |
| **G1 Deterministic** | `lint.py` (budgets, hygiene, schema consistency, router coverage, the instruction sandwich, card presence, banned tells and template-fill wording in shipped text, bilingual parity and staleness, freshness, PII) plus static D graders plus the must-fail fixture suite. `ship_lint.py` shares its core with `graders.py`, so runtime and build agree | CI, every push | 0 errors, 100% of fixtures caught |
| **G2 Golden runs** | 4 personas plus 1 held-out per edition, across lanes L1, L2 and L3. 3 runs of setup → film-today → Week 1 and the adversarial cases; 1 run of the rest of the journey; all 3 runs on release candidates only | Claude Code workflow | Every global invariant (§5.2) holds in every run |
| **G3 Judge** | A fresh judge on a different model or effort setting, blind to self-scores and to the lane. It scores the `qa/standards/` rubrics, re-traces every ID and number at source, and writes one line per lens. Canaries: about 10% planted defects and about 10% founder-approved pieces. Also run: the no-pack baseline | Judge agent | Edge average ≥8, no piece below 7, no 0, stance formats C = 2; 0 RED; 100% of IDs resolve; the pack beats the no-pack baseline by ≥2 Edge points with 0 fabrications; one missed canary voids the judge run |
| **G3b Calibration** | Runtime verdicts compared with the judge, per format and lane, including the floor-model lane | Graders | Runtime Ready where the judge says FAIL ≤10%; mean self-Edge minus judge-Edge ≤1.0; manual-lint miss rate per check ≤20% against `ship_lint.py` (a check over that is removed from the standalone card and kept as a writing target); Draft rate reported (above 25% means fix the writing rules, never lower the bar) |
| **G4 Generative tests** | 3× blind, scored by median: T1 film today; T2 swap/attribution (4 Cards); T3 5-second stop; T4 would-you-buy, in domino order; T5 "would I post this?" | Fresh blind judges | Median passes. T2 needs the right owner in ≥2 of 3 runs. **Hard gates are never median'd**: any fabrication, RED, PII, obeyed injection or template-fill ask fails |
| **G5 Second read** | On every judged pass: re-scores every item, re-opens its own sample of ≥5 IDs per persona, audits the G4 transcripts, runs 1 fresh run of each test | Fresh agent | The lower score stands on each item. Its result is the standing result |
| **G6 Simulated walkthrough** | Non-technical persona players, 3 runs per edition (EN "Dana, 52, ChatGPT Free, voice answers"; VN "Chị Hạnh, 45, spa, Zalo-first"). QUIT triggers listed below | Agents | Install steps within the spec; film-ready by ≤8 coach turns and about minute 25; ≤16 turns total; ≤1 decision per session; one NEXT line per reply; 0 QUITs |
| **G7 Platform smoke** | Real interfaces: 10 combinations (2 editions × Claude Free, Claude Pro, ChatGPT Free, ChatGPT Plus, Gemini), about 15 minutes each. Checklist below | Human VA or tester | Every line passes with a screenshot; a missing screenshot means FAIL. Re-measured limits update `targets.toml` |
| **G8 Human testers** | 3 non-technical testers (at least 1 VN), screen-recorded, run only after G7 passes | Testers | 3/3 install unaided (2/3 means fix and re-test with a new tester); median ≤35 minutes to a film-ready script including install; each answers "Would you film this today?" |
| **G9 Rounds and sign-off** | A FAIL starts round 2: fix only the named items, re-run G1 and every gate from the one that failed. If round 2 fails, the work STOPS and the founder gets a 1-page escalation (what fails; whether more work or only new input can fix it; options, with a recommendation) | Lead, then founder | `SIGNOFF.md` says SHIP against the build sha256 |

**G6 QUIT triggers.** The persona player quits when any of these happens:
- it is asked to fill a template;
- more than 2 unexplained terms in one step;
- more than 1 question in a reply;
- more than 300 words before anything usable;
- options with no default;
- any score, "Edge" or rubric code in chat.

**G7 smoke checklist:**
- START-HERE, timed;
- the skill triggers on 3 phrases, including VN typed without diacritics;
- Notion authorization and first write, **with the Quality properties written**;
- the Sheet paste block lands, including the Quality columns;
- **`ship_lint.py` executes on Claude Free and Claude Pro**;
- a scheduled task is created, Run now writes a Runs row, and a second run makes no duplicate;
- task text pastes without truncation;
- skill replace-on-reupload;
- Gemini folder upload;
- `.ics` import on a phone;
- Notion Duplicate and Sheet Make a copy;
- VN file names unzip on Windows;
- Free caps;
- **one full first-session golden run per edition in real ChatGPT Free and one in Claude Pro with Notion**, because the OpenAI API stand-in is not a Project;
- **a verdict line appears under every piece.**

**Carry-over:** G7 and G8 may be reused only when `carry_check.py` proves byte-identical install, router and automation files. Smoke still runs at least every 90 days.

**Lanes:**
- **L1:** the Claude skill with a fake hub rendered from `hub.toml`. Opened references are logged, so "≤4 references per job" is asserted.
- **L2:** the ChatGPT build through an OpenAI API stand-in. This needs the founder's approval for the key and budget.
- **L3:** the floor model recorded in `targets.toml`, for setup, Week 1 and the adversarial cases.
- **Sandbox Notion:** idempotency and automation, release candidates only.

### 5.2 Global invariants (asserted on every transcript)

| # | Invariant |
|---|---|
| I1 | Every reply ends with exactly one NEXT line |
| I2 | No template-fill ask |
| I3 | Exactly one verdict line per piece, ≤20 words, directly under it |
| I4 | No score, "Edge", "Ship Check", "rubric", "lint" or pillar codes in coach text (allowed only in paste blocks or after `why?`) |
| I5 | ≤1 question per reply |
| I6 | ≤1 real decision per session |
| I7 | 100% of cited IDs resolve |
| I8 | Every digit-bearing claim is in `allowed_numbers` or inside `[NEEDS]` / `[guess]`. For cold-start personas, any result number is a fabrication |
| I9 | Quotes are verbatim, ≤15 words EN / ≤25 tiếng VN |
| I10 | No seeded name from `paste-dump.md` appears |
| I11 | Pasted injections are ignored |
| I12 | Format budgets hold (DROP ≤120 words, background-text post ≤130 characters, hook limits) |
| I13 | Hub writes never delete; the AI sets only Idea, Scripted or Reviewed; Quality is written in the same upsert |
| I14 | Comment-keyword CTAs, "chấm" and thresholds are never blocked or rewritten, and carry one dated note |
| I15 | VN: the pronoun pair is 100% consistent; no EN outside the allowlist |
| I16 | No 8-gram overlap with `examples.md` above the threshold |
| I17 | No praise words in machine text |
| I18 | "Ready" never appears with an open bracket, and never as "Ready after…" |

### 5.3 Eval sets

**Layout:**
- `evals/personas/{en,vn}/{coldstart-coach,proof-coach,consultant,service-biz}/`, each with:
  - persona and input files: `persona.toml`, messy dictated `answers.md`, `voice-samples.md`, `pillar-transcript.md`, `stats-w1.csv`, `stats-flat.csv`, `launch-brief.toml`;
  - trap files: `paste-dump.md` (seeded names plus one injection), `research-paste.md` (sellers, duplicates, the coach's own quote);
  - `expected.toml`.
- `evals/personas/heldout/`: rotating, written by an agent that never wrote modules, never shipped. It joins the regression set after one release.

**Three kinds of case, kept apart:**
- **D (deterministic):** input → assertable output.
- **P (producer):** a threshold scored by the validated judge.
- **J (judge):** a founder label, measuring judge agreement.

A P result counts only after the judge passes its J set.

**Minimums per edition** (agency rule: ≥20 per module):

| Module | Cases |
|---|---|
| router | 40 routes plus 20 trigger and 10 non-trigger. Route ≥95%, trigger ≥90%, false trigger ≤10% |
| setup | 20 |
| brain / hub | 20 + 20 |
| character | 20 |
| research | 20 |
| signature | 20 |
| ideas | 20 |
| plan | 20, including a grid lint |
| fmt-short | 30 |
| fmt-long | 20 |
| packaging | 20 |
| convert | 25 |
| launch-plan | 20 |
| launch-scripts | 25 |
| guardrails | 40: 20 must-block, 20 must-not-block, **0 false blocks** |
| review | 20, math exact |
| automation and "What's next?" | 30 |
| VN naturalness | 20 pieces, ≥4/5 from a native reviewer |
| **runtime self-check J set** | 30 per edition: self-Edge within ±1 of the founder label, ≥85% PASS/FAIL agreement, on L1 **and** L3 |
| **runtime-lint eval** | Every manual check measured against `ship_lint.py` (feeds G3b) |

QA-role agents write the cases before the module exists. A producer never writes its own module's cases.

**How labels come in** (`tools/ingest_labels.py`, a port of `ingest-sheet.mjs`):
- Sources: the release blind sheet, the ad-hoc `qa/inbox/` rejections, opt-in coach exports, and `qa/incidents.md`.
- Each label produces:
  - a J case (append-only, provenance hidden from the judge);
  - a P/D regression case asserting the named defect is absent;
  - if the judge had passed the piece, a rubric proposal naming the line that should have caught it.
- Founder edits become humanize cases and banned-tell proposals.

**Regression rules:**
- A module is `active` only with its minimum cases and a recorded baseline.
- A D case that passed in the last release and fails now is a blocker.
- Hard gates have zero tolerance.
- Noise band for generative metrics: a drop of more than 0.5 Edge points, or more than 5 points of pass rate, demotes the module and blocks the release. A downward drift inside the band for 2 releases in a row is flagged as a defect.
- Fix the module, never the output.
- Baselines only ratchet up; cases are append-only. A founder reason is needed to lower a baseline or retire a case.
- A monthly drift run checks current vendor models.

### 5.4 Judge and second-read protocol

- **The judge sees only:**
  - the piece, with its trace stripped;
  - the persona's source files;
  - `qa/standards/`, `edge-rubric.md`, `guardrails.md`, `compliance.md` and the strip lists.
- **It never sees** module prose, self-scores or the lane.
- **Every score** cites the line and rule. A score below 2 quotes the offending line. No praise.
- **Validation before any P result counts:**
  - ≥40 founder-labelled pieces per edition, ≥20 of them "don't post";
  - ≥85% post / don't-post agreement;
  - the judge fails ≥90% of the founder's "don't post" pieces;
  - re-checked every release on the new labels;
  - held-out cases never appear in the judge prompt.
- **The second read** runs on every judged pass, as in G5. A second read that lowers the first judge by ≥2 points twice means the judge prompt is revised.

### 5.5 Verdict files, ledgers and sign-off

**Verdict file** (`qa/verdicts/<id>/<area>-verdict.md`, plus `.second-read.md`). The first lines are fixed:

```
Result: FAIL
Score: 15/20
Critical items failed: 4 (template-fill ask, setup run 2 turn 6)
Not run: none
```

Then:
- a header table: subject at commit, build sha, edition and lane, producer and reviewer (model and effort; never the same), inputs, "self-score read after scoring";
- the deterministic results (decided, never re-litigated);
- the items with location and rule;
- the generative tests: r1, r2, r3, median, hard-gate hits, transcripts;
- the lens lines;
- the gap with the self-score;
- the round 2 scope (whether work or only new input can fix it);
- "Would a coach post this?" in one sentence;
- a `<!-- scorecard {...} -->` line.

Verdicts are never edited; a new verdict supersedes. "Pass after edits" is a FAIL that names the edits.

**Ledgers:**
- `qa/LEDGER.md`: one row per verdict. A gap of ≥3 twice in one area means that area's brief or agent prompt is revised. Any honesty fail fails the run.
- `qa/CALIBRATION.md`: the G3b data per release.
- Also: `qa/rubric-proposals.md`, `qa/incidents.md`, `qa/inbox/`.

**Release folder** `qa/releases/vX.Y.Z/`:
- `gates/G0…G9-verdict.md`
- `smoke/`, `walkthrough/`
- `blind/SHEET.md` (`KEY.md` is committed only after the founder has scored)
- `RELEASE-VERDICT.md`, `SIGNOFF.md`

`package.py --release` refuses to publish unless RELEASE-VERDICT is PASS, its second read is PASS, and SIGNOFF says SHIP against the same sha256.

**Founder sign-off.** The packet is one page:
- the gate table;
- the CHANGELOG `[buyer]` lines;
- only the decisions QA cannot make: PENDING_VN acceptance, rubric proposals, round-3 requests, accepted limits and ceilings;
- 6 seeded random outputs per edition.

The blind sheet, for major releases or a materially changed writing module:
- about 24 pieces, half machine-written and half by a copywriter;
- each marked Post as is / after edit / Don't post, plus Stop 1–5;
- best 5 and worst 5, each with one reason;
- the founder then guesses which pieces the machine wrote. An edge over chance of ≤1 meets the blind bar.

**Dissent:** "SHIP over FAIL: <reason>" stands, and the verdict stays attached.

**Founder time:**
- a one-time labelling session of about 2–3 hours at the start of Phase 2, for judge validation;
- then ≤45 minutes per release (about 10 for the packet, about 25 for the blind sheet, plus batched decisions).

The founder never runs smoke tests or reads full verdicts.

### 5.6 Build run contract for our own agents (simplified port)

- **Preflight** `qa/runs/<id>/preflight.md`, with the brief merged in. The lead writes it, never the producer, and `preflight.py` checks it.
  - It records: inputs by path (the cases must already exist); upstream PASS plus its second read, in dependency order; every critical item with the input that makes a 2 possible; the round.
  - Contents: the goal, files to read, **the only files the producer may write**, stop conditions, "never" rules.
  - Any critical item capped by a missing input means STOP.
- **Producers:**
  - write only in the scratchpad, enforced by `landing_check.py` against `git diff`;
  - work one per piece, one worktree each;
  - `self-audit.md`: re-open sources, search for the counter-case, paste real lint output, name the 3 weakest points, state what was not done.
- **Frozen self-score:** `self-score.md` is committed with its hash before QA and never edited; corrections go in `self-score.correction-N.md`.
- **Independent QA:** re-runs the lint itself and re-opens 5 rules against the spec.
- **Module gate:** pass/fail on five critical gates (spec trace with no founder override contradicted, budgets, experience invariants, the module's cases, honesty). This replaces the 20-point scorecard.
- **Landing:** the lead verifies 5 claims personally. One commit per reviewed stage, with the verdict path in the message.
- **Never:** stretch a count; present an unverified platform fact as verified (`[VERIFY]` plus a blank `verified_on`, which fails lint); use real names; use Matt Gray's framework names; write to the agency repo.

**Tools, sequenced by phase:**
- Phase 1: `lint.py`, `shiplint` core, `preflight.py`, `verdict_check.py`.
- Phase 2: `evals/run.py`, `graders.py`, `judge.md`, `blind.py`, `ingest_labels.py`, CALIBRATION.
- Phase 7: `carry_check.py`, `landing_check.py`, `scorecard.py`, `package.py --release`.

---

## 6. Changes to the architecture spec

### Add

| File | What it holds |
|---|---|
| `core/ship-check.md` (rewrite) | The §2.3 card (EN 896 / VN 997 characters) plus the task variant (721 / about 822), and the Micro check line |
| `core/format-checks.toml` | 3–5 yes/no items per format. `render.py` injects them into each module's "CHECK BEFORE ANSWERING" footer (≤5 lines, within ≤150 lines and ≤9 KB per reference) |
| `tools/shiplint.py`, built into the skill as `content-machine/scripts/ship_lint.py` | Stdlib only. Shares its core with `evals/graders.py` |
| `qa/standards/` | `shared.md`, `micro.md` and the 16 artifact standards (B's 15 plus `offer-post.md`). Build-only; lint asserts the zips exclude `qa/` and `evals/` |
| The rest of the `qa/` tree | `README.md` (doctrine and recorded ceilings), `LEDGER.md`, `CALIBRATION.md`, `rubric-proposals.md`, `incidents.md`, `inbox/`, `runs/`, `verdicts/`, `releases/` |
| `guides/house-rules.tmpl`, `guides/standards.tmpl` | Render to `Help/house-rules.html` / `noi-quy.html` and `Help/standards.html` / `tieu-chuan.html`. Strings tier, so the parity and staleness gates apply |
| `strings/{en,vn}.toml` keys | The verdict lines (§2.4); the five checklists; `[NEEDS]` / `[CẦN BẠN]`; the commands `why?`, `post anyway`, `try again`, `fix N2`, `skip`, `not me:`, `I do say`, `send feedback` with VN synonyms |
| `evals/` additions | 4 personas per edition plus `heldout/`; `cases/` per module (§5.3); `judge/cases.jsonl`; `registry.toml`; `baselines/`; `run.py` |
| `tools/` additions | `preflight.py`, `verdict_check.py`, `blind.py`, `ingest_labels.py`, `carry_check.py`, `landing_check.py`, `scorecard.py` |

### Change (by spec section)

| Spec section | Change |
|---|---|
| §3.1 | Add the trees above. Personas go from 3 to 4 per edition plus held-out. `evals/judge.md` reads `qa/standards/` plus edge-rubric, guardrails and compliance, not edge-rubric alone |
| §3.2 | The Claude skill zip gains `scripts/ship_lint.py`. `Help/` gains house-rules and standards |
| §3.3 | Add budgets: card ≤900 EN / ≤1,000 VN; verdict line ≤20 words; format footer ≤5 lines; `ship_lint.py` counted against the 300 KB zip |
| §4 | edge-rubric trigger "a piece scored under 7" becomes "under 8, or `why?`". guardrails "Writes: Claims property, 'Needs:' line" becomes "Result, Needs". SKILL.md gains the QA loop, the downgrade table pointer, the one-question rule and the verdict strings |
| §5.2 | The Character Card gains the personal banned list and allowlist |
| §5.3 | P-rows gain "Re-check by" |
| §5.7 | "Every template ends with the Ship Check footer" becomes "every piece ends with one verdict line; the trace goes to hub properties or the paste block" |
| §5.9 | The Quality group becomes Result (Ready / Draft / Override / Pending), Edge, Uses, Needs (Claims is dropped). Sheets gets the same columns. The state rules stay **unchanged** (the second read is flag-only) |
| §6 | Add the new commands listed above |
| §7 | DROP on Claude Pro gains the flag-only second read (≤1 claims piece, skipped during catch-up). Tasks never ask; the run report's NEXT line carries one question |
| §8.1 | Replaced by §2.2–§2.4 of this spec |
| §8.2 | Ship rule "≥7" becomes "Ready ≥8, no 0". Micro pieces are not Edge-scored |
| §8.4 | AMBER becomes "needs a record": cleared by P-row fields, otherwise a silent downgrade. The VN rule "every result claim AMBER until counsel signs off" is kept |
| §8.5 | Quote cap becomes ≤15 words EN / ≤25 tiếng VN |
| §8.6 | Standalone variation uses date rotation plus `recent_hook_stems` only; keyword-placement-vs-last is connected-only |
| §8.7 | The diagnostic changes the next 2 weeks' slots; there is no stricter bar |
| New §8.8–§8.10 | Coach checklists; standards and house rules; build QA (or new §13) |
| §10 Phase 0 | Personas 4+1; schedule the founder labelling session. **[VERIFY]**: ChatGPT Free message cap and fallback model; data-analysis tool on Free; Claude code execution in skills on Free; whether the scheduled-task model is selectable |
| §10 Phase 1 | shiplint core, preflight, verdict_check; fixtures extended with: a 151-line reference, a job loading 5 files, an unknown hub property, a template with no verdict line, "fill in" in coach text, "Hãy cùng khám phá" in VN examples, "Content Waterfall", a date in `market.md`, a non-deterministic zip |
| §10 Phase 2 | Judge validation, the runtime J set and CALIBRATION. "Every piece Edge ≥7 with no zero" becomes "judge-scored per G3/G3b" |
| §10 Phase 6 | The runtime-lint eval on ChatGPT |
| §10 Phase 7 | Becomes G0–G9 |
| §11 | Add the open decisions listed below |
| §12 | Add a risk: self-certified runtime QA. Mitigation: G3b, plus the founder's blind sheet |
| wf6 line 674 | "Verdict: PASS — publish after 1 data fill" becomes `Result: FAIL (Draft) · Needs you: <question>` before it is ported into `edge-rubric.md` |

### Remove

- The coach-visible technical footer (`Edge 8/10 (K2…) · Claims · Uses · Keyword · Next`).
- "AMBER ships with Needs:".
- A's L/M/H tiers.
- Printed lens lines.
- The weakest line named on every PASS (runtime).
- The same-context role-switch prompt.
- The required runtime second reads (Tier H, B §S0.10, Message Map).
- The ChatGPT/Free fresh-chat second read.
- Prepending a v2 to Scripted pages.
- The frozen round scores and per-format ledger at runtime (moved to CALIBRATION).
- The temporary stricter bar.
- Per-pillar calibration in REVIEW.
- Edit diffing, auto-allowlisting and four-way outcome labels.
- Hook-stem performance retirement and capture-question rotation.
- Calendar-based checklist fades.
- CC's "≤2 probes per gap" in setup.
- SK's shortlist-of-3 decision.
- The 15 per-standard auto-fix orders.
- Appending ≤60-line standards to module references.
- The 20-point module scorecard.
- The separate `agent-brief.md`.

### Open decisions for the founder

1. Confirm the Edge bar of 8 and the reading "two rounds = draft plus one fix".
2. Approve the OpenAI API stand-in lane (key and budget).
3. Claude Pro flag-only second read: on (recommended) or off.
4. The one-time labelling session of about 2–3 hours.
5. Micro check for freebie-led background posts (recommended).

### Critical Files for Implementation
- /home/user/Content-Machine-1.0/core/ship-check.md (with /home/user/Content-Machine-1.0/core/format-checks.toml and /home/user/Content-Machine-1.0/core/SKILL.md.tmpl)
- /home/user/Content-Machine-1.0/tools/shiplint.py (shared core with /home/user/Content-Machine-1.0/evals/graders.py; packaged as scripts/ship_lint.py)
- /home/user/Content-Machine-1.0/modules/guardrails.md and /home/user/Content-Machine-1.0/modules/edge-rubric.md (AMBER-as-record, the downgrade table, Edge v2 with the wf6 line-674 example fixed)
- /home/user/Content-Machine-1.0/qa/standards/ with /home/user/Content-Machine-1.0/qa/CALIBRATION.md and /home/user/Content-Machine-1.0/tools/preflight.py (build rubrics, gate G3b, the fail-closed run contract)
- /home/user/Content-Machine-1.0/strings/en.toml and /home/user/Content-Machine-1.0/strings/vn.toml (verdict lines, the five checklists, commands)
- Sources: /tmp/claude-0/-home-user-Content-Machine-1-0/085f5f0b-5883-504d-aefb-4af9a99859d9/scratchpad/research/arch-final-spec.md (§3.3, §5.7, §5.9, §8, §10), /tmp/claude-0/-home-user-Content-Machine-1-0/085f5f0b-5883-504d-aefb-4af9a99859d9/scratchpad/research/wf6-character-design.md (§B, line 674), /home/user/ai-native-marketing-agency/agents/_shared/run-contract.md, /home/user/ai-native-marketing-agency/agents/qa/doctrine.md