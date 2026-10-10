# VG1 VN Day-0: grader fixes, before and after

The graders were fixed per review.md §8 "Grader fixes" (VG-1–VG-16). The EN round's G11–G18 and P8, done in the same
pass (`../g2-en-day0/grader-fixes.md`), apply to VN as well. Files: `evals/graders.py`, `tools/cmcore/checks.py`,
`evals/run.py`, `evals/acceptance.toml` and their tests.

How the regression was run:
- Scratch copies of the 7 run folders were graded twice. The run folders in `evals/runs/` were not touched.
- "Before" is the grader at HEAD (`c4c6298`). It gives the same verdicts as the stored `grades.json`.
- "After" is the fixed grader. Both use the HEAD strings, which are the strings the transcripts were made with.
- The working tree's strings give the same verdicts. Every check reads kit wording from `strings/vn.toml` keys: the
  map labels, `map.ok`, `cta.*`, `cmd.*`, `card.*`, `film.now_or_text`, `setup.dump_posts` and `message.pushback.who`.
- Labels: R, R(kit), R(m), R (soft) and FP are the review's, from §1 and §5.

## Result

- **False positives: all 23 are gone.** That is I15 ×7, day0_shape ×5 runs (7 items), I11 ×4, I23 ×2,
  vn_natural ×2, I6, I9 and day0_timing.
- **Real defects: 8 of 9 still fail.**
  - The ninth is Tuấn's quit_triggers. VG-14 reads his own quit list, which leaves out "two questions" (his
    "Dễ rối" list has it). So the check now passes with status "warn", and the item sits under "confusions".
  - The defect itself, `setup.multi_income` asking two questions, still fails I5.
- **New detections: the review's "graded nowhere (real)" list.** The new `vn_messages` check and VG-6 / VG-7 catch
  them:
  - "DỪNG" in an inbox reply (proof, service-biz, Tuấn);
  - "anh/chị" in the consultant's 4 messages;
  - "Dạ" from chị to em (proof, Hạnh S1);
  - a Northern "nhé" in the dump prompt to a Southern or Central coach (coldstart, consultant, service-biz, Tuấn);
  - coldstart's card top inside the copy box, and its "[động tác 1–3]" and "[dán quà]" blanks.
- **Proof-coach now fails only `vn_messages`.** Both of those items are real per the review.

## Per failed item (review §1, §5)

| Run | Check · item | Label | Before | After |
|---|---|---|---|---|
| proof | I15: inclusive "mình", "thì tìm mình" on the Map and card lines, "than" | FP | fail | pass ✓ (VG-1, VG-2) |
| proof | day0_shape · YOUR WORD `LÃI ẢO (không dấu: LAI AO)` | FP | fail | pass ✓ (VG-3) |
| proof | day0_shape · save backup `Dự phòng: … Zalo "Cloud của tôi"` | FP | fail | pass ✓ (VG-5) |
| proof | vn_natural, 14% (direction lines counted) | FP | fail | pass ✓ (VG-12: written 23%, floor 15%) |
| coldstart | I15: "than", "IT", `why_this_one`, "(vd chị trưởng phòng …)" | FP | fail | pass ✓ |
| coldstart | day0_timing: Map at 8, 11 coach turns | R(kit + m) | fail | fail ✓ |
| coldstart | day0_shape · YOUR WORD `CỨNG ĐƠ · không dấu: … (mình đoán, …)` | FP | fail | pass ✓ |
| coldstart | day0_shape · `[Tên]`, `[tên]` | R(m) | fail | fail ✓ |
| coldstart | vn_natural, written 16% against her 64% | R (soft) | fail | fail ✓ (VG-12) |
| consultant | I8: "200 triệu, 70%, 80%, 6 tháng lương" in proof | R(m) | fail | fail ✓ |
| consultant | I9 `"Cloud của tôi"` | FP | fail | pass ✓ (VG-9) |
| consultant | I11: "không phải cam kết", "tốt nhất" in principles, "số 1" in rhythm | FP | fail | pass ✓ (VG-10) |
| consultant | I15: "tôi" on the numbered Map line, "Mình chạy thử…", "Mình vẫn giữ…" | FP | fail | pass ✓ |
| consultant | day0_timing: "the Map has 0 labelled lines" | FP | fail | pass ✓ (VG-8: 4 lines) |
| consultant | day0_shape · no CTA found ("tôi gửi") | FP | fail | pass ✓ (VG-4) |
| consultant | day0_shape · save backup | FP | fail | pass ✓ |
| service-biz | I6: "em chỉ chọn viết cho ai" (`message.pushback.who`) | FP | fail | pass ✓ |
| service-biz | I15: "than" | FP | fail | pass ✓ |
| service-biz | day0_shape · no CTA found ("nhắn riêng Trang, tụi em gửi") | FP | fail | pass ✓ |
| service-biz | day0_shape · save backup | FP | fail | pass ✓ |
| Hạnh S1 | I11: "cam kết" (negated), "trị dứt điểm" (card top never-list) | FP | fail | pass ✓ |
| Hạnh S1 | I15: "than", "Mình chạy thử…" | FP | fail | pass ✓ |
| Hạnh S1 | I23: "không giảm sốc" (her own words) | FP | fail | pass ✓ (VG-11) |
| Hạnh S1 | day0_timing: film-ready at 20.2 | R | fail | fail ✓ |
| Hạnh S1 | day0_shape · CTA read as "riêng" | FP | fail | pass ✓ |
| Hạnh S1 | day0_shape · save backup | FP | fail | pass ✓ |
| Tuấn | I5: `setup.multi_income`, 2 questions | R(kit) | fail | fail ✓ |
| Tuấn | I11: "không phải cam kết (gì hết)" | FP | fail | pass ✓ |
| Tuấn | I15: "mình" on the Map, card and OK lines, "than" | FP | fail | pass ✓ |
| Tuấn | quit_triggers: 2 questions | R(kit; "a confusion, not a quit, for him") | fail | **pass, status warn** (VG-14) |
| Tuấn | day0_shape · YOUR WORD `GỒNG LÃI (không dấu: …)` | FP | fail | pass ✓ |
| Tuấn | day0_shape · save backup | FP | fail | pass ✓ |
| Tuấn | vn_natural, 14% | FP | fail | pass ✓ (written 22%, floor 18%) |
| Hạnh S0 | I11: "không phải cam kết" | FP | fail | pass ✓ |
| Hạnh S0 | I15: "than" | FP | fail | pass ✓ |
| Hạnh S0 | I23: "không giảm sốc gì hết", "ký trong ngày thì giảm sốc" (both hers) | FP | fail | pass ✓ |
| Hạnh S0 | day0_shape · CTA read as "ok" from the TIẾP line | FP | fail | pass ✓ (VG-4) |
| Hạnh S0 | day0_shape · save backup | FP | fail | pass ✓ |
| Hạnh S0 | day0_shape · `[Tên]` | R(m) | fail | fail ✓ |
| Hạnh S0 | vn_natural, written 13% against her 53% | R (soft) | fail | fail ✓ |

The vn_natural shares of the written pieces match the review's: proof 23% (22%), Tuấn 22% (21%), coldstart 16% (15%)
and Hạnh S0 13% (13%). The spoken lines' share is now in `details.spoken_particle_share` (proof 0%, Tuấn 0%) and is
never compared.

## Per run

| Run | Failed before | Failed after | New items after |
|---|---|---|---|
| proof | I15, day0_shape, vn_natural | vn_messages | DỪNG in "Quà + tin trả lời inbox 1"; "Dạ, chị gửi em cách soi lãi thật…" |
| coldstart | I15, day0_timing, day0_shape, vn_natural | day0_timing, day0_shape, vn_natural, vn_messages | card top inside the copy box; `[động tác 1–3]`, `[dán quà]`; "Bạn cứ xả hết ra nhé" to a Nam coach |
| consultant | I8, I9, I11, I15, day0_timing, day0_shape | I8, vn_messages | "anh/chị" in 4 messages; "Anh cứ xả hết ra nhé" to a Trung coach |
| service-biz | I6, I15, day0_shape | day0_shape, vn_messages | the whole card 7,078 characters (VN max 6,600; not in the review); DỪNG in an inbox reply; "nhé" to a Trung coach |
| Hạnh S1 | I11, I15, I23, day0_timing, day0_shape | day0_timing, vn_messages | "Dạ, chị gửi em 3 bước…" |
| Tuấn | I5, I11, I15, quit_triggers, day0_shape, vn_natural | I5, vn_messages | DỪNG in an inbox reply; "nhé" to a Nam coach |
| Hạnh S0 | I11, I15, I23, day0_shape, vn_natural | day0_shape, vn_natural | none |

Counts:

| Grade | Failed items | False positives | Real defects |
|---|---|---|---|
| Before | 32 | 23 | 9 |
| After | 8 + 13 new | 0 | 8 carried over (Tuấn's quit_triggers moved to "confusions") + 13 new |

The 13 new items, all real per the review's "graded nowhere (real)" list or §6:
- `vn_messages` ×10: DỪNG ×3, anh/chị ×1 (4 messages), Dạ ×2, a Northern particle ×4;
- coldstart's card top in the box ×1;
- coldstart's blanks ×1 (4 blanks, added to the placeholder item that `[Tên]` already failed);
- service-biz's whole card ×1. This is the schema budget; the review did not measure it.

## What each fix does on these runs

- **VG-1.** The English scan leaves out "than" (Vietnamese: to complain), ALL-CAPS words ("IT") and card field names
  (`why_this_one`).
- **VG-2.** The pronoun scan leaves out three kinds of line:
  - a line that opens with the Map's KNOWN FOR label (numbered or not) or the card's NÓI GÌ (`card.visible.what`);
  - the Map's OK line (`map.ok`);
  - text in brackets.
- **VG-2, inclusive "mình".** "mình" as the inclusive "we" no longer counts when the pair has no "mình". Its clause must
  not put the coach's form after it, except as a vocative after a particle ("…nghe anh"). "Mình gửi anh Tuần 1" still
  fails (tested).
- **VG-3.** `word_head()` cuts "(không dấu: …)", "· không dấu …", "(… đoán …)" and ", em đoán …".
- **VG-4.** In the CTA strings:
  - the pronoun reads as any self-form: tôi, tui, em, chị, anh, tụi em, or a name;
  - "hay" also reads "hoặc";
  - an addressee may come before the comma ("nhắn riêng chị,", "nhắn riêng Trang,").
  The NEXT line is never read, and a command word (`cmd.*`) or "riêng" is never the keyword.
- **VG-5.** The backup line reads "dự phòng", "Cloud của tôi" and "gửi/chép … Zalo".
- **VG-6.** The card is found when its top sits in a copy box. The card-top item then fails, "the card top is inside the
  copy box with the machine block".
- **VG-7.** In VN runs, a short bracketed text is a blank. Tags, links and brackets the kit's own strings print
  ("[nơi · tháng]") are not.
- **VG-8.** Map labels may carry "1 " / "1." / "1)", and a "BẢN ĐỒ" heading is ignored. The consultant's Map has 4
  lines.
- **VG-9.** A quote of the kit's own wording ("Cloud của tôi") is not checked by I9.
- **VG-10.** I11 skips four things:
  - a banned phrase right after a negation ("không phải cam kết");
  - the card top's never-list (`card.visible.never`);
  - the card's `principles` value;
  - the card's `rhythm` value.
  "cam kết có người trong 60 ngày" still fails (tested).
- **VG-11.** A never-word used as the coach said it in the run (the word with 2 neighbouring words) is theirs. This
  covers "không giảm sốc gì hết" and also her "ký trong ngày thì giảm sốc" in Hạnh S0's long post. The I23 phrase share
  also reads the card's `phrases` / `openers_closers` (only those the coach said in the run; the keyword never counts).
  Without that, the long post and the inbox replies that VG-15 now splits off would have dropped Hạnh S1 to 3 of 7.
- **VG-12.** `split_script()` sorts each line of a piece:
  - direction lines are dropped ("Chữ trên màn hình", "Khung hình đầu", "Cảnh n", "chữ:", "On-screen", "First
    frame");
  - "Ý n" beats are dropped with beat-card delivery;
  - "Câu đầu" / "Câu cuối" are spoken;
  - the rest is written.
  The particle share compares the written lines with written-posts.md.
- **VG-13, new check `vn_messages`.** It has four items:
  - "anh/chị" in a message box;
  - DỪNG / "nhận tin nữa" in a one-to-one reply (inbox, Messenger, "trả lời"); a Zalo series is exempt;
  - "Dạ" opening a line where the coach writes as chị / anh to an em;
  - "nhé / nhỉ / đấy / cơ" in the dump prompt to a persona whose `dialect` is Nam or Trung.
- **VG-14.** quit_triggers reads the persona's own quit list ("Bỏ ngang khi:", "Quits if:", persona.toml "quits on …").
  A generic trigger that the list leaves out is reported under "confusions" with status "warn". The EN floor's wall of
  text is on its persona's list, so it still fails.
- **VG-15.** Two more title shapes start a piece:
  - sentence-case titles that open with a format and carry a "·" ("Bài dài · thứ Sáu, 09/10 · Facebook", "Tin trả lời
    inbox 1 · …", "Quà + tin trả lời inbox 1 · …", "Zalo · thứ Năm …");
  - day-first titles with a dd/mm date ("Thứ Tư, 07/10 · Zalo").
  The long posts no longer merge into N1.
- **VG-16.** The summary prints active film-ready minutes, the clock in brackets: Hạnh "19.9 (44.9)" and "20.2 (45.2)".
- **G15 early win.** It came 5.6–7.5 active minutes after the dump prompt, each time in the reply to the coach's first
  send. The personas sent that first chunk at minute 5.1–7.4. These are warnings, with the minutes in
  `details.early_win` (VP-4: graded against the persona's real send). Session minutes are 23.2–32.2, all within 40.

## Choices to know

- **Tuấn's quit_triggers is the one R that no longer fails.** VG-14 asks for exactly this. The defect stays visible in
  I5 and in `quit_triggers.confusions`.
- **The keyword-once check (EN G17) is not run on VN.** acceptance `[week]` scopes it to EN, and nobody has reviewed VN
  pieces against the rule.
- **service-biz's 7,078-character card** is a new failure from EN G14, on the VN budget of 6,600 in
  `platform/targets.toml`. Tuấn's card is 6,591, just under.

## Not done here

VP-1 to VP-5 are simulator and persona work outside the grader files: the Free-plan rule in COACH.md, a channel-and-list
sentence early in the dump, "chấm" in chunk 2, chunk length and note classification. The reviewer-only items stay with
a reader:
- "nhắn riêng Trang";
- a gift promised in today's caption before it exists;
- the "cam kết" register;
- the naturalness scores in §6.

## After the fix round

Graded at the end of the fix round (6 Oct), after the verify pass hardened VG-2, VG-13, G13, G18 and P8 (397 tests
OK).
- Scratch copies of the 7 run folders were graded twice with the final `evals/graders.py` / `evals/run.py`. The
  run folders in `evals/runs/` were not touched.
- **HEAD strings:** a scratch root with `strings/*.toml` from `c4c6298`, the strings the transcripts were made with.
  Everything else is the working tree.
- **Final strings:** the working tree as is.
- **With HEAD strings the result matches the "After" column above item for item.** With the final strings it does
  not, for one reason: the new `setup.dump_posts` (VK-12 cut) no longer matches the old transcripts' dump prompt, so
  the graders cannot find it (see the last two columns).

| Run | Failed checks (HEAD strings) | Failed items | Map turn | Film-ready | Early win (first send) | Kit fix that targets it | Final strings differ |
|---|---|---|---|---|---|---|---|
| proof | vn_messages | DỪNG in inbox reply 1; "Dạ, chị gửi em…" | 6 | 17.6 | 7.1 (6.9) | VK-6; VK-8 | day0_timing fails: early win timed from turn 1 |
| coldstart | day0_timing, day0_shape, vn_natural, vn_messages | Map at 8, 11 turns; card top in the box; `[động tác 1–3]`, `[dán quà]`, `[Tên]`, `[tên]`; written particles 16%; "nhé" to a Nam coach | 8 | 18.4 | 6.5 (6.3) | VK-4, soft cut, K30; none (slip); VK-7, VK-19; none (soft); VK-12 | the "nhé" item is not run |
| consultant | I8, vn_messages | trap "200 triệu" in proof; "anh/chị" in 4 messages; "nhé" to a Trung coach | 7 | 19.9 | 7.5 (7.4) | VK-13; VK-7; VK-12 | day0_timing fails; the "nhé" item is not run |
| service-biz | day0_shape, vn_messages | whole card 7,078 (max 6,600); DỪNG in an inbox reply; "nhé" to a Trung coach | 7 | 17.7 | 7.2 (7.0) | none (K29 not mirrored to VN); VK-6; VK-12 | day0_timing fails; the "nhé" item is not run |
| Hạnh S1 | day0_timing, vn_messages | film-ready 20.2; "Dạ, chị gửi em 3 bước…" | 6 | 20.2 (45.2) | 5.6 (5.5) | soft cut (~1,500 tiếng); VK-8 | none |
| Tuấn | I5, vn_messages | `setup.multi_income` 2 questions; DỪNG; "nhé" to a Nam coach | 7 | 18.2 | 7.1 (7.0); quit_triggers warn | VK-3; VK-6; VK-12 | day0_timing fails; the "nhé" item is not run |
| Hạnh S0 | day0_shape, vn_natural | `[Tên]`; written particles 13% | 7 | 19.9 (44.9) | 5.6 (5.1) | VK-7; none (soft) | day0_timing fails |

Early win: every run missed the 4-minute budget, each time in the reply to the coach's first send (minute in
brackets), so G15 records a warning in `details.early_win`; day0_timing shows status "warn" where nothing else fails
it. All 7 runs are valid. Counts with HEAD strings: 8 carried real items + 13 new, 0 false positives, as in the "After"
table above.

The final-strings column is an artefact of re-grading old transcripts with new kit strings. A VG2 re-run carries the
new `setup.dump_posts`, so the dump prompt is found again. Until then, grade VG1 runs with HEAD strings (a scratch
root with `strings/*.toml` from `c4c6298`, passed to `evals/run.py --root`).

Still open for the graders:
- The dump-prompt finder keys on the `setup.dump_posts` text only, so any later rewording of that string breaks
  timing on older runs again. A second anchor (the mic tip or the topic hint list) would make it robust.
- G15 warns rather than fails when the early win comes in the reply to the first send (founder's call).
- DỪNG in an outbound one-to-one Zalo message ("gửi riêng 3 học viên cũ") is not flagged; the kit (fmt-short 6.3) is
  ambiguous on Zalo to acquaintances.
- The service-biz whole card (7,078 > 6,600) has no VN kit fix: K29's trim order needs about 38 B the method file
  does not have.
