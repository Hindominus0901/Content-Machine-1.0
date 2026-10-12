# MEASURE · v1315-en-thin · EN coldstart-coach (thin play) · v13.15 (HEAD f5e7797, pack 1.3.15)

Run: 20 coach turns, Day 0 through the Brand Card + Week-1 table, then one Monday "next" (N2). Grade: FAIL, **run invalid (pace)**: see the end.

| # | v13.15 fix | Result |
|---|---|---|
| 1 | Thin rule on the Day-0 piece | Not triggered, and that was correct: the dump had one full story (birthday relay → garage → pull-ups), so the reply was **FILM TODAY** (512 words, 5 beats), with no POST TODAY and no story question. **Added by me: beat 5** = 1 of 5 beats = **20%** (14% counting the first and last lines) ✓ ≤30%. To hit 500 words the machine used more of the coach's own lines, not padding. |
| 2 | Health/money line, no cure/guarantee | The exact line "individual result, not a promise" is in the FILM TODAY caption and in the card's proof field. The spoken script and the beat cards use variants ("That's my result, not a promise for yours" / "My result, not a promise"): partial ✓. 0 guarantee/cure words. The brother's unweighed result was never used. |
| 3 | pack_version | `pack_version=1.3.15` in the card box ✓ |
| 4 | One first-line format | 20/20 machine replies open with "◆ Content Machine · …" ✓ |
| 5 | No VN leftovers; EN route | 0 Zalo / chấm / cô hồn ✓. Follow-ups go by DM (DM reply 1/2) and "by text or DM" to 3 dads ✓. The word "WhatsApp" never appears (no list, Instagram buyer). |
| 6 | Keyword once | FILM TODAY caption: comment word "30 MINUTES" once, as the ask (switched to "Message me…" after "quiet"); the season keyword "keep up" once in the caption body, 0 times in the spoken script ✓. N2: "keep up" once in the body, and the ask is a send ✓. Note: "30 minutes" also appears as a topic word (hook, payoff name). |
| 7 | Hooks in a frame | FILM TODAY: "You don't need an hour. You need 30 minutes, 3 times." (belief flip, HOOKS-EN flip 1). N2: "Dads don't have a willpower problem. They have a calendar problem." (belief flip 2). Week table: Myth/Truth (Tue), "If you're…, read this" (Wed), belief flip (Thu). Fri "this one's you" is weak. ✓, but the grader does not recognise belief flips (see below). |
| 8 | Strategy ≤3 replies, each ending on one OK; minutes | 3 strategy replies (157 / 88 / 155 words of talk; limits 160 / 100 / 160), each ending on one OK ✓, plus a 4th short reprint of the ask line after the coach's "comment thing? Feels salesy" (quiet applied at once). **Day-0 piece at minute 22.1** (active), after 14 coach turns. |

## Grader fails: real vs misread
- **pace (invalid run): real, a simulator slip.** I modelled the 2 pasted posts (turn 5) at 0.6 min; the rule is ≥1.0 min. Times were not changed after the grade (that would also make the run invalid). The machine content is not affected.
- **day0_strategy, "why this one" printed in reply 1: real.** The kit prints it only on "why?".
- **day0_strategy, WHAT I FOUND has 1 line (want 2–3): misread.** The kit says "≤3 lines, or what's a guess". With no tool, one guess line is within the kit.
- **I8, "result number for a cold-start persona" on Beat 1 ("I work out 30 minutes…"): misread.** That line is a routine, not a result. The real result line (0 → 8 pull-ups, 35 → 37) is the coach's own record, which is allowed (proof_gate: own story).
- **hook_lab, first line fills no frame: misread / alignment gap.** The EN `HOOK_FRAMES` in graders.py has no belief-flip, "Everyone says…, but" or Myth/Truth frame, though v13.15 adds them to the kit. Strictly, "You don't need X. You need Y" sits in HOOKS-EN, not in §CM-FORMATS 1's list, so the method file and the hook library also disagree.
- **I23, 2 of 6 pieces use a coach phrase (min 50%): partly real.** N2 reworded "you're not lazy, you're booked" to "he's not lazy. he's booked"; the gift and DM boxes carry none. It is a proxy check.
- **day0_timing: mostly persona-driven.** There were 17 session coach turns: the voice-mode detour, the 4 dump sends, brb / ok back and 2 pushbacks. The early win at 4.4 active minutes (max 4) comes from the scripted sound-wave detour plus a 301-word first send.
- Leaks: pass (warn only). The warnings are the coach's own dump/W1/W2 words, plus "Instagram Reels first, the same video" (the kit's platform default; it matches answer-bank wording by coincidence).
