# Grader and protocol fixes from the VG6 / G7 retest (review §8)

Round: `review.md` §8 (Graders G44-G46, Protocol P18, and the case strings that quote `setup.plan_guess`). Not done here: G47 (optional),
the kit items, the re-runs, the founder call.

## What changed

| Item | Where | Change | Tests |
|---|---|---|---|
| G44 | `evals/graders.py` `i15_vn_language` | "chuyện" joins the before-word list ("Kể tiếp chuyện chị trong toilet nhà mẫu" is the client). The look-back window grows from 6 to 8 characters, because "chuyện " is 7 | `VG6G7RoundGraderTests.test_g44_*`: the NEXT-line and prose forms pass; "Chị thấy đúng không?", "Kể tiếp đi, chị nghe nè.", "Chuyện đó chị lo" still fail |
| G45 | `evals/graders.py` `check_vn_messages` (new `_audience_chunks(r, body_only=True)`) | The slash check runs on the piece body without its title line; the title is the coach-facing label. The DỪNG and "Dạ" checks and I15 are unchanged | `test_g45_*`: Tuấn's title passes; "Chào anh/chị," inside the box, "anh/chị" mid-message and a box under a plain label still fail |
| G46 | `evals/graders.py` `check_day0_shape` (new item, `GUESS_TAG_RE`) | "YOUR WORD carries the guess tag unless the dump quotes it from 3+ named clients". Reads `expected.toml [keyword] day0_heard`: `false` needs the tag on the first printed Map's keyword, `true` needs none. Runs only with the key (a bool) and a Map. A tag counts with or without brackets ("(my guess", "(mình đoán, Tuần 1 kiểm lại)", "· em đoán, …"); a source note is not a tag | `test_g46_*` (5): untagged fails, all tag forms pass, notes do not count, `true` flips it, no key / no Map / non-bool = not run, the first Map decides (a later coach change needs no tag), the VN Map |
| G46 data | `evals/personas/*/*/expected.toml` (13 files) | `[keyword] day0_heard = false` in all 13, with a reason line each (table below) | |
| P18 | `evals/run.py` (`run_date`, `--today` default) | MACHINE.md says "Today's date: Tuesday 6 October 2026" from `--today`, else the persona's `day0` (time kept: "Monday 12 October 2026, 06:45"), else the day the packet is made. "the date in the transcript" is gone | `test_run.RunPackets.test_p18_*`; the old `2026-10-06` assert now reads the weekday form |
| Cases | `evals/cases/setup.en.toml`, `router.en.toml` | Every regex and note quoting "(my guess; one word changes it)" now matches "(my guess, where unheard; one word changes it)" (setup 16 places, router 4). The optional-follow-up regexes accept both forms | `test_graders` plan fixture (L1933) updated; `test_g8` item list gets the new item (not run without the key) |

`tools/tests/test_checks.py` L189 still quotes the old tail as a `_GUESS_AFTER` sample. It still passes (not in this task's file list); the new text matches the same pattern (35 characters after the comma, limit 40).

## Ground truth: `day0_heard`

All 13 are `false`: no dump gives the buyer phrase from 3+ named clients. The 4 that had no check before are first.

| Persona | Phrase | Why not heard |
|---|---|---|
| vn/hanh | ngại chào | Thảo only; "bao nhiêu em nói y hệt" is anonymous (Loan quotes another phrase) |
| vn/tuan | gồng lãi, dí cọc | The toilet caller (no name) + "khách nói hoài", "bảy tám nhà" |
| vn/consultant | tuyển hoài | The seafood-chain owner + 3 anonymous lines. **Rests on founder call (a)**; flip to `true` if the founder counts them |
| en/consultant | record year | Marcus + "all of them say some version of it". **Same founder call** |
| en/coldstart, vn/coldstart | keep up, cứng đơ | No clients; unnamed people only |
| en/linda | without the badge | Renée only |
| en/proof, vn/proof | one more chapter, lãi ảo | Lorraine only; Ngân only |
| en/service, vn/service | nothing room, phát sinh | Megan Whitfield only; chị Loan only |
| heldout en / vn | the crib is lava, tăng xông | Courtney only; mẹ bé Su only |

## Regression: 49 `evals/runs/*day0*` folders with a transcript, graded as scratch copies

Before = a `git worktree` of HEAD (removed afterwards); after = this tree. `vg7-*` has no transcript and is skipped. Totals: all-pass 4 → 1 of 49.

| Change | Runs | Right? |
|---|---|---|
| I15 fail → pass | vg6 Tuấn | Yes. The only I15 evidence was "chuyện chị" (the client) in the T3 NEXT line |
| vn_messages fail → pass | vg6 Tuấn | Yes. The only evidence was "chị/anh" in the title "Hỏi 3 khách cũ … đổi chị/anh cho đúng người" |
| day0_shape new item fails, run was all-pass | g7 Erin, vg6 Khoa, g4 Dan | Yes. "YOUR WORD" untagged; Dan has no clients, Erin and Khoa each have one named client plus anonymous lines (founder call (a)) |
| day0_shape new item fails, check was passing but the run already failed elsewhere | vg6 Hạnh, vg6 Tuấn, g2 Linda, vg1 Tuấn, vg4 Hạnh | Yes. Same reason; vg6 Hạnh and Tuấn also still fail `vn_natural` |
| day0_shape new item fails, check already failing for other items | 26 runs (g1-g3 EN, vg1-vg5 VN) | Yes. Extra evidence line only; the verdict does not move |
| New item passes (keyword tagged) | 15 runs: g1 Erin/Dana/Corinne S1, g2 Dana/Corinne S1, g3 Dana S1, g5/g6 Erin, vg1 Minh Anh and Hạnh, vg2 Minh Anh and Tuấn, vg3 Minh Anh, vg5 Hạnh and Tuấn | Yes. "(my guess)", "(mình đoán, …)", "(em đoán, …)" or the unbracketed "· mình đoán, Tuần 1 kiểm lại" |
| Any other verdict | none. No other check or item changed in any run | |

The new item fails 34 of 49 runs and passes 15, and never reads "not run" here (all 13 personas have the key and every run printed a Map). The 4 retest runs (vg6 ×3, g7) all fail it, as the review says ("4/4 untagged passed `day0_shape`").

## Checks

- `python3 -m unittest discover -s tools/tests`: 460 tests, OK (9 new). Against HEAD's graders and run.py the 9 new tests fail, so they test the change.
- `python3 tools/lint.py`: 0 errors (the 31 warnings are the budget notes of the `dist/` build; HEAD's worktree has 16 without `dist/`).
