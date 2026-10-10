# Research brief: audience research and idea generation for Content Machine 1.0

*Method note: this session ran out of WebSearch calls, so I built the brief by fetching primary pages directly with WebFetch. I could not fetch two items, so they come from the books themselves and are flagged where they appear: Hormozi's $100M Leads content chapter and the DigitalMarketer Before/After Grid. The worked examples use one illustrative persona throughout: a leadership coach for first-time managers in tech. Its quotes are invented to show the format. They are not real data.*

---

## 1) Key insights

1. **Good ideas come from mining what customers say, not from brainstorming.** Copyhackers (Joanna Wiebe) mined 500+ Amazon reviews across six addiction books. One reviewer's sentence, "If you think you need rehab, you do," became the headline. It got ">400% more clicks… and >20% more lead-gen form submits" than the control. **[PRACTITIONER: one case study]** So the pack's first job is to collect exact customer phrases. Generating ideas comes second.

2. **Capture a fixed set of categories.** The quick version is three buckets: what prospects *love*, *hate* and *worry about*. The full version is six: problems in life, problems with current solutions, motivations, desires, features they love, and anxieties or hesitations. **[PRACTITIONER: Copyhackers]**

3. **AI can sort the data, but it can't do the listening.** Copyhackers' ChatGPT method analysed 86 reviews in about 28 minutes using a "rank complaints by frequency" prompt. **[PRACTITIONER]** Anthropic's own guidance is to put long data at the top of the prompt and the question at the end, which improves quality "up to 30 percent" in tests. It also says to have the model *quote first* before it analyses. **[DATA: platform docs]** That gives us a rule: every insight must carry a verbatim quote and a source label. Without one, the AI will make up customer language.

4. **Third-party Reddit tools are fragile.** GummySearch shut down on 11/30/2025 "to comply with Reddit's API policies, which forbid commercial applications." **[DATA]** The pack can't depend on third-party Reddit tools. It needs manual copy-paste, Google `site:` searches, and the AI's own browsing where available.

5. **On social platforms, outliers matter more than keywords.** 1of10 measures an outlier against the channel's own baseline. A video at 3x or more of the channel average "is worth noting," and 5x or more "is a strong signal." Confirm the pattern across several channels before acting. Outliers lead saturation by about 2–6 weeks. **[PRACTITIONER/vendor]** 1of10 also claims "70% of all YouTube views now come from the Homepage." **[vendor claim, unverified]** What you copy from an outlier is the underlying pattern (the format), never the surface topic.

6. **Platforms reward content that gets shared.** Instagram says Reels ranking predicts whether you'll "reshare, watch through, like, or visit the audio page." Explore leans much harder on how popular a post seems. **[DATA: platform]** So relatable and entertainment ideas should be scored on one question: would someone send this to a friend?

7. **Repeated exposure builds liking, up to a ceiling.** A meta-analysis of 208 experiments (Bornstein 1989) found the mere-exposure effect "typically reaches its maximum effect within 10–20 presentations" and can decline after that. Exposure can also *amplify* a bad first impression. **[DATA: lab studies, not social media]** This backs the founder's dominoes view. Ideas should be planned as clusters around a few core beliefs, with the format varied so people don't tire of them.

8. **You are already an expert to someone.** Ship 30's "2-Year Test" says you are an expert to the person who is 2 years behind you. Their phrase is "Obvious (To You), Non-Obvious (To The Reader)." **[PRACTITIONER]** This is the direct answer to "I don't know what to say."

9. **Structure multiplies ideas.** Applying the 4A framework to one topic bucket produced 24 ideas, and more than 100 across three buckets. Ship 30's breakout loop shows how a series grows from one winner: one "101" thread led to 15+ follow-up threads and "more than 2,000,000 views." **[PRACTITIONER]**

10. **Examples steer voice better than adjectives do.** Anthropic recommends 3–5 relevant, diverse examples wrapped in `<example>` tags. **[DATA: platform docs]** For a banned-words list, Wikipedia's "Signs of AI writing" catalogs the tells: *delve, tapestry, pivotal, underscore, testament*, "serves as", "not just X, but also Y", the rule of three, and too many em dashes. **[DATA: observational catalog compiled by editors]**

11. **A point of view matters more than a niche.** Dan Koe: ideas pass through your worldview ("philosophical refraction"). Treat short-form posts as your note-taking, and each week turn the best idea into a long-form piece. **[PRACTITIONER]**

---

## 2) Frameworks and templates

### F1. Research brief (Wiebe's four pre-mining questions)
**Source:** Copyhackers, Amazon review mining. **[PRACTITIONER]**

**How it works:** Answer four questions, in order, *before* collecting anything. The third question is the one that unlocks the rest. Your competition isn't only other coaches. It's also books, YouTubers, apps, DIY and doing nothing, and every one of those has public reviews and comments to mine.

```
WHO: [role/life stage] who [situation] and want [outcome]
WHAT SOLUTIONS THEY WANT: ...
WHAT THEY USE TODAY (incl. DIY, free content, "doing nothing"): ...
WHERE THOSE SOLUTIONS LIVE ONLINE (→ where to mine):
  books → Amazon/Goodreads reviews | YouTubers → comments | subreddits | FB groups
  podcasts → reviews & Q&A episodes | competitor IG/TikTok/LinkedIn comments
  MY OWN: DMs, sales-call transcripts, intake forms, onboarding surveys
```

**Example:** WHO: engineers promoted to manager in the last 18 months. WANT: a team that respects them, and to stop drowning. USE TODAY: management books, management podcasts, r/managers, asking their old boss. MINE: Amazon reviews of the top 3 management books, r/managers, comments on "new manager mistakes" YouTube videos.

### F2. VOC mining sprint (review mining plus AI extraction)
**Sources:** Copyhackers (method and search string), Anthropic docs (prompt structure). **[PRACTITIONER + DATA]**

**Steps (about 90 minutes):**
1. **Collect 50–150 raw snippets, best source first:**
   1. Your own sales calls, DMs and intake forms. This is the language people use when they're ready to buy.
   2. Reviews of the 3 best-selling books in the niche.
   3. Top-of-all-time threads in the niche subreddit.
   4. Comments on the top videos in the niche.
   5. Comments on competitors' posts.
   6. Facebook groups (manual search).
2. **Search strings:**
   - `site:amazon.com inurl:"product-reviews" "tired of" ~[keyword]` (Copyhackers). Swap in "frustrated by" or "wanting".
   - `site:reddit.com "[topic]" ("does anyone else" OR "I'm so tired" OR "how do I" OR "I wish")`
3. **Paste the text raw.** Wiebe: "paste their words – with as few 'summaries' or abstractions as possible."
4. **Run the extraction prompt below**, then save the results to the VOC Bank.

**VOC Bank columns:** `ID | Verbatim quote | Source label+link | Category (Pain/Desire/Fear/Objection/Failed solution/Identity/Trigger event) | Hell or Heaven | Awareness level | Frequency | Intensity 1–5 | Idea seed`

**Prompt:**
```
<raw_data>
[PASTE everything. Label each chunk, e.g. [Reddit r/managers], [Call #3], [Amazon 2★]]
</raw_data>

You are a direct-response researcher. Audience: [WHO]. My offer: [OFFER].
Using ONLY the raw data above:
1. First extract every quote expressing a pain, desire, fear, objection, complaint
   about an existing solution, identity statement ("I'm the kind of person who…"),
   or trigger event ("the moment I knew I had to change…"). Copy word for word;
   never paraphrase inside quotation marks. Keep the source label.
2. Group into: PAINS (hell now) | DESIRES (heaven) | FEARS about changing |
   OBJECTIONS to buying help | FAILED SOLUTIONS | IDENTITY | TRIGGER EVENTS.
3. Rank themes inside each group by frequency; show the count.
4. List 20 "money phrases": vivid, specific, emotional lines usable as hooks verbatim.
5. Flag anything surprising or that contradicts typical [niche] advice.
Output a table: Theme | Count | 2 best verbatim quotes | Source.
If the data does not support a theme, do not invent it. Mark any inference "[AI inference]".
```

### F3. Hell/Heaven and Forces map (the bridge to the three content types)
**Sources:** before/after state mapping as practised in direct response (similar to DigitalMarketer's Before/After Grid; I couldn't fetch that page to confirm its fields). JTBD "forces of progress" from Moesta and Christensen: push, pull, anxiety, habit. Awareness levels from Eugene Schwartz, *Breakthrough Advertising* (1966). **[PRACTITIONER]**

```
               HELL (today)                     HEAVEN (after)
HAS:           ...                               ...
FEELS:         ...                               ...
AVERAGE TUESDAY: ...                             ...
HOW OTHERS SEE THEM: ...                         ...
IDENTITY:      "I'm a ___"                       "I'm a ___"
PUSH (why today is unbearable):      PULL (what attracts them to the new way):
ANXIETY (fear of changing/buying):   HABIT (why they keep doing the old thing):
ENEMY (belief/practice/myth keeping them stuck — never a person):
AWARENESS MIX: unaware / problem / solution / product / most aware (% guess)
```

**How each part maps to a content type:**
- Hell moments and the average Tuesday become **Entertainment** (POV, "if you know you know").
- Push and pull become **Educational**.
- Anxiety, habit and objections become **Converting** (objection-busting, case studies, offer posts).

**Example:**
- Hell Tuesday: "back-to-back 1:1s, then I code at 9pm because I'm still the best engineer."
- Anxiety: "if I stop coding I'll lose my edge."
- Habit: "fixing it myself is faster."
- Enemy: the player-coach myth.

That one map produces three pieces:
- Entertainment: *"POV: it's 9pm and you're 'just quickly fixing' your report's PR again."*
- Educational: *"3 things a new manager must stop doing in week one."*
- Converting: *"My client was still coding 20 hrs/week as a manager. What changed in 30 days."*

### F4. Weekly outlier scan
**Sources:** 1of10 (thresholds and manual method), Sandcastles and ViewStats (tools), Dan Koe (X search operator). **[PRACTITIONER]**

**Steps (30–45 minutes, weekly):**
1. Track 10 creators: 5 in your niche, 3 adjacent ones (same audience, different topic), and 2 bigger general creators your audience follows. SparkToro's free report shows who an audience follows.
2. Sort each creator by "Popular" on YouTube. On IG, TikTok or LinkedIn, scroll their last 30–50 posts.
3. Work out the **outlier ratio**: post views ÷ the creator's typical (median) views. Log anything at 3x or more and prioritise 5x or more. My suggestion: where the typical figure isn't visible, use views ÷ followers as a rough stand-in.
4. Validate: only keep a pattern that shows up in at least 2 creators (1of10 says to "repeat across 10 channels").
5. Adapt it: keep the *pattern* and swap in your VOC theme, your proof and the angle they missed.

On X, use `from:[username] min_faves:1000` (Koe).

**Optional tools:**
- 1of10: YouTube only. Free plan has 60 credits a month; Pro is $89/month.
- ViewStats: YouTube outliers.
- Sandcastles: "top 1% outliers" across TikTok, IG and Shorts, from $39–49/month.

**Outlier Log columns:** `Creator | Link | Views | Typical | Ratio | Hook verbatim | Format | Angle | Emotion | Pattern ("[format] about [topic] for [who] using [device]") | My version`

**Prompt:**
```
<outlier>Creator typical views: [X]. This post: [Y]. Transcript/caption: [PASTE]</outlier>
<my_voc>[PASTE 5 VOC quotes with IDs]</my_voc>
Deconstruct why this outperformed: (1) hook verbatim + hook type; (2) the pattern
as a topic-free reusable template; (3) emotion/belief triggered; (4) beat-by-beat
structure; (5) what top comments ask that it didn't answer. Then write 5 versions
of the template for [WHO], each built on one VOC quote (cite its ID).
Do not reuse any sentence from the original.
```

### F5. Idea multiplier (topic × angle × format × hook)
**Sources:**
- Ship 30 for 30: Content Buckets (general, niche, industry) and the 4A framework. Its four types are *Actionable* ("how"), *Analytical* ("here are the numbers"), *Aspirational* ("yes, you can!") and *Anthropological* ("here's why": fears, failures, lies).
- Hormozi, *$100M Leads*, from the book; I couldn't fetch it online.
  - The hook is built from topic, headline and format.
  - Topic sources: far past, recent past, present, trending, manufactured.
  - Headline elements: recency, relevance, celebrity, proximity, conflict, unusual, ongoing.
  - Retain viewers with lists, steps and stories.

**[PRACTITIONER]** The widely shared "Hormozi content matrix" graphic looks like a community remix. I found no primary Hormozi source that uses that name.

**How it works:**
- **Topic** = a VOC theme, not a list of your expertise.
- **Angle** = one of the 8 angles below.
- **Format** = list, steps, story, POV skit, myth vs truth, before/after.
- **Hook** = a money phrase from the VOC Bank.

The arithmetic: 3 pillars × 8 themes × 8 angles × 3 formats = 576 combinations, from which you score and keep the top 30.

| Angle | Stem | Content type |
|---|---|---|
| Actionable | "How to [desire] without [pain] in [time]" | Edu |
| Analytical | "I reviewed [N] [things]. Here's what [finding]" | Edu/Conv |
| Aspirational | "[Client/past me] went from [hell] to [heaven]: 3 lessons" | Conv |
| Anthropological | "Why [audience] secretly [fear/failure]" | Edu/Ent |
| Contrarian/Enemy | "Stop [common advice]. Do [my belief] instead" | Edu/Conv |
| Relatable POV | "POV: [hell moment]" / "IYKYK: [shared memory]" | Ent |
| Proof | "Case study: [client], [number] in [time]" | Conv |
| Objection | "'[objection verbatim]': here's the truth" | Conv |

**Prompt:**
```
<voc_bank>[PASTE top themes + quote IDs]</voc_bank>
<belief_bank>[PASTE]</belief_bank>  <proof_bank>[PASTE]</proof_bank>
For theme "[THEME]" generate one idea per angle: Actionable, Analytical,
Aspirational, Anthropological, Contrarian, Relatable POV, Proof, Objection.
For each: working title ≤12 words using a customer phrase where possible;
content type (Educational/Entertainment/Converting); format; quote ID used;
proof/story ID used, or "NEEDS PROOF". Use no facts that are not in my banks.
```

### F6. Idea notebook and breakout loop
**Sources:** Dan Koe; Nicolas Cole and Dickie Bush (Ship 30). **[PRACTITIONER]**

**Daily capture (10 minutes):** keep one inbox note under four headers: *Noticed* (calls, DMs), *Consumed* (an idea worth stealing), *Believe* (something others don't) and *Happened* (stories).

**Remixing a stolen idea** (Koe's rule): "contemplate utility, apply it to your goals, rephrase from your perspective."
- Koe's example: Goethe's "architecture is frozen music" became "Books are paper sculptures. Writing is the clay and articulation is the chisel."
- Coach version: "What gets measured gets managed" becomes "What doesn't get said in a 1:1 gets said in the exit interview."

**Topic tree:** pick 2–3 core interests, broaden each to its market, then break it into topics and subtopics. Koe's target is to cover "this entire domain in 6–12 months."

**Breakout loop:**
1. Make noise.
2. Listen for signal.
3. Double down.
4. Turn one breakout into many: "Super of 1 is a Super of 9."
5. Repeat.

This is the dominoes mechanism in operational form.

### F7. Idea scoring
**Source:** my synthesis of the sources above; no single source proposes it.

Score each criterion 1–3:
- **Evidence:** VOC frequency and intensity.
- **Outlier proof:** the pattern already won elsewhere.
- **Proof-ability:** you have a story or result to back it.
- **Offer proximity:** 1 = general topic, 3 = an objection to your own offer.
- **Share trigger:** would someone send it to a friend? (the Instagram reshare signal).
- **Series potential:** can it spawn 3 or more follow-ups?
- **Ease:** can you make it in under 30 minutes?

The total is out of 21. Kill any idea that scores Evidence 1 *and* Proof-ability 1.

Report two sub-scores:
- **Reach** = share trigger + outlier proof + evidence.
- **Trust/Buy** = proof-ability + offer proximity + evidence.

The weekly plan picks the best ideas while enforcing a mix across the three content types.

### F8. Story, belief and proof banks, built through an AI interview
**Sources:**
- Ship 30's 2-Year Test questions: "What skills do you have today that you didn't have back then?" and "What were you struggling with back then that you no longer struggle with?"
- Koe on point of view.
- Matthew Dicks, *Storyworthy*, "Homework for Life": a daily habit of logging story moments. From the book; not fetched.

**[PRACTITIONER]**

**Bank schemas:**
- **Story:** `Title | Time (far past/recent/present) | Before → turning point → after | Emotion | Lesson | Pain theme it proves`
- **Belief:** `"Most [niche] people believe __. I believe __ because [story/proof ID]." | Enemy`
- **Proof:** `Client | Start (hell) | Result (number + timeframe) | Quote | Permission Y/N | Screenshot`

**Prompt:**
```
Act as a journalist building my Story, Belief and Proof banks. Ask ONE question at
a time; after each answer ask one follow-up for specifics (names, numbers, what was
said, what I felt, what changed). Cover in order: (1) the 2-Year Test; (2) the moment
I chose this work; (3) 5 client transformations with numbers and a quote; (4) 5 things
most people in [niche] get wrong + the enemy behind each; (5) 3 failures and lessons.
Every 5 answers, update the three bank tables. Keep my words; don't polish.
```

Tip: answer by voice dictation. Speech is closer to how the person sounds on video. **[PRACTITIONER]**

### F9. Voice capture
**Sources:** Anthropic prompting docs; Wikipedia's "Signs of AI writing." **[DATA: platform and editorial]**

**Steps:**
1. Collect 3–5 varied samples: best captions, an email, and a transcribed voice note or sales call.
2. Run the extraction prompt below to produce a Voice Card.
3. Load the Voice Card and the samples into every scripting session.

**Prompt:**
```
<examples><example>[SAMPLE 1]</example> … <example>[SAMPLE 5]</example></examples>
Analyze how I write/speak. Produce a Voice Card: sentence-length habits; phrases I
repeat (quote them); how I open and close; how I explain (analogies/stories/numbers);
humor; slang/profanity level; how I address the audience; things I never do.
Then 10 DO and 10 DON'T rules, each backed by a quote from my samples.
```

**Banned list (seeded from Wikipedia):** delve, tapestry, testament, pivotal, crucial, intricate, underscore, garner, vibrant, showcasing, "serves as/stands as", "not just X, but also Y", "it's not X, it's Y", reflexive rule of three, em-dash overuse, sprinkled boldface, and "Despite its challenges…" style conclusions.

---

## 3) What this means for the Content Machine design

1. **Build the research layer as a set of "banks" (files).** The `research/` folder holds:
   - `research-brief`, `voc-bank`, `hell-heaven-map`, `outlier-log`
   - `story-bank`, `belief-bank`, `proof-bank`
   - `voice-card`, `idea-bank`

   Every scripting and series skill reads these banks. If a bank is empty, the assistant runs the matching interview or worksheet before writing anything.

2. **The first session ("Day 0", about 2 hours) runs in a fixed order:**
   1. Interview (F8)
   2. Voice Card (F9)
   3. Research brief (F1)
   4. VOC sprint (F2)
   5. Hell/Heaven map (F3)
   6. Multiplier (F5)
   7. Scoring (F7)
   8. First series

   The deliverable is 30 scored ideas and one planned series on day one, so the user has an immediate win.

3. **Give every research step two modes.** In the "AI can browse" mode, the assistant pulls threads and reviews itself. In the "paste mode," the pack supplies search strings and labelled paste blocks. Paid tools stay optional. Nothing should depend on Reddit's API (see the GummySearch shutdown).

4. **Hard-code an anti-fabrication rule.** VOC quotes must be verbatim and carry source labels. Anything synthesised is tagged `[AI inference]`. Every idea must cite a quote ID plus a proof or story ID, or be flagged `NEEDS PROOF`. Prompts follow Anthropic's pattern: data first, quote extraction next, the question last.

5. **Generate ideas as clusters, never one at a time.** One VOC theme runs through the 8-angle matrix and naturally becomes a series: Entertainment (hell moments) → Educational (push and pull) → Converting (anxiety, objection, proof). This turns the founder's dominoes belief into a mechanism. The exposure research supports repetition but warns about wear-out, so the format should rotate.

6. **Idea bank schema:** `ID | Title | Quote ID | Theme | Angle | Type | Format | Awareness | Proof ID | Story ID | Reach score | Trust/Buy score | Series ID | Status | Results (views, ratio vs own median, saves, sends, DMs, calls booked)`. Tracking DMs and calls booked ties content back to both outcomes.

7. **Cadence:**
   - **Weekly (30 min):** the outlier scan plus Ship 30's Review → Reflect → Plan → Act on your own posts. Any post at 3x or more of your own median counts as a breakout and gets 3–9 follow-ups.
   - **Monthly:** refresh the VOC from DMs and calls (the highest-value source).
   - **Quarterly:** redo the Hell/Heaven map and belief bank.

8. **Use a "proof gap" alert to tie research to selling.** When many high-demand ideas carry NEEDS PROOF, the system tells the user which testimonials or case studies to collect next.

9. **Load voice every time.** The Voice Card and banned list ship as a file that is always loaded, with an automatic de-AI pass before any script is returned.

10. **Keep every worksheet to one page and fill-in-the-blank, each with the same worked persona.** Anthropic calls examples "one of the most reliable ways" to steer output, and they also show beginners what "done" looks like.

---

## 4) Sources

- Copyhackers: Amazon review mining for copywriting — https://copyhackers.com/2014/10/amazon-review-mining/
- Copyhackers: Rapid-fire review mining — https://copyhackers.com/how-to-do-rapid-fire-review-mining/
- Copyhackers: Use ChatGPT for review mining — https://copyhackers.com/ai-prompt/use-chatgpt-for-review-mining/
- Anthropic: Prompting best practices (examples, long context, quote grounding) — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Wikipedia: Signs of AI writing — https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Wikipedia: Mere-exposure effect (Zajonc 1968; Bornstein 1989) — https://en.wikipedia.org/wiki/Mere-exposure_effect
- Instagram: Instagram Ranking Explained — https://about.instagram.com/blog/announcements/instagram-ranking-explained/
- 1of10: home page and pricing — https://1of10.com/
- 1of10: How to Find Viral YouTube Videos Before Everyone Else — https://1of10.com/blog/how-to-find-viral-youtube-videos/
- ViewStats — https://www.viewstats.com/
- Sandcastles — https://sandcastles.ai/
- SparkToro — https://sparktoro.com/
- AlsoAsked — https://alsoasked.com/
- GummySearch closing notice — https://gummysearch.com/closing-time/ ; alternatives list — https://gummysearch.com/gummysearch-alternatives/
- Ship 30 for 30: 3 Content Frameworks (Buckets, 4A, Curiosity Gap) — https://www.ship30for30.com/post/online-writing-frameworks
- Ship 30 for 30: 112 ideas in 30 minutes — https://www.ship30for30.com/post/how-to-generate-112-new-content-ideas-in-30-minutes
- Ship 30 for 30: The 2-Year Test — https://www.ship30for30.com/post/the-2-year-test-a-framework-for-endless-content-ideas
- Ship 30 for 30: 1 breakout into dozens of ideas — https://www.ship30for30.com/post/5-clear-steps-to-turn-1-breakout-data-point-into-dozens-of-proven-content-ideas
- Ship 30 for 30: Writer's Reflection Tool — https://www.ship30for30.com/post/writers-reflection-tool-how-to-find-out-what-your-audience-is-interested-in-reading
- Dan Koe: How I Hunt For Viral Ideas — https://thedankoe.com/letters/how-i-read-books-for-maximum-intelligence-5-minute-habit/
- Dan Koe: How To Write Authentic Content — https://thedankoe.com/letters/dont-get-replaced-by-ai-how-to-write-authentic-content/
- Dan Koe: You don't need a niche, you need a point of view — https://thedankoe.com/letters/you-dont-need-a-niche-you-need-a-point-of-view/
- DigitalMarketer: Customer Avatar Worksheet — https://www.digitalmarketer.com/blog/customer-avatar-worksheet/
- Books, not fetched: Alex Hormozi, *$100M Leads* (2023), https://www.acquisition.com/books ; Eugene Schwartz, *Breakthrough Advertising* (1966); Matthew Dicks, *Storyworthy* (2018); Bob Moesta, *Demand-Side Sales 101* (2020), JTBD forces of progress.