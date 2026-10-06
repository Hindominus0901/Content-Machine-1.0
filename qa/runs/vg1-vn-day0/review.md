Result: FAIL

# VG1 VN Day-0 golden round: independent review

Build under test: run `meta.json` build `4885b33b5db7`; repo HEAD `f5de31d1ca12`, working tree clean. Kit: each run's
`packet/kit/`, identical to the current `dist/vn` (`1-INSTRUCTIONS.txt` md5 04b64481…, 9,507 B / **7,493 of 7,500 NFC
chars**; `CONTENT-MACHINE-VN.md` md5 3705b37e…, **56,311 of 56,320 B**; S0 had no method file). Every §CM anchor is
≤3,600 B (largest: MAP 3,368, SETUP 3,272, NATURAL 3,209).

Reviewer: independent, native Vietnamese reader. I wrote neither the kit nor the runs.

How this review was done:
- All 7 transcripts were read in full, as the coach would read them on their phone.
- Scratch copies of the 7 folders were re-graded with the current `evals/run.py grade`. The verdicts match the stored
  `grades.json` exactly. The run folders were not touched.
- Leaks were checked in all 7 runs, more than the 3 asked for, in two ways:
  - every word and number in a machine turn that no earlier coach turn and no kit file holds;
  - in proof-coach, consultant and Tuấn, a 4-tiếng scan against `expected.toml`, `voice-samples.md` and `persona.toml`.
  Each hit was checked by hand.
- Each failed check is traced to the transcript line and to the kit line or grader code behind it.
- Naturalness was scored on `qa/standards/vn-naturalness.md` VN1–VN8, with `docs/research/vn-language-guide.md` as the
  yardstick. Every line I mark is quoted with a natural fix (section 6).

Why FAIL:
- **The grader passes 0 of 7 runs.** Of the 32 failed items, 9 are real and 23 are false positives (72%). The false
  positives bury the real defects, and none of the message-language defects below is graded at all.
- **Day-0 budgets miss in 2 of 7 runs.**
  - coldstart: Map at coach turn 8 (max 7) and 11 coach turns (max 10). Her first video she could film came at 21.0
    active minutes.
  - Hạnh S1: film-ready at active minute 20.2 (max 20).
- **Real kit defects:**
  - `setup.multi_income` asks two questions in one message (Tuấn: I5, and "two questions" is on his confusion list).
  - A Map pushback holds Week 1 for one more turn (coldstart, service-biz). DECISIONS says any message after the Map
    brings Week 1.
  - Three coaches objected to comment keywords in words (coldstart, consultant, Tuấn). The machine argued back ("đâu
    có ép ai") and made each one type 'nhẹ'.
  - The ~10-minute dump cut skipped chunk 3, so the consultant's 250-person email list and his LinkedIn channel were
    never heard. That is quit point #12 hit by omission.
- **Language, the founder's top concern:**
  - The pieces read like Vietnamese people wrote them. All 14 FILM TODAY and Week-1 post sets pass VN1–VN8, with 0
    translationese patterns in 7 runs, 0 pronoun slips and the right regional particles.
  - The coach-facing replies fail VN6 in 7 of 7 runs. The cause is two fixed kit strings printed on every Map screen:
    "đăng caption dạng bài chữ" and "Muốn kết nhẹ hơn thì gõ 'nhẹ'".
  - The 1:1 messages fail in 4 of 7 runs: a call-centre "nhắn chữ DỪNG" opt-out in three, a form-letter "anh/chị" in
    one. Two runs open "Dạ" from an older chị to a younger em, and two put Southern "chút xíu / tìm tới" into a Hà Nội
    voice.

## 1. The runs

Map turn = the number of coach turns up to the Map. With K2 the film-ready turn is the same turn.

Film-ready is in active minutes; clock time is in brackets where the coach was away.

Verdict codes: R = real defect, R(kit) = the kit caused it, R(m) = machine slip, FP = grader false positive.

| Run | Lane · app | Valid | Outcome | Coach turns | Map turn | Film-ready | Week 1 on next answer | Failed (grader) | Verdict per failed item |
|---|---|---|---|---|---|---|---|---|---|
| proof-coach | S1 · ChatGPT Plus, Win laptop + Android | yes | Map + video, Week 1, card (own reply); launch pushback answered in one line | 8 | 6 | 17.6 | ✓ | I15, day0_shape, vn_natural | I15 FP · day0_shape FP ×2 (YOUR WORD, save backup) · vn_natural FP (script directions counted; soft note: spoken lines carry 0 particles) |
| coldstart-coach | S1 · ChatGPT Free, iPhone | yes | talking-head video, then a movement-only rewrite she filmed; Week 1; Free limit (165 min); card in the evening | 11 | 8 | 18.4 (filmable 21.0) | ✗ +1 turn | I15, day0_timing, day0_shape, vn_natural | I15 FP · day0_timing R(kit + m) · day0_shape: YOUR WORD FP, `[Tên]` R(m) · vn_natural R (soft) |
| consultant | S1 · Claude Pro | yes | Map + video, Week 1 with the comment asks he had refused, then all text posts + card; back only on Sunday | 9 | 7 | 19.9 | ✓ | I8, I9, I11, I15, day0_timing, day0_shape | I8 R(m) · I9 FP · I11 FP · I15 FP · day0_timing FP (numbered Map labels) · day0_shape FP ×2 |
| service-biz | S1 · ChatGPT Free, Android | yes | Map + video; homestay pushback, then a second OK turn; Week 1; card | 10 | 7 | 17.7 | ✗ +1 turn (kit) | I6, I15, day0_shape | all FP; one real defect the graders missed ("nhắn riêng Trang") |
| Hạnh | S1 · ChatGPT Free, Android, no computer | yes | 3 chunks with 25 min away; Map + video, Week 1, card | 8 | 6 | 20.2 (45.2) | ✓ | I11, I15, I23, day0_timing, day0_shape | I11 FP · I15 FP · I23 FP · day0_timing R (marginal; kit can't time the dump) · day0_shape FP ×2 |
| Tuấn | S1 · ChatGPT Plus, iPhone + laptop | yes | Map + video, Week 1 with a Bán kèm path for the apartment, card | 9 | 7 | 18.2 | ✓ | I5, I11, I15, quit_triggers, day0_shape, vn_natural | I5 R(kit) · I11 FP · I15 FP · quit_triggers R(kit; a confusion, not a quit, for him) · day0_shape FP ×2 · vn_natural FP |
| Hạnh | S0 · ChatGPT Free, Android (compact mode) | yes | Map + video, Week 1 + card in one 2,162-word reply | 8 | 7 | 19.9 (44.9) | ✓ | I11, I15, I23, day0_shape, vn_natural | I11 FP · I15 FP · I23 FP · day0_shape: YOUR WORD FP, save FP, `[Tên]` R(m) · vn_natural R (soft) |

Totals:
- **Valid runs: 7 of 7. Quits: 0.** The simulator says 6 of 7 coaches come back tomorrow. The consultant comes back
  only on Sunday, the one free slot he never got to mention (chunk 3).
- **Failed items: 32.** 9 are real: 4 R(kit), 3 R(m), 2 R (soft language). 23 are FP: I15 ×7, day0_shape ×5, I11 ×4,
  I23 ×2, vn_natural ×2, I6, I9, day0_timing.
- **I16 is n/a** in 7 of 7 runs (`locales/vn/examples.md` does not exist yet).
- **Summary-table bug, as in G2.** `run.py summary` prints clock time in "Film-ready min" for the two Hạnh runs (44.9,
  45.2); their active times are 19.9 and 20.2.

## 2. Day-0 shape and budgets (wf15 §1 as amended by K2; acceptance `[day0]`)

Key: ✓ = matches · ~ = partly · ✗ = missing or wrong.

| Step / budget | proof | cold | cons | svc | Hạnh S1 | Tuấn | Hạnh S0 |
|---|---|---|---|---|---|---|---|
| Reply 1: setup line, promise, mic tip, xưng hô question | ✓ | ✓ | ✓ (Claude: mic tip moved to reply 2, per kit) | ✓ | ✓ | ✓ | ✓ |
| Early win after chunk 1 (min after dump start; acceptance ≤4, ungraded) | ~ 7.1 | ~ 6.5 | ~ 7.5 | ~ 7.2 | ~ 5.6 | ~ 7.1 | ~ 5.6 |
| Dump closed by the ~10-min line | ✓ after c2 | ✓ after c2 | ✓ after c2 | ✓ after c2 | — 3 chunks (9.6 min after c2) | ✓ after c2 ("chờ tui chút" cut off) | ✓ after c2 (she asked to continue later) |
| Missing facts ≤3, one per message, each a guess | ✓ 0 | ~ 2, one avoidable | ✓ 1 | ✓ 1 | ✓ 0 | ✗ 1 message with 2 questions | ✓ 1 |
| Map: 4 lines + "OK hay sửa một dòng?" | ✓ | ✓ | ~ numbered + "BẢN ĐỒ" heading | ✓ | ✓ | ✓ | ✓ |
| QUAY HÔM NAY in the Map reply: script, caption box, CTA + 'nhẹ', "Quay luôn…" | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Week 1 on the next answer, full mix | ✓ | ✗ +1 turn; Zalo ask-3 and Zalo msg merged; gift has 3 blanks | ✓ (no email: list unheard) | ✗ +1 turn | ✓ | ✓ | ✓ |
| Card: top ≤500 + machine block + save line with Zalo backup | ✓ 474 | ~ top inside the copy box (graders skipped the card) | ✓ 494 | ✓ 480 | ✓ 452 | ✓ 434 | ✓ 353 |
| NEXT + reminder invite | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Map ≤7 coach turns (VN) | ✓ 6 | ✗ 8 | ✓ 7 | ✓ 7 | ✓ 6 | ✓ 7 | ✓ 7 |
| Film-ready ≤20 active min | ✓ 17.6 | ✓ 18.4 (filmable 21.0) | ✓ 19.9 | ✓ 17.7 | ✗ 20.2 | ✓ 18.2 | ✓ 19.9 |
| ≤10 coach turns | ✓ 8 | ✗ 11 | ✓ 9 | ✓ 10 | ✓ 8 | ✓ 9 | ✓ 8 |
| Session ≤40 active min | ✓ 23.2 | ✓ 26.1 | ✓ 32.2 | ✓ 24.5 | ✓ 27.0 | ✓ 23.2 | ✓ 25.2 |

Notes:
- **K2 works.** Today's video came in the Map reply in 7 of 7 runs, and 6 of 7 runs were film-ready in ≤20 active
  minutes (G2 EN: 5 of 7).
- **Where the turns go.** A VN coach spends turns on: "Bắt đầu", xưng hô, chunk 1, the paste, chunk 2, and 'xong' after
  the cut. That puts the Map at turn 6 with zero questions. Each question, and each wait for a second OK, adds one turn.
  - coldstart lost 2 turns:
    - T6 asked "Chắc chưa có kết quả của khách để kể, đúng không?", though chunk 2 had already said "nó là bạn mình chứ
      hông phải khách, mình cũng hông có đo gì hết";
    - T9 re-asked for OK after "ok. Ủa vậy mấy cái ngủ…", against §CM-MAP "'ok' kèm chỗ sửa → sửa rồi đi tiếp".
  - service-biz lost 1 turn: T8 waited for OK after the homestay pushback (§CM-MAP "CÃI BẢN ĐỒ, 1 dòng, vẫn chờ OK").
- **The 'xong' round trip costs a turn in 6 of 7 runs.** The cut line "Hôm nay vậy là đủ rồi. Gõ 'xong', hoặc nói thêm
  một phút." needs a reply before anything happens (same finding as G2 EN).
- **Reading load.**
  - Week 1 replies ran 1,194–1,477 words (5–6 phone screens).
  - Card replies ran 1,082–1,833 words. Every S1 run moved the card to its own reply ("dài quá: card ở tin sau"), which
    costs a turn each time.
  - S0 sent both in one 2,162-word reply on ChatGPT Free.
  - coldstart wrote "Viết ngắn thôi, đọc trên điện thoại mỏi mắt" and then got a 1,082-word code box. That is legal
    under the K3 rule, but it is still a wall.
- **Card memory risk.** `schemas/brand-card.toml` keeps the message, topics and keyword only in the visible top
  ("message, big_ideas and keyword are not repeated here"). A coach who copies just the code box into Zalo "Cloud của
  tôi" (the backup each save line offers) loses the Map.

## 3. VN specifics

| Check | Result |
|---|---|
| Xưng hô asked in reply 1 | ✓ 7/7: "Cho mình hỏi trước: gọi bạn là anh, chị hay bạn? (gõ 1 chữ là được)" |
| Pair held from reply 2, 0 slips | ✓ 7/7, **0 real slips**. Every I15 pronoun hit is FP (section 5). "Dạ, em chào chị/anh." in reply 2 in all em-runs |
| Inclusive "mình" ("Mình chạy thử 4 tuần nhé chị") | Natural Vietnamese for "let's", not a slip (guide §4.5). The proof notes call it a defect; I disagree |
| Coach's audience address kept apart and stable | ✓ 7/7: "mình – các chị em", "mình – mấy bạn", "tôi – anh chị", "Đức, tụi em – anh chị", "chị – các em", Tuấn "mình – bạn" on video and "tui" on Facebook (as in his own posts). Defects: the consultant's 1:1 messages say "anh/chị"; Tuấn's 1:1 form drifts between the card ("tui – anh, chị"), the inbox ("mình – bạn") and Zalo ("Tuấn – anh chị") |
| Regional particles | ✓ after the region was heard (nha / nghe / nhé, "rứa, ni, chi" for Quảng). ✗ Reply 2's template "…cứ xả hết ra nhé" gives a Bắc particle to the 4 Nam/Trung coaches before their region is known; Tuấn "dị ứng giọng Bắc" |
| Zalo-first messages | ✓ 7/7: comment → inbox/Messenger → Zalo, a Zalo ask-3 and a Zalo message every Week 1. No email anywhere, because the consultant's list (250) was never heard |
| Keyword CTAs and "chấm" never blocked | ✓ never blocked or rewritten, and keywords come from client words (LÃI ẢO, CỨNG ĐƠ, TUYỂN HOÀI, PHÁT SINH, NGẠI CHÀO, GỒNG LÃI), each with the no-diacritics form. **"chấm" / threshold was not exercised:** proof's "chấm" and "đủ 100 comment" sit in chunk 3, which was cut |

## 4. Leak spot-check (all 7 runs)

- **Clean in 7 of 7.** No persona fact appears in a machine turn before the coach said it. Every number in machine text
  is either one the coach said, a date or kit constant, or a marked guess:
  - service "95 tới 120 triệu", from his 96 and 112 triệu stories;
  - proof "khoảng 60 học viên cũ trên Zalo (em đoán)", from "60 học viên" and "nhóm Zalo".
- **Unsaid words in machine turns are normalisations or plain Vietnamese:**
  - spelling fixes: shopee, livestream, melamine (for "sốp pi", "lai stream", "mê la min");
  - script verbs: giơ, cầm, cuốn;
  - kit fields: asia, ho;
  - "muốn cọc cho lẹ" in Tuấn's `trait`: a Southern word he never said, but not a fact.
- **Two guesses match `persona.toml` and are not leaks:**
  - proof "Facebook cá nhân và nhóm" is the §CM-LOCALE 4 default ("khách 30+ → Facebook cá nhân + nhóm");
  - proof talk day thứ Ba is the Day-0 weekday. The same rule gave the consultant and service-biz thứ Ba, which is
    wrong for both.
- **The answer-key n-gram hits** (expected.toml, voice-samples.md) in proof, consultant and Tuấn are all joins of
  phrases the coach dictated. The voice fields (tone, rhythm, openers) do not track `expected.toml`. For example, proof
  "thẳng, ấm, tự giễu" vs the key "thẳng · gần gũi · khiêm tốn".
- **The protocol leak check passed with 8–14 warnings per run.** I agree with each simulator's reading; three runs had
  card lines rewritten after a first INVALID grade.

## 5. Failed grader checks: real or false positive

- **I15 ×7: FP.**
  - "than" is Vietnamese (to complain), from the kit's own Map template "{ai} hay than" (start-block step 5). It hits
    6 runs because `EN_FUNCTION_WORDS` (graders.py L247) holds "than".
  - "it" is the coach's "IT" (coldstart T10: "có bạn làm IT"). "this" is the card field `why_this_one` (coldstart T11).
  - Pronoun hits:
    - inclusive "Mình chạy thử 4 tuần nhé chị" (strings `map.ok`);
    - the coach's own public self-reference inside the Map and card lines: "thì tìm mình / tôi / chị Hạnh / Đức",
      which is start-block step 5 "{coach tự xưng}";
    - "chị trưởng phòng", a third person in brackets (coldstart T10).
  - Code: `i15_vn_language` L1763–1800 scans `prose_text()` with no exemption for these.
- **day0_shape (7 runs): 5 FP, 2 real.** The false positives have three causes.
  - **"YOUR WORD is the CTA keyword"** (proof T6, coldstart T8, Tuấn T7, Hạnh S1 T6, Hạnh S0 T7). `_norm_word` (L2953)
    keeps "(không dấu: LAI AO)", "(mình đoán, Tuần 1 kiểm lại)" and ", em đoán từ câu các em hay than". The kit requires
    "kèm dạng không dấu" on that line.
  - **The CTA parser** (`cta_keyword` L2932, `CTA_FALLBACK_RE` L2926):
    - in consultant T7 and service T7 it finds no CTA, because the slot pattern wants "mình gửi" and the machine
      correctly wrote "tôi gửi" and "tụi em gửi" (step 6: "theo cách coach gọi khách");
    - in Hạnh S1 it read "nhắn riêng chị" as the keyword "riêng";
    - in Hạnh S0 it took "gõ 'ok' là" from the TIẾP line.
  - **"save line has no backup"** (6 runs): `SAVE_BACKUP_RE` (L276) has no VN form for the kit's own "Dự phòng: gửi
    vào Zalo "Cloud của tôi"" (start-block line 44).
  - **Real parts inside day0_shape:**
    - unfilled `[Tên]` in coldstart T10 ("[Tên] ơi … Hỏi [tên] đúng một câu thôi") and Hạnh S0 T8;
    - coldstart's gift also ships "a) [động tác 1] b) [động tác 2] c) [động tác 3]" and inbox "[dán quà]", which
      `PLACEHOLDER_RE` (L268) does not catch. The "Cần bạn" line under the gift is correct kit behaviour; the blanks in
      a gift already promised in today's caption are the problem.
  - **Blind spot.** coldstart put the card top inside the code box, so the card-top and save-line items returned
    `null`: the card was not found.
- **I11 ×4: FP.** The hits are:
  - the negated honesty line "không phải cam kết" (consultant, Hạnh S1, Tuấn, Hạnh S0);
  - "trị dứt điểm", listed in Hạnh's card top as "không bao giờ:";
  - "tốt nhất", inside the consultant's own principle "người phỏng vấn tốt nhất là người sẽ làm sếp trực tiếp";
  - "số 1", from "đánh số 1-2-3".
  `i11_injection` (L1535) drops never_say/do_say values only (EN G5), not the VN top line or negations.
- **I23 ×2 (both Hạnh): FP.** "không giảm sốc gì hết" is her own negated method line (chunk 2), copied into the gift.
  The card's never_say keeps the bare word "giảm sốc", which is right.
- **vn_natural ×4: two FP, two real (soft).**
  - The check counts script direction lines as sentences: "Chữ trên màn hình", "Khung hình đầu", "Cảnh n", and the
    beat-card "Ý n" notes (`vn_sentences` L2536). Without them, the written pieces (captions, posts, messages) score:

    | Run | Written pieces | Coach's posts | Floor (40%) | Verdict |
    |---|---|---|---|---|
    | proof | 22% | 38% | 15% | **FP** |
    | Tuấn | 21% | 46% | 18% | **FP** |
    | coldstart | 15% | 64% | 26% | **R** |
    | Hạnh S0 | 13% | 53% | 21% | **R** |

  - Read aloud, coldstart's captions are flatter than hers: she writes "nha", "nè", "á", ":))" on most lines. Hạnh S0's
    CTA drops her "nhé :))".
  - The spoken script lines carry 0 particles in proof (0/22) and Tuấn (0/24). With beat-card delivery the coach adds
    those aloud, so this is not a defect.
  - The translationese density is **0 patterns in 7 of 7 runs**, which matches my reading.
- **day0_timing ×3: 2 R, 1 FP.**
  - **coldstart R(kit + m):** the causes are in section 2.
  - **Hạnh S1 R:** 20.2 active minutes, marginal. She dictated 14.6 minutes over 3 chunks; the kit's "quá ~10 phút"
    can't be timed from text, and she was 9.6 minutes in after chunk 2. There were no questions after "xong".
  - **consultant FP:** "the Map has 0 labelled lines". He printed "1 ĐIỀU KHÁCH NHỚ:" with number prefixes;
    `_map_label_re` (L2764) is anchored on the bare label.
- **I5 + quit_triggers (Tuấn T6): R(kit).**
  - The `setup.multi_income` template (§CM-SETUP 6) is "… Đúng không? Hay nói luôn: tháng này nguồn nào nuôi anh?",
    two questions against "tối đa 1 câu hỏi".
  - For Tuấn, two questions in one message is a confusion item, not a quit. The grader's generic trigger list
    over-reaches.
- **I8 (consultant T9): R(m), minor.** "200 triệu, 70%, 80%, 6 tháng lương" sit in the card's `proof` field as
  "chưa dùng … (không có căn cứ)". `proof` is defined as "đếm được, khách đồng ý" (§CM-CARD 3). Refused or unsourced
  claims belong in `not_now`, which is what Tuấn's card did ("dễ thành hứa quá lời").
- **I9 (consultant): FP.** "Cloud của tôi" is the kit's Zalo backup name.
- **I6 (service-biz T8): FP.** `DECLARATIVE_BEFORE_RE` (L1273) does not allow "chỉ" before "chọn". The line is the
  kit's `message.pushback.who`; it reads translated anyway (section 6).
- **Graded nowhere (real):**
  - "Không muốn nhận tin nữa thì … nhắn … chữ DỪNG" in a 1:1 inbox reply (proof, service-biz, Tuấn);
  - "anh/chị" in the consultant's four 1:1 messages;
  - "Dạ" from chị to em (proof, Hạnh S1);
  - "nhắn riêng Trang" (service-biz);
  - card top inside the code box (coldstart);
  - the gift promised in today's caption before it exists (service-biz; coldstart's has blanks).
- **Piece split.** VN titles such as "Bài dài · thứ Sáu, 09/10 · …" are not piece titles (`FORMAT_TITLE_RE` L141), so
  the long post merges into N1's piece. Content checks still read it; per-piece checks (I12, I23) do not.

## 6. Naturalness (VN1–VN8)

Bars (vn-naturalness.md):
- Pieces: VN3, VN4, VN6 and VN7 must score 2, total ≥13/16.
- Machine prose to the coach and the Map lines: VN3, VN4 and VN6 must score 2, total ≥10/12.

Regions present: Bắc (proof, Hạnh ×2), Nam (coldstart, Tuấn), Trung (consultant, service-biz, Quảng). I read all three.

| Run | Coach-facing replies /12 | Map lines /12 | QUAY HÔM NAY /16 | Week-1 posts /16 | Zalo + inbox /16 | Would the coach post the pieces as they are? |
|---|---|---|---|---|---|---|
| proof | 10 ✗ (VN1 1, VN6 1) | 11 ✓ | 15 ✓ | 15 ✓ | 13 ✗ (VN1 1, VN5 1, VN6 1) | Posts and scripts yes. Two messages need one line each (DỪNG, "chút xíu / tìm tới") |
| coldstart | 9 ✗ (VN1 1, VN5 1, VN6 1) | 11 ✓ | 15 ✓ | 15 ✓ (VN5 1) | 15 ✓ | Yes, once the 3 desk moves and `[Tên]` are filled |
| consultant | 9 ✗ (VN1 1, VN5 1, VN6 1) | 11 ✓ | 16 ✓ | 15 ✓ (VN8 1 before 'nhẹ') | 13 ✗ (VN4 1, VN6 1) | Posts yes. Messages no: every one says "anh/chị" |
| service-biz | 8 ✗ (VN1 1, VN2 1, VN5 1, VN6 1) | 11 ✓ | 15 ✓ (VN1 1) | 15 ✓ (VN1 1) | 15 ✗ (VN6 1) | Yes, once "Trang" is lower-cased; drop the DỪNG line |
| Hạnh S1 | 10 ✗ (VN1 1, VN6 1) | 11 ✓ | 16 ✓ | 16 ✓ | 14 ✓ (VN1 1, VN5 1) | Yes |
| Tuấn | 9 ✗ (VN1 1, VN5 1, VN6 1) | 11 ✓ | 16 ✓ | 16 ✓ | 15 ✗ (VN6 1) | Yes; drop the DỪNG line |
| Hạnh S0 | 10 ✗ (VN1 1, VN6 1) | 11 ✓ | 15 ✓ (VN5 1) | 15 ✓ (VN5 1) | 15 ✓ | Yes, once `[Tên]` is gone and the "cam kết" line is in her words |

Totals:
- **Pieces: QUAY HÔM NAY and Week-1 posts pass in 14 of 14 sets** (average 15.4/16).
- **Messages pass in 3 of 7 runs.**
- **Map lines pass in 7 of 7** (11/12 each, VN2 1 for length).
- **Coach-facing replies pass in 0 of 7.** Every VN6 hit is a kit string (`film.now_or_text` and the 'nhẹ' hint in
  all 7; `message.pushback.who` in service-biz). Only coldstart adds a calque of its own (line 10).
- **Release bar G3** (pieces average ≥14/16, no critical below 2): **not met** while 4 runs' messages carry a VN6 or
  VN4 at 1.

What reads right (keep it):
- The stories run scene → quoted words → action → small step:
  - proof long post: "Học viên mình nhắn lúc 1 giờ sáng: "Chị ơi hóa ra em toàn lãi ảo"";
  - service-biz: "Năm 2019, có ông chú cầm cây chổi chỉ vô mặt Đức.";
  - consultant: "Nhìn mặt thì đoán. Cho làm 2 tiếng thì biết.";
  - Tuấn: "Có chị gọi mình từ trong toilet nhà mẫu".
- There are no essay connectors.
- Inbox questions sound like people talking:
  - service-biz: "Nhà mình tính sửa bếp liền hay đang coi trước, anh chị?";
  - Tuấn: "Mà nhà bạn đang nhắm căn nào rồi, hay mới bắt đầu tính?";
  - coldstart: "Làm thử rồi nhắn mình nghe nha.".
- Tuấn's honesty line is how it should be done: "Đó là con số của một nhà, nhà bạn phải tính theo lương nhà bạn, không
  phải cam kết gì hết."
- Coach-facing lines that read like a person: "Dạ, em nhận rồi.", "Không vội đâu chị, chị cứ ra tiếp khách.", "Chị bấm
  micro nhỏ trong ô chat thì em không nói chen vào nữa.", "Brand Card em gửi ở tin sau, cho tin này khỏi dài thêm."

Native reviewer marks: S = stiff, D = translated, R = wrong region, X = wrong pair. Each line is followed by its source
and a natural fix.

**Coach-facing, from kit strings (every run):**

1. D: "Quay luôn bây giờ, hoặc đăng caption dạng bài chữ cũng được."
   - Source: 7/7 runs, `film.now_or_text`.
   - "caption" is English to Hạnh and Đức, and "dạng bài chữ" back-translates smoothly ("post the caption as a text
     post").
   - Fix: "Quay luôn bây giờ, hoặc đăng phần chữ làm bài viết."
2. D: "Muốn kết nhẹ hơn thì gõ 'nhẹ'."
   - Source: 7/7 runs, from step 6 "(muốn nhẹ hơn thì gõ 'nhẹ')" and `cta.not_pushy`.
   - A calque of "say 'quiet' for a softer ending". No coach can tell what "kết" refers to.
   - Fix: "Ngại xin comment thì gõ 'nhẹ'."
3. S (register): "Người xem comment là nhận được thứ có ích thật, đâu có ép ai."
   - Source: coldstart T9, consultant T8, Tuấn T8; `cta.not_pushy`.
   - Each time it came straight after the coach objected. "đâu có ép ai" from em to a 42-year-old anh reads as talking
     back.
   - Fix: on an objection, switch and say so: "Dạ, vậy mình kết bằng nhắn riêng: 'Nhắn tôi chữ TUYỂN HOÀI, tôi gửi
     mẫu phiếu việc 1 trang.'"
4. D: "Dạ, ai cũng xem được hết, em chỉ chọn viết cho ai thôi: chống thấm, thay ống em để bán kèm…"
   - Source: service-biz T8; `message.pushback.who`.
   - Back-translates cleanly ("Everyone can see it, I only choose who to write for"), and the sentence runs 55 tiếng.
   - Fix: "Dạ, ai đọc cũng được hết anh, bài chỉ nói với đúng một kiểu khách thôi. Chống thấm, thay ống thì em để bán
     kèm qua tin nhắn."
5. S, and 2 questions: "Em đoán vợ chồng trẻ đang ở trọ, tính mua căn một hai phòng ngủ, là kiểu khách mua được nhiều
   món nhất: … Đúng không? Hay nói luôn: tháng này nguồn nào nuôi anh?"
   - Source: Tuấn T6; `setup.multi_income`.
   - "mua được nhiều món nhất" makes a home buyer sound like a shopper.
   - Fix: "Em đoán nên viết cho vợ chồng trẻ đang ở trọ tính mua căn, vì nhà đó vừa mua căn qua anh, vừa cần hợp đồng
     che người đứng tên vay. Đúng không anh?"
6. R: "Anh cứ xả hết ra nhé:"
   - Source: reply 2 to the coldstart, consultant, service-biz and Tuấn coaches, before their region was known.
   - Fix: "Anh cứ xả hết ra:" (no particle until the dump shows the region).
7. S (jargon): "ngày nói chuyện thứ Ba (em đoán, chị nhắn một chữ là đổi)"
   - Source: 7/7 runs; `setup.plan_guess`. Also "Muốn em nhắc vào ngày nói chuyện…".
   - Nobody has told the coach what the weekly talk is.
   - Fix: "thứ Ba hằng tuần chị ngồi kể 15 phút để em viết tuần sau (em đoán, …)".
8. VN1: "Brand Card", "⋯ dưới card → Lưu vào dự án", "Kiểm tra cài đặt: ✓ hướng dẫn ✓ file phương pháp"
   - Source: 7/7 runs.
   - These are English or system words that five personas list as confusing. Three runs glossed them unprompted ("phần
     để em nhớ chị", "bản tóm tắt để em nhớ anh").
9. S: "ĐIỀU KHÁCH NHỚ: Dân văn phòng hay than "…" thì tìm mình: cứ 45 phút đổi tư thế, 3 động tác 5 phút ngay tại bàn,
   thở ra dài thả vai, chứ không chữa cháy cuối tuần, mặc đồ công sở cũng làm được."
   - Source: the Map template (start-block step 5). The same shape is in every run, and it runs 45–55 tiếng in
     coldstart, consultant, service-biz, Hạnh and Tuấn.
   - Without "nào" the line reads as a statement, and the stacked methods read as a brochure.
   - Fix: "Dân văn phòng nào hay than "ngồi tới 4 giờ chiều là lưng cứng đơ" thì tìm mình: mỗi ngày 5 phút ngay tại
     bàn, chứ không chữa cháy cuối tuần."

**Coach-facing, machine's own words:**

10. S: "Còn chuyện tối 9 giờ phải vịn cạnh bàn của chính bạn thì đủ sức nặng rồi."
    - Source: coldstart T6.
    - "của chính bạn" is a calque (guide A14).
    - Fix: "Chuyện tối 9 giờ bạn phải vịn cạnh bàn là đủ rồi."
11. S: "Mình vẫn giữ một chuyện cho khách nhớ, chạy thử 4 tuần rồi tính."
    - Source: consultant T8.
    - Fix: "Mình cứ giữ một điều cho khách nhớ, chạy thử 4 tuần rồi tính nghe anh."

**Pieces and messages:**

12. S (call-centre): "Không muốn nhận tin nữa thì em nhắn chị chữ DỪNG."
    - Source: proof, service-biz and Tuấn, in inbox reply 2, sent to someone who just said they want to buy.
    - The kit means this line for Zalo series (§CM-MESSAGES 3). The machine applied it to a 1:1 reply, following
      §CM-GUARDRAILS "(trong inbox thì nói … cách dừng)".
    - Fixes: proof "Em chưa cần thì cứ nói chị một tiếng nhé."; service-biz "Anh chị chưa cần thì cứ nói em một tiếng
      nghe."; Tuấn "Chưa cần thì cứ nói mình một tiếng nha."
13. VN5: "Dạ, chị gửi em 3 bước cầm gương nói thật nhé." (Hạnh S1) and "Dạ, chị gửi em cách soi lãi thật…" (proof)
    - Source: §CM-MESSAGES 5 'Tin 1 = "Dạ" + đủ quà'.
    - "Dạ" from an older chị to a younger em is page-staff voice (guide §4.6).
    - Fix: "Chị gửi em 3 bước cầm gương nói thật nhé." Hạnh S0 got this right.
14. R + S: "Em ơi, chị nhờ em chút xíu nhé. … Hồi mới tìm tới chị, em đang gặp chuyện gì?"
    - Source: proof; Hạnh S1 is the same; strings `research.ask3`, `ask3.question`.
    - "chút xíu" and "tới" are Southern in a Hà Nội voice, and "gặp chuyện" means "ran into trouble".
    - Fix: "Em ơi, chị nhờ em tí nhé. … Hồi mới tìm đến chị, em đang khổ nhất chuyện gì?" The neutral kit form is in
      VK-9.
15. X (guide X10): "Anh/chị ơi, tôi Khoa đây. Nhờ anh/chị chút xíu…" and "Tôi gửi anh/chị mẫu phiếu việc 1 trang…"
    - Source: the consultant's 4 messages.
    - A slash in a 1:1 message is the mark of a form letter.
    - Fix: "Anh ơi, tôi Khoa đây. Nhờ anh một chút…", plus one line above the box: "gửi chị thì đổi 'anh' thành 'chị'".
16. Placeholders: "[Tên] ơi, mình đang làm mấy clip… Hỏi [tên] đúng một câu thôi: … giờ [tên] thấy khó nhất chỗ nào?"
    - Source: coldstart; Hạnh S0 has "[Tên] ơi, c hỏi e…".
    - Hạnh edits on a cracked screen.
    - Fixes: coldstart "Mình đang làm mấy clip cho dân văn phòng hay bị lưng cứng đơ. Hỏi bạn đúng một câu thôi nha:
      ngồi máy tính cả ngày, giờ bạn thấy khó nhất chỗ nào?"; Hạnh S0 "Em ơi, c hỏi e một câu thôi nhé: …".
17. VN1: "Anh chị nào sắp sửa bếp thì comment PHÁT SINH hay nhắn riêng Trang, tụi em gửi…"
    - Source: service-biz ×4.
    - Capitalised "Trang" reads as a woman's name.
    - Fix: "… hay nhắn tin cho trang, tụi em gửi …".
18. S (legal register; "cam kết" is not their word): "Kết quả tuỳ từng nhà, không phải cam kết." (service-biz long
    post) and "Đây là kết quả của một spa. Kết quả tuỳ người, không phải cam kết." (Hạnh S0 Video 2)
    - §CM-HUMANIZE already says "viết bằng chữ của họ".
    - Fixes: service-biz "Mỗi nhà mỗi khác, nhà chị Loan là rứa, không phải nhà mô cũng y chang."; Hạnh "Mỗi spa mỗi
      khác các em ạ, đây là sổ của Thảo, chị không hứa em nào cũng được thế."
19. S: "28 Tết năm 2019, mình ngồi bệt dưới sàn kho, cộng sổ cả năm 2018 vào cái vở ô li của con."
    - Source: proof caption.
    - Fix: "28 Tết năm 2019, mình ngồi bệt dưới sàn kho, lấy cái vở ô li của con ra cộng sổ cả năm 2018."
20. S (guide N3 rhythm): "Các em ngại chào không phải vì các em kém. Mà vì cách chào các em từng thấy toàn là dọa."
    - Source: Hạnh S1 long post. It appears once, so it is not scored down.
    - Fix: "Các em ngại chào đâu phải tại các em kém, mà tại cách chào các em từng thấy toàn là dọa."
21. VN5 (particles): coldstart 15% of written sentences end in a particle vs her 64%; Hạnh S0 13% vs her 53%.
    - Hạnh S0: "Em nào đang ngại chào thì comment NGẠI CHÀO hoặc nhắn riêng, chị gửi 3 bước cầm gương nói thật." →
      "… chị gửi 3 bước cầm gương nói thật nhé :))"
    - coldstart: "hồi làm kế toán, 26 tuổi mà 9 giờ tối đứng dậy lấy nước phải vịn cạnh bàn" → "… phải vịn cạnh bàn
      luôn á"
22. S: "Chị Hạnh đây em. Em comment NGẠI CHÀO nên chị gửi em 3 bước…"
    - Source: Hạnh S0, tin 1.
    - Fix: "Chị Hạnh đây em. Chị gửi em 3 bước cầm gương nói thật, chị đang làm ở quầy nhé:"

## 7. Read as the coach: confusion, reading load, repeats, quits

- **proof (Thu, Hà Nội, Plus).**
  - Confusion words she lists that the run printed: "Brand Card", the save route.
  - Undefined: "ngày nói chuyện".
  - Week 1 runs 1,194 words and the card 1,394.
  - Southern "chút xíu / tìm tới" in her Zalo template. Her quit line is "nha, nè", so it is not hit, but it drifts.
  - Lost to the cut: her 2,000-contact Zalo, the 3,100-member group, the 20/11 launch, "chấm", and "đừng bắt chị học
    thuộc". The card stores "list_size: khoảng 60 … (em đoán)".
- **coldstart (Minh Anh, Sài Gòn, Free iPhone).**
  - The "hết đau" refusal is given twice (T5, then T6 after her pushback). Both are prompted; it adds load.
  - She asked "mình quay động tác thôi được hông?" and got a good movement-only rewrite. She had to argue twice before
    the quiet CTA.
  - She said "Viết ngắn thôi" and got a 1,082-word box with the card top inside it.
  - The gift has 3 blanks.
- **consultant (Khoa, Đà Nẵng, Claude Pro).**
  - He refused comment keywords flatly at the Map; Week 1 shipped 4 of them. "Tôi không quay video" then cost a
    1,833-word rewrite.
  - Every 1:1 message says "anh/chị".
  - Lost to the cut: LinkedIn as his main channel, and the email list.
  - The save route is in English UI words; "Brand Card" is on his confusion list.
- **service-biz (Đức, Đà Nẵng, Free Android).**
  - The homestay pushback got a calqued line and a wait for a second OK.
  - "Trang" in every CTA.
  - "Lưu vào dự án" on Free is on his confusion list.
  - Thảo can paste everything: copy boxes throughout, which is good.
- **Hạnh S1 (Hà Nội, 45, Free Android, no computer).**
  - Voice mode handled ("em không nói chen vào nữa"), and the mid-dump customer handled ("Không vội đâu").
  - Her confusion words "⋯" and "dự án" are in the save line; "caption" is English.
  - "Dạ, chị gửi em".
  - About 2,750 words over the last 2 replies on Free.
- **Tuấn (Sài Gòn, Plus).**
  - Two questions in one message (his confusion item).
  - A Bắc "nhé" in reply 2 (he "dị ứng giọng Bắc").
  - After typing 'nhẹ' he was told to edit 4 captions himself ("Mấy caption Tuần 1, anh đổi dòng cuối thành câu này là
    được.").
  - The apartment got a #QC Bán kèm post and an inbox path, with a "Cần anh" line that asks 3 things at once.
- **Hạnh S0 (compact).**
  - Same quality as S1, with no method file.
  - Week 1 + card in one 2,162-word reply on Free.
  - `[Tên]` in a message for a cracked screen.
  - "cam kết" in a caption.

Acceptance [quit_points] (17):

| # | Quit point | Hit? |
|---|---|---|
| 1 | method file requested mid-session | no; S0 ran compact mode without asking |
| 2 | Door B project that does not exist | n/a |
| 3 | save-for-reward gate | no; Week 1 always came before the card |
| 4 | nothing back during minutes 8–10 of the dump | no; every chunk answered within 0.5 min, early win 5.6–7.5 min in |
| 5 | brand wall with framework codes | ~ coldstart: card top and the 4,500-character machine block in one box, right after "Viết ngắn thôi". Labelled "không cần đọc" in the other 6 |
| 6 | paid stream parked with no bridge or side door | no; spa side door (Hạnh), apartment Bán kèm (Tuấn), homestay and chống thấm (service-biz) |
| 7 | "locked 90 days" | no ("chạy thử 4 tuần") |
| 8 | "new chat outside the project" | no ("vào đoạn chat mới nhất") |
| 9 | Mac mic not found | n/a; mic tips given. **Unverified: "Windows: bấm Win+H" for Vietnamese dictation** |
| 10 | Claude save without a picture route or backup | ~ consultant: word route + Zalo backup, no picture (as in EN) |
| 11 | keyword CTA with no quiet option | no; the quiet option is always offered. But a spoken objection was argued in 3 runs instead of honoured |
| 12 | email list ignored | **consultant**: 250-person list in chunk 3, never heard. Card "list_size: chưa rõ (em đoán: chưa có danh sách gửi tin)" |
| 13 | two-device Weekly Talk or clip trimming | no |
| 14 | FB insights screenshots required | no |
| 15 | xưng hô asked late | no; reply 1 in 7/7 |
| 16 | reading the script while filming on the same phone | no; beat cards; S0 printed "học thuộc" |
| 17 | Notion-hosted setup page | no |

In all: 1 hit (#12, by omission) and 2 partial (#5, #10).

## 8. Prioritised fix list

Headroom today:
- VN instruction block: 7 chars (7,493 of 7,500).
- VN method file: 9 B (56,311 of 56,320).
- PHONE-STARTER: 235 chars (7,265 of 7,500).
- Every anchor ≤3,368 of 3,600 B.

The P1+P2 kit set below nets −27 chars in the block (→ 7,466) and −18 B in the method file (→ 56,293). The deltas are
measured on NFC text. Lines that also print in PHONE-STARTER change there too. Mirror to EN wherever the same string
exists.

### Kit fixes

**P1: blocks acceptance, or the founder's language concern**

VK-1. **Coach-facing calques on every Map screen** (VN6 in 7/7).
- `strings/vn.toml` `film.now_or_text`: "Quay luôn bây giờ, hoặc đăng caption dạng bài chữ cũng được." becomes
  "Quay luôn bây giờ, hoặc đăng phần chữ làm bài viết." (−9 chars, block).
- `core/vn/start-block.md` step 6: "(muốn nhẹ hơn thì gõ 'nhẹ')" becomes "(ngại xin comment thì gõ 'nhẹ')" (+4).
- `strings/vn.toml` `cta.not_pushy`: becomes "Ai comment cũng nhận quà thật, đâu ép ai. Ngại xin comment thì gõ
  '{{t:cmd.quiet}}'." (−36 B, §CM-CTA-KIT).

VK-2. **A spoken objection to comment keywords is argued, not honoured** (coldstart, consultant, Tuấn).
- `modules/vn/convert.md` §CM-CTA-KIT 5: "Không tự bỏ; lời xả từ chối xin comment thì nhẹ từ đầu." becomes
  "Không tự bỏ; coach chê comment (lúc xả hay sau Bản đồ) là nhẹ luôn." (+9 B).
- `cta.not_pushy` then answers only the question "Nghe như spam?".
- This keeps DECISIONS ("ON by default"; the coach decides) and saves the 'nhẹ' turn plus the self-edit Tuấn was
  given.

VK-3. **One question per message** (I5 and quit_triggers, Tuấn).
- `strings/vn.toml` `setup.multi_income` becomes: "Bạn đang có {n} nguồn thu. Mình đoán nên viết cho {buyer}, vì họ
  mua được nhiều món của bạn. Đúng không?" (−41 B, §CM-SETUP 6).
- The coach still volunteers which stream pays: Tuấn did, in the same answer.

VK-4. **The Map pushback holds Week 1, against DECISIONS K2** ("OK, or any other message, then brings Week 1").
- `modules/vn/message.md` §CM-MAP: "CÃI BẢN ĐỒ, 1 dòng, vẫn chờ OK:" becomes "CÃI BẢN ĐỒ, 1 dòng rồi Tuần 1:" (−1 B).
- Saves 1 turn in coldstart and service-biz.

VK-5. **The dump close costs a round trip in 6/7 runs and can't be timed.** Needs founder OK; mirror EN K1.
- `core/vn/start-block.md` step 3: 'quá ~10 phút: "{{t:dump.enough}}"' becomes
  'quá ~10 phút (~1.300 tiếng): "{{t:dump.enough}}" rồi làm luôn bước 4.'
- `strings/vn.toml` `dump.enough` becomes "Hôm nay vậy là đủ rồi, còn gì nói sau cũng được."
- Net +27 chars (block).
- Effect: −1 coach turn in 6/7 runs (coldstart's Map to 7, the others to 5–6), and a cap the model can count.

VK-6. **Call-centre opt-out in 1:1 replies** (proof, service-biz, Tuấn).
- `modules/vn/guardrails.md` line 6: "(trong inbox thì nói để làm gì, cách dừng)" becomes
  '(trong inbox: để làm gì, "chưa cần thì nói mình")' (+8 B).
- The DỪNG line stays for Zalo series only (§CM-MESSAGES 3, Luật 91/2025).

VK-7. **"anh/chị" and `[Tên]` in 1:1 messages** (consultant ×4, coldstart, Hạnh S0).
- `modules/vn/humanize.md` §CM-NATURAL 4: "tin riêng gọi số ít." becomes
  'tin riêng gọi số ít, không "anh/chị", [Tên].' (+28 B).

**Kit budget for P1:**
- Block: VK-1 −5, VK-5 +27 → +22. Paid by the two cuts in P2 VK-12 (−43).
- Method file: VK-1 −36, VK-2 +9, VK-3 −41, VK-4 −1, VK-6 +8, VK-7 +28 → −33 B.

**P2: real defects in 2+ runs**

VK-8. **"Dạ" from an older chị to a younger em** (proof, Hạnh S1).
- `modules/vn/fmt-short.md` §CM-MESSAGES 5: 'Tin 1 = "Dạ" + đủ quà' becomes 'Tin 1 = đủ quà' (−9 B).
- §CM-NATURAL 4 already says "Nhắn khách, người lớn hơn: "Dạ… ạ"".

VK-9. **Southern words in the ask-3 template for Bắc coaches, and "gặp chuyện"** (proof, Hạnh S1).
- `strings/vn.toml` `research.ask3`: "Nhờ bạn chút xíu:" becomes "Nhờ bạn một chút:" (+1 B).
- `ask3.question`: "Hồi tìm tới mình, bạn đang gặp chuyện gì vậy?" becomes "Hồi mới tìm mình, bạn đang kẹt chuyện gì?"
  (−6 B). This drops the regional "vậy"; the region particle is added per the TIẾNG VIỆT line.

VK-10. **The Map pushback line reads translated** (service-biz).
- `strings/vn.toml` `message.pushback.who`: "Ai cũng xem được hết, mình chỉ chọn viết cho ai thôi." becomes
  "Ai đọc cũng được, bài chỉ nói với đúng một kiểu khách." (+7 B).
- This also removes the I6 FP.

VK-11. **Map line 1 has no "nào" and grows into a 4-method list** (5/7 runs over 45 tiếng).
- `core/vn/start-block.md` step 5: "{ai} hay than" becomes "{ai} nào hay than" (+4 chars).
- "{kết quả theo khoảng, không thì quy trình}" becomes "{kết quả theo khoảng, hay quy trình}" (−6).

VK-12. **Pay for the block** (both cuts are redundant with the method file).
- `core/vn/start-block.md` line 38: drop "(DANG KY = ĐĂNG KÝ)" (−20). "nhận cả cách viết không dấu" stays.
- Step 7: "Đường đi: comment → Messenger → Zalo." becomes "Chốt qua Zalo." (−23). It also assumed Facebook for TikTok
  Tuấn.
- Reply 2: "Bạn cứ xả hết ra nhé:" becomes "Bạn cứ xả hết ra:" (−4). This also fixes the Bắc "nhé" to Nam/Trung coaches.

VK-13. **Unsourced claims stored as proof** (I8, consultant).
- `modules/vn/brain.md` §CM-CARD 3: "proof: đếm được, khách đồng ý," becomes "proof: đếm được, khách đồng ý (không thì
  not_now)," (+22 B).

VK-14. **The dump cut loses list and channel facts** (consultant #12; proof's 2,000 Zalo and FB group). Needs founder
OK, same as G2 EN.
- Either let step 4 guess-ask the list when the dump never named one ("Mình đoán: chưa có danh sách email/Zalo để gửi
  tin. Đúng không?", ~+25 chars in step 4, counted in the 3-question cap), and drop "số bạn Zalo" from §CM-SETUP 5's
  never-ask list;
- or accept #12 by omission for long talkers.

**P2 totals:**
- Block: VK-11 −2, VK-12 −47 → with P1, −27 → 7,466.
- Method file: VK-8 −9, VK-9 −5, VK-10 +7, VK-13 +22 → with P1, −18 B → 56,293.
- Anchors after: SETUP ~3,231, CTA-KIT ~2,497, MAP ~3,374, NATURAL ~3,237, CARD ~3,201, GUARDRAILS ~2,452 (all ≤3,600).

**P3: one run, or cosmetic** (each names its cost)

VK-15. **"ngày nói chuyện" is undefined on Day 0.**
- `strings/vn.toml` `setup.plan_guess`: "ngày nói chuyện {day}" becomes "{day} ngồi kể 15 phút cho tuần sau" (+16 B).
  Fits in the 27 B left after P1+P2.

VK-16. **The card box lacks the Map** (memory risk if only the box is saved).
- `schemas/brand-card.toml`: add `known_for topics[3] keyword` to the machine block. In §CM-CARD 3 this is +28 B.
- Cut: `strings/vn.toml` `month.save_card` ', chạm 2 cái là xong' (−24 B, printed in §CM-CARD 4).

VK-17. **"học thuộc" vs the beat-card default.**
- `core/vn/start-block.md` step 6: "(dưới 30 giây, học thuộc)" becomes "(dưới 30 giây, thuộc câu đầu, câu cuối)"
  (+14 chars). Fits after VK-12.

VK-18. **"Brand Card" and "Lưu vào dự án" are English or unverified UI words** (five personas list them).
- Keep the name (the setup line and card detection use it), but gloss it where the coach first meets it: the TIẾP
  before the card, "Nhắn 'tiếp', em gửi Brand Card (phần em ghi nhớ về chị)". Three runs did this unprompted. About
  +20 chars in the block.
- Cut: " Windows: bấm Win+H." (−20) if Windows voice typing has no Vietnamese. **Verify first.** Also verify the ChatGPT
  Android/iPhone per-message "Lưu vào dự án".

VK-19. **The gift is promised in today's caption before it exists** (service-biz; coldstart's has blanks).
- §CM-CTA-KIT 2 "Đã hứa mà chưa có: viết ngay." Add to step 6: "quà in luôn dưới caption" (about +27 chars; needs
  its own cut), or accept that Week 1 arrives on the next message.

VK-20. **`list_size` is required but never asked.**
- `modules/vn/brain.md` §CM-CARD 3: "list_size" becomes "list_size?" (+1 B).

### Grader fixes (`evals/graders.py`, `evals/run.py`)

VG-1. **I15 English check.** `EN_FUNCTION_WORDS` (L247) holds "than", which is Vietnamese.
- For VN, drop "than", skip ALL-CAPS tokens ("IT") and snake_case card field names (`why_this_one`) at L1797–1800.
- Removes FP in 7/7 runs.

VG-2. **I15 pronoun scan** (L1774–1792).
- Exempt the rendered `map.ok` ("Mình chạy thử…").
- Exempt lines that open with `map.known` / `card.visible.what` (the coach's own "thì tìm {coach}").
- Skip text in brackets ("(vd chị trưởng phòng…)").
- Removes FP in 5 runs.

VG-3. **day0_shape YOUR WORD.** `_norm_word` (L2953) should strip "(không dấu: …)", "không dấu …", "(… đoán …)" and a
trailing ", em đoán …". FP in 5 runs.

VG-4. **day0_shape CTA** (`_slot_capture` L2908, `CTA_FALLBACK_RE` L2926, `cta_keyword` L2932).
- Let "mình gửi" match any self-form (tôi, tui, em, chị, anh, tụi em, a name).
- Let "nhắn riêng" take an optional addressee.
- Accept "hoặc" for "hay".
- Never read the TIẾP line. FP in 4 runs.

VG-5. **SAVE_BACKUP_RE** (L276): add `dự phòng|(?:gửi|chép)[^.\n]{0,20}zalo|cloud của tôi`. FP in 6 runs.

VG-6. **Card found when its top sits inside the copy box** (`_is_card_reply` L2814 and the card-top item). Today the
coldstart card is invisible to the graders.

VG-7. **PLACEHOLDER_RE** (L268): add any bracketed Vietnamese text of ≤24 chars except `[guess]`, `[đoán]`, `[x]`, `[ok]`.
This catches "[động tác 1]" and "[dán quà]".

VG-8. **`_map_label_re`** (L2764): allow a leading "1 " / "1." and a "BẢN ĐỒ" heading. FP consultant.

VG-9. **I9** (L1450): skip quotes that are kit text (`kit_tokens` L770). FP consultant.

VG-10. **I11** (L1535): drop negated hits ("không phải cam kết", "không … cam kết"), the card top's "không bao giờ:"
segment, and the `principles` / `rhythm` values. FP in 4 runs.

VG-11. **I23** (L2317): a never-word right after a negation, which the coach said in that form, is theirs ("không giảm
sốc gì hết"). FP in 2 runs.

VG-12. **vn_natural** (`vn_sentences` L2536, `_vn_pieces` L2563).
- Drop direction lines ("Chữ trên màn hình", "Khung hình đầu", "Cảnh n", "chữ:"), and "Ý n" notes when
  delivery=beat-cards.
- Compare written pieces with written-posts.md; compare spoken lines separately.
- With this, proof and Tuấn pass, and coldstart and Hạnh S0 still fail (real).

VG-13. **New VN message checks** for the misses in section 5:
- X10 "anh/chị" in a 1:1 copy box;
- "DỪNG" in an inbox reply outside a Zalo series;
- "Dạ" opening a 1:1 box when `address_1to1` puts the coach above the reader (chị–em, anh–em);
- a Bắc-only particle in a south/central run's reply 2 (low).

VG-14. **quit_triggers** (L2735): read the persona's own "Bỏ ngang khi" list. Two questions is "Dễ rối" for Tuấn and
counts under I5 only.

VG-15. **VN piece titles** in `FORMAT_TITLE_RE` (L141): "Bài dài", "Bán kèm", "Quà", "Tin trả lời inbox n", "Tin
Zalo", "Thứ Tư, 07/10 · Zalo". Today the long post merges into N1.

VG-16. **`run.py summary`**: print active minutes in "Film-ready min" (Hạnh 19.9 / 20.2, not 44.9 / 45.2). Same bug as
G2.

### Simulator and protocol fixes

VP-1. **The Free-plan model differs by run.**
- coldstart modelled a 165-min hard stop after 10 messages.
- Hạnh S1, Hạnh S0 and service-biz modelled "falls back to a smaller model, no stop" at 8–10 messages.
- `COACH.md` should fix one rule for ChatGPT Free and Claude Free, so timing is comparable across personas.

VP-2. **Chunk 3 always holds channels, lists, hours and launch dates** in every VN persona, so the cut always drops
them.
- What was lost: consultant's email list and LinkedIn; proof's 2,000 Zalo, group, 20/11 launch and "chấm"; service's
  Tết slots and capacity; coldstart's offer idea and camera fear.
- Fix: move one "kênh + danh sách" sentence into chunk 1 or 2 for at least 2 personas, or label them long talkers and
  grade #12 by omission.

VP-3. **"chấm" / threshold is untested in VN.** Move proof's "Bài chấm với đủ 100 comment…" pushback into chunk 2 or the
Map turn, so I14 runs in at least one VN run.

VP-4. **The early-win budget is unreachable with these personas.** Chunk 1 is dictated for 4.6–6.1 minutes against the
kit's "kể xong một chuyện (2–3 phút) thì gửi", so early win lands 5.6–7.5 minutes into the dump (acceptance ≤4,
ungraded). Split chunk 1, or grade the budget against the persona's real send.

VP-5. **Notes classify a few items differently from this review.**
- proof calls inclusive "Mình chạy thử…" a real defect; I find it natural.
- coldstart calls film-ready 18.4 "talking-head"; I count it, since the machine could not know about her camera fear,
  but I report her filmable minute as 21.0.
- Keep this reviewer pass for VN until VG-1 to VG-13 land.

## Fix round

Done 6 Oct, uncommitted. The founder's DECISIONS bullet "Long dumps, missing facts, an early piece to post" supersedes
VK-5 and VK-14. Build OK; lint 0 errors (31 warnings); 397 tests OK. VN sizes: block 7,495 / 7,500 chars; method
file 56,318 / 56,320 B; PHONE-STARTER 7,275 / 7,500; ship.kit 923 / 1,000; largest anchors MAP 3,339, SETUP 3,343
(of 3,600 B). Each added byte is paid by a cut named in its module header or at the top of `strings/vn.toml`. Re-grade
tables: `grader-fixes.md` "After the fix round".

Kit:
- VK-1 applied: `film.now_or_text` "Quay luôn bây giờ, hoặc đăng phần chữ làm bài viết."; step 6 "(ngại xin comment thì gõ 'nhẹ')"; `cta.not_pushy` drops "đâu có ép ai".
- VK-2 applied: §CM-CTA-KIT 5, an objection in words (dump, Map or later) → quiet at once, unposted pieces reprinted; "Nghe như spam?" alone gets not_pushy.
- VK-3 applied: `setup.multi_income` is one question (EN too).
- VK-4 applied: "CÃI BẢN ĐỒ, 1 dòng rồi Tuần 1" (EN too).
- VK-5 superseded by DECISIONS: soft cut past ~1,500 tiếng, `dump.enough` carries the first guess.
- VK-6 applied: inbox replies say "chưa cần thì nói mình"; DỪNG stays for Zalo series.
- VK-7 applied: §CM-NATURAL 4 "không "anh/chị", [Tên]".
- VK-8 applied: "Tin 1 = đủ quà".
- VK-9 applied, own wording: "Nhờ bạn một chút"; ask3.question "Hồi mới tìm đến mình, bạn đang loay hoay nhất chuyện gì?".
- VK-10 applied: `message.pushback.who` "Ai đọc cũng được, bài chỉ nói với đúng một kiểu khách."
- VK-11 applied: "{ai} nào hay than", "{kết quả theo khoảng, hay quy trình}".
- VK-12 applied: reply 2 and `mic.claude_vn` drop "nhé"; "Chốt qua Zalo."; the (DANG KY = ĐĂNG KÝ) example dropped.
- VK-13 applied: "proof: đếm được, khách đồng ý (không thì not_now)".
- VK-14 superseded by DECISIONS: the dump prompt lists "đăng ở đâu, có danh sách Zalo, email chưa"; "số bạn Zalo" off the never-ask list; the plan line names the list.
- VK-15 applied through `setup.plan_guess` ("{day} hằng tuần kể 15 phút cho tuần sau").
- VK-16 partly: the `month.save_card` cut applied; the Map in the card's machine block deferred (schema change, needs bytes).
- VK-17 applied: "(dưới 30 giây, nhớ ý rồi nói)".
- VK-18 declined: no block budget for the gloss. Win+H verified to support Vietnamese, so `mic.windows` stays; the per-message "Lưu vào dự án" route is still unverified.
- VK-19 applied: the gift in a copy box under today's caption; "chưa viết thì không hứa" (EN too).
- VK-20 superseded by list_size = ask|{n}.
- EN K mirrors: K22, K24, K25, K26, K27, K30, K31 applied; K28 declined (the block's Zalo backup already prints; no bytes); K29 deferred (about 38 B; method file has 2 B); K33 not needed (VN has no conflicting clause).

Graders:
- VG-1 applied.
- VG-2 applied, narrowed in verify (only the inclusive "mình" of map.ok; only example brackets).
- VG-3 applied (`word_head()`).
- VG-4 applied.
- VG-5 applied.
- VG-6 applied.
- VG-7 applied.
- VG-8 applied.
- VG-9 applied (kit-wording skip; low risk noted).
- VG-10 applied.
- VG-11 applied.
- VG-12 applied.
- VG-13 applied as the new `vn_messages` check; series labels narrowed to "chuỗi" / "series" in verify.
- VG-14 applied: Tuấn's quit_triggers is now warn / confusion; his two-question defect still fails I5.
- VG-15 applied.
- VG-16 applied.

Simulator and protocol:
- VP-1 deferred (one Free-plan rule in COACH.md).
- VP-2 deferred; the soft cut and facts asked up front cut its cost, but a re-run must show it.
- VP-3 deferred ("chấm" in chunk 2).
- VP-4 partly: G15 grades the early win against the persona's first send; chunk length unchanged.
- VP-5 deferred (keep this reviewer pass until a VG2 run confirms VG-1..VG-13).

Eval cases: `evals/cases/*.vn.toml` are stale and get a full rewrite next; none was edited (all regexes compile).

Open: the VN budgets are spent (block 5 chars, method file 2 B), so K28/K29/VK-16/VK-18 each need a named cut; the
service-biz whole card (7,078 > 6,600) has no fix; re-grading VG1 transcripts needs HEAD strings (the new
`setup.dump_posts` hides their dump prompt); DỪNG in outbound one-to-one Zalo needs a reviewer's ruling; re-run VG2.
