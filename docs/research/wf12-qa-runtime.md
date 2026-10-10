# Content Machine 1.0: runtime QA (Layer 1) and coach checklists (Layer 2)

I read the agency QA sources (doctrine, run contract, brain/qa index, copy quality and house rules, research quality, the claims-lint, copy-verdict, email-verdict, launch-verdict, report-verdict and second-read skills, W-09 and ADR-014) along with the plan, the arch spec (§2, §5, §7, §8, §10), the Edge Check v2 spec (wf6 §B) and the research spec (wf7 §2.0, Step 6, §7). No files were written.

**The rule that ties the two layers together:** anything the machine cannot see becomes a coach tick, and every coach tick asks only about something the machine cannot see. That keeps the checklists to 3–5 ticks, and the machine never claims a check it did not run ("not run" is not "clean").

---

## 1. Mapping: agency QA rule → Content Machine runtime

Status key: **K** kept · **A** adapted · **D** dropped · **L2** moved to the coach checklists · **L3** moved to build QA.

| # | Agency rule (source) | How it runs in Content Machine | St. |
|---|---|---|---|
| 1 | The only question: would it embarrass the company or harm the client if it went live as is (doctrine) | The Ship Check's governing question: "Would this embarrass the coach or cost a buyer's trust if posted as is?" | K |
| 2 | Four layers, cheapest first (doctrine, ADR-014) | Lint → Edge v2 + format STANDARD → lenses → coach outcome (the human sample). On Claude Pro a scheduled second read is added. Scoring does not start until the lint is clean. | A |
| 3 | Claims lint: patterns for money, "N clients", "in N days", guarantee, %, multipliers, "up to/typically/results may vary", scarcity (claims-lint §2) | Same pattern scan in EN and VN, plus VN superlatives (nhất / duy nhất / số 1) and health words. A hit is cleared only by a record (a P-row or a Ledger row), never by argument. A quiet lint is not a pass: the compliance lens reads for what the patterns miss ("about six weeks later", implied health claims). | K |
| 4 | Three claim marks, no fourth; a hedge is not a cure; the disclosure sits beside the claim, and footer-only is major (claims-lint §3–6) | **GREEN** means the record was opened and its words match. **AMBER** means a record is needed: the claim stays in brackets and the piece is not Ready until it is filled. **RED** means remove or refuse. The typical-results line goes in the same caption, slide or spoken beat, never only in the bio or comments. | K |
| 5 | Leak lint (other tenants) | Becomes a privacy leak check (audience names or handles, client names without consent) plus a swipe leak check (no verbatim lines over 8 words from reference creators or competitors; swipes teach structure only). | A |
| 6 | Link, tracking, CWV, craft Tier 0 and email-auth checks | Dropped: the machine builds no pages and sends nothing. The human-checkable parts become ticks ("walk the path on your phone"; "your email tool adds unsubscribe and address"). | D→L2 |
| 7 | Rubric lines scored 1–5; any 1–2 blocks; ship only at 4+ on every line (W-09) | Edge v2: 5 pillars scored 0–2, plus format STANDARD lines scored 0–2. Any 0 blocks, and every critical STANDARD line must be at 2. | A |
| 8 | RMBC four dimensions and bands <60 / 60–79 / ≥80 | K ≈ result specificity, V ≈ mechanism and belief shift, A ≈ proof believability, LADDER ≈ CTA clarity. The bands become ≤5 re-ideate / 6–7 fix / ≥8 pass. | A |
| 9 | Lenses (skeptical prospect, compliance, mobile, closer), one line each, uncertainty fails | Five lenses: buyer, compliance, 5-second phone, "sounds like me", Message Map. On Tier H a sixth, the DM/call lens (the port of the closer), is added. | K+ |
| 10 | Human sample at the gate; rejections become labels (doctrine L4, ADR-014) | Each piece records a coach outcome (posted as is / edited / rejected / "not me"), plus overrides. These are local labels, and the founder receives them only through an opt-in export. | A |
| 11 | The verdict is a record, written first, with no praise, evidence attached, within an SLA | An internal QA record in the hub whose first line is `Result: PASS/FAIL`. The coach sees one line. The machine's own text never uses praise words (EN: great, powerful, amazing; VN: tuyệt vời, xuất sắc, quá đỉnh). The SLA is dropped. | A |
| 12 | Message match: ad → page → application → confirmation (doctrine) | Domino continuity: each piece's link-forward matches the next piece's hook; the keyword CTA's promise matches its A-row asset; the ad hook matches the offer-post headline; the email continues the post it follows. A broken chain is a structural fail. | A |
| 13 | Tracking: events fire once and deduplicate | Dropped. Replaced by the booking-form attribution question and keyword-comment counts in REVIEW. | D |
| 14 | Eval sets of ≥20 cases per skill; promotion by eval; regressions demote (ADR-014) | Release gate: at least 20 labelled cases per job per edition. | L3 |
| 15 | When wrong, fix the rubric instead of defending the verdict | An incident row records the line that should have caught it. That becomes a personal rule (Voice Card banned list or Hard Limits) and, opt-in, a founder rubric proposal at the quarterly update. | A |
| 16 | Dissent: a CEO approval over a fail stands, the verdict stays attached, and it is not raised again | "Post it anyway" is honoured except on hard stops. The verdict stays in the hub and the machine does not nag. | K |
| 17 | Preflight: inputs exist, upstream passed, the critical items can reach 2, round number (run contract §1) | A per-piece preflight checks the Message Map, the Voice Card, that cited material IDs exist, and the Tier H gates (proof gate, Ledger, A-row, consent, transcript). The outcome is **GO / DOWNGRADE / NEEDS YOU**. DOWNGRADE is added so the coach never hits a dead end: founding framing, a process story instead of an income number, no seat line. | A |
| 18 | The lead writes the preflight; QA checks it | The router job card fixes the preflight items. The checker re-verifies each preflight claim at source (for example, "proof gate open" means the P-row consent is re-opened). | A |
| 19 | The brief is written by the lead, never the producer (§2) | The slot row is the brief (rung, belief, keyword, format, CTA). The plan writes it, not the writer step. | A |
| 20 | Honesty over targets; stretched label, squinted backer, rounded-up count, "most" vs "some", cut quote all fail (§3) | Fewer pieces beat padded pieces: "3 shorts this week, not 5, because only 3 stories exist" is a pass. The stretched-label list for Content Machine is in §2.6 below. | K |
| 21 | Blank is not zero; unknown is not a guess | `[NEEDS: …]` (VN `[CẦN BẠN: …]`). In the scoreboard, missing stats read "not supplied", never 0. | K |
| 22 | Self-audit: re-open sources, look for the counter-case, recount, name the 3 weakest (§4) | The writer re-opens the cited IDs. The buyer lens is the counter-case. Numbers are recounted from P-rows. The checker names one weakest line per piece, even on a PASS. | A |
| 23 | Frozen self-score, read only after QA scores (§4–5) | In one shared context the writer gives **no score**, so the checker is not anchored. The checker's round-1 score is frozen in the hub, and the second read and the coach outcome are compared against it. | A |
| 24 | The reviewer never produced the work and starts from a fresh context (§5) | Not possible inside one reply. The in-chat checker is labelled "same-context" and uses the separation tactics in §2.4. A real fresh context comes from the Claude Pro scheduled second read, or a fresh chat for Tier H. | A (partial, labelled) |
| 25 | QA re-verifies at source with its own sample | At this scale the checker covers everything: 100% of IDs resolved, every quote compared character by character, and the first and last words of every transcript PASSAGE found again. | K |
| 26 | Generative tests run 3 times blind; the median scores (§5) | Dropped per piece (too costly). Kept at Season level: at re-plan, 3 hooks are written from the Brief alone and each gets the swap test. Also kept in release evals. | A/L3 |
| 27 | `Result:` line first; no conditional pass | Internally `Result: PASS/FAIL`. For the coach, "Ready" or "Needs you". Any open [NEEDS] means not Ready. | K |
| 28 | A second read on every pass; the lower score stands; its result is the standing result (§6) | Claude Pro: every Tier H piece plus a sample of Tier M, run in DROP (at most 3 per run). Other platforms: Tier H in a fresh chat, batched. The lower score stands. | A (sampled) |
| 29 | Two rounds, then the CEO; round 3 needs the CEO's yes (§7) | At most two fix rounds, then one question to the coach. A third attempt happens only on "try again" or "post anyway". | K |
| 30 | Honesty ledger: a gap of ≥3 twice triggers an SOP revision (§8) | A machine QA ledger per format (checker vs second read vs coach outcome). A gap of ≥2 twice in 30 days tightens that format (§5.3). | A |
| 31 | Drafts outside the repo; the lead verifies 5 claims; robots audit; one producer (§9) | The AI sets only Idea, Scripted or Reviewed. It never says "saved" before the write returns. Research respects blocks and privacy (wf7 §7.2), and the coach re-opens 3 research lines (G11). One script per Slot Key (upsert). | A |
| 32 | House rule 2: nothing invented → `[NEEDS: …]` | Kept as written. A coach with no results says what they have instead. | K |
| 33 | House rule 3: a quote is exact with its link; buyer quotes are paraphrased in copy | V-rows are exact and linked. In content, strangers are paraphrased and clients are quoted only with their written OK. | K |
| 34 | House rules 4–5: pseudonyms; sources (robots, read-only, no private groups) | Role only, A01 / C01; in Paste mode names become letters. The research access rules live in the research files, not the QA card. | K |
| 35 | House rule 6: US English | Edition output contract, VN xưng hô consistency, and the EN-leakage scan with its allowlist. | A |
| 36 | quality.md Part A (Sabri's writing checklist) | Folded into humanize and G3 voice lint (simple words with rhythm, never fragments; nothing unnecessary; "you"; no corporate voice). | A |
| 37 | Part B: the nine persuasion questions | Checked at series level: each Domino series answers all nine across D1–D7, checked at plan time. Per piece only for offer posts, sales emails and ads. | A |
| 38 | Part C critical items C1–C7 | C1 a level-3 pain line from a V or R row on Credible and Trustable pieces · C2 the desire as a picture (V) · C3 specificity (K) · C4 offer unmistakable (offer-post STANDARD) · C5 voice (Au + G3) · C6 truth (G2) · C7 delivered as it would be posted, notes after. | K (distributed) |
| 39 | "Would I run it?" in three forms, including "after these edits" | Two forms only: "Yes, because…" or "No, because…". The third form contradicts the run contract's no-conditional-pass rule. | A |
| 40 | copy-verdict: every score cites a rubric line and a location; never score the piece you would have written | Any score below 2 quotes the line. A score with no location is removed. | K |
| 41 | The reviewer never rewrites or suggests wording | In one chat: the checker names the defect, then the writer fixes it in a separate step. After any fix the whole piece is linted again (the V-999 lesson: defect classes regenerate). | A |
| 42 | Recorded ceilings are never waived and never punished twice (copy-verdict §4) | Cold start with the proof gate locked: Authority is capped at 1 and the verdict names the cap. Trustable pieces pass only with founding framing. Nothing is invented to clear a cap. | K |
| 43 | A failing verdict is recorded, not discarded | A QA history toggle on the hub page. Needs-you pieces stay as DRAFT rows. | K |
| 44 | email-verdict: seeds, renders, tokens, the stop after a booking | Text-level lines only (subject length, preview as an open loop, one CTA, token fallbacks written, continuity). The booked-stop becomes a launch tick. | A/L2 |
| 45 | launch-verdict: not run ≠ pass; walk the funnel on a phone | The machine never says "your link works". "Walk the path on your phone" is a tick. Launch assets are checked as one set (Ledger, continuity). | L2 |
| 46 | report-verdict: every number traced; blank ≠ 0; a benchmark is never the client's number; the verdict is never softened | Scoreboard rules: "not supplied", "typical, not yours" labels, and the break point stated plainly. | K |
| 47 | ADR-014: the reviewer runs on a different model setting from the author | Optional: the Claude Pro second-read task uses another model, if the scheduler allows it (verify in Phase 0). | Opt. |

---

## 2. The runtime QA loop, per output

### 2.1 Risk tiers decide which layers run (cheapest first)

| Tier | Outputs | Layers |
|---|---|---|
| **L** | DROP idea and hooks, titles and thumbnail options, capture questions, plan rows | Preflight (Message Map) · lint subset (hook lengths, tells, new hook stem, claim words) · Edge-lite ≥4/5. Nothing is shown to the coach; failing ideas are dropped. |
| **M** | Native short, clip, carousel, text post, nurture email, pillar guide, cut-down, cut kit | Everything in L, then full lint · Edge v2 + format STANDARD · lenses (phone, me, map, plus buyer on Credible) · checker · ≤2 fixes · second read sampled on Claude Pro |
| **H** | Anything with a result number, testimonial, client case, income or health topic, offer or direct-response post, ad, sales email, DM flow with a price, launch P1 with slots and P5–P8 | Everything in M, then all 6 lenses · a claim-by-claim mark · Ledger check · second read **required** · the before-posting checklist every time |

### 2.2 The loop (Ship Check v2)

**Step 0. PREFLIGHT** (per piece, before any drafting). Check:
- (a) the Message Map exists: ONE buyer, problem in their words (V-ID), promise, named method, enemy, offer or founding pilot, 3 pillars, and the not-now list;
- (b) the Voice Card has at least 2 verbatim samples (otherwise generic mode: Au and C capped at 1);
- (c) the Bank holds the material this angle needs (S, V, P, R IDs). If it doesn't, pick the angle the Bank can prove ("material-first drafting").

Tier H also needs: the proof gate open with a P-row that has Consent=Y for this use and Substantiated=Y; a Ledger row with 4 yeses for any urgency; an A-row for every keyword CTA; consent on any client story; the transcript for a cut.

The outcome is one of three:
- **GO.**
- **DOWNGRADE:** founding framing, a process story instead of an income number, no seat line, a composite story labelled as composite. Stated in one line.
- **NEEDS YOU:** only when no honest version exists (for example "write a testimonial post" with no testimonial). The message says what is missing and who can supply it (you, your client, your VA), and everything else still ships.

**Step 1. WRITE** all pieces in the batch from Bank material. The writer gives no score.

**Step 2. DETERMINISTIC SELF-LINT** (mechanical, run on the whole batch at once; its result is final). Each item is a count or a match, never a judgment:

| Group | Rule |
|---|---|
| Lengths | Verbal hook ≤12 words EN / ≈18 syllables VN · title hook ≤6 words · carousel S1 ≤10 words · BG post ≤130 characters · email ≤250 words with subject ≤50 characters · word count = word_rate × seconds ±15% · text post: hook before the "See more" / "Xem thêm" cut |
| Sentences | Average ≤15 words, none over 25, at least 1 punch line of ≤5 words. No semicolons or em dashes in spoken lines. Questions only in the CTA |
| Strip lists (H1–H9 EN / V1–V9 VN) | 0 hedges in the hook and claim lines · ≤1 AI tell · ≤1 "not X but Y" · no throat-clearing · no recap ending |
| Trace | Every number, name, quote and result carries an ID; every ID resolves; quotes match V/O rows exactly; numbers come only from P-rows; a public P-row has consent for this use; result claims need Substantiated=Y |
| Claims scan | Every pattern hit is mapped to a record → GREEN, AMBER (bracketed) or RED |
| Scarcity | Every urgency or scarcity word maps to a Ledger row |
| Keyword | Chosen K appears exactly once, in this piece's rotated placement · ≤2 coined terms · keyword CTA has an A-row |
| Ladder | 1 rung · 1 B-ID · the CTA matches the rung table · a link-forward exists |
| Variation | Hook-stem ID not in the last 10 · same structure no more than twice in a row · keyword placement differs from the last piece |
| Cut | Each PASSAGE's first and last words are found in the transcript · ≥70% verbatim |
| Privacy | No audience names or handles; client names only with consent |
| VN | Xưng hô consistent · no English outside the allowlist · price format · #QuảngCáo where required · "kết quả cá nhân, không phải cam kết" beside any income figure · gift worth ≤50% of the price |
| Brackets | Any `[NEEDS]` or `[PROOF NEEDED]` makes the piece a DRAFT |

*Option (decision for the founder):* on Claude, where code execution is already on (install step 1), ship `scripts/ship_lint.py` inside the skill and run it once per batch. On ChatGPT and Gemini the model does the same counts by hand. Phase 2 measures how many more misses the script catches.

**Step 3. RUBRIC SCORE**, done by the checker:
- Edge v2 (K, V, A, Au, C, each 0–2), hard gates G1–G3, and the borrowed-attractor detector (flex-only, freebie-only or résumé-only fails outright and triggers "flip it");
- the **format STANDARD**, which lives in the "CHECK BEFORE ANSWERING" footer `render.py` already adds to each format file. Critical lines per format:
  - **Short:** 3 aligned hooks; final line written first; one beat per take.
  - **Clip:** stands alone.
  - **Carousel:** one rule per slide; last slide carries the lead magnet and the keyword.
  - **Pillar:** Proof → Promise → Plan opening; 4–6 segments, each with a CLIP LINE; mid CTA at about 65%; the open loop closes; thumbnail text adds to the title and never repeats it.
  - **Email:** preview is an open loop; one CTA with specific link text; continuity with the post it follows; no new promise.
  - **Offer post:** C4 offer unmistakable (what you get, price, risk, how to leave, one next step); a not-for list; process guarantee only.
  - **Ad:** hook readable with the sound off; one claim; the lead sits in the first visible line; no personal-attribute phrasing; proof gate.
- Calibration: values stated as absolutes; the coach's own patterns quantified; outcomes for others as ranges.

**Step 4. LENS PASSES** (one line each; uncertain = fail):
1. **Skeptical buyer** (Card WHO plus the top O-row): which claim would I not believe? Is there a trust cue within 2 sentences?
2. **Compliance and platform** (the edition's compliance.md): which line would a regulator or platform reject? (FTC / EU; VN Law 19/2023, the Advertising Law, superlatives.)
3. **5-second phone read:** title hook, first line and on-screen text alone. Is it clear who this is for and why to stay? Does it work with the sound off, and before "See more"?
4. **"Does it sound like me?"** Against the Voice Card samples, banned words and xưng hô. Would any line make the coach stumble? Does it pass the swap test?
5. **"Does it follow the Message Map?"** One of the 3 pillars, not on the not-now list, uses the buyer's own problem words, points up the ladder to the offer, and the "why this gets clients" line exists in the hub.
6. *(Tier H)* **DM/call lens:** what will the person who DMs ask next that this post made worse?

**Step 5. INDEPENDENT CHECKER PASS.** This is where steps 3 and 4 are performed; §2.4 lists the separation tactics.

**Step 6. FIX ROUNDS** (at most 2). Fix only the defects the checker named, then re-lint the whole piece, then re-score. Round 1's score is frozen; round 2's is stored next to it.

If the piece still fails after round 2, the machine decides whether **more work** could fix it (unlikely after 2 rounds) or whether **only new input** can. In the second case the piece ships as a DRAFT with ≤1 question per piece and ≤3 per batch, asked together at the end of the reply. A third attempt happens only on "try again" or "post anyway".

**Step 7. VERDICT.**
- **PASS** means all of these: Edge ≥8/10, no pillar at 0, gates G1–G3 pass, critical STANDARD lines at 2, 0 open [NEEDS], and all lenses ok.
- Stance formats (F1, F4, F6, F9, F11, F13) also need C = 2.
- A recorded ceiling is named in the verdict, not waived. Example: "Authority capped: no consented client results yet", which a founding-framed Trustable piece is allowed to carry.
- Everything else is FAIL, shown as "Needs you".

**Step 8. "Would I post this?"** One line written by the checker as the coach's head of content: "Yes, because <evidence tied to a pillar>" or "No, because <the defect>". The evidence must be concrete (a keyword, a scene, a P-ID), never an adjective.

**Step 9. WRITE THE RECORD, THEN PRINT ONE LINE.**
- On Claude with Notion, the QA record is written into the page's Quality properties and a "QA" toggle. Because it goes into the tool call, the check is done in writing without appearing in chat.
- On ChatGPT and Sheets, a compact QA cell goes in the paste block's Quality column.
- Chat shows only the verdict line per piece and one NEXT line per batch.

Internal record (hub; property names in English in both editions):
```
Result: PASS
QA · 2026-W41-N1 · Tier M · round 1/2 · checker: same-context
Score: 9/10 (K2 V2 A1 Au2 C2) · G1 ok G2 ok G3 ok · STANDARD 4/4 critical
Lenses: buyer ok · compliance ok · phone ok · me ok · map ok
Trace: S-2 B-1 P-3 resolved 3/3 · quotes 1/1 exact · claims GREEN
Ceiling: A capped at 1 (proof gate locked)
Weakest: line 4 "most clients…" (range, no n)
Would I post this? Yes, because it names "<K-1>" and Lan's real cancellation call.
Second read: pending → 8/10 PASS (standing 8, lower stands)
Coach outcome: (blank until "posted N1" / edited / "not me")
```

### 2.3 Proposed SKILL.md card (replaces the ~900-character card)

The card would grow to about 1,300 characters EN (≤1,500 VN). A ≤800 / ≤1,000-character task variant drops lenses 1 and 6.
```
SHIP CHECK v2 — silent · once per batch · uncertain = FAIL · never praise
0 PREFLIGHT: Message Map · tier L/M/H · Bank material · H: proof gate/Ledger/A-row/consent → GO|DOWNGRADE|NEEDS YOU
1 WRITE from Bank IDs only; no self-score
2 LINT (final): lengths · avg≤15/max25 · strip hits · 0 hedges hook/claims · tells≤1 · IDs resolve · quotes exact ·
  numbers from P · claim words→record · urgency→Ledger · K×1 rotated · 1 rung/1 belief/CTA=rung/link-fwd · new stem
3 CHECK as a stranger: re-open every ID; Edge K V A Au C + STANDARD; quote the line for any score <2
4 LENSES 1 line each: buyer · compliance · 5-sec phone · sounds like me · Message Map (+DM/call on H)
5 FIX named defects only → re-lint all → re-score · max 2 rounds → else NEEDS YOU (≤1 q/piece)
6 PASS = ≥8, no 0, gates ok, STANDARD critical=2, 0 [NEEDS]. Name ceilings; never waive; never invent.
PRINT: Ready · 9/10 · I'd post this, because <evidence>  |  Needs you: <one question>
```

### 2.4 Making the checker as independent as possible inside one chat

1. **Two phases per reply.** Draft every piece in the batch first, then check them all. Drafting and checking are never interleaved.
2. **A cold-start role switch.** "You did not write these. Forget why they were written. Score only what is on the page, as the coach's most skeptical buyer and a platform reviewer."
3. **A fresh rubric.** The rubric text is placed immediately before scoring:
   - Claude: re-open `edge-rubric` and the format STANDARD block;
   - ChatGPT: re-retrieve the `§CM-EDGE` anchor;
   - tasks: the embedded card.
   This counters rubric drift in long chats.
4. **Restricted inputs.** The draft text, the re-fetched Bank rows, the Message Map and the Voice Card. Not the plan notes or the writer's reasoning.
5. **Re-open sources.**
   - Connected: one Notion query for all cited IDs.
   - Standalone: the mini-bank inside the Brief.
   - Cuts: search the transcript for each PASSAGE's boundaries.
   - Research lines: list 3 V-IDs with links for the coach to re-open (G11).
6. **Evidence rule.** Every 2 names its evidence; every score below 2 quotes the line. A score with no location is removed.
7. **Adversarial goal.** The checker looks for the reason the piece would fail, and names one weakest line even on a PASS.
8. **The lint is final.** The checker cannot pass anything the lint failed. An ID that will not resolve (a Notion read failed, say) is a FAIL, never "probably fine".
9. **No rewriting while checking.** Fixes come afterwards and are limited to the named defects.
10. **Honest labels.** The record says `checker: same-context` and never calls itself independent.
11. **Real fresh contexts:**
    - *Claude Pro:* DROP (weekdays 06:37) adds a **second-read step**. It covers Scripted rows since the last DROP that have QA=PASS and an empty Second Read: all Tier H, plus 1 random Tier M. At most 3 pieces, or 1 when a CUT or catch-up also runs.
      - It re-scores every item from its own source sample, and the lower score stands.
      - On a FAIL it sets QA=FAIL and Needs. If the coach has not edited the page (Notion's Last edited by = the integration), it **prepends** a v2 above v1 and leaves v1 in a toggle.
      - This requires amending the spec rule "scheduled runs never overwrite a non-empty Scripted body" to "never delete; may prepend v2 to an untouched page".
      - The drop reports it in one line.
    - *ChatGPT, Claude Free and Gemini:* for Tier H only, the machine adds at the end of the batch: "Before you post the launch pieces: open a new chat in this Project and paste them with 'Content Machine: second read'." That is one extra message per Tier H batch, not per piece.
12. **Calibration (Phase 2 evals).** Measure the same-context checker against an independent judge. If its scores run high by ≥1 point on average, or PASS/FAIL agreement is below 85%, raise the in-chat PASS bar to 9 or extend the required second read to Tier M.

### 2.5 Honesty rules (shown to the model; enforced by the lint and checker)

- Nothing is invented. A missing fact is `[NEEDS: one question]` (VN `[CẦN BẠN: …]`). Inferences in plans are tagged `[guess]` or `[AI inference]`; in scripts the material is simply not used.
- **Stretched labels are FAIL**:
  - a piece tagged Trustable with no P-ID;
  - process proof presented as a result;
  - coach recall tagged as client words;
  - a composite story not labelled as composite;
  - a paraphrase presented as a quote;
  - "most clients" when the P-rows say 3 of 8 (counts show n);
  - "echo" counted when it was the coach repeating their own keyword;
  - a pattern claimed from fewer than 2 people in 2 places;
  - "saved to your board" before the write returned;
  - "your tasks ran" or "your link works" when the machine did not see it.
- Hedges never cure a claim: "up to", "typically" and "results may vary" each need their own record.
- Blank is not zero. Missing stats read "not supplied". A benchmark is labelled "typical, not yours". Fewer than 10 posts reads "too early to judge".
- Shortfalls are reported, never padded. A missing pillar gets the mini-pillar, not generic filler.

### 2.6 The one line the coach sees (EN / VN)

The verb follows the format: film for video, post for text, send for email.

| State | EN | VN (xưng hô follows the Card; default mình–bạn) |
|---|---|---|
| Pass | `Ready to film · 9/10 · I'd post this, because it uses "<K>" and Lan's real cancellation call.` | `Sẵn sàng quay · 9/10 · Mình sẽ đăng bài này, vì có "<K>" và đúng cảnh chị Lan huỷ lịch.` |
| Pass with a ceiling | `Ready to post · 8/10 (proof capped until your first client result) · I'd post this, because …` | `Sẵn sàng đăng · 8/10 (phần bằng chứng tạm giới hạn tới khi có kết quả khách đầu tiên) · Mình sẽ đăng, vì …` |
| Needs you | `Needs you (1 question) · What did she say, word for word? I won't make it up.` | `Cần bạn (1 câu) · Hôm đó chị ấy nói nguyên văn câu gì? Mình không tự bịa phần này.` |
| Hard stop | `Not writing this line: "3 seats left" isn't a real cap yet. Give me the real number and I'll write it.` | `Câu này mình không viết: "chỉ còn 3 suất" chưa phải giới hạn thật. Bạn cho mình con số thật, mình viết ngay.` |
| Downgrade | `Written as a founding offer: no client results to show yet.` | `Mình viết theo dạng mời khách đầu tiên: chưa có kết quả khách để đưa vào.` |
| Override | `Posted on your call · my check: 6/10 (no clear stance) · logged.` | `Đăng theo quyết định của bạn · mình chấm 6/10 (chưa có quan điểm rõ) · đã ghi lại.` |
| Second read changed it | `Re-checked N2 this morning and fixed one number. New version is on top.` | `Sáng nay mình kiểm lại N2 và sửa một con số. Bản mới nằm trên cùng.` |
| Not checked | `Not checked yet (usage limit) · don't post · say "finish batch".` | `Chưa kiểm xong (hết lượt) · khoan đăng · nhắn "làm tiếp batch".` |

The ID footer the spec currently prints (`Uses S-2 B-1 P-3…`) moves into the hub properties or the paste block.

---

## 3. Token and message budget per output (free tiers)

These are planning estimates to be measured in Phase 2. The message caps are not in the research files except Claude Free's practitioner figure of roughly 15–40 messages per 5 hours; ChatGPT Free's cap and fallback model need verifying in Phase 0.

**Fixed context per scripting reply:** SKILL.md plus ≤4 references plus the Brief, about 16k input tokens (arch §3.3). The Ship Check v2 card adds about 350 tokens.

| Output | Tier | QA tokens per piece (est.) | Extra messages | Free-tier batch per reply |
|---|---|---|---|---|
| DROP (1 idea + 3 hooks, ≤120 words) | L | ~150 | 0 | 1 per day |
| Short, clip or text post (script ~300–450) | M | ~800–1,200 (+~400 if a fix round runs) | 0 | 3 |
| Carousel | M | ~1,000 | 0 | 2–3 |
| Nurture email | M | ~900 | 0 | 3 |
| Pillar guide | M | ~1,200–1,500 | 0 | pillar + N1 + N2 = one Monday reply |
| Cut kit (20–40 min transcript; 4–8k input tokens EN, more in VN) | M | ~2.5–3.5k per kit (PASSAGE checks) | 0 (already 2 replies) | split across 2 replies |
| Offer post, case, ad, sales email, launch P5–P8 | H | ~1,500–2,000 | +1 per Tier H batch (fresh-chat second read; Claude Pro: 0, it is scheduled) | 2 |
| Second read (Claude Pro DROP) | — | ~1,000 per piece, at most 3 per run | 0 (scheduled) | — |
| Season plan or re-plan | plan-level | ~600 (nine-questions coverage, belief chain, mixes, give:ask ≥3:1) | 0 | — |

**Batching rules that protect the coach's limits:**
1. **QA never costs a message.** Every layer runs inside the reply that delivers the draft. Needs-you questions are batched at the end of that reply (≤3), and the coach answers them in the next message they would send anyway.
2. **One Ship Check per batch.** Lint all pieces together, and fetch all cited Bank IDs in one query (within the ≤30 hub calls per run).
3. **The tier decides the depth.** Tier L never runs lenses or the checker.
4. **Fix only the failing pieces;** never regenerate the batch.
5. **Print ≤40 tokens of QA per piece.** Detail goes to Notion through the tool call, or to the paste block's Quality column.
6. **Second reads run off-peak:** in Claude Pro's scheduled DROP, or in one fresh chat per Tier H batch.
7. **Usage cap mid-batch:** each unchecked piece gets QA=Pending and the run is Partial; "finish batch" resumes. A piece is never marked PASS unchecked.
8. **Free tiers:** 3 scripts per reply and 3 per scheduled task. The ChatGPT task carries the ≤800 / ≤1,000-character card variant (lenses 2–5 only), which fits the existing task sub-budget.
9. **The ChatGPT Free fallback model** (after the flagship cap) is the biggest quality risk. The mechanical rules are deliberately model-robust. Phase 0 and 2 should also run the golden personas on the fallback model, and the Tier H fresh-chat second read is there to catch degraded output.

---

## 4. Coach-facing checklists (Layer 2)

Rules:
- Every tick is a yes/no question, answered in one reply ("all yes", or "no on 2"). Nothing is ever a template to fill.
- A "no" means the machine fixes or downgrades the piece. It never lectures.
- Each list fades once it becomes a habit. Tier H lists never fade.

**Before filming / Trước khi quay.** Shown in the BATCH film list for weeks 1–3, then only for Mode C, Tier H pieces, or after a "not me" outcome. A static callout also sits on the Notion Film Queue view.

| EN | VN |
|---|---|
| 1. Say the first line out loud once. Sounds like you? If not, voice-note what you'd say and I'll match it. | 1. Đọc to câu mở đầu một lần. Nghe có giống bạn nói không? Nếu không, gửi voice câu bạn hay nói, mình sửa theo. |
| 2. Every [NEEDS] spot is filled, or tell me to cut it. | 2. Chỗ nào còn [CẦN BẠN] thì điền, hoặc bảo mình cắt đi. |
| 3. You can say the last line without reading it. | 3. Câu chốt cuối bạn nói được mà không cần nhìn. |
| 4. Your keyword is said once, where it's marked. | 4. Từ khoá của bạn được nói đúng một lần, ở chỗ đã đánh dấu. |

**Before posting / Trước khi đăng.** Shown with every Tier H piece. For Tier M, in weeks 1–2 only, then as a single line ("3 ticks in your board"), and it returns after any incident.

| EN | VN |
|---|---|
| 1. Every number and client story in it is true, and that client said yes to being shown. | 1. Mọi con số và câu chuyện khách trong bài đều thật, và khách đã đồng ý cho bạn kể. |
| 2. The comment keyword delivers something real today (link opens, DM reply ready). | 2. Từ khoá comment hôm nay trao được thứ thật (link mở được, tin nhắn inbox đã soạn sẵn). |
| 3. Any "seats left" or deadline line is real, and you'll stick to it. | 3. Dòng "còn X suất" hay hạn chót (nếu có) là thật, và bạn sẽ giữ đúng. |
| 4. Caption line 1 and the on-screen text make the same promise. | 4. Dòng đầu caption và chữ trên màn hình nói cùng một lời hứa. |
| 5. After posting, tell me "posted N1". | 5. Đăng xong nhắn mình "đã đăng N1". |

**Weekly review / Review tuần.** These are REVIEW's fixed input request every Friday, so they replace the stats prompt rather than adding to it.

| EN | VN |
|---|---|
| 1. Stats for posts older than 2 days (4 numbers or a screenshot). | 1. Số liệu các bài đã đăng hơn 2 ngày (4 con số hoặc ảnh chụp màn hình). |
| 2. Calls, sales and "how did you find me?" answers this week. | 2. Tuần này có bao nhiêu cuộc gọi, đơn chốt, và khách trả lời "biết mình từ đâu" thế nào? |
| 3. Did anyone say your words back to you? Paste them. | 3. Có ai nhắc lại đúng chữ của bạn không? Dán vào đây. |
| 4. Anything I wrote this week that didn't sound like you? | 4. Có câu nào mình viết tuần này không giống giọng bạn? |
| 5. Read the 3 bets: "ok", or change one. | 5. Đọc 3 việc cho tuần tới: nhắn "ok", hoặc đổi một việc. |

**Before a launch / Trước khi launch.** Shown on Prep day (T-7) and again in the cart-open morning Launch Desk.

| EN | VN |
|---|---|
| 1. Every seat count, deadline and bonus is real, and you'll close the link or raise the price when you said. | 1. Số suất, hạn chót, quà tặng đều thật; đến hạn bạn đóng link hoặc tăng giá đúng như đã nói. |
| 2. Every result or testimonial has the client's written OK, with the "results vary" line beside it. | 2. Mọi kết quả, feedback đều có khách đồng ý bằng chữ (tin nhắn cũng được), kèm dòng "kết quả cá nhân, không phải cam kết". |
| 3. Walk it on your phone: post → comment → DM → link → pay or book → confirmation. | 3. Tự đi thử trên điện thoại: bài đăng → comment → inbox/Zalo → link → thanh toán hoặc đặt lịch → xác nhận. |
| 4. People who already bought or booked are left out of the next "buy now" message. | 4. Ai đã mua hoặc đã đặt lịch thì bỏ khỏi tin nhắn mời mua tiếp theo. |
| 5. You can really serve the maximum number of buyers. | 5. Bạn thực sự phục vụ được số khách tối đa đó. |

**Monthly re-plan / Lên kế hoạch tháng.** The opening message of "plan next month".

| EN | VN |
|---|---|
| 1. Still the same ONE buyer, problem and offer? If not, say what changed. | 1. Vẫn đúng MỘT kiểu khách, MỘT vấn đề, MỘT gói dịch vụ? Nếu đổi, nói mình nghe đổi gì. |
| 2. Any new client result, or a new OK to share one? | 2. Có kết quả mới của khách, hoặc khách mới đồng ý cho chia sẻ? |
| 3. Any stance you no longer believe, or a format you dread making? | 3. Có quan điểm nào bạn không còn tin, hoặc dạng content nào bạn ngại làm? |
| 4. Anything you've said publicly that's no longer true (client count, results, price)? | 4. Có điều gì bạn từng nói công khai mà giờ không còn đúng (số khách, kết quả, giá)? |
| 5. Price, dates or offer changed? | 5. Giá, lịch hay gói dịch vụ có gì thay đổi? |

On ChatGPT, a "yes" to tick 5 brings back the upkeep line: replace MY-BRAND-BRAIN.md and paste the task texts again if the version stamp changed.

---

## 5. How QA results feed back

### 5.1 Resonance log

**What gets logged** (Character Card LOG, plus the K-row `echo_count`, plus V-rows tagged `echo`):
- phrases the audience said back (weekly tick 3, the DROP capture question);
- "this is me" replies;
- "why me" answers from calls and the booking form;
- unfollows after a stance post, logged as a healthy filter.

**What it changes:**
- Keywords: `echo_count` ≥3 keeps the keyword and makes it spoken; 0 echo after 90 days puts it up for replacement at the Card refresh.
- Stance heat and the Recognition Bank.
- "More" bets.
- Per-pillar calibration once there are ≥20 posts: the median performance ratio of pieces scoring C=2 vs C≤1, and Au=2 vs ≤1, is reported in REVIEW as data. It never lowers the bar.
- The diagnostic's break point sets a **temporary stricter bar.** Example: "not trusted" means A and Au must be 2 on the next 2 weeks' Credible and Trustable pieces.

### 5.2 Honesty ledger for the coach's own claims

This is a "Claims" view over the P-rows, built automatically from Step 2's TRACE on every posted piece. Columns:

`Claim as said | Slot Keys used | P-ID | Substantiated | Consent date + allowed uses | typical-results line | first used | re-check by (90 d, or when the offer changes) | status: live / dated / retired`

- **Monthly re-plan (tick 4)** re-confirms the claims due. A claim that is dated, has expired consent, or no longer fits the offer is withheld from new scripts until re-confirmed.
- **After each launch, the Scarcity Ledger is reconciled.** Did the link close? Was the cap held, with no reopen? If not, urgency lines stay blocked in the next launch until the coach states an enforcement plan.

### 5.3 Machine QA ledger (the port of run contract §8)

Per piece: checker score round 1 and round 2, second-read score, coach outcome (posted as is / edited / rejected / "not me"), and performance ratio. On Claude, an edit is detected when the Notion body changed between Scripted and Posted.

| Trigger | Effect |
|---|---|
| The second read scores a format ≥2 lower, twice in 30 days | That format's next batches load the full edge-rubric plus examples, and the checker must cite evidence for every 2 |
| "Not me" twice for the same pattern | The pattern is added to the Voice Card's banned list |
| The coach reverts the same auto-strip 3 times (for example they really do say "literally") | A personal allowlist entry. Hard stops and G1 polarity limits are never allowlisted; the coach may add limits, never remove them |
| A posted piece causes a complaint, a platform warning or coach regret | An incident row naming the rubric line that should have caught it, plus a personal rule (Hard Limits or the Voice Card) |

The founder sees none of this unless the coach opts in to "send feedback". The export is anonymised Runs and QA rows, which become labelled eval cases and rubric proposals for the quarterly update. It is never automatic, because of privacy and PDPL.

### 5.4 Retire rules

| What | Rule |
|---|---|
| Format | ≤0.5× the trailing median on its primary metric for 4 weeks → retired at the monthly re-plan; monthly tick 3 can also retire it |
| Hook stem | Ratio below 1× after ≥5 uses → out of rotation; at ≥2× → "More" |
| Stance | The coach no longer believes it, a G1 issue, or flat across 3 uses → retired, with the reason in the Card log |
| Keyword | Echo 0 after 90 days, or the coach changes the Message Map → retired at the Card refresh |
| Proof (P-row) | Consent withdrawn, the offer changed, or past its re-check date and not re-confirmed → retired |
| Capture question | Unanswered 3 times → rotated out |
| QA rules | Personal allowlists only (5.3). Hard stops, privacy, G1 and the no-invention rule never retire |

---

## Reconciliations the build must settle

1. **Edge pass bar.** The plan and wf6 say ≥8; arch §8.2 says ship at ≥7. I recommend PASS at ≥8, with 6–7 going to auto-fix and then Needs you. 7 only passes when the shortfall is a recorded ceiling.
2. **"AMBER ships with Needs:"** (arch §8.1/§8.4) is a conditional pass, which the run contract forbids. Recommendation: an open record means a DRAFT. AMBER becomes a type of claim (one that needs a record), not a shipping state.
3. **"Scheduled runs never overwrite a Scripted body"** blocks second-read fixes. Amend to: never delete; prepend v2 only on pages the coach has not edited.
4. **Card budget.** The Ship Check card goes from ~900 to ~1,300 characters EN (≤1,500 VN). A ≤800 / ≤1,000-character task variant is added.
5. **Where the QA procedure lives.** The ≤4-references-per-job cap rules out a separate `qa.md`. The loop lives in SKILL.md, the format STANDARDs in each format file's generated footer, and the second-read steps in `automation.md`.
6. **The coach line replaces the technical footer.** The IDs move into new hub properties (§5.9): QA Result (PASS / FAIL / Pending / Override), Tier, Round, Second Read, Coach Outcome, plus a QA toggle in the page body. Sheets gets the same columns.
7. **Optional deterministic lint script** for the Claude path (code execution is already required at install). Decide in Phase 2 by comparing its catch rate.
8. **Phase 0 additions:** ChatGPT Free's message cap and fallback-model behaviour; whether Claude scheduled tasks can pick a model for the second read; whether Notion's "Last edited by" is readable through the connector.

### Critical Files for Implementation
- /home/user/Content-Machine-1.0/core/ship-check.md (Ship Check v2 card plus the ≤800-character task variant; rendered into SKILL.md, the ChatGPT instructions and every task)
- /home/user/Content-Machine-1.0/core/SKILL.md.tmpl (QA loop, checker separation, verdict-line strings, the second-read command)
- /home/user/Content-Machine-1.0/modules/edge-rubric.md, with /home/user/Content-Machine-1.0/modules/guardrails.md (Edge v2, the claim marks, preflight DOWNGRADE rules, the honesty and stretched-label list)
- /home/user/Content-Machine-1.0/schemas/hub.toml, with /home/user/Content-Machine-1.0/automation/tasks.toml (Quality properties, the Claims view, DROP's second-read step, the prepend-v2 state rule)
- /home/user/Content-Machine-1.0/strings/en.toml and /home/user/Content-Machine-1.0/strings/vn.toml (verdict lines, the five checklists, `[NEEDS]` / `[CẦN BẠN]`)
- Sources to port from: /home/user/ai-native-marketing-agency/agents/_shared/run-contract.md, /home/user/ai-native-marketing-agency/agents/qa/doctrine.md, /home/user/ai-native-marketing-agency/agents/qa/skills/claims-lint/SKILL.md, /tmp/claude-0/-home-user-Content-Machine-1-0/085f5f0b-5883-504d-aefb-4af9a99859d9/scratchpad/research/wf6-character-design.md (§B)