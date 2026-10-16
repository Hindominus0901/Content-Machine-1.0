Result: FAIL (valid run; all 9 v13.1 real failures fixed or mostly fixed, 1 of them partly; the grader's FAIL is now mostly false, with 3 small real slips and 4 kit gaps left)

# Retest v13.2: VN copywriter-thin, Day 0 + second chat, S1 + web, level-ups shipped

Reviewer: the simulator of this run, reviewing afterwards against the standards. I did not write the kit. Same trigger and rubrics
as retest-v131 (`qa/standards/calendar.md`, `strategy-doc.md`, `banks.md`, `copy-frameworks.md`, `channel-teardown.md`, `hub.md`,
`hook-lab.md`, `research-brief.md`, `vn-naturalness.md`), plus the v13.1 review's real failures and ten defects as the checklist.

## Method (same as retest-v131)
- Persona change first: `evals/personas/vn/copywriter-thin/answers.md` got a `dig.channels` line in the Answer bank (her broken
  English; 3 channels she likes and 3 she competes with, described by kind, no names: an American copywriter's weekly newsletter on
  listening before writing, an older Vietnamese copywriter who takes sales pages apart on Facebook, an English podcast on small 1:1
  service businesses; "một chị làm copywriting trên TikTok hay nói về sale page", a man selling a content course for coaches
  ("post every day", templates), an ads agency for coaches that promises inbox; "I don't write their names"). In v13.1 she had to
  type "skip" there.
- Packet: `python3 evals/run.py --root <scratch git-archive of HEAD 4511a15> packet --suite day0 --edition vn --lane S1 --persona
  copywriter-thin --web --tag v132 --today 2026-10-09 --out <scratch>`, folder copied to `evals/runs/v132-copywriter-thin/`. The
  kit was built in a clean copy of HEAD so the repo's `dist/` was not written; that build is byte-identical to the repo's `dist/vn`
  (`diff -rq` clean). build_sha 518cc0871370, all 9 level-ups in `packet/kit/Level-ups/`; COACH.md and MACHINE.md byte-identical to
  v131's. HEAD did not move during the run.
- Two roles kept apart. MACHINE read only `packet/kit/`: the block, then the §CM- sections it names (method §CM-OPTIONS, MEMORY,
  SETUP, DIG, CARD, TODAY, WEEK, FORMATS, POSTS, MESSAGES, MAP, DRIFT, CTA-KIT, RESEARCH-LITE, EDGE, VOICE, HUMANIZE, NATURAL,
  GUARDRAILS, LOCALE; PLAYBOOK engine/tiers/lines/calendar/doc; RESEARCH §CM-RESEARCH/LISTEN/CHANNELS/AUDIENCE/NICHE). COACH answered
  only from `persona.toml`, `answers.md`, `written-posts.md`: English dictation for the dump and answers, "banj", "ok", "A", her
  pushback lines verbatim.
- **Pace rules checked before writing coach times** (`evals/run.py` check_pace: a dictated chunk ≥ words/160 active min; a pasted
  post ≥ 0.5 min each; COACH.md: 130 wpm dictation, 30–40 wpm typing, 200 wpm reading, machine reply = coach + 0.3). Chunks 1–4 took
  1.8 / 1.5 / 1.4 / 0.9 min (need 0.74 / 0.89 / 0.83 / 0.48); the paste turn (2 posts) 1.9 (needs ≥ 1.0). **Protocol: valid**
  (turns, pace, edits pass; leaks warn only; research_leaks pass on 16 queries; edited: 0).
- Research: real WebSearch/WebFetch, read-only, 16 queries logged with the turn they ran after (3, 5, 8, 9, 11, 12), 13 pages
  opened, 12 read, 3 sites (Voz, VnExpress, Substack; 7 hosts). Afterwards I re-fetched the 10 kept lines with an exact-string
  prompt: 10 of 10 verbatim (lines 4 and 5 are one VnExpress commenter); one Voz line was dropped on re-fetch (no stated role). Caveat: I had read `expected.toml` as reviewer before playing;
  Q8 matches one of its query forms (logged in notes.md; no line kept from it).
- Flow played: xưng hô → dump (chunk 1, the 2 pasted posts, chunks 2–4) → 6 interview questions, one ask each (channels now
  answered) → strategy in 3 steps (each one A/B/C: channel to read, how to read closed places, hours) → "Show me the research" →
  "B … ok" → ONE reply: FILM TODAY + caption + gift + inbox replies + Week 1 table + N1–N5 + ask-3 Zalo + Chrome box + files + Brand
  Card + save lines → testimonial trap → **new chat** two days later, "tiếp" → reminders A → calendar links. No app cut modelled.
- Artefacts: `transcript.jsonl` (graded, frozen as `transcript.raw.jsonl`), `transcript.md`, `notes.md` (Research log),
  `CHIEN-LUOC-NOI-DUNG.md`, `NICHE.md`, `HUB.md`, `grades.json`.

## Turns and time
| | Coach turns | Active min | Budget | v13.1 |
|---|---|---|---|---|
| Strategy step 1 (after 7 setup/dump + 6 interview) | 13 | 17.7 | VN 7 + 6 turns, ≤25 min ✓ | 13 · 15.2 |
| Strategy step 3 (the OK step) | 15 | 22.0 | ✓ (grader strategy_minutes 22.0) | 15 · 21.1 |
| FILM TODAY ready (one reply with Week 1 and the card) | 17 | 27.3 | ≤35 acceptance ✓ · **≤24 brief ✗ (+3.3)** | 17 · 30.3 |
| Day 0 end (testimonial trap answered) | 18 | 37.5 | **≤45 min ✓ · ≤17 turns ✗ (18)**; grader 11 + 6 + 2 = 19 ✓ | 18 · 40.1 |
| Second chat (new chat, Sun 11/10) | 2 | ~2.0 | — | 2 · ~1.5 |
| Total | 20 | 39.5 (grader) | | 20 · 41.7 |

Words the coach reads (tiếng, whole reply): strategy steps 248 · 187 · 314 (grader strategy_talk_words 314, under 450; kit caps
≤250 · ≤150 · ≤250: steps 2 and 3 over); the research view 394 (v13.1 1,082); after the OK, one line (≈25 tiếng) before FILM TODAY.
Where the 3.3 minutes over the 24-minute target went: the "Show me the research" detour (24.1 → 27.0, 2.9 min and one turn) and her
new 141-word channel answer (1.5 min where v13.1 had a 0.6-min "skip"). Without the detour: film-ready ≈ 24.4 min, Day 0 17 turns.
The interview took 6.9 min (v13.1 5.8), the three strategy readings and choices 6.4 min (v13.1 8.8).

## Grader results (`python3 evals/run.py grade evals/runs/v132-copywriter-thin`)
`FAIL I2, I6, I11, quit_triggers, day0_timing, day0_strategy, hook_lab, strategy_doc, research_log · edited: 0`. **Valid run.**
PASS now: I9, I15, I23 (7 of 9 pieces of 60+ tiếng carry her phrases, 78%), deny_list, day0_shape, lengths (shorts 539 · 519 ·
522 · 524 spoken tiếng, long post 918, email 245), vn_natural (particles 17% vs her 20%), vn_messages, running_tag, research_leaks;
I3, I5, I8 still pass. v13.1 failed I9, I15, I23, deny_list and day0_shape; all five pass.

| Check | Real / FP | Note |
|---|---|---|
| I2 | **FP** | "điền form" is the kit's own R3 Chrome-box safety line, negated ("Không đăng, comment, …, điền form, đăng nhập…"); the line above the box ("rồi dán kết quả lại đây") makes the grader read the whole box as a form she fills |
| I6 | **FP** | "bước 3 chọn giờ" in the step-2 header ("TUYẾN BÀI (cho khoảng 3 tiếng một tuần, mình đoán; bước 3 chọn giờ)") is a pointer to the next step, read as a second decision next to the one A/B/C |
| I11 | **real (machine)** | "lớp duy nhất không ai chép được của bạn" (N2 Ý 2): a sentence added while lengthening the short to 500+ tiếng; "duy nhất" is on the block's LỜI HỨA list |
| quit_triggers | **FP (both items)** | "điền form" (as I2); "1081 words before … early win": the early win is at turn 3, but v13.2 dropped the quote marks on the 3 câu đáng tiền and the grader's usable_at only knows the early win as 2+ quoted lines |
| day0_timing | **FP** | "early win 20.5 active minutes after the dump started (max 4)": same cause (it finds the first "usable" thing at turn 15); film-ready, strategy, map turns (14 seen, limit 7 + 6 dig answers + 2 step OKs) and session limits pass |
| day0_strategy | **FP** | only the "chọn" of I6; every other item passes (one A/B/C per step with exactly one "(máy khuyên)", OK read at the end of "B. Three hours… ok", 4 pillars, 40/40/20, WHAT I FOUND 3 lines with sources) |
| hook_lab | **FP (grader) · real smell (kit)** | N2 on-screen "AI đâu có gặp khách bạn" vs first line "Mình hỏi coach nghiên cứu khách thế nào, câu trả lời hay gặp nhất là vầy.": the overlap is "gặp", "khách" used differently; the on-screen adds a contrast. But the on-screen line is the kit's own HAY example in §CM-FORMATS 1, copied verbatim (defect 6 below) |
| research_log, strategy_doc | **real (machine), minor** | KEEP line 4 ("Không hiểu họ đã trải nghiệm bao nhiêu tình huống trong cuộc đời", VnExpress) is about life experience, not "toàn lý thuyết, chưa tự làm được"; lines 1, 2, 5 still give 3 people on 2 hosts. strategy_doc fails on the same KEEP (its "holds" quote "sau 4 tập, theo số của bạn ở buổi thứ Sáu." is a parsing slip) |
| leaks | warn only | 5 warnings, all Vietnamese renderings of what she dictated or said ("chỉ kéo thêm người tới thứ chưa ai muốn" = "pull more people to something nobody want"; the August numbers) |

Real failures: 2 graded (I11, the KEEP line) + 1 ungraded machine slip (copying the kit's example hook). False: I2, I6,
quit_triggers ×2, day0_timing, day0_strategy, hook_lab's reason. Not graded but real against the kit: strategy steps 2 and 3 over
their own caps (187 > 150, 314 > 250).

## Verdict per area
| Area | Verdict | Evidence |
|---|---|---|
| A/B/C at each step, one recommended | **PASS** | Steps 1–3 each carry exactly one A/B/C with "(máy khuyên): reason" after the bracket ("B) 2 bản tin Substack … (máy khuyên): cùng tệp khách là coach, có bài trong 90 ngày…"); reminders A/B in the second chat. No "Bạn có muốn…không?" |
| Strictly sequential | **PASS** | dump → interview → 1/3 → 2/3 → 3/3 → research view → OK → pieces; the view ends "Bước 3/3 vẫn đang chờ bạn: số giờ mỗi tuần. A) … B) … (máy khuyên) … C) …" |
| ≤1 question per reply | **PASS** | every reply ≤1 "?"; interview replies 2–6 are the question only (no "Mình nhận rồi.", §CM-DIG 4 v13.2); dig.offer is now one ask ("Khách làm với bạn thì nhận được gì, trả bao nhiêu?") |
| Research done, sources, buyer lines | **WEAK** | 16 queries, 13 pages, links in the one-screen view, 9/9 re-fetched lines verbatim. Still 0 lines from Nhi's buyer (a coach) at 2 places (3rd run in a row); the KEEP is again the coaches' audience; Facebook groups and TikTok unread |
| Liked + competitor channels | **WEAK** | She now names 6 channels by kind; none could be identified (no names) or opened (TikTok, Facebook); the machine offered its own 2 Substack finds as the recommended B and read 24 titles, 2 posts, 0 comments. Her kinds are in NICHE.md "Tiếng nói lớn" as unread |
| Niche (NICHE.md) | **WEAK** | 7,136 B (5,919 characters, inside C6's 6,000), 13 sources, full query list; prices and seasons still "(mình đoán)" |
| Broad pillars | **PASS** | "Nghe khách nói · Vì sao người ta mua · Viết để bán · Gói và cách bán", each with a reason; grader parses exactly 4 |
| Content lines per pillar | **PASS-** (kit conflict) | 8 lines at 3 hours (v13.2 cap ≤8 ✓), CHUYỂN ĐỔI weekly ✓; "Gói và cách bán" has NIỀM TIN + CHUYỂN ĐỔI, no THU HÚT (defect 2); lines built for hours the coach is asked one step later (defect 1) |
| Mix | **PASS** | 40/40/20 with her goal as reason; month THU HÚT 8 · NIỀM TIN 8 · CHUYỂN ĐỔI 4 |
| 4-week calendar | **PASS** | Week 1 table only in chat, after FILM TODAY; weeks 2–4 in the strategy file part 6 with totals and hours; 2 lines run once in month 1 (said) |
| One framework + one bank item per piece | **PASS** (silent) | FILM TODAY flip-a-belief, N1 one-scene with the research KEEP, N2 debunk-the-advice, N3 open-loop long post with the August result, N4 objection, N5 short letter |
| Word lengths | **PASS** | 539/519/522/524 spoken, 918 long, 245 email. Drafts landed 436–484 and were lengthened before printing (§CM-HUMANIZE 7) |
| Hooks strong | **PASS (grader: FP fail) / WEAK (me)** | FILM TODAY's on-screen "Tim nhiều, chẳng ai hỏi giá" now says the buyer's problem (v13.1 "Thiếu lý do, không thiếu bài" was a flat contrast); N2's on-screen is the kit's example copied |
| Vietnamese only, natural | **PASS** | no English in pieces, particles 17%, her phrases in 7 of 9 pieces ("Khách không đến từ bài đăng. Khách đến từ chuyện họ tin bạn đủ để nhắn một tin." in FILM TODAY; "Nên đừng hỏi đăng mấy bài một tuần." in N3; "Chị ơi, em là Nhi nè." in the ask-3 Zalo); 0 bare "trụ cột"; 3 câu đáng tiền unquoted |
| Guardrails | **PASS-** | testimonial refused with a consent Zalo ("Câu … mình chưa đưa vào bài: chị ấy chưa nói cho dùng công khai."); August result carries "Kết quả của một coach thôi, tuỳ người, không phải cam kết"; one "duy nhất" slipped into N2 |
| Strategy doc (SD1–SD12) | **PASS-** | 9 parts in order, all 4 tables in part 6, lines, mix, system, gift, ladder, research basis; "Vì sao là bạn" left as [CẦN BẠN: …]; the pillar-4 gap and the once-a-month lines said openly |
| Hub + HUB.md | **PASS** | no hub A/B/C on Day 0, HUB.md 7 parts, 2,707 B, one "Lưu:" line |
| Memory resume (new chat "tiếp") | **PASS** | "Brand Card v1 ✓ / Mình nhớ: chiến lược đã OK hôm 9/10 (4 trụ cột nội dung, 40/40/20, từ khoá HỎI GIÁ) … · đang dở bước: cài lời nhắc trên lịch." then reminders A/B |

## v13.1 → v13.2, real failure by failure
| # | v13.1 real failure | v13.2 | Quote (turn) | Notes |
|---|---|---|---|---|
| 1 | I9: 3 câu đáng tiền quoted from English dictation | **fixed** | "Mình nhận rồi. 3 câu đáng tiền bạn vừa nói: / - Khách hỏi gì, bạn cũng hỏi lại đúng một câu: vì sao." (3) | block step 3 and §CM-SETUP 2 now agree with §CM-NATURAL 1; I9 PASS. Side effect: the grader no longer sees the early win (grader gap 1) |
| 2 | I15: bare "chị" for the finance coach while the coach is "bạn" | **fixed** (machine) | "Có tin chị ấy đồng ý là mình đưa vào N3 ngay" · "Chị ấy trả lời rồi thì dán vào đây" (18) | no kit change was made; the machine kept §CM-NATURAL 2; I15 PASS |
| 3 | I23: 0 of 10 pieces use her phrases | **fixed** | "Khách không đến từ bài đăng. Khách đến từ chuyện họ tin bạn đủ để nhắn một tin." (17, FILM TODAY Ý 2) · "Nên đừng hỏi đăng mấy bài một tuần." (17, N3) | KIỂM TRA 3 "câu hay nói (≥ nửa số bài)"; 7 of 9 = 78% |
| 4 | deny_list: bare "trụ cột" 3× | **fixed** | "Đã chốt: điều khách nhớ, 4 trụ cột nội dung, kênh B." (14) · "(4 trụ cột nội dung, 40/40/20, từ khoá HỎI GIÁ)" (19) | §CM-NATURAL 7 row and §CM-OPTIONS 1 rewording; deny_list PASS |
| 5 | quit "300 words before usable" (step 2: 431 words of talk) | **fixed** (that cause) · grader still FAIL (FP) | step 2 is 187 tiếng whole (14) | v13.2 "tin 2 ≤150 … (tuyến: mỗi cụm một dòng tên · loại, bảng đủ vào file)"; the FAIL now comes from the unquoted early win and "điền form" (both FP) |
| 6 | "(máy khuyên: …)" form, 3 lines read as unmarked | **fixed** | "A) bạn có Claude in Chrome hay ChatGPT Work: mình gửi khung, bạn dán vào Chrome, 15 phút (máy khuyên): coach nói thật trong nhóm" (14) | §CM-OPTIONS 3 "(lý do sau ngoặc)" + strings; every marked-option item passes |
| 7 | YOUR WORD rendered from English with no guess tag | **fixed** | "TỪ KHOÁ: HỎI GIÁ (gõ HOI GIA cũng nhận; mình đoán: bạn kể bằng tiếng Anh, Tuần 1 kiểm lại)." (15) | TỪ KHOÁ "Chưa đủ, hay kể tiếng Anh: … (mình đoán…)"; day0_shape PASS |
| 8 | N4 had the keyword only in the ask | **fixed** | "Coach làm 1 kèm 1, … tuần nào cũng đăng, tim nhiều mà không ai hỏi giá." (17, N4 Ý 4) | KIỂM TRA 0 "từ khoá có cả ngoài lời mời"; every piece carries it in the body |
| 9 | KEEP line that does not say the pattern | **not fixed** (machine) | "Không hiểu họ đã trải nghiệm bao nhiêu tình huống trong cuộc đời" listed under KEEP "người lạ nghi coach toàn lý thuyết" | rule 5 already says it; a different weak line this time; the KEEP still stands on lines 1, 2, 5 |

v13.1 kit defects (its "Top remaining defects"), for completeness:
| v13.1 defect | v13.2 | Quote (turn) |
|---|---|---|
| 5 Option A "mình đọc luôn" untrue in a Project | **fixed** | "A) … mình gửi khung, bạn dán vào Chrome, 15 phút" (14); the Chrome box comes with Week 1 |
| 6 Day-0 research view 1,082 tiếng, ~5.6 min | **fixed** (mostly) | one screen, 394 tiếng, "Một màn hình, câu nào cũng chép y trên trang, kèm link; đủ từng lượt tìm, từng trang ở NICHE.md." (16); the detour still costs 2.9 min and a turn |
| 7 Strategy step 2 over a screen | **partly** | 187 tiếng (v13.1 473) but over the kit's own ≤150; step 3 314 over ≤250 |
| 8 Content-line arithmetic | **partly** | 8 lines at 3 hours, CHUYỂN ĐỔI weekly; the "every pillar THU HÚT + NIỀM TIN" rule still breaks with 4 pillars, and lines now depend on hours asked a step later |
| v13 defect 5: drafts land short | **fixed** | 4 shorts 519–539 on print (drafts were 436–484; lengthened before printing) |
| Smaller: Claude micro line right after "bấm micro nhỏ trong ô chat" | **not fixed** | turn 2 still says both |
| Smaller: "Không lộ … tên file" vs file-naming lines | **not fixed** | the block keeps "Không lộ … tên file"; the reply names CHIEN-LUOC-NOI-DUNG.md, NICHE.md, HUB.md as §CM-STRATEGY-DOC 1 asks |

## Top remaining defects (file · section · fix)
Budgets: VN block 8 chars left, VN method 19 B left, STRATEGY-VN 16 B left (no change proposed there); PLAYBOOK-VN 4,502 B
(45,056 − 40,554) and RESEARCH-VN 6,179 B (54,272 − 48,093) of headroom. Deltas are UTF-8 bytes. The method package is byte-neutral.

1. **Lines are fixed before hours are known** (step 2 asks for lines "theo giờ", step 3 asks the hours; the machine guessed 3 hours
   and then recommended 3 hours on the strength of its own guess). `modules/vn/strategy-doc.md` `strategy-doc.grow-engine` 1 (PLAYBOOK
   §CM-STRATEGY-ENGINE 1): move the hours A/B/C into tin 2 and the reading A/B/C into tin 3: "tin 2 bước 3–4 (tuyến: …) + cách đọc nơi
   chưa mở được, hỏi một lần (§CM-RESEARCH) · tin 3 bước 5–8 (chưa biết số giờ: A/B/C số giờ; …)" → "tin 2 số giờ (chưa biết: A/B/C)
   + bước 3–4 (tuyến theo mức máy khuyên: …) · tin 3 bước 5–8 (lịch chỉ chọn kiểu, chưa in bảng) + cách đọc nơi chưa mở được, hỏi một
   lần (§CM-RESEARCH)" (≈ +10 B PLAYBOOK). Same order in `modules/vn/message.md` §CM-MAP: "· 2 tuyến bài, tỷ lệ; nơi chưa mở được: A/B/C
   đọc bằng cách nào, hỏi một lần (§CM-RESEARCH) · 3 hệ thống, số giờ," → "· 2 số giờ, tuyến bài, tỷ lệ · 3 hệ thống; nơi chưa mở được:
   A/B/C đọc bằng cách nào, hỏi một lần (§CM-RESEARCH)," (method ≈ 0 B: words moved) and `modules/vn/research.md` R0 header "ngày 0 ở
   tin chiến lược thứ 2" → "thứ 3" (0 B).
2. **Four pillars at 3 hours cannot all carry THU HÚT + NIỀM TIN plus a CHUYỂN ĐỔI line in ≤8** (pillar 4 lost its THU HÚT).
   `modules/vn/strategy-doc.md` `strategy-doc.grow-lines` 1 (§CM-CONTENT-LINES 1): "cụm có 2 tuyến thì mỗi loại một." → "cụm có 2 tuyến
   thì mỗi loại một; cụm giữ tuyến CHUYỂN ĐỔI thì NIỀM TIN + CHUYỂN ĐỔI." (+58 B), and §CM-STRATEGY-DOC 4 SOÁT and part 3 "cụm nào cũng
   có tuyến THU HÚT và tuyến NIỀM TIN" → "… (trừ cụm giữ tuyến CHUYỂN ĐỔI)" (+2 × 36 B). PLAYBOOK +130 B.
3. **Strategy caps the required content cannot meet** (step 2 187 > 150, step 3 314 > 250; acceptance's 450 passes). The line rows
   are talk. `strategy-doc.grow-engine` 1: "(tuyến: mỗi cụm một dòng tên · loại, bảng đủ vào file)" → "(tuyến: một khung chép, mỗi cụm
   một dòng tên · loại; bảng đủ vào file)" (+18 B PLAYBOOK) and after "tin 3 bước 5–8" add "(lịch, quà mỗi thứ ≤12 tiếng)" (+33 B).
   `modules/vn/message.md` §CM-MAP "tin 2 ≤150 (bảng vào file)" → "tin 2 ≤150 (tuyến trong khung)" (+5 B method; package with fix 6).
4. **Channels described by kind are never read** (her 6 channels: no names; the machine searched by kind, found none, and offered its
   own finds). `modules/vn/channel-research.md` C1 (RESEARCH §CM-CHANNELS) after "kênh bạn kể khi đủ 2+, không thì kênh mình tìm.":
   add "Coach tả kênh mà không nêu tên: tìm theo kiểu tả (nền tảng + chủ đề), YouTube, Substack trước; A) ghi "kênh bạn tả, cần tên";
   khung Chrome Tuần 1 đọc luôn kênh đó." (+≈190 B RESEARCH).
5. **Zero lines from Nhi's own buyer for the third run** (coaches talk in closed Facebook groups; the open web gives their audience).
   `modules/vn/research.md` R3 2 (§CM-LISTEN) after "tiêu đề nhiều view nhất của đối thủ.": add "Người mua là người làm nghề (coach,
   chuyên gia): bài tự kể của người cùng nghề (Substack, Spiderum), comment dưới bài của kênh dạy nghề đó; nhóm nghề chỉ qua Chrome."
   (+≈200 B RESEARCH). The Day-0 line 1 and keyword stay "(mình đoán)" until then, as they did here.
6. **The kit's HAY hook example is this persona's niche, and gets copied verbatim** (N2's on-screen = §CM-FORMATS 1's example).
   `modules/vn/fmt-short.md` §CM-FORMATS 1 "HAY: chữ "AI đâu có gặp khách bạn" · khung đầu: chat AI gõ dở "từ khoá cho coach" · câu đầu:
   "Đọc vài bài, hỏi AI một câu, vậy mà gọi là hiểu khách?" · câu cuối: "Hiểu khách là nghe họ kể, tới lúc họ nói ra câu bạn không đoán
   được."" → an example from another niche of about the same length (e.g. a spa: chữ "Khách quen đi đâu rồi?" · khung đầu: sổ hẹn tháng
   này trống ba dòng · câu đầu: "Ba khách quen của chị không quay lại, mà không ai chê câu nào." · câu cuối: "Khách không chê thì cũng
   không nói, mình phải hỏi trước."). **Method package 3 + 6: ≈ −5 B net**, within the 19 B left.
7. **The research detour still costs the 24-minute target** (2.9 min, and the 18th Day-0 turn; the coach asks because WHAT I FOUND
   names places but no link). `modules/vn/research.md` R3 kết quả 1, third template line: "Chưa đọc được: {nơi} (bạn dán thì mình đọc) ·
   gõ "xem nghiên cứu" để xem từng câu, kèm link." → "… · câu GIỮ đầu: {link} · gõ "xem nghiên cứu" để xem từng câu." (+≈20 B RESEARCH).
   Worth a test, not a sure win: this persona asks for "every process", and the view itself is already one screen.
8. **Lengthening invites claims** ("lớp duy nhất…" was added to reach 500 tiếng). Machine slip against the block's LỜI HỨA; §CM-HUMANIZE
   7 already says "thêm cảnh, ví dụ". No kit change proposed (method room is taken by 3 + 6).
9. **KEEP lines that do not say the pattern** (line 4). Machine slip against RESEARCH rule 5. No kit change.
10. **Turn 2 still tells a Claude coach to tap the chat mic, then not to** ("bấm micro nhỏ trong ô chat …" then "Dùng micro trên
    bàn phím điện thoại, vì micro của Claude chưa nghe được tiếng Việt."). `strings/vn.toml` `mic.claude_vn` → "Micro nhỏ của Claude
    chưa nghe được tiếng Việt: dùng micro bàn phím điện thoại." (a correction of the line before, not a second instruction; about
    −4 chars in the block, which has 8 left).

## Grader gaps to hand the integrator
1. `usable_at` / `early_win` know the early win only as 2+ quoted lines; v13.2 dropped the quotes for English dictation, so a run
   that follows the kit fails `day0_timing` ("early win 20.5 min after the dump started") and `quit_triggers` ("1081 words before
   anything usable"). Accept the early-win lead line (strings `setup` "3 câu đáng tiền bạn vừa nói:") followed by 2+ list lines.
2. `I2` / `quit_triggers` "điền form": a template word inside a negated list ("Không đăng, …, điền form") in the kit's own R3 Chrome
   frame is read as asking the coach to fill a form (BACK_RE on "dán kết quả lại đây" pulls the box in). Skip negated hits, or the box
   that opens "CHỈ ĐỌC, NGHE KHÁCH".
3. `I6` / `day0_strategy`: "bước 3 chọn giờ" (a forward pointer in a header) counts as a second decision.
4. `hook_lab` onscreen_repeat: two shared tokens used in different senses ("gặp", "khách") count as the on-screen repeating the first
   line (100%), though the on-screen adds a contrast the first line lacks.
5. `strategy_doc` quotes "sau 4 tập, theo số của bạn ở buổi thứ Sáu." as the sentence that "holds" the KEEP; the failure itself
   (research_log's weak line) is right, the quoted sentence is not the one that cites it.

## What improved against retest-v131
- All five v13.1 grader failures that were real kit or machine misses on language and form now pass: I9, I15, I23, deny_list,
  day0_shape; the "(máy khuyên)" form, the keyword's guess tag and the keyword in N4's body are fixed.
- Day 0 down from 40.1 to 37.5 active minutes; film-ready from 30.3 to 27.3; the research view from 1,082 to 394 tiếng; strategy
  steps from 358 · 473 · 495 to 248 · 187 · 314 tiếng.
- Shorts printed at 519–539 tiếng without the coach asking; FILM TODAY's on-screen says the buyer's problem.
- The Chrome option tells the truth (a box she pastes, 15 minutes), and the channel question is answered instead of skipped.
- Still open: 0 coach-side buyer lines, channels by kind unread, the 24-minute target (+3.3) and 18 Day-0 turns, both from the
  research detour.
