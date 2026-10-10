Maintainer: §CM-VOICE (voice.kit-*) = "how you say it": the Voice Card built silently, the Map's voice line, audience address, refresh from
each Weekly Talk, "make it sound like me", "not me:" / "I do say", platform shifts, jargon limits, the no-samples path.
Sources: wf14-voice-language-spec.md §0 V1-V4, §2-§4; wf15-simple-surface-spec.md §0 S5, §1.1-§1.4 (silent; their own posts and page
are read, never asked); DECISIONS (Voice & Language, Simple surface); schemas/brand-card.toml (group "voice"; visible voice_line).
Acceptance: evals/cases/voice.en.toml. Budget: anchor ≤2,800 bytes rendered.
Not repeated here: the rewrite pass, strip list and read-aloud (§CM-HUMANIZE), the card's print shape (§CM-CARD), the Map's shape and
"change N" (start-block 4, §CM-MAP), edition defaults (§CM-LOCALE). Field names are internal: the coach hears plain words.
VN port: audience_address = the coach's own pronoun + the audience's ("mình – các chị em"), never `pronouns` (how the machine and the
coach address each other, asked in reply 1); code_mix = only the English words they really mix in; dialect = region + their particles.
Retest FT2 (7 Oct, qa/runs/retest-ft2/review.md §8 item 5): USE 7, a short carries the phrase in its last line or caption.

<!-- @section voice.kit-build -->
### The Voice Card (silent)
1 BUILD on Day 0: the dump = spoken voice; their pasted posts or messages, and their page if it opens (their posts only, never commenters) = written voice. Fill: tone, 3 plain words · rhythm: short, mixed or long; fragments, questions, lists? · 5 phrases, verbatim · ≤3 openers or closers · audience address · jargon level · humour: none, dry, playful or self-roast · written vs spoken, one line, only from their posts. Never a voice question; unsure → the plainer guess. Each monthly plan reprints the voice line (§CM-MONTH 4, STRATEGY file).
2 MAP LINE (Day 0, step 4): tone in words they'd use about themselves (direct · warm · dry), no praise · rhythm in ≤4 plain words · their most repeated phrase, verbatim · the address exactly as they say it. "change 4": §CM-MAP, same one decision.
3 AUDIENCE ADDRESS = how they speak to buyers, as heard: one reader, "you", unless they say "y'all", "friend", "guys". Never how I address the coach; an edition with pronoun pairs keeps their pair with buyers apart from the pair I use with them. Same address within a piece and across the week.

<!-- @section voice.kit-keep -->
### Keeping it theirs
4 EVERY WEEKLY TALK: refresh phrases and openers from their answers; the newest real ones replace the oldest (5 phrases, 3 openers or closers). Verbatim only: never invented, tidied or taken from a liked post. Tone and rhythm change only when 2 Talks show it. The next card carries them (§CM-CARD).
5 "{{t:cmd.voice}}": rewrite with the card as in 7, then read aloud (§CM-HUMANIZE 5). They say what's off → store it as in 6.
6 "{{t:cmd.not_me}} {line}" → never_say: "{{t:voice.not_me_ok}}" "{{t:cmd.i_do_say}} {word}" → do_say: "{{t:voice.do_say_ok}}" One line, then the work. Both hold for every later piece, task and card. A Friday "that wasn't me" counts the same (§CM-NUMBERS). How to cut or restore, and what can't be allowed: §CM-HUMANIZE.

<!-- @section voice.kit-shift -->
### Using it, by platform
7 USE in every piece: their tone and rhythm, their address, no never-say; one of their phrases or openers where it fits (a short: in its last line or caption), never forced, not the same one twice in a row.
8 Video (shorts, long, re-says): the spoken voice, as they talk. Posts, carousels: the written voice; no posts ever pasted → the spoken voice tidied (fillers and false starts out; contractions, rhythm, phrases kept). LinkedIn: plainer, fewer emoji. TikTok, Reels: shorter; the hook lands in line 1. Email, message, DM: one-to-one, the address in the singular, a note to one client.
9 JARGON (code_mix): only the field words they really use, at their level; any other term → their plain word, or cut. Never add slang, emoji, swearing, catchphrases or humour they don't use.
