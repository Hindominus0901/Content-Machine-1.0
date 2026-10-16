# Social listening and secondary research source map for Content Machine 1.0 (EN and VN, checked 5 Oct 2026)

This was read-only and no files were created. The founder's method is the frame. `brain/research/playbook.md` and `ceo-method.md` define it: the checklist first, then 3–5 places where the audience is clearly present, then a "why" loop. A pattern only counts if it shows up in at least two places from different people. The output is a brief with conclusion → root-cause insights → voice of customer → context → still unknown.

**What carries over from the agency repo:**
- The source tiers in `sources.md`: own customers first, peers next, vendors last.
- The social-listening table and the search phrasing in `sources.md`.
- The capture rule: exact words, link, date, place, role only.
- Quotes of about 15 words or fewer, and re-opening 5 random agent-captured lines (`sop.md`, "Chrome lines are evidence, with checks").
- The two Chrome batch prompts, with the repo, commit and lint steps removed.

---

## 1) What Claude and ChatGPT can reach

| # | Fact | Source / evidence |
|---|---|---|
| C1 | **Claude web search works on every plan, including Free. Research mode is paid only** (Pro, Max, Team, Enterprise). | claude.com/pricing; https://academy.claude.com/tutorials/using-research |
| C2 | **Claude's page fetcher (`Claude-User`) obeys robots.txt.** | https://support.claude.com/en/articles/8896518 |
| C3 | **Sites whose robots.txt blocks Claude's fetcher (5 Oct 2026):** LinkedIn, Quora, Amazon, TikTok, Instagram, Threads, Facebook and X. On some of these the block is a blanket `*` rule rather than a Claude-specific one. | robots.txt fetched on 5 Oct 2026 |
| C4 | **Reddit:** reddit.com returns 403 ("blocked due to a network policy") to non-browser requests. The Claude Code fetcher I tested refuses it outright ("unable to fetch from www.reddit.com"). Reddit sued Anthropic in June 2025. | My test; https://www.expertinstitute.com/resources/insights/reddit-sues-anthropic-data-scraping-ai-training/ |
| C5 | **Readable by fetch in my tests:** Voz (it returned live thread titles), Tinhte, webtretho.vn, otofun.net.vn, Unica, Gitiho, Goodreads book pages, and VnExpress article text. **VnExpress comments load by JavaScript, so a fetch doesn't see them.** | My tests on 5 Oct 2026 |
| C6 | **YouTube comments and transcripts can't be read by fetch.** YouTube's robots.txt blocks the comment and transcript paths for all bots, and both load by JavaScript. Claude has no built-in YouTube access. | robots.txt; my test; https://adityabawankule.io/guides/claude-code-youtube-analysis |
| C7 | **Claude in Chrome:** generally available since 26 Aug 2026 on paid plans only; Free accounts can't use it. It reads pages in the user's own logged-in browser. It blocks adult, pirated and some financial sites. There is an automatic or manual approval mode, and Anthropic names prompt injection as the main risk. A server-side classifier sometimes blocks legitimate domains with no override. | https://gigazine.net/gsc_news/en/20260827-claude-chrome-available/ ; https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely ; claudeissues.com reports |
| C8 | **Chrome captures** keep a summary plus short quotes (about 15 words or fewer), never full comments. | Agency repo, `training/runbooks/research-local-chrome.md` |
| G1 | **ChatGPT Free** has web search and **5 lightweight deep research runs per month**. Plus gets 10 full + 15 lightweight; Pro gets 125 + 125. | Third-party tracker, checked 29 Jul 2026: https://aiplanfinder.com/chatgpt-usage-limits |
| G2 | **ChatGPT and Reddit:** OpenAI has had Reddit Data API access since May 2024, so ChatGPT search can surface Reddit threads. **This makes it the best AI route to Reddit.** | https://www.barchart.com/story/news/26279967/openai-reddit-teaming-in-deal-that-will-bring-reddits-content-to-chatgpt |
| G3 | **ChatGPT's page fetcher (`ChatGPT-User`) may ignore robots.txt:** "Because these actions are initiated by a user, robots.txt rules may not apply." In practice, logins and bot walls still block it on Facebook, Instagram, TikTok, LinkedIn, Quora and Trustpilot. | https://developers.openai.com/api/docs/bots |
| G4 | **Atlas is gone.** It was discontinued on 9 Jul 2026 and stopped working on 9 Aug 2026. It was replaced by **ChatGPT Work** (an agent with a built-in cloud browser) and the **ChatGPT Chrome extension**. The extension reads the page you're viewing and is still rolling out; deep tasks go to the desktop app. Reports say it also reads YouTube videos; check that in your own account. | https://ppc.land/openai-kills-atlas-browser-folds-it-into-new-chatgpt-work-agent/ ; https://gigazine.net/gsc_news/en/20260710-openai-chatgpt-atlas-end/ ; https://www.superchargebrowser.com/library/openai-chatgpt-chrome-extension-2026 |
| G5 | **ChatGPT Work can now sign in to websites** (25 Aug 2026; Plus, Pro, Business). The model doesn't see the password, but hands-on reviews found CAPTCHAs and freezes. "Agent mode" on Plus was about 40 messages a month as of May 2026 (third-party figure). | https://decrypt.co/376757/openai-agentic-chatgpt-work-signs-in-without-you ; https://www.macstories.net/?p=198275 ; https://www.g-talent.net/blogs/chatgpt/precio-agentes-chatgpt-plan-2026 |
| P1 | **Meta Ad Library** shows **active ads only** for ordinary ads. Political and social-issue ads are kept 7 years, and ads that reached the EU are kept 1 year. **For US and VN coaches, the longest-running active ad is your "winner" signal.** | https://transparency.meta.com/en-us/researchtools/ad-library-tools |
| P2 | **TikTok Creative Center** is free with a TikTok for Business login. It has Top Ads, Keyword Insights and Trends by country, including Vietnam. | https://viettelstore.vn/tin-tuc/tiktok-creative-center-la-gi-huong-dan-su-dung-cong-cu-sang-tao-tiktok-hieu-qua-nhat (6 Jul 2026) |
| P3 | **LinkedIn Ad Library** is public with no account needed. **Google Ads Transparency Center** shows ads from the last 30 days. | https://www.admapix.com/blog/ad-intelligence/google-ads-transparency-center-guide |
| P4 | **AnswerThePublic** and **AlsoAsked** each give 3 free searches a day. AI web search doesn't show Google's "People Also Ask" box, so that is done by hand. | https://aeoengine.ai/blog/answer-the-public-free-guide-review ; https://help.alsoasked.com/en/articles/6577966-how-can-i-get-free-searches |
| P5 | **Amazon's full review pages need a login.** About 10–20 featured reviews still show on the product page. | Search summary citing https://www.ecommercebytes.com/2026/08/16/ |
| P6 | **Skool:** posts are visible to members only, even in "public" groups. The Discovery directory (name, member count, price) is public. | Apify Skool scraper docs |
| P7 | **Threads search needs a login** (since Dec 2024). | https://routenote.com/blog/search-on-threads/ |
| P8 | **Reddit Answers** (Reddit's own AI search): logged-out 10 questions a week, logged-in 20 a day. These limits are unconfirmed. Reddit says it will drop the logged-in/logged-out split from Q3 2026. | https://techcrunch.com/?p=3090181 |
| P9 | **Arctic Shift** (free Reddit archive) works. A plain subreddit listing returned posts dated 5 Oct 2026 for r/vozforums, r/TroChuyenLinhTinh and r/VietNam. **Keyword and title searches timed out.** GummySearch closed on 30 Nov 2025. | My API tests; earlier brief wf1 |
| P10 | **NotebookLM** imports public YouTube videos that have captions as a text transcript. It can't import videos under 72 hours old or without captions. | https://blog.google/technology/ai/notebooklm-audio-video-sources/ ; https://cellphones.com.vn/sforum/cach-dong-bo-youtube-voi-notebooklm |

**VN site checks (5 Oct 2026):**
- **Spiderum** shows a 503 page, "Spiderum đang bảo trì" (under maintenance).
- **kyna.vn** redirects to skills.kynaenglish.vn.
- **edumall.vn** fails with a TLS error. Treat it as defunct.
- **webtretho.com** redirects to webtretho.vn, now "Mạng xã hội dành cho phụ nữ Việt Nam" (a social network for Vietnamese women).
- **otofun.net** redirects to otofun.net.vn ("Mạng xã hội OTOFUN").
- **tiki.vn** returns 403 to non-browser requests. **Trustpilot** shows "Verifying Connection" and **Quora** a Cloudflare challenge.
- **Voz robots.txt** says `search=yes, ai-train=no, use=reference`. It blocks training bots but not `Claude-User`.
- **Tinhte** blocks only ClaudeBot.
- **VnExpress** explicitly allows `ChatGPT-User`, `Claude-User` and `OAI-SearchBot`.
- **Lazada** allows OpenAI's agents. **Shopee** disallows its rating pages.

**VN context:**
- DataReportal's *Digital 2026: Vietnam* reports 79.0M social media users (Oct 2025, 77.6% of the population): Facebook about 79M, Zalo 78.3M monthly users, TikTok 76.1M adults (+9.9% a year). https://datareportal.com/reports/digital-2026-vietnam
- Q&Me publishes free reports, including the H1 2026 trend report (24 Jul 2026). https://qandme.net
- The VN personal data law (Law 91/2025/QH15) has been in force since 1 Jan 2026 and replaces Decree 13/2023. Micro and household businesses are exempt; small firms get a 5-year grace period with conditions. https://tilleke.com/insights/vietnams-new-personal-data-protection-law-a-closer-look

**What this means for the pack:**
1. No AI reads logged-in social platforms on its own. Those need the user's own browser (Claude in Chrome, or the ChatGPT extension) or copy-paste.
2. Reddit goes through ChatGPT. Claude can't reach it.
3. Public VN forums (Voz, Tinhte, Otofun, Webtretho) and competitor pages are directly readable by both.
4. Every step needs three modes:
   - **AI-browse:** public pages.
   - **My-browser:** Claude in Chrome or the ChatGPT extension.
   - **Paste:** copy by hand, free on any plan.

---

## 2) EN source map (US/global)

Legend: ✓ works · ✗ blocked · Chrome = Claude in Chrome (paid) · Ext = ChatGPT Chrome extension · Risk: G (green) / A (amber) / R (red)

| Source | What it gives a coach | Claude | ChatGPT | By hand | Risk |
|---|---|---|---|---|---|
| **Reddit**: the audience's own subreddits, not coaching subs (e.g. r/careerguidance, r/smallbusiness, r/loseit, r/managers, r/findapath) | "Is it worth it", burned stories, failed DIY attempts, identity pain | ✗ fetch; search gives titles only; paste | **✓ search (licensed)**; deep research | Google `site:reddit.com "[phrase]"`; Reddit Answers; copy the thread | A: never in bulk; read by hand or in ChatGPT |
| **Reddit archive** (Arctic Shift) | Older threads with dates and permalinks | Advanced users only | Same | arctic-shift.photon-reddit.com; one subreddit at a time; search times out on big ones | G for reading; cite the reddit permalink |
| **Quora** | How beginners frame the problem | ✗ robots | ✗ robots, bot wall | Google `site:quora.com` | G by hand; low priority |
| **YouTube comments** under niche creators' videos | Raw reactions, "this happened to me", unanswered questions | ✗ fetch; **Chrome ✓** (sort by Top, scroll) | Ext / Work | Sort by Top, copy 30–50 | G (read-only) |
| **YouTube transcripts, podcasts** | Long-form stories, competitor frames and claims | Paste the transcript or use NotebookLM | Ext reportedly reads videos; or paste | "…more → Show transcript"; NotebookLM; Apple Podcasts transcripts and reviews | G (analysis only) |
| **Amazon reviews** of the books the buyer reads | Hopes, beliefs, what was useless (2–3★ are gold) | ✗ robots; Chrome ✓ when logged in | ✗ robots; Work with a login | Logged in: filter 1–3★, copy 20 | G |
| **Goodreads** | Longer, reflective versions of the same | Fetch often works; Chrome ✓ | May work | Filter by stars | G |
| **Trustpilot, G2/Capterra, Google reviews, Yelp** (competing programs, agencies, local services) | Horror stories, refund fights, broken promises | Bot wall in test; **Chrome ✓** | Ext | 1–2★ first, then three 5★ | G |
| **LinkedIn comments** under creators' posts | B2B buyers (founders, managers), status language | ✗ robots; Chrome ✓, low volume | ✗; Ext | Search posts and read the comments | A: LinkedIn bans bots; account risk |
| **X** | Quick complaints, hot takes | ✗; Chrome ✓ | ✗; Ext | Advanced search: `"[phrase]" min_faves:10 lang:en` | A |
| **TikTok** comments and search suggestions | Pain in their slang; objections under creator videos | ✗ robots; Chrome ✓ | ✗; Ext | App search, "Others searched for", comments | G by hand, A by agent |
| **Instagram Reels comments** | Reactions under competitor reels; comment-keyword demand | ✗; Chrome ✓ | ✗; Ext | By hand | A |
| **Facebook groups** you already belong to | The most honest venting | ✗; Chrome ✓ (member only) | ✗; Ext | The group's own search box | A; R if you'd quote private posts. Paraphrase only |
| **Skool** | Discovery: competitor communities, sizes, prices (market map). Inside your own groups: members' questions | Discovery readable; Chrome inside | Same | skool.com/discovery | A; never mine paid groups you joined just to research |
| **Meta Ads Library** | What the market is told; longest-running active ads = winners | Chrome ✓ | Ext / Work | facebook.com/ads/library: country, all ads, keyword | G |
| **TikTok Creative Center** | Top ads by industry and country, keyword insights | Chrome ✓ (login) | Ext | Free business login | G |
| **LinkedIn Ad Library, Google Ads Transparency** | B2B ad claims; Search and YouTube ads | Chrome / by hand | Same | linkedin.com/ad-library, adstransparency.google.com | G |
| **Google autosuggest, People Also Ask, related searches** | What they type, in order | Not shown in AI search; Chrome ✓ | Same | Incognito: "[topic] a…z"; expand PAA; AlsoAsked / AnswerThePublic (3 free a day) | G |
| **Google Trends** | Seasonality, rising queries | Chrome ✓ (JavaScript-heavy) | Same | trends.google.com | G |
| **Competitors' sites, offers, funnels** | Promises, prices, guarantees, mechanisms (the claim bank) | **✓ fetch / Research** | **✓ search / deep research** | Opt in to see the email sequence | G |
| **Market and context reports** | Market size and trends. **Never the buyer's voice** | ✓ Research | ✓ deep research | — | G |

---

## 3) VN source map

| Source | What it gives a coach | How to reach it | Risks | 3 search phrases |
|---|---|---|---|---|
| **Facebook groups by niche.** Group types to look for: kinh doanh online / chủ shop; freelancer / marketing; HR / người đi làm; mẹ bỉm / nuôi dạy con; giảm cân / eat clean / gym; đầu tư / tài chính cá nhân / F0; du học / IELTS; tâm lý / chữa lành. Find them with "hội", "cộng đồng", "group". | The biggest VN source: venting, "xin review" posts, "lùa gà" (scam) stories, prices people paid | **Only groups the coach is already in.** Use "Tìm kiếm trong nhóm" (search in group) by hand, or Chrome with manual approval, or Ext. AI search ✗. | Private posts: paraphrase only; no names, avatars or screenshots; Meta bans automated collection; VN data law | `"xin review" khóa [X]` · `"lùa gà" [lĩnh vực]` · `"có ai giống mình" [vấn đề]` |
| **Facebook Ad Library (Việt Nam)** | Competitors' active ads: hooks ("0đ", "chỉ còn N slot", "ib/chấm"), offers, landing pages | Chrome / by hand: country Việt Nam, all ads, sort by start date. Active ads only. | Low | `khóa học [lĩnh vực]` · `workshop miễn phí [lĩnh vực]` · `coaching 1:1 [lĩnh vực]` |
| **TikTok VN** comments, search suggestions, Creative Center VN | Gen Z and millennial pain, skeptical comments under coach videos, "Mọi người cũng tìm kiếm" suggestions, top VN ads | App by hand; Chrome ✓; Creative Center needs a login. AI fetch ✗. | Read-only; never reply as a test | `[X] lùa gà` · `review thật [X]` · `[vấn đề] có ai giống mình không` |
| **YouTube VN** | Comments under VN creators and podcasts; long talks for language and frames | Comments: Chrome or by hand. Transcripts: NotebookLM (needs VN captions) or "Hiện bản chép lời" (Show transcript). | G | `[X] có thật sự hiệu quả` · `học [X] mất bao lâu` · `[vấn đề] tuổi 30` |
| **Voz** (voz.vn) | Men 20–35, IT and office workers, students; cynical about "coach" and get-rich courses; salary and career talk; very blunt. Register: "thím", "fen". F17 "Chuyện trò linh tinh". | **Claude fetch ✓ (tested)**, ChatGPT ✓, Google `site:voz.vn` | robots says `ai-train=no, use=reference`: read for reference, never republish; use pseudonyms | `site:voz.vn coach "lùa gà"` · `site:voz.vn "khóa học" "có đáng"` · `site:voz.vn "thím nào" học [X]` |
| **Tinhte** | Tech, AI, productivity and photography audience; "anh em" register | Claude/ChatGPT fetch ✓ (only ClaudeBot blocked) | G | `site:tinhte.vn "khóa học" AI` · `site:tinhte.vn "có nên học" [X]` · `site:tinhte.vn "kinh nghiệm" [X]` |
| **Webtretho** (now webtretho.vn) | Women and mothers: marriage, parenting, women's careers, beauty; "các mẹ / chị em" | Fetch ✓ (site loads); Google `site:webtretho.vn` | Sensitive family and health topics: paraphrase, aggregate | `"các mẹ" cho con học [X]` · `"chị em" có ai từng [vấn đề]` · `webtretho "bị lừa" khóa học` |
| **Otofun** (now otofun.net.vn) | Men 30–50, Hanoi, car owners, small business owners; money, investing, family; "các cụ / mợ" | Fetch ✓ (site loads); Google `site:otofun.net.vn` | G/A | `"các cụ cho em hỏi" [X]` · `otofun "có nên" học [X]` · `otofun "mất tiền" khóa học` |
| **Spiderum** | Long essays by young educated readers on self-help, career, psychology. Best for identity and root causes. | **Under maintenance on 5 Oct 2026 (503).** Use Google results; recheck. | G | `site:spiderum.com "khủng hoảng tuổi 25"` · `site:spiderum.com self-help "vô ích"` · `site:spiderum.com "tại sao" [vấn đề]` |
| **Reddit:** r/VietNam (English, expats and diaspora, weak for local buyers); r/vozforums and r/TroChuyenLinhTinh (Vietnamese, active Oct 2026) | Small but honest VN threads | **ChatGPT search ✓**, Claude ✗, Arctic Shift listings | A (as in the EN map) | `site:reddit.com/r/vozforums "khóa học"` · `reddit "coach" "lừa đảo"` · `r/TroChuyenLinhTinh "có ai" [vấn đề]` |
| **Shopee / Tiki / Lazada / Fahasa** reviews of self-help and business books and course vouchers | 1–3★ reviews: "không như quảng cáo" (not as advertised), "sáo rỗng" (empty); what buyers expected | By hand in the app (filter by stars), or Chrome. Tiki blocks bots; Shopee robots disallows rating pages; Lazada allows OpenAI agents. | G by hand | `sách [chủ đề] bán chạy` · review filter `1 sao` + `"không như quảng cáo"` · `khóa học online [X] voucher` |
| **Zalo groups / communities** | Real client questions and objections. This is **primary** research, from the coach's own groups only. | By hand: the coach copies messages from **their own** groups, strips names, pastes | **R for any group you don't run.** VN data law; Zalo terms; never pull phone numbers | In-chat search: `học phí` · `có hiệu quả không` · `sợ` |
| **Unica, Gitiho, Kyna** (kyna.vn redirects to skills.kynaenglish.vn); **Edumall unreachable, treat as defunct** | Competitor course titles, prices ("giảm 80%"), outlines, ratings, student reviews, overused claims | Claude/ChatGPT fetch ✓ for Unica and Gitiho pages; reviews may need Chrome | G | `site:unica.vn [chủ đề]` · `"review khóa học" [tên giảng viên]` · `[tên giảng viên] "lừa đảo"` |
| **Google VN autosuggest**, "Mọi người cũng hỏi" (People Also Ask), Google Trends VN (optionally Cốc Cốc suggest) | What they type and in what order; seasonality | **By hand** in an incognito window on google.com.vn, adding a–z after the phrase; Trends set to "Việt Nam" | G | `[chủ đề] có nên` · `[chủ đề] lừa đảo` · `[chủ đề] cho người mới bắt đầu` |
| **VnExpress comments** (also Tuổi Trẻ, Thanh Niên, Kenh14) | A large, older, more conservative sample on money, work, education, "học online", scams | Article text: fetch ✓ (robots allows both). **Comments: by hand or Chrome**, sorted "Quan tâm nhất" (most liked). | G; commenters' names are public, still use pseudonyms | `site:vnexpress.net "khóa học" làm giàu` · `site:vnexpress.net coach` · `site:vnexpress.net "người trẻ" [vấn đề]` |
| **Threads VN** | Gen Z and millennial confessions; career and relationship venting | **Search needs a login.** By hand or Chrome. AI ✗. | A | `[vấn đề] có ai giống tui không` · `tâm sự [vấn đề]` · `đi học [X] xong thấy` |
| **Market and context (secondary)** | Platform sizes, consumer trends, the ad landscape | ✓ Claude Research / ChatGPT deep research | G | DataReportal *Digital 2026: Vietnam*; Q&Me free reports; Brands Vietnam / Advertising Vietnam |

---

## 4) Search-phrase bank

**EN.** Use the niche's own words from the voice-of-customer lexicon.
- **Burned:** "[program type] waste of money" · "coaching scam" · "paid $[N] for a coach and" · "never again [program type]" · "got burned by a coach" · "asked for a refund" · "high ticket coaching regret"
- **Doubting:** "is [solution / coach / program] worth it" · "does [method] actually work" · "anyone had success with [program]" · "[program] review reddit" · "too good to be true"
- **Buying:** "looking for a [type] coach" · "recommend a [type] coach" · "how much does a [type] coach cost" · "[competitor] vs [competitor]" · "alternatives to [competitor]"
- **Identity:** "am I the only one who [problem]" · "starting to think I'm not cut out for" · "should I just go back to [job]" · "my husband/wife thinks I'm wasting money on" · "I feel like a failure because"
- **Trigger and desire (bonus):** "the moment I knew I had to" · "I just want to [outcome] without [pain]"

**Operators:**
- Google: `site:reddit.com` / `site:quora.com` / `"exact phrase"` / `OR` / `before:2026-01-01`
- X: `"phrase" min_faves:10 lang:en`
- Amazon: filter reviews by star rating
- YouTube: sort comments by Top
- TikTok: read "Others searched for"

**VN** (natural register; swap in the niche's words):
- **Burned (bị hớ / bị lừa):** "lùa gà" · "mất tiền oan" · "tiền mất tật mang" · "học xong vẫn không áp dụng được" · "không như quảng cáo" · "đòi hoàn tiền" · "đốt [N] triệu vào khóa học"
- **Doubting:** "[X] có thật không" · "có nên học [X] không" · "[X] có đáng tiền không" · "review thật [X]" · "[X] có lừa đảo không" · "học [X] có hiệu quả không"
- **Buying:** "xin review khóa [X]" · "tìm coach [lĩnh vực]" · "nên học [X] ở đâu" · "học phí [X] bao nhiêu" · "[X] hay [Y] tốt hơn" · "ai biết chỗ nào dạy [X] uy tín"
- **Identity:** "có ai giống mình không" · "mình có phải người duy nhất" · "30 tuổi vẫn chưa [X]" · "cảm thấy mình vô dụng" · "bế tắc / mất phương hướng" · "chồng/vợ bảo mình phí tiền" · "bố mẹ không ủng hộ"
- **Forum register cues:** Voz "thím nào…", "fen"; Otofun "các cụ cho em hỏi"; Webtretho "các mẹ ơi", "chị em"; Tinhte "anh em"; Facebook "cho mình hỏi", "xin review thật", "ib/chấm" (seller tells).

---

## 5) The 1-hour research sprint for a DIY coach

The founder's order, compressed. A second loop turn can run next week.

| Min | Step | Claude Pro/Max | Claude Free | ChatGPT Plus | ChatGPT Free |
|---|---|---|---|---|---|
| 0–8 | **Checklist + 3 scope questions.** Four customer layers (demographics, psychographics, behavior, culture) and the context (market, product, company, competitors). The coach answers 3 primary questions: who bought fastest, what they said first, why people said no. | In the Project with the Brand Brain | Same, pasted in | In the Project | In chat |
| 8–20 | **Secondary research (AI, in the background).** Market awareness and sophistication; 5 competitors' promise, price, angle and proof; "what none of them say"; claim bank. | **Research mode** | Web search, 2–3 queries | **Deep research** | 1 of 5 lightweight deep research runs a month, or search |
| 8–35 | **Listening in 3 places, about 15–20 lines each (40–60 total).** **EN:** YouTube comments + Reddit + 1–2★ book or competitor reviews. **VN:** one Facebook group you're in + TikTok VN comments + Voz or Otofun/Webtretho, plus the VN Facebook Ad Library. | **Claude in Chrome** (manual approval) for YouTube, Facebook, reviews, Ad Library; Voz by fetch; Reddit by paste | **Paste mode:** copy by hand into labelled blocks | Search for Reddit and Voz; **Ext** on the open page; avoid Work logins on main social accounts | Search + paste |
| 35–50 | **Patterns + why loop.** Sort into the VoC grid; keep only patterns seen in ≥2 places from different people; ask "why" and turn it into one question; run one follow-up search per top pattern. | ✓ | ✓ | ✓ | ✓ |
| 50–60 | **Brief.** The playbook format (conclusion: demand → product → bridge; 3 root insights with their why-chains; 10–20 VoC lines; context; still unknown), plus **10 signature-keyword candidates** taken from audience words and **10 idea seeds**, saved to the Research Bank. | ✓ (Notion connector) | Copy out | ✓ | ✓ |

**Collect prompt** (Chrome or paste):

```
Read [PLACE]. Keep only lines where the author is clearly [BUYER].
For each line: exact words (≤15 words), link, date, place, role only (no names or handles).
Tag: pain 1/2/3, desire, fear, failed solution, belief, objection, trigger.
Stop when nothing new appears.
```

**Why prompt:**

```
Using only the lines above:
group them into patterns; keep a pattern only if it appears in ≥2 places from different people;
for each, write pattern → why → why → root, and list the evidence against it;
mark anything inferred as [AI inference].
```

**Automations:** scheduled tasks can only re-run the public part (ChatGPT search for Reddit; fetch for Voz, competitor pages and news). Logged-in listening stays a weekly step for the coach or Chrome.

---

## 6) Privacy and terms rules

These merge the agency house rules with what the platforms require.

1. **Read-only and low volume.** Never post, react, join, DM or submit forms while researching. Set agents to manual approval on social sites.
2. **Only spaces you already belong to.** Never join a private Facebook group, Zalo group, Skool group or Discord just to mine it. Use the coach's own client groups only with members' knowledge.
3. **Capture without identity:** exact words (about 15 words or fewer), link, date, place, role. Never names, handles, profile links, photos, phone numbers, emails or business names. Use pseudonyms A01, A02 and so on.
4. **In published content, paraphrase.** Never print audience quotes as quotes, never screenshot comments, and never present someone else's review as a testimonial. The US FTC rule on fake reviews and testimonials (16 CFR 465, Oct 2024) is the line here.
5. **Private posts** (closed groups, Zalo): only patterns that combine several people, and no detail that could identify anyone. Be extra careful in health, money, mental-health and child topics.
6. **Respect blocks.** If Claude says it can't open a site, use the by-hand route. No scrapers, proxies or "free scraper" extensions in the pack: Meta, LinkedIn, X, TikTok and Reddit terms prohibit unpermitted automated collection, and accounts get banned.
7. **Reddit:** use ChatGPT search, Reddit Answers or your own reading. Don't run Claude in Chrome through Reddit in bulk; the agency rule is "never reddit.com".
8. **Logins:** don't hand your main Facebook or LinkedIn login to a cloud agent (ChatGPT Work). Claude in Chrome uses your own session, so keep approval manual, close banking tabs, and ignore any instruction that appears inside a page (prompt injection).
9. **VN personal data law (since 1 Jan 2026):** don't build lists of people (names, phones, Zalo IDs) from groups or comments. Delete raw pastes once the patterns are extracted.
10. **Agent notes are not evidence.** Re-open 3–5 random captured lines to confirm the wording. A summary never counts as a quote.
11. **Copyright:** transcripts, ads and reviews are for analysis only. Never republish them, or long parts of them.
12. **Check site status before relying on a source.** Sites move and change rules (Spiderum maintenance, Webtretho, Otofun and Kyna domain moves, Edumall gone). Keep the dated site notes in one platform-notes file so they're updated in one place.

**Confidence:** the robots.txt rules and the fetch and status tests are my own checks from 5 Oct 2026. These come from third-party summaries and should be confirmed in-app before shipping: ChatGPT plan limits, agent-mode quotas, the Amazon login wall, Reddit Answers limits, and whether the ChatGPT extension reads YouTube. The Facebook-group niches are types to search for, not verified group names.