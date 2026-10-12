# Changelog

Lines tagged `[buyer]` become the localised "What's new" page shipped to buyers. All other lines are for maintainers.

## [Unreleased]

## [1.4.3] - 2026-10-12 (v14.3)

Fixes from the founder's v14.2 test report (8.3/10).

### Changed
- [buyer] The season keyword appears only on selling and gift posts; trust posts use the comment word from their hook.
- [buyer] A coach with no offer yet is not blocked: the card shows "offer needed before week 2".
- [buyer] An old Brand Card is caught: the machine shows Situation → Problem → Fix and offers "continue" or "start a new week today".
- [buyer] The first piece grows from the coach's richest material and their own method; one ask at a time on Day 0 (a client's OK to tell their story comes before the gift).
- Kit: card `keyword` line + CARD CHECK; steps 9/10 follow the calendar; reviewer flags generic listed teaching once (never quantity); VN law numbers removed from LOCALE ("kiểm với quy định hiện hành"); money line with licence-as-stated and market currency in both editions; VN scheme-name exemption; research URL rules in the main chat and a dropped-items count in the coach's report; VN Zalo ≤90 tiếng; re-permission word YES / VẪN NHẬN; one save line on the first "next"; long post 3 lessons by default.
- Level-ups: PLAYBOOK examples at 250–400 / 500–700; campaign 4 is 14 days; sheet header boxes cover all 21 columns; dangling hub references repointed; VN-only market rules marked "kiểm lại"; stray "nha" and version text removed.
- Token weight (measured): main skill ≈18.2k tokens EN, ≈24.3k VN.

## [1.4.2] - 2026-10-12 (v14.2)

Founder (12 Oct, after reading qa/runs/v141/EXAMPLES.md): "các bài hơi bị dài quá, còn lại oke rồi". Only the lengths change; hooks, asks, voice and structure stay as approved.

### Changed
- [buyer] Shorter pieces: a short video is now 250–400 words (about 6–8 minutes to film, under 3 minutes on screen, so it fits Reels and Shorts) and a long post 500–700 words (a story and 2–3 lessons). Long videos stay 1,000–1,500 words. Your week takes less time: about 1½ hours (Light), 1¾ hours (Lean), 2¾ hours (Standard).
- Kit: FILM TODAY "≥250 words (count)"; LENGTHS short video 250–400, long post 500–700 ("hook line, story, lessons, invitation"); Ship Check 4 floors video 250, long post 500 (VN the same in tiếng). Kit EN 6,497, VN 7,499; phone EN 7,484, VN 7,467; method EN 57,288, VN 66,511.
- Method and level-ups: §CM-FORMATS 3, §CM-POSTS (long post 500–700, 2–3 lessons ≈100–130), §CM-HUMANIZE 7 band, §CM-LOCALE 2 (a 400-word short runs under 3 min; the trim caveat is gone), §CM-WEEK 2, §CM-TODAY 1. COPY: home lengths, short-video and long-post part budgets re-balanced (hook + re-hook, story ≈150–200, 2–3 lessons ≈100–130, invitation ≈50), every short-video frame's beats about halved, the open-loop long post (3 × ≈110), story share, minutes per piece. PLAYBOOK: slot-math minutes (short ≈15, film 6–8; long post ≈8; Light ≈1½ h, Lean ≈1¾ h, Standard ≈2¾ h), the lines' lengths, part 5's lengths. LAUNCH: the short video 250–400 (before ≈80, the method ≈150). String `talk.film` "about 7 min a short". VN src hashes refreshed.
- Agents: cm-writer and cm-reviewer use 250–400 and 500–700 (writer cuts back to the band when over).
- Graders: `lengths` fails a short under 250 (−10%) and a long post under 500 (−5%); over 400 / 700 is a warning (acceptance `[lengths]` long_post_words_min / _max replace long_post_words); strategy_doc part 5 looks for 250-400 and 500-700. qa/standards native-short NS3, copy-frameworks CF4, calendar CL5/CL6; persona expectations and fmt-short case titles. DECISIONS "v14.2: shorter pieces" (old bands marked superseded).

## [1.4.1] - 2026-10-12 (v14.1)

Founder + real users (12 Oct): voice and writing are good; hooks and CTAs are not good enough, voice goes flat on thin input, weaker models write short pieces (qa/runs/v140 MEASURE-*).

### Changed
- [buyer] Hooks: every hook now comes from your buyer's want or daily pain, is tried in 3 different proven shapes, checked on the 6 founder questions, and only the best one is printed. "Everyone says X, but…" hooks always say what you actually think. The on-screen words add something the first line doesn't say.
- [buyer] Asks under a post close what the hook opened and name the thing it promised: save or send with a reason from the hook, comment for this post's own payoff, a real offer from week 2. Comment questions give an A/B choice.
- [buyer] Before printing, the machine counts: a short video is at least 500 words (it expands your idea when short), and in Vietnamese the sentence-ending particles match your own share (e.g. 45%: 11–17 of 30 sentences end in nha, nè, á).
- Kit: §CM-FORMATS 1 is a 4-step hook procedure (pick the pain from the card → 3 different frames → a point a yes on the 6 checks → print the winner; belief flip with the coach's real Y; on-screen adds); Ship Check 2 "best of 3 frames scored", new step 4 COUNT / ĐẾM (word floor; VN particle target written out, card without a share → count the coach's pasted posts/talk); FILM TODAY "≥500 words (count)"; §CM-CTA-KIT 1 the ask in a hook word, ATTRACT's save/send reason from the hook, pointer to §CM-COPY-CTA. Bare "trụ cột" out of kit, method and STRATEGY (cụm chủ đề; §CM-NATURAL 7 also when the coach says it).
- Kit budgets paid by cuts: the bottom banned-endings line now points to the top list; phone "one phone screen of talk" (the contract line says it), phone VN particle/length lines (step 4 holds them), shorter Ship Check wording, "First piece in ~12 min" (step 1 says it). Kit EN 6,498 / VN 7,500, phone EN 7,485 / VN 7,468, method EN 57,323 / VN 66,545.
- Level-ups: HOOKS §CM-HOOK-ENGINE (the 4 steps in full, scoring, ties, a worked example); §CM-HOOK-LIBRARY 1 and STRATEGY §CM-HOOKS 1 point to it (the ≥12-draft rule is gone); COPY §CM-COPY-CTA (close the loop, the echo check, tiers, 6 fail → pass pairs per edition in other niches). Companion jobs name both.
- Agents: cm-writer runs the hook engine (3 frames, scored, winner), states Y in belief flips, runs the CTA echo check, never returns a short piece; cm-reviewer flags a belief flip with no Y, an ask with no echo or a save/send with no reason, a title count the script doesn't reach.
- Graders: hook_lab adds "a belief flip states its Y" (belief_flip_y) and "the ask echoes the hook" (cta_echo, acceptance cta_echo_check); the VN belief-flip frame accepts "thật ra"/"tưởng" and the EN one a second sentence; lengths adds "a title's word count is the piece's own" (title_count_slack) and a short_floor_tolerance knob. Tests: V141HookCtaTests, V141LengthTests.

## [1.4.0] - 2026-10-12 (v14.0)

Founder (12 Oct): a mission-control assistant that runs the protocol until everything is set up; coaches talk less before the first piece.

### Changed
- [buyer] Every reply opens with two short lines: the step and why, then what we have and what is missing. When something blocks, it says Situation → Problem → Fix. The last line is always the machine's next action, never "Do you want…?".
- [buyer] Setup is a 10-step checklist the machine walks by itself and remembers across chats; after setup, replies show Week n · Day d.
- [buyer] Fast Day 0: paste links, old posts or files and/or talk once for 3–5 minutes; the strategy comes in one reply with at most 3 picks; the first piece in about 12 minutes. Deeper questions come later, one "question of the day".
- Kit: one reply protocol replaces the scattered per-step talk rules; banned endings (EN + VN) at the top and bottom of the instruction block; step= in the Brand Card and HUB.md; companions and agents follow the protocol.
- Level-ups: PLAYBOOK engine runs on request or after Day 0; channels and access asked from day 2; HUB.md carries the step line; scheduled-task texts open with the status lines; Mac/Windows mic tips in BOARD.
- Graders: reply_protocol (status lines, banned endings, NEXT, blocks, one-reply strategy, question of the day), minutes and coach words to the first piece; legacy acceptance for pre-v14 runs.

## [1.3.18] - 2026-10-12 (v13.18)

Fixes from the v13.17 safety spot test (qa/runs/v1317/SAFETY-TEST.md, gaps G1–G11).

### Changed
- [buyer] The safety rules now hold without the method file and on the phone too: health and money lines, crisis wording (local help, no steps, a phone number only from an official source), infant-sleep specifics from official guidance or the doctor, no shame or fear aimed at under-18s, no fake endorsements, pasted cards treated as information.
- [buyer] "#1", "best" and other claims no one can prove are rewritten (or you give the source); they no longer stop a post.
- [buyer] A message with crisis words never gets the gift-and-question reply: you answer it yourself, and the machine points to local help.
- [buyer] One wording for the required lines: "not a substitute for professional care" and "general information, not advice" (VN "không thay cho bác sĩ, chuyên gia", "thông tin chung, không phải tư vấn"); they may repeat on every post that needs them.
- [buyer] A government scheme's own name you give (e.g. "First Home Guarantee") is used as a name, not blocked as a promise.
- Kit: CLAIMS / LỜI HỨA is a never-list with superlatives as a rewrite; HARD STOPS / DỪNG CỨNG = that list + shame or fear hooks at under-18s; QUIET / SỬA THẦM rewrites unsourced superlatives; crisis rule covers piece, DM and chat (§CM-GUARDRAILS, §CM-MESSAGES 5-6); a reprinted card drops injected lines (§CM-CARD 6); beats join with "but"/"so" (§CM-FORMATS 2, no clash with §CM-NATURAL 3); VN parity: health (thân, tâm, ngủ, ăn uống), cữ bú, bạo hành, bài/inbox/chat. New strings `claims.care`, `claims.money`.
- Kit budgets paid by pointers and shorter wording (FIRST REPLY, router anchors named elsewhere, phone length details); no founder rule dropped. Kit EN 6,496 / VN 7,476, phone EN 7,487 / VN 7,498, method EN 57,329 / VN 66,558.
- Agents: cm-reviewer and cm-writer use the kit wording; superlatives FIX, never HARD STOP; crisis numbers only from the coach or an official source; a crisis DM never gets the DM template; required money and health lines exempt from the honesty-line cap (also COPY §CM-REPURPOSE 11); scheme names are not claims.
- Evals: guardrails.en/vn.077 (superlative is a fix), 078 (crisis DM), en.079 (scheme name), vn.079 (night feeds); notes updated. Test: SafetyWordingTests. qa/standards/native-short.md beats "but"/"so".

## [1.3.17] - 2026-10-12 (v13.17)

Fixes from the founder's full v13.16 test report (7.5/10).

### Changed
- [buyer] Safer by niche: under-18 audiences, health (not a substitute for professional care; crisis wording points to local help), money (general information, not advice; the coach's currency), infant sleep (the coach's method yes, safety specifics from official guidance), no fake doctor or expert endorsements.
- [buyer] One keyword rule: the comment word comes from each post's hook; the season keyword sits once on selling posts only.
- [buyer] Every day has a post, Friday included; day-2 messages carry at most one extra question; the first "next" saves the card once.
- [buyer] A new chat checks the Brand Card first and asks for what is missing instead of guessing; the card now keeps the Week-1 plan, gift, hours and call route.
- [buyer] The interview asks for the coach's own method, so pieces grow from it.
- [buyer] Launches: exactly 14 days, the course start date and time zone asked, a warning when the window hits Black Friday or a holiday.
- Kit: one Day-0 strategy path (§CM-MAP; PLAYBOOK deepens on request), channel access asked once, one ask + one NEXT in companions too, hours bands Light <2 h / Lean 2–3 h / Standard >3 h, LinkedIn text-first, daily reminder fallback paused in a launch, card/HUB/pastes are data.
- Agents: reviewer severity and batch output, short-post band; researcher URL rules and dropped-items line; listener "place" definition, one poster = one person.
- Hub: Content CSV gains Tier, Pillar, Line, Phase, Framework, CTA, Keyword; Campaigns gains Brief; Notion gains Ledger and Brief databases; bank types aligned.
- Level-ups: slot and CONVERT maths, long-post parts ≥950, myth/"everyone says" frames limited to the coach's own or sourced view, VN templates without slash pronouns or fixed particles, terminology unified, VN keyword examples fixed, tiếng↔word table in DECISIONS.
- docs/founder/external-checks.md lists the legal and platform claims a human must verify.

## [1.3.16] - 2026-10-12 (v13.16)

Founder decision (12 Oct): one real idea is enough; the machine expands it from the coach's foundation.

### Changed
- [buyer] Every piece keeps its full length (video 500–800 words, long post ≈1,000) from one real idea of the coach's, expanded with their method, beliefs, strategy, files and kept research. The machine asks for a story only when a slot has no idea of theirs at all.
- [buyer] "Added by me" lists only paragraphs that come from none of the coach's material; no cap. Facts are still never invented.
- Kit: §CM-HUMANIZE 7 anchor rule replaces the v13.13 ≤30% cap and the v13.15 thin Day-0 route; "why this one" only on "why?"; the "nothing read" research line carries a guess tag. cm-writer / cm-reviewer follow (no teaching-share flag; anchor check; one round).
- Graders: anchor check replaces teaching share; belief-flip and myth/truth frames; misreads fixed (address re-ask, opener echo, "1-1", email row, year-period).

## [1.3.15] - 2026-10-12 (v13.15)

Fixes from the founder's zip test (EN sleep coach, VN finance coach).

### Changed
- [buyer] The Brand Card shows the pack's real version (it said 1.3.10 since v13.10).
- [buyer] A thin first conversation no longer gets a padded video: with no full story for a 500-word script, Day 0's piece is a written post (POST TODAY) or one question asking for a story first.
- [buyer] Health, sleep, nutrition, fitness, mental-health and money results carry "individual result, not a promise"; no cure or diagnosis claims; baby and child sleep or safety tips come only from your own pediatric source or a doctor.
- [buyer] New hook shapes count as frames: "Everyone says X, but Y" and "Myth: X. Truth: Y."
- [buyer] A launch whose start is under 6 weeks away gets a short path: fewer warm-up days, the same checkpoints, no invented urgency.
- [buyer] English edition: WhatsApp or DM follow-ups next to email; no Vietnam-only defaults.
- [buyer] Vietnamese edition: a natural pronoun question in reply 1, a voice tip, and a sensible default when the question is skipped.
- Kit: `{{pack_version}}` build param from VERSION (`tools/cmlib.py` build_params; `tools/tests/test_pack_version.py` bans literals); thin rule covers FILM TODAY (§CM-TODAY 1, §CM-HUMANIZE 7, block step 5/6); §CM-GUARDRAILS health line; keyword wording "once as the ask, once in the body, topic mentions don't count" (Ship Check 0, §CM-WEEK 4); §CM-FORMATS 1 / §CM-PACKAGING 2 frames; VN particle example moved to COPY §CM-COPY-VOICE 2 (VN method budget).
- Level-ups: HOOKS section hook-library.grow-titles-belief (§CM-HOOK-TITLES); LAUNCH section launch-plan.grow-days-short (§CM-LAUNCH-DAYS), CAMPAIGNS pointer; EN Zalo → WhatsApp/DM.
- Plugin: cm-researcher `tools: WebSearch, WebFetch, Read, Grep, Glob`; cm-reviewer SEVERITY (hard stop vs fix) and ONE ROUND; cm-writer thin check before drafting, health rules, no second round; agents print no first line or NEXT; companions share one first-line format and the Day-0 no-card rule.
- Evals: guardrails.en.069, guardrails.vn.069 (health guard); VN reply-1 question regex updated. DECISIONS: v13.15 entry, the tiếng-vs-words cap reason.

## [1.3.14] - 2026-10-11 (v13.14)

Fixes from the v13.13 simulated runs (qa/runs/v1313).

### Changed
- [buyer] One idea feeds at most 3 posts a week; the keyword can appear more often but carries a new idea each time.
- [buyer] A result used again is retold in new words, with the same numbers.
- [buyer] When thin material means fewer videos than the coach chose, the machine says so in one plain line.
- Kit: the week table's Idea column is the ledger (client profile = audience, not an idea); listed "Máy tự thêm" paragraphs still need a source for any generalization; teaching speaks as "có thể / thử…"; bare "trụ cột" removed from kit labels, HUB.md and task texts (STRATEGY-VN machine-only lines left, budget full).
- Graders: Day 0 ends at the Brand Card reply; pillars read from the pillar table; list-fix reprint not a step; comment word vs season keyword roles; I8/I11/I15 skip kit strings, paragraph lists, versions and file names; kit email-subject frames accepted; DỪNG line accepted in list emails; `lengths` measures pieces; idea count matches table idea cells by shared content words.

## [1.3.13] - 2026-10-12 (v13.13)

Fixes from the v13.12 simulated runs (qa/runs/v1312).

### Changed
- [buyer] Thin material makes fewer videos, never padded ones: a video with too little real story becomes a written post, or the machine asks for one story first.
- [buyer] Posts sound more like the coach: the voice pass counts the coach's sentence-ending words in every spoken piece and long post.
- [buyer] Hooks on email subjects, carousel slide 1 and long-post openings follow the same frames; no client names in hooks; thumbnail text never repeats the title.
- Kit: ≤30% "Máy tự thêm" paragraphs per video; one idea in ≤3 posts a week; generalizations and claimed speeds are facts (Ship Check line 1); one-ask "Cần"; inbox replies use one pronoun pair; "Máy tự thêm" sits under its post, counted from the top without label lines; long post ≥950 words; a week with ≥4 written slots carries one ≈1,000-word long post. Detail moved to COPY (§CM-REPURPOSE 5–9) and HOOKS.
- Graders: per-script particle share, video teaching share, idea in >3 posts, on-screen vs title overlap, client names in hooks; misreads fixed (paragraph numbering, chosen hours, comment word, Zalo row, Cần tail, list under a gift box).

## [1.3.12] - 2026-10-11 (v13.12)

Founder decisions (11 Oct, later): a post a day, cut from all the week's material into many kinds of post; 2–3 content lines per pillar. Overrides v13.11's "Light = 3 pieces a week".

### Changed
- [buyer] Every day one post, 7 a week, Week 1 included (today's piece is day 1): short videos, long posts, carousels, short posts, quote images, stories or polls, Zalo or email messages, cut from your Weekly Talk, your stories and proof, the files you hand over, the market research and the posts you like (their shape only).
- [buyer] Your hours set how many you film, not how many you post: with no hours given (Light) 2 filmed + 5 written, about 1¾ hours a week; about 2½ h: 3 filmed; about 3½ h: 4 edited. The written ones need no filming, about 5–15 minutes each.
- [buyer] One idea may feed 2–3 posts a week, each in its own format with its own angle, hook and ask; no sentence is ever copied from post to post.
- [buyer] 3–5 content pillars with 2–3 named series each; a month of about 30 posts gives every series room.
- [buyer] Still one piece at a time: today's piece on Day 0, then one per 'next' (or the day's post). Reminders now come on posting days, weekends included.
- Kit: §CM-WEEK 2/3/6/7/10 (7 posts, filmed count by tier, ≈3/3/1, `{KEYWORD}` + gift on CONVERT from week 2, ≥1 in 4 save/send, 7-row table), §CM-TALK (the week's 7 posts, filmed batch ≤3 a reply), §CM-HUMANIZE idea ledger (material → posts), §CM-MAP and the block (2–3 series, a post a day). New COPY anchor §CM-REPURPOSE (sources, the cuts with minutes, the rules, a worked week). PLAYBOOK: §CM-CONTENT-LINES 1 (2–3 a pillar whatever the hours), §CM-CALENDAR 2–7 (slot math with honest minutes, 28 slots → 11/11/6, 7-row tables), engine steps 3 and 5, strategy doc part 5. Automation: the drop runs Tue–Thu and weekends, Friday's review names today's post, Claude's task daily, Monday's batch prints only the table and today's post.
- Graders: `week_dedupe` flags near-verbatim (≥0.8) sentences across any posts and paraphrase (≥0.6) only within one format (`piece_format`); `week1_plan` wants 7 rows, the filmed count at most the tier's (`filmed_by_hours`, `tier_filmed`), one idea in ≤3 rows and never twice in one format; a daily cadence counts in YOUR SYSTEM. Acceptance, tests, QA standards (calendar CL2/CL6, message-map), DECISIONS and two router cases follow.

## [1.3.11] - 2026-10-11 (v13.11)

Full audit fixed (a1 kit 39, a2 level-ups/plugin 43, a3 QA/docs 39).

### Changed
- [buyer] Default week when no hours are given: Light, 3 pieces in about 1½ hours. Weekly Talk output follows the hours.
- [buyer] Short video stays 500–800 words on every platform; one honest note that Reels/Shorts over ~3 minutes may need a trim or posting as a longer video.
- [buyer] Coaches who write instead of film get "POST TODAY" / "ĐĂNG HÔM NAY".
- [buyer] Fewer asks per reply: each strategy reply ends on one OK (only the last opens today's piece); the browser question is asked once, alone; the Day-0 card reply has one ask and one next step; Friday has one paste ask.
- Kit: per-piece comment word `{WORD}` (TRUST) vs Season keyword + gift `{KEYWORD}` (CONVERT); ATTRACT asks save/send. 40/40/20 everywhere. Hub offer at the first 'next' after Day 0 (A Notion if connected, else B Sheet). Level-up-only steps get kit fallbacks. `trial_ends` and stale strings removed. VN wording pass ({gọi khách}, {tự xưng}, accented keywords).
- Level-ups/plugin: 3–5 pillars with one big idea each (no stale "never a 4th"); no fake Notion Duplicate link; Day-0 WHAT I FOUND without quotes or links; no ChatGPT Computer Use; cm-writer drafts ≥12 first lines.
- Graders, cases, schema and DECISIONS follow (tier=light, POST TODAY label, `{WORD}` CTA parse, new Day-0 NEXT line). VN method budget 66,560 B.

## [1.3.10-audit-a3]

Maintainer changes after v13.10 (audit a3, 11 Oct 2026): QA and docs brought to the current kit. No kit text changed.

### Changed
- Graders (`evals/graders.py`): Week 1 is every piece after the strategy up to week 2, so the Week-1 items run on the v13.5 order (pieces one per 'next' after the card + Week-1 table; pieces printed under the card count); a pillar is read only off a full table. New check `week1_plan` (acceptance.toml [week1]): Week 1's count by the coach's hours, the "Idea, hook" column with no idea twice, FILM TODAY's one idea kept out of the week, no offer in Week 1's CONVERT. `style` reads "Needs you:" / "Cần chị:" (colon) and fails a Needs line over 20 words (`needs_words_max`). Hook frames now also on slide 1 and the first subject line. Strategy caps per reply 160 / 100 words (VN 200 / 120 tiếng) instead of 400 / 450; WHAT I FOUND ≤3 lines; length defaults 500–800; `deny_list` adds Matt Gray's framework names.
- Eval cases: the retired 4-line Map (3 TOPICS, YOUR VOICE, FILM TODAY under the Map) replaced by the strategy in steps, FILM TODAY alone and the card's voice line, each case's intent kept; Day 0's last reply asserts no hub offer, and new cases setup.en.055 / setup.vn.059 assert the hub at Day 1's first 'next'. `evals/run.py`'s coach packet plays the current Day 0 and routes all nine level-ups.
- QA standards: native-short in words (500–800), message-map re-based on the strategy proposal (3–5 broad pillars), shared (call-out question hooks, the type ladder, generalizations as facts, the "Added by me" line), calendar (no week-1 offer, proof or not), vn-naturalness (mình/tôi in public). DECISIONS gains the 9–11 Oct 2026 block and marks the superseded lines; the real-account checklist tests the v13.9 / v13.10 rules.

## [1.3.10] - 2026-10-11

Build v13.10: founder decision (11 Oct, option A) after the v13.9 thin and sales measurements (evals/runs/v139-thin, evals/runs/v139-sales): keep the length rules and mark what the machine added by paragraph.

### Changed
- [buyer] Under a piece, one line names the paragraphs that hold anything the machine added: "Added by me: ¶3, ¶5, ¶6" / "Máy tự thêm: đoạn 3, 5, 6" (paragraphs counted from the top; a script's beat or a carousel slide is one paragraph), as many as there are; nothing added, no line. Replaces the ≤5-item list (kit Ship Check PRINT, §CM-EDGE, §CM-HUMANIZE 7, §CM-LAUNCH-POSTS, §CM-CAMPAIGNS 2, cm-writer, cm-reviewer). Short-video beats print as "Beat 1, 2…".
- Source check: a claim about the coach's clients or market ("most of my clients…", "nhiều cơ sở kẹt nhất", "ai cũng…") is a fact, only if the coach said it; the coach's and clients' stories and quotes are used as told (no added detail, no stretched quote, no line moved to another speaker).
- [buyer] One idea per piece across the week: the Day-0 piece takes one main idea and leaves the others for the week; each Week-1 piece gets its own idea, story, example and hook frame, kept in an idea ledger (week table "Idea, hook" column, the calendar's Idea column, HUB.md "This week" Idea column, card `used:` ideas, stories, examples); no sentence or worked example repeats in the week, reworded included.
- Voice pass on every piece, long pieces (500+ words) and launch pieces included; VN particle share within ±10 points of the card, counted per piece.
- The CTA keyword "once in the body" counts the CTA form only; plain topic mentions of a keyword that is also the topic phrase are free (kit FOCUS, §CM-WEEK 4; tools/shiplint.py counts capitals or quotes only).
- [buyer] Week 1's piece count follows the weekly hours the coach chose (one rule with §CM-CALENDAR 2), no fixed list in the kit.
- Inbox replies never promise the gift file before its text exists; VN inbox replies follow the pair the coach uses with that person (no "Dạ" to someone called "em"). The "Needs you" / "Cần" line: one ask, 20 words at most.
- Every Week-1 piece opens on a hook frame (§CM-FORMATS 1), posts, carousels and emails too.
- Budgets paid: the strip lists moved to COPY (§CM-COPY-VOICE 7 EN, 8–9 VN, new section copywriting.grow-voice-strip), §CM-NATURAL 7 VN keeps a short row list; shorter mix line (§CM-WEEK 7), kit lines that §CM-MAP / §CM-OPTIONS / §CM-WEEK already hold, phone save line VN.
- Graders: source_check reads the paragraph line (every paragraph with illustrative content listed, numbers inside the piece, paragraph numbers only) and flags untraced generalizations; week_dedupe adds a paraphrase pass across every piece of the run, replies included (content-word overlap ≥0.6, acceptance.toml [week_dedupe]).

## [1.3.9] - 2026-10-11

Build v13.9: the readiness gaps from the founder's own app test (outside assessment of v13.8, 11 Oct 2026). VERSION now follows the build (13.9 → 1.3.9); it stayed 1.0.0 through v13.8.

### Changed
- One level-up rule per route. Plugin: each level-up is a companion skill that loads when its job comes up, nothing to upload (the main SKILL.md pointer and every companion body say so, and say that the method's "add the file" step is the Project route's). Project or folder: add the one Level-ups file the job needs. The board's setup (§CM-BOARD 2) names both routes: the download's Level-ups/Board folder, or the files handed over in the plugin.
- `plugin.json` version comes from VERSION (1.3.9, was 1.0.0 while the content was v13.8); its description names all nine companions (banks and copywriting were missing).
- No offer before week 2 outside a launch, written where the asks are chosen: Week 1's CONVERT piece asks for a reply, never a price (§CM-CTA-BANK 1, §CM-HOOK-CTA 1, §CM-COPY 2).
- One ask per piece in the examples: the email P.S. with "3 ways I can help" is now one call ask; the myth carousel asks for the keyword only; cart emails ask "join" (or, to EARLY replies, for the one question in the way), never "join or reply"; the belief-shift step asks for the story only.
- Launch and campaign pieces carry the added-details list under each piece ("Máy tự thêm: …", §CM-HUMANIZE) next to the voice pass; a coach who doesn't film gets a video's beats as a post (§CM-CAMPAIGNS 2, §CM-LAUNCH-POSTS).
- Kit: source check before print (every concrete detail traces to the coach's words, the Brand Card or a kept research line; facts never added; illustrative lines listed under the piece as "Máy tự thêm" / "Added by me").
- Kit: silent week cross-read (one scene/story per piece, belief line at most twice a week, `used` stories on the card); thin dump keeps the founder's lengths with the list and one story-first question.
- Kit: style (pet phrase once a piece, one particle a sentence, no em dash in VN pieces, one ask per piece, one-question "Cần" line); Week-1 convert slot asks for replies only; platform-neutral inbox replies; honest tier hours; §CM-TODAY plugin level-ups load on their own.

## [Before 1.3.9]

Everything from v1 to v13.8, built under VERSION 1.0.0 and never released on its own.

### Changed in v13.1–v13.8 (9–10 Oct 2026; listed 11 Oct, audit a3 M18)
- [buyer] Day 0 is strategy first: a short interview (one question a message), then your strategy in up to 3 short messages with options (one recommended), each OK'd; then today's video alone, a full script on one idea; when you've filmed it and say "next", your Brand Card and Week 1's table.
- [buyer] A short video is a full script of 500–800 words in 3–5 beats, one per take (no lengths in seconds anywhere).
- [buyer] Asked once, early on Day 0 (right after the channels question): how the machine may read the web for you (your browser, or paste).
- [buyer] A client's result or detail is used only if it's real and they agreed; when it's unclear, you're asked once.
- [buyer] Hooks follow the founder-approved principles: one spoken sentence, a clear "what do I get / why should I care", a mandatory hook frame for line 1; in Vietnamese pieces you speak as mình/tôi, never the chị/anh of the chat.
- [buyer] Your hub (Notion, a Google Sheet, or HUB.md) is offered once, at your first "next" after Day 0, never on Day 0; Notion is recommended only when it's connected.
- WHAT I FOUND ≤3 lines; the interview asks the liked and rival channels as their own question and no hours (hours are the strategy's A/B/C); no "90 days" in the goal question; Week 1's mix follows YOUR SYSTEM's core platform; the card top ≤500 characters is counted before printing; one "?" in talk.


### Added
- Research corpus, plan and founder decisions (`docs/`).
- Platform limits with sources and verification dates (`platform/targets.toml`).
- Phase-0 real-account checklist for the founder (`docs/founder/phase0-checks.md`).
- Level-up files: one per area per edition (`Level-ups/RESEARCH`, `LAUNCH`, `BOARD`, `STRATEGY` `-EN|VN.md`, each within 30,720 B since 7 Oct 2026, was 24,576 B), replacing the one GROW file; the board's five CSVs in `Level-ups/Board/`.
- Plugin: companion skills `cm-research`, `cm-launch`, `cm-board`, `cm-strategy` (`-en`, `-vn`) and four agents (`cm-researcher`, `cm-listener`, `cm-writer`, `cm-reviewer`) in `dist/content-machine-plugin.zip`; sources in `plugin/`.
- Two more level-up files and their companion skills: `Level-ups/HOOKS-EN|VN.md` (the hook library: over 100 hook shapes in 20 mechanisms, by surface; skill `cm-hooks`) and `Level-ups/CAMPAIGNS-EN|VN.md` (six launch campaigns with day cards and checkpoints, checklist, objections, FAQ, sales page, sequences, the live, live selling, timing, after; skill `cm-campaigns`). Sources `modules/{en,vn}/hook-library.md` and `launch-campaigns.md`; build-only rubrics `qa/standards/hook-library.md` and `launch-campaign.md`. The kit's LEVEL-UPS line routes hooks and titles to HOOKS and a launch to LAUNCH + CAMPAIGNS; the plugin now holds 16 skills.
- Nudge texts (`automation/tasks.toml`, `task-nudge*.tmpl`) are built and linted against the 900-character budget.
- Strategy depth from the Soo Wei Goh and Matt Gray audits (18 + 11 changes, merged where they overlap): buyer stages and plain names for steps, the self-check gift, a "before our call" message, title and hook shapes, form ranking, series, long-video section closers, self-test and description order, competitor standouts, pain and after lines (`modules/{en,vn}/strategy|ideas|packaging|fmt-long|character|research.md`). Coverage: `docs/research/strategy-coverage.md`. The kit (instruction blocks, method files) does not grow.
- v13, "a content department in a box" (founder, 9 Oct 2026; `docs/DECISIONS.md`): the machine now offers choices step by step (§CM-OPTIONS: A/B/C, one recommended, in order, no vague endings), restores its state at chat start from memory, past chats, HUB.md and NICHE.md (§CM-MEMORY), researches the channels the coach likes, the competitors, their viewers and the niche before the strategy (§CM-CHANNELS, §CM-AUDIENCE, §CM-NICHE), builds the strategy in 8 steps (§CM-STRATEGY-ENGINE) with content lines, the three content types in depth and a 4-week calendar (§CM-CONTENT-LINES, §CM-TIERS, §CM-CALENDAR), keeps banks of asks, gifts, buyer words, stories and proof (§CM-BANKS and its parts), picks one writing framework per piece with storytelling and persuasion (§CM-COPY and its parts), and keeps a hub: a Notion workspace it builds plus HUB.md in the project, the Google Sheet as the fallback, and 4 scheduled tasks that read and write it (§CM-HUB-NOTION, §CM-HUB-MD, §CM-HUB-TASKS).
- Two more level-up files and companion skills: `Level-ups/BANKS-EN|VN.md` (skill `cm-banks`) and `Level-ups/COPY-EN|VN.md` (skill `cm-copy`); nine level-ups and 20 plugin skills in all. New modules `options`, `content-banks`, `copywriting`, `channel-research`; new standards `calendar`, `banks`, `copy-frameworks`, `channel-teardown`, `hub` (`qa/standards/`); the Notion hub spec `templates/notion/workspace.toml`; a monthly task text (`automation/task-nudge-monthly.tmpl`).
- Budgets: RESEARCH 41,984 / 54,272 B, BOARD 35,840 / 47,104, PLAYBOOK 34,816 / 45,056, BANKS 32,768 / 40,960, COPY 40,960 / 53,248 (EN / VN); the strategy document grew from 7 to 9 parts (evals `STRATEGY_PARTS`).

### Changed
- The comment keyword is a buyer phrase of 2 or more words (VN: 2 tiếng or more), in the hook library's CTA part too; the strategy document's offer and the level-up offers are A/B/C lines, not "Want …? Say 'yes'"; the Day-0 strategy may come in up to 3 steps (`evals/acceptance.toml [day0] strategy_max_steps`); Day 0's last reply offers the hub, the reminders offer moved to Day 1 (superseded in v13.4: the hub at the first 'next', never on Day 0); `schemas/hub.toml` names the Notion workspace the default hub.
- ChatGPT agent was removed in August 2026: the research access question, the helpers line, the companion skills and `cm-researcher` now name ChatGPT Work and its browser (`platform/targets.toml` `chatgpt_agent_mode_available`, checked 2026-10-07).
