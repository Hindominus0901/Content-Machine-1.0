Result: FAIL (run graded invalid on one coach-side timing slip; the kit findings below stand)

# Retest v13 ("content department in a box"): VN copywriter-thin, Day 0 + second chat, S1 + web, level-ups shipped

Reviewer: the simulator of this run, reviewing afterwards against the standards. I did not write the kit. Trigger: the founder's
request of 9 Oct (CONTEXT.md: choices at every open step with one recommended, strictly in sequence, real research on liked and
competitor channels and the niche, copy frameworks, hub, memory). Rubrics: `qa/standards/calendar.md`, `strategy-doc.md`,
`banks.md`, `copy-frameworks.md`, `channel-teardown.md`, `hub.md`, `hook-lab.md`, `research-brief.md`, `vn-naturalness.md`.

## Method (same as retest-ft2, plus the v13 path)
- Packet: `python3 evals/run.py packet --suite day0 --edition vn --lane S1 --persona copywriter-thin --web --tag v13 --today
  2026-10-09`, folder renamed to `evals/runs/v13-copywriter-thin/`. Kit = `dist/vn` built from e7fb2b6, byte-identical to a fresh
  scratch build (`diff -rq` clean), with all 9 level-ups in `packet/kit/Level-ups/`.
- **HEAD moved during the run**: a3a7e7c ("VN polish of the v13 parts") landed after the packet was made. It rewords
  `dig.find`, the hub A/B/C label and a few terms; none of the defects below is fixed by it (checked by diff). Fix text below is
  written against a3a7e7c.
- Two roles kept apart. MACHINE read only `packet/kit/` (the block, then the §CM- sections it names: method file §CM-OPTIONS,
  MEMORY, SETUP, DIG, MAP, WEEK, FORMATS, POSTS, MESSAGES, CTA-KIT, RESEARCH-LITE, EDGE, VOICE, HUMANIZE, NATURAL, GUARDRAILS,
  LOCALE; PLAYBOOK engine/tiers/lines/calendar/doc; RESEARCH §CM-RESEARCH/LISTEN/CHANNELS/AUDIENCE/NICHE; COPY §CM-COPY + 6
  framework parts; BANKS §CM-BANKS/CTA-BANK; BOARD §CM-HUB-NOTION/HUB-MD; STRATEGY §CM-STRATEGY/SEASON/HOOKS; HOOKS library +
  short). COACH answered only from `persona.toml`, `answers.md`, `written-posts.md`: English dictation for the dump and answers,
  "banj", "A", "ok A", "tiep", her pushback lines verbatim.
- Research: real WebSearch/WebFetch, read-only, 15 queries logged with the turn they ran after (3, 4, 9), 15 pages opened, 13 read,
  7 hosts. I re-fetched 5 kept lines afterwards (Voz ×3, VnExpress ×2): all 5 verbatim on the page.
- Flow played: xưng hô → dump (4 chunks + 2 pasted posts) → 6 interview questions → strategy 3 steps with A/B/C → "Show me the
  research" → OK → calendar + FILM TODAY + gift + DM replies → "tiep" → Week 1 (N1–N5, ask-3 Zalo, paste steps) → testimonial trap
  → Brand Card + hub A/B/C → HUB.md → **new chat** two days later, "tiếp" → reminders A → calendar links.
- Artefacts: `transcript.jsonl` (graded), `transcript.md` (readable), `notes.md` (Research log), `CHIEN-LUOC-NOI-DUNG.md`,
  `NICHE.md`, `HUB.md`, `grades.json`.

## Turns and time
| | Coach turns | Active min | Budget (VN) |
|---|---|---|---|
| To strategy step 1 | 13 (7 setup/dump + 6 interview) | 20.2 | 7 + 6, ≤25 min ✓ |
| Strategy OK (after 3 steps + research view) | 17 | 31.2 | — |
| FILM TODAY ready | 17 | 31.6 | ≤35 ✓ |
| Week 1 printed | 18 | 38.4 | — |
| Day 0 end (HUB.md) | 20 | 52.9 | ≤45 min, ≤11 + 6 turns ✗ |
| Second chat (new chat, Sun 11/10) | 2 | ~1.5 | — |
| Total | 22 | 56.7 (grader) | |
Words the coach reads: strategy steps 281 · 394 · 289 tiếng; the post-OK reply 2,298 tiếng (1,351 of talk, mostly the 4 calendar
tables, before FILM TODAY); Week 1 reply 3,281 tiếng.

## Grader results (`python3 evals/run.py grade evals/runs/v13-copywriter-thin`)
`FAIL I3, I5, I6, I8, I9, I11, I23, deny_list, quit_triggers, day0_timing, day0_strategy, day0_shape, vn_natural, hook_lab,
strategy_doc, research_log, invalid run: pace · edited: 0`. research_leaks PASS (15 queries); leaks WARN only.

**invalid: pace** is mine (coach side): turn 5 pastes 2 posts in 0.7 min, the protocol wants ≥1.0. The protocol forbids fixing a
coach time after the first grade, so it stays. Nothing else in the protocol failed.

| Check | Real / FP | Note |
|---|---|---|
| I3 | real (machine) | the "Cần bạn" line under N2 is 24 words (max 20) |
| I5, quit "2 questions" | **FP** | the "?" inside two Google Calendar URLs (turn 22) |
| I6 | **FP / stale** | counts "OK hay sửa" + the word "quyết định" in a calendar cell; and "≤1 decision a session" now contradicts v13's A/B/C at every step |
| I8 | **FP** | page counts, years, URL ids, word counts and the 40/40/20 mix read as claims; no result number was invented |
| I9 | 1 real, 1 FP | real: a paraphrase in quotes in the research box ("đăng mà không ai hỏi"); FP: a series name in quotes |
| I11 | FP | "duy nhất" in ordinary use ("Cái đổi duy nhất là chữ trên trang") |
| I23 | 1 real, 3 FP | real: 2 of 9 pieces carry her phrases (22%); FP: "viral", "lùa gà" are search words in the research box; "Hook" is kit wording in HUB.md (defect 9) |
| deny_list | real (machine + kit) | bare "trụ cột" 5× (machine: "cùng 4 trụ cột", calendar column; kit: HUB.md spec) |
| quit "300 words before usable" | **real** | 1,351 tiếng of calendar before FILM TODAY (defect 2) |
| day0_timing | mixed | real: 56.7 min, 21 turns; FP: "Map has 2 labelled lines / 1 step": the grader needs 3+ labels per step and cannot see §CM-MAP's own 2+3+2 split |
| day0_strategy | mixed | real: WHAT I FOUND ran to 5 lines (defect 10); FP-ish: "Week 1 has no ATTRACT/TRUST/CONVERT" because titles carry no type (defect 6, real machine/kit gap) |
| day0_shape | real | N3 (share ask) has no keyword (§CM-WEEK 4 vs the calendar's ATTRACT ask) |
| vn_natural | real | sentence-final particles 8% in pieces vs 20% in her posts (min 10%) |
| hook_lab | 1 real, 1 FP | real: on-screen "Tim nhiều chưa phải là tin" is a flat claim; FP: three subject lines printed on one line read as one 83-char subject |
| strategy_doc | mixed | real: flat hooks ("Không cần chiến dịch đâu"), bare "trụ cột", KEEP stretched; FP: "part 5 in seconds" (it says "không tính giây"), "mix not given" (it is: THU HÚT 40 · NIỀM TIN 40 · CHUYỂN ĐỔI 20) |
| research_log | real | KEEP lines 1 and 4 don't say the pattern in their own words; 2 lines left |
| lengths, vn_messages, running_tag | PASS | shorts 540 · 500 · 508 · 501 spoken tiếng, long post 942, email 230 |

## Verdict per area

| Area | Verdict | Evidence |
|---|---|---|
| A/B/C at each step, one recommended, no vague ending | **WEAK** | Every strategy step, gift, hub and reminder ends on A/B/C + "(máy khuyên)" with a reason ("A) THU HÚT 40 · NIỀM TIN 40 · CHUYỂN ĐỔI 20 (máy khuyên): … người lạ nghi coach nói suông (4 người, 2 nơi)"). No "Bạn có muốn…không?" anywhere. But the calendar had no A/B/C (one line: "muốn 2 tuần đầu nhẹ hơn thì gõ 'nhẹ hơn'"), the channel choice had none, and the CTA ladder was never a choice |
| Strictly sequential | **WEAK** | Order held: dump → interview → strategy → OK → pieces; no piece before the OK. But the block's "≤3 bước" made step 2 carry three decisions (lines, mix, system) in one message; the engine's 8 single steps never ran (defect 1) |
| ≤1 question per reply | **PASS** | All 22 replies ≤1 "?" in talk (turn 22's two are URLs). Yet interview Q4 stacked 3 asks in one sentence and the coach fired "Two questions in one message. One at a time please." (defect 3) |
| Research really done, sources listed, buyer lines verbatim with place/date | **WEAK** | 15 queries, 13 pages, 7 hosts, links in "xem nghiên cứu"; 5 re-fetched lines verbatim. But no line from Nhi's actual buyer (a coach) in 2+ places: the one KEEP is the coaches' audience distrusting coaches ("…Có kiếm thức thực tế không hay toàn lý thuyết ?" Voz 2021–23; "Cứ qua một khóa học là thành life coach. Dễ vậy sao?" VnExpress 7/2024), and two of its 4 lines are a stretch. Facebook groups, TikTok and YouTube comments were unreadable; the keyword stays "(mình đoán)" |
| Liked + competitor channels | **WEAK** | The coach skipped the ask; the machine picked 3 Substack newsletters selling content help to independent experts, read 12 posts each (titles, dates, CTAs, gifts) and built AI CŨNG NÓI / CHƯA AI NÓI / BẠN NÓI ĐƯỢC. No A/B/C of candidates (CT1), no views, 0 comments readable (CT2, CT4), no paste steps for the channels |
| Niche (NICHE.md) | **WEAK** | Saved, 3,416 chars, sources listed; half the blocks are "(mình đoán)" (prices, seasons, myths) |
| Broad pillars | **PASS** | "Nghe khách nói · Tâm lý người mua · Viết để bán · Gói và cách bán", 3–4 tiếng each, a year of posts each, with an alternative split offered |
| Content lines per pillar | **WEAK** | 2 named lines per pillar, each with format, words, cadence, type ("Câu khách nói tuần này", "Một ca, kể lại"…). "Gói và cách bán" has no ATTRACT line (CL2/SD11) |
| ATTRACT / TRUST / CONVERT mix | **PASS** | A/B/C with the default recommended and a research reason; calendar totals "THU HÚT 8 · NIỀM TIN 8 · CHUYỂN ĐỔI 4 = 40/40/20 ✓"; no direct ask in week 1 |
| 4-week calendar complete | **PASS** (content) / **FAIL** (placement) | 4 tables × 5 rows × 11 columns, week headers with trust step and belief, totals and hours. But it is printed as 1,351 tiếng of talk before FILM TODAY (quit trigger) and its own step-6 choice is skipped |
| One framework + one bank item per piece | **PASS** (silent) | FILM TODAY five-line story · N1 slippery slope · N2 open-loop long post · N3 belief shift · N4 objection answer · N5 one-lesson story; each from one bank item (client quote, café story, "9 coach, 2 người gần nhất tới qua giới thiệu", the consented August result). Not recorded anywhere the coach or hub can see (`hub:Uses` empty in HUB.md) |
| Word lengths | **PASS** | Shorts 540/500/508/501 spoken tiếng, long post 942, email 230, never seconds. But first drafts landed at 300–400 and needed a 4th/5th beat to reach 500 (defect 5) |
| Hooks strong | **WEAK** | 3 of 6 pass HL1–HL9: N1 ("Em bán được cho người quen thôi, người lạ coi xong là lướt." over "Một bài, hai kiểu người đọc"), N2, N4 ("180 người, một email" over "Coach hỏi mình hoài: làm sao có thêm người theo dõi?"). Flat: FILM TODAY's on-screen "Tim nhiều chưa phải là tin", N3's first line "Khách không đến từ bài đăng.", N5 subject "Không cần chiến dịch đâu" |
| Vietnamese only, natural | **WEAK** | Pieces are Vietnamese, mình–bạn in posts, em–chị in DMs as her W2; 1 translationese hit in 5,225 tiếng. But particles 8% vs her 20%, her phrases in 2 of 9 pieces, "content", "Reels", and "Hook:" in HUB.md |
| Guardrails | **PASS** | Testimonial trap: "Câu "Em là người đầu tiên hỏi chị khách nói gì" mình chưa đưa vào bài: chị ấy chưa nói cho dùng công khai." + a consent Zalo; the August result carries "Kết quả tuỳ người, không phải cam kết"; no invented number |
| Strategy doc (SD1–SD12) | **WEAK** | 9 parts in order, lines, mix, system, gift and ladder present; part 6 points to the chat instead of holding the 4 tables; bare "trụ cột"; two flat hooks |
| Hub + HUB.md | **WEAK** | HUB.md has the 7 parts, 2,856 chars, one "Lưu:" line. The hub A/B/C recommended C against HQ1's "A (Notion, recommended)" because the kit's two hub texts disagree (defect 7) |
| Memory resume (new chat "tiếp") | **PASS** (with a kit conflict) | "◆ … Brand Card v1 ✓ / Mình nhớ: chiến lược đã OK hôm 9/10 (4 trụ cột, 40/40/20, từ khoá HỎI GIÁ) · … · đang dở bước: cài lời nhắc trên lịch." then the waiting A/B. Card and HUB.md were never saved to the project, so this only worked by reading the old chat, which §CM-CARD 6 says to ignore (defect 8) |

## Top 10 kit / module defects (file · section · fix)
Budgets: VN method 71 B left, VN block 1 char, STRATEGY-VN 16 B. Deltas are UTF-8 bytes of the replaced span.

1. **Day-0 strategy: 3 steps or 8?** `core/vn/start-block.md` step 5 "CHIẾN LƯỢC ≤3 bước", `modules/vn/message.md` §CM-MAP "Ngày 0:
   ≤3 bước", vs `modules/vn/strategy-doc.md` `strategy-doc.grow-engine` 1–2 ("thay cho bản chiến lược gói trong một tin", "Mỗi tin
   một bước", 8 steps) and `qa/standards/calendar.md` CL3 ("One step a reply, in order 1→8"); acceptance `strategy_max_steps = 3`.
   The run followed the block: steps 3/4/5 in one message, 6 after the OK without A/B/C, 8 never offered. **Fix** (PLAYBOOK, −20 B):
   in grow-engine 1 replace "thay cho bản chiến lược gói trong một tin (§CM-MAP: các dòng của nó thành lựa chọn của mình ở bước 1,
   2, 4, 5, 8)" with "gộp 3 tin như §CM-MAP: bước 1–2 · 3–5 · 7–8 kèm nghiên cứu, mỗi tin A/B/C riêng; bước 6 ra sau OK"; CL3 gets
   the same Day-0 grouping; graders `day0_strategy` must accept a step with 2 labels (it saw 1 step here).
2. **The calendar buries FILM TODAY.** `modules/vn/setup.md` `setup.kit-order` 9 and start-block step 6 put "lịch 4 tuần
   (§CM-CALENDAR), QUAY HÔM NAY, Tuần 1" in that order: 1,351 tiếng of tables before anything to film (quit trigger), Day 0 ran 52.9
   min. **Fix** (byte-neutral, block and method): reorder to "QUAY HÔM NAY, Tuần 1 (§CM-WEEK), lịch 4 tuần (§CM-CALENDAR)", and in
   `strategy-doc.grow-calendar-table` 4 print only week 1's table on Day 0, weeks 2–4 to the strategy file part 6 and HUB.md.
3. **Interview asks stack.** `strings/vn.toml` `dig.find` (a3a7e7c: "…bạn đang đăng ở đâu? Kể luôn 2–3 kênh bạn thích, 2–3 kênh đối
   thủ nhé.") and `dig.goal` ("…làm được gì cho bạn, mỗi tuần dành cho nó được mấy tiếng?"). The coach answered the first part and
   wrote "Two questions in one message. One at a time please." **Fix** (−115 B, both strings render in the method file): `dig.find` →
   "Khách mới giờ tìm tới bạn bằng cách nào, và bạn đang đăng ở đâu?"; `dig.goal` → "90 ngày tới bạn muốn content làm được gì cho
   bạn?"; hours go to the system step as A/B/C ("A) 3 tiếng tối Chủ nhật (bạn nói)…"); channels move to defect 4's card.
4. **Day-0 research can't reach the buyer, and nothing asks.** `modules/vn/research.md` `research.grow-access` R0 "(ngày 0 không hỏi
   …)" and `channel-research.grow-channels` C1 ("Chưa có, hay thiếu: tự tìm rồi đề xuất … A/B/C"), with no slot on Day 0 for either
   choice. Result: 0 coach-side buyer lines, a KEEP from the coaches' audience, keyword "(mình đoán)", channels picked silently.
   **Fix** (RESEARCH, about +60 B, cut the duplicate "Không chờ: đọc ngay…" line to pay): strategy step 1 card carries one line
   "Kênh mình đọc thay bạn: A) {kênh} (máy khuyên: cùng tệp khách, đăng trong 90 ngày) B) {kênh} C) bạn gõ tên" and step 3 carries
   "Chưa đọc được {nơi}: A) bạn có Claude in Chrome: mình đọc luôn (máy khuyên) B) bạn dán 20 comment C) để Tuần 1" (founder: ask
   ONCE).
5. **FILM TODAY "nhớ ý rồi nói, 3 ý" vs 500–800 spoken words.** `modules/vn/fmt-short.md` `fmt-short.kit-video-short` 2–3, 7 and
   start-block step 6. Drafts landed at 300–400 and reached 500 only with a 4th/5th beat; the persona wants bullets ("give me
   bullets"). **Founder decision needed**; proposed (method, about +40 B, pay with defect 6's −11 and defect 3's −115): item 3 "500–800
   chữ, QUAY HÔM NAY cũng vậy: mỗi ý 3–5 câu nói, trên mỗi ý một dòng gạch đầu để nhớ".
6. **Piece titles don't name the type.** `fmt-short.kit-video-short` 5 'In: "N1 · {day} · {loại} · {n} chữ"': "loại" was read as
   the format; Week 1 shows THU HÚT / NIỀM TIN / CHUYỂN ĐỔI only in the calendar, so the grader counted 0/0/0. **Fix** (method,
   −11 B): '"N1 · {day} · {dạng} · THU HÚT|NIỀM TIN|CHUYỂN ĐỔI · {n} chữ"', dropping the duplicate '(ngày 0: "QUAY HÔM NAY · nhớ ý
   rồi nói")' that start-block step 6 already says.
7. **Two hub recommendations.** `strings/vn.toml` `levelup.offer_board` ("C) chỉ file HUB.md ở đây. Mình chọn {letter}") vs
   `modules/vn/hub.md` `hub.grow-notion-build` 4 (A "máy khuyên", C "Để sau") vs `qa/standards/hub.md` HQ1 (A recommended). The run
   recommended C (no Notion connected, 3 hours a week) and fails HQ1 as written. **Fix** (method, +23 B): "C) để sau, chỉ HUB.md.
   Notion đã kết nối: chọn A, không thì C: {why}." and HQ1 to match.
8. **New chat: "read old chats" vs "ignore account memory".** `modules/vn/brain.md` `brain.kit-fix` 6 ("Bỏ qua trí nhớ tài khoản.
   Không có card … dán card") vs `modules/vn/options.md` `options.kit-memory` 1 and the block ("tự xem chat cũ, bộ nhớ, HUB.md").
   The coach never clicked "Add to project"; the resume worked only because the machine followed the block over §CM-CARD 6.
   **Fix** (method, −2 B): "Bỏ qua trí nhớ tài khoản." (33 B) → "Card ở chat cũ: dùng luôn." (31 B); the save nudge already
   exists as `card.save_line`, printed once when the card was found only in a chat.
9. **Bare "trụ cột", English "hook" in coach-facing hub files.** `modules/vn/hub.md` `hub.grow-hubmd` 2 ("các trụ cột", "3 hook",
   column "Tầng") and `hub.grow-notion` 1 (properties "Trụ cột", "Kiểu hook", "Tầng"). Copied into HUB.md they hit the deny-list
   and I23 ("Hook:"); the machine also shortened the calendar column to "Trụ cột". **Fix** (BOARD, +6 B per site): "trụ cột nội
   dung", "câu mở", "Loại"; the calendar column list in `strategy-doc.grow-calendar-table` already says "Trụ cột nội dung": add
   "(viết đủ)".
10. **WHAT I FOUND overflows.** `modules/vn/research.md` `research.grow-paste` R3 kết quả 1 template is already 4 lines (incl. "Chưa
    đọc được…" and "Gõ "xem nghiên cứu"…"), and `channel-research.grow-card` C4 folds the channel lines in too: 5 lines, two with no
    source. **Fix** (RESEARCH, −37 B): merge the last two template lines into 'Chưa đọc được: {nơi} (bạn dán thì mình đọc) · gõ "xem
    nghiên cứu" để xem từng câu."' and let the channel line replace "Nguồn câu khách" when there is no client line.

Also found (smaller):
- `modules/vn/locale.md` `locale.kit-language` 2 and `modules/en/locale.md` 2 still say "video ngắn 120–200" / "short video
  120–200": stale since 7 Oct night. Byte-neutral fix: "120–200" → "500–800" (22 B both).
- `modules/vn/plan.md` `plan.kit-week` 4 ("Từ khoá 1 lần trong bài + lời mời") vs the calendar's ATTRACT ask "gửi cho một người
  bạn": N3 ended up with no keyword (day0_shape). Say "trong thân mọi bài, kể cả bài mời gửi bạn".
- The block's "Không lộ … tên file" vs §CM-STRATEGY-DOC/§CM-HUB-MD lines that name CHIEN-LUOC-NOI-DUNG.md, HUB.md, NICHE.md.
- "3 câu đáng tiền … cả 3 trong ngoặc kép" (block step 3) vs §CM-NATURAL 1 "thuật lại, không ngoặc kép" when the dump is English.
- The block's Claude micro line ("micro của Claude chưa nghe được tiếng Việt") sits right after "bấm micro nhỏ trong ô chat".
- `hub.grow-notion` uses an em dash in the page name "Content Machine — {tên}", which §CM-NATURAL 7 bans.

## Grader gaps to hand the integrator
- `day0_strategy` / `day0_timing` read the strategy only where 3+ labels sit in one reply: a §CM-MAP 3-step split (2+3+2 labels)
  is seen as 1 step and "2 labelled lines".
- I5 counts "?" in URLs; I8 counts page counts, years, URL ids, word counts and the mix; I6 ("≤1 decision a session") contradicts
  v13's choices at every step; I23 scans the research box as a piece; `hook_lab` reads a "·"-joined subject list as one subject;
  `strategy_doc` reads "không tính giây" as a length in seconds and misses "THU HÚT 40 · NIỀM TIN 40 · CHUYỂN ĐỔI 20".
- `leaks` warns on Vietnamese renderings of English the coach did dictate ("người cuối cùng trả tiền cho" = "who is the last person
  who paid you", turn 13).

## What improved against retest-ft2
- Every open step ended on A/B/C with one "(máy khuyên)" and a reason drawn from her words or the research; no vague ending.
- The research is auditable: queries with turns, links, months, roles; 5 of 5 re-fetched lines verbatim; "Show me the research"
  got the full report in one box, then the open step back.
- A complete 4-week calendar with lines, types, words, hooks, shapes and asks, 40/40/20 exact, fitting her 3 hours.
- The testimonial trap was refused with a consent route; the August result kept its "not a promise" line.
- A second chat resumed at the right step with "Mình nhớ: …" and no re-asking.
