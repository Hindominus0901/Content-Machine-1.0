# Retest VG4 + G5: grader fixes G31–G38, protocol P14–P15

Regression: scratch copies of the 4 run folders (`evals/runs/vg4-*`, `evals/runs/g5-*`; the originals untouched),
graded with `evals/run.py grade` three ways:
- **before**: the HEAD graders (`80e092a`, unchanged since) on the kit the runs ran on (`ce09d30`); this equals the
  stored `grades.json`;
- **HEAD graders on the new kit** (`6e61e51`, VK-33 etc.);
- **after**: the fixed graders, on both kits (same result on each).

The kit fixes for the real defects are not in these runs, so those must still fail.

## What changed

| Item | Where | Change |
|---|---|---|
| G31 | `check_day0`, `posts_only_turns` | A coach turn with more of its words in pasted `written-posts.md` paragraphs than in talk (the POST_RUN test `dump_cut` uses) is left out of the Map's turn count (DECISIONS wf14 V3: the posts "add no extra turn"). Details list it (`map_posts_only_turns`); the evidence names it. A post pasted inside a dictated chunk still counts as a send. |
| G32 | `check_day0` (early win) | An early win in the reply to the coach's first send is a warning whenever it is over budget (`first_send > limit` dropped). A later early win stays a failure. |
| G33 | `NEGATED_BEFORE_RE` | "hổng" / "hông" negate like "không": "hổng phải cam kết" is no claim. |
| G34 | `reply_decisions`, `map_topics` (I6) | A Map topic reprinted in a line (a Week-1 heading, the card top) is blanked out before the decision scan; the rest of the line is still read. |
| G35 | `_is_marker` / `_is_piece_title` (`BARE_LABEL_RE`, `_bare_label`), `_silent_end`, `analyse_reply` | A bare reply label ("Tin trả lời inbox 1", "DM reply 1", "Ai nhắn X · Tin trả lời inbox 1 (…)") starts a piece. A piece ends at its copy box: after the box, a new paragraph that is not another box or its "Caption:" ends it. The Brand Card (title, WHAT YOU SAY, heading; in a box from the box) bounds every piece. |
| G36 | `check_day0_shape`, `film_text_version` | New item "FILM TODAY's text version carries YOUR WORD outside its ask": the box under a line offering the text post (`film.now_or_text`, `film.not_filming`, "as text", "đăng chữ", "bài viết"…), else the script's first line + the caption. G30's script + caption item stays. |
| G37 | `_vn_pieces`, `pasted_posts`, `check_vn_natural` | Pieces leave out titles and bare labels, dated notes ("Lưu ý (06/10/2026): …") and the Brand Card; a chunk with more than half its tokens in POST_RUN runs of an earlier chunk (the gift, then inbox 1) counts once. The particle share compares with the `written-posts.md` posts the coach pasted in the run (all of them when none was). |
| G38 | `LIST_NAMED_RE`, `LIST_PAIR_RE` (day0_shape email item) | VN names a list by its size: "email thì có 250 người"; the card's `list_size: email 250 · Zalo khoảng 380` names both (email wins). "email thì không có" names none. |
| Kit change | `_slot_pattern`, `_cta_lit` (`PARTICLE_ANY`), `VN_SELF` | A VN particle at a clause end in a string (VK-33's "…mình gửi {gift} nhé.", `map.ok`'s "nhé") reads as any particle or none ("nha", "nghe anh"). An ALL-CAPS keyword before a comma is no longer cut as an addressee's name ("Nhắn tôi chữ TUYỂN HOÀI, tôi gửi…" → "TUYỂN HOÀI", not "TUYỂN"). |
| P14 | `evals/run.py` `check_pace` | Pasted-post paragraphs leave the dictated words and the 12-gram dictation test; each pasted post needs ≥0.5 min (`PASTE_MIN_PER_POST`). |
| P15 | `evals/run.py` COACH.md step 2, `acceptance.toml` | The packet states the cut from `[day0] dump_cut_words_<ed>`: "past about 1,200 words (VN: 1,200 tiếng) of your talk, your pasted posts not counted". The acceptance comment says "~1,200 tiếng, pasted posts left out". |

Tests: `VG4RoundGraderTests` (9) in `tools/tests/test_graders.py`, 2 in `tools/tests/test_run.py`; all 11 fail on the
HEAD graders. Docs: `evals/README.md`, the `graders.py` docstrings.

## Before → after, per run

| Run | Before | HEAD graders, new kit | After |
|---|---|---|---|
| VN Hạnh | day0_timing (Map 8/7), vn_natural (16% vs 53%) | + day0_shape "FILM TODAY has no keyword CTA" | vn_natural (19% vs 54%) |
| VN Tuấn | **invalid: pace** (135 "dictated" words in 0.7 min); I11, day0_timing (early win 4.3), vn_natural (4% vs 46%) | + the same CTA FP | **invalid: pace** (2 pasted posts in 0.7 min, needs ≥1.0); day0_shape (N3 and the text version: keyword only in the ask), vn_natural (3% vs 38%); early win a warning |
| VN consultant | I6, day0_timing (Map 8/7) | + the same CTA FP | day0_shape (text version: keyword only in the ask); the email item now runs and passes |
| EN Erin | I12, day0_timing (Map 8/6, film-ready 21.4), day0_shape (card 5,881) | unchanged | I12, day0_timing (Map 7/6, the posts turn 4 not counted; 21.4), day0_shape (card 5,881; text version: keyword only in the ask) |

Before, 10 failed checks plus 1 protocol fail: 5 real, 2 R(protocol), 3 FP. After, 7 failed checks plus 1 protocol
fail, all real: the 5 real ones from before, plus 4 grader misses now caught (inside day0_shape). FP: 3 → 0.
R(protocol): 2 → 0, under the founder call G31 follows. The kit change's CTA false positive (3/3 VN) is gone.

## Review §4, row by row

| # | Run · check | Verdict | After |
|---|---|---|---|
| 1, 8 | Hạnh, consultant VN · Map 8 (max 7) | R(protocol) | **pass**: 7, posts-only turn 5 not counted (G31) |
| 2 | Hạnh · vn_natural | R (count inflated) | still fails: 10 of 52 sentences (19%), W1+W2 54%, min 21.5% (G37; was 11 of 67) |
| 3 | Tuấn · pace | slip, wrong reason | still invalid, right reason (P14) |
| 4 | Tuấn · I11 "hổng phải cam kết" | FP | **gone** (G33) |
| 5 | Tuấn · early win 4.3, first send at 4.0 | FP | **warning** (G32) |
| 6 | Tuấn · vn_natural | R | still fails: 2 of 62 (3%), W1+W2 38% (was 3 of 79 vs 46%) |
| 7 | consultant · I6 "quyết định" in the Week-1 heading | FP | **gone** (G34) |
| 9, 11 | EN · I12 13-word first line; card 5,881 | R(m) | still fail |
| 10 | EN · Map 8 (max 6), film-ready 21.4 | R(kit) | still fail: Map 7 (max 6) after G31, 21.4 |
| miss | FILM TODAY's text version (Tuấn, consultant VN, EN) | grader miss | **caught** (G36); Hạnh's passes |
| miss | Tuấn N3, keyword only in the ask | grader miss | **caught** (G35) |
| miss | the card inside the last Week-1 piece (Hạnh, consultant inbox 2; EN short) | grader bug | **gone** (G35) |
| miss | consultant VN "Week 1 has an email" not run | grader miss | **runs, passes** (G38) |

## Other runs (the 37 G1–G4 / VG1–VG3 folders, scratch copies, before vs after on the `ce09d30` kit)

- **G36** flags the text version in 15 older runs (pre-K40), keyword only in the ask in 14 and "nowhere" in g1
  service-biz S0. Three gain a failing check from it: g2 service-biz S1, vg1 proof-coach, vg3 coldstart.
- **G31**: every Day-0 run here pastes its posts as a turn of their own, so every Map count drops by 1. The Map
  budget failure clears in 5 older runs: g1 consultant, g2 linda, g2 proof-coach S0 and S1, vg1 coldstart. g1
  coldstart floor still fails (7, max 6).
- **G35**: vg1 consultant's "Bài chữ · Thứ Ba" now fails "keyword only in the ask", because the card top had hidden
  it. I23's phrase share now fails in vg1 Hạnh S0 (43%) and vg2 Tuấn (46%): the card top's quoted phrases no longer
  count as the last piece's.
- **G37**: vn_natural now passes in vg2 coldstart (28% vs 58%) and vg3 Tuấn (16% vs 38%, W1+W2 instead of W1–W3).
- **P14**: g1 coldstart floor, already invalid, also shows a paste slip. No other pace verdict changed.

## Open items

1. **G37 and the 0.4 ratio.** Comparing with the pasted W1+W2 lowers Tuấn's reference from 46% to 38%, because W3,
   a Zalo reply, carries the particles. That is why VG3 Tuấn (16%) now passes. The guide says "below half of
   theirs", and `particle_share_ratio_min` is 0.4. The question is whether it should be raised to 0.5. VG4 Hạnh and
   Tuấn fail at either value.
2. **G31 covers the Map budget only.** `session_max_turns` (10) still counts a posts-only turn. No run here is near
   10.
3. **Paste boxes (pre-existing).** `PASTE_LABEL_RE` reads "dán y khung này làm bài viết" (Hạnh's caption) and "ready
   to paste" (Erin's gift) as paste boxes, so vn_natural and I23 never read those boxes. G36 accepts either kind.
4. **P15.** The retest workflow brief is outside the repo and still says "about 1,500 tiếng". It needs the same
   line as COACH.md.
5. **Re-runs per review §8.** Tuấn still needs a valid sample (pace).
