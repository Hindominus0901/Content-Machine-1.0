Ship Check cards (docs/research/wf12-qa-spec.md §2.3). One source, included with {{>ship.…}}:
- ship.kit   → the instruction block and Phone Starter (no hub, no script; the coach's words are the Bank)
- ship.card  → SKILL.md and the L3 skill (hub rows, scripts/ship_lint.py)
- ship.task  → standalone task text (VA tier)
Budgets (platform/targets.toml): card ≤900 EN, task ≤800 EN, NFC characters.

<!-- @section ship.kit -->
SHIP CHECK · silent · every piece · unsure → cut or downgrade · no praise
0 FOCUS: one big idea from the Map · one idea ≤15 words · one belief ("you think X → actually Y") · not a NOT NOW topic
1 WRITE only from what the coach told you. Missing fact → downgrade (process story, founding offer, no seat line) or ask
2 TRUTH: every number, name and quote is theirs; quotes exact; a client result only with the client's OK; urgency only if real
3 STAND-OUT, each 0–2, need ≥8 and no 0: keyword once + one specific · one idea, one belief · proof shown · a detail only they have · a stance someone could disagree with. No hedge in the hook
4 VOICE + BUYER: their tone, rhythm, phrases and audience address, no never-words; a buyer on a phone stops and believes it in 5 s. Fix once
PRINT: a ready piece → the content only. A missing fact → one line "Needs you · <question>". WHY and checks only on "why?"

<!-- @section ship.card -->
SHIP CHECK · silent · once per batch · unsure → cut or downgrade · no praise
0 PRE: slot row + Bank material? Else DOWNGRADE (process story, founding, no seat line); ask only if the piece rests on the missing fact
1 WRITE from Bank IDs; refuse hard stops
2 LINT (Claude: scripts/ship_lint.py, final): digits/names/quotes in cited rows · quotes exact · result claim = P-row Substantiated+consent · urgency from Ledger · keyword ×1 · new hook stem · no hedge in hook · 0 [NEEDS]
3 CHECK after all drafts, cited rows reread. Gates: polarity, truth, voice. Edge 0–2: K keyword+specific · V one idea, one belief · A proof shown · Au only-you detail · C a stance. Format checks. Unsure = fail: 5-sec phone, sounds like Card, buyer believes it
4 FIX named defects once. Ready = gates, Edge ≥8, no 0, format yes
PRINT under each: Ready to <verb> · I'd post it: <Bank fact> | Needs you: <1 question/reply>

<!-- @section ship.task -->
SHIP CHECK (task) · silent · unsure → cut or downgrade · never guess or praise
1 Write only from Brief IDs; refuse fake scarcity, invented proof, guarantees, attacks on people
2 Every digit/name/quote sits in a cited Brief row; quotes exact; result claim only from a P-row marked Substantiated+consent, else the process story; urgency only from the Ledger
3 Keyword once · hook stem not in recent_hook_stems · no hedge in hook · Edge none at 0: keyword+specific, one idea, proof shown, only-you detail, a stance
4 Missing fact → [NEEDS: one question] and the piece is a Draft. Never ask in a task; the run report carries 1 question
PRINT under each: Ready to <verb> · I'd post it: <Brief fact> | Draft · needs: <question>
