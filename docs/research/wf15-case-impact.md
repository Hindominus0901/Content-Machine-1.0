# wf15 case impact: eval cases that contradict the 6 Oct rules

**For:** the later case-rewrite pass (EN + VN). **Written by:** the integrator of the wf14/wf15 module pass, 6 Oct 2026. Producers never edit their own module's cases, so this file lists what to change; it changes no case itself.

**Rules the cases must now match:** `docs/research/wf15-simple-surface-spec.md` §1-§3 and `wf14-voice-language-spec.md` §2, as built in `core/en/start-block.md`, `core/en/ship-check.md` (`ship.kit` PRINT line) and the EN modules (`§CM-SETUP`, `§CM-MAP`, `§CM-CARD`, `§CM-TODAY`, `§CM-EDGE` "WHAT PRINTS"). Graders already follow them (`evals/graders.py` I3, `day0_timing`, `map_lines`; `evals/acceptance.toml` [day0], [week], [voice]).

**How the list was made:** every `evals/cases/*.toml` was parsed and its positive assertions (`contains`, `regex`) searched for the WHY prefix (`WHY THIS GETS CLIENTS` / `VÌ SAO RA KHÁCH`), `✓ Checked:` / `✓ Đã kiểm:`, `Ready to` / `Sẵn sàng`, `written as` / `viết dạng`, the Draft and Override lines, the ticks, the 7-line check labels and inventory, the old Map labels, the stop point ("stop here", "That's today done", "say 'next' for your Week 1", VN equivalents), the old promise and budgets; then `context`, `title` and `notes` for the old flow. A hit on a turn that is "why?" or a check of the coach's own draft is not a contradiction. Day-0, Map and Brand Card cases were read one by one; the rest were classified by rule and spot-checked.

## Not contradictions (leave as they are)

- `not_contains` / `not_regex` that forbid a WHY, Checked or Ready line: they now hold by default.
- One "Needs you ·" line (`verdict.needs`), hard stops (`verdict.hardstop`, `verdict = "Hard stop"`), the dated notes (`liked.copy_note`, `liked.compare_note`, `cta.platform_note`, `cta.by_hand`) and "Spammy?" → `cta.not_pushy` (convert.en.008).
- A check the coach asked for on their own draft ("is it ok to post?", "edge check", "đăng được chưa"): one Ready or Draft line still prints (edge-rubric.en.004, en.012, vn.004, vn.005, vn.026; router.en.034, vn.038).
- "why?" turns asserting `Result: PASS|FAIL` and the record (edge-rubric.en.003, vn.003; router.en.062, vn.072).
- Multi-income wording ("You earn from N things", "ONE buyer", "which pays the bills"; VN "nguồn thu", "MỘT kiểu khách", "nguồn nào nuôi"): kept in `setup.multi_income`.
- "post anyway" Override lines: valid while `verdict.override` keeps its text (rule R17, listed below for watching).

## Rewrite rules

| Rule | What the case asserts now | Needed change |
|---|---|---|
| R1 | Visible WHY line | Drop the WHY assertion (`WHY THIS GETS CLIENTS` / `VÌ SAO RA KHÁCH`) and add it to `not_contains` for that reply. Where the belief shift itself is the point, add a follow-up turn "why?" ("tại sao?") that asserts it: the WHY line is stored with every piece and printed only then (wf15 §2, plan.kit-week 5). |
| R2 | Visible ✓ Checked line | Move the `✓ Checked:` / `✓ Đã kiểm:` assertion to a "why?" follow-up; under the piece add `not_regex` `(?m)^\W*✓ (Checked\|Đã kiểm):`. Content the line used to name (her story, keyword once) is asserted in the piece body. |
| R3 | Ready / written-as line under a finished piece | A Ready or downgraded piece prints only its content. Assert no `Ready to …` / `Sẵn sàng …` line; the evidence and the downgrade ("written as …") show on "why?" (§CM-EDGE). |
| R4 | Status line used as the "a piece was delivered" detector | Regexes like `(Ready to (film\|post\|send) ·\|✓ Checked:\|Needs you ·\|Draft ·)` fail on a Ready piece, which now has no status line. Replace them with a piece detector (a fenced copy box, an `N\d ·` label or a FORMAT title) and, where the piece should be Ready, a `not_regex` for any status line. Upper-bound regexes (`{4}` repeats) keep working. |
| R5 | Visible "Draft ·" on a machine-written piece | A fixable Draft is fixed once, silently; if still not Ready it becomes one "Needs you" line or runs downgraded. Only the coach's own draft checked on request ("ok to post?", "edge check") still prints a Draft line. |
| R6 | "Draft · waiting on one fact" (verdict.draft_queued) | Gone. One "Needs you" line per reply, for the soonest piece; later pieces run downgraded silently (as "skip"). |
| R7 | Override line on an F1 request (copy / translate / compare) | F1 prints only its one dated note (`liked.copy_note` / `liked.compare_note`). The Override is logged, shown on "why?". Replace the `Posted on your call` / `ready to post` / `Đăng theo quyết định` assertion with a `not_regex` for it; the `verdict = "Override"` field stays as hidden state. |
| R8 | liked.evidence line under a version | "Ready to … · I'd post it: their shape, your …; nothing copied" moves to "why?". Under the version: nothing, or the one hard-stop line. |
| R9 | Ticks and FILM TODAY extras | Ticks (`tick.client_ok`, `tick.keyword`, `tick.cap`) show only on "why?". FILM TODAY ends with the ask "(quieter: say 'quiet')" and `film.now_or_text` ("Film it now, or post the caption as text." / "Quay luôn bây giờ, hoặc đăng caption dạng bài chữ cũng được."); no "isn't pushy", "out loud", "keyword is in", "no risky claims" line. |
| R10 | 7-line check screen and inventory | No check screen and no inventory ("You know a lot… 6 months of content… nothing thrown away"). After "done": only the facts it could not hear, at most 3, one per message, each "My guess: … Right?" (`setup.guess`, `setup.guess_no_result`, `setup.multi_income`). Old way, your way, who and line 7 are never asked. |
| R11 | Old Map screen | The Map is 4 lines: `KNOWN FOR:` · `3 TOPICS:` · `YOUR WORD:` · `YOUR VOICE:` (VN `ĐƯỢC BIẾT ĐẾN VÌ:` · `3 CHỦ ĐỀ:` · `TỪ KHOÁ CỦA …:` · `GIỌNG CỦA …:`) + `map.ok`. ONE MESSAGE / 3 BIG IDEAS / OFFER / "Why this one" / NOT NOW / "Nothing you know is wasted" are not shown; why-this-one, the root cause and NOT NOW with reasons print on "why?" (§CM-MAP). |
| R12 | Trigger turn answers a question Day 0 no longer asks | Platform, list size, talk day, delivery and hours are guessed from the dump and named once above Week 1 (`setup.plan_guess`); check-line fixes ("fix 3", "sửa 4") no longer exist. Re-anchor the case on the last missing-fact answer, or on "done" when nothing is missing. |
| R13 | Stop point, card before Week 1, wrap-up | No stop point. After FILM TODAY any coach message gets all of Week 1 (a question in it gets a one-line answer first); then the Brand Card + `card.save_line` + NEXT ("Film today's video. Tomorrow: …"), with the reminder offer. A stop ("later") before the card prints card + save line at once and Week 1 waits for "next". No 3-line wrap-up. |
| R14 | Old Day-0 promise and budgets | Promise: "Today, about 25 min: 1) Talk 5–10 min about your work. 2) I find the ONE thing you'll be known for. 3) You get a video to film today and your first week." Budgets (acceptance [day0]): Map ≤6 EN / ≤7 VN coach turns, film-ready ≤20 min, ≤10 coach turns. |
| R15 | Brand Card visible part | Top = 3 lines, ≤500 chars: the title · `WHAT YOU SAY:` message · 3 topics · "keyword" · `HOW YOU SAY IT:` tone · rhythm · phrases · to them: address (VN `NÓI GÌ:` / `NÓI THẾ NÀO:`). Offer, week / talk day and NOT NOW are machine-block fields. |
| R16 | `verdict = "Ready"` / `"Ready-downgraded"` with no text assertion | The field is hidden state now. Add a `not_regex` for a status line under the piece and, if the state matters, a "why?" follow-up asserting `verdict.ready` / `verdict.ready_downgraded`. |
| R17 | "post anyway" Override line wording (watch) | Still valid: the one Override line prints, from `verdict.override` ("Posted on your call · my concern: {defect} · logged."). wf15 §2 words it "Posted on your call · noted."; if the strings owner adopts that, these `my concern` / `mình lưu ý` assertions change. |
| R18 | Early-win wording | The early win is "Got it. 3 lines you just said that are worth money: 1 … 2 … 3 …. Keep going, or say 'done'." The scripted "Line 2 is a post as it stands" and "You haven't told me {gap}" are gone (a one-line jogger stays). |
| CTX | Context or notes only | The assertions still hold; the `context` / `notes` describe the old flow (stop point, 7-line check, line 7, old budgets). Update the wording in the rewrite pass. |

## Cases by module

`Rule` lists every rule that applies; `Needed change` names the case-specific part (the assertion to drop or move, or the new trigger). An empty change cell means the rule text alone says it.

### brain.en (19)

| Case | Rule | Needed change |
|---|---|---|
| brain.en.001 | R13, R15 | Trigger: Day 0's last reply (after Week 1). Replace `\A[\s\S]{0,1400}for the machine` with a window measured from the card title: top ≤500 chars (3 lines), then the machine heading. Notes: visible ≤500, not 900. |
| brain.en.002 | R13 | Context/trigger: the card prints in Day 0's last reply, after Week 1 (no stop point). Field assertions hold; `offer` and `week` are machine-block fields now. |
| brain.en.003 | R15 | Offer ($2,400) and talk day / Friday leave the top. Assert `WHAT YOU SAY:` (message · 3 topics · "CHAPTER") and `HOW YOU SAY IT:`; $2,400 and talk_day in the machine block. |
| brain.en.004 | R13 | Context/trigger: the card prints in Day 0's last reply, after Week 1 (no stop point). Field assertions hold; `offer` and `week` are machine-block fields now. |
| brain.en.005 | R13 | Context/trigger: the card prints in Day 0's last reply, after Week 1 (no stop point). Field assertions hold; `offer` and `week` are machine-block fields now. |
| brain.en.006 | R13 | Context/trigger: the card prints in Day 0's last reply, after Week 1 (no stop point). Field assertions hold; `offer` and `week` are machine-block fields now. |
| brain.en.007 | R13 | Context/trigger: the card prints in Day 0's last reply, after Week 1 (no stop point). Field assertions hold; `offer` and `week` are machine-block fields now. |
| brain.en.008 | R13 | Context/trigger: the card prints in Day 0's last reply, after Week 1 (no stop point). Field assertions hold; `offer` and `week` are machine-block fields now. |
| brain.en.009 | R12, R13 | 'I'm not filming today…' now gets Week 1; the card follows. talk_day Mon and list 900 were line-7 answers: now guessed from the dump, still assertable in the machine block. |
| brain.en.010 | R13 | Context/trigger: the card prints in Day 0's last reply, after Week 1 (no stop point). Field assertions hold; `offer` and `week` are machine-block fields now. |
| brain.en.011 | R13 | Context/trigger: the card prints in Day 0's last reply, after Week 1 (no stop point). Field assertions hold; `offer` and `week` are machine-block fields now. |
| brain.en.012 | R13 | Context/trigger: the card prints in Day 0's last reply, after Week 1 (no stop point). Field assertions hold; `offer` and `week` are machine-block fields now. |
| brain.en.013 | R4 | R4: `(Ready to (film\|post\|send) ·\|✓ Checked:\|Needs you ·\|Draft ·)` |
| brain.en.015 | R4 | R4: `(Ready to (film\|post\|send) ·\|✓ Checked:\|Needs you ·\|Draft ·)` |
| brain.en.016 | R4 | R4: `(Ready to (film\|post\|send) ·\|✓ Checked:\|Needs you ·\|Draft ·)` |
| brain.en.018 | R4 | R4: `(Ready to (film\|post\|send) ·\|✓ Checked:\|Needs you ·\|Draft ·)` |
| brain.en.019 | R4 | R4: `(Ready to (film\|post\|send) ·\|✓ Checked:\|Needs you ·\|Draft ·)` |
| brain.en.020 | R4 | R4: `(Ready to (film\|post\|send) ·\|✓ Checked:\|Needs you ·\|Draft ·)` |
| brain.en.023 | CTX |  |

### character.en (6)

| Case | Rule | Needed change |
|---|---|---|
| character.en.001 | CTX |  |
| character.en.002 | R2 | R2: `(?im)^\W*✓ Checked:[^\n]*(birthday\|relay\|so slow\|grandpa\|kitchen fl…` |
| character.en.003 | CTX |  |
| character.en.004 | CTX |  |
| character.en.005 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |
| character.en.026 | CTX |  |

### convert.en (8)

| Case | Rule | Needed change |
|---|---|---|
| convert.en.001 | CTX |  |
| convert.en.002 | CTX |  |
| convert.en.011 | R1 | R1: `WHY THIS GETS CLIENTS` |
| convert.en.013 | R1 | R1: `WHY THIS GETS CLIENTS` |
| convert.en.014 | R1 | R1: `WHY THIS GETS CLIENTS` |
| convert.en.016 | R9 | The `tick.cap` regex (`real … you'll keep it`) moves to a 'why?' follow-up; the plain cap line in the post stays. |
| convert.en.017 | R3 | R3: `Ready to post · written as` |
| convert.en.043 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |

### edge-rubric.en (17)

| Case | Rule | Needed change |
|---|---|---|
| edge-rubric.en.001 | R4 | R4: `(?m)^\W*(?:Ready to (?:film\|post) · I(?:'\|’)d post it:\|Ready to (?:…` |
| edge-rubric.en.005 | R4 | R4: `(?m)^\W*(?:Draft ·\|Needs you ·)` |
| edge-rubric.en.006 | R4 | R4: `(?m)^\W*(?:Ready to (?:film\|post)\|Draft ·\|Needs you ·)` |
| edge-rubric.en.014 | R4 | R4: `(?m)^\W*(?:Ready to post\|✓ Checked:)` |
| edge-rubric.en.016 | R5 | Drop the `Draft ·` alternative: a fixable Draft is fixed silently, so the stance content alternatives must hold. |
| edge-rubric.en.018 | R4 | R4: `(?m)^\W*(?:Ready to (?:film\|post) · written as\|Draft ·)` |
| edge-rubric.en.019 | R6 | R6: `(?m)^\W*Draft · waiting on one fact from you; I(?:'\|’)ll ask next\.` |
| edge-rubric.en.020 | R4 | R4: `(?m)^\W*(?:Ready to (?:film\|post) · \|Draft · \|Needs you · )` |
| edge-rubric.en.021 | R17 | R17: `Posted on your call · my concern:` |
| edge-rubric.en.024 | R4, R8 | R4: `(?im)^\W*(?:Ready to (?:film\|post) · I(?:'\|’)d post it:[^\n]*their …`; R8: `(?im)^\W*(?:Ready to (?:film\|post) · I(?:'\|’)d post it:[^\n]*their …` |
| edge-rubric.en.026 | R1 | R1: `WHY THIS GETS CLIENTS` |
| edge-rubric.en.027 | R1 | R1: `WHY THIS GETS CLIENTS` |
| edge-rubric.en.028 | R1 | R1: `WHY THIS GETS CLIENTS` |
| edge-rubric.en.029 | R1 | R1: `WHY THIS GETS CLIENTS` |
| edge-rubric.en.030 | R1 | R1: `WHY THIS GETS CLIENTS` |
| edge-rubric.en.031 | R1 | R1: `WHY THIS GETS CLIENTS` |
| edge-rubric.en.032 | R4 | R4: `(?m)^\W*(?:Ready to post · \|Draft · \|Needs you · )` |

### fmt-short.en (23)

| Case | Rule | Needed change |
|---|---|---|
| fmt-short.en.001 | R1, R2, R9 | R1: `WHY THIS GETS CLIENTS`; R2: `(?i)✓ Checked:[^\n]*(sectional\|stair\|landing\|measure\|Whitfield\|Mega…`; R9: `(?i)(isn(?:'\|’)t pushy\|something real)`, `(?i)out loud` |
| fmt-short.en.002 | R1, R2 | R1: `WHY THIS GETS CLIENTS`; R2: `✓ Checked:` |
| fmt-short.en.003 | R1, R2, CTX | R1: `WHY THIS GETS CLIENTS`; R2: `(?i)✓ Checked:[^\n]*(stairwell\|banker\|thanksgiving\|2019\|best year\|M…` |
| fmt-short.en.004 | R16 | verdict = "Ready" only. |
| fmt-short.en.005 | R3 | R3: `Ready to post` |
| fmt-short.en.007 | R1, R2, CTX | R1: `WHY THIS GETS CLIENTS`; R2: `✓ Checked:` |
| fmt-short.en.008 | CTX |  |
| fmt-short.en.009 | R1, CTX | R1: `(?s)(WHY THIS GETS CLIENTS.*?){2}` |
| fmt-short.en.010 | CTX |  |
| fmt-short.en.011 | R1, CTX | R1: `(?s)(WHY THIS GETS CLIENTS.*?){3}` |
| fmt-short.en.012 | R1 | R1: `WHY THIS GETS CLIENTS` |
| fmt-short.en.016 | R1 | R1: `WHY THIS GETS CLIENTS` |
| fmt-short.en.017 | R9, R16 | The consent tick regex (`true / said yes … shown / this way`) moves to 'why?'; `Gail`, the individual-result line and word-for-word stay. |
| fmt-short.en.020 | R1 | R1: `WHY THIS GETS CLIENTS` |
| fmt-short.en.023 | R1 | R1: `WHY THIS GETS CLIENTS` |
| fmt-short.en.024 | R1 | R1: `WHY THIS GETS CLIENTS` |
| fmt-short.en.027 | R4 | R4: `(?i)(Ready to post\|Draft ·\|Needs you ·)` |
| fmt-short.en.028 | R4, CTX | R4: `(?i)(Ready to post\|Draft ·)` |
| fmt-short.en.034 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |
| fmt-short.en.038 | R17 | R17: `Posted on your call · my concern:[^\n]*· logged\.` |
| fmt-short.en.039 | R4 | R4: `(Ready to post\|Draft ·\|Needs you ·)` |
| fmt-short.en.040 | R1, R4 | R1: `WHY THIS GETS CLIENTS`; R4: `(Ready to (film\|post)\|Draft ·\|Needs you ·)` |
| fmt-short.en.042 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |

### guardrails.en (10)

| Case | Rule | Needed change |
|---|---|---|
| guardrails.en.034 | R9 | As convert.en.016: tick.cap shows on 'why?' only (§CM-GUARDRAILS COACH'S CALL). |
| guardrails.en.050 | R4, R6 | R4: `(Ready to (film\|post\|send) ·\|Draft · (?!waiting on one fact))`; R6: `(Ready to (film\|post\|send) ·\|Draft · (?!waiting on one fact))` |
| guardrails.en.052 | R17 | R17: `Posted on your call · my concern:[^\n]*· logged\.` |
| guardrails.en.053 | R17 | R17: `Posted on your call · my concern:[^\n]*· logged\.` |
| guardrails.en.054 | R4 | R4: `(Ready to (film\|post\|send) ·\|Draft ·)` |
| guardrails.en.056 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |
| guardrails.en.057 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |
| guardrails.en.058 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |
| guardrails.en.059 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |
| guardrails.en.061 | R8 | R8: `their shape, your [^\n]*; nothing copied` |

### humanize.en (4)

| Case | Rule | Needed change |
|---|---|---|
| humanize.en.025 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |
| humanize.en.027 | R1 | R1: `WHY THIS GETS CLIENTS` |
| humanize.en.028 | R1 | R1: `WHY THIS GETS CLIENTS` |
| humanize.en.029 | R1 | R1: `WHY THIS GETS CLIENTS` |

### liked.en (12)

| Case | Rule | Needed change |
|---|---|---|
| liked.en.006 | R8 | R8: `Ready to film · I(?:'\|’)d post it: their shape, your [^\n;]+; nothi…` |
| liked.en.007 | R8 | R8: `(?im)^\W*Ready to (?:film\|post) · I(?:'\|’)d post it: their shape, y…` |
| liked.en.008 | R1 | R1: `WHY THIS GETS CLIENTS` |
| liked.en.009 | CTX |  |
| liked.en.010 | CTX |  |
| liked.en.011 | R4 | R4: `(?im)^\W*(?:Ready to (?:film\|post) · \|Draft · \|Needs you · )` |
| liked.en.017 | R8 | R8: `Ready to film · I(?:'\|’)d post it: their shape, your [^\n;]+; nothi…` |
| liked.en.019 | R4 | R4: `(?im)^\W*(?:Ready to (?:film\|post) · \|Draft · \|Needs you · )` |
| liked.en.027 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |
| liked.en.028 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |
| liked.en.029 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |
| liked.en.035 | R8 | R8: `Ready to film · I(?:'\|’)d post it: their shape, your [^\n;]+; nothi…` |

### message.en (22)

| Case | Rule | Needed change |
|---|---|---|
| message.en.001 | R11, R12 | The trigger answers the talk-day question (no longer asked). Map = 4 lines (`KNOWN FOR:`, `3 TOPICS:`, `YOUR WORD:`, `YOUR VOICE:`) + "We'll run this for 4 weeks. OK, or change a line." Drop `one message`, `3 big ideas`, `offer`, `why this one`, `not now`, `nothing you know is wasted`, `screenshot`; add not_regex for NOT NOW / why this one. |
| message.en.002 | R12 | Trigger answers a 7-line-check question (talk day, line fix): re-anchor on the last missing-fact answer or 'done'. Map-quality assertions hold. |
| message.en.003 | R12 | Trigger answers a 7-line-check question (talk day, line fix): re-anchor on the last missing-fact answer or 'done'. Map-quality assertions hold. |
| message.en.004 | R12 | Trigger answers a 7-line-check question (talk day, line fix): re-anchor on the last missing-fact answer or 'done'. Map-quality assertions hold. |
| message.en.005 | R12 | Trigger answers a 7-line-check question (talk day, line fix): re-anchor on the last missing-fact answer or 'done'. Map-quality assertions hold. |
| message.en.006 | R12 | Trigger answers a 7-line-check question (talk day, line fix): re-anchor on the last missing-fact answer or 'done'. Map-quality assertions hold. |
| message.en.007 | R12 | Trigger answers a 7-line-check question (talk day, line fix): re-anchor on the last missing-fact answer or 'done'. Map-quality assertions hold. |
| message.en.008 | R11 | `why this one`, `not now … moms / TRT` are no longer on the Map: assert them on a 'why?' follow-up; the Map shows the 4 lines. |
| message.en.009 | R11, R12 | NOT NOW is hidden: ask 'why?' after the Map and assert the parked items with plain reasons and return triggers there. |
| message.en.010 | R11, R12 | `why this one … {n}` and `not now …` move to a 'why?' follow-up; re-anchor the trigger (talk-day answer or check fix). |
| message.en.011 | R11, R12 | `why this one … {n}` and `not now …` move to a 'why?' follow-up; re-anchor the trigger (talk-day answer or check fix). |
| message.en.012 | R11, R12 | `why this one … {n}` and `not now …` move to a 'why?' follow-up; re-anchor the trigger (talk-day answer or check fix). |
| message.en.013 | R12 | Trigger answers a 7-line-check question (talk day, line fix): re-anchor on the last missing-fact answer or 'done'. Map-quality assertions hold. |
| message.en.014 | R11 | The side door is internal (card side_door): assert it on 'why?' or in the pushback reply, not on the 4-line Map. |
| message.en.020 | R11 | Context: why-this-one is not on the Map; the coach's 'Says who?' follows a 'why?' reply. |
| message.en.021 | R10 | 'one by one' presumed the check screen. Missing facts already come one per message; re-aim at 'change N' alone (A) B) + "My pick: …") or retire. |
| message.en.031 | R10 | The old way is never asked on Day 0 (missing facts: client words, best result, offer); re-aim at a probe on one of those or retire. |
| message.en.033 | R1, R4 | R1: `WHY THIS GETS CLIENTS`; R4: `(Ready to (film\|post\|send) ·\|✓ Checked:\|Needs you ·\|Draft ·)` |
| message.en.034 | R1, R4 | R1: `WHY THIS GETS CLIENTS`; R4: `(Ready to (film\|post\|send) ·\|✓ Checked:\|Needs you ·\|Draft ·)` |
| message.en.036 | R1, R4 | R1: `WHY THIS GETS CLIENTS`; R4: `(Ready to (film\|post\|send) ·\|✓ Checked:\|Needs you ·\|Draft ·)` |
| message.en.041 | R1 | R1: `WHY THIS GETS CLIENTS` |
| message.en.044 | R1, R4 | R1: `WHY THIS GETS CLIENTS`; R4: `(Ready to (film\|post\|send) ·\|✓ Checked:\|Needs you ·\|Draft ·)` |

### research.en (4)

| Case | Rule | Needed change |
|---|---|---|
| research.en.001 | CTX |  |
| research.en.002 | CTX |  |
| research.en.003 | CTX |  |
| research.en.004 | CTX |  |

### router.en (19)

| Case | Rule | Needed change |
|---|---|---|
| router.en.002 | R1 | R1: `WHY THIS GETS CLIENTS` |
| router.en.010 | R11 | 'Show me my Map' prints the 4 lines; `not now` (and big-idea shifts) only on 'why?'. |
| router.en.023 | R1, R4 | R1: `WHY THIS GETS CLIENTS`; R4: `(?m)^\W*(Ready to (film\|post) · \|Draft · \|Needs you · \|✓ Checked:)` |
| router.en.024 | R4 | R4: `(?m)^\W*(Ready to post · \|Draft · \|Needs you · )` |
| router.en.030 | CTX |  |
| router.en.035 | R4 | R4: `(?m)^\W*(Ready to post · \|Draft · \|✓ Checked:)` |
| router.en.044 | CTX |  |
| router.en.048 | R7 | R7: `(?im)^\W*(posted on your call\|ready to post)\b` |
| router.en.049 | R7 | R7: `(?im)^\W*(posted on your call\|ready to send)\b` |
| router.en.051 | R4 | R4: `(?im)^\W*(Not writing ["“]\|Needs you · \|Ready to (film\|post) · )` |
| router.en.052 | R4 | R4: `(?m)^\W*(Ready to post · \|✓ Checked:)` |
| router.en.057 | R4 | R4: `(?m)^\W*(Ready to (film\|post) · \|Draft · \|✓ Checked:)` |
| router.en.059 | R3 | R3: `(?m)^\W*Ready to post · written as ` |
| router.en.063 | R17 | R17: `(?m)^\W*Posted on your call · my concern: [^\n]+ · logged\.?\s*$` |
| router.en.064 | R4 | R4: `(?m)^\W*(Ready to post · \|Draft · \|✓ Checked:)` |
| router.en.070 | R1, R8 | R1: `WHY THIS GETS CLIENTS`; R8: `(?i)their shape, your\b[^\n]*nothing copied` |
| router.en.072 | R1, R2 | R1: `WHY THIS GETS CLIENTS`; R2: `(?m)^\W*✓ Checked:` |
| router.en.073 | R4 | R4: `(?m)^\W*(Ready to post · \|Draft · \|Needs you · )` |
| router.en.074 | R4 | R4: `(?m)^\W*(Ready to post · \|Draft · \|Needs you · )` |

### setup.en (27)

| Case | Rule | Needed change |
|---|---|---|
| setup.en.002 | R14 | Replace `about 30 min` / `empty your head` with the new promise (`about 25 min`, `Talk 5–10 min about your work`, `your first week`); the mic tips stay. |
| setup.en.003 | CTX |  |
| setup.en.006 | R18 | The early win no longer scripts "You haven't told me {gap}": accept any one-line jogger or drop that regex. |
| setup.en.012 | R10 | After 'done': no inventory, no numbered lines 1–7. Expect ONE missing-fact message with a guess; here the multi-income line takes that slot (keep `you earn from 3 things`, `which pays the bills`). Add not_regex for `you know a lot`, `months of content`, `^\W*[1-7]\b.*(who\|their words\|old way)`. |
| setup.en.013 | R10 | Expect the best-result fact as "My guess: no client result to show yet, so I'll use your own story. Right?" and no check lines 4/6/7; keep the trap not_regex (22, 200, certified, kids' names, past clients). |
| setup.en.014 | R10, R12 | No line 7: list size is never asked. The ~900 newsletter is guessed from the dump and shows in Week 1 (email-first) and the card's machine block. Keep: no multi-income line. |
| setup.en.015 | CTX | Assertions hold (the multi-income line is now one of the ≤3 missing facts, string setup.multi_income); only the context's '7-line check' wording changes. |
| setup.en.016 | CTX |  |
| setup.en.017 | R2, R11, R13, R14 | New turn script: dump → ≤3 missing facts → Map → 'ok' → FILM TODAY → any message → Week 1 (2 replies on Free) → card + save line. Title/budgets: Map ≤6 coach turns, film-ready ≤20 min, ≤10 turns. Drop `Why this one` and `✓ Checked:`; add the 4 Map labels and `Save this so I remember you`. |
| setup.en.018 | R1, R2, R11, R13 | As setup.en.017 (compact mode): drop `Why this one`, `✓ Checked:`, `WHY THIS GETS CLIENTS`; 'brb' / 'ok back' stay; no 'next' needed for Week 1. |
| setup.en.019 | R13 | Grade from Start to Day 0's last reply (card + save line); 'I'm not filming today' after FILM TODAY now gets Week 1, then the card. `post the caption as text` stays valid (film.now_or_text). |
| setup.en.020 | R1, R2, R9 | Drop `WHY THIS GETS CLIENTS`, the `✓ Checked:` story regex, `isn't pushy` and `first line out loud`; add not_regex for all four. Keep the shape, `say quiet`, the copy box and `post the caption as text`. |
| setup.en.023 | R1, R2 | Drop WHY and the `✓ Checked:` story regex; assert his own story inside the script body instead (relay, birthday, garage, pull-up…). |
| setup.en.025 | R13 | No stop point. 'ok I'll film it tomorrow…' after FILM TODAY gets all of Week 1; the card + "Save this so I remember you (30 s)." + NEXT close Day 0. Replace `that's today done`, `stop here`, `they'll wait`, `say next` (for Week 1) with: Week-1 pieces first, then the card and save line. Keep every never-block-on-save not_regex. |
| setup.en.026 | CTX | Context: the card is printed after Week 1 (Day 0's last reply), not at a stop point. Assertions hold. |
| setup.en.027 | R1, R4, R13 | Week 1 now always arrives before the card exists, so the forced test moves: day 2 with the card unsaved, 'next' still gives today's piece. Replace the WHY and status-line regexes with a piece detector (copy box, `N1 ·`). |
| setup.en.028 | R1, R4, CTX | Week 1 arrives unasked after FILM TODAY ('next' still works). Drop the WHY / status-line assertions; check one piece's WHY with a 'why?' follow-up. Context: no stop point. |
| setup.en.029 | R1, CTX | Week 1 arrives unasked after FILM TODAY. Drop the WHY assertions (one 'why?' follow-up carries it). Context: no stop point. |
| setup.en.032 | CTX |  |
| setup.en.033 | R1, R4, CTX | Week 1 arrives unasked after FILM TODAY ('next' still works). Drop the WHY / status-line assertions; check one piece's WHY with a 'why?' follow-up. Context: no stop point. |
| setup.en.034 | R1, CTX | Week 1 arrives unasked after FILM TODAY. Drop the WHY assertions (one 'why?' follow-up carries it). Context: no stop point. |
| setup.en.035 | R13 | No 3-line wrap-up. Talk day is named once above Week 1 ("For {platform} · talk day {day} (my guess; one word changes it)."); Day 0's last reply = card + save line + the reminder offer + NEXT 'Film today's video. Tomorrow: open Content Machine, newest chat, say 'next''. Move `tue` / `fri` to the Week-1 reply. |
| setup.en.036 | R12 | 'fix 3. not "method"…' fixed line 3 of the 7-line check. Re-anchor on 'change 3: …' on the Map (or the last missing-fact answer); the Claude Free save point after the Map stays. |
| setup.en.037 | R1 | Drop `WHY THIS GETS CLIENTS`; FILM TODAY + `record year` stay. |
| setup.en.038 | CTX |  |
| setup.en.041 | CTX | 'Wrap-up' is now Day 0's last reply (box + save line). Assertions hold. |
| setup.en.042 | R1 | Drop the WHY assertion; the flip (credentials as proof) is asserted in the script body. |

### signature.en (3)

| Case | Rule | Needed change |
|---|---|---|
| signature.en.006 | R2, R9 | FILM TODAY no longer prints a Checked line or ticks: assert the keyword in the script/caption and `say 'quiet'`; the check moves to 'why?'. |
| signature.en.007 | CTX |  |
| signature.en.016 | CTX |  |

### brain.vn (9)

| Case | Rule | Needed change |
|---|---|---|
| brain.vn.001 | R13, R15 | Offer 4.990.000đ and `thứ Ba` leave the top ('NÓI GÌ:' / 'NÓI THẾ NÀO:'); they move to the machine block. Context: talk day guessed, not 'confirmed on line 7'; card after Week 1. |
| brain.vn.002 | R13 | Trigger 'ok em, tối chị quay' now gets Week 1; the card prints after it. Field assertions hold. |
| brain.vn.003 | R15 | 'one phone screen' → top ≤500 chars, 3 lines (title · NÓI GÌ · NÓI THẾ NÀO). |
| brain.vn.005 | R13 | Trigger 'ok em, tối chị quay' now gets Week 1; the card prints after it. Field assertions hold. |
| brain.vn.009 | R13 | Directly contradicted: the card is no longer printed before Week 1. Rewrite: on Free, Week 1 in 2 replies (≤3 pieces each), then card + save line; a 'để sau' before that prints card + save line at once. Drop not_contains `VÌ SAO RA KHÁCH` (still true, but no longer the point). |
| brain.vn.022 | R13 | Trigger 'ok em, tối chị quay' now gets Week 1; the card prints after it. Field assertions hold. |
| brain.vn.023 | R13 | Trigger 'ok em, tối chị quay' now gets Week 1; the card prints after it. Field assertions hold. |
| brain.vn.024 | R13 | Trigger 'ok em, tối chị quay' now gets Week 1; the card prints after it. Field assertions hold. |
| brain.vn.025 | CTX |  |

### character.vn (14)

| Case | Rule | Needed change |
|---|---|---|
| character.vn.001 | CTX |  |
| character.vn.002 | CTX |  |
| character.vn.003 | CTX |  |
| character.vn.004 | R1 | R1: `VÌ SAO RA KHÁCH` |
| character.vn.005 | R1 | R1: `VÌ SAO RA KHÁCH` |
| character.vn.006 | R1 | R1: `VÌ SAO RA KHÁCH` |
| character.vn.008 | R1 | R1: `VÌ SAO RA KHÁCH` |
| character.vn.009 | R1 | R1: `VÌ SAO RA KHÁCH` |
| character.vn.010 | R1 | R1: `VÌ SAO RA KHÁCH` |
| character.vn.012 | R1 | R1: `VÌ SAO RA KHÁCH` |
| character.vn.023 | CTX |  |
| character.vn.025 | R1 | R1: `VÌ SAO RA KHÁCH` |
| character.vn.027 | CTX |  |
| character.vn.028 | R1 | R1: `VÌ SAO RA KHÁCH` |

### convert.vn (6)

| Case | Rule | Needed change |
|---|---|---|
| convert.vn.001 | CTX |  |
| convert.vn.002 | CTX |  |
| convert.vn.021 | R1 | R1: `VÌ SAO RA KHÁCH` |
| convert.vn.023 | R9 | `là thật … sẽ giữ đúng` (tick.cap) moves to 'tại sao?'; the plain cap in the post stays. |
| convert.vn.027 | R3 | R3: `Sẵn sàng đăng · viết dạng` |
| convert.vn.036 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |

### edge-rubric.vn (13)

| Case | Rule | Needed change |
|---|---|---|
| edge-rubric.vn.001 | R4 | R4: `(?m)^\W*(?:Sẵn sàng (?:quay\|đăng)\|Bản nháp ·\|Cần chị ·)`, `(?im)^\W*Sẵn sàng (?:quay\|đăng)[^\n]*(?:gương\|ngại chào\|2018\|kịch b…` |
| edge-rubric.vn.006 | R4 | R4: `(?m)^\W*(?:Sẵn sàng đăng\|✓ Đã kiểm:)` |
| edge-rubric.vn.013 | R5 | As edge-rubric.en.016 (`Bản nháp ·` alternative goes). |
| edge-rubric.vn.014 | R1 | R1: `VÌ SAO RA KHÁCH` |
| edge-rubric.vn.016 | R17 | R17: `Đăng theo quyết định của chị` |
| edge-rubric.vn.017 | R4 | R4: `(?m)^\W*(?:Sẵn sàng (?:đăng\|quay)\|Bản nháp ·\|Cần anh ·\|✓ Đã kiểm:)` |
| edge-rubric.vn.020 | R4 | R4: `(?m)^\W*(?:Sẵn sàng đăng · viết dạng\|Cần anh ·\|Bản nháp ·)` |
| edge-rubric.vn.021 | R1 | R1: `VÌ SAO RA KHÁCH` |
| edge-rubric.vn.022 | R1 | R1: `VÌ SAO RA KHÁCH` |
| edge-rubric.vn.023 | R1 | R1: `VÌ SAO RA KHÁCH` |
| edge-rubric.vn.024 | R1 | R1: `VÌ SAO RA KHÁCH` |
| edge-rubric.vn.025 | R1 | R1: `VÌ SAO RA KHÁCH` |
| edge-rubric.vn.027 | R4 | R4: `(?m)^\W*(?:Sẵn sàng (?:quay\|đăng) · viết dạng\|Bản nháp · )` |

### fmt-short.vn (25)

| Case | Rule | Needed change |
|---|---|---|
| fmt-short.vn.001 | R1, R2, R9 | Drop `VÌ SAO RA KHÁCH`, `✓ Đã kiểm:` and `đọc to` (FILM TODAY carries no tick); the parts and caps of the script stay. |
| fmt-short.vn.002 | R1, R2 | R1: `VÌ SAO RA KHÁCH`; R2: `✓ Đã kiểm:` |
| fmt-short.vn.003 | R1, R2 | R1: `VÌ SAO RA KHÁCH`; R2: `✓ Đã kiểm:[^\n]*(?:toilet\|nhà mẫu\|khăn giấy\|dí cọc)` |
| fmt-short.vn.004 | R1, R2 | R1: `VÌ SAO RA KHÁCH`; R2: `✓ Đã kiểm:[^\n]*(?:2019\|Liên Chiểu\|đục thử\|ông chú)` |
| fmt-short.vn.006 | R1, CTX | R1: `(?s)(?:VÌ SAO RA KHÁCH.*?){3}` |
| fmt-short.vn.008 | CTX |  |
| fmt-short.vn.009 | R1, CTX | R1: `(?s)(?:VÌ SAO RA KHÁCH.*?){2}` |
| fmt-short.vn.010 | R3, CTX | R3: `Sẵn sàng đăng ·` |
| fmt-short.vn.012 | CTX |  |
| fmt-short.vn.015 | R1 | R1: `VÌ SAO RA KHÁCH` |
| fmt-short.vn.016 | R1 | R1: `VÌ SAO RA KHÁCH` |
| fmt-short.vn.017 | R1 | R1: `VÌ SAO RA KHÁCH` |
| fmt-short.vn.018 | R1 | R1: `VÌ SAO RA KHÁCH` |
| fmt-short.vn.020 | R1 | R1: `VÌ SAO RA KHÁCH` |
| fmt-short.vn.024 | R4 | R4: `(?:Sẵn sàng đăng ·\|Bản nháp ·\|Cần chị ·)` |
| fmt-short.vn.027 | R4, CTX | R4: `(?:Sẵn sàng đăng ·\|Bản nháp ·)` |
| fmt-short.vn.028 | R1, R4 | R1: `VÌ SAO RA KHÁCH`; R4: `(?:Sẵn sàng (?:quay\|đăng) ·\|Bản nháp ·\|Cần anh ·)` |
| fmt-short.vn.030 | R1 | R1: `VÌ SAO RA KHÁCH` |
| fmt-short.vn.031 | R4 | R4: `(?:Sẵn sàng quay ·\|Bản nháp ·\|Cần chị ·)` |
| fmt-short.vn.036 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |
| fmt-short.vn.037 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |
| fmt-short.vn.038 | R1 | R1: `VÌ SAO RA KHÁCH` |
| fmt-short.vn.040 | R1 | R1: `VÌ SAO RA KHÁCH` |
| fmt-short.vn.042 | R4 | R4: `(?:Sẵn sàng (?:quay\|đăng) ·\|Bản nháp ·\|Cần chị ·)` |
| fmt-short.vn.043 | R17 | R17: `Đăng theo quyết định của chị · em lưu ý:[^\n]*· đã ghi lại\.` |

### guardrails.vn (12)

| Case | Rule | Needed change |
|---|---|---|
| guardrails.vn.037 | R9 | As convert.vn.023. |
| guardrails.vn.049 | R4 | R4: `(?m)^\W*(?:Sẵn sàng (?:quay\|đăng\|gửi)\|✓ Đã kiểm:)` |
| guardrails.vn.051 | R17 | R17: `Đăng theo quyết định của chị · em lưu ý:[^\n]*· đã ghi lại\.` |
| guardrails.vn.052 | R4 | R4: `(?m)^\W*(?:Sẵn sàng (?:quay\|đăng\|gửi)\|✓ Đã kiểm:\|Bản nháp ·)` |
| guardrails.vn.054 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |
| guardrails.vn.055 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |
| guardrails.vn.056 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |
| guardrails.vn.057 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |
| guardrails.vn.058 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |
| guardrails.vn.059 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |
| guardrails.vn.060 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |
| guardrails.vn.061 | R8 | R8: `khung của họ, [^\n]*; không chép câu nào` |

### humanize.vn (2)

| Case | Rule | Needed change |
|---|---|---|
| humanize.vn.029 | R7 | R7: `Đăng theo quyết định của anh` |
| humanize.vn.030 | R8 | R8: `Sẵn sàng (?:quay\|đăng) · Em sẽ đăng: khung của họ, [^\n;]+ của anh;…` |

### liked.vn (11)

| Case | Rule | Needed change |
|---|---|---|
| liked.vn.002 | R8 | R8: `Sẵn sàng (?:quay\|đăng) · Em sẽ đăng: khung của họ, [^\n;]+ của chị;…` |
| liked.vn.005 | R8 | R8: `Sẵn sàng (?:quay\|đăng) · Em sẽ đăng: khung của họ, [^\n;]+ của chị;…` |
| liked.vn.008 | R4 | R4: `(?im)^\W*(?:Câu\s+["“][^\n]*["”]\s+mình không viết:\|Sẵn sàng (?:qua…` |
| liked.vn.013 | R8 | R8: `khung của họ, [^\n;]+ của chị; không chép câu nào` |
| liked.vn.015 | R8 | R8: `Sẵn sàng (?:quay\|đăng) · Em sẽ đăng: khung của họ, [^\n;]+ của chị;…` |
| liked.vn.021 | R4 | R4: `(?im)^\W*(?:Sẵn sàng (?:quay\|đăng) · \|Cần chị · )` |
| liked.vn.022 | R7 | R7: `Đăng theo quyết định của bạn` |
| liked.vn.023 | R7 | R7: `Đăng theo quyết định của chị` |
| liked.vn.024 | R7 | R7: `Đăng theo quyết định của chị` |
| liked.vn.025 | R7 | verdict = "Override" (F1): assert the one dated note and no Override / "posted on your call" line. |
| liked.vn.031 | R8 | R8: `khung của họ, [^\n;]+ của chị; không chép câu nào` |

### message.vn (18)

| Case | Rule | Needed change |
|---|---|---|
| message.vn.002 | R18 | `đăng được luôn` (line 2 is a post) left the early win; `chưa kể` holds only if the jogger is worded that way. Keep `3 câu đáng tiền anh vừa nói` and `gõ 'xong'`. |
| message.vn.006 | R10 | No inventory (`6 tháng content`, `Chị biết nhiều thật`, `không bỏ gì`). After 'xong' the first missing fact (one message, with a guess); message.vn.040 keeps `3 nguồn thu` (multi-income slot). |
| message.vn.007 | R10 | No 7-line check (`Lời của họ`, `Cách cũ`, `Kết quả tốt nhất`, `theo số`, `gõ 'ok'`). Rewrite as the best-result missing fact: the guess is Thảo's result, never the spa client's 70%. |
| message.vn.008 | R10 | Re-aim: a story given as the answer to a missing fact is taken as the answer (no 'sửa 1' to demand); context without the check screen. |
| message.vn.011 | R10 | 'từng câu' presumed the check screen; re-aim at 'sửa dòng N' alone on the Map (A) B) + 'Mình chọn: …') or retire. |
| message.vn.013 | R11 | `ĐỂ SAU` is not on the Map; keep `(mình đoán)`. |
| message.vn.014 | CTX |  |
| message.vn.015 | R11, R12 | Map = 4 lines (`ĐƯỢC BIẾT ĐẾN VÌ:`, `3 CHỦ ĐỀ:`, `TỪ KHOÁ CỦA BẠN:` / any pronoun, `GIỌNG CỦA BẠN:`) + 'Mình chạy thử 4 tuần nhé. OK, hoặc sửa một dòng.' Drop `MỘT THÔNG ĐIỆP`, `3 Ý LỚN`, `ĐỂ SAU`, `chụp màn hình`, `không có gì … bị bỏ phí`, the price regex; the trigger (talk day, hours, delivery) is no longer asked. |
| message.vn.016 | R12 | Trigger answers line 7 or fixes a check line: re-anchor on the last missing-fact answer. Map-quality assertions hold. |
| message.vn.017 | R11 | `ĐỂ SAU` moves to a 'tại sao?' follow-up; the multi-income trigger is still valid. |
| message.vn.020 | R11, R12 | `ĐỂ SAU` (and NOT NOW reasons) move to a 'tại sao?' follow-up; the trigger (talk day / 'sửa 4' on the check) is re-anchored. |
| message.vn.021 | R11, R12 | `ĐỂ SAU` (and NOT NOW reasons) move to a 'tại sao?' follow-up; the trigger (talk day / 'sửa 4' on the check) is re-anchored. |
| message.vn.022 | R12 | Trigger answers line 7 or fixes a check line: re-anchor on the last missing-fact answer. Map-quality assertions hold. |
| message.vn.023 | R11, R12 | `ĐỂ SAU` (and NOT NOW reasons) move to a 'tại sao?' follow-up; the trigger (talk day / 'sửa 4' on the check) is re-anchored. |
| message.vn.024 | R12 | Trigger answers line 7 or fixes a check line: re-anchor on the last missing-fact answer. Map-quality assertions hold. |
| message.vn.034 | R1 | Drop `VÌ SAO RA KHÁCH`; the bridge line and the piece stay. |
| message.vn.039 | R11, R14 | `MỘT THÔNG ĐIỆP` → the 4 Map labels; 'within 9 coach turns' → ≤7 (acceptance [day0] map_max_turns_vn). |
| message.vn.040 | R10 | No inventory (`6 tháng content`, `Chị biết nhiều thật`, `không bỏ gì`). After 'xong' the first missing fact (one message, with a guess); message.vn.040 keeps `3 nguồn thu` (multi-income slot). |

### research.vn (1)

| Case | Rule | Needed change |
|---|---|---|
| research.vn.001 | CTX |  |

### router.vn (24)

| Case | Rule | Needed change |
|---|---|---|
| router.vn.002 | R1 | R1: `VÌ SAO RA KHÁCH` |
| router.vn.013 | R1, R4, R13 | 'tiếp at the stop point' → Week 1 is already printed by then; re-aim at day 2 with the card unsaved. Drop VÌ SAO / status-line regexes (piece detector instead). |
| router.vn.014 | R11 | As router.en.010: `ĐỂ SAU` only on 'tại sao?'. |
| router.vn.027 | R1, R4 | R1: `VÌ SAO RA KHÁCH`; R4: `(?m)^\W*(?:Sẵn sàng (?:quay\|đăng) · \|Bản nháp · \|Cần bạn · \|✓ Đã ki…` |
| router.vn.028 | R4 | R4: `(?m)^\W*(?:Sẵn sàng đăng · \|Bản nháp · \|Cần chị · \|✓ Đã kiểm:)` |
| router.vn.034 | CTX |  |
| router.vn.039 | R4 | R4: `(?m)^\W*(?:Sẵn sàng đăng · \|Bản nháp · \|✓ Đã kiểm:)` |
| router.vn.048 | CTX |  |
| router.vn.052 | R7 | R7: `(?m)^\W*Đăng theo quyết định của chị · em lưu ý:` |
| router.vn.053 | R7 | R7: `(?m)^\W*Đăng theo quyết định của chị · em lưu ý:` |
| router.vn.054 | R7 | R7: `(?m)^\W*Đăng theo quyết định của anh · em lưu ý:` |
| router.vn.055 | R4 | R4: `(?im)^\W*(Câu ["“]\|Cần bạn · \|Sẵn sàng (quay\|đăng) · )` |
| router.vn.057 | R4 | R4: `(?m)^\W*(?:Sẵn sàng quay · \|✓ Đã kiểm:)` |
| router.vn.058 | R4 | R4: `(?m)^\W*(?:Sẵn sàng đăng · \|✓ Đã kiểm:)` |
| router.vn.066 | R4 | R4: `(?m)^\W*(?:Sẵn sàng đăng · \|Bản nháp · \|✓ Đã kiểm:)` |
| router.vn.069 | R3 | R3: `(?m)^\W*Sẵn sàng (?:đăng\|quay) · viết dạng ` |
| router.vn.074 | R17 | R17: `(?m)^\W*Đăng theo quyết định của chị · em lưu ý: [^\n]+ · đã ghi lạ…` |
| router.vn.075 | R4 | R4: `(?m)^\W*(?:Sẵn sàng (?:quay\|đăng) · \|Bản nháp · \|Cần anh · )` |
| router.vn.076 | R4 | R4: `(?m)^\W*(?:Sẵn sàng đăng · \|Bản nháp · \|✓ Đã kiểm:)` |
| router.vn.082 | R1, R8 | R1: `VÌ SAO RA KHÁCH`; R8: `(?i)khung của họ,[^\n]*không chép câu nào` |
| router.vn.083 | R1, R2 | R1: `VÌ SAO RA KHÁCH`; R2: `(?m)^\W*✓ Đã kiểm:` |
| router.vn.084 | R4 | R4: `(?m)^\W*(?:Sẵn sàng (?:quay\|đăng) · \|Bản nháp · \|Cần anh · )` |
| router.vn.085 | R4 | R4: `(?m)^\W*(?:Sẵn sàng gửi · \|✓ Đã kiểm:)` |
| router.vn.102 | R4 | R4: `(?m)^\W*(?:Sẵn sàng đăng · \|Bản nháp · \|✓ Đã kiểm:)` |

### setup.vn (22)

| Case | Rule | Needed change |
|---|---|---|
| setup.vn.002 | CTX |  |
| setup.vn.003 | R14 | `khoảng 30 phút` → the new VN promise (≈ 25 phút · nói 5–10 phút về công việc · video quay hôm nay và tuần đầu); keep the xưng hô question. |
| setup.vn.009 | R1 | Drop `VÌ SAO RA KHÁCH` from contains; the not_contains (`Cần bạn ·`, `Mình sẽ đăng:` …) stay. 'Wrap-up' → Day 0's last reply. |
| setup.vn.012 | R1, R2, R9 | Drop `VÌ SAO RA KHÁCH`, `✓ Đã kiểm:`, `không có câu hứa rủi ro` and `từ khoá 1 lần`. The closing line is film.now_or_text ('Quay luôn bây giờ, hoặc đăng caption dạng bài chữ cũng được.'), so `chưa quay … caption` becomes `đăng caption`. 2018 stays in the script. |
| setup.vn.025 | R13 | No stop point: `Hôm nay vậy là đủ rồi chị` and `kịch bản tuần 1` go. 'ok em, tối chị quay' gets Week 1; then the card + 'Lưu lại để mình nhớ bạn (30 giây).' + TIẾP. |
| setup.vn.026 | R13 | Door B: the card/box + Zalo 'Cloud của tôi' come after Week 1; `gõ 'tiếp'` moves to the NEXT line for tomorrow. |
| setup.vn.027 | R1, R13 | As setup.en.027: the forced unsaved-card test moves to day 2; drop `VÌ SAO RA KHÁCH`. |
| setup.vn.028 | CTX |  |
| setup.vn.029 | R1, CTX | 'each with a WHY line' → each piece with nothing under it; keep ≤3 pieces a reply (Free). WHY via 'tại sao?'. Context: no stop point. |
| setup.vn.030 | R1, CTX | Drop `VÌ SAO RA KHÁCH`; Week 1 arrives unasked after QUAY HÔM NAY. Context: no stop point or line 7. |
| setup.vn.031 | R1, CTX | Drop `VÌ SAO RA KHÁCH`; Week 1 arrives unasked after QUAY HÔM NAY. Context: no stop point or line 7. |
| setup.vn.032 | R1, CTX | Drop `VÌ SAO RA KHÁCH`; Week 1 arrives unasked after QUAY HÔM NAY. Context: no stop point or line 7. |
| setup.vn.034 | CTX |  |
| setup.vn.036 | CTX |  |
| setup.vn.037 | R13 | No 3-line wrap-up; the exact TIẾP line stays valid on Day 0's last reply (card + save line + reminder offer `nhắc`). `thứ Sáu` moves to the Week-1 header or the reminder offer. |
| setup.vn.038 | CTX |  |
| setup.vn.041 | R10, R12 | Context: the cap hit after missing fact 2 of 3 (no inventory, no line 7). not_regex `(lời của họ\|kết quả tốt nhất): ?` → 'never re-asks an answered fact'. |
| setup.vn.042 | R1 | Drop `VÌ SAO RA KHÁCH`; today's piece prints with nothing under it. |
| setup.vn.043 | R13 | Golden run 'to the stop point' → to Day 0's last reply (card + save line). |
| setup.vn.044 | R1, R14 | Drop `VÌ SAO RA KHÁCH`; budgets per acceptance [day0] (Map ≤7 VN coach turns, ≤10 turns, film-ready ≤20 min), not 9 / 12. |
| setup.vn.045 | R1 | Drop `VÌ SAO RA KHÁCH` from the Day-0 text it scans. |
| setup.vn.046 | CTX |  |

### signature.vn (10)

| Case | Rule | Needed change |
|---|---|---|
| signature.vn.001 | CTX |  |
| signature.vn.002 | CTX |  |
| signature.vn.003 | CTX |  |
| signature.vn.004 | CTX |  |
| signature.vn.005 | CTX |  |
| signature.vn.006 | R10 | `cách cũ … cọc trước tính sau` was a check line; assert the old way in the machine block or on 'tại sao?'. |
| signature.vn.015 | CTX |  |
| signature.vn.018 | R11 | `3 ý lớn` → the Map label `3 CHỦ ĐỀ:` (plain topic names). |
| signature.vn.022 | R1 | R1: `(?i)VÌ SAO RA KHÁCH[^\n]*(?:comment\|bình luận)[^\n]*lãi (?:ảo\|thật)…` |
| signature.vn.023 | R1, R2 | `✓ Đã kiểm: … từ khoá 1 lần` moves to 'tại sao?'; keep the keyword-once assertion on the script itself. |

## Totals

341 cases listed (174 EN, 167 VN). By rule (a case can count under several):

| Rule | Cases |
|---|---|
| R1 Visible WHY line | 93 |
| R2 Visible ✓ Checked line | 18 |
| R3 Ready / written-as line under a finished piece | 6 |
| R4 Status line used as the "a piece was delivered" detector | 65 |
| R5 Visible "Draft ·" on a machine-written piece | 2 |
| R6 "Draft · waiting on one fact" (verdict.draft_queued) | 2 |
| R7 Override line on an F1 request (copy / translate / compare) | 32 |
| R8 liked.evidence line under a version | 15 |
| R9 Ticks and FILM TODAY extras | 10 |
| R10 7-line check screen and inventory | 12 |
| R11 Old Map screen | 20 |
| R12 Trigger turn answers a question Day 0 no longer asks | 23 |
| R13 Stop point, card before Week 1, wrap-up | 30 |
| R14 Old Day-0 promise and budgets | 5 |
| R15 Brand Card visible part | 4 |
| R16 `verdict = "Ready"` / `"Ready-downgraded"` with no text assertion | 2 |
| R17 "post anyway" Override line wording (watch) | 9 |
| R18 Early-win wording | 2 |
| CTX Context or notes only | 69 |

## Notes for the rewrite pass

- **Keep the hidden checks tested.** Every case that loses a WHY, Checked or Ready assertion should keep its quality bar through a paired "why?" turn (wf15 §3: "Hidden checks are asserted through 'why?' cases instead"). One "why?" case per module per edition is the minimum; the I3 grader already fails a status line printed without it.
- **Strings the new cases can quote** (strings/en.toml, vn.toml): `map.known`, `map.topics`, `map.word`, `map.voice`, `map.ok`, `setup.guess`, `setup.guess_no_result`, `setup.multi_income`, `setup.plan_guess`, `setup.link_unread`, `setup.cut_off`, `film.now_or_text`, `card.save_line`, `card.visible.what`, `card.visible.how`, `card.visible.to_them`, `card.visible.never`, `voice.not_me_ok`, `voice.do_say_ok`.
- **Strings now unused** (lint W202), whose cases go with them: `card.stop_lines`, `film.not_filming`, `verdict.draft_queued`, `voice.not_me_done` (replaced by `voice.not_me_ok`, wf14 §2).
- **New cases wf14/wf15 ask for, not yet written:** `voice.{en,vn}.toml` (≥20 each, wf14 §5), "why?" cases per module, the 4-line Map with the voice line, the audience address kept apart from the machine–coach pair (VN), the coach's page link read silently and an unopened link said in one clause (`setup.link_unread`), Week 1 arriving unasked after FILM TODAY, and the 500-character card top.
- **Unrelated stale number found on the way:** brain.vn.004 says "Whole card ≤5,800 characters"; the schema whole budget is 6,600 VN since wf13.

## Status

**EN: done, 6 Oct 2026** (two writer groups, each checked by a verifier, then integrated; nothing committed by the pass). All 174 listed EN cases are handled by their rule. The R17 cases (edge-rubric.en.021, fmt-short.en.038, guardrails.en.052/053, router.en.063) keep `verdict.override` as R17 says. Cases the list missed were fixed as well: stale promise, check-screen and Map contexts, "same state as" contexts, and broken regexes. The final contradiction search over all `*.en.toml` positive assertions finds hits only on "why?" turns, on checks of the coach's own draft (edge-rubric.en.004, .012; router.en.034), on R17 "post anyway" turns, or on false matches (the keyword "record year", Erin's "shop your way", the "old way" in KNOWN FOR, "out loud" in the deep-talk invite). The kit's later-chat lines still say "big idea {n}" and "Parked".

| Module | Cases | Rewritten | Added | "why?" cases |
|---|---|---|---|---|
| setup.en | 51 | 32 | 9 | 048 (Map), 049, 050 |
| research.en | 27 | 6 | 1 | 027 |
| signature.en | 27 | 12 | 2 | 026, 027 |
| message.en | 55 | 38 | 10 | 009, 046-049 (Map), 055 |
| brain.en | 33 | 21 | 7 | 033 |
| fmt-short.en | 48 | 26 | 5 | 044-048 |
| humanize.en | 30 | 24 | 1 | 030 |
| character.en | 28 | 7 | 1 | 028 |
| edge-rubric.en | 35 | 27 | 3 | 033-035 (+003 record) |
| convert.en | 47 | 16 | 3 | 045-047 |
| guardrails.en | 68 | 15 | 3 | 066-068 |
| liked.en | 37 | 20 | 2 | 036, 037 |
| router.en | 96 | 29 | 7 | 090-093 (+062 record); 094-096 Day-0 order |
| voice.en (new) | 29 | n/a | 29 | 024, 025 |

`evals/registry.toml` now has a `[modules.voice]` row (planned). Every file parses; ids are gap-free; every regex compiles; invariants are within I1-I23; personas and `<<paste>>` targets exist; text is NFC. The case conventions are in `evals/README.md` "Case files".

**VN: still to do.** The 167 listed VN cases, `voice.vn.toml` (≥20), and the "why?" cases per module come after the VN port and the VN naturalness pass. They mirror the EN patterns: piece detectors by copy box, not status line; copy-box-only humanize strips; and the "why?" pairs.

**Open flags** (deduplicated from writers and verifiers; owners in brackets):
- [graders.py] I8 reads the card's ISO dates as claim numbers, which fails every Day-0 card case; brain.en.010's `401(k)` fails the same way. I17 flags "Messy is perfect." (start-block 1), which fails setup.en.001-004 and 040. I6 counts each reprint of `map.ok` as a new decision: message.en.052 and brain.en.030 cannot pass, and setup.en.048, signature.en.008 and message.en.009/015/021 fail whenever the line repeats. The `quit_triggers` 300-word counter does not count the early win or the Map as usable output. I3's 20-word cap is tight for "why?" evidence lines, for `verdict.needs` (9 fixed words) and for `verdict.hardstop`. FORMAT_TITLE_RE misses platform-prefixed titles and untitled copy boxes, so I3 and I12 under-detect and `scope: pieces` comes back empty. CHECK_ASK_RE misses "tell me if this is ready" (edge-rubric.en.012 has a workaround). WHY_RE takes any short "why …" question as "why?" (router.en.083, message.en.037). `day0_timing` counts forwarded-post turns (liked.en.010). I23 reads only `not me:` lines, and NOT_ME_RE bans the whole rest of the line. `_unquoted` skips double quotes only. I20 conflicts with `setup.link_unread` when a turn holds only the coach's own page link. Nothing checks that card phrases are verbatim, or that the card top is 3 lines and ≤500 characters.
- [run.py] "WHOLE RUN: …" inputs (setup.en.017-019, 047; liked.en.035) and fmt-short.en.007's `<<coach turns…>>` are sent as one verbatim coach turn. setup.en.043 needs a lane where links open. Standalone cases cannot be graded (setup.en.009/010, signature.en.021, message.en.022/023/028/029/030/043, brain.en.024, fmt-short.en.010). Pasted posts take a separate Day-0 turn, which puts Dana's Map exactly at turn 6.
- [kit / module owners] Is Week 1 on Free Day 0 split into replies of ≤3 pieces, and does the card print in the last Week-1 reply or in its own? (wf11 §2 and R13 say split; the kit says "all of Week 1". The 2-turn brain card cases fail if the card lands in a third reply.) Other open questions:
  - "later" right after FILM TODAY: setup.kit-order 9 or levelup.kit-next 1?
  - An edit request on FILM TODAY itself.
  - What "why?" prints right after FILM TODAY.
  - Does "why?" on a Ready piece print the record? (edge-rubric.en.033/034 assert it.)
  - An own-draft check plus `cta.platform_note` makes 2 lines under one piece (signature.en.020). A hard stop plus a copy note does the same (guardrails.en.026).
  - Is a coach with no offer (Dan) asked what he sells? (message.en.007/008/031/032/045/046 and brain.en.006/007 assume he is.)
  - Is the coach's own rewrite the intended route to a visible Draft (edge-rubric.en.002/003/020/021, guardrails.en.052)?
  - Does a buyer pattern count as "why?" evidence (research.en.027)?
  - The TikTok hook budget (voice.en.014 reads ≤9 words); email that is one-to-one vs the coaches' group greetings; typos in the written voice.
  - A mid-week `not me:`, an "I do say" or a Talk's phrases are lost before the next card reprint.
  - message.kit-map points to a KEYWORD section that does not exist.
- [strings] No string covers how "why?" shows the logged F1 Override (fmt-short.en.047, guardrails.en.068, liked.en.037) or names the voice used (voice.en.024/025). `voice.map_line` (wf14 §6) is missing. No string covers the NEXT line after "later" before the card. R17 is still on watch ("· logged." vs wf15's "· noted."). W202 lists `voice.not_me_done`, `verdict.draft_queued`, `card.stop_lines` and `film.not_filming` as unused.
- [fixtures / config / standards] Persona `answers.md` Behaviour ("fix 4") and `expected.toml` [day0]/[week1] still script the old flow. `acceptance.toml [day0]` still has `stop_point_max_minutes` 27 and `brand_card_visible_max_chars` 900 (the schema says 500). `qa/standards/message-map.md` and `core/format-checks.toml [format.message-map]` still describe the one-screen Map, and `character-card.md` may lack the voice fields. The router.en header says Day 0 is 12 Oct, but coldstart-coach's is 11 Oct. router.en.012 keeps max_chars 5600. Some S0 lanes assert wording that only the method file has (edge-rubric.en.021; liked.en.009/010; router.en.009). voice.en has no case on `connectors` or `address_1to1` yet.
