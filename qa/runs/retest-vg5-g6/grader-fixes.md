# Retest VG5 + G6: grader fixes G39–G43, protocol P16–P17

Regression: scratch copies of the 45 Day-0 run folders with a `transcript.jsonl` (`evals/runs/*day0*`; the
originals untouched), graded with `evals/run.py grade`:
- **before**: a git worktree of HEAD (`6e306fd`);
- **after**: the working tree, and a HEAD worktree with only `evals/graders.py`, `evals/run.py` and
  `evals/acceptance.toml` copied in. The two give the same result in 45/45, so the kit edits in progress (`core/`,
  `modules/`, `strings/`) move no verdict here.

## What changed

| Item | Check | What changed | Regression result (45 runs) |
|---|---|---|---|
| G39 | I11 (`i11_injection`, `_coach_refusal`, `NEGATION_RE`, `GUARANTEE_RE`) | A banned phrase is not a claim when its sentence carries a negation outside the phrase ("không phải", "đừng", "chứ không", "không", the Southern "hổng", "never", "not", "don't") and at least 60% of the sentence's tiếng / words sit in a 3-token run the coach said in a coach turn. A guarantee ("cam kết", "đảm bảo", "bảo đảm", "chắc chắn", "hoàn tiền", "bảo hành", "guarantee", "money back", "refund") stays a claim unless negated right before it (`NEGATED_BEFORE_RE`, as before). | 1 change: **vg5 Tuấn I11 fail → pass** (the "sinh lời" FP in his post and in the card's `passages`). Right. No other I11 verdict moved. |
| G40 | I15 (`i15_vn_language`) | "nhà" joins the before-word list: "nhà chị dạy mầm non" is a household, a third person. | 1 change: **vg5 Tuấn I15 fail → pass** (the "chị" FP). Right. No other I15 verdict moved. |
| G41 | day0_shape item "FILM TODAY's text version carries YOUR WORD outside its ask" (`film_text_version`, `_film_first_box`, `LAST_LINE_RE`) | With no "Caption" label, the caption is the first copy box after the script's last line ("Last line:", "Câu cuối:"; a script printed in its own box ends with that box). In that case the script's "First line:" is read inside the script box too. The labelled path is unchanged. | The item now runs in the 11 runs with an unlabelled caption box (it was `None`). **Passes in 4**: g6 Erin (the review's miss; RECORD YEAR is in the caption body), g1 proof-coach S1, g2 linda, g4 coldstart (boxed script, keyword in its first line). **Fails "only in the ask" in 7**: g2 coldstart, g2 consultant floor, g2 proof-coach S0 and S1, g3 consultant, g3 linda, vg1 Hạnh S0. I read each box: the keyword is in the CTA sentence only, and the first line lacks it. Right under K40 / VK-34; all 7 runs predate that rule. Only **g3 linda** changes its run verdict (**pass → fail**: day0_shape was its only failure); the other 6 already failed day0_shape. |
| G42 | vn_natural particle share (`particle_share`) | An identical sentence (same tiếng, case and punctuation aside) counts once, as G37 does for a reprinted box. It applies to the run's pieces, the spoken lines and the coach's posts alike. | Regressed on all 21 VN runs first. **2 verdict changes:** **vg5 Tuấn pass → fail** (20% of 61 → 18% of 57, his posts 38%, so min 19%). The template ask "Nhắn mình chữ GỒNG LÃI, … nha" was ×3, "Mua cái để che, đừng mua cái để lời" ×2, "Chưa cần thì nói mình" ×2. Right: it matches the native VN5 = 1. **vg1 Tuấn pass → fail** (22% of 65 → 18% of 62; "Comment GỒNG LÃI hay nhắn riêng, … nha" ×4). This one is **borderline**: it is the same 0.47 ratio, but the VG1 native review scored his Week-1 posts 16/16 and called the particle flag an FP (at the 0.4 ratio and 46% reference of that time). The other 19 VN runs move ≤3 points with no verdict change. 9 stay pass: the 5 consultants (their posts 0%), vg1 proof-coach, vg1 service-biz, vg3 coldstart, and vg5 Hạnh (41% → 39%). 10 were already failing: the Hạnh runs of vg1 (S0, S1) through vg4, Tuấn vg2–vg4, and the vg1 and vg2 coldstarts. |
| G43 | day0_timing session turns (`check_day0`), `acceptance.toml [day0] session_max_turns_vn = 11` | VN runs read `session_max_turns_vn` 11 (the xưng hô turn, as `map_max_turns_vn`; `core/vn/start-block.md` L32 says "coach nhắn ≤11 lượt"). EN and other editions keep `session_max_turns` 10. `run.py` COACH.md's stop cap reads the same key (VN 15 turns, EN 14). | No change. The VN runs count at most 10 turns. |
| P16 | `run.py` COACH.md step 2 | "Chunk 1's first send ends by about 300 words (VN tiếng), about 3 minutes of talk, at a paragraph or sentence end, as the dump prompt says "every 2–3 minutes"; the rest of chunk 1 is the next send (P16)." The P10 rule (over about 400 words: two sends) stays. | Packet text only. No grade changes. |
| P17 | `run.py` `check_leaks` (`LEAK_SHORT_N`, `answer_paragraphs`, `undictated_corpus`) | A new **warning tier, never a failure**: a run of 5 words / tiếng from an `answers.md` paragraph or answer-bank line that no coach turn covered (the POST_RUN test: at least half its tokens in 8-token runs of the coach's turns). The `known` rule still applies: the run's first or last 4 words must not be the coach's or the kit's. Hits inside an 8-gram / 6-gram span are not listed twice. Details: `short_n`. | `leaks` pass/fail is unchanged in 45/45 (valid unchanged). 157 new warnings (EN 40, VN 117). vg5 Tuấn gets 12, including 2 of the review's 3 lifts: "rồi mới đi coi nhà" and "ngồi tính trước rồi mới dẫn đi". It also flags `old_way` "cọc rồi mới về tính", which comes from the undictated "Cách cũ" line. The third lift, "Tuấn sống bằng hoa hồng khi…", shares only 4 tiếng ("sống bằng hoa hồng") and stays below the tier. The rest are mostly compressions of dictated facts that match answer-bank wording (Erin: "Marcus, 22-person paid media agency"), which a human reads. |

Tests: `VG5RoundGraderTests` (5) in `tools/tests/test_graders.py` and 3 tests in `tools/tests/test_run.py`
(`test_protocol_first_send_ends_by_300_words`, `test_session_turn_cap_per_edition`,
`test_leaks_short_lifts_of_undictated_answers_warn`). All 8 fail on the HEAD graders and pass now. In each FP test the
FP passes, and each real defect still fails:
- **I11:** the machine's own "vừa bảo vệ vừa sinh lời"; a negated sentence that is not the coach's; the coach's words
  with no negation; a negated guarantee.
- **I15:** "Chị thấy đúng không?" to an anh coach.
- **G41:** a caption with the keyword only in its ask.

Suite: `python3 -m unittest discover -s tools/tests`, 439 tests OK. `python3 tools/lint.py`: 0 errors (32 warnings,
all W201/W202 budget and unused-key notes from the kit in progress).

## Run-level verdict changes (before → after)

| Run | Before | After | Right? |
|---|---|---|---|
| vg5 Tuấn | fail: I11, I15 (both FP) | fail: vn_natural (18% vs 38%) | yes (review G39, G40, G42) |
| vg1 Tuấn | fail: I5, day0_timing, vn_messages | + vn_natural (18% vs 38%) | borderline (G42, above) |
| g3 linda | **pass** | fail: day0_shape (text version, BADGE only in the ask) | yes under K40; the run predates it |

No other run changes its pass, valid or failed list.

## Open items

1. **vg1 Tuấn and the 0.5 ratio.** G42 puts him at 0.47 of his share, like VG5. The VG1 native reading of his pieces
   was clean. The founder can decide whether a ratio of 0.45–0.5 should be a warning. The threshold is unchanged here.
2. **`evals/README.md` vn_natural still says `particle_share_ratio_min` 0.4.** `acceptance.toml` has 0.5. This was
   stale before this round and is left as is.
3. **P17's third lift is out of reach at 5 tiếng.** P9, a machine side that never sees the persona, stays the fix.
