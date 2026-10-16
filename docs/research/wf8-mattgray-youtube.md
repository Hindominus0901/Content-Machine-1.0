# Matt Gray YouTube sweep: brief for Content Machine 1.0

**How I got the data.** The handle in the task, `@matt_gray`, points to a different channel (a music upload). His real channel is **https://www.youtube.com/@realmattgray**, with 291K subscribers as of 2026-10-05.

- **Titles and view counts** come from the channel's Popular and Latest tabs, scraped on 2026-10-05.
- **Descriptions and chapters** come from watch pages, fetched through the r.jina.ai proxy.
- **Thumbnails**: I looked at 19 of them directly (i.ytimg.com maxresdefault).
- **Transcripts**: YouTube captions are blocked from this IP. His podcast, *The Matt Gray Show* (RSS: https://anchor.fm/s/d9770d10/podcast/rss, 170 episodes), carries the same audio as the YouTube videos. Durations match within 1 second, and the transcribed content matches the YouTube chapters. I transcribed the first 55–95 seconds of 29 episodes with Whisper (base.en). I also scanned 7 full episodes for section markers and CTAs, and transcribed EP142 (his packaging system) in full.
- Machine transcription makes small errors, for example "Founder West" or "Foundruss" for "Founder OS".
- Tags used below: **[V-audio]** = verified from audio, **[V-page]** = verified on a YouTube page, **[INFERRED]** = my inference, **[UNVERIFIED]** = not checked.
- One file was written by mistake: an early curl saved a temporary copy of the wrong channel's page to the session scratchpad (`mg_videos.html`). No project files were created or changed.

---

## 1) Inventory

### 1a. Most-viewed videos (Popular tab, top 50)

| # | Title (verbatim) | Views | Length | URL id |
|---|---|---|---|---|
|1|how to work less (and earn more)|621K|12:40|YIm4R2RAzfQ|
|2|success is hard until you build systems like this|575K|13:55|iemuHxed0nY|
|3|how to force yourself to be consistent and do hard things|547K|12:56|-eS14mBhnhA|
|4|the psychology of building a brand everyone loves|463K|15:21|6V4y0AX69h4|
|5|How to Build a Profitable Personal Brand (In Just 30 Days)|406K|19:18|dn7x0Sr2IhY|
|6|how to build a profitable personal brand (in just 7 steps)|371K|14:18|iONQNwRHd7Y|
|7|how to BEAT the new LinkedIn algorithm in 16 minutes|287K|16:48|0H4uouOn7lI|
|8|how to grow from 0 to 100K followers (on any platform)|243K|21:13|0U_7KTXvWVY|
|9|how to start a business from nothing (do this first)|193K|20:39|i16XTiS6cOw|
|10|I’m 35. If you’re in your 20s or 30s watch this.|165K|31:21|Q7yqgltP4Ps|
|11|how I gained 468,000 LinkedIn followers|164K|26:46|EDJMrlk4xIw|
|12|business is hard until you design it like this|162K|30:27|CQVBR5oVc-A|
|13|how I gained 950,000 Instagram followers (copy this system)|151K|29:03|ciV-FH9zRnQ|
|14|How To Make Your Life Insanely Simple (In 6 Months)|148K|10:59|c7KlqF2eAaE|
|15|why 97% fail at business (6 mistakes to avoid)|146K|16:59|I2iAjBMcXYk|
|16|The 5 levels of business in 12 minutes|140K|12:38|uyeRi2Lc954|
|17|if you don’t understand Elon Musk, you don’t understand business|136K|20:04|9oRWxopIQ9o|
|18|Why Alex Hormozi Will Be a Billionaire in 3 Years|129K|1:22:46|9XUCWQ8Ka_I|
|19|how I helped Ali Abdaal create a $5M funnel|123K|16:30|afq4xMghd8I|
|20|If You Only Watch One Personal Brand Video, Make It This|121K|15:31|lRe3iKyAXQA|
|21|money habits I stole from 7 billionaires (that made me rich)|116K|16:19|tyOrpQelKUA|
|22|how to REINVENT your identity for 2026 (the COMPLETE life audit)|113K|30:53|jfk79DkNksw|
|23|how to make millions from content without going viral|107K|17:49|RwMtod7yfqA|
|24|If I Wanted to Build a Personal Brand In 2026, I’d Do This|103K|17:19|7KnIaB5GTDA|
|25|how to manage your time like a CEO|102K|16:43|9TLsmDBh6lU|
|26|how to get ahead of 99% of people with AI|102K|15:09|0O9R2xbZTYE|
|27|How Dan Koe Makes $4.2M and 98% Profit with No Employees|101K|53:41|D3SMpmJmLEY|
|28|copy this content strategy, it’ll blow up your business|94K|19:13|nJhTQpiuNow|
|29|social media is about to change forever. here's how to get ahead.|85K|16:36|99UKPcsiKF4|
|30|what Steve Jobs can teach you about business (that harvard can’t)|83K|21:57|geuturFMM3M|
|31|5 Levels Of Discipline (Most People Stop at Level 1)|82K|15:46|q7PGsuqjQdE|
|32|how to build a personal brand so magnetic they beg to buy|74K|18:03|L0hb2o3X7Dg|
|33|how I went from -$15k to $8.7 million (my story)|73K|13:20|1GMCTIo1HMU|
|34|The One Person Business, Reinvented|64K|15:53|JUZbDKDecn8|
|35|become addicted to discipline in 14 minutes|64K|13:44|Jp91F_Opl7E|
|36|The 1 Change That Made Ali Abdaal $5,000,000|63K|56:07|HLG9leMUE48|
|37|how i'd start and scale a profitable business in 2026|56K|18:07|GxR4JS5nE0U|
|38|how I build systems (so my business runs without me)|55K|15:01|uNqfRatc1hk|
|39|I built a complete “business operating system” using claude code|54K|19:02|3Bfx4osqbfE|
|40|you’d be richer if you relaxed|54K|29:54|5zf0NCq3sis|
|41|how to build a brand AI can't copy|53K|18:23|b1Z2nl9vIik|
|42|these 6 Al skills will get you ahead of 99% of people|45K|18:31|LHpS8lulAQc|
|43|how to build a profitable personal brand (my complete blueprint)|44K|40:57|qNdu19bwrT8|
|44|my honest advice to a 28 yr old millionaire (lessons every founder must hear)|42K|32:39|735Mpvrb84k|
|45|38 systems I use to run a 34-person company (without losing my mind)|38K|30:12|-Mh9j8XjQd4|
|46|give me 58 seconds and i’ll break the identity holding you back|37K|0:58|P1lsJ9C87Ko|
|47|I helped Sam Kolder turn his creative genius into a scalable business|35K|24:08|BDkA0xnVht4|
|48|give me 15min and I'll teach you how to make $1M with content|34K|14:27|aJjZGCiJhzo|
|49|if you're about to start a business, please watch this...|32K|43:18|5Fbfu7j45_c|
|50|how to build a personal brand so magnetic they beg to buy (a second, different video)|32K|23:49|k82KwZVEWEQ|

All URLs take the form `https://www.youtube.com/watch?v=<id>`.

### 1b. Latest 30 videos (Aug–Oct 2026)

View counts are shown where the watch page returned them:

- If you’re ambitious but feel lost, please watch this (9.7K, YO1NAuy5G9c)
- Social Media Is Hard Until You Make Hires Like This (7.6K, e03FXSvKFbE)
- How I’d Build an 8 Figure Business (If I Had to Start Over) (15.6K, cxCKL-d0LZw)
- This $6M Business Owner Asked Me How To Hit $10M With Content (17.4K, nSCOuKz7F7g)
- give me 14 minutes and I'll fix the reason your brand makes no money (12.6K, oeOyZo71zwU)
- How To Get Everything You Know Into Everything You Publish (ongt5tdwz38)
- How To Turn Your Passion Into a High Ticket Offer (-8J5MBHz_fU)
- Personal Branding Is Hard Until You Build Systems Like This (23.2K, 12MVv0PxFgI)
- The 7 Laws of a Personal Brand Everyone Loves (5.6K, OarEwyrcc68)
- If I Wanted to Build a Personal Brand, I'd Do This (19.4K, RMdcJt9gM7A)
- why grinding harder won't build you wealth (wSCsr4gN9ug)
- your goals keep failing until you run this meeting (SNgjjhQElq0)
- I built a content machine that runs itself with Claude Code (6.5K, 5_EGJ1pcRkU)
- How I gained 914,000 LinkedIn followers (and made $1.2M/month) (9.7K, Hd7zlV0sDXU)
- how to manage your health like a CEO (dY3c8YNe2Vg)
- I built a complete operating system for a $4M business (copy this) (iPBVAKDa7FA)
- how to build a personal brand so powerful people beg to buy (kCSV-WZEu9s)
- I built a social media machine for a $7M roofing founder (6.8K, WA3xMnN8kA0)
- how to become so magnetic your clients chase you (XWOsLExQeVM)
- if your content gets views but no clients, do this (I4WNDfPf1_Y)
- if you think like an artist, you will become impossible to ignore (NMQ8CkBXrSA)
- how I became consistently profitable (the founder OS code) (rkGLJybQDq4)
- why your content gets views but makes $0.00 (learn how to fix it) (3.0K, mUBomP0Kpcg)
- how to plan a whole month of content (in 7 steps) (6.3K, oOQQP5Yi6Yg)
- how I’m automating 97% of my business with AI (se4rp_VAUMk)
- if you think I have it “figured out”, watch this (6AAjWeffBdI)
- how to build a marketing team in 2026 (personal media company playbook) (5BDL8VHp2W0)

Takeaway: in 2026 most uploads get 3K–25K views. A few outliers reach 100K–140K.

### 1c. Other sources

- **Shorts tab** (48 titles, 262–1.6K views each). Examples: "Stop sending newsletters. Send this 9-day sequence instead", "Here are the 10 signs your business can’t run without you.", "Every $5M+ business runs on this exact system. Here’s why", "I get 80% of my leads from 2 platforms. here’s how I chose them". Shorts on YouTube are clearly not a growth lever for him [V-page].
- **Podcast feed** (https://anchor.fm/s/d9770d10/podcast/rss): 170 episodes mirroring the YouTube audio, EP1 (Jan 2023) to EP172 (Sep 19, 2026). The 2023 episodes are long guest interviews (Dan Martell, Neil Patel, Chris Do, Tiago Forte, Jay Abraham, Sam Ovens).
- **Founder OS Head of Video profile** (https://torre.ai/a5ba3bc1-2892-49c2-85cb-ff12ab2b0efa): "One shoot day, one month of content"; "100+ longform videos shipped"; packaging is owned end to end.

---

## 2) Patterns and templates

### P1. Title formulas

Stats over the top 60 titles:
- 72% start lowercase. Title Case came back in mid-2026.
- 37% end in a parenthetical.
- 53% contain a number. Only 10% contain "$".
- 30% start with "how to"; 10% with "how I".
- 30% say "you/your"; 32% say "I/my".
- 17% name a famous person.
- Median length is 10 words (range 4–14). Median 54 characters, max 77.

| Formula | Real examples | Template | Coach/consultant version |
|---|---|---|---|
|**A. How-to + parenthetical qualifier**|"how to work less (and earn more)" 621K; "How to Build a Profitable Personal Brand (In Just 30 Days)" 406K; "how to build a profitable personal brand (in just 7 steps)" 371K; "how to grow from 0 to 100K followers (on any platform)" 243K; "how to start a business from nothing (do this first)" 193K|how to [outcome] ([in just N steps / in N days / on any [X] / do this first / step by step])|"how to get 10 clients from LinkedIn (in just 30 days)"|
|**B. "[Domain] is hard until you [verb] it like this"**|"success is hard until you build systems like this" 575K; "business is hard until you design it like this" 162K; "Personal Branding Is Hard Until You Build Systems Like This"; "Social Media Is Hard Until You Make Hires Like This"; "your goals keep failing until you run this meeting"|[domain] is hard until you [build/design/run] [thing] like this|"sales calls are hard until you structure them like this"|
|**C. "How I [precise result]" + (copy this)**|"how I gained 468,000 LinkedIn followers" 164K; "how I gained 950,000 Instagram followers (copy this system)" 151K; "How I gained 914,000 LinkedIn followers (and made $1.2M/month)"; "how I went from -$15k to $8.7 million (my story)" 73K|how I [precise number + result] ([copy this system / and made $X])|"how I booked 47 discovery calls from one webinar (copy this)"|
|**D. "I built/helped/fixed X for a [$ size] [niche] founder"**|"I built a social media machine for a $7M roofing founder"; "This $6M Business Owner Asked Me How To Hit $10M With Content"; "how I helped Ali Abdaal create a $5M funnel" 123K; "I helped Sam Kolder turn his creative genius into a scalable business"; podcast-only: "fixing their $80K/month coaching offer to unlock $250K/month"|I [built/fixed] [system] for a [$ size] [niche] [founder/owner]|"I rebuilt a $40K/month dentist's referral system"|
|**E. Numbered levels/laws/steps**|"The 5 levels of business in 12 minutes" 140K; "5 Levels Of Discipline (Most People Stop at Level 1)" 82K; "The 7 Laws of a Personal Brand Everyone Loves"; "why 97% fail at business (6 mistakes to avoid)" 146K; "38 systems I use to run a 34-person company (without losing my mind)"|The [N] [levels/laws/systems] of [topic] ([most people stop at level 1])|"The 4 levels of a coaching business (most coaches stall at level 2)"|
|**F. Hypothetical restart: "If I wanted…, I'd do this"**|"If I Wanted to Build a Personal Brand In 2026, I’d Do This" 103K; "If I Wanted to Build a Personal Brand, I'd Do This"; "How I’d Build an 8 Figure Business (If I Had to Start Over)"; "how i'd start and scale a profitable business in 2026" 56K|If I wanted to [goal] in [year], I'd do this|"If I had to rebuild my consulting practice from zero, I'd do this"|
|**G. Identity call-out + "watch this"**|"I’m 35. If you’re in your 20s or 30s watch this." 165K; "If you’re ambitious but feel lost, please watch this"; "if you're about to start a business, please watch this..." 32K; "if your content gets views but no clients, do this"|If you're [identity/situation], (please) [watch/do] this|"If you're a coach stuck at $10K/month, please watch this"|
|**H. Time-boxed fix: "give me N minutes"**|"give me 14 minutes and I'll fix the reason your brand makes no money"; "give me 15min and I'll teach you how to make $1M with content" 34K; "give me 58 seconds and i’ll break the identity holding you back" 37K; "how to BEAT the new LinkedIn algorithm in 16 minutes" 287K; podcast-only: "If you can spare me 9 minutes, you'll get 10 years of your life back"|give me [N minutes] and I'll [fix/teach] [painful thing]|"give me 11 minutes and I'll fix why your offer isn't selling"|
|**I. Borrowed authority (a famous name)**|"if you don’t understand Elon Musk, you don’t understand business" 136K; "Why Alex Hormozi Will Be a Billionaire in 3 Years" 129K; "what Steve Jobs can teach you about business (that harvard can’t)" 83K; "money habits I stole from 7 billionaires (that made me rich)" 116K|what [icon] can teach you about [topic] (that [authority] can't)|"what Oprah can teach you about client retention"|
|**J. Contrarian / negation**|"how to make millions from content without going viral" 107K; "you’d be richer if you relaxed" 54K; "why grinding harder won't build you wealth"; "why your content gets views but makes $0.00 (learn how to fix it)"|why [common effort] won't [result] / how to [result] without [feared thing]|"how to fill your practice without posting daily"|
|**K. Superlative / "only one"**|"If You Only Watch One Personal Brand Video, Make It This" 121K; "copy this content strategy, it’ll blow up your business" 94K; "…(my complete blueprint)"|If you only watch one [topic] video, make it this|"If you only watch one video on pricing your coaching, make it this"|
|**L. Psychology / identity**|"the psychology of building a brand everyone loves" 463K; "if you think like an artist, you will become impossible to ignore"; "how to become so magnetic your clients chase you"|the psychology of [desired state] / how to become so [trait] [people] [chase you]|"the psychology of clients who refer you"|

### P2. Thumbnail system (19 thumbnails viewed directly)

**Rules he follows:**
- **2–5 words**, set in bold geometric sans. Mostly white lowercase, with a lime-green brand accent. Since 2026 the text often ends with a period.
- **The thumbnail never repeats the title.** It adds the emotional or curiosity layer. Examples:
  - "success is hard until you build systems like this" → **"10 minutes/day"** (laptop showing the 5-step framework dial)
  - "how to force yourself to be consistent…" → **"how to get addicted"** (3 panels: gym / notebook template / laptop)
  - "the psychology of building a brand everyone loves" → **"build a cult like brand"** (7 rainbow panels numbered "1 level…7 level", famous faces)
  - "The 7 Laws…" → **"one law matters most."** (same 7-panel rainbow device)
  - "how I gained 950,000 Instagram followers" → **"you’re posting wrong"** plus **"0 followers → 950K followers"**
  - "how to BEAT the new LinkedIn algorithm" → **"0 followers → 846K followers"** plus **"LinkedIn blueprint"**
  - "This $6M Business Owner…" → **"step 1 isn’t content."** (whiteboard, lime dashed circles)
  - "give me 14 minutes…" → **"$5,000/hour strategy."** (hand-drawn lime curve: audience → diagnosis → price → offer → hiring)
  - "How I’d Build an 8 Figure Business…" → **"$15,359,892"** (black on a lime box)
  - "If you’re ambitious but feel lost" → **"you’re not behind."**
  - "I’m 35…" → **"no one told you"**
  - "business is hard until you design it like this" → **"building a dream business"** (back to camera, facing a whiteboard)
  - "how to start a business from nothing" → **"start now"**
  - "0 to 100K followers" → **"just start"**
  - "how to work less" → **"work less"**, the one partial overlap
  - The 30-day personal brand video (406K) has **no text at all**: a lifestyle shot of a laptop on a beanbag by an infinity pool.
- **Visual devices:**
  1. Cinematic film-grain lifestyle frame + 2-word overlay + hand-drawn white arrow.
  2. Multi-panel progression ("$0 / $10K / $1M"; 7 numbered rainbow strips).
  3. Before → after numbers joined by a dashed arrow.
  4. Hand-drawn lime "journey curve" whose labeled nodes are the video's steps (niche, values, vision, voice, style, story, team).
  5. Artifact props: whiteboard, framework on a laptop screen, notebook template, a wall of printed frameworks, a phone showing his profile.
  6. "Named system" lockup: small "the 2-day" / giant caps "PERSONAL BRAND" / small "blueprint." in lime.
  7. Back-to-camera or over-the-shoulder shot of a board, which creates curiosity about what is on it.
- **Face**: calm, neutral or contemplative, often not looking at the lens. No shocked faces. Black tee, warm natural light, desaturated palette plus lime.
- **His own taxonomy** (EP142) [V-audio]: three validated styles are "panel thumbnails", "solo screen… with a bit of text", and "talking head with some sort of graph behind".

**Template:** [2–5 word emotional or contrarian claim that the title does NOT say] + [one device: before→after number / numbered panels / labeled journey curve / framework artifact] + [calm face or back-to-camera] + [one brand accent color].

**Coach version:** title "how to fill your coaching calendar in 30 days" + thumbnail "stop chasing leads." with a curve labeled offer → content → lead magnet → call → client.

### P3. Intro structure: the roughly 40-second open

Median time to "Step/Level/Law one" is about 0:40 (range 0:21–1:14) [V-audio]. The beats, in order:

1. **Contrarian or pattern-break line**
2. **Proof** (precise numbers)
3. **Mirror** (the viewer's current pain, in concrete behaviors)
4. **Named structure + promise**
5. **Objection removal** ("without ads / zero experience / without becoming a creator")
6. **Optional open loop or lead-magnet mention**
7. **"Let's get into it."**

Line-by-line breakdowns [V-audio, auto-transcribed]:

1. **how to work less (621K)**
   - Question setup: "If you thought of someone making 730K per month, how long would you guess they are working? Most would guess 12 to 14 hours a day."
   - Contrarian: "I'm doing the complete opposite."
   - Proof: "$9 million a year and only work four hours a day."
   - Mirror backstory: "When I was 22… 15 hour days… no control and no freedom."
   - Promise: "step-by-step approach to make more and work less."
   - Named structure: "four pillars of leverage."
   - Visualization: "Imagine total freedom. What do you picture?"
   - Preview with pacing: "We'll cover each of these in 60 seconds."
   - Credibility objection: "but first, why should you even listen to me?"
2. **success is hard until… (575K)**
   - Question + simplicity: "What if I told you that the only thing you need to get unstuck… faster than 99% of people is a simple 10-minute system?"
   - Transformation proof: burnout → "four hours a day."
   - Named structure + promise: "my simple five-step system… so fast it feels like cheating."
   - Step 1 starts at **0:21**.
3. **psychology of a brand (463K)**
   - Cinematic cold open with archival clips: "to everyone who's ever told anyone with a dream they can't. This video is for you."
   - Thesis: "Every iconic brand started with a founder that focused on a key principle."
   - Validation: "Anyone working on a big vision is going to get called crazy."
   - Proof: "studied these principles for the last 15 years."
   - Promise: "seven core principles so you can stop playing small."
   - Principle 1 at 0:40.
4. **30-day personal brand (406K)**
   - Mirror: "So you want to build a personal brand, but you don't know how… you're stuck with a low follower account and bad posts… This video is for you."
   - Confession: "One of my biggest regrets is not building a personal brand sooner."
   - Evidence: Tesla 30M vs Elon 187M; Spanx vs Sara Blakely; Virgin vs Branson.
   - Promise: "blueprint… in the next 30 days."
   - Proof: "used it on my own personal brand."
5. **7 steps (371K)**
   - Binary stakes: "Your personal brand will either make you money or waste hours and days of your time."
   - Reframe: "The question is no longer should you… but how…"
   - Proof with struggle: "took me nearly a decade to crack the code… both 10x."
   - Objection removal: "this isn't just about going viral or being famous."
   - Promise: "by the end of this video you'll know exactly how."
6. **LinkedIn algorithm (287K)**
   - Contrarian: "LinkedIn is one of the most underestimated platforms."
   - Proof: "846,000 followers in just 36 months, all without spending a cent on ads."
   - Asset reveal: "a deck of 80 slides… so you can hand this off to your team."
   - Realism: "didn't happen overnight."
   - Stakes: "we want to actually make dollars."
7. **0 to 100K (243K)**
   - Rapid proof montage: "LinkedIn… 272K, 14 months. X to 170K, 10 months. Instagram to 710K, 11 months. And here's today."
   - Named structure: "three-part system."
   - Objection removal: "zero audience, zero budget, and zero experience."
   - Audience-data mirror: "73.9% of you said you had fewer than 1,000 followers… congratulations… that's exactly where I started."
8. **start from nothing (193K)**
   - Direct mirror: "I know what your problem is. You think you have nothing."
   - Objection removal: "You don't need some assistant, some full-time filmmaker, an expensive office."
   - Named concept: "the founder-led business model."
   - Proof: "$850,000 a month."
9. **business is hard until (162K)**
   - Binary: "two kinds of businesses."
   - Mirror: "everything just starts to feel heavy. You've built a house of cards."
   - Empathy + proof: "16 years… studied more than 400 different businesses."
   - Named structure: "traffic, entry points, the math, the team, the real goals."
   - Social proof: "Thousands of founders come to me to install this."
10. **5 levels of business (140K)**
    - Contrarian: "Most people try to hustle their way to making millions."
    - Proof: "$13 million a year."
    - Diagnosis: "fail, not because they're lazy, but because they try to bring level one behaviors into a level five business."
    - Metaphor: "each level requires a death."
    - Promise, then Level 1 at 0:33.
11. **millions without viral (107K)**
    - Contrarian: "If you want millions of followers… you have to be boring."
    - Proof: "3 million followers… $700,000 a month."
    - Scope: "not the trends, not tactics, the underlying framework."
    - Bridge: "But first, you need to understand this," followed by the 100-year-old bestsellers analogy.
12. **If I wanted to build a PB in 2026 (103K)**
    - Objection removal as the opener: "You do not need every post to go viral or turn into an influencer…"
    - Identity call-out: "If your business is already working and your brand still depends on you… this blueprint was built for exactly where you are."
    - Promise: "complete two-day blueprint… without shooting content every day, without learning to edit."
13. **Personal Branding Is Hard Until…** (2026; this is literally his 5-line story framework)
    - Title restated.
    - Mirror: "You open the app five times to check if the post finally took off. You take one week off and the whole thing stalls."
    - Friction: "nearly made me want to quit."
    - Shift: "stopped treating my brand like a performance and started treating it like a machine."
    - Proof stack.
    - Named structure: "five systems."
    - **Open loop**: "at the end, I'm going to give you the final exam."
14. **7 Laws**
    - Clip quote cold open.
    - Question: "Why does everyone love these people?"
    - Seven one-line character teasers as open loops: "A fashion founder who films his factory floor… a barefoot music producer who says he knows nothing about music…"
    - Proof: "48,000 pieces of content… 3.5 million… 17,500 founders."
15. **packaging first** (EP142)
    - Contrarian: "Most people don't struggle with content because their ideas are bad. They struggle because their ideas are invisible."
    - Principle: "Attention happens before quality."
    - Promise: "why we generate hundreds of titles and hundreds of thumbnails for one idea."
    - **Lead magnet at 0:40.**

**Template:**
1. [Contrarian line: "Most people think X. It's actually Y."]
2. [Proof: precise number + timeframe + "without [feared cost]"]
3. [Mirror: 2 concrete behaviors the viewer does today]
4. [Shift: "Then I stopped ___ and started ___."]
5. "In this video I'll give you the [N]-[step/level/law] [named system]…"
6. [Objection removal: "even if you ___ / without ___"]
7. [Optional open loop: "at the end, the one question that tells you ___"]
8. "Let's get into it."

**Coach version:** "Most coaches don't have a lead problem, they have a trust problem. I booked 212 calls last year without ads. If you're refreshing your inbox after every post… In this video: the 4-stage referral system… even if your list is under 500… and at the end, the one question that predicts if a lead will buy."

**Founder-session variant** (whiteboard videos) [V-audio]:
- Open on the **guest's payoff quote**: "I think we've been in circles in a branch, and now you gave us the whole tree" (EP116); "My dream was to have 100k month" (EP70); "Oh, this is not gonna make sense" (roofing).
- Then the narrator's identity call-out: "If you're stuck at 50k…".
- Then a diagnosis: "Leadership is the cap on your success."
- Then the promise: "help my friend Manuela get to that next stage."
- Then the guest states the constraint.

### P4. Body structures

From chapter lists [V-page]:
- **Levels with persona names.**
  - Scrapper → Operator → CEO → Empire Builder → Icon.
  - Dreamer → Tinkerer → Beautiful Prison → Media Company CEO → Iconic Founder-Led Brand.
  - Consistency: Design the System → Become the System → Scale the System.
- **Steps.**
  - Personal brand: Niche of You → Values/Vision → Audience → Identity → Story → Content GPS → Support Team.
  - Zane session: map the money → apply page with four ways in → platforms → topics → every CTA points to a lead magnet → 9-email engine.
- **Days**: Day 1 (parts 1–3) / Day 2 (parts 1–3).
- **Laws/Principles/Systems**, each with a coined name: "One-Word Moat", "Five Year Mirror", "Generosity Algorithm", "Slack Test", "Disappearing Act", "Ship Messy Protocol", "One Domino Decision".
- **Phases** on a whiteboard: Traffic → Entry Points → Content GPS → Math → Goals.
- **Diagnosis + 3 fixes**: "Diagnosis / Fix 1: Price one hour / Fix 2: Ask one question / Fix 3: Make one hire".
- **Chronological documentary**: the 8-figure story.

Section-close pattern: "Your job at level two is to stop being the bottleneck" (EP133) [V-audio].

**Naming template:** [number or size word] + [concrete noun] + [system noun: Protocol / Test / Moat / Mirror / Algorithm / Decision / Act].

**Coach version:** "The Two-Call Close", "The Referral Mirror", "The 48-Hour Follow-Up Protocol".

### P5. Retention devices

All [V-audio] unless noted:
- **Section bridge teasers** that sell the next section:
  - "So now you know what to post, but System 3 decides whether that content gets ignored or spreads."
  - "Law three is where things are going to get a little uncomfortable."
  - "The next one is the law that almost nobody in business will admit out loud."
- **Open loop paid off near the end**: final exam at 0:29, paid off at about 7:04.
- **Quick test**: "When people think of you, what one word comes to mind? If you can't answer that in two seconds, you don't have a brand yet. You have an account."
- **Guess-the-number**: "100 reps… 10% better… how much better do you think? No. Not a thousand times… 13,800 times."
- **Forbidden reveal**: real dashboards with cash collected; "my team was like, are we sure we want to show this? But said, f*** it."
- **Movie or archival clips as analogies**: Moneyball; Jobs-era quotes.
- **One famous case study per section**: George Heaton, Rick Rubin, Casey Neistat.
- **Audience poll stats**: "73.9% of you…"
- **Customer testimonial clip** before the final CTA (7 Laws at about 11:07).
- **End-screen bridge**: "There's zero overlap with this one you just watched"; "if you're earlier in the climb, start with the map…".
- **Ritual sign-off**: "Welcome to the Founder Freedom movement" / "let's win together".

### P6. CTA and lead-magnet architecture

Minute marks [V-audio]:

| Video (length) | Lead-magnet CTA | Offer CTA | Ending |
|---|---|---|---|
| EP142 packaging (17:38) | 0:40, repeated 16:58 | book a call + apply, 17:05 | — |
| EP136 (18:02) | 0:27 ("snapshot exercise… after this video") | — | — |
| 5 levels of business (12:37) | 4:43 (37%), repeated 11:56 | apply / book call, 12:18 | next video 12:26, like/sub 12:34 |
| 7 Laws (11:55) | 5:37–5:49 (47%: "Profitable Personal Brand Playbook… completely free, link in description") | service pitch 7:17 (61%: "My team builds personal brands on these exact laws"); apply 11:29 after testimonial 11:07 | next video 11:35 |
| PB systems (10:17) | 8:59 (87%) | apply 6:54 (67%) | like/sub + next video 10:05 |
| Month of content (21:57) | 6:00 (27%, "content machine scorecard") | offer timeline 21:06 ("by day 7… day 30… day 60"), then apply | next video 21:48 |
| Roofing session (26:29) | — | newsletter mention inside the session 22:06; Founder OS 26:15 | — |
| Jan 2024 "work less" | — | — | no spoken CTA; ends on an aspirational summary |

So the CTA system clearly tightened between 2024 and 2026 [INFERRED].

**Lead-magnet names** follow [topic] + [asset type] [V-page]:
- Unstuck Playbook
- Consistency OS Playbook
- Iconic Brand Playbook
- Content Idea Machine ("100 content ideas in just 30 minutes")
- Personal Brand Template
- LinkedIn Growth Deck
- 5 Levels of Business Checklist
- Content ROI Reality Check
- Personal Brand Team Evaluation
- Content GPS Alignment Audit
- Tasteful AI Content Playbook
- The New LinkedIn Formula
- Profitable Personal Brand Playbook (the 2026 default)
- In the audio: idea-to-click exercise, content machine scorecard, founder dependency test

**Description template**, 2026 [V-page]:
1. Line 1: "Get [Lead Magnet] here".
2. Line 2: "Want to work with me?"
3. A **one-line hook**: "I had a video do 14 million views. Nobody bought anything." / "You take one week off and the whole thing stalls."
4. A 3–4 sentence summary that names the systems.
5. A closing aphorism: "Your business shouldn't get bigger while you get smaller."
6. Newsletter link, then the "$30K+/month? free workshop" link, then the careers link.
7. Chapters named "Step/Law/Level N: [Coined Name]".

In 2024 to early 2025 descriptions also listed **"Video title ideas (for the algo):"** with 4–6 alternate titles. Whether that helps search is [UNVERIFIED].

**CTA logic stated on LinkedIn** (EP121) [V-audio]: ask for a repost, ask for a follow, then offer a lead magnet "tightly coupled with the subject matter" ("Want my deep work checklist?"). Hook = first three lines: curiosity ("I just read about a study I can't stop thinking about") → data + identity ("Introverts are more effective leaders according to Harvard") → conventional wisdom to react against.

### P7. Packaging process, in his words (EP142) [V-audio]

1. Keep an idea bank (Google Sheet) built from sales calls, plus "outlier" references.
2. Research outliers in 1of10 with these filters: **≥3x outlier, ≥95K views, >5 min, last 6 months**. Track channels, including out-of-niche "aesthetic" ones. Save YouTube playlists for titles, thumbnails and editing.
3. Brand filter: "can we position this video effectively with what we're actually selling?" Check cash collected and applications per past video, by editor, category and format.
4. Write **50–60 titles**, shortlist **6** and rank them. Make **50–100 thumbnail concepts** across the 3 styles. Packaging is "80% of the importance"; "worth spending an extra 30 minutes" on a video that takes about 15 hours.
5. Test in YouTube Studio: best title + 3 distinct thumbnails. Retest when views per hour taper.
   - Example: "how to build a plan for 2026 you'll actually use" → "don't set a goal for 2026 until you watch this" (about 22% better); thumbnail text "stop wasting your year".
   - Example: the discipline video was flat for about 22 days, then took off after switching to a panel thumbnail with "how to get addicted". This matches the 547K thumbnail I viewed.
6. Use the "top 10 ranking" metric. Ranked 1–2 of 10: let it ride. Ranked 9–10 of 10: re-package. Watch for a flat or rising click-through rate.

### P8. Retitles and title franchises

**Evidence of retitling** [INFERRED]. Podcast episode titles (posted 0–4 days after the YouTube upload, with identical audio) differ from the current YouTube titles:
- EP34 "How I Work 4 Hours a Day (and Make $730,000/Month)" → "how to work less (and earn more)" 621K
- EP111 "Do THIS for 10min Everyday, It Will Be (Almost) Impossible to Fail" → "success is hard until you build systems like this" 575K
- EP107 "The power of delusional self belief (how to build a $1B brand)" → "the psychology of building a brand everyone loves" 463K
- EP121 "LinkedIn is about to change forever (and nobody even realizes)" → "how to BEAT the new LinkedIn algorithm in 16 minutes" 287K
- EP39 "How to Get 100K Followers in 90 Days (3 Part System)" → "how to grow from 0 to 100K followers (on any platform)"
- EP45 "How I Made $13.2M Starting From $0" → "how to start a business from nothing (do this first)"
- EP41 "How I Broke 6 Limiting Beliefs…" → "why 97% fail at business (6 mistakes to avoid)"
- EP103 "how to make profitable content for ANY business" → "copy this content strategy, it’ll blow up your business"
- EP172 "I Sold My Business for 8 Figures. Here’s What I’d Build First" → "How I’d Build an 8 Figure Business (If I Had to Start Over)"

The direction is consistent: from "I made $X" brag titles toward **viewer-outcome or psychology titles**.

**Title franchises** [V-page]:
- "how to build a personal brand so magnetic they beg to buy" was used on two different videos (74K and 32K). "…so powerful people beg to buy" was added in 2026.
- "I’m 35. If you’re in your 20s or 30s…" (EP76) was followed by an "…in your 30s or 40s…" version (EP110).
- "how to build a profitable personal brand" appears in 4 or more titles.

### P9. Format portfolio, in his words (EP140) [V-audio]

1. **Systems breakdowns.**
2. **Real systems demos** (screen share).
3. **Founder-mentor sessions** (whiteboard).
4. Vlogs only now and then ("few and far between… kind of entertaining").

His rules:
- "pick three content formats max and rotate them forever… Change the input, not the structure."
- SELL = **Story, Educate, List**.
- "how to or how I videos" are "consistently the most profitable."
- His top cash video "is like our 42nd most popular video… 100K plus of cash collected."

Earlier eras: 2023 guest interviews and famous-founder analyses (Hormozi, Dan Koe). In 2026, "I built X with Claude Code" demos.

---

## 3) What the Content Machine should copy

1. **A title-formula library** (A–L above), each with a template and a coach example. Require the skill to output **20+ titles**, shortlist 6, and generate a **separate 2–5 word thumbnail line that adds to the title rather than repeating it**.
2. **A thumbnail brief generator** using his 7 devices: before→after numbers, numbered panels, labeled journey curve, framework artifact, named-system lockup, back-to-camera board shot, lifestyle frame + arrow. Specify one brand accent color and a calm face.
3. **An intro script skill** that enforces the 8 beats: contrarian → proof → mirror → shift → named N-part structure → objection removal → open loop → "let's get into it". Hard cap: first section starts by 0:45. Include a founder-session variant that opens on the guest's payoff quote.
4. **A naming skill** for frameworks, sections and levels: persona levels ("The Scrapper…") and coined systems ("[N]-[noun] [Protocol/Test/Moat]"), plus a "Your job at this level is…" closer for each section.
5. **A retention pass**: write a bridge teaser between every section, one quick test, one guess-the-number, one forbidden reveal, a final-exam open loop, a testimonial before the CTA, and an end-screen line ("zero overlap").
6. **A CTA placement map**: contextual lead magnet at 0:30–0:45 or at 25–50%, offer CTA at 60–70%, lead magnet + apply in the last 60 seconds, then an end-screen bridge and a ritual sign-off. Lead-magnet naming = [topic] + [Playbook/Scorecard/Audit/Checklist/Template].
7. **A description template**: magnet line → work-with-me line → one-line hook → summary → aphorism → named chapters.
8. **A packaging workflow and post-publish relaunch checklist**: outlier filters (≥3x, last 6 months), brand filter ("does this sell what we sell?"), A/B test plan, the "top 10 ranking" rule for re-packaging, and a "franchise your winners" rule.
9. **A format constraint**: the client picks 3 formats max (breakdown / demo / client session). Metric = cash and applications per video, not views.
10. **Vietnamese edition** [INFERRED]: the structures carry over unchanged. Swap the borrowed-authority names and the $ figures for VN-relevant ones, and check that lowercase/aphorism styling works in Vietnamese. Untested.

---

## 4) Sources

- Channel: https://www.youtube.com/@realmattgray (Videos, Popular and Shorts tabs, scraped 2026-10-05)
- Watch pages for descriptions and chapters, form `https://www.youtube.com/watch?v=<id>`, for: iemuHxed0nY, -eS14mBhnhA, 6V4y0AX69h4, dn7x0Sr2IhY, iONQNwRHd7Y, 0H4uouOn7lI, lRe3iKyAXQA, OarEwyrcc68, 12MVv0PxFgI, YIm4R2RAzfQ, YO1NAuy5G9c, e03FXSvKFbE, cxCKL-d0LZw, nSCOuKz7F7g, oeOyZo71zwU, RMdcJt9gM7A, WA3xMnN8kA0, oOQQP5Yi6Yg, uyeRi2Lc954, RwMtod7yfqA, 7KnIaB5GTDA, mUBomP0Kpcg, 5_EGJ1pcRkU, Hd7zlV0sDXU
- Thumbnails: `https://i.ytimg.com/vi/<id>/maxresdefault.jpg` for 19 of the ids above (EDJMrlk4xIw returned 404)
- Audio transcripts: The Matt Gray Show RSS, https://anchor.fm/s/d9770d10/podcast/rss
  - Intros: EP34, 39, 43, 45, 47, 61, 70, 76, 80, 87, 91, 107, 111, 113, 116, 121, 128, 133, 136, 140, 142, 151, 158, 159, 163, 167, 170, 171, 172
  - Full or sectional transcripts: EP34, 121 (7:50–10:40), 133, 140 (5:30–11:15), 142, 158, 163, 170, 171
- Founder OS Head of Video profile: https://torre.ai/a5ba3bc1-2892-49c2-85cb-ff12ab2b0efa
- Apple Podcasts search API (to find the feed): https://itunes.apple.com/search?term=matt%20gray&entity=podcast
- Background only: https://favikon.com/blog/who-is-matt-gray-b2b-influencer, https://podengine.ai/podcasts/the-matt-gray-show