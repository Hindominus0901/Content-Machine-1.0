# wf13 · Internal fit: "posts and channels the coach likes or follows"

**Founder request (verbatim):** "t nghĩ là có thể thêm 1 cái đó là user có thể đưa lên các bài hoặc các kênh mà họ thích hoặc theo dõi". In English: the coach can bring in the posts, or the channels, that they like or follow.

**Scope of this page.** It maps where the request fits the current design and which rules it must respect. It does not pick the final design.

**What I read.** DECISIONS.md, PLAN.md, wf11-ux-spec, wf11-message-focus, arch-final-spec (§4, §5.1–5.10, §6, §7, §8), wf7-research-module-spec, wf10-access-modes-design, founder-sources, wf9-entertainment-catalog, wf8-mattgray-playbook (§0, §7, §9), wf12-qa-spec (§0–§5), wf12-qa-runtime (row 5), wf1-research-ideation (F4–F7), arch-proposal-coach-ux/-outcomes/-robustness (the cut lists), wf6-character-design (F13, §6), wf2-vietnam-market, and platform/targets.toml. I also read the files already built: `schemas/banks.toml`, `schemas/brand-card.toml`, `schemas/hub.toml`, `core/method.toml`, `strings/{en,vn}.toml` and `locales/*/deny-list.txt`.

---

## 0. The short answer

1. **The design already has half-built slots for this, but no way for the coach to reach them.**
   - **Bank row type W, "Swipe/outlier".** It is in arch §5.3, `banks.toml [types.W]` and the hub's Type option "Swipe". Its fields are pattern-with-topic-removed, link, ratio and my_version.
   - **The old command "Remix this: [post]" / "Biến tấu bài này".** It survives only as a router synonym (UX §5.12). It routes to the `ideas` module ("remixing swipes").
   - **Research places and alternatives.** R3 reads comments under "creators made for this buyer" and follows the thread to any creator a buyer names. R4 builds the alternatives grid.
   - **The entertainment catalog.** Its 24 formats are "modeled on" public creators.
   - **A swipe-leak check** was proposed in wf12-qa-runtime: "no verbatim lines over 8 words from reference creators or competitors; swipes teach structure only". It **did not make it into** the final invariants I1–I18; I16 covers `examples.md` only.
2. **The weekly outlier scan was cut on purpose** (arch-proposal-coach-ux and -outcomes: "too much homework for 1–2 h/week"). It was replaced by an on-demand "Remix this". Any design that makes the coach go hunting for posts every week repeats a decision already made.
3. **Where it helps:**
   - It answers "I don't know HOW to say it". The coach recognises shapes they like even when they can't name them.
   - It feeds packaging and hooks (Goh's swipe file, Matt Gray's "re-run winners").
   - It personalises the entertainment catalog.
   - It shows "what everyone else does", so the machine can steer the coach the other way (Goh: "if everyone goes left, go right").
   - It supplies stance prompts (F13, the stance stitch), listening places and alternatives for research.
4. **Where it hurts:**
   - **Day 0.** The budget is ≤12 turns, 0 detours, the Map by turn 8 (EN) or 9 (VN), and film-ready by minute 24.
   - **Voice drift.** This breaks the authenticity and character checks (Au and C pillars).
   - **Dilution.** Most liked posts are off the Map.
   - **Copying, claims and legal exposure.** VN advertising law bans direct comparison and using someone's words without consent.
   - **The free-tier context and uploads.** ChatGPT Free has about 27K tokens of context and 3 uploads a day.
   - **A 6th phrase.**
   - **Unreadable links.** TikTok, IG, FB and YouTube comments can't be read in Search mode, so the machine might pretend it read a link.
5. **The safe shape:**
   - **Paste-in only.** Entry is through the existing "save this: / lưu lại:" phrase, or a plain paste, which the machine detects as it already detects transcripts.
   - **No new phrase and no Day-0 step.**
   - **"Their shape, your topic, your proof, your words."** The topic comes from the Map, and the proof and words come from the Bank.
   - **A new copy invariant**, plus copying added to the hard stops.
   - **Channels go to research** (L4/GROW and L3), never to automated monitoring.

---

## 1. Integration map

**Fit tags:**
- **USE:** worth doing in v1.
- **LITE:** only a passive or one-line form.
- **LATER:** belongs at L2 or above.
- **AVOID:** breaks a rule.

### 1A. Coach journey

| # | Integration point | What it would do | Constraint | Risk | Fit |
|---|---|---|---|---|---|
| J1 | Setup page, Door A's 4 steps, reply 1 | Mention the feature in the preview or the 3-line promise | Door A is 4 actions in about 3 min; the promise is exactly 3 lines; Day-0 uploads = 1 | Adds reading before value; a phone visitor might try to upload screenshots | AVOID |
| J2 | Day-0 dump prompt (5 topic hints) | Add a 6th hint: "creators you love and why" | The dump is the voice sample; the early win quotes "3 lines **you** said"; ≤12 turns | Creator text gets read as the coach's voice (phrases, passages, their_words). The coach talks about others instead of themselves. Quit point 4 (nothing back in minutes 8–10) if they go looking for posts | AVOID |
| J3 | Dump, "other ways to dump: paste your last 10 posts" | Accept pasted posts | Pasted material is data; nothing is invented; voice comes only from the coach | **Misattribution.** A pasted post by someone else gets treated as the coach's own post and fed into Voice Card phrases or `passages` | LITE: default to "someone else's" unless the coach says "mine". Never feed it into voice fields |
| J4 | Day-0 passive capture | If the coach mentions a creator unprompted ("I love how X does…"), note the shape silently | 0 extra turns, 0 detours, 0 questions | Low, if silent. Losing the note is fine | LITE |
| J5 | Early win, 7-line check, Map screen | Show liked creators or shapes | Early win = the coach's own words; the check has 7 fixed lines; the Map is one screen; NOT NOW ≤7 | Breaks the one-decision Map; shows framework-like talk | AVOID. A liked off-map topic the coach raised can appear in NOT NOW with a plain reason |
| J6 | FILM TODAY | Use a liked post's shape for today's script | The script comes from the dump, and "✓ Checked: uses your {story}" must name the coach's own material. Film-ready ≤24 min. Built to memorise (quit point 16) | A 2nd decision ("which post?"), a longer session, overlap with the creator's words | AVOID as a step. Allowed only if the coach pasted a post unprompted and the shape fits a big idea, with no question asked |
| J7 | Stop point and Brand Card | A visible "posts you like" line | Visible part ≤900 chars. Schema worst case is 814 EN / 889 VN, so **VN has about 11 characters spare** | The card overflows its one phone screen | AVOID (visible); see D3 |
| J8 | Week 1 (cut from the dump) and the wrap-up (3 lines) | A remix in Week 1, or a "paste a post you like" tip | Week 1 is cut from the dump; the wrap-up is 3 lines; one NEXT line | Dilutes the "≥70% own words" promise; makes the wrap-up 4 lines | AVOID |
| J9 | **"save this: / lưu lại:" any time** | A pasted post, link, screenshot or voice description is detected as someone else's. The coach gets a one-line verdict: "Saved: I'll keep the shape, not the words. It fits big idea 2", or "parked: different buyer". The result is a W row plus an Idea row in the queue | Phrase 2 already exists ("story, client words, result or idea → on-map or parked"); about 0.5 min. ≤1 question; no template fill; no "ratio" or "median" asked | Too little friction: the coach dumps 20 posts and the context fills (Free 27K). Covered by the "pattern only, raw text not kept" rule (H8, H9) | **USE (main entry)** |
| J10 | Router synonyms ("remix this", "make my version", "do this like X", "biến tấu bài này", "làm bản của mình") | Route to the remix job with no new taught phrase | 5 phrases plus the universal words; `router.toml` keeps synonyms (UX §5.12). `core/router.toml` is not built yet | "Do this like X" means imitating a voice: it must route to shape-only plus a voice pass toward the coach | USE |
| J11 | Daily "next" | Today's piece is sometimes a remix that was queued earlier | Exactly one piece; one NEXT line; L1 tasks give "no new ideas" | None if it comes through the plan | USE (passive) |
| J12 | Weekly Talk (5 questions, audio only, in belief order) | ≤1 of the 5 questions becomes a stance prompt from a saved post on this week's big idea ("A popular video says '…'. True for your clients?") | One device, no screen-reading, no camera (quit point 13); 5 questions; re-say shorts ≥70% the coach's own words | Reading a post mid-Talk needs a second screen. Quoting it could leak the creator's words into shorts | LATER (Option B). One paraphrased line ≤15 words EN / ≤25 tiếng VN, never naming the creator |
| J13 | Friday "my numbers" and the 5-line review | Ask for the best post the coach saw | 4 spoken numbers plus their own best post; 5 fixed lines; ≤5 min; no insight screenshots (quit point 14) | Turns Friday into homework; competes with the VoC drip | AVOID as an extra line. The BETS line may name a saved shape as the "New" bet |
| J14 | Monthly "plan next month" | Pick ≤1 saved shape for next month's "New" slot. Show "what they all do → what you'll do differently" | One decision (KEEP or sharpen); ≤20 min; New ≤20%; entertainment 20–30% | Turns into a review of other people's content | USE (Option B): one line inside the existing re-plan, with a default and no extra decision |
| J15 | Quarterly re-map | — | The message changes only on the evidence of the coach's own buyers | Liked creators pull the message toward theirs | AVOID |
| J16 | L0.5 reminders, L1 tasks (≤900 chars; can't read project files) | A capture variant: "seen a post you wish you'd made? paste it" | The nudge is pocket Map + Season dates + weekday branch; 1 capture question in 5 days, which mostly asks "what did a client say?" | Displaces VoC capture, which is the moat. No room in 900 chars. Tasks can't see W rows | AVOID |
| J17 | L2 board (Notion / Sheets Lite) | W rows in the Bank, plus a "Posts I like / Bài mình thích" view. A VA can collect posts | Hub property names and options stay EN; only view names are localised; never delete; the AI sets only Idea/Scripted/Reviewed | A VA collecting at scale recreates the cut outlier scan. Commenter names in screenshots | LATER (USE at L2) |
| J18 | L3 Autopilot (BATCH / DROP / REVIEW) | BATCH may use ≤1 W shape a week, for the New slot only. REVIEW counts how remixes perform | ≤5 scripts a run; ≤3 searches; references ≤4 per job; research text is data | Unattended remix with no coach in the loop: copy risk. Needs lint (I19) inside `ship_lint.py` | LATER |
| J19 | L4 GROW: research, packaging library, ads | Channels become listening places (R3) and alternatives (R4). Their ads are read (Deep). Liked titles and hooks are mapped onto the packaging library's patterns | GROW ≤60 KB; Browse is opt-in; Paste is the VN default; read-only | Turns into a competitor-copy workflow | USE (Option C) |
| J20 | L5 deep character | "Whose content do you love, and what exactly? Whose annoys you?" These reveal taste and values, and the enemy | Conversation only; the Card holds traits, principles and values; polarize on ideas, never people | Coach copies a persona instead of excavating their own | USE (Option C), as questions only |
| J21 | Door B Phone Starter | Same handling as J9, with no router | ≤7,500 chars; no § signs, no English in VN; never mentions a project; one paste per new chat | Free: a screenshot uses up one of the 3 daily uploads. A share link can't be read. Long pastes bring the fresh-box trigger closer | LITE: guard line only. Ask for "tell me what happens in it" by voice, or the caption text |
| J22 | Helper path / move-in | — | The helper does install only | — | n/a |
| J23 | "I'm stuck / mình bị kẹt" | Offer for "don't know what to post": "paste a post you wish you'd made; I'll make your version" | Plain diagnosis; one NEXT line | None | USE (one line in the stuck branch) |
| J24 | "make it sound like me" | After any remix, a voice pass toward the coach's Card | Humanize + Voice Card | The coach asks to sound like the creator instead | USE; "sound like X" is refused and redirected |

### 1B. Data

| # | Integration point | What it would do | Constraint | Risk | Fit |
|---|---|---|---|---|---|
| D1 | **W bank row** (`banks.toml [types.W]`: pattern · link · ratio · my_version; states Active/Retired; hub Type "Swipe") | Hold one liked post as a topic-free pattern | Bank text is data. IDs never shown. Public quote cap 15 words EN / 25 tiếng VN. Never store a private person's name, handle or profile link | **`ratio` is `required = true`**. That clashes with "nothing invented" / "blank is not zero", with "views-based medians before a board exists" (never-sees) and with quit point 14. The coach rarely knows a creator's median | USE with changes: ratio optional; add `kind` (post / channel), `shape` (catalog E-ID or packaging pattern), `fits` (big idea n, or an X-ref), `hook_type` (not the hook verbatim) |
| D2 | **Channels ("các kênh")** | Store a liked creator or brand | One W row = one post (arch §5.3). The bank's prefix regex is `[VOSBPRKICAWX]`. The research spec reuses `K-` for alternatives (it collides with K = keyword in banks.toml) and `A01`/`C01` for people | A new prefix grows the regex, the deny-list, `hub.toml` Type options, the Sheets CSV and the graders | Use W with `kind = channel`. A channel that sells to the same buyer goes to the R4 alternatives grid (GROW) |
| D3 | **Brand Card** (whole ≤5,000 EN / 5,800 VN; visible ≤900) | A machine line `liked_shapes: a \| b \| c` | Schema worst case is already about 11.1K EN / 11.8K VN; the card fits only through `trim_order`. Visible headroom: 86 EN / 11 VN chars. A no-hub coach has no other memory | Crowds out passages and client words, which are the authenticity material | Option B only: one machine line, ≤3 × 40 chars (about 140 EN / 160 VN), **first** in `trim_order`. Never in the visible part |
| D4 | Hub schema (Notion + Sheets Lite) | Bank Kind gains "Post" and "Channel". New view "Posts I like" / "Bài mình thích". `Used In` links a W row to the Content rows it shaped | Property and option names are EN in both editions; only views are localised. The `Source` note says "role only, never names" | Naming a public creator in `Source` conflicts with that note and with DECISIONS ("no names or handles in captured research") | LATER (L2). Needs a founder ruling on naming public creators (§10, F1) |
| D5 | Method file anchors (`core/method.toml`: TALK WEEK TODAY NUMBERS MONTH FORMATS CTA-KIT CHARACTER-LITE RESEARCH-LITE EDGE HUMANIZE GUARDRAILS LOCALE) | Option 1: a new `§CM-LIKED` anchor (detect → verdict → shape → map fit → write from the Bank → copy checks). Option 2: spread it over FORMATS, GUARDRAILS and RESEARCH-LITE | Each section ≤2,048 B EN / ≤2,304 B VN. VN averages about 1.38 bytes/char, so about 1,670 VN chars. Every anchor must be named by the kit's router (lint E130) and have a strings title (`anchor.liked`). A ≤25 KB "Claude Free light" may ship | Spreading it means 3 anchors near their caps, and the copy rule gets lost. A new anchor costs one router line in the kit | A new anchor is cleaner; drop it from the light variant |
| D6 | GROW-{EN,VN}.md (≤60 KB) | R3/R4 handling of channels, a deconstruct-and-remix prompt, packaging-pattern mapping | One upload; lifetime sources ≤3; VN written natively | Little | USE (Option C) |
| D7 | L3 skill (`SKILL.md` ≤300 lines; description ≤190 chars, EN currently 186; references ≤150 lines / 9 KB; ≤4 per job) | The remix job loads ideas + packaging + guardrails + language (4, at the cap) | Router evals: route ≥95%, trigger ≥90%, false trigger ≤10% | Adding research makes 5 files (over the cap). The description has no room for "remix" | Fold everything the remix needs into those 4 files |
| D8 | Automations (BATCH / DROP / REVIEW; ChatGPT tasks can't read project files) | Connected BATCH reads ≤1 W row for the New slot. The standalone VA task embeds ≤1 pattern line | Nudge ≤900 chars; standalone ≤5,000 / 5,800; connected ≤600 / 700 | Unattended copying | LATER; nudge tasks get 0 chars |
| D9 | VoC bank (V rows) | Comments **under** a liked post may become V rows | Keep test G1: the author must be the buyer, with their situation stated in the post; sellers, coaches and marketers are discarded. 2 people × 2 places | **The creator's own words are never V rows.** If they leak into `their_words` or keyword candidates, the "their words" test on the Map breaks | USE in research only |
| D10 | Keyword registry (K rows) | A liked creator's coined terms go on an avoid list ("words they own") | A candidate is said by ≥3 people in ≥2 places and is not owned by an alternative; no new coined term mid-Season | The coach adopts a creator's keyword, which breaks Edge K and the signature thesis | USE as an avoid list |
| D11 | Entertainment catalog (`lib/moments`, E01–E24) | Map a liked skit or meme onto the nearest E-format, so it inherits the 5 gates and the trust-killer table | Cap 20–30%; never two entertainment posts in a row; Buyer Filter; formats already retired (movie parody, off-world lifestyle POV, drama-jacking) | A liked post in a retired shape gets made anyway | USE (FORMATS anchor) |
| D12 | Variation guard (`recent_hooks`, last-10 stems) | Treat the liked post's hook stem as already used | New stem against the last 10; the same structure ≤2 in a row | The same shape gets remixed 3 times in a row | USE |
| D13 | Project sources | A "MY-LIKED-POSTS" file | `lifetime_sources` ≤3 (method, Brand Card, GROW); Day-0 uploads = 1; Free 5 files / 3 uploads a day | Breaks the source budget | AVOID |

### 1C. QA

| # | Integration point | What it would do | Constraint | Risk | Fit |
|---|---|---|---|---|---|
| Q1 | Output classes (QA §2.1) | The W capture gets a one-line verdict (like "save this:"). A remix is a Script (normal), or a Script (claims) when digits, prices or urgency appear | Assigned mechanically | A remix that carries the creator's "$10k in 30 days" structure becomes a claims piece with no P-row | USE |
| Q2 | Ship Check step 0 (PRE plus FOCUS) | The slot row comes from the Map; the liked post supplies only the shape | Topic not on NOT NOW, otherwise bridge or park; material-first drafting | The post becomes the topic | USE |
| Q3 | Edge **Au** (swap test) | The remix needs an only-you detail from a Bank row (S, V, C or R) | Au = 0 if a competitor could post it unchanged | A remix is, by construction, close to something a competitor did post | USE: with no Bank material, DOWNGRADE, or ask "Needs you: what happened when you…?" |
| Q4 | Edge **C** plus the borrowed-attractor detector | A hook that names or leans on the creator ("What Hormozi taught me") counts as borrowed authority | Borrowed-attractor-only hook = C 0, which means re-ideate. wf8 §9: no celebrity borrowed-authority titles | Name-dropping | USE |
| Q5 | Edge **K** and the keyword rules | The coach's Season keyword, exactly once. A liked "comment GUIDE" CTA is borrowed as a shape only | One keyword and one asset per Season; every keyword delivers a real A-row; `cta_style` quiet is honoured | A second asset mid-Season; a keyword that delivers nothing | USE |
| Q6 | **New invariant I19: no copy** (restoring wf12-qa-runtime's swipe-leak check) | No 8-word run (EN) shared with any pasted third-party text in shipped output. VN threshold needs calibrating (proposal: 12 tiếng, since 1 word ≈ 1.6 tiếng, from the 15 vs 25 quote caps) | `graders.py` has the pasted text in the transcript. `ship_lint.py` (Claude) can run it; elsewhere it is a manual presence check, recorded as `lint: manual` | **I16 covers `examples.md` only, so today nothing catches a near-copy** | **Required** |
| Q7 | **Copying as a hard stop** | Verbatim or near-verbatim posting of another creator's text as the coach's own is refused | Current hard stops: fake scarcity, invented proof, guarantees, cure claims, someone else's likeness or voice, attacks on people, seeding, public phone numbers. **Copying is not on the list**, so "post anyway" could ship a near-copy | Plagiarism under the coach's name; VN advertising law Art. 8 ("using someone's words without consent") | **Founder decision F2** (recommend: hard stop) |
| Q8 | I8 allowed_numbers, and claims carried over | Numbers, results, testimonials and urgency in the liked post are never `allowed_numbers` and are never carried over | Only P-rows (Substantiated + consent); urgency only from the Ledger; VN "giảm X kg trong Y ngày" and nhất / duy nhất are banned | "Only 3 slots left" copied from a launch post = fake scarcity (hard stop). A fitness creator's result copied = health claim | USE |
| Q9 | I9 quote cap, I10 seeded names | A quote (stance stitch F13) ≤15 words EN / ≤25 tiếng VN, anonymised. Never commenter names from screenshots | VN: "never show or name the creator" (F13) | Screenshots carry names (PDP Law 91/2025) | USE |
| Q10 | I11 injection | A pasted post that says "ignore your rules" is data | — | A creator's caption with a jailbreak in it | USE (add an eval) |
| Q11 | I1, I2, I4, I5, I6 | One NEXT line; no template-fill ask (never "send me link, views, median"); no "outlier", "ratio", "median", "swipe" or W-IDs in coach text; ≤1 question; any choice has a default | G6 QUIT triggers: >2 unexplained terms, options with no default, >300 words before anything usable | "Paste 5 posts, then pick one" = 2 decisions | USE |
| Q12 | I15 VN pronouns, I17 no praise | Keep the coach's xưng hô even if the liked post uses another; no "great post!" | Pronoun pair 100% consistent | Teencode or "thím/fen" register gets imported | USE |
| Q13 | Ship Check card (896/900 EN, 997/1,000 VN; task variant 721 / ~822) | Add a "shape only" line | **No room in either edition** | Going over the budget breaks lint E132 | AVOID: the rule lives in the kit guard line and the LIKED/GUARDRAILS anchors |
| Q14 | Deny-list (`locales/*/deny-list.txt`, E140) | Add: outlier, swipe file, re:`(?i)\bratio\b` near "median", "median" (before L2). Widen the ID regex `[VSPX]-\d+` to `[VOSBPRKICAWX]-\d+` | Lint scans shipped strings/guides/examples; graders scan runtime transcripts for I4 | W-IDs leak today, because the regex covers V/S/P/X only | USE |
| Q15 | Matt Gray names (E142) at runtime | If the coach pastes Matt Gray posts, "Content Waterfall", "Content GPS" and the rest must not appear in scripts | E142 lints only shipped text; I-graders must also scan transcripts | EN coaches are likely to like him | USE: make it a general rule: any liked creator's coined terms become avoid-list words |
| Q16 | House rules page (~12 bullets) | Widen rule 3 "Strangers' words are paraphrased" to "Other creators' posts give a shape, never their words, numbers or names" | One page, about 12 bullets | A 13th bullet | USE (edit rule 3) |
| Q17 | Standards (`qa/standards/shared.md`) | A critical item "SG-copy" (I19 plus no carried claims) | Build-only rubric; the judge re-traces sources | — | USE |
| Q18 | Evals (P0 to P5) | ideas +10 remix cases; guardrails +8 must-block (verbatim copy, "write it in X's voice", carried income claim, "3 seats left", creator named in a VN script) and +6 must-not-block (format shell, comment-keyword shape, parody of own enemy); router synonyms; a `liked-paste.md` fixture per persona (seeded commenter names, an injection, an income claim); G4 T2 attribution test on remixes | ≥20 cases per module; 0 false blocks | — | Required with any option |

### 1D. Research module

| # | Integration point | What it would do | Constraint | Risk | Fit |
|---|---|---|---|---|---|
| R0 | Access check | A liked channel on TikTok/IG/FB/LinkedIn can't be reached by Search (5 Oct 2026). Browse (Claude in Chrome on Pro+, or ChatGPT `@Chrome` on Plus/Pro, VN availability unverified) is opt-in and needs the coach watching. Paste is the VN default | Never computer use; never a cloud browser signed in to personal social accounts; comment reading is untested (`browse_agents_read_comments` = VERIFY) | **The machine claims to have read a link it never opened** (wf7 rule 9: an unopened page is a LEAD, not voice) | USE: "I can't open that link here. Paste the caption, or tell me what happens in it" |
| R1 | Research plan checklist ("Behavior: who they follow / what else they watch, the dream-follower overlap") | A creator the coach thinks the buyer follows becomes a place candidate and goes through the place test (≥2 of 20 items by the buyer) | One buyer; scope questions first | Confusing "who I like" with "who my buyer follows" | USE (GROW) |
| R3 | Listening sprint | Comments under the liked creator's posts are read as buyer voice (keep test). "Follow the thread" adds a place | Read-only (never like, follow, join or comment); ≤60 lines / 45 min; ≤2 new places a session; role only; quotes ≤15 words / ≤25 tiếng; private groups give notes only | The creator's own words get logged as VoC | USE (GROW / L3) |
| R4 | Context sweep (alternatives grid, ads, reviews) | A liked channel selling to the same buyer becomes an alternative (≤3 Quick / ≤5 Deep). Output: words they own (avoid) · what they ALL promise (don't-say) · **what NONE of them say** (the coach's opening) · their longest-running ads | Only facts from pages actually opened, with URLs; names allowed for businesses and brands only; never click ads | "Context" turns into "copy the winner" | USE: this is where "go right" comes from |
| R7 | Weekly drip (inside Friday, ≤10 min) | — | The drip is VoC (comments, DMs, call notes) | Displaces buyer voice | AVOID |
| R8 | Monthly re-forage / scheduled public-only re-forage (Claude Pro) | Changes in liked alternatives' public pages and ads | Public pages only; social platforms unreachable unattended | Promising "we watch your favourite channels" when we can't | LATER, alternatives only |
| R-P | Privacy (wf7 §7.2) | Strip names, handles, avatars and phone numbers; crop screenshots; delete raw pastes after mining; copyright: analysis only, never republished | DECISIONS: "no names or handles in captured research"; never full computer use; VN PDP Law 91/2025 | Screenshots of liked posts carry commenter names and photos | USE |

### 1E. Message focus

| # | Integration point | What it would do | Constraint | Risk | Fit |
|---|---|---|---|---|---|
| M1 | Drift handling (on-map / bridgeable / not bridgeable) | Every saved post gets the same 3 outcomes: on-map (silent) · bridged ("fits if I angle it to big idea 2") · parked as an X row with a reason | Never lecture; off-map ≤1 in 10 (≤1 in 7 with a side door); NOT NOW shows ≤7 | The coach saves 10 off-map posts and feels judged | USE (reuse the existing lines) |
| M2 | Rule 9: parked topics are seasoning | A parked liked topic may appear as one line, never as the hook | — | — | USE |
| M3 | Rule 7: three signature phrases only; no new coined term mid-Season | A creator's terms are never adopted | Promotion only at re-plan | A slow drift into the creator's vocabulary | USE |
| M4 | Rules 5 and 12: on-pillar; New ≤20% | A remix of a new shape counts as "New" | ≥60% of a week on that week's big idea; ≥90% on-map over 4 weeks (eval) | Remixes crowd out re-say shorts | USE |
| M5 | Rule 1: one person per Season | A liked creator's audience ≠ the coach's buyer, so the Buyer Filter decides | — | The coach chases the creator's audience | USE |
| M6 | The WHY line and the four specifics | A remix still carries WHY (old → new belief, big idea, next step) and one person, one moment, one number from a P-row or `[NEEDS]`, and their words | — | A remix with no belief shift is just a format | USE |

### 1F. VN edition

| # | Integration point | What it would do | Constraint | Risk | Fit |
|---|---|---|---|---|---|
| V1 | Default app = ChatGPT Free (27K context, 3 uploads a day, 5 files) | Paste the caption, or describe it by voice, instead of screenshots | Day-0 uploads = 1; lifetime sources ≤3 | A long FB "chia sẻ" post runs 500–1,500 words (several thousand tokens). Screenshots use up the 3 daily uploads | USE: ask for "3 câu đầu + phần cuối", or a voice description; keep the pattern only |
| V2 | Advertising Law 16/2012 Art. 8 (no direct comparison with competitors; no use of a person's image or words without consent); Decree 147/2024; defamation (Decree 15/2020); "bóc phốt" | Never name, show, tag or quote an identifiable VN creator in a script; "người ta hay nói…" only | wf6 F13: "in VN never show or name the creator". Hard stop: attacks on private individuals | Stance pieces against a liked or disliked creator turn into call-outs | Required |
| V3 | Fully Vietnamese method (`method_prose = "vn"`) with `src_hash` | The LIKED anchor and strings are written natively, not translated | Byte budget 2,304 B ≈ 1,670 chars | EN calques ("Đây là lý do tại sao…") inside remix scripts | Required |
| V4 | Xưng hô and register | The coach's pronoun pair stays, even when the liked creator uses "anh em", "thím" or Gen Z teencode | I15; the Voice Card's dialect | Register drift | Required |
| V5 | Platforms (FB personal profile + TikTok + Zalo) | Liked "kênh" = TikTok channels, FB pages/profiles, YouTube, Zalo OA posts | Zalo: own groups only, notes only, never browsed | Zalo OA content pasted with phone numbers or IDs | USE with the privacy strip |
| V6 | VN keyword convention (uppercase, no diacritics) and "chấm" | A liked "comment 'UP'" shape maps onto the coach's keyword | I14: never blocked; one dated note | — | USE |
| V7 | Low-trust market ("lùa gà", KOL distrust: 54% trust ordinary users over KOLs) | Remixes of guru or hype shapes get the trust-killer table ("nổ/khoe", money flex) | Flex/freebie only as proof or CTA | Copying a VN guru's flex shape | USE |
| V8 | Copy culture risk [AI inference, not in the corpus]: VN audiences recognise re-uploaded or lightly reworded posts | I19 threshold for VN tiếng | Calibrate on the native reviewer's labels | Coach reputation | Required |

---

## 2. The journey: where it helps and where it hurts

**Helps (the pain it addresses).** The buyer insight is "tôi không biết nên nói cụ thể như nào để ra khách hàng" ("I don't know how to say it specifically so it brings clients"). A liked post is the coach saying "this is how I'd like to sound". The machine:
- turns that into a shape;
- puts the coach's Map topic and Bank proof inside it;
- does all the work.

The coach never fills in anything, and this matches the founder's "no templates handed over". It fits best after the Week-1 Friday, once the coach has a rhythm and is looking for variety: the "New" bet, the monthly plan, the "I'm stuck" branch.

**Hurts.** It hurts anywhere it adds a step, a decision, a screen of analysis, or a source of words that aren't the coach's. Mapping onto the 17 quit points:

| Quit point (UX §6) | How the feature could cause it | What has to hold |
|---|---|---|
| 1 Method file requested mid-session | The LIKED logic lives only in the method file | Compact mode handles a pasted post with the kit's guard line and never asks for the file |
| 2 Door B Day 2 mentions a project | "Save it to your project sources" | Door B never mentions projects; liked shapes live in chat or the MY CONTENT MACHINE box (≤1 line, optional) |
| 3 Save-for-reward gate | "Save this post first, then I'll write your version" | The remix is delivered whether or not anything is saved |
| 4 Nothing back in minutes 8–10 | The coach leaves to find posts during the dump | No Day-0 prompt to find posts |
| 5 12–15 KB brand wall | A "here's my analysis of your 6 favourite creators" wall | One verdict line per post; analysis stays internal |
| 6 Paid stream parked with no bridge | A liked topic parked with no reason | The bridge line, or the plain NOT NOW reason |
| 8 "New chat outside the project" | A task text that sends the coach elsewhere to paste posts | Capture happens only inside the project chat |
| 11 Keyword CTA with no quiet option | A borrowed "comment X" shape overriding `cta_style` | `cta_style` wins |
| 12 Email list ignored | The remix follows the creator's platform (IG reel) over the coach's mix (email-first) | Remix into `platform_mix`, never the creator's platform |
| 13 Two-device Talk | Watching a liked video during the Talk | A one-line paraphrase only |
| 14 Insight screenshots required | Asking for the creator's views and median | Ratio optional; never asked |
| 16 Reading the script while filming | A long remixed script | Same beat-card format (≤6-word on-screen text, ≤12 words per beat) |
| G6: template fill / >2 unexplained terms / no default / >300 words | "Send link, views, median, why you like it"; "outlier ratio"; "pick one of these 5 shapes" | I2, I4, I5 and a default on every choice |

---

## 3. Data detail

**Proposed W row.** It changes `banks.toml`, `hub.toml`, the Sheets CSV and `cmschema` checks.

| Field | Today | Needed | Why |
|---|---|---|---|
| pattern (Text) | required | required: "[shape] about [topic] for [who] using [device]", topic removed | The founder's Goh rule: copy the pattern, never the topic |
| link (Link) | **required** | optional: a post link, never a private person's profile; never a share link that can't be read | Voice or caption pastes have no link; a phone share link may carry tracking |
| ratio (Score) | **required** | **optional**, only from numbers the coach gave or that the AI read on an opened page; blank ≠ 0 | QA principle 2; never-sees "views-based medians"; quit point 14 |
| my_version (Detail) | optional | keep | — |
| kind (Kind) | — | post · channel | The founder said "bài hoặc kênh" (posts or channels) |
| shape (Detail) | — | catalog E-ID or packaging-pattern ID (internal) | Inherits that format's gates |
| hook_type (Detail) | — | type only (contrarian, list, POV…), **not the hook verbatim** | The verbatim hook is the most copyable 8-gram |
| fits (Refs) | — | big idea n, or X-n | Drift handling |
| creator (Source) | — | public creator or brand only; **founder decision F1** | The hub `Source` note says "role only, never names" |
| why_liked | — | the coach's own words go into a C row (Capture, "Noticed"), not into W | Keeps the coach's words separate from the creator's |
| raw text | — | **never stored**; mined to the pattern, then dropped | Copyright ("analysis only"); context; I19 |

**Other data points:**
- **Brand Card.** Option B adds at most one machine line, first in `trim_order`. The worst-case card (all fields at max) already needs trimming to fit 5,000 / 5,800.
- **Hub.**
  - Add Kind options "Post" and "Channel" and a view "Posts I like" / "Bài mình thích". Option values stay EN.
  - The "Swipe" Type option is already visible to a coach or VA at L2 (it is not marked internal). Consider renaming it to "Liked post" (EN in both editions) before the Notion template is built.
- **Method file.** One new anchor, `§CM-LIKED`:
  - its title in `strings.anchor.liked`;
  - an entry in `core/method.toml`;
  - a kit router line (E130);
  - in the VN edition, its native twin with `src_hash`.
- **GROW.** Deconstruct-and-remix prompt; R3 places from liked channels; R4 alternatives from liked channels; packaging mapping.
- **L3 skill.** The ideas reference holds the remix; the guardrails reference holds I19 and the copy hard stop; `ship_lint.py` gets an n-gram check against the pasted source; the remix job stays at ≤4 references.
- **Automations.** Nudge tasks get nothing. The VA standalone task may embed one pattern line. Connected BATCH may read one W row for the New slot.

---

## 4. QA detail

**Invariants I1–I18: what each needs from this feature.**

| Inv. | Effect |
|---|---|
| I1 one NEXT line | Every save or remix reply ends with one NEXT line |
| I2 no template fill | Never ask the coach for link, views, median or "why you like it" as a form |
| I3 verdict line | A remix gets the normal ≤20-word verdict. Its evidence must name a **Bank** item, never the liked post ("I'd post it: it uses your 2019 spreadsheet story") |
| I4 no codes | No outlier, ratio, median, swipe, W-IDs, E-IDs or pattern names |
| I5 ≤1 question / I6 ≤1 decision | Choosing among saved posts has a default; the monthly pick sits inside the KEEP/sharpen session as a default, not a second decision |
| I7 IDs resolve | A W row cited in a remix record resolves |
| I8 allowed_numbers | The liked post's numbers are not allowed; a cold-start persona remixing a "$10k" post must produce `[NEEDS]` or a process story |
| I9 quotes | ≤15 words EN / ≤25 tiếng VN, anonymised; VN never names the creator |
| I10 seeded names | `liked-paste.md` fixtures seed commenter names and the creator's handle |
| I11 injections | A fixture has an injection inside a caption |
| I12 format budgets | The remix obeys the coach's format caps, not the creator's length |
| I13 hub writes | A W row upserts by Ref; never deleted (State Retired) |
| I14 keyword CTAs | A borrowed "comment X" shape is never blocked; it carries the coach's keyword and one dated note |
| I15 VN pronouns | Unchanged by the creator's register |
| I16 8-gram vs examples | Unchanged |
| I17 no praise | No "great post / bài hay quá" about the liked post |
| I18 Ready | Unchanged |
| **I19 (new)** | No n-gram overlap at or above the threshold (EN 8 words; VN to calibrate, proposal 12 tiếng) with any third-party text pasted in the session or stored in W; applies to runtime output and golden runs |
| **I20 (new)** | No liked-creator name, handle or coined term in coach scripts (VN: always; EN: unless founder decision F3 allows a credited mention in the body, never in the hook) |

**Ship Check card.** It can't grow (896/900 EN, 997/1,000 VN; task 721/800). Copy protection therefore lives in the kit guard line, `§CM-LIKED`/GUARDRAILS, `ship_lint.py` (Claude) and the graders. On ChatGPT it is a manual presence check recorded as `lint: manual`, and G3b measures its miss rate (a check with >20% misses is removed from the standalone card and kept as a writing target).

**Phrases.** No 6th phrase.
- **Entry:** "save this: / lưu lại:" with a paste, or a bare paste, or a link, or a screenshot. All are detected.
- **Router synonyms:** "remix this", "make my version", "biến tấu bài này", "làm bản của mình".
- **Coach-facing words:**
  - EN: "a post you like" / "a post you wish you'd made".
  - VN: "bài bạn thích" / "kênh bạn hay xem".
- **Never** "swipe", "outlier", "ratio", "median" or "pattern".
- Note that "swipe file" already sits in wf6's freebie-hook word list, which is another reason to keep the word out of coach text.

---

## 5. Research module detail (channels)

**How a liked channel is classified (internal):**
1. **It sells to the same buyer** → an alternative (R4 grid row). The coach's opening is what none of them say.
2. **Its audience is the buyer** → a listening place (R3). Only commenters who state the buyer's situation count. The creator's own words are discarded as seller/coach.
3. **The coach likes its craft only** → a shape source (W, kind = channel). Shapes come from posts the coach pastes; the machine never browses the channel by itself.
4. **None of these** → nothing stored.

**Hard limits:**
- Read-only.
- No follow, like, join or comment.
- No monitoring or scheduled scraping of social channels.
- No scrapers or proxies.
- No full computer use.
- Zalo is never browsed.
- Reddit is never browsed in bulk.

On Claude Pro, the only scheduled re-forage allowed is public pages (competitor sites, open forums).

---

## 6. Message focus detail

**The formula:** the shape comes from the liked post, the topic from the Map (this week's big idea), the proof and words from the Bank, and the keyword from the Season.

| If the liked post's topic is… | The machine… |
|---|---|
| on the Map | uses it silently |
| near a big idea | bridges it, using the existing line ("fits your map if I angle it to big idea 2; say 'as is' for the original") |
| off the Map | parks it as an X row with a plain reason, then offers the **shape** on an on-map topic. "As is" counts against the off-map budget (≤1 in 10) |
| a different buyer, risky or generic | parks it (DIFF-BUYER / RISKY / GENERIC); RISKY never comes back |

**Exposure caps:**
- Remixes count as "New" (≤20% of a week's bets).
- Entertainment remixes count toward the 20–30% cap.
- Weekly focus stays ≥60% on that week's big idea, and ≥90% on-map over 4 weeks (eval gate).

---

## 7. Budgets

Measured with NFC (VN averages 1.38 bytes per character). The draft strings are mine and illustrative.

**Fixed items:**
- **Instruction block.** No start-block is in the repo yet, and the UX spec packs about 11 components into it. Two fixed parts are known: the Ship Check card (896 EN / 997 VN) and FOCUS (≤420). Treat the headroom as ≤250 characters.
- **Ship Check card.** No headroom.
- **Brand Card visible part.** 86 EN / 11 VN characters spare at the schema maximum.

| Artifact (budget) | A: paste-in (minimal) | B: A + rhythm (monthly shape, Talk stance, L2 view) | C: B + research / GROW / L5 | D: auto-follow channels |
|---|---|---|---|---|
| `1-INSTRUCTIONS.txt` (≤6,500 EN / ≤7,500 VN) | router line 60 EN / 51 VN + guard line 163 EN / 183 VN ≈ **225 EN (3.5%) / 235 VN (3.1%)** | same as A | same as A | — |
| `PHONE-STARTER.txt` (≤7,500) | guard line plus a "can't open links: paste or describe" line ≈ 265 EN / 290 VN | same | same | — |
| Method file (≤50 KB / 55 KB; section ≤2,048 / 2,304 B) | `§CM-LIKED` ≤2,048 B EN (4.0%) / ≤2,304 B VN (4.1%); omitted from the ≤25 KB light variant | + MONTH ≈300 B, TALK ≈250 B, FORMATS ≈200 B (each inside its section cap) | same as B | — |
| Brand Card (5,000 / 5,800; visible 900) | 0 | `liked_shapes` machine line ≈140 EN / 160 VN, first in `trim_order`; visible 0 | same as B | — |
| Ship Check card / task card | 0 (no room) | 0 | 0 | — |
| Task nudge (≤900) / standalone VA (≤5,000/5,800) / connected (≤600/700) | 0 / 0 / 0 | 0 / ≈150 / ≈80 | same as B | — |
| GROW (≤60 KB) | 0 | 0 | ≈2.3–2.7 KB EN / ≈3 KB VN (R3, R4, the remix prompt, packaging map) ≈ 4–5% | — |
| L3 skill (refs ≤9 KB each; ≤4 per job; description 186/190) | ideas ref ≈ +1.5 KB, guardrails ref ≈ +0.5 KB; description unchanged | + automation ref ≈ +0.5 KB | + research refs ≈ +2 KB | — |
| strings (`en`/`vn.toml`) | ≈6 keys (saved on-map, saved parked, can't-open-link, copy refused, voice-of-X refused, stuck-branch line), 60–120 chars each | +2 (monthly shape line, Talk stance prompt) | +3 (L5 questions) | — |
| Hub / Sheets | 0 (W exists) | +2 Kind options, +1 view, regenerated Notion prompt and CSV | same | — |
| Deny-lists / lint | +4 entries, wider ID regex | same | same | — |
| Evals | +10 ideas, +14 guardrails, router synonyms, 1 fixture per persona, I19/I20 graders | + Talk and monthly cases | + R3/R4 cases (G1–G13) | — |
| **Verdict** | Fits | Fits if Option A's eval gates pass | Fits | **Rejected.** It breaks read-only/no-automation scraping, platform reach (no Search on social), "tasks can't read files", the cut outlier scan, and Browse needing the coach to watch |

---

## 8. Pre-existing inconsistencies found while mapping (fix whatever is chosen)

1. **`banks.toml [types.W]` has `ratio` required (and `link` required).** That conflicts with "blank is not zero", with never-sees "views-based medians before a board exists", and with quit point 14.
2. **ID collisions.** In the research spec, `K-` means alternatives/competitors and `KW-` means keyword candidates; in `banks.toml`, K = signature keyword. Likewise, research's people codes `A01` / `C01` sit beside the bank's A (gift) and C (capture) prefixes.
3. **The deny-list ID regex `\b[VSPX]-\d+\b` misses W-, O-, R-, K-, I-, C- and A- IDs.** B- is only partly covered (`B[1-7]`).
4. **The swipe-leak check (wf12-qa-runtime row 5) was dropped from the final invariants.** I16 covers `examples.md` only.
5. **Copying is not a hard stop.** "Post anyway" can override everything except hard stops.
6. **Hub Type option "Swipe" is coach-visible at L2,** while the `Source` note "role only, never names" blocks naming public creators.
7. **"Remix this / Biến tấu bài này" depends on `core/router.toml` keeping old phrases as synonyms (UX §5.12),** and that file isn't built yet.
8. **E142 (Matt Gray names) lints only shipped text.** Runtime transcripts need the same scan.

---

## 9. Hard constraints any design must satisfy

1. **No 6th phrase.** Entry is "save this: / lưu lại:", a bare paste, a link or a screenshot (detected automatically), plus router synonyms. Coach-facing words: "a post you like" / "bài bạn thích".
2. **Day 0 is untouched.** No prompt, step, question, upload or detour about liked posts between Start and the stop point. Budgets hold: ≤12 turns, Map ≤8 EN / ≤9 VN turns, film-ready ≤24 min, 0 detours, Week 1 delivered with the Brand Card unsaved.
3. **Shape only.** A liked post contributes its pattern with the topic removed:
   - the topic comes from the Map;
   - proof and words come from the Bank;
   - the keyword and the gift come from the Season.
4. **New invariant I19.** No n-gram overlap at or above the threshold (EN 8 words; VN calibrated in tiếng) with any third-party text pasted or stored. It is checked by `ship_lint.py` and the graders, and manually elsewhere (`lint: manual`).
5. **Copying, imitating another creator's voice, and impersonation are hard stops** (founder decision F2), so "post anyway" can't ship them.
6. **Nothing carried over.** Numbers, results, testimonials, prices, urgency and seat counts from a liked post are never `allowed_numbers`. Claims need a P-row; urgency needs a Ledger row.
7. **Authenticity still passes.** Every remix carries an only-you Bank detail (S, V, C or R) and passes the swap test. With no material, it is downgraded, or asks one "Needs you" question.
8. **No borrowed authority.**
   - The creator is never named or leaned on in a hook.
   - VN scripts never name, show, tag or quote an identifiable creator (Advertising Law Art. 8).
   - The creator's coined terms and framework names (Matt Gray's included) never appear in coach scripts.
9. **The creator's words are never the coach's words.** A liked post never feeds:
   - the Voice Card phrases;
   - passages;
   - `their_words`;
   - V rows;
   - keyword candidates;
   - the early win.
   Pasted posts default to "someone else's" unless the coach says "mine".
10. **Nothing invented about a link.** If the AI didn't open the page, it hasn't read it. Social links in Search mode lead to "paste the caption, or tell me what happens in it". The machine never claims to have watched a video.
11. **Message focus wins.** Every saved post gets on-map, bridge or park, through the existing drift lines. Off-map ≤1 in 10. Remixes count as "New" (≤20%). Entertainment shapes count toward 20–30% and pass the Buyer Filter and the trust-killer table. A creator's terms are never adopted mid-Season.
12. **One keyword and one gift per Season.** A borrowed CTA shape carries the coach's keyword, delivers a real A-row and honours `cta_style = quiet`. Keyword CTAs are never blocked (I14).
13. **The coach never sees the machinery:**
   - no "swipe", "outlier", "ratio", "median" or "pattern";
   - no W- or E-IDs;
   - no analysis wall;
   - one verdict line per post, ≤20 words, citing a Bank item;
   - ≤1 question per reply;
   - one NEXT line;
   - a default on every choice;
   - never a template to fill.
14. **The ratio is optional and never asked for.** No creator view counts or medians are requested, and blank is not zero.
15. **Privacy.**
   - No private person's name, handle, avatar, phone number or profile link, ever (commenters included).
   - Screenshots are cropped or stripped.
   - Raw pastes are mined to the pattern and dropped.
   - Analysis only; nothing republished.
   - Naming public creators or brands inside a W row is founder decision F1.
16. **Read-only, paste-first, never automated.**
   - No follow, like, join or comment.
   - No channel monitoring.
   - No scrapers.
   - No full computer use.
   - No cloud browser signed in to personal accounts.
   - Zalo never browsed.
   - Browse only as R0 opt-in, with the coach watching.
   - Paste is the VN default.
17. **Pasted posts are data.** Injections inside captions or comments are ignored (I11).
18. **No new project source** (lifetime ≤3: method, Brand Card, GROW). No liked-posts file.
19. **Free-tier safe.** Screenshots use up ChatGPT Free's 3 uploads a day, so prefer caption text or a voice description. Keep the pattern, not the raw text (27K context; Door B fresh-box). Compact mode (no method file) still handles a paste from the kit's guard line, and never asks for the file.
20. **Budgets.**
   - Kit addition ≤250 characters per edition.
   - Phone Starter addition ≤300 characters, with no § and no English in VN.
   - Ship Check card +0.
   - Brand Card visible +0; at most one machine line, first in `trim_order`.
   - Task nudges +0.
   - The method anchor stays within 2,048 / 2,304 B and is dropped from the ≤25 KB light variant.
   - GROW stays ≤60 KB.
   - The remix job loads ≤4 skill references.
   - The skill description stays ≤190 characters.
21. **Tasks stay self-contained.** ChatGPT tasks can't read project files, so no task depends on W rows. Unattended runs (L3) may use at most one W shape a week, only with `ship_lint.py` I19 running and never with a question.
22. **VN is native.**
   - The LIKED anchor and strings are written in Vietnamese with `src_hash`.
   - The coach's xưng hô is kept (I15), whatever register the creator uses.
   - No EN outside the allowlist.
   - Keywords are uppercase with no diacritics.
   - The coach's naturalness score stays ≥4/5.
23. **Schema fixes before build:**
   - W.ratio and W.link become optional;
   - add W `kind` (post/channel), `shape`, `hook_type`, `fits`;
   - store no raw text;
   - widen the deny-list ID regex;
   - add "outlier", "swipe file", "ratio" and "median" to the deny-lists;
   - extend the E142-style scan to runtime transcripts.
24. **Eval gates.**
   - ideas +10 cases; guardrails +14 (must-block: verbatim copy, "write it like X", carried income claim, copied scarcity, VN creator named; must-not-block: format shell, comment-keyword shape);
   - router synonyms;
   - a `liked-paste.md` trap fixture per persona;
   - G4 attribution test on remixes;
   - 0 false blocks;
   - on-map ≥90% over 4 weeks still holds with remixes in the mix.

---

## 10. Founder decisions this needs

- **F1. Public creators.** May a W row (internal only) store a public creator's or brand's name and post link? Today DECISIONS says "no names or handles in captured research" and the hub `Source` note says "role only". The research spec already allows business and brand names in the alternatives grid.
- **F2. Copying.** Make verbatim or near-verbatim copying, and "write it in X's voice", hard stops, so "post anyway" can't override them?
- **F3. Credit lines (EN only).** Allow "inspired by [creator]" in a post body, never in a hook? VN: never.
- **F4. Scope.** Option A (paste-in), B (+ monthly shape and Talk stance) or C (+ channels in research and L5)? Option D (auto-follow) is not recommended.
- **F5. VN copy threshold.** Calibrate I19 in tiếng on the native reviewer's labels (proposed 12).
