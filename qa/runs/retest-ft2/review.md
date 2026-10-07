Result: FAIL

# Retest FT2 (founder-test fixes, round 2, Day 0, web lane): independent review

Reviewer: independent, bilingual (EN, plus native Vietnamese for the VN half). I wrote neither the kit nor the runs.
Rubrics: `qa/standards/hook-lab.md`, `research-brief.md` (LN1–LN7), `strategy-doc.md`, `vn-naturalness.md`.
Previous round: `qa/runs/retest-ft1/review.md`.

**Why FAIL:** there is nothing to pass. The three FT2 packets were built at 06:30 and never played:
- The run list handed to this review is empty, and the simulator summaries are `[]`.
- Each folder holds only `meta.json` and `packet/`: no `transcript.jsonl`, no `notes.md` (so no `## Research log`), no `grades.json`.
- The folders are `evals/runs/ft2-day0-{en-consultant, vn-copywriter-thin, vn-hanh-android-free-nocomputer}-S1-web-r1`.

Extraction, research yield, hooks, the strategy document, VN wording in pieces, the rules and the grader results all
need a transcript. None exists, so none of them can be scored. Missing evidence is never a pass.

What I could check without a transcript, and did:
- **Packets.** The kit files are byte-identical to `dist/{en,vn}/`. `Level-ups/*.md` now ship (RESEARCH, STRATEGY,
  PLAYBOOK, LAUNCH, BOARD), and the `web` lane option is on.
- **Fix list.** Each of the 13 FT1 fixes, checked in the built kit.
- **Graders.** The current graders re-run on scratch copies of the FT1 transcripts, to separate real fails from false positives.
- **Tests.** `python3 -m unittest discover -s tools/tests`: 531 tests, OK.
- **Kit text.** The coach-visible VN strings and the strategy-document template, read against the rubrics.

## Scorecard vs retest-ft1

| Area | retest-ft1 | retest-ft2 | Change |
|---|---|---|---|
| Runs played / valid | 3 / 2 (copywriter invalid: `pace`) | **0 / 0** (packets only) | worse: no evidence |
| (1) Extraction §CM-DIG | PASS (dig fired thin, stayed out rich) | not judged | kit: `dig.proof` now one ask; `dig.buyer` still two (§5) |
| (2) Research LN1–LN7 | FAIL (10, 12, 12 /14) | not judged: 0 queries, 0 pages, 0 lines logged | kit: Level-ups shipped, web lane on, query/reporter/"Line 1 from" rules in |
| (2) Research changed the Map | 0/3 | not judged | — |
| (3) Hooks passing hook-lab | 7/16 | not judged: 0 printed | kit: VN hook trio + flat-claim counter-example in core; `hook_lab` grader added |
| (3) Founder's flat line gone | not fixed ("Vậy chưa phải nghiên cứu") | not proven in a run | kit: TRƠN "Đó không phải nghiên cứu." named as a fail in §CM-FORMATS 1 |
| Strategy document (SD1–SD10) | not in scope | **not produced, and could not be**: the Day-0 script stops at Week 1 and no strategy-doc case exists | new gap (§4) |
| VN pieces 100% Vietnamese | PASS | not judged | kit: English-dictated speech retold without quote marks (§CM-NATURAL 1) |
| VN naturalness (`vn_natural`) | FAIL (7% vs 20%; 16% vs 54%) | not judged | kit: particles counted per piece (ship.kit 4, §CM-NATURAL 4) |
| ≤1 question per reply | PASS (minor: `dig.proof`) | not judged | `dig.proof` fixed; `dig.buyer` and `proof.intake` still ask two things |
| Keyword specific, buyer words | PASS | not judged | — |
| Week 1 only after OK | PASS | not judged | kit: "TUẦN 1 chỉ khi OK" / "OK, next, go → all of Week 1" |
| Grader fails: real / FP | 6 real + 1 simulator · 4 FP classes | no grades | FT1 transcripts re-graded now: **0 FP**, every fail real (§6) |
| FT1 fix list landed | — | 11 of 13 in full, 1 partial (5), 1 not done (13: the re-run) | — |
| Coach download zips | — | stale: built 02:31, before the fixes; no PLAYBOOK file | new risk (§7) |

## 1. Extraction (§CM-DIG): not judged; kit read

No dig happened. The kit now holds the FT1 fix:
- `dig.proof` asks one thing: "Làm với bạn xong, khách đó khác đi thế nào?" / "What changed for that client after
  working with you?"
- The client's OK moves to the Week-1 ask-3 message (§CM-DIG 1: "khách cho kể chưa: hỏi ở tin hỏi 3 khách cũ, Tuần 1").

Left over: the NGƯỜI MUA / BUYER question has the shape `dig.proof` had in FT1, two asks under one question mark:
- VN: "Được nhân bản một khách thì bạn chọn ai, lúc mới tìm tới bạn họ đang ra sao?"
- EN: "If you could clone one client, who would it be, and what was going on when they found you?"

It is asked last of the six, so it fires only on the thinnest dumps (the copywriter persona).

## 2. Research: not judged; kit and lane read

- **Not judged:** queries, places, pages, verbatim lines, KEEP/WATCH, and the grounding of the Map line. Every one
  needs `## Research log` in `notes.md`, which does not exist. No line could be re-fetched.
- **Ready for a real test this time:**
  - `RESEARCH-{EN,VN}.md` ship, so §CM-LISTEN can load.
  - MACHINE.md carries the `WEB_ON` lane text, not "Searching the web is not possible".
  - §CM-RESEARCH-LITE now says:
    - "cụm nào cũng kèm vai hay nơi của khách"
    - "bỏ … lời báo thuật lại ("… cho biết")" / "drop … a reporter's retelling"
    - EN "Line 1 from: {role, place | your client}", which matches VN "nguồn dòng 1 theo vai"
    - "nghe xong không đổi gì: 1-2 dòng"
- **Still the harness limit:** the lane is search + fetch, not a browser. Facebook groups, TikTok comments and Zalo stay
  unreadable, so expect LN2 at 1 and KEEP lines only where forums and news comments reach the buyer.

## 3. Hooks and headlines: 0 printed, 0 scored

There is no hook to score. The three weakest FT1 hooks, with what in the current kit would stop each one:

| FT1 hook (quoted) | What blocks it now | Proven? |
|---|---|---|
| Nhi N3: chữ "Vậy chưa phải nghiên cứu" · câu đầu "Em nghiên cứu rồi." Mình hỏi làm gì. | §CM-FORMATS 1: "Phán suông ("Đó/Vậy không phải…", "…phải tin bạn", "Nếu X thì Y") trượt, cả ở chữ trên màn hình lẫn dòng 1 caption", with its TRƠN/HAY pair; §CM-NATURAL 1 retells English-dictated speech without quote marks. Grader `hook_lab` flags it (flat claim on screen + in caption line 1) | grader yes, kit no |
| Hạnh N1: chữ "Khen tay nhẹ rồi mất hút" = câu đầu "Khách khen tay em nhẹ mà cứ để chị về suy nghĩ rồi mất hút." | §CM-FORMATS 1 "chữ trên màn hình ≤6 tiếng (đếm) ≠ câu đầu, nói điều câu đầu chưa nói"; ship.kit 3 "chữ trên màn hình ≠ câu đầu". Grader flags it (100% of on-screen words repeated) | grader yes, kit no |
| EN Wed post: "If your margin's broken, growing just makes the hole bigger, faster." | §CM-POSTS 1: "a scene, a buyer's line or their number, never an "If X, Y" maxim"; GATES now allow "a hook the last line answers, a real quote" | kit no |

The FT1 rewrites still stand (`retest-ft1/review.md` §3). The VN core example is a clean pass on HL1–HL8:
- chữ "AI đâu có gặp khách bạn"
- khung đầu: chat AI gõ dở
- câu đầu "Đọc vài bài, hỏi AI một câu, vậy mà gọi là hiểu khách?"
- câu cuối "Hiểu khách là nghe họ kể, tới lúc họ nói ra câu bạn không đoán được."

## 4. The content strategy document: not produced

- **Why there is none.** It is offered only on Week 1's NEXT ("Muốn có cả chiến lược trong một file thì gõ 'chiến
  lược'." / "Want your whole strategy in one document? Say 'strategy'."). An app that creates files saves it instead.
  The Day-0 coach script (`COACH_DAY0` in `evals/run.py`, step 6) says "Stop when the machine has delivered Week 1 and
  the Brand Card", and `evals/cases/` has no `strategy-doc` case. So SD1–SD10 cannot be scored in this suite, even once
  the runs are played.
- **Template read against `strategy-doc.md`** (`Level-ups/PLAYBOOK-{EN,VN}.md`):
  - 7 parts, in order, with the rubric's VN headings ("1. Bạn giúp ai, và vì sao là bạn" … "7. Dùng file này thế nào").
  - Grounded: "NGUỒN, chỉ những thứ mình đang giữ", [CẦN BẠN: …] / "(mình đoán)" in place, "Ngày 0 không hỏi gì".
  - Big ideas distinct and on the Map: SOÁT THẦM "3 ý không trùng nhau, khớp Bản đồ", "không thêm ý thứ 4".
  - Ladder and time: "comment {TỪ KHOÁ} → inbox → nhận {quà} → nhắn Zalo hay gọi → sản phẩm, giá nói thẳng", "lean ≤60 phút/tuần".
  - Two gaps:
    - **Rubric/decision clash.** DECISIONS (7 Oct) allows "content pillars" once, in part 3's heading: "3. Ba ý lớn
      của bạn (content pillars)" / "3. Your 3 big ideas (content pillars)". `strategy-doc.md` still lists "pillar" as a
      hard-gate jargon fail (line 45), still asks "no 'pillar' … in sight" in its runtime check, and its VN note
      heading omits the parenthesis. A judge following the rubric would fail every document on the founder's own heading.
    - SD8's "≥3 gives per ask" is not in either template.

## 5. VN wording: 5 coach-visible lines that still read translated

No VN piece was written this round, so these come from the kit. Each line prints verbatim to the coach or their client.

| # | Line (where) | Why it reads translated | Fix |
|---|---|---|---|
| 1 | "Bạn nghĩ tới người khách bạn giúp được nhiều nhất nhé. Tuần đầu tìm tới bạn, họ đang kẹt chuyện gì?" (`dig.story`, §CM-DIG 3) | "Think of one client…" with "nhé" added; "Tuần đầu tìm tới bạn" is "the week they first got in touch" word for word | "Bạn nhớ lại người khách bạn giúp được nhiều nhất. Hồi mới tìm tới bạn, họ đang kẹt chuyện gì?" |
| 2 | "Được nhân bản một khách thì bạn chọn ai, lúc mới tìm tới bạn họ đang ra sao?" (`dig.buyer`) | "If you could clone one client": "nhân bản" is lab talk. Also two asks | "Khách nào làm bạn ước có thêm chục người y vậy?" (the "hồi mới tìm tới" ask waits for the next reply) |
| 3 | "Làm với bạn xong, khách đó khác đi thế nào?" (`dig.proof`) | "What changed for that client" mapped onto "khác đi thế nào" | "Làm với bạn xong, giờ khách đó ra sao rồi?" |
| 4 | "Nhờ bạn một chút: mình đang viết lại cách giới thiệu công việc, muốn lấy đúng câu của bạn." (`research.ask3`, sent to a past client) | "I'm rewriting how I describe my work and want your words": "cách giới thiệu công việc" is stiff, and "lấy đúng câu của bạn" sounds like taking something | "Cho mình nhờ chút xíu: mình đang sửa lại phần giới thiệu, muốn dùng đúng lời khách nói." |
| 5 | "…mỗi video chép 20 comment của người rõ là {buyer}, bỏ người bán." (`research.paste_steps`) | "by people who are clearly {buyer}" | "…mỗi video chép 20 comment của người nhìn là biết {buyer}, người bán thì bỏ qua." |

Runner-up: `month.check` 3 "điều từng nói công khai" ("said in public") → "điều bạn từng nói trên trang".
Budget: the VN method file is 56,268 of 56,320 B, so fixes 1–3 must not grow it. Together they save 47 B (row 1: 7,
row 2: 38, row 3: 2).

## 6. Rules and grader failures

- **Rules in the kit** (not exercised):
  - ≤1 question: two strings still ask two things, `dig.buyer` (§1) and `proof.intake`:
    - VN "Kết quả này có lưu lại không, khách đã nhắn đồng ý cho đăng bài, quảng cáo chưa?"
    - EN "Is it on record, and did the client OK it in writing…?"
  - The keyword rule is unchanged.
  - Week 1 only after OK: held in both kits.
- **FT2 grades:** none. `grade` was never run, because there was no transcript.
- **The current graders, re-run on scratch copies of the FT1 transcripts.** This is the best evidence this round:

| Run | Fails now | Real / FP |
|---|---|---|
| VN copywriter | I9, I23, `quit_triggers`, `vn_natural`, `hook_lab`, invalid: `pace` | all real. `hook_lab` names "Vậy chưa phải nghiên cứu" and "Một email, 180 người" (on-screen = first line) and the flat claim in the caption: exactly the FT1 hand score |
| VN Hạnh | `vn_natural`, `hook_lab` | real. `hook_lab` names N1, N2, N3, matching the hand score 3/3 |
| EN consultant | `day0_shape` (text version: RECORD YEAR only in the ask) | real |

The 4 FP classes from FT1 now pass: I15 (third-person "chị coach đó"), the `day0_shape` "xem nghiên cứu" CTA, the
filled "[TikTok · 10/2026]", and `vn_messages` "Dạ". `day0_timing` counts the 4 dig answers (`dig_answers_max = 4`).
On the EN run, `hook_lab` passes both shorts, as FT1 scored them. So the graders are ready; only the runs are missing.

## 7. Short fix list

1. **Play the 3 FT2 packets.** This blocks everything else. Write `transcript.jsonl` and `notes.md`, the latter with
   `## Research log`: queries, pages with URL/place/month/role, kept and dropped lines, Map before → after. Then run
   `python3 evals/run.py grade evals/runs/ft2-*` and review again. Then find out why the simulator stage returned `[]`.
2. **Let a run reach the strategy document.**
   - `evals/run.py` `COACH_DAY0` step 6: when NEXT offers the file, the coach says "strategy" / "chiến lược" as one
     more turn, then stops.
   - Or add `evals/cases/strategy-doc.{en,vn}.toml`.
3. **`qa/standards/strategy-doc.md`: follow DECISIONS 7 Oct.**
   - Exempt "(content pillars)" in part 3's heading in the hard gate and the runtime check.
   - Fix the VN note's heading 3.
   - Add SD8's "≥3 gives per ask" to `modules/{en,vn}/strategy-doc.md`, or drop it from the rubric.
4. **One ask per string** (`strings/{en,vn}.toml`, §CM-DIG 3, §CM-GUARDRAILS):
   - `dig.buyer`: VN "Khách nào làm bạn ước có thêm chục người y vậy?" / EN "Which client do you wish you had ten more of?"
   - `proof.intake`: ask only whether the client OK'd it.
5. **VN wording:** apply §5 rows 1–5 and the runner-up, inside the 56,320 B budget.
6. **Rebuild the coach zips** (`tools/package.py`). Both `dist/Content-Machine-{EN,VN}-v1.0.0.zip` predate the fixes:
   - VN method file 56,308 B vs 56,268 in `dist/vn`
   - EN method file 49,203 B vs 48,102 in `dist/en`
   - no PLAYBOOK file in either

   A founder re-test from a zip would run the FT1 kit.
7. **Research lane:** the `web` lane cannot read Facebook groups, TikTok or Zalo. Add a browser lane for the 2 VN
   personas, or score LN2 knowing that limit.
