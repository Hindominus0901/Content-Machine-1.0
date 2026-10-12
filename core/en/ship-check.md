Ship Check cards (docs/research/wf12-qa-spec.md §2.3). One source, included with {{>ship.…}}:
- ship.kit   → the instruction block and Phone Starter (no hub, no script; the coach's words are the Bank)
- ship.card  → SKILL.md and the L3 skill (hub rows, scripts/ship_lint.py)
- ship.task  → standalone task text (VA tier)
Budgets (platform/targets.toml): card ≤900 EN, task ≤800 EN, NFC characters.
Retest FT2 (7 Oct, qa/runs/retest-ft2/review.md §8 items 1, 2): ship.kit 3 runs the hook check on every hook and caption line 1 (no hedge, flat claim or maxim; on-screen ≠ line 1 reworded); 2 TRUTH covers a client action or thought. Paid by dropping "a client result only with the client's OK; urgency only if real" (the CLAIMS line right after the card says both, as VN did in FT1). ship.kit 897 → 899.

Strategy first (founder, 7 Oct night): ship.kit 0 FOCUS names one pillar and one type; 1 FACTS merges WRITE and TRUTH and lets topics and teaching come from the machine's expertise (only facts must be theirs); 3 drops "in 5 s" (lengths are words, never seconds). ship.card "5-sec phone" → "line-1 stop". ship.kit 899 → 879.

v13.10 (founder 11 Oct): 0 the CTA keyword once (topic uses free); 1 a claim about their clients or market is a fact, quotes keep their speaker, stories not padded; 2 every hook on a §CM-FORMATS 1 frame (kit); 3 each piece, long ones too; PRINT "Added by me: ¶2, ¶5" by paragraph (phone spells it out, kit → §CM-EDGE). ship.kit 895 → 899.

v13.13 (12 Oct, qa/runs/v1312): 1 SOURCE names generalizations and speeds ("most…", "10 min, done") as facts; 2 (kit) the frame covers the email subject and slide 1, no client name, on-screen <2 title words. Paid by "WHY only on why?" (§CM-EDGE), "(each piece, long ones too)" (§CM-HUMANIZE 2), shorter wording. ship.kit 899 → 897.

v13.16 (12 Oct, founder "one idea is enough"): 1 drops "no padding" (it read as a length cap) and lists only "teaching from none of these"; PRINT (phone) lists paragraphs with a line from none of their sources. ship.kit 900 → 890.

<!-- @section ship.kit -->
SHIP CHECK · silent · every piece · unsure → cut or downgrade
0 FOCUS: one pillar, one type · one idea ≤15 words · one belief (X → actually Y) · not NOT NOW · {{#if phone}}comment word once, in the ask; Season keyword (CONVERT) once, body or caption{{else}}keywords: §CM-CTA-KIT 1{{/if}}
1 SOURCE: each scene, number, name, quote, result, client act, thought, cause → effect, their past, claim on clients, market ("most…", "10 min, done"): from their words, card, a kept research line; quotes exact, same speaker; else cut. Teaching from none of these: listed
2 STAND-OUT ≥8, no 0{{#if phone}}: a specific · one idea, one belief · proof shown · an only-them detail · a disputable stance{{else}} (§CM-EDGE){{/if}}. Every hook, caption line 1: {{#if phone}}no hedge, flat claim or maxim; on-screen adds one thing, not line 1 again{{else}}a §CM-FORMATS 1 frame (subject, slide 1), no client name; on-screen: <2 title words{{/if}}
3 VOICE + BUYER: tone, rhythm, phrases (in ≥half the pieces; each ≤1×), address, no never-words; a buyer stops at line 1, believes it. Fix once
PRINT: the piece; under it "Added by me: ¶2, ¶5"{{#if phone}}: every paragraph (beat, slide; counted from the top) with a line from none of their sources; none: no line{{else}} (§CM-EDGE){{/if}}. Missing fact, hard stop → "Needs you · <one question>"

<!-- @section ship.card -->
SHIP CHECK · silent · once per batch · unsure → cut or downgrade · no praise
0 PRE: slot row + Bank material? Else DOWNGRADE (process story, founding, no seat line); ask only if the piece rests on the missing fact
1 WRITE from Bank IDs; refuse hard stops
2 LINT (Claude: scripts/ship_lint.py last): digits/names/quotes in cited rows · quotes exact · result claim = P-row Substantiated+consent · urgency from Ledger · keyword ×1 + ask · new hook stem · no hedge in hook · 0 [NEEDS]
3 CHECK after all drafts, cited rows reread. Gates: polarity, truth, voice. Edge 0–2: K keyword+specific · V one idea, one belief · A proof shown · Au only-you detail · C a stance. Format checks. Unsure = fail: line-1 stop, sounds like Card, buyer believes it
4 FIX named defects once. Ready = gates, Edge ≥8, no 0, format yes
PRINT under each: Ready to <verb> · I'd post it: <Bank fact> | Needs you: <1 question/reply>

<!-- @section ship.task -->
SHIP CHECK (task) · silent · unsure → cut or downgrade · never guess or praise
1 Write only from Brief IDs; refuse fake scarcity, invented proof, guarantees, attacks on people
2 Every digit/name/quote sits in a cited Brief row; quotes exact; result claim only from a P-row marked Substantiated+consent, else the process story; urgency only from the Ledger
3 Keyword once + the ask · hook stem not in recent_hook_stems · no hedge in hook · Edge none at 0: keyword+specific, one idea, proof shown, only-you detail, a stance
4 Missing fact → [NEEDS: one question] and the piece is a Draft. Never ask in a task; the run report carries 1 question
PRINT under each: Ready to <verb> · I'd post it: <Brief fact> | Draft · needs: <question>
