Result: FAIL (valid run; 8 of the 10 v13 defects fixed or mostly fixed, 2 partly; new real failures are mostly machine slips plus 3 kit gaps)

# Retest v13.1: VN copywriter-thin, Day 0 + second chat, S1 + web, level-ups shipped

Reviewer: the simulator of this run, reviewing afterwards against the standards. I did not write the kit. Same trigger and rubrics
as retest-v13 (`qa/standards/calendar.md`, `strategy-doc.md`, `banks.md`, `copy-frameworks.md`, `channel-teardown.md`, `hub.md`,
`hook-lab.md`, `research-brief.md`, `vn-naturalness.md`), plus the v13 review's ten defects as the checklist.

## Method (same as retest-v13)
- Packet: `python3 evals/run.py --root <scratch git-archive of HEAD 49882c5> packet --suite day0 --edition vn --lane S1 --persona
  copywriter-thin --web --tag v131 --today 2026-10-09 --out <scratch>`, folder copied to `evals/runs/v131-copywriter-thin/`. The
  kit was built in a clean copy of HEAD so the repo's `dist/` was not written; that build is byte-identical to the repo's
  `dist/vn` (`diff -rq` clean). build_sha cbab3f5447fd, all 9 level-ups in `packet/kit/Level-ups/`. HEAD did not move during the run.
- Two roles kept apart. MACHINE read only `packet/kit/`: the block, then the §CM- sections it names (method §CM-OPTIONS, MEMORY,
  SETUP, DIG, CARD, TODAY, WEEK, FORMATS, POSTS, MESSAGES, MAP, DRIFT, CTA-KIT, RESEARCH-LITE, EDGE, VOICE, HUMANIZE, NATURAL,
  GUARDRAILS, LOCALE; PLAYBOOK engine/tiers/lines/calendar/doc; RESEARCH §CM-RESEARCH/LISTEN/CHANNELS/AUDIENCE/NICHE; COPY §CM-COPY;
  BANKS §CM-BANKS; BOARD §CM-HUB-NOTION/HUB-MD; HOOKS §CM-HOOK-SHORT). COACH answered only from `persona.toml`, `answers.md`,
  `written-posts.md`: English dictation for the dump and answers, "banj", "skip", "A", her pushback lines verbatim.
- **Pace rules checked before writing coach times** (`evals/run.py` check_pace: a dictated chunk ≥ words/160 active min; a pasted
  post ≥ 0.5 min each; COACH.md: 130 wpm dictation, 30–40 wpm typing, 200 wpm reading, machine reply = coach + ~0.3). The paste
  turn (2 posts) took 1.5 active min (needs ≥ 1.0); chunks 1–4 took 1.5 / 1.3 / 1.2 / 0.8 min (need 0.74 / 0.89 / 0.83 / 0.48).
  **Protocol: valid** (turns, pace, edits pass; leaks warn only; research_leaks pass on 22 queries).
- Research: real WebSearch/WebFetch, read-only, 22 queries logged with the turn they ran after (3, 5, 9, 11), 12 pages opened, 11
  read, 8 hosts. Afterwards I re-fetched the 6 kept Voz/VnExpress lines: 6 of 6 verbatim on the page, all in reader comments.
- Flow played: xưng hô → dump (chunk 1, the 2 pasted posts, chunks 2–4) → 6 interview questions, one ask each → strategy in 3
  steps (each one A/B/C: channel, how to read closed places, hours) → "Show me the research" → "B … ok" → ONE reply: FILM TODAY +
  caption + gift + inbox replies + Week 1 table + N1–N5 + ask-3 Zalo + Chrome box + files + Brand Card + save lines → testimonial
  trap → **new chat** two days later, "tiếp" → reminders A → calendar links. Modelled with no app cut (v13 modelled one), so no
  "tiep" turn.
- Artefacts: `transcript.jsonl` (graded, frozen as `transcript.raw.jsonl`), `transcript.md`, `notes.md` (Research log),
  `CHIEN-LUOC-NOI-DUNG.md`, `NICHE.md`, `HUB.md`, `grades.json`.

## Turns and time
| | Coach turns | Active min | Budget |
|---|---|---|---|
| Strategy step 1 (after 7 setup/dump + 6 interview) | 13 | 15.2 | VN 7 + 6 turns, ≤25 min ✓ |
| Strategy step 3 (the OK step) | 15 | 21.1 | ✓ (grader strategy_minutes 21.1) |
| FILM TODAY ready (one reply with Week 1 and the card) | 17 | 30.3 | ≤35 acceptance ✓ · ≤24 brief ✗ |
| Day 0 end (testimonial trap answered) | 18 | 40.1 | ≤45 min ✓ · ≤17 turns ✗ (18; the grader's 11 + 6 + 2 step-OKs = 19 ✓) |
| Second chat (new chat, Sun 11/10) | 2 | ~1.5 | — |
| Total | 20 | 41.7 (grader) | |
Words the coach reads: strategy steps ≈358 · 473 · 495 tiếng (grader: 476 of talk, over strategy_max_words_vn 450); the research
view 1,082; after the OK, **one line (≈25 tiếng) before FILM TODAY** (v13: 1,351 tiếng of calendar). Where the 6 minutes over the
24-minute film-ready target went: three strategy readings (≈7 min) and the "Show me the research" detour (≈5.6 min).

## Grader results (`python3 evals/run.py grade evals/runs/v131-copywriter-thin`)
`FAIL I6, I8, I9, I11, I15, I23, deny_list, quit_triggers, day0_timing, day0_strategy, day0_shape, strategy_doc, research_log ·
edited: 0`. **Valid run.** PASS: lengths (shorts 530 · 520 · 500 · 510 spoken tiếng, long post 940), vn_natural (particles 16% in
pieces vs her 20%, min 10%), hook_lab, vn_messages, running_tag, research_leaks; I3 and I5 now pass (v13 failed both).

| Check | Real / FP | Note |
|---|---|---|
| I6 | **FP** | counts the word "chọn" in "chỗ bạn chọn là kênh mình đọc giúp" as a second decision next to the one A/B/C line |
| I8 | **FP** | "11/2024 → 8/2026" date ranges in the research view; "10 mục", "60 câu" are the kit's own Chrome-box template numbers |
| I9 | real (machine + kit) | "làm sao viết bài", "viết sao" in quotes are my Vietnamese renderings of her English (§CM-NATURAL 1 says no quotes; block step 3 and §CM-SETUP 2 say quotes) |
| I11 | **FP** | "hàng đầu" inside "khách hàng đầu tiên" (a quoted title and a query) |
| I15 | 1 real, rest FP | real: "Có tin chị đồng ý…", "Chị trả lời rồi…" use bare "chị" for the finance coach while the coach is "bạn" (reads as addressing her); FP: "chị ấy", and the em–chị Zalo draft in its copy box |
| I23 | real (machine) | 0 of 10 pieces of 60+ tiếng use one of her phrases or openers ("Khách không đến từ bài đăng.", "Chị ơi, em là Nhi nè."); §CM-VOICE 7 wants half |
| deny_list | real (machine) | bare "trụ cột" 3× ("4 trụ cột" at turns 14 and 19, "trên trụ cột" in the research view) |
| quit "300 words before usable" | real (kit + machine) | strategy step 2: 431 words of talk, no copy box (the 9-line content-line table is talk) |
| day0_timing | **FP** | "Map after 14 coach turns (max 7 + 6)": the grader reads the map at the last step and does not add the 2 step OKs that strategy_max_steps = 3 allows; film-ready and session limits pass |
| day0_strategy | mostly FP | FP: FILM TODAY "after 'B. Three hours… ok', not an OK" (it ends "ok"); "2 open choices" (same "chọn" as I6); 8 pillars (it parsed my reason text and the "chia theo nỗi lo" alternative as pillars); WHAT I FOUND "6 lines, 2 unsourced" (it splits the kit's own 3-line template on " · "). Real (machine): I wrote "(máy khuyên: …)" with the reason inside the brackets, the kit's form is "(máy khuyên): …", so 3 A/B/C lines read as unmarked. Also FP not failed: mix read as 50/35/15 from "muốn … thì gõ 50/35/15" |
| day0_shape | 2 real, 2 FP | real: YOUR WORD "VIẾT SAO" is my rendering of "they ask me how, how do I write the post" and carries no "(mình đoán)"; N4 has VIẾT SAO only in the ask (§CM-WEEK 4). FP: "{tên bạn}" is the gift's fill-in for the coach's reader; "[CHƯA CÓ]" on the card is the kit's own marker |
| research_log, strategy_doc | real (machine) | KEEP line 4 ("Bất cứ ai, với số tiền đủ nhiều, đều có thể trở thành người đi khai vấn về cuộc sống") is about money buying the title, not "only theory"; lines 1, 2, 3, 5 still give 2 hosts |
| leaks | warn only | 8 warnings, all Vietnamese renderings of what she dictated ("chỉ kéo thêm người tới thứ chưa ai cần" = "pull more people to something nobody want") or kit phrases |

Real failures: 9 (I9, I15 partly, I23, deny_list, quit_triggers, the "(máy khuyên)" form, keyword tag, N4 keyword, KEEP line 4).
False: I6, I8, I11, day0_timing, most of day0_strategy and 2 of day0_shape.

## Verdict per area
| Area | Verdict | Evidence |
|---|---|---|
| A/B/C at each step, one recommended | **PASS** (form slip) | Steps 1–3 each carry exactly one A/B/C with one recommended and a reason ("A) … (máy khuyên: đúng người bạn bán cho, mình đã đọc 3 bài)"); the rest prefilled; reminders A/B in the second chat. No "Bạn có muốn…không?" anywhere. Slip: reason inside the brackets |
| Strictly sequential | **PASS** | dump → interview → step 1/3 → 2/3 → 3/3 → OK → pieces; no piece before the OK; the research request answered, then step 3 put back ("Bước 3/3 vẫn đang chờ bạn: số giờ…") |
| ≤1 question per reply | **PASS** | every reply ≤1 "?"; no coach pushback; dig.find, dig.channels and dig.goal now one ask each |
| Research done, sources, buyer lines | **WEAK** | 22 queries, 12 pages, links in "xem nghiên cứu", 6/6 re-fetched lines verbatim. Still 0 lines from Nhi's buyer (a coach) in 2 places; the KEEP is again the coaches' audience distrusting coaches; Facebook groups and TikTok unread |
| Liked + competitor channels | **WEAK → better** | Now offered as A/B/C (step 1) and read before the strategy: 2 Substack channels, 24 titles, 3 posts, 0 comments readable; AI CŨNG NÓI / CHƯA AI NÓI / BẠN NÓI ĐƯỢC in the file. No views or comments to rank |
| Niche (NICHE.md) | **WEAK** | 4,488 B, 9 sources; prices, seasons and myths still "(mình đoán)" |
| Broad pillars | **PASS** | "Nghe khách nói · Vì sao người ta mua · Viết để bán · Gói và cách bán", each with a reason line, an alternative split offered |
| Content lines per pillar | **PASS** (kit conflict) | 9 named lines, each pillar has THU HÚT + NIỀM TIN, one CHUYỂN ĐỔI line; but 9 > §CM-CONTENT-LINES 1's "6–8 at 3 hours" (defect R1 below) |
| Mix | **PASS** | 40/40/20 prefilled with her goal as the reason; month totals THU HÚT 8 · NIỀM TIN 8 · CHUYỂN ĐỔI 4 |
| 4-week calendar | **PASS** | Week 1 table only in chat, after FILM TODAY; weeks 2–4 in the strategy file part 6, with headers, totals and hours |
| One framework + one bank item per piece | **PASS** (silent) | FILM TODAY flip-a-belief, N1 one-scene-one-lesson with research line 4, N2 debunk-the-advice from her dump, N3 open-loop long post with the August result, N4 objection with her "who I do not take", N5 short letter |
| Word lengths | **PASS** | 530/520/500/510 spoken tiếng, 940 long, email 206; first drafts were 300–430 and needed 1–2 more beats each (defect 5 still partly open) |
| Hooks strong | **PASS (grader) / WEAK (me)** | hook_lab PASS; N1, N4, N3 hooks are concrete; FILM TODAY's on-screen "Thiếu lý do, không thiếu bài" is still a flat contrast |
| Vietnamese only, natural | **WEAK** | no English in pieces ("marketing" cut before sending), particles 16%; but 0 of her phrases in pieces (I23) and 3 bare "trụ cột" in talk |
| Guardrails | **PASS** | testimonial refused with a consent Zalo ("Câu … mình chưa đưa vào bài: chị ấy chưa nói cho dùng công khai."); August result carries "Kết quả của một coach thôi, tuỳ người, không phải cam kết"; no invented number |
| Strategy doc (SD1–SD12) | **PASS-** | 9 parts in order, all 4 tables in part 6, lines, mix, system, gift, ladder, research basis; "Vì sao là bạn" left as [CẦN BẠN] |
| Hub + HUB.md | **PASS** | no hub A/B/C on Day 0 (no Notion), HUB.md 7 parts, 2,663 B, one "Lưu:" line |
| Memory resume (new chat "tiếp") | **PASS** | "Brand Card v1 ✓ / Mình nhớ: chiến lược đã OK hôm 9/10 … · đang dở bước: cài lời nhắc trên lịch." then reminders A/B; §CM-CARD 6 now agrees with the block |

## v13 → v13.1, defect by defect
| # | v13 defect | v13.1 | Quote (turn) | Notes |
|---|---|---|---|---|
| 1 | Strategy: 3 steps or 8? | **fixed** | "◆ Content Machine · Bước 1/3 · Điều khách nhớ, trụ cột nội dung" (13) · "Bước 2/3 · Tuyến bài, tỷ lệ" (14) · "Bước 3/3 · Hệ thống, quà, lời mời, từ khoá" (15) | engine 1 now maps 8 steps to 3 messages; step 6 is "chỉ chọn kiểu", step 8 prefilled; each message one A/B/C |
| 2 | Calendar buries FILM TODAY | **fixed** (placement) · **partly** (time) | after the OK: "Đã chốt: khoảng 3 tiếng…" then "QUAY HÔM NAY · video ngắn · THU HÚT · 530 chữ" (17) | ≈25 tiếng before FILM TODAY (v13 1,351); film-ready 30.3 min (v13 31.6), still over the 24-min target |
| 3 | Interview asks stack | **fixed** | "Giờ khách mới tìm tới bạn từ đâu?" (10) · "Trong nghề có 2–3 kênh nào bạn hay xem…?" (11) · "Trong 90 ngày tới, đăng bài phải mang lại cho bạn điều gì?" (12) | no "one at a time" pushback; dig.offer and dig.buyer still pack 2–3 asks in one sentence (no pushback, one "?") |
| 4 | Research can't reach the buyer, nothing asks | **partly** | "KÊNH MÌNH ĐỌC GIÚP BẠN … A) … (máy khuyên…)" (13) · "Mình chưa đọc được nhóm Facebook của coach … A) bạn có Claude in Chrome…: mình đọc luôn" (14) | both choices now asked once; but 0 coach-side buyer lines again, and "mình đọc luôn" became a box she must paste into Chrome herself (R2 below) |
| 5 | FILM TODAY 500–800 vs "nhớ ý rồi nói" | **partly** | "500–800 chữ, cả QUAY HÔM NAY: kịch bản nói đủ câu" (§CM-FORMATS 3) | the rule is now one rule and lengths PASS; drafts still landed 300–430 and took extra beats; §CM-FORMATS "thẻ ý (mặc định)" vs block "kịch bản đủ câu" still both there; her "give me bullets" never asked |
| 6 | Titles don't name the type | **fixed** | "N1 · thứ Hai 12/10 · video ngắn · THU HÚT · 520 chữ" (17) | grader week_types 2/2/1 |
| 7 | Two hub recommendations | **fixed** | no hub question on Day 0; "Lưu: bấm vào HUB.md … → Add to project." (17) | §CM-TODAY and §CM-HUB-NOTION 4 now agree: no Notion on Day 0 → HUB.md only |
| 8 | New chat: read old chats vs ignore memory | **fixed** | "Card với HUB.md mình lấy từ đoạn chat hôm thứ Sáu; trong file dự án chưa có." (19) | §CM-CARD 6 "Card ở chat cũ: dùng luôn."; no save-nudge string, the line was improvised |
| 9 | Bare "trụ cột", "hook" in hub files | **partly** | kit hub files now "trụ cột nội dung", "Kiểu câu mở"; but "Đã chốt: điều khách nhớ, 4 trụ cột…" (14), "(4 trụ cột, 40/40/20…)" (19) | deny_list still fails 3×, now on the machine side (the method file itself still uses bare "trụ cột" in §CM-OPTIONS 1 and 4) |
| 10 | WHAT I FOUND overflows | **fixed** (kit) | 3 lines: "9 câu … 3 nơi …" · "Nguồn câu khách: …" · "Chưa đọc được: … · gõ "xem nghiên cứu"…" (15) | the grader still counts 6 by splitting on " · " (FP) |

Smaller v13 items: locale "120–200" → "500–800" **fixed**; §CM-WEEK 4 now says the keyword goes in the body "cả bài mời gửi
bạn" **fixed** (I still missed it in N4); hub page-name em dash **fixed** ("Content Machine · {tên}"); 3 câu đáng tiền in quotes vs
§CM-NATURAL 1 **not fixed** (now I9); Claude micro line right after "bấm micro nhỏ trong ô chat" **not fixed**; "Không lộ … tên
file" vs file-naming lines **not fixed**.

## Top remaining defects (file · section · fix)
Budgets: VN block 2 chars left, VN method 243 B left, STRATEGY-VN 16 B left (no change proposed there); PLAYBOOK-VN 5,342 B and
RESEARCH-VN 6,476 B of headroom. Deltas are UTF-8 bytes (block also NFC chars). The block and method packages are byte-neutral.

1. **3 câu đáng tiền quoted from English dictation** (I9; persona quit risk). `core/vn/start-block.md` step 3 ("… vừa nói:" cả 3
   trong ngoặc kép,) vs `modules/vn/humanize.md` §CM-NATURAL 1. **Fix (block −27 B / −22 chars)**: delete " cả 3 trong ngoặc
   kép,"; `modules/vn/setup.md` `setup` 2 "3 câu nguyên văn trong ngoặc kép," → "3 câu nguyên văn trong ngoặc kép (kể tiếng Anh:
   ý Việt, bỏ ngoặc)," (+44 B, method package below).
2. **Her phrases never reach the pieces** (I23 0/10). `core/vn/start-block.md` KIỂM TRA 3 "giọng, nhịp, câu hay nói, cách gọi
   khách của coach" → "giọng, nhịp, câu hay nói (≥ nửa số bài), cách gọi khách" (+10 B / +5 chars; paid by fix 1: **block net
   −17 B / −17 chars**).
3. **Bare "trụ cột" and "hook" in talk** (deny_list 3×; the kit models it). `modules/vn/options.md` §CM-OPTIONS 1 "định vị, trụ
   cột, tuyến bài, tỷ lệ, nền tảng, lịch, quà tặng, lời mời, kiểu chiến dịch, bài nào trước, hub" → "8 bước chiến lược (§CM-MAP),
   kiểu chiến dịch, bài nào trước, hub" (−62 B), and a row in `modules/vn/humanize.md` §CM-NATURAL 7: "trụ cột (trơn), hook →
   trụ cột nội dung, câu mở" (+64 B).
4. **Keyword rendered from English dictation is printed as the client's word** (day0_shape). `modules/vn/signature.md` TỪ KHOÁ
   "Chưa đủ: cụm khách" → "Chưa đủ, hay kể tiếng Anh: cụm khách" (+22 B). **Method package 1+3+4 paid by** `modules/vn/message.md`
   §CM-MAP "Không in: ĐỂ SAU, điểm, tên khung." (−43 B, the block's "Không lộ mẫu, tên khung, điểm" already says it) and
   `strings/vn.toml` `dig.offer` "Khách gật đầu làm với bạn thì họ nhận được gì, làm theo cách nào, trả bao nhiêu?" → "Khách làm
   với bạn thì nhận được gì, trả bao nhiêu?" (−40 B, also drops the third ask): **method net −15 B**.
5. **Option A "mình đọc luôn" is not true in a Claude or ChatGPT Project** (defect 4 residue). `modules/vn/research.md` R0 2
   "A) bạn có Claude in Chrome hay ChatGPT Work: mình đọc luôn" → "… : mình gửi khung dán vào Chrome, 15 phút" (+26 B, RESEARCH
   headroom; Cowork keeps "đọc luôn" via R0 1).
6. **Day-0 "xem nghiên cứu" is 1,082 tiếng and costs ~5.6 min** (film-ready 30.3). `modules/vn/research.md` R3 kết quả 2: after
   "Sau R6: in brief mới nhất." add "Ngày 0: một màn hình (kết luận, câu GIỮ kèm link, nơi chưa đọc), phần còn lại ở NICHE.md."
   (+115 B, RESEARCH headroom).
7. **Strategy step 2 is over a screen** (476 tiếng; quit trigger at 431 words). `modules/vn/strategy-doc.md`
   `strategy-doc.grow-engine` 1 "tin 2 bước 3–4 + cách đọc" → "tin 2 bước 3–4 (tuyến: mỗi cụm một dòng tên · loại, bảng đủ vào
   file) + cách đọc" (+74 B, PLAYBOOK headroom).
8. **Content-line arithmetic cannot hold** (4 pillars × THU HÚT + NIỀM TIN + 1 CHUYỂN ĐỔI = 9 > "6–8 at 3 hours"; a "2 tuần" CHUYỂN
   ĐỔI line vs §CM-CALENDAR 3 "tuần nào cũng một"). `modules/vn/strategy-doc.md` §CM-CONTENT-LINES 1 "Khoảng 3 tiếng một tuần:
   tổng 6–8 tuyến, không phải tuần nào cũng đủ mặt." → "Khoảng 3 tiếng: 6–8 tuyến (4 cụm: 9), không phải tuần nào cũng đủ mặt;
   tuyến CHUYỂN ĐỔI tháng đầu ra mỗi tuần." (+48 B, PLAYBOOK headroom).
9. **"(máy khuyên)" form** (3 A/B/C lines unmarked for the grader). Machine slip against `strings/vn.toml` `options.recommended`
   and §CM-OPTIONS 3 '"(máy khuyên)": {bằng chứng}'. No kit change; the grader could accept "(máy khuyên: …)".
10. **Third-person "chị" while the coach is "bạn"** (I15). Machine slip against §CM-NATURAL 2 "Một chữ gọi một người suốt bài";
    write "chị ấy" every time. No kit change.

## Grader gaps to hand the integrator
- `day0_timing`: the map-turn budget does not add the step OKs that `strategy_max_steps = 3` allows (14 seen vs 7 + 6; should be
  7 + 6 + 2).
- `day0_strategy`: an OK at the end of a longer line ("B. Three hours… ok") is not read as the OK; "chọn" in talk counts as a
  second open choice (also I6); pillars are parsed from the reason text after ":" and from an alternative-split line; WHAT I FOUND
  is split on " · ", which the kit's own 3-line template uses; the mix is read from "gõ 50/35/15" (the alternative), not the line.
- I8 reads date ranges ("11/2024 → 8/2026") and the kit's own template numbers in a copy box as claims; I11 matches "hàng đầu"
  inside "khách hàng đầu tiên"; I15 counts "chị ấy" and an em–chị message inside a copy box; day0_shape flags a gift's
  "{tên bạn}" fill-in and the card's "[CHƯA CÓ]".

## What improved against retest-v13
- Valid run (v13 went invalid on pace); I3 and I5 pass; Day 0 down from 52.9 to 40.1 active minutes and 20 to 18 coach turns.
- One ask per interview message, no pushback; the channel and the reading-method choices are asked once, as A/B/C.
- FILM TODAY is the first thing after the OK; only week 1's table is in chat; all 4 weeks live in the strategy file.
- Piece titles carry the type; no conflicting hub recommendation; the new chat resumes from the old one without a kit conflict.
