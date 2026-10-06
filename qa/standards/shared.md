# Shared script gate and Edge v2 (`shared`)

Build-only rubric (wf12-qa-spec §3.1). Never shipped: lint E153 keeps `qa/` out of every zip. It is the G3 judge rubric for every script and the source of `standard = "shared"` eval cases.
Sources, in order: wf12-qa-spec §0, §2, §3.1 (final, wins) · wf12-qa-standards S0/SG (draft) · wf6 §B Edge Check v2 and §6 borrowed-attractor detector · wf13 §4, §6 (SG-copy) · DECISIONS (F1).

## Purpose

One question: would this script embarrass the coach, or cost a buyer's trust, if it went out as it is, under the coach's name, tomorrow? This standard checks truth, safety and edge for every script. Every format standard is scored on top of it and never restates its items.

## Scope

- **Artifact:** every script of 40 words EN / 60 tiếng VN or more: native short, text post, carousel, email/Zalo message, pillar guide, cut-kit asset, offer post, ad, launch asset.
- **Output class:** Script, normal and Script, claims (spec §2.1). Shorter pieces use `micro.md`; Ideas use Edge-lite; structured artifacts use their own standard.
- **SG-copy** applies on the default path: any remix the machine started from a post the coach likes (wf13 §4). N/A when the piece has no source post.

## Items

Gates are pass/fail: 2 = clear, 0 = not clear, there is no 1. Code gates are decided by the `ship_lint.py` / `graders.py` output, which is final and never re-argued.

| ID | Item | 0 | 1 | 2 | Critical |
|---|---|---|---|---|---|
| SG1 | Trace | Any number, name, quote or result not found in a cited row; an ID that does not resolve; a quote that does not match its row or runs over 15 words EN / 25 tiếng VN; a stranger's words printed as a quote or testimonial; a seeded or commenter name; a liked post's number, result or story used as the coach's | — | Every number, name, quote and result cites a resolving Bank ID. Numbers come only from P-rows (`allowed_numbers`). Quotes are verbatim from V or O rows; strangers are paraphrased; clients are quoted only with consent for this use. Inference is tagged `[guess]` | yes · hard gate |
| SG2 | Claims (AMBER = a record is needed) | Any RED: a guaranteed income, health or other outcome; cure or treat; an invented or AI testimonial, result, quote or statistic. Or: an AMBER claim printed with no record; urgency with no 4-yes Ledger row; a hard ask while the proof gate is locked; "up to", "typically" or "results may vary" used to cover an unsupported claim | — | Every AMBER claim (result number, testimonial, health or fitness outcome, income) is cleared by its P-row (Substantiated = Y, consent covers this use, Re-check by not passed), or was downgraded quietly (process story, founding framing, the coach's own side). Income carries the context block and "individual result, not a promise". Guarantees cover the process only. Every urgency line maps to a Ledger row with 4 yeses | yes · hard gate |
| SG3 | Polarity | On the default path: a named person, brand, competitor or KOL. At any time: an identity group; punching down at beginners or clients; outrage with no teaching underneath; heat above 3; an attack on a private individual or protected group | — | The target is an idea, practice, standard or system; people get warmth. Yellow-zone targets are reframed (peers as a category, anonymised client patterns, platforms, the past self). Heat ≤3. A named comparison appears only on the coach's explicit request, with the dated compare note and a logged Override (F1) | yes · hard gate |
| SG-copy | Distance (remix the machine started) | Fewer than 2 of topic, stance, format and platform differ; a run of 6 EN words / 8 tiếng VN from the source (`locales/<lang>/stock-phrases.txt` exempt); the source's point order mirrored; the same-feed test fails; a translation offered for posting; a coach-requested copy, translation or comparison with no dated note | — | All DISTANCE tests pass: ≥2 of the four differ, no run, no mirrored order, someone who follows both accounts would not call it the same post. The source's numbers and coined terms are absent. On an explicit coach request to copy, translate or compare, DISTANCE is skipped and the piece carries ONE dated note (`liked.copy_note` / `liked.compare_note`) with an Override logged | yes · default path |
| SG4 | Voice lint | Lint still fails after the fix round | — | Lint passes (rules below) | code gate |
| SG5 | Edge v2 | ≤5/10, any pillar at 0, or borrowed-attractor-only | 6–7/10 with no pillar at 0, or a stance format with C = 1 | ≥8/10, no pillar at 0. Stance formats (F1, F4, F6, F9, F11, F13) also have C = 2 | yes |
| SG6 | Ladder | No Map pillar or B-ID; a topic on the NOT NOW list; two ideas; the keyword missing from the words (only in the ask) or used twice outside the ask; an ask above the rung; a keyword CTA with no A-row | One weak link: no link-forward, or the CTA one rung off | One Map pillar (not on NOT NOW), one idea, one belief (B-ID), the CTA for the rung, a link-forward. The keyword appears once in the words, plus the ask (the ask is not counted), in a rotated placement: hook, on-screen text, spoken payoff, caption line 1, or a long post's or carousel's opening. A keyword CTA points at a real A-row; with none, the CTA is follow or save and a lead magnet is proposed | yes |
| SG7 | Variation | Lint fails | — | Hook stem not in the last 10 pieces / `recent_hook_stems`; the same structure at most twice in a row; keyword placement differs from the last piece (connected path only; standalone uses date rotation plus `recent_hook_stems`, spec §6) | code gate |
| SG8 | Read-aloud (feeds Au) | Reads as someone else, or as AI | 1–2 lines the coach would not say aloud | The coach would say every line, word for word, to a buyer tomorrow; it matches the Card voice samples | no: SG8 < 2 caps Au at 1; SG8 = 0 sets Au to 0 |

**CTA ladder (SG6):** Admirable = follow · Likable = send to a friend · Credible = save, or comment the keyword · Trustable = DM the keyword, or book.

**SG4 voice-lint rules:** hook ≤12 words EN / ≈18 tiếng VN · 0 hedges in the hook and in claim lines; body ≤1 per 100 words unless odds or a condition follow · average sentence ≤15 words, none over 25, ≥1 punch line ≤5 words · ≤1 AI tell · ≤1 "not X but Y" · no throat-clearing · questions only in the CTA · no recap ending. Strip lists: `locales/<lang>/banned-tells.txt` (wf6 H1–H9 / V1–V9) plus the Card's personal banned list. **Sounds like the coach** (judge lens, wf14 §5): the piece matches the Brand Card's Voice Card fields `tone`, `rhythm` (written voice for posts, spoken for scripts), `phrases` / `openers_closers` where natural and `audience_address` (VN: the coach-to-audience pair, kept apart from the machine-to-coach pair); 0 `never_say` hits; no jargon or English the coach doesn't use (`code_mix`).

### SG5 pillars (Edge v2, 0–2 each)

| Pillar | 0 | 1 | 2 |
|---|---|---|---|
| K Signature | Generic category language; the problem in expert jargon the audience doesn't use | One signature term bolted on (CTA or hashtag only), or a coined term without the audience's word for the problem | A client verbatim phrase (2+ mentions) or coined term in the hook or punch line, AND the problem in the audience's words; ≤2 coined terms in the piece |
| V Value | No takeaway, a platitude, or 3+ competing ideas | A takeaway that is generic, not actionable, or below line 3 | One idea in ≤15 words, visible by line 2, plus a step for today (practical) or a "what I stand for / who this is for" line (identity; Likable F3, F7, F8, F10, F14) |
| A Authority | A claim with no proof, an invented stat, a guarantee, or résumé-only credibility | Proof that is generic ("helped hundreds"), far from its claim or one-sided; or an outcome stated as certain | Each main claim has a trust cue (P-row number, client scene, receipt) within 2 sentences; outcomes as ranges or conditions (values absolute, own patterns quantified, others' outcomes as ranges); ≥1 cost, limit or not-for line |
| Au Authenticity | Fails the swap test (any coach could post it); 3+ AI tells; voice unlike the Card samples | Sanitised detail; a story with no cost or flaw; 1–2 AI tells | A detail only this coach could write (scene, date, quirk, ritual, verbatim phrase); cadence matches the Card samples; stories carry a cost or flaw; 0 AI tells |
| C Character | No stance; a borrowed-attractor-only hook; an attack on people | A generic stance (no Card anchor), hedged, the opposing view not refuted, or no boundary | An owned stance that passes 3D (Disagree, Defend, Demonstrate), anchored to a Card trait, principle, enemy or hill; definitive (no hedge in the hook, present tense, answer first); refutes the old view with a reason; a boundary or not-for line. Likable: a stated choice with its value counts as a stance |

- **Borrowed-attractor detector** (flex, freebie, résumé; wf6 §6): trigger in the hook or lines 1–3, no why signal in lines 1–3, and the removal test fails = X-only: C = 0, Au ≤1, FAIL whatever the total. Why at line 4 or later = X-led: C ≤1. As evidence or as the CTA: fine.
- **Generic mode** (no Character Card): Au and C capped at 1, so a stance format cannot pass.

## Build pass rule

- **Shared rule (every standard):** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; all hard gates clear; no conditional pass; uncertain = 0.
- **Here:** SG1, SG2, SG3 and SG-copy (when it applies) clear; SG4 and SG7 clear in the lint output; SG5 = 2; SG6 = 2.
- The scored total is Edge (K + V + A + Au + C, max 10), so the 0.8 rule reads Edge ≥8, with no pillar at 0 and C = 2 on stance formats. Gates are never added to the total.
- Every score cites its line and rule; a score below 2 quotes the offending line. The judge re-traces every ID and number at source.
- A recorded ceiling (generic mode; Authority while the proof gate is locked) is named in the verdict and never lowers the bar.
- A piece about a result with no record is correctly a Draft with `[NEEDS: …]`: SG2 scores what is printed, and the piece never counts as Ready (I18).
- Release bar (G3) sits on top: Edge average ≥8 per persona and edition, no piece below 7, no 0.

## Hard gates

No override, no median (House Rules §12, spec G4). Any hit fails the piece whatever the score:
- fake scarcity;
- invented or AI-generated testimonials, results, quotes or statistics;
- income or health guarantees, and unsubstantiated income or health claims; cure or treat claims;
- someone else's results, testimonials, numbers or story presented as the coach's own (F1);
- an AI likeness or voice of anyone else; impersonating people or brands;
- attacks on protected groups or private individuals;
- clone-account seeding; asking people to post phone numbers publicly.

**Never blocked** (one dated note at most; blocking or silently rewriting one fails I14 and the 0-false-block bar):
- comment keywords, thresholds ("đủ 100 comment"), "chấm" and coded CTAs;
- bold stances on ideas; flexes or freebies used as proof or as the CTA;
- copying, translating or a named comparison on the coach's explicit request (F1).

## Runtime check shipped

Ships as the Ship Check card (`core/{en,vn}/ship-check.md`, spec §2.3; ≤900 chars EN / ≤1,000 VN), not as `format-checks.toml` lines. The VN card is fully Vietnamese (PLAN reconciliation 1 supersedes the spec's English-card note). SG-copy adds 0 to the card: `shiplint.py --source` runs it on Claude; ChatGPT does a manual presence check, recorded `lint: manual`. The card's yes/no content:

| # | EN | VN |
|---|---|---|
| 1 | Does every digit, name and quote sit in a cited row, quotes exact? | Mọi con số, tên và trích dẫn đều có trong dòng đã dẫn, trích nguyên văn? |
| 2 | Is every result claim backed by a P-row (Substantiated + consent) and every urgency line by the Ledger, else downgraded? | Mọi kết quả đều có dòng P (đã kiểm chứng + được đồng ý), mọi câu khan hiếm đều có trong Ledger; nếu không thì hạ cấp? |
| 3 | Does it push on an idea or practice, never on a person or group? | Chỉ phản bác ý tưởng, cách làm; không nhắm vào người hay nhóm người? |
| 4 | Edge ≥8, none at 0: keyword + specific, one idea, proof shown, only-you detail, a stance? | Edge ≥8, không trụ nào 0: từ khoá + cụ thể, một ý, có bằng chứng, chi tiết chỉ bạn có, một quan điểm? |
| 5 | Keyword once in the words (plus the ask), new hook stem, no hedge in the hook, 0 open brackets? | Từ khoá 1 lần trong bài (cộng lời mời), hook mới, không rào đón trong hook, không còn ngoặc [CẦN BẠN]? |

## VN note

- Hook ≈18 tiếng; the DISTANCE run is 8 tiếng; the quote cap is 25 tiếng (all counted after NFC).
- One xưng hô pair, 100% consistent (I15); no English outside the allowlist.
- Until VN counsel signs off, every result claim needs a record (spec §6, §8.4) and carries "kết quả cá nhân, không phải cam kết". Superlatives (nhất, duy nhất, số 1, tốt nhất) need a survey or award (Circular 12/2026). "#QuảngCáo" / "Được tài trợ" when someone else promotes the offer.
- SG3: politics and the state, regions (Bắc/Nam) and family duty are hard limits; apply the face test (would you say it to an anh/chị đi trước?). A VN stance stitch (F13) never shows or names the creator.
- C: "Nhận trước, đứng vững sau" (admit your own mistake, then hold the stance) counts as definitive. Heat one notch lower for B2B and older audiences; the wording stays definitive.
- SG4: keep relationship particles (nhé, nha, ạ); cut permission-seeking ones (xin phép, đúng không ạ). Income reads as "khoe" easily: flipped-paycheck pieces use a range or no number.

## Calibration (fictional coaches)

**PASS.** EN, a bookkeeping coach for solo plumbers. F1 stance short, Admirable, pillar 2, B3. Verbal hook: "Your accountant isn't slow. Your shoebox is." Body: the old way (the April dump) refuted, the Friday rule, proof "212 client quarters (P-02)", boundary "If you only invoice twice a year, skip this." Keyword "Friday shoebox" in caption line 1; CTA: "Follow. Part 2 on Friday: the sheet itself." Edge K2 V2 A1 Au2 C2 = 9/10 (A: the proof sits 3 sentences from its claim). SG1–SG3 clear, SG-copy N/A, SG6 2, lint clean. **Result: PASS.**

**FAIL.** VN, a coach for small flower-shop owners (mình–bạn). A remix the machine started from a post the coach liked. Source line: "Hoa đẹp chưa đủ, khách cần một lý do để quay lại mỗi tuần." Remix line: "Hoa đẹp chưa đủ, khách cần một lý do để quay lại." That is a 12-tiếng run from the source. SG-copy = 0. Edge 8/10 does not matter. **Result: FAIL** (SG-copy: "Hoa đẹp chưa đủ, khách cần một lý do để quay lại").
