# Strategy coverage: Soo Wei Goh and Matt Gray

Where each idea of the founder's two strategy references lives in the machine (DECISIONS, 7 Oct 2026: "Soo Wei Goh and Matt Gray are the two primary strategy references"). Checked 7 Oct 2026 against `modules/en` and the built `dist/en` files, after the two audits' changes were applied.

- **Soo Wei Goh is the primary reference.** His trust stages, buyer-vs-sharer reach, objection mining and media-company loop set the order of the season, the review and the idea engine. Matt Gray's ideas fill in packaging, hooks, long video, naming and the gift.
- **Matt Gray's names stay out of coach text.** His ideas ship renamed in plain words; his framework names (Content Waterfall, Content GPS, 4-3-2-1, Authenticity Machine, Founder OS) never appear in shipped files (`tools/tests/test_build.py` checks the level-up files; `locales/*/deny-list.txt` blocks 4-3-2-1). Goh's stage names, "dream follower" and "Buyer Mirror" stay internal too.
- **House rules hold in every change:** no framework names, scores or IDs for the coach, at most one question per reply, one NEXT line, no invented numbers, results or testimonials, and fake scarcity stays hard-blocked.

Abbreviations: INS = `1-INSTRUCTIONS.txt` · CM = `CONTENT-MACHINE-EN.md` (the kit method file) · STR / RES / LCH / BRD = `Level-ups/{STRATEGY,RESEARCH,LAUNCH,BOARD}-EN.md`. Each VN file carries the same anchor (`-VN`), written natively.

## What changed (7 Oct 2026)

- **Soo Wei Goh: 18 changes applied** (16 level-up edits, 2 optional kit edits). Changes 17 (the price said plainly) and 18 (a "before our call" message once someone books) moved from the kit to STR §CM-SEASON (week 4 and item 4), because the kit's instruction blocks and method files must not grow; change 18 shares one rule with change 4 (§CM-STRATEGY-REVIEW 3 points to it).
- **Matt Gray: 11 changes applied.** Overlaps merged into one rule each: his title shapes and Goh's case-study titles are one list (the "effort but no result" shape and Goh's "you're wasting… (here's the fix)" are one shape); his long-video shapes and Goh's client-decision outline are one item (§CM-LONG 3); his buyer stages (§CM-STRATEGY 6) are the stages Goh's "who it's for" line and the titles point to.
- **Sizes:** STRATEGY-EN 20,032 → 25,997 B, RESEARCH-EN 18,705 → 19,108 B; STRATEGY-VN 24,495 → 30,688 B, RESEARCH-VN 24,528 → 25,072 B. The level-up budget (`budgets.levelup_*`) went from 24,576 to 30,720 B per file. The kit did not grow (CONTENT-MACHINE-EN 49,203 B, -VN 56,308 B; instruction blocks unchanged).

## Soo Wei Goh (primary reference)

76 rows: 72 ideas now covered, 1 kit-level idea now covered in the strategy level-up (x1), 3 excluded by design (x2-x4). Out of scope and not counted: premium visual identity, lighting and camera, editing style, in-house team and hiring, setters and closers, the private-profile disqualifier, qualifying forms on lead magnets, the training sales page, application page and ads, ascension, long free courses, and the offer operations from his 9 steps.

| # | Goh idea | Where it lives |
|---|---|---|
| 1 | Trust is built in 4 steps, in order (admire → like → believe → trust). Jumping to proof falls flat | STR §CM-SEASON 1: "Trust comes in order; jumping to proof falls flat." |
| 2 | Stage-to-funnel map: admire + like = top, belief shift = middle, proof and objection-killing = bottom | STR §CM-SEASON 1, weeks 1-4 ("Week 3, believable: proof shown, never claimed" · "Week 4, safe to buy from: objections answered"). CM §CM-WEEK 7: "a reach, a relate, a teach and (week 2+) a proof piece" |
| 3 | Tag every piece by funnel stage and judge each stage separately | Now covered · STR §CM-STRATEGY-REVIEW 1: "by big idea, job (reach, relate, teach, proof: §CM-WEEK 7), form and series". CM §CM-WEEK 5: the WHY line names the next step |
| 4 | The top of the funnel aims at buyer ∩ a wider follower who shares | STR §CM-STRATEGY 3: "Reach circle: topics both the buyer and the friends who share with buyers live" |
| 5 | Talking only to buyers kills reach ("puddle to ocean") | STR §CM-SEASON 3: "a buyer would tag a friend; a random 19-year-old scrolls past" |
| 6 | Entertainment must still come from the buyer's world (cross-reference at founder-sources line 139) | STR §CM-MOMENTS 2: "both ways (the buyer would tag a friend AND would pay to fix it)" |
| 7 | Funnel-shaped trust script: wide hook → credibility line → niche words so the wrong crowd leaves → belief shift → close | Covered · STR §CM-HOOKS 3 (shorts). Long video now covered · STR §CM-LONG-INTRO 3: "One line says who it's for by the buyer's stage … so the wrong viewers leave early" |
| 8 | Three-question check: breaks a limiting belief? hook broad enough? one message? | STR §CM-HOOKS 3: "Silent check: it breaks one belief · the hook is wide enough · one message." |
| 9 | Three hooks per short: on-screen title, visual, spoken | CM §CM-FORMATS 1: "3 hooks, ONE idea: on-screen text ≤6 words · first frame · first line". STR §CM-HOOKS 1 |
| 10 | Great hooks open loops beyond the topic | CM §CM-FORMATS 1: "opening a loop past the topic". STR §CM-HOOKS 1: "Each opens a loop bigger than the topic." |
| 11 | Past-client form: where they found you · the first piece that made them take you seriously · the last piece before booking · why then · hesitations · why you | Covered · RES §CM-RESEARCH-PLAN R2 2: "Where did you first come across me? · What first post or moment made you take me seriously? · The last thing you saw before you messaged, and how sure were you by then? …" |
| 12 | The same form's "how convinced were you before the call?" | Now covered · RES §CM-RESEARCH-PLAN R2 2: "The last thing you saw before you messaged, and how sure were you by then?" |
| 13 | Route the answers: first-serious → top, last-before-booking → middle | STR §CM-IDEAS 1: "what first made them take the coach seriously → reach; the last thing before they messaged → trust; what almost stopped them → objections" |
| 14 | "Five whys" with favourite clients | RES R2 3: "FIVE WHYS WITH A FAVORITE CLIENT" |
| 15 | Mirror the buyer's exact words in every hook and script | INS DAY 0 6: "≥70% their words". CM §CM-MAP KEYWORD. STR §CM-HOOKS 2: "a buyer's line word for word" |
| 16 | Three reasons to admire you that only you combine = your mechanism / moat | Now covered · STR §CM-SEASON 1, week 1: "the mix only they bring (when known: the 3 things clients admire, §CM-CHARACTER-DEEP 2) shown in a scene" |
| 17 | Lean into ONE extreme trait | STR §CM-CHARACTER-DEEP 2: "ONE extreme trait to lean into". STR §CM-CHARACTER-SCENES 3 |
| 18 | Show, don't tell | STR §CM-CHARACTER-SCENES 1: "Never "I'm honest" … a scene shows it". STR §CM-HOOKS 4: "never say "with proof"" |
| 19 | Objection mining: call transcripts → objections → limiting beliefs → middle and bottom pieces | RES R2 4: "objections ranked by people · under each, the belief holding it … → one piece shifting it before the call". STR §CM-SEASON 2 |
| 20 | "An objection on a call = content failed to do its job" | RES R2 4: "("content failed here")". RES R6 1 |
| 21 | Swipe file: save what moved you emotionally and 10× standouts | Now covered · STR §CM-IDEAS 1: "none saved yet → once, one line above NEXT: "When a post hits you hard, or does far better than that account usually does, send me a screenshot. I keep its shape, never its words."" · CM §CM-LIKED 4-5 |
| 22 | Remix a proven format with a twist | CM §CM-LIKED 7: "2+ of topic, stance, format, platform differ" |
| 23 | "If everyone goes left, go right" | CM §CM-MONTH Your angle: "EVERYONE SAYS … NOBODY SAYS … YOU CAN SAY". STR §CM-IDEAS 1: "the gap" |
| 24 | Hard-to-copy topics are a moat | STR §CM-IDEAS 5: "Hard to copy beats easy" |
| 25 | Format: the "I made it" moment | Now covered · STR §CM-CHARACTER-SCENES 1: "a milestone (the day it first worked: where they were, who they told, what was said; never the money as the hook)" |
| 26 | Format: paycheck / spend breakdown | STR §CM-CHARACTER-SCENES 1: "a choice (what they spend on, what they won't)". CM §CM-CHARACTER-LITE Talk 2: "rituals, spending" (no money flex, by design) |
| 27 | Format: client decision breakdown (the top converter) | STR §CM-SEASON 1, week 3: "a client decision broken down". STR §CM-LONG 3. CM §CM-POSTS 7: "Case: each decision → what changed → result" |
| 28 | Format: one-on-one session breakdown (long) | STR §CM-LONG 3: "a live consult". STR §CM-LONG-INTRO 2: "CLIENT SESSION" |
| 29 | Format: mastermind / event clips | Now covered · STR §CM-LONG-CUTS 1: "A talk, workshop or group call they already recorded is cut the same way; everyone heard or shown OK'd first." · STR §CM-IDEAS 6 |
| 30 | Capture prompt: "what did you do this week that was interesting?" | STR §CM-WHAT-TO-SAY 1: "Something happened this week: a client call, a DM, a question, a win, a mistake". CM §CM-TALK 2 |
| 31 | Zone-of-genius capture (record them while they're in flow) | CM §CM-TALK 1: "answer out loud, like telling a friend", plus the re-say pieces. STR §CM-LONG-CUTS |
| 32 | Format ranking for consultants (talking head, story and events at the top; trend audio and street interviews at the bottom) | Now covered · STR §CM-IDEAS 6: "Form, when free to pick, best first: to camera with a story · a moment from a real session, talk or group call … · last, and only if asked: voice-over, green screen, trend audio, street interviews" |
| 33 | Credible value: what only you can say | STR §CM-IDEAS 2: "only this coach could say it". INS SHIP CHECK 3: "a detail only they have" |
| 34 | Be the first to put free what others keep behind a paywall | Now covered · STR §CM-IDEAS 1: "what their field teaches only behind a paywall → their own version, free and in full, before anyone else (their method only…)" |
| 35 | Borrowed credibility | Now covered · STR §CM-HOOKS 3: "one line why listen (their fact: years in the work, people helped, where they've taught or been invited, someone known they've worked with and may name; never a brag)" |
| 36 | Packaging and positioning beat raw value; package first | STR §CM-PACKAGING 1: "Package first: the title before the piece" |
| 37 | Lower the guard ("nothing to sell you") | Now covered · STR §CM-LONG-INTRO 3: "No offer in this video: one line may say so ("No pitch in this one."), only if true." · LCH §CM-LAUNCH-LIVE 1, §CM-LAUNCH-POSTS 1 |
| 38 | Long-form first for high-ticket; most shorts come from long-form | Now covered · STR §CM-LONG 1: "after a month of posting (from week 3 when their offer is sold on a call: the long video does the trust work before it)". The Weekly Talk stays the default (DECISIONS) |
| 39 | Pre-production loop: past winners, objections, client answers → ideas → score → package → script → film → weekly review | STR §CM-IDEAS 1-4. CM §CM-NUMBERS. STR §CM-STRATEGY-REVIEW |
| 40 | Score ideas for reach and packaging before scripting | STR §CM-IDEAS 2: "the buyer stops and a friend would share it … a stranger gets it from ≤8 words" |
| 41 | Weekly review of what stood out | CM §CM-NUMBERS 3: "Top post" only with a board, 10+ same type, 2×+ usual |
| 42 | The founder only does ideas and recording; the rest is run for them | INS: "You are Content Machine: the coach's content department." CM §CM-TALK close |
| 43 | Pipeline board: idea → scripted → filmed → posted | BRD §CM-BOARD 1: "status (Idea → Scripted → Filmed → Posted)" |
| 44 | Titles with a specific number and a timeframe | Now covered · STR §CM-PACKAGING 2: "from {before} to {after} in {time}" · "{N} years of {topic} in {N} minutes (their own years)"; numbers only from the coach's facts (§CM-PACKAGING 3) |
| 45 | Title: "if I had to start over" | STR §CM-PACKAGING 2: "if I had to {get result} from zero, I'd do this". STR §CM-LONG 3 |
| 46 | Title: "avoid these N mistakes" | STR §CM-PACKAGING 2: "{N} mistakes {buyers} make with {X}" |
| 47 | Brackets: "(full breakdown)", "(just do this)" | STR §CM-PACKAGING 2: "(full breakdown)". STR §CM-PACKAGING 3: "the bracket removes an objection … or adds a bonus" |
| 48 | Thumbnail of 2-4 words that adds to the title | STR §CM-PACKAGING 4: "2-4 words that ADD to the title" |
| 49 | Lowercase, casual titles | STR §CM-PACKAGING 3: "casual case is fine" |
| 50 | Script and filter lines that weed out non-buyers | Covered · CM §CM-CTA-KIT 9 "Not for you if…" · STR §CM-STRATEGY 3 "NOT FOR". Long video now covered · STR §CM-LONG-INTRO 3: who it's for by stage, "never by worth" |
| 51 | Case-study title: "did X daily, nothing clicked… until" | Now covered · STR §CM-PACKAGING 2: "{client role} {did X} for {time} and nothing moved, until {one change}" |
| 52 | Case-study title: "from A to B in N days" | Now covered · STR §CM-PACKAGING 2: "from {before} to {after} in {time}: what {client role} changed (their OK'd record, its context in the piece)" |
| 53 | Compression title: "$X of knowledge in N mins" | Now covered · STR §CM-PACKAGING 2: "{N} years of {topic} in {N} minutes (their own years)"; never dollars |
| 54 | Problem + fix title: "you're wasting N% … (here's how to fix it)" | Now covered · STR §CM-PACKAGING 2: "your {effort} gets {what they see now} but no {what they want} (here's the fix)" (one shape with Matt Gray #7) |
| 55 | Inner-shift title: "I removed X, now I …" | STR §CM-CHARACTER-SCENES 2: "I {old way} for {N} years. It cost {X}. Now I {Y}." STR §CM-LONG-INTRO 2: "I stopped X and started Y" |
| 56 | Reinvent the case study: kill the boring interview | Now covered · STR §CM-LONG 3: "A client decision runs: their stuck moment, in their words → where they started → the belief they held → the decision that changed it → the steps → the result with its context → who it's for and who not; never a read-out interview" |
| 57 | Reaction / meta-breakdown: a viral piece → why it worked (one principle) → how you'd do it | Now covered · STR §CM-IDEAS 1: "something the buyer's world is already talking about (a well-known post, ad or brand move) → the one principle behind it → how a {buyer} would use it; in the coach's words, never the clip" |
| 58 | Behind the scenes of real work ("closing a deal live") | Now covered · STR §CM-CHARACTER-SCENES 1: "the work itself (prepping a session, answering a client; no client shown without OK)" |
| 59 | Story sequences that pre-sell and push viewers to long-form | Now covered · STR §CM-LONG-CUTS 3: "1 email or message and 3 story frames (§CM-MESSAGES 7) pointing to the long video" |
| 60 | Mid-video ask for a free resource | STR §CM-LONG 2: "The gift at about a third" |
| 61 | Comment keyword → automatic DM | CM §CM-CTA-KIT 1, 7: "Comment {KEYWORD} and I'll send you {gift}." |
| 62 | "By the DM they've decided; you're confirming, not selling" | Now covered · STR §CM-STRATEGY-REVIEW 3: "calls that start unsure … → next season's weeks 3-4 answer those doubts, plus the "before our call" message (§CM-SEASON 4); the aim is a call that confirms, not one that convinces" · CM §CM-MESSAGES 5 |
| 63 | Post-booking video so they arrive convinced | Now covered · STR §CM-SEASON 4: "Someone books a call → one "before our call" message: what the call covers, one OK'd client decision or their process, one thing to think over" (moved from the kit, which must not grow) |
| 64 | Content and revenue are one system; optimise for buyers, not views | CM §CM-NUMBERS 3: "Hands up first; views aside". STR §CM-STRATEGY-REVIEW 1 |
| 65 | Offer before content: one buyer, one thing | INS DAY 0 3: "guess the ONE buyer". CM §CM-SETUP 6: "Offer = the stream they want to grow" |
| 66 | Document, don't perform; connection beats expertise | CM §CM-TALK 2: "each a real scene". CM §CM-NATURAL 5. STR §CM-SEASON 1, week 2 |
| 67 | No views = a curiosity (packaging) problem, not a value problem | Now covered · STR §CM-STRATEGY-REVIEW 2, DROP: "Little reach on an idea buyers keep asking about: the packaging failed, not the idea; a new first line and on-screen words once (long video: §CM-PACKAGING 5), then judge." · CM §CM-NUMBERS 6 |
| 68 | Sell the result, not the vehicle | STR §CM-HOOKS 4: "Outcome over method". STR §CM-PACKAGING 3: "the viewer's result" |
| 69 | Volume compounds: one idea → many pieces; repackage winners | STR §CM-STRATEGY-REVIEW 3: "the 2 best pieces → return next month in a new form". STR §CM-LONG-CUTS. STR §CM-WHAT-TO-SAY 3 |
| 70 | Batch filming | CM §CM-TALK close: "Film the 4 shorts back to back, 1–2 takes each, about 20 min." |
| 71 | Give before asking ("value debt"); patient selling | CM §CM-WEEK 6: "≥3 gives per ask"; "DM or book → week 2+, only with proof". LCH §CM-LAUNCH-STEPS: "≥3 giving pieces before the first ask" |
| 72 | Analyse content instead of just consuming it | CM §CM-LIKED 4: "Shape: hook → beats → ask" |
| x1 | "Cut broke language"; say the price plainly | Now covered · STR §CM-SEASON 1, week 4: "the offer at its exact price, said plainly (no "just", no apology)" (moved from the kit, which must not grow) · CM §CM-CTA-KIT 9 "exact price" |
| x2 | Excluded by design: income-and-age flex titles ("$X at 20") | STR §CM-PACKAGING 3: "never income as the hook". STR §CM-HOOKS 5: "a money flex" |
| x3 | Excluded by design: be everywhere (daily long-form + daily stories) | CM §CM-WEEK 2: Lean ≤60 min a week (DIY coach) |
| x4 | Excluded by design: day-in-the-life vlogs | STR §CM-STRATEGY 3: "never the coach's lifestyle". LCH P4 "a week inside" only |

## Matt Gray (ideas used, names never)

60 rows: 56 ideas now covered, 4 skipped by brief or blocked by the don't-copy rules (#19, #30, #58, #60).

| # | Matt Gray idea (plain words) | Where it lives |
|---|---|---|
| 1 | Packaging comes before production: the title is written before the piece | OK · STRATEGY §CM-PACKAGING 1 "Package first: the title before the piece; the piece keeps its promise." |
| 2 | Write many titles, cut to a few, pick the best (solo scale, not 50-60) | OK · §CM-PACKAGING 1 "Draft about 20 silently; the best goes on the piece" |
| 3 | Retitle toward the viewer's outcome, never the creator's brag | OK · §CM-PACKAGING 3 "the viewer's result, never the coach's brag" |
| 4 | Exact, odd numbers beat round ones (real ones only), money written in full | OK · §CM-PACKAGING 3 "exact odd numbers only from the coach's own facts, never income as the hook"; METHOD §CM-LOCALE 5 |
| 5 | The bracket removes an objection or adds a bonus | OK · §CM-PACKAGING 3 "the bracket removes an objection ("without ads") or adds a bonus" |
| 6 | Lowercase/casual case is a style choice, not a rule | OK · §CM-PACKAGING 3 "casual case is fine" |
| 7 | Title shape library (how to…without, X is hard until, start over, N mistakes, situation call-out, views-but-no-clients, N levels, give me N minutes) | Now covered · STR §CM-PACKAGING 2: "if you're {the buyer's stage or situation}, watch this · your {effort} gets {what they see now} but no {what they want} (here's the fix) · the {N} stages of {X} … · give me {N} minutes and I'll show you the fix for {pain}" |
| 8 | Thumbnail words (2-4) add to the title, never repeat it; one picture idea (before→after number, calm face, the board) | OK · §CM-PACKAGING 4 "2-4 words that ADD to the title… never repeat it"; design spec SKIP by brief |
| 9 | Re-package an underperformer once, by a simple rule (no A/B at small scale) | OK · §CM-PACKAGING 5 "one under their usual views after 7 days gets a new title OR new thumbnail words" |
| 10 | Mirror opener: two concrete things the viewer did today | OK · §CM-HOOKS 2 "two things the viewer did today"; §CM-LONG-INTRO 2 |
| 11 | Contrarian / reframe opener ("Most X think A. It's B." / "You're not X, you're Y") | OK · §CM-HOOKS 2 "Most {buyers} think X. It's Y."; §CM-TEXT-FORMATS 2 "You're not lazy. You're unclear." |
| 12 | Volume-authority opener ("I've done X N times…") | OK · §CM-HOOKS 2 "I've {done X} {N} times. Only one thing mattered." |
| 13 | Scene and ritual openers; named rituals with day and time as content | OK · §CM-TEXT-FORMATS 3 scene; §CM-CHARACTER-SCENES 1 "a ritual (every Monday at 7)"; METHOD §CM-CHARACTER-LITE "a ritual or choice + why" |
| 14 | Restart hypothetical ("if I had to start from zero") | OK · §CM-PACKAGING 2; §CM-LONG 3 "if I had to start over" |
| 15 | Ruled-out opener ("Not A. Not B. Not C. It was D.") | Now covered · STR §CM-HOOKS 2: "the ruled-out list: "Not {usual fix}. Not {usual fix}. It was {their answer}."" |
| 16 | List hook = one exact number + one unexpected plain word, ending in ":" | Now covered · STR §CM-HOOKS 2: "a number with one plain word nobody expects ("{N} boring {habits} that {result}"), their real N and habits only" · §CM-TEXT-FORMATS 3 |
| 17 | Lines 1-3 do the work: curiosity → why listen → promise | OK · CM §CM-POSTS 1 "Line 2 re-hooks"; STR §CM-HOOKS 3 "one line why listen (their fact: years in the work, people helped, …; never a brag)" |
| 18 | Recurring series that return (age / years-in lessons, yearly re-runs, winners re-run) | Now covered · STR §CM-IDEAS 1: "series: a shape that drew hands up twice returns on a set rhythm (each quarter, each year in business, each client milestone) with what changed since, never the same text re-dated" |
| 19 | Borrowed authority (famous quotes, person and book studies, curation lists, a celebrity case per section) | SKIP · blocked: METHOD §CM-CHARACTER-LITE BORROWED; playbook §9 |
| 20 | Alarm hooks, profanity, income and lifestyle flex, showing cash dashboards | OK as blocked · §CM-HOOKS 5 "Never the whole hook: a money flex…"; §CM-EDGE BORROWED; §CM-MOMENTS 2 "no money flex" |
| 21 | List post: hook ":" → 2-5 word heads → one fact → quotable payoff; one-line paragraphs, no hashtags, ≤1 emoji, plain reading level | OK · §CM-TEXT-FORMATS 3 "each a 2-5 word head, one fact of theirs, a quotable last line"; METHOD §CM-LOCALE 1 |
| 22 | Story → principle as two roles → "steal this week" checks → time box → ask | OK · §CM-TEXT-FORMATS 3 "the principle as two roles… 'try it for 14 days'" |
| 23 | Five-line story: mirror → friction → realisation → shift → invitation | OK · METHOD §CM-POSTS 2 "their moment → the cost or their own flaw → what they saw → what changed → the invitation" |
| 24 | Problem/solution split; teach post with steps | OK · METHOD §CM-POSTS 7 "surprising claim → why the usual fix fails → their way in 3 numbered steps" |
| 25 | Humble line before the ask on number posts ("yours will differ, start small"); 2 things to watch | Now covered · STR §CM-TEXT-FORMATS 4: "one humble line in their words: where the numbers came from …, that the reader's won't match, and the smallest first step … 2 things to watch while trying it" |
| 26 | Cheat-sheet image: the image holds only the skeleton and reads alone when reshared; the story stays in the post | Now covered · STR §CM-TEXT-FORMATS 3: "an image, if any, holds only the hook and the item heads and reads alone when reshared; the story, their numbers and the ask stay in the post" |
| 27 | Carousel: words first, slide 1 the hook in big type, one message per slide, each a screenshot, last slide = this piece's gift + one word | OK · §CM-TEXT-FORMATS 1; METHOD §CM-POSTS 5 (10-12 slides per the founder digest, not his 8) |
| 28 | Carousel style presets (reflection with no ask, personal, event promo rarely) | OK in effect · METHOD §CM-WEEK 6 reach asks; §CM-SEASON 4; visual presets SKIP by brief |
| 29 | Newsletter: scene → lesson → method in parts → one resource → reply; one promo block; offer in P.S.; 6 subject formulas | OK · §CM-TEXT-FORMATS 2 "subject in buyer words: how I {result} (with {limit}) · I ignored {X} (it cost me {Y}) · {N} signs…" |
| 30 | X threads; the same post re-dated each year | SKIP · X not a default platform (METHOD §CM-LOCALE 4); re-dating blocked by §9 (series rule in Change 6 needs a real update) |
| 31 | Long-video open: contrarian → proof → mirror → shift → named plan → "even if" → loop → "let's go", first section by 0:45 | OK · §CM-LONG-INTRO 1-3 "the first section starts by 0:45" |
| 32 | Three opens: contrarian, story, client session (with consent) | OK · §CM-LONG-INTRO 2 "CONTRARIAN · STORY · CLIENT SESSION… Written client OK first." |
| 33 | Bridge line that sells the next section; open loop paid off at the end | OK · §CM-LONG-INTRO 4 "one bridge line sells the next"; §CM-LONG 2 "the last part pays off the loop" |
| 34 | Section closer: "your job at this step is…" | Now covered · STR §CM-LONG 2: "one line worth quoting, often "your job at this step is…"" |
| 35 | Quick self-test once mid-video (a few-seconds test) | Now covered · STR §CM-LONG 2: "Once, mid-video, a quick self-test for the viewer, as a statement: "If {X} takes you more than {a few seconds}, {Y} isn't there yet."" |
| 36 | A client line right before the last ask; end bridge to the next video by stage | Now covered · STR §CM-LONG 2: "one OK'd client line, if they have one, right before the one ask; the next video to watch, for a viewer a stage earlier or later" |
| 37 | Gift at about a third, offer at about two thirds, both at the end | OK · §CM-LONG 2 "The gift at about a third…; the offer at about two thirds, only if one exists" |
| 38 | Body shapes: steps, levels/stages, diagnosis + fixes, client session | Now covered · STR §CM-LONG 3: "the N stages (§CM-STRATEGY 6) · one diagnosis + 3 fixes" |
| 39 | Pick ≤3 formats and rotate them for good: change the input, not the structure | Now covered · STR §CM-LONG 3: "They keep 2-3 shapes and rotate them: each video changes the topic and the story, not the shape" |
| 40 | Video description in a fixed order; chapters named "Step n: {name}" | Now covered · STR §CM-LONG 5: "DESCRIPTION (YouTube, podcast), in this order: the gift line … · chapters "Step n: {the step's name}"" |
| 41 | One deep piece → many pieces; repurpose the winners, not everything | OK · §CM-LONG-CUTS 2-3; §CM-STRATEGY-REVIEW 3 "the 2 best pieces → return next month in a new form" |
| 42 | Positioning from three questions: who you're 5 years ahead of, what people already come to you for, what you're quietly intolerant of | OK · §CM-STRATEGY 1 "Who are you about 5 years ahead of?…" |
| 43 | Point of view run as a campaign: 3 big ideas, old way → new way, every piece ladders up | OK · §CM-STRATEGY 2 "each 'old way → new way'… every piece ladders up to one"; METHOD §CM-WEEK 1 |
| 44 | One known-for line, few topics, one main platform + email, repeated signature phrases (his 4-3-2-1, renamed) | OK · METHOD §CM-MAP KNOWN FOR / 3 TOPICS; §CM-LOCALE 4 "One main platform plus email."; §CM-VOICE 1 "5 phrases, verbatim" |
| 45 | Name your steps, rituals and models in your own words; one fixed meaning; same name on every surface | Now covered · STR §CM-STRATEGY 6: "NAMES … a plain name of 2-4 words from the coach's own words (a concrete thing + what it does), never ™, "system" or another creator's term … One name, one meaning" · CM §CM-MAP |
| 46 | Stage ladder of the buyer ("most stall at stage 2", "your job at this stage is…") as diagnosis and content spine | Now covered · STR §CM-STRATEGY 6 (the 4-5 stages, "most {buyers} stall at stage {n}…", "your job at this stage is…", DM reply 1's sorting question) · §CM-PACKAGING 2 · §CM-LONG 3 · §CM-LONG-INTRO 3 |
| 47 | Role vs role contrast | OK · §CM-TEXT-FORMATS 3 "the principle as two roles" |
| 48 | Common enemy; show the buyer their future self | Now covered · enemy: STR §CM-STRATEGY 2. Future self: RES §CM-RESEARCH-ROOT R6 1: "AFTER (an ordinary day once it's fixed, only lines they wrote)" |
| 49 | Monthly voice capture becomes a month of content; monthly self-review | OK · METHOD §CM-TALK (weekly, 5 scene questions); §CM-MONTH 1 "Monthly check"; §CM-NUMBERS 4 bets |
| 50 | Pain signals and dream signals in what the buyer sees, hears, feels | Now covered · RES §CM-RESEARCH-ROOT R6 1: "their words, 10-20 lines by pattern, split PAIN (what they see, hear and feel now) and AFTER …" |
| 51 | Outlier research (≥3× usual, last 6 months), idea bank from calls, brand filter | Now covered · RES §CM-RESEARCH-ROOT R4 F: "top 3 pieces of the last 6 months at about 3× that account's usual views or comments, counts as shown" + USE "standouts → title and hook shapes (§CM-PACKAGING)" · STR §CM-IDEAS 1-2 · CM §CM-LIKED 5 |
| 52 | Gift named after this piece's result; the ask closes the loop; one trigger word per asset; DM delivery | OK · §CM-SEASON 4 "the gift named after THAT piece's result… Each ask closes the loop"; METHOD §CM-CTA-KIT 1, 7; LAUNCH §CM-LAUNCH-MESSAGES 1 |
| 53 | Diagnostic gift: a ~10-minute self-scored check with "your first gap", feeding qualification | Now covered · STR §CM-SEASON 4: "a 10-minute self-check, 5-10 yes/no lines in buyer words, then "your first gap: {step}" … the gap they send back answers DM reply 1's sorting question; no line promises what fixing it will earn" |
| 54 | CTA mix ≈ 60% gift / 20% direct / 20% none or share | OK · §CM-SEASON 4 "most pieces offer the gift… about 1 in 5 asks for a message or call" |
| 55 | Judge pieces by money and applications, not views | OK · METHOD §CM-NUMBERS 3 "Hands up first; views aside."; §CM-STRATEGY-REVIEW 1 |
| 56 | Funnel: gift → follow-up → call → offer, with a sorting question | OK · METHOD §CM-MESSAGES 5 "ONE question sorting buyers from browsers" |
| 57 | 5-day welcome after the gift; workshop show-up with real deadlines, short replay | OK · LAUNCH §CM-LAUNCH-MESSAGES 6 "AFTER THE GIFT, 5 messages in 5 days"; §CM-LAUNCH-LIVE 2 |
| 58 | Apply page with 3 questions, routing, pre-call videos, multi-step opt-in, tracked links | SKIP · closer and funnel ops; nearest: METHOD §CM-MESSAGES 5, §CM-MAP SIDE DOOR |
| 59 | Don't copy: his names, inflated value math, fake scarcity, income promises | OK · 1-INSTRUCTIONS CLAIMS "fake scarcity, cures, income promises"; LAUNCH §CM-LAUNCH-BRIEF 5 |
| 60 | Team-scale volume and testing (50-100 thumbnails, 3 posts a day, A/B), design specs | SKIP · team ops and design; METHOD §CM-WEEK 2 "Lean (default) ≤60 min a week" |

## Sources

- `founder-sources.md` (the Goh digest), `wf2-sooweigoh-luebben.md` part A, `wf8-mattgray-*.md` (playbook, YouTube, Instagram, LinkedIn/X, newsletter and lead magnets).
- The two audits behind this table (7 Oct 2026) listed each THIN or MISSING idea with the module edit that closes it; every edit is in `modules/{en,vn}/strategy|ideas|packaging|fmt-long|character|research.md`.
