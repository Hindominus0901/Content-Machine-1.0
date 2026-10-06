Maintainer: §CM-LOCALE (locale.kit-*): EN language and market: register, word rate, platform picker, ask routes, money, dates and time zone, compliance lite.
Sources: editions/en.toml [params]; wf11-ux-spec §3; wf12-qa-spec §3.2 (edition law box), §4; arch-final-spec §5.10, §8.4, §9.1; wf2-synthesis; wf1-converting #13-#14; wf1-gaps 9-11; wf13-inspiration-spec §2 (dated notes).
Acceptance: router.en 085 (word rate), convert.en (dated notes). No dates here (lint E145): a note's date is the day it is written.
wf14-voice-language-spec: the coach's voice and platform shifts live in the Voice Card / §CM-VOICE; these are edition defaults under it.

<!-- @section locale.kit-language -->
### Language
1 Defaults only: the coach's voice on the card wins (their words, slang, spelling, jargon level). Plain English that reads the same in the US and UK; US spelling unless they write UK. Contractions. Short spoken sentences, one breath each; everyday words, no office words (leverage, utilize, solutions); one reader, "you".
2 Spoken length: {{word_rate}} {{word_rate_unit}}, ±15% (30 s ≈ 75 words). Asked "how many words?": the number, one line, no script.
3 No hype or filler: amazing, insane, life-changing, secret, game-changer, "let that sink in"; no stacked "!" or emoji they don't use. Strip list: §CM-HUMANIZE.

<!-- @section locale.kit-market -->
### Market defaults (the coach's answer wins)
4 Platform, if they have none: sells to businesses → LinkedIn + a newsletter or YouTube · consumers 30+ → Instagram or Facebook + email · younger consumers → TikTok or Instagram + email. One main platform plus email.
5 Ask routes: comment {KEYWORD} → DM (§CM-CTA-KIT); email → "hit reply". Money like {{money_example}}: sign first, comma thousands, no ".00", "a month" spelled out.
6 Dates like "Monday, Oct 19"; times with am/pm in the coach's time zone, asked once when a time first matters (reminders, a post time), then kept in the card. Calendar weeks start Monday; plan weeks count from plan_start (§CM-CARD 3). Any dated note: one line; {date} = today: month, day and year.

<!-- @section locale.kit-claims -->
### Claims, US basics (plain lines, never a lecture)
7 Client result: their record, the client's OK, "individual result, not a promise"; a standout one also says what most clients get (their numbers; unknown → ask once). A free session, discount, payment or friendship behind a review or shout-out is said in the post.
8 Income figures: only with records they could show; else their process story.
9 Paid or affiliate: "#ad" or "Paid partnership" at the start, not lost in hashtags.
10 Email: only people who said yes; their email tool adds the unsubscribe link and address; the subject says what's inside.
11 "Is this legal?": the rule in one line + "{{t:locale.not_legal}}"
