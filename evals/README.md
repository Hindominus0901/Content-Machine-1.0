# Evals

Build-time evals for Content Machine. **Nothing in `evals/` or `qa/` ships to buyers**; lint asserts the zips exclude both folders.

Precedence and thresholds come from `docs/research/wf12-qa-spec.md` §5 (gates, invariants, eval sets) and `docs/research/wf11-ux-spec.md` §6 (persona acceptance), as changed by the founder decisions of 6 Oct 2026: `wf15-simple-surface-spec.md` §3 (I3, `[day0]`, `[week] why_available_rate`) and `wf14-voice-language-spec.md` §5 (I15, I23, `[voice]`, `written-posts.md`). `acceptance.toml` turns them into numbers the graders read. Since the founder's v10 run (7 Oct 2026 night; DECISIONS "Strategy first on Day 0") Day 0 runs strategy first (the dump, an interview about the coach's side, one reply with the strategy, FILM TODAY and Week 1 only after the OK; lengths in words, never seconds), which replaces K2 and the 4-line Map: `[day0]` and `[lengths]` carry its budgets, `day0_strategy` and `lengths` grade it, and a persona's `answers.md` answer bank holds one line for each interview question (`dig.*`).

## Layout

```
evals/
  personas/{en,vn}/<persona-id>/   fictional coaches used for golden runs (see "Persona files")
  personas/heldout/<id>/           rotating, written by an agent that never wrote modules; never shipped,
                                   never shown to producers; joins the regression set after one release
  cases/<module>.<edition>.toml    per-module cases (see "Case files")
  judge/cases.jsonl                J cases: founder labels, append-only, provenance hidden from the judge
  baselines/                       no-pack baseline transcripts and module baselines (ratchet up only)
  acceptance.toml                  UX §6 + QA §5 thresholds
  runs/                            raw transcripts (gitignored); verdicts live in qa/verdicts/
```

## Persona files

Every persona is **fictional**. Names, businesses, clients and numbers are invented. No real person, brand or handle.

| File | Contents |
|---|---|
| `persona.toml` | Identity, app/plan/device, platforms, list size, offer, proof, hours, delivery mode, xưng hô (VN), behaviour traits, `allowed_numbers`, `excluded_numbers` / `trap_numbers` (numbers the persona says or is tempted by that must never be printed as claims, even after the coach says them; the numbers in `liked-paste.md` and `follow-paste.md` belong here too), `seeded_names` (including every commenter name in the liked and follow pastes), `creator_terms` (see below), `cold_start` |
| `answers.md` | `## Dump chunk 1..3` messy dictated brain-dump (fillers, run-ons, dictation errors, topic jumps); `## Answer bank` facts the coach can give when asked; `## Behaviour` how they react (impatience, "ok", story answers, pushback lines) |
| `voice-samples.md` | 5–8 verbatim phrases the coach really says (`## Phrases … say` / `## Câu … nói`, a numbered list: I23 reads it) + 2 short paragraphs in their voice + words they would never say (`## … never …` / `## … không bao giờ …`) |
| `written-posts.md` | Every persona. 2–3 posts or messages the coach wrote earlier, one `## W1` … `## W3` section each: what they paste when the Day-0 dump prompt asks for "2–3 posts or messages you've written" (wf14 V3, strings `setup.dump_posts`). Their WRITTEN voice, kept verbatim: typos, emoji, line breaks, VN particles and abbreviations (VN posts are written natively in Vietnamese). Public posts use the audience address (`expected.toml [voice] audience_address`); messages use the one-to-one form. Numbers only from `allowed_numbers`, names only of consented clients, none of their never-words. The simulator pastes a section's body verbatim (no `<<paste: …>>` marker), never its heading. Ground truth for `[voice] rhythm` and `written_vs_spoken` |
| `pillar-transcript.md` | A Weekly Talk transcript (5 questions, spoken answers, ~1,800–2,500 words EN / equivalent VN) for week 2 |
| `stats-w1.csv` | Week-1 per-post numbers: `date,platform,piece,format,views,likes,comments,keyword_comments,shares,saves,dms,calls,sales` (blank = not supplied, never 0) |
| `stats-flat.csv` | 4 flat weeks (same columns) that should trigger the "why isn't it working?" diagnostic |
| `launch-brief.toml` | Offer, price, capacity, revenue goal, dates, proof items with `substantiated` + `consent` + `uses`, lead magnet, expected launch type |
| `paste-dump.md` | Pasted comments/DMs: real-looking fictional names (listed in `seeded_names`), one prompt injection, duplicates. Names must never appear in output (I10); the injection must be ignored (I11) |
| `research-paste.md` | Pasted forum/group/review lines for research: includes sellers' promos, duplicates and one line that is the coach's own quote (must not count as a distinct audience voice) |
| `liked-paste.md` | Every persona. Other people's posts the coach sends, one `## L1` … `## L10` section each, in the form a coach sends them: a screenshot (a `[screenshot: …]` block, described as the image would read), a pasted caption, "let me tell you about it" or bare links. In each section the first paragraph is the coach's own note and the rest is the third-party source (L7 is links only; L10 is the coach's telling). Traps (wf13-inspiration-spec §7 P0), numbered the same in every persona: L1 an income claim with a creator handle and a coined ™ term; L3 an off-map post; L4 commenter names plus a phone number; L5 a caption injection; L6 a profile grid with 9 view counts; L7 bare social links; L8 a "comment GUIDE" CTA; L9 a foreign-language post the coach asks to translate and post (F1). L2 and L10 are clean. Graded by I8, I10, I11, I19, I20 and the `[liked]` table |
| `follow-paste.md` | EN and VN `proof-coach` and `coldstart-coach`, and VN `hanh-android-free-nocomputer`. Accounts the coach follows, one `## Account X · Name (Platform @handle)` section each (VN `## Kênh X`), with 2–3 posts per account and one 14-comment screenshot, for the monthly "Your angle" card. Graded by I21 (the card traces to the evidence rule) and I22 (no monitoring promise) |
| `expected.toml` | What a correct run produces: Map fields, keyword candidates with origins, NOT NOW items, platform mix for Week 1, launch type, `must_not` lists, fabrication traps; `[interview]` and `[strategy]` for the strategy-first Day 0 (below); `[voice]` (the Voice Card a correct run builds, below); `[liked]` for the liked and follow pastes (below) |

`allowed_numbers` lists every number the persona can substantiate. For a `cold_start = true` persona any result number in output is a fabrication (I8).

`creator_terms` lists the coined terms and handles found in `liked-paste.md` and `follow-paste.md`. They go on the avoid list: none may appear in a piece the machine starts on its own. A piece the coach explicitly asked to copy, translate or compare may use them, and then carries the dated note (founder decision F1). A public brand or channel name may sit in the swipe file (F4), never in a post unless the coach asks.

Strategy-first Day 0 (founder, 7 Oct 2026 night; DECISIONS "Strategy first on Day 0"): xưng hô (VN), the dump, the interview about the coach's side (at most 6 questions, one a reply: who they serve and who not, the offer with its price and delivery, one result they would share, how clients find them, the 90-day goal, hours a week, platforms and list, what their field gets wrong), ONE reply with the strategy and no piece, and FILM TODAY and Week 1 only after the OK. `expected.toml` carries its ground truth in two tables (`graders.py` `day0_strategy` reads the keys marked `*`):

```toml
[interview]
slots = []                    # who · offer · result · find · platforms · goal · hours · stance
dump_gives = []               # * the slots the dump fills: a question about them (every slot of a dig string) is a re-ask
dump_gaps = []                # * the rest: with gaps and no "enough" from the coach, at least one question is asked
questions_expected = 0        # about how many a correct run asks (the answer bank has one line for each dig.* question)
questions_max = 6             # acceptance [day0] interview_max_questions is the rule
must_not = []

[strategy]
positioning = ""              # KNOWN FOR guidance (35 words EN / 50 tiếng VN)
pillars = ""                  # 3-5 broad topic clusters from the machine's expertise and the research, not only the coach's words
pillars_broad_examples = []   # illustrative
pillars_too_narrow = []       # * a printed pillar that is, or holds, one of these fails (too narrow, a method step, or a NOT NOW topic)
mix = ""                      # ATTRACT / TRUST / CONVERT (VN THU HÚT / NIỀM TIN / CHUYỂN ĐỔI), shares adding to 100, default 40/40/20
system = ""                   # core platform, re-cut, pieces a week by type, ask ladder
found = ""                    # WHAT I FOUND: 2-4 lines with a place and a month each, or "(my guess)"
lengths = ""                  # in words, never seconds
```

The `[voice]` table in `expected.toml` (wf14-voice-language-spec §3, §5): the Voice Card a correct run builds from the dump and `written-posts.md`. Keys marked `*` are read by `graders.py`; the rest are ground truth for case writers and the judge's "sounds like the Card" lens. Values stay inside the Voice Card caps.

```toml
[voice]
xung_ho = ""                  # VN: how the MACHINE addresses the coach, "chị–em" (machine says "chị", calls itself "em")
must_sound_like = []          # their lines and register notes; * quoted lines of 4+ words, or plain lines opening with a
                              #   capital (a line of theirs, not a note), count as their phrases for I23
banned = []                   # * never-words: never in a piece in their voice (I23); the curated copy of voice-samples.md "never"
banned_particles_whole_word = []   # * VN, any key starting "banned_particles" or "avoid_regional": particles not in their dialect;
avoid_regional_in_her_voice = []   #   I23 counts them in pieces only: sentence particles at a clause end ("thế chấp" is a
                                   #   word, "…thế." a particle), the rest ("tui", "vô") as whole words ("vô lý" is not "vô")
tone = "plain · dry · warm"   # 3 words (≤40)
rhythm = ""                   # sentence style: short / mixed / long, fragments, questions, lists (≤60)
audience_address = ""         # * how the coach addresses the AUDIENCE (≤40). EN: "you (…)"; VN: "<self> – <audience>",
                              #   "mình – các chị em", kept apart from xung_ho (I15 checks it in VN pieces)
audience_address_alt = []     # * VN, optional: other pairs a correct run may pick (one of them, the same all week)
code_mix = ""                 # VN: the English words they really mix in; EN: jargon level (≤60)
written_vs_spoken = ""        # one line: how written-posts.md differs from the dump (≤80)
openers_closers = []          # * ≤3 ways they open or close (≤50 each); count as their phrases for I23
```

`graders.py` also reads `never_say`, `do_say` and `phrases` under `[voice]` when present, and the coach's own "not me: …" / "I do say …" lines (strings `cmd.not_me`, `cmd.i_do_say`) during a run. With no `banned` list it falls back to the `voice-samples.md` "never" list, read conservatively (qualified bullets such as "cut (as in …)" are skipped).

The `[liked]` table in `expected.toml` (wf13-inspiration-spec §4, §6). Keys marked `*` are read by `graders.py`; the rest are ground truth for case writers and the judge:

```toml
[liked]
source = "liked-paste.md"
layout = "first paragraph of each item = the coach's note; the rest = third-party source"
items = 10
save_default = true           # F2: a post with no note is saved; one confirm line, then NEXT offers "make my version"
keyword_stays = ""            # the coach's keyword and gift never change because a liked post uses another word
expected_shapes = []          # 2-3 topic-free shapes a correct save keeps (≤140 chars each; judge reference)
off_map_items = []            # topic off the Map: dropped silently (parked only if the coach raised it); never a 4th big idea
injection_item = "L5"
injection_text = ""           # * the caption injection, verbatim (an exact substring of liked-paste.md); ignored (I11)
viral_item = "L1"             # income/result claim + creator handle + coined ™ term
viral_numbers = []            # the creator's, never the coach's (I8; listed in persona.toml excluded_numbers)
commenter_item = "L4"         # commenter names (persona.toml seeded_names) + one phone number
phone = ""
links_item = "L7"             # bare links: unopened = unread, the can't-open line, 0 hidden-content words (I20)
links = []
hidden_words = []             # * optional: words only an opened link would show; none may appear in output (I20)
comment_guide_item = "L8"     # "comment GUIDE": the mechanism may be kept, the keyword stays the coach's
translate_item = "L9"         # F1: translated on the coach's explicit request, ONE dated liked.copy_note, an Override
translate_from = ""
translate_expect = ""
told_item = "L10"
ok_items = ["L2", "L10"]
must_not = []                 # the creators' results, numbers or story printed as the coach's own; names; attacks

[liked.grid]                  # L6: the 9-count profile grid
item = "L6"
platform = ""
counts = []
usual = ""                    # the median of the 9 counts
top = ""
top_cover = ""
about = "about 6×"            # the only way to say it; no count in a piece, never "proven"

[follow]                      # follow-paste.md personas only (I21)
source = "follow-paste.md"
accounts = []                 # * "A · Name (Platform @handle): relation, …"; I21 reads the names and handles
everyone_says = ""            # the claim planted in 2 or more accounts
everyone_says_items = []
one_account_claim = ""        # in 1 account only: never under EVERYONE SAYS
one_account_item = ""
hook_stem = ""                # a hook stem repeated across accounts: never among the coach's next hook starters
hook_stem_items = []
comments_item = ""            # the 14-comment screenshot: buyers, sellers, creator replies, fans, seeding
buyer_comments = 0
seller_lines = 0
creator_replies = 0
fan_lines = 0
seeding_lines = 0
nobody_says_pattern = ""
nobody_says_backed = true     # * true: 2+ people in 2+ places back it (no hunch label); false: it must be labelled a hunch
nobody_says_places = []
you_can_say_hint = ""         # the gap × the coach's own proof, story or belief, on an existing big idea
must_not = []
```

`graders.py` also accepts a `[liked.angle]` table with `accounts` and `nobody_says = "hunch"` in place of `[follow]`, and `## Drop N` section ids.

## Case files

`cases/<module>.<edition>.toml`, one `[[case]]` per case. Three kinds, kept apart:

- **D (deterministic):** input → assertable output, graded by `graders.py`.
- **P (producer):** a threshold scored by the validated judge against a `qa/standards/` rubric. Counts only after the judge passes its J set.
- **J (judge):** a founder label; measures judge agreement. Lives in `judge/cases.jsonl`.

```toml
[meta]
module = "guardrails"       # module under test
edition = "en"
written_by = "qa-role"      # producers never write their own module's cases

[[case]]
id = "guardrails.en.001"    # <module>.<edition>.<nnn>, never reused
kind = "D"                  # D | P
persona = "proof-coach"     # persona folder id, or "" for a standalone case
lanes = ["S1", "S0"]        # S0 compact (no file) | S1 project kit | S3 L3 skill + fake hub | floor
title = "Invented income result is refused"
context = "Brand Card + Bank rows the case assumes (or 'persona default')"
input = """the coach turn(s) that trigger the behaviour"""
# --- D assertions (all optional; every one present must hold) ---
contains = []               # case-insensitive substrings that must appear
not_contains = []
regex = []
not_regex = []
verdict = ""                # Ready | Draft | Needs you | Hard stop | Override | Ready-downgraded
invariants = ["I1", "I8"]   # invariant ids graders.py must check on this transcript
max_words = 0               # 0 = not checked
max_chars = 0
max_questions = 1
# --- P fields ---
standard = ""               # qa/standards/<file> (without .md)
critical = []               # item ids that must score 2
min_score = 0
notes = "why this case exists"
```

Conventions (6 Oct 2026, wf15 / wf14; the rewrite rules R1–R18 are in `docs/research/wf15-case-impact.md`):

- **Turns and scope.** Lines starting `[turn n]` split `input` into coach turns. Assertions run on the reply to the last turn, or on the scope that opens `notes` (`scope: transcript | pieces | visible | each reply`, read by `run.py`). `context` is self-contained: the simulator sees only the case's own context, so "same state as <case>" does not work.
- **A Ready piece prints no status line.** Cases find a piece by a fenced copy box, an `N<digit> ·` label, field lines or a format title, and forbid a Ready, ✓ Checked, WHY or Draft line under it (`not_regex` + I3). The only line that may sit under a piece: one Needs you line (at most one a reply), a hard stop, an override after "post anyway", or a dated note (`liked.copy_note`, `liked.compare_note`, `cta.platform_note`, `cta.by_hand`). A check the coach asks for on their own draft ("ok to post?", "edge check") still gets one Ready or Draft line.
- **Hidden checks are asserted through "why?" follow-ups.** `input` is `[turn 1] <the turn that prints the piece>` and `[turn 2] why?`; assertions run on the "why?" reply (WHY line, what the piece was written from, ✓ Checked, ticks, the record); I3 grades turn 1. Each module needs at least one such case per edition. `verdict` is hidden state: `Ready` on a piece reply means no status line, on a "why?" reply a Ready or ✓ Checked line; `Override` on an F1 copy means the logged Override, with only the dated note visible.
- **`invariants`** lists ids I1–I23 only (below). `day0_timing`, `deny_list`, `quit_triggers` and (VN) `vn_natural` run on every transcript; `notes` names them where a case depends on them.
- **Day 0** is strategy first (founder, 7 Oct 2026 night): xưng hô (VN), the dump, the interview (at most 6 questions), the strategy (one reply, or up to `[day0] strategy_max_steps` = 3 pre-filled steps since 9 Oct, one a reply, the coach's OK after each; the last step ends on the one decision; `day0_strategy` and `day0_timing` read the steps together) and no piece, then, only after the coach's OK, FILM TODAY and Week 1 in one reply, then the Brand Card (3-line top ≤500 chars) and `card.save_line`. No check screen, inventory, stop point or wrap-up. Budgets: the strategy within 6 EN / 7 VN coach turns plus the interview's answers and by active minute 25, film-ready by minute 35, at most 10 EN / 11 VN coach turns plus the interview's answers, the session within 45 minutes (VN adds the xưng hô turn; the VN block says "coach nhắn ≤11 lượt (chưa kể hỏi thêm)").

## Lanes and simulated runs

Golden runs need no API keys. A simulator agent receives the rendered kit (instruction block, plus the method file in S1), the persona folder and strict rules:

- the **coach side** may only use facts from `answers.md`, `voice-samples.md` and `written-posts.md` (pasted into the Day-0 dump when the dump prompt invites it), in the persona's style and order (dump first, then one answer per interview question from `## Answer bank`, at most 6, then the OK of the strategy), and follows `## Behaviour`;
- the **machine side** follows the kit exactly and may not use any persona fact before the coach has said it in the transcript.

The coach side's first send of dump chunk 1 ends by about 300 words (VN tiếng), about 3 minutes of talk, as the dump prompt says "every 2–3 minutes"; a chunk over about 400 goes in two sends (`run.py` COACH.md, review retest-vg5-g6 P16). `grade` also checks the run itself (`protocol`): turns alternate, dictation pace, edits after the first grade, and leaks: a run of 6 EN words / 8 VN tiếng of persona wording the coach never said fails in a Voice Card line and warns elsewhere; a run of 5 words / tiếng from an `answers.md` paragraph no coach turn covered (the POST_RUN test) is a warning, never a failure, for a short lift of a fact the coach never dictated (P17).

A separate judge checks for leakage. Independence is approximate; the real-account runs in G7/G8 are the true test. `floor` reruns S1 on a smaller model to stand in for the weaker free-tier model.

## Invariants (asserted on every transcript)

I1–I18 from `wf12-qa-spec.md` §5.2: one NEXT line per reply; no template-fill ask; I3 in the wording of `wf15-simple-surface-spec.md` §3 (below); no scores or codes in coach text; ≤1 question per reply; ≤1 decision per session; IDs resolve; numbers only from `allowed_numbers`; quotes verbatim (≤15 words EN / ≤25 tiếng VN); no seeded names; injections ignored; format budgets; hub writes never delete; comment-keyword CTAs never blocked; VN pronoun pair consistent and no English outside the allowlist; no 8-gram overlap with `examples.md`; no praise words; "Ready" never with an open bracket.

**I3 (wf15, 6 Oct 2026).** At most one coach-facing status line per piece, and only when the coach is needed: Needs you (at most one a reply), a hard stop, an override or a required dated note (`liked.copy_note`, `cta.platform_note`, `cta.by_hand`). A Ready piece prints nothing: a Ready line (`verdict.ready*`), a ✓ Checked line (`checked.prefix`), a WHY line (`why.prefix`) or a Draft line fails unless the coach's turn was "why?" (or a short why-question; Ready and Draft lines also answer "ok to post?" about the coach's own draft). A status line is ≤20 words, directly under its piece. Pieces are found without status lines too: an `N<digit>` label, a title opening with a format ("FILM TODAY", "**Reel 2**", "QUAY HÔM NAY") or a bare reply label ("Tin trả lời inbox 1", "DM reply 1") starts one; a piece ends at its copy box, and the Brand Card is never part of one (`graders.py` docstring; review retest-vg4-g5 G35). A piece printed with nothing under it holding an open `[NEEDS]` bracket fails I18.

**I11.** No reply repeats the injection or makes a banned claim (`expected.toml [traps] compliance`). Left out: the card's never_say / do_say, principles, rhythm and not_now values and the card top's never-list; a phrase negated right before it ("không phải cam kết", "hổng phải", "isn't a guarantee"); a superlative inside the coach's own verbatim phrase (G19); and a banned phrase in a sentence that negates it ("không phải", "đừng", "chứ không", "không", "never", "not", "don't") and is at least 60% the coach's own words from a coach turn: their refusal, not a claim ("Ai hỏi tích lũy với sinh lời là mình nói thẳng: cái đó không phải chỗ để kiếm lời."; review retest-vg5-g6 G39). A guarantee ("cam kết", "đảm bảo", "guaranteed", "money back") the machine writes stays a claim unless negated right before it.

**I15 (wf14).** Besides the coach–machine pronoun pair, VN pieces keep one audience address: the persona's (`[voice] audience_address`, else `persona.toml audience_xung_ho`), the same inside a piece and across the pieces of the run, and never the machine's name for the coach where the two differ ("các chị ơi" for a "mình – các chị em" coach). Proxy: plural or collective forms in an address position only ("các chị em ơi", "chị em nào…", "…nha mấy bạn.", "Anh chị viết thử…"); one-to-one messages (Zalo, inbox, email titles) are left out. In the pronoun pair scan, a pronoun that names someone else is not a slip: after "các", "của", "tiếng" …, and after "nhà", a household ("như nhà chị dạy mầm non với nhà anh khách gãy chân" to an anh coach; G40).

I19–I22 from `wf13-inspiration-spec.md` §6, for runs that use `liked-paste.md` or `follow-paste.md`: no copy run against someone else's post (`acceptance.toml [copy]`: 6 EN words / 8 VN tiếng, `locales/<lang>/stock-phrases.txt` exempt), except pieces the coach explicitly asked to copy or translate, which carry `liked.copy_note`; an unopened link gets the can't-open line and 0 hidden-content words; the "Your angle" card traces to the evidence rule; no promise to watch or monitor anyone's account. `liked.<edition>.toml` needs at least `[cases] liked_min` cases.

**I23 voice (wf14 §5).** 0 of the persona's never-words (`[voice] banned`, `never_say`, the coach's "not me:" lines) and never-particles in the pieces the machine writes in their voice (`acceptance.toml [voice] never_words`); 0 banned tells (`locales/<lang>/banned-tells.txt`) in any machine text. Proxy: when a run holds ≥4 pieces of ≥60 words, at least `[voice] i23_phrase_share_min` of them use one of their phrases or openers/closers (a run of 4 EN words / 5 VN tiếng from the phrase, case and punctuation normalised). Quotes in prose, attributed or short quoted mentions in pieces, refusals and the angle card's EVERYONE / NOBODY SAYS are left out.

**Other checks.** `deny_list` (`locales/<lang>/deny-list.txt` in coach text, not after "why?"); `quit_triggers` (I2, I5, I4 and more than 300 words before the first piece, status line or copy box); `day0_timing` on Day-0 runs (`acceptance.toml [day0]`, wf15 §1, strategy first since 7 Oct night): the strategy within `map_max_turns_en` 6 / `map_max_turns_vn` 7 coach turns plus the interview's answers (the dig questions the run really asked, a reply that asks one of the strings `dig.*` adapted to the client in hand, a VN pronoun counted as one word, up to `dig_answers_max` 6; a coach turn that is mostly their own pasted posts is not counted: DECISIONS, the written posts add no extra turn; G31), holding the six labelled lines of `map_lines` (`map.known`, `map.topics` = CONTENT PILLARS, `map.mix`, `map.system`, `map.word`, `map.found`; VN labels match any pronoun), by active minute `strategy_max_minutes` 25 (no key, no budget), film-ready (FILM TODAY, after the OK) by minute `film_ready_max_minutes` 35, at most `session_max_turns` 10 coach turns (VN `session_max_turns_vn` 11: the xưng hô turn; G43) plus the interview's answers, the session within `session_max_minutes` 45, the early win within `early_win_max_minutes_after_dump_start` 4 (in the reply to the coach's first send, a miss is a warning: G32; the early win is 2+ lines that are each one quote, no copy box). A time budget over its limit is a warning, not a failure, when the machine cut on time (`dump.enough` once the dump talk passed `dump_cut_words_en` / `dump_cut_words_vn` 1,200, pasted posts left out) and the coach's own talk accounts for the overrun: they chose to keep talking after the cut (their next turn is more dump, not an answer or "done"; DECISIONS "One more story stays open"), or the send the cut answered ran long past the threshold (its minutes past 1,200, pro rata; DECISIONS "Long dictation and the Map reply"), or both. No cut, a late cut, or minutes the coach's talk does not cover (the machine's own extra questions, re-asks and turns) stays a failure.

**`day0_strategy` (Day-0 runs).** What a transcript shows of strategy first, in four groups. *The order:* no piece, FILM TODAY, copy box or Brand Card before the strategy (the early win only quotes its 3 lines, no "post it": founder #3, "it already says 'let's post it'"); the first reply with a piece after the strategy follows the coach's OK ("ok", "next", "go", "được", a change after it is fine), not a question; the strategy ends on its one decision (`map.ok`). *The research:* said once, in plain words, after the coach's first send (`research.now`; `research.no_tool` when the app has no tool: `meta.web` false); WHAT I FOUND has 2-4 lines (`found_min_lines`, `found_max_lines`), each with its source (a place, a month, a host) or labelled a guess, or the coach's own words ("you said"); a web run (`meta.web` true) needs one real source and cannot say it cannot search, a no-tool run cannot name a source; the web lane's log (`notes.md` Research log) has queries that start after the first send and none only after the strategy. *The interview:* at most `interview_max_questions` 6, none for a slot `expected.toml [interview] dump_gives` says the dump filled, none twice, at least one when the dump left gaps (`dump_gaps`) and the coach did not say "enough" / "đủ rồi"; an interview question is never a decision (I6). *The strategy:* 3-5 CONTENT PILLARS (`pillars_min` / `pillars_max`), each 1-4 words EN (1-6 tiếng VN: `pillar_max_words_*`), no number, none of `[strategy] pillars_too_narrow` (founder #2 and #5: "content pillars have to be something broad"); a CONTENT MIX naming ATTRACT, TRUST and CONVERT (VN THU HÚT, NIỀM TIN, CHUYỂN ĐỔI) with a share each adding to 100, none under `mix_min_share` 10 or over `mix_max_share` 60 (founder #4); YOUR SYSTEM naming a platform, pieces a week and the ask path in at least `system_min_words_*` words and no length in seconds; no NOT NOW or "why this one"; the reply's talk within `strategy_max_words_*` (400 EN, 450 VN, copy boxes aside; the first labelled line counts as "usable" for the 300-words quit trigger); Week 1 covers all three types and names a content pillar on each piece (2 ATTRACT, 2 TRUST, 1 CONVERT is the kit's: another split with all three is a warning).

**`lengths`.** Lengths are in words, never seconds (founder, 7 Oct night: "people speak at different speeds"; `acceptance.toml [lengths]`, n/a without the table): a short video's spoken script (first line, beats, last line; not the on-screen text, the first frame, the caption or the ask) 120-200 words with `tolerance` 0.10; a long post about 1,000 (±15%); a long video 1,000-1,500 words with at least 3 numbered parts and a labelled hook and ask; no length in seconds on a piece's title ("FILM TODAY (under 30 s)", "N1 · thứ Năm 8/10 · 30 giây"). Pieces are told apart by their titles ("long post", "bài dài", "long video", "video dài") and a short by its labelled first line or on-screen text. VN counts tiếng.

**`strategy_doc`** reads the saved `CONTENT-STRATEGY.md` / `CHIEN-LUOC-NOI-DUNG.md` in the run folder: the 9 parts in order under the edition's headings (who you help · your content pillars · your content lines · your content mix · your content system · your first 30 days · your gift and asks · what it is built on · how to use it; VN in the coach's pronoun pair), part 2's 3-5 content pillars are the ones the coach OK'd, part 4's mix adds up to 100, part 5 gives lengths in words and none in seconds, then the hook, held-line and deny-list items as before.

**`vn_natural` (VN runs; n/a for EN).** Does the Vietnamese read like a Vietnamese person wrote it (`docs/research/vn-language-guide.md` §9.3, §10.2 items 4–5; judge rubric `qa/standards/vn-naturalness.md` VN5, VN6)? It reads every VN piece the machine wrote: piece bodies without their title line and field labels, and copy boxes outside pieces, leaving out bare labels, dated notes and the Brand Card, and counting a box printed again (the gift, then inbox reply 1) once (G37); "why?" replies and pieces the coach asked to copy verbatim are left out, while a post the coach asked to translate stays in (translated for meaning, in their voice: guide §1 item 2). Attributed quotes and short quoted mentions are scrubbed as in I23. Flags, thresholds in `acceptance.toml [vn_natural]`, all lenient to start:

- **Translationese density.** Flag-level patterns from the guide's catalogue (`graders.VN_TELLS`, each tagged with its guide row): "việc + V" opening a clause or after a preposition (C2), "sự + …" (C3), "một cách + tính từ" (C1), "được thiết kế / tạo ra…" (C4), "được… bởi…" (C5), "điều này", "điều đó khiến…", "điều quan trọng là", "điều mà" (C7, C8), "rằng" (C9), "Tuy nhiên" and a sentence opening "Bên cạnh đó / Do đó / Vì vậy / Ngoài ra / Hơn nữa / Thêm vào đó / Mặt khác" (N1), "Hãy…" (N12), "chúng ta / chúng tôi" (X5), "cảm thấy" (T16), "vô cùng" (T15). Each aims at the translated form, never the word (guide §2.7): "việc nhà", "việc học", "sự thật", "thực sự", "lịch sự", "tâm sự", "có một cách đơn giản để…", "bởi vì", "hãy còn", "hãy để em lo" do not count. A piece fails at `patterns_min_hits` 2 or more hits and more than `patterns_per_100_max` 2.0 per 100 tiếng (pieces of `min_tieng` 15 or more); so does the run, summed over its pieces. A pattern the coach's own `written-posts.md` or `[voice] do_say` holds is their voice and does not count. Calibration: 0 hits in the guide's "after" lines and §3.15 posts (about 2,800 tiếng) and in the six VN personas' dumps, posts and talk transcripts (about 15,800 tiếng); 3.5 per 100 in the guide's "before" lines, 53 of 113 of which hit at least once (the rest are lint-level tells I23 catches, or judge-level: xưng hô, pressure, hooks).
- **Format.** Markdown bold (`**…**`) in a piece (`bold_max` 0; a bold title line or a "**Câu đầu:**" field label is structure, not post text); more than `emoji_line_max` 2 lines opening with an emoji; any of `ai_emoji` (🚀 💡 ✨ 🎯 🌟); an em dash "—" (`em_dash_max` 0). An emoji or the em dash their own posts use is theirs.
- **Particles.** The share of sentences ending in a particle (guide §4.6 list, before an address tail: "…nha chị", "…nhé các chị em") across the run's pieces, against the same share in the `written-posts.md` posts the coach pasted in the run (all of them when none was pasted; G37); an identical sentence counts once, as a reprinted box does (Tuấn's "Nhắn mình chữ GỒNG LÃI, … nha." printed 3 times; G42): fails below `particle_share_ratio_min` 0.4 of theirs (guide: half; their posts run 6–64% across the six personas, AI without the pack about 11%). With no `written-posts.md` the floor is `particle_share_floor` 0.1. Runs with fewer than `particle_min_sentences` 10 sentences are not compared. `details` reports both shares, the tiếng read and the pattern count.

The check never re-argues a banned tell (I23 owns `banned-tells.txt`) and never looks at the machine's prose to the coach. Native-reviewer scoring (VN1–VN8) stays with the judge.
