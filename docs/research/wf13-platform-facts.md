# wf13: How a coach can bring posts and channels they like into ChatGPT and Claude (platform facts, checked 5 Oct 2026)

**Feature being sized.** The founder wants coaches to bring in posts or channels they like or follow, so the machine can learn from them. This brief only establishes what the two apps can and cannot take in today. Design choices are left to the spec, apart from a short "what this means" section.

**Labels**
- **[DATA]**: an official help page, release note, robots.txt or policy page, read on the date shown.
- **[PRAC]**: a third-party or community source, or my own probe.
- **[UNVERIFIED]**: needs a hands-on test in a real account. Phase-0 checks are listed in §10.

**Method**
- help.openai.com refuses direct fetches (HTTP 403), so I read it through a text-reader proxy (r.jina.ai). The text is verbatim, and each page's "Updated" line is recorded.
- support.claude.com, platform.claude.com, learn.chatgpt.com, YouTube help, Meta newsroom and TikTok guidelines were read directly.
- robots.txt files were downloaded directly on 5 Oct 2026.
- Facts reused from the earlier briefs `wf10-*` and `wf11-ux-facts.md` (same day) say so.

---

## 0. Bottom line (for the spec writer)

1. **Pasting a social link is not a reliable route in either app.**
   - **Claude** honours robots.txt [DATA]. Instagram, Facebook, Threads and X disallow all non-whitelisted agents. TikTok and LinkedIn name `Claude-User` explicitly. So on Claude, a pasted IG, FB, Threads, X, TikTok or LinkedIn link should be refused on every plan [DATA robots + Anthropic policy; real behaviour is UNVERIFIED].
   - **ChatGPT**'s user-initiated fetcher "may not" follow robots.txt [DATA]. Login walls, rate limits and JavaScript-only pages still apply, so expect partial or empty reads [PRAC/UNVERIFIED].
   - **Newsletter and blog links** (Substack and similar) work in both apps [DATA robots + PRAC probe].
   - **YouTube links**: at best title and description. There is no transcript via link in either app's chat [PRAC/UNVERIFIED].
2. **Screenshots are the universal route** on both apps, every plan, phone and desktop [DATA].
   - The binding limit is **ChatGPT Free: 3 file uploads per day** [DATA]. Images very likely count toward it (the exact image count is [UNVERIFIED]).
   - **Claude** takes **20 images per message** on every plan [DATA], limited only by usage caps.
   - Do **not** stitch a carousel into one tall image. Both apps downscale large images (Claude to a 2,576 px long edge), so small text becomes unreadable [DATA + inference]. Send separate screenshots.
3. **Video and audio files:**
   - **ChatGPT accepts video uploads on all plans, Free included**, but OpenAI says the analysis "may not analyze the entire video or accurately interpret its audio" [DATA].
   - **Claude accepts no video or audio files** [DATA, by omission from the official upload list, 23 Jul 2026].
   - Neither app takes an audio file to transcribe in chat in a documented way.
   - So spoken content from reels or videos has to arrive as **text**: a YouTube transcript, captions typed in by the coach, or the coach's own summary.
4. **YouTube transcripts:**
   - The reliable no-install route is **desktop "Show transcript" → copy → paste** [PRAC]. Vietnamese auto-captions exist [DATA].
   - On a phone, transcripts can be viewed but not easily copied [PRAC].
   - Pastes over 10,000 characters become an attachment in ChatGPT on all plans [DATA]. Whether that attachment counts against Free's 3-a-day cap is [UNVERIFIED].
   - The **ChatGPT browser extension side chat** officially reads a YouTube video's timestamped transcript when captions exist [DATA]. It needs the desktop app plus a Chromium browser; whether Free can use it is [UNVERIFIED].
5. **Browse mode can see a creator's grid with counts**, so median and outlier maths is possible:
   - TikTok, YouTube, X and Threads show view counts; the Instagram Reels tab shows views unless the creator hides them [PRAC].
   - LinkedIn shows no public impressions [PRAC].
   - Browse needs paid tiers: **Claude in Chrome on Pro+**, or the ChatGPT extension (Plus for full use; Free/Go "limited") [DATA via wf10].
   - All of this conflicts with Meta's and LinkedIn's anti-automation terms [DATA]. Keep it read-only, low-volume, coach-driven and **opt-in**.
6. **Saving a swipe:**
   - ChatGPT Projects accept **pasted text** and **"Save to project"** replies as sources [DATA]. Whether these count toward the Free 5-file cap is [UNVERIFIED].
   - "Add links from apps" accepts **only Google Drive and Slack links**, not social URLs [DATA].
   - Claude Projects accept text as knowledge [DATA]. On Free, all knowledge must fit the context window (no RAG) [DATA].
7. **Originality rules punish reposts, not inspiration.**
   - Meta (Facebook from Jul 2025, sharpened 13 Mar 2026; Instagram extended to photos and carousels 30 Apr 2026), TikTok (Community Guidelines) and YouTube (YPP "reused" and "inauthentic", 15 Jul 2025) all cut reach or pay for content reposted "without anything new" [DATA; the IG April 2026 detail is PRAC].
   - So the machine should use liked posts as **pattern and angle input**, always rewritten in the coach's own story, proof and voice. It should never output near-copies and never tell the coach to repost a screenshot or clip.

---

## 1. Summary table: route × app × plan × device

Legend:
- ✅ works [DATA]
- 🟡 partial, or works with a catch
- ❌ fails or is not offered
- ❓ unverified (Phase-0)
- 📱 phone app, 💻 desktop app or web
- Go and Plus differ from Free only in upload and tool quotas unless noted.

### 1a. ChatGPT

| # | Route | Free | Go | Plus | Device notes |
|---|---|---|---|---|---|
| R1 | Paste **newsletter or blog** URL (Substack, own site) | ✅ search and fetch on all plans [DATA]. Public, server-rendered pages read fine [PRAC probe] | ✅ | ✅ | 📱💻 |
| R2 | Paste **YouTube** video URL | 🟡❓ Third parties say ChatGPT "can't ingest a YouTube URL on its own" [PRAC, Jul 2026]. At best title and description; no transcript | same | same | 📱💻 |
| R3 | Paste **Instagram** post or reel URL | ❓ likely ❌ or caption-only. The robots file says "Disallow: /" for all non-whitelisted agents. ChatGPT-User "may" ignore robots [DATA], but IG returned **429** to a logged-out data-centre fetch [PRAC probe] | same | same | 📱💻 |
| R4 | Paste **TikTok** URL | ❓ likely ❌. robots names `ChatGPT-User` with Disallow: / [DATA]. Logged-out fetch got a generic shell page [PRAC probe] | same | same | |
| R5 | Paste **Facebook** link: public Page post / personal profile / group | ❓ Page post: likely login wall (probe got a shell page). Personal profile: ❌ mostly login-walled. **Group: ❌**, since private groups need login | same | same | |
| R6 | Paste **LinkedIn** post URL | ❓ likely ❌. robots disallows `ChatGPT-User` [DATA]. A company page returned meta text to a logged-out fetch [PRAC probe] | same | same | |
| R7 | Paste **Threads** URL | ❓ 🟡 robots "Disallow: /" for all; a logged-out fetch got the profile's og:description [PRAC probe] | same | same | |
| R8 | Paste **X** post URL | ❓ likely ❌. robots "Disallow: /" for all; probe got HTTP 402 [PRAC probe] | same | same | |
| R9 | **Screenshot** of one post | ✅ image input on all plans [DATA]. Counts toward **3 uploads/day** (very likely; exact count ❓) | ✅ higher quota [DATA] | ✅ 80 files / 3 h [DATA] | 📱 camera, photos and files; 💻 drag or paste [DATA] |
| R10 | **Carousel** of 5–20 screenshots | 🟡 Free cap breaks this (3/day) | 🟡 | ✅ ≤10 files per send [DATA for projects; PRAC for chat] | Don't stitch (downscaling) |
| R11 | **Video file** (mp4 screen recording) | 🟡 accepted on Free [DATA]. "May not analyze the entire video or accurately interpret its audio" [DATA]. Counts as an upload [DATA] | 🟡 | 🟡 | 📱 if Photos won't pick it, use Files [DATA] |
| R12 | **Audio file** (m4a voice memo) | ❓ not in the official upload FAQ. Native mp3/mp4 transcription was a feature *request* in Jul 2026 [PRAC]. Record mode is Plus+ and macOS only [PRAC] | ❓ | ❓ | |
| R13 | **YouTube transcript**, copy-paste | ✅ text paste. Over 10k chars it becomes an attachment (revert with "Show in text field") [DATA]. Whether that counts as an upload ❓ | ✅ | ✅ | 💻 copy works; 📱 copy is awkward or impossible [PRAC] |
| R14 | **Browser extension side chat** on a YouTube video (transcript) | ❓ Free/Go Work is "Limited (desktop app)" [DATA via wf10] | ❓ | ✅ "can use the video's timestamped transcript" when captions exist [DATA] | 💻 only: desktop app plus Chrome, Edge, Brave or Vivaldi |
| R15 | **Browse**: open a creator profile and list recent posts with counts | ❓ limited | ❓ | 🟡❓ extension in the coach's own logged-in browser [DATA]. Asks per site [DATA]. Works in principle; accuracy ❓ | 💻 only. Cloud browser (Plus/Pro) does **not** use the coach's logins [DATA via wf10] |
| R16 | **Save a swipe** (text) into the Project | 🟡 paste-text source and "Save to project" exist [DATA]. **5 files/project** cap; whether text sources count ❓ | 🟡 25 files | ✅ 25 files | Project *creation* is web/Windows only [DATA via wf11]; 📱 can use projects |
| R17 | **Share-sheet** from the IG/TikTok app straight to ChatGPT | ❓ probably sends only the link (→ R3/R4) | ❓ | ❓ | 📱 |
| R18 | **Copy the caption text** and paste | ✅ text always works. On phones, which social apps let you copy a caption ❓ | ✅ | ✅ | 💻 always possible on the web |

### 1b. Claude

| # | Route | Free | Pro | Device notes |
|---|---|---|---|---|
| R1 | Paste **newsletter or blog** URL | ✅ web search on all plans since 27 May 2025 [DATA]. Web fetch reads pasted URLs [DATA]. "New experience": no toggle, Claude searches when it helps [DATA] | ✅ | 📱💻. Fetch only reads text, HTML or PDF, not JavaScript-only pages [DATA, API doc] |
| R2 | Paste **YouTube** URL | 🟡❓ robots allows /watch but disallows the transcript endpoints (`/api/`, `/youtubei/`, `/timedtext_video`) [DATA]. Fetch doesn't render JavaScript [DATA, API]. At best title and description | same | |
| R3 | Paste **Instagram** URL | ❌ (expected). robots: everyone not whitelisted gets "Disallow: /", and ClaudeBot is named "Disallow: /". Anthropic bots "respect… robots.txt" [DATA] | ❌ | |
| R4 | Paste **TikTok** URL | ❌ robots names `Claude-User` Disallow: / [DATA] | ❌ | |
| R5 | Paste **Facebook** link (Page / profile / group) | ❌ robots: `Claude-User` falls under `User-agent: *` → Disallow: / [DATA] | ❌ | |
| R6 | Paste **LinkedIn** URL | ❌ robots names `Claude-User` Disallow: / [DATA] | ❌ | |
| R7 | Paste **Threads** URL | ❌ robots `*` Disallow: / [DATA] | ❌ | |
| R8 | Paste **X** URL | ❌ robots `*` Disallow: / [DATA] | ❌ | |
| R9 | **Screenshot** of one post | ✅ JPEG, PNG, GIF and WebP [DATA]. Limited only by the 5-hour usage cap | ✅ | 📱 "+" → Add files or photos; iOS and Android widgets have a camera [DATA] |
| R10 | **Carousel** of 5–20 screenshots | ✅ **20 images per message**, ≤10 MB each, ≤8000×8000 px [DATA]. Up to 20 files per chat (support page) [DATA]. Heavy on Free usage | ✅ | |
| R11 | **Video file** (mp4) | ❌ not a supported type [DATA by omission, 23 Jul 2026]. Third parties confirm "no ability to process… video" [PRAC] | ❌ (❓ whether the code sandbox could take an mp4 and extract frames) | |
| R12 | **Audio file** | ❌ [DATA by omission + PRAC]. Claude mobile **dictation doesn't support Vietnamese** [DATA via wf11] | ❌ | |
| R13 | **YouTube transcript**, copy-paste | ✅ text. Large pastes eat Free usage | ✅ | 💻 copy; 📱 hard [PRAC] |
| R14 | Browser-agent transcript read | ❌ (no Claude in Chrome on Free) [DATA via wf10] | ❓ Claude in Chrome can read the open page; reading the transcript panel is not documented | 💻 Chrome only |
| R15 | **Browse**: list a creator's recent posts with counts | ❌ | 🟡❓ Claude in Chrome (GA 26 Aug 2026) reads the tab the coach is signed in to [DATA via wf10]. Reddit blocked since 18 Sep 2026 [PRAC] | 💻 Chrome on desktop; Cowork built-in browser on desktop app (Pro) [DATA via wf10] |
| R16 | **Save a swipe** into Project knowledge | ✅ "+" → upload documents, text files or code snippets [DATA]. Free: max 5 projects, and all knowledge must fit the context window (no RAG) [DATA] | ✅ RAG expands capacity up to about 10× [DATA] | Phone project editing ❓ |
| R17 | **Share-sheet** from a social app to Claude | ❓ probably the link only → R3–R8 ❌ | ❓ | 📱 |
| R18 | **Copy caption** and paste | ✅ | ✅ | |

---

## 2. Route: pasting a link (detail)

### 2.1 How each app's fetcher behaves
- **ChatGPT.** "When users ask ChatGPT… a question, it may visit a web page with a ChatGPT-User agent… Because these actions are initiated by a user, **robots.txt rules may not apply**." [DATA, OpenAI crawler docs, platform.openai.com/docs/bots, read 5 Oct 2026]
  - Web search is on Free, Go, Plus, Pro and logged-out users, on web, desktop and mobile, "subject to your plan's usage limits" [DATA, "Searching the web with ChatGPT"].
  - No help page promises that a pasted social URL will be read.
- **Claude.** "Claude-User supports Claude AI users. When individuals ask questions to Claude, it may access websites using a Claude-User agent." and "Anthropic's Bots respect 'do not crawl' signals by honoring industry standard directives in robots.txt." [DATA, support.claude.com/en/articles/8896518, updated 7 Apr 2026]
  - Web search covers all plans; web fetch reads pasted URLs. Fetching a long article "will use substantially more of your context window" [DATA, support.claude.com/en/articles/10684626, "updated this week"].
  - In the "new Claude experience" there is no web-search toggle [DATA, same page].
  - API web-fetch documentation [DATA, platform.claude.com, read 5 Oct 2026]. claude.ai is assumed to use the same tool, which is [UNVERIFIED]:
    - "does not support websites dynamically rendered with JavaScript".
    - Error codes include `url_not_allowed` for "robots.txt" and `unsupported_content_type` ("only text, HTML, and PDF").
    - The URL must appear in a user message.

### 2.2 robots.txt facts (downloaded 5 Oct 2026) [DATA]

| Site | Rule that matters |
|---|---|
| instagram.com | Header: "Collection of data on Instagram through automated means is prohibited unless you have express written permission". GPTBot and ClaudeBot: Disallow: /. Everyone not whitelisted (`*`): Disallow: / |
| facebook.com | Same Meta header. `*`: Disallow: /. ClaudeBot has its own group with partial paths, but `Claude-User` has no group, so it falls under `*` |
| threads.com | Same structure as Instagram. `*`: Disallow: / |
| x.com | `*`: Disallow: / |
| tiktok.com | One group lists GPTBot, OAI-SearchBot, ClaudeBot, **ChatGPT-User**, **Claude-User** and Claude-SearchBot → Disallow: / |
| linkedin.com | **ChatGPT-User**: Disallow: /. **Claude-User**: Disallow: /. `*`: Disallow: / ("email whitelist-crawl@linkedin.com") |
| youtube.com | `*` may fetch /watch, but `/api/`, `/youtubei/`, `/timedtext_video`, `/comment` and `/results` are disallowed. Transcripts and comments are off-limits to robots-respecting agents |
| substack.com | Posts allowed. `/p/*/comment/*`, `/inbox`, `/subscribe` and `/embed` disallowed |
| reddit.com | The robots request itself was blocked ("Your request has been blocked due to a network policy") |

### 2.3 Own probe (my sandbox; **not** the ChatGPT or Claude fetchers; data-centre IP) [PRAC, 5 Oct 2026]

Logged-out GET with the ChatGPT-User user-agent:

| Site | Result |
|---|---|
| Instagram profile | **429** (rate-limited, empty) |
| X profile | **402** |
| YouTube watch page | **429** |
| Facebook Page | 200 but a shell titled only "Facebook" (no post text) |
| TikTok profile | 200, generic "TikTok - Make Your Day" shell |
| LinkedIn company page | 200 with og:description ("34,453,923 followers…") |
| Threads profile | 200 with og:description ("5.7M Followers • 168 Threads…") |
| Substack newsletter | 200 with full content |

**Reading:** social platforms block, throttle or blank anonymous server fetches. Whatever an app reads from a social link is likely meta text at best: a caption snippet or follower counts, not the full post, the video or the comments.

### 2.4 Third-party reports [PRAC]
- **YouTube on ChatGPT:**
  - "There is no official ChatGPT YouTube integration in 2026… The consumer app can't ingest a YouTube URL on its own; you supply the transcript." (usecarly.com, 9 Jul 2026)
  - Another guide says YouTube is "blocked from ChatGPT's browsing tools" (yingtu.ai; the page now returns 410, so treat it as weak).
  - Gemini added native YouTube support in Oct 2025 (same sources). Context only; it is not one of our target apps.
- **Older study:** 47 of the top 100 sites blocked ChatGPT's Browse-with-Bing (originality.ai, 2023; old, context only).
- **Claude:** "Standalone Claude cannot directly open… private Instagram links"; LinkedIn is not among Anthropic's connectors as of Aug 2026 (marketbetter.ai, 2026).

---

## 3. Route: screenshots and images

### 3.1 ChatGPT [DATA unless marked]
- **Plans and devices:**
  - "Image inputs are available on Free and paid ChatGPT plans, subject to plan-specific usage limits." All platforms: web, iOS and Android. Add with **+ → Add photos & files**, drag, or paste from the clipboard (Image Inputs FAQ, "Updated: last month").
  - On mobile web, photos can be attached before signing in.
- **Types and size:** PNG, JPEG, non-animated GIF; **20 MB per image**. Third parties also report WebP working [PRAC].
- **How many per message:** "depends on… the size of the images and the amount of text". No fixed number is published.
  - Projects page: "only 10 files can be uploaded at the same time" [DATA].
  - Third party: 10 per message [PRAC, merlio.app, 19 Jan 2026].
- **Daily caps:**
  - File Uploads FAQ (updated about 11 Sep 2026): "Users can upload up to 80 files every 3 hours. **Free users are limited to 3 file uploads per day.** Note that we may lower these limits during peak hours." Failed uploads can count. The remaining quota is not shown.
  - The Free tier FAQ lists "File and image uploads" as one tool with its own limit, so images very likely share the 3/day cap. The exact image count is [UNVERIFIED].
  - Third parties disagree: Free "2 images per day", Plus "50" [PRAC, merlio Jan 2026]. Another says "No current OpenAI Help Center… page… establishes 50 image uploads per day" [PRAC, laozhang, updated 14 Jul 2026].
  - Go: "Extended access to file uploads" with no number given [DATA].
- **Reading quality:**
  - Official limitations include "Non-English: The model does not perform as well handling images with text of non-Latin alphabets, such as Japanese or Korean."
  - Vietnamese uses a Latin alphabet with diacritics, so it is not covered by that warning, but diacritic accuracy is [UNVERIFIED].
  - Also listed: "Big text: Enlarge text within the image", and "images are resized before analysis".
- **Text embedded in PDFs:** on non-Enterprise plans, documents get "text-based retrieval… extract digital text from the file and **discard any images**" (File Uploads FAQ).
  - So a PDF built from screenshots may lose their text unless the PDF is OCR'd.
  - The new iOS camera **Scan** mode (1 Oct 2026) combines several captured pages into one PDF [DATA, release notes]. Whether that PDF carries OCR text is [UNVERIFIED].
- **Live camera or screen share in Voice:** "Live does not support video or screen sharing." The older **Advanced** voice keeps video and screen share "to eligible subscribers" on iOS and Android, with daily limits (ChatGPT Voice help, updated about 25 Sep 2026). This is a fragile route; not recommended.

### 3.2 Claude [DATA]
- **Types:** JPEG, PNG, GIF, WebP. Chat uploads: "Up to 20 files per chat", up to 8000×8000 px (support.claude.com "Upload files to Claude", updated 23 Jul 2026).
- **Per message:** "**20 per message on claude.ai**", max **10 MB** per image on claude.ai (platform vision docs, read 5 Oct 2026).
- **Downscaling:**
  - Images larger than the model's limit are downscaled. Claude 4.7+ models use a **2,576 px long edge** and 4,784 visual tokens.
  - A carousel stitched into one tall strip (for example 1080×10,000) would shrink to about 280 px wide, and the text would become illegible [inference from DATA].
  - The docs warn: "make sure [text is] legible and not too small."
- **Plans and devices:**
  - The upload page gives no per-plan image cap. Paid plans mainly raise overall usage [PRAC].
  - Phone: "+" → Add files or photos; iOS and Android widgets have a camera button [DATA, Claude iOS/Android help].
- **Privacy:** "Claude cannot be used to name people in images and refuses to do so" [DATA, vision limitations]. This fits the pack's privacy-first rule.
- **Conflicting help pages:** "Upload files to Claude" (23 Jul 2026) says **500 MB per file** in chat. "Create and edit files" (6 Aug 2026) says "**30MB** per file for both uploads and downloads". The project knowledge limit is 30 MB per file. Ignore this for screenshots, which are well under both limits.

---

## 4. Route: video and audio files

**ChatGPT** [DATA, Image Inputs FAQ, "Updated: last month"]:
> "Can I upload videos to ChatGPT? Yes. ChatGPT can accept video files as attachments through supported upload methods, **including on Free plans**. Availability varies by platform, upload method, and account… If you can't select a video in Photos, check whether you can attach it through Files instead. ChatGPT may use tools to analyze uploaded videos, but its analysis can be incomplete or inaccurate. **It may not analyze the entire video or accurately interpret its audio.** Video attachments count toward your plan's file-upload limits."

- Size: the 512 MB hard file cap applies [DATA]. There is no published length limit.
- How analysis works: "extracts keyframes, transcribes the audio separately" [PRAC, vomo.ai updated 2 Sep 2026 / cometapi]. OpenAI's own wording is only "may use tools". Whether speech is transcribed, in English and in Vietnamese, is [UNVERIFIED].
- Audio files: not mentioned in the File Uploads FAQ [DATA by omission].
  - A Jul 2026 community feature request asks for "Transcribe speech from audio and video"; OpenAI Support logged it as a request [PRAC, community.openai.com, 13 Jul 2026].
  - Record mode (macOS desktop; Plus/Pro/Business) transcribes live recordings, not uploaded files [PRAC].
  - A "Meetings" plugin (beta, macOS desktop, Pro/Business) records and deletes the audio [DATA, release notes].

**Claude:**
- Officially supported uploads are documents and images only. No audio or video format is listed [DATA by omission, 23 Jul 2026].
- "Claude currently supports image analysis (vision) but has no ability to process or analyze video files natively" [PRAC, anycap.ai / claudeissues feature request]. A Chinese-language source claiming 15-minute/50 MB video support on Free contradicts the official page; treat it as **false unless tested**.
- No Claude release note from Jun to Oct 2026 mentions audio or video input [DATA, release-notes page read 5 Oct 2026].

**Getting the video in the first place** [PRAC/UNVERIFIED]:
- Instagram and Facebook do not generally offer a download button for others' reels.
- The practical capture is a phone screen-recording, which Meta and TikTok originality rules penalise if reposted.
- Treat any video capture as private study material only.

---

## 5. Route: YouTube transcripts

| Item | Fact | Label |
|---|---|---|
| Vietnamese auto-captions | YouTube automatic captions cover a long language list that **includes Vietnamese** | [DATA, YouTube Help 6373554] |
| Desktop path | Video page → **…more** under the description → scroll → **Show transcript** → select all → copy | [PRAC, recast.studio / anyspeech.io / zapier 2026] |
| Phone path | The transcript can be viewed in the YouTube app, but "mobile apps don't allow you to copy or download transcripts" | [PRAC] → Phase-0 check |
| Transcript via pasted link (ChatGPT/Claude chat) | Not available. Claude respects robots and the transcript endpoints are disallowed. For ChatGPT, third parties say the URL can't be ingested | [DATA robots + PRAC] |
| Transcript via browser agent | ChatGPT side chat: "When captions are available, ChatGPT can use the video's timestamped transcript to explain, summarize, or answer questions." It treats transcripts as untrusted | [DATA, learn.chatgpt.com/docs/chrome-extension, published 5 Oct 2026] |
| Transcript via Claude in Chrome | Not documented. It can read the open page, so opening "Show transcript" first may work | [UNVERIFIED] |
| Paste size in ChatGPT | Pastes **>10,000 characters** become an **attachment** (Free/Go since 22 Jun 2026; all plans by 4 Aug 2026). "Show in text field" turns it back into text | [DATA, release notes] |
| Rough size | 1 minute of speech ≈ 130–160 words ≈ 800–1,000 characters. A 10-minute video already passes 10k characters | [PRAC estimate] |
| ChatGPT Free context | About 27K "instant" context, so a 60-minute transcript may only partly fit | [PRAC via wf11; UNVERIFIED] |
| Claude Free | Long pastes cost usage. Free resets every 5 hours | [DATA, web-search page; usage page via wf11] |

---

## 6. Route: Browse mode (browser agents on a creator's profile)

Capability facts are reused from the `wf10-*` briefs, which were checked against official pages on 5 Oct 2026.

- **Claude in Chrome** [DATA via wf10]:
  - Generally available 26 Aug 2026; Pro, Max, Team and Enterprise. **Not Free.** Desktop Chrome only.
  - Reads the tab the coach is signed in to.
  - Manual approval mode is available; asks per site.
  - "Never" does CAPTCHA bypass or facial-image scraping, and never follows instructions found in web content.
  - **Reddit** is blocked with "This site is not allowed due to safety restrictions" since 18 Sep 2026 [PRAC, GitHub #95326].
  - LinkedIn account-restriction risk [PRAC, GitHub #80986].
- **Cowork built-in browser** (Pro/Max/Team, desktop app) [DATA via wf10]:
  - Logins can be imported per site only from Chrome, Edge or Firefox on macOS, and only from Firefox on Windows.
- **ChatGPT browser extension** [DATA, learn.chatgpt.com, 5 Oct 2026]:
  - Needs the ChatGPT desktop app plus Chrome, Edge, Brave, Opera or Vivaldi. Side chat is not available in Opera.
  - "ChatGPT can read or act on sites where you're already signed in, such as LinkedIn."
  - Asks per site: Allow once / Allow for this site / Allow for all sites / Decline.
  - The extension asks for "Read and change all your data on all websites" and "browsing history" permissions.
  - Free/Go: Work is "Limited (desktop app)". Whether Free can use the extension is [UNVERIFIED] (wf10).
- **ChatGPT Work cloud browser** (Plus/Pro) runs on OpenAI's computer and "doesn't use your personal browser's… signed-in sessions" [DATA via wf10].

**Can it list recent posts with counts, so the machine can compute outliers against the creator's median?** Counts each platform shows to a viewer:

| Platform | Public counts on the profile or grid | Label |
|---|---|---|
| TikTok | Play count on every video tile in the profile grid | [PRAC] |
| YouTube | Views and relative upload date on the channel's Videos and Shorts tabs | [PRAC] |
| Instagram | **Reels tab**: "Anyone can view the counts for posts in the Reels tab". Main grid: view counts only for your own posts. **Creators can hide view counts.** Like counts can also be hidden | [PRAC, lindseygamble.com, 17 Apr, year not shown] |
| Threads | View counts on posts, visible to others on tap. Profile-level views shown above 10k/30 days unless turned off | [PRAC, socialmediatoday / metricool] |
| X | View count on posts | [PRAC; help.x.com page exists but blocked my fetch] |
| LinkedIn | Reactions, comments and reposts only. Impressions visible to the author only | [PRAC/UNVERIFIED] |
| Facebook Page | Reactions, comments and shares on posts. Plays on Reels | [UNVERIFIED] |

So median and outlier maths is **feasible on TikTok, YouTube, IG Reels, Threads and X**. On LinkedIn and Facebook the machine falls back to an engagement proxy. Accuracy and speed of agent listing (about 12–20 posts) is [UNVERIFIED].

**Constraints:**
- Meta's robots header and Terms ban automated collection without permission, "regardless of whether… logged-in" [DATA via wf10].
- LinkedIn's User Agreement bans "browser plugins and add-ons… to scrape or copy" [DATA via wf10].
- Anthropic puts responsibility for site terms on the user [DATA via wf10].
- For the pack, this means:
  - Opt-in only, read-only, one profile at a time, at human pace, with Manual approve.
  - Public creator accounts only; no private people's names stored.
  - Never Facebook groups or comment threads under the "collect" framing without the privacy filter.
  - **Phone-only coaches cannot use Browse at all** (both agents are desktop-only).

---

## 7. Route: saving swipes into the Project (persistent "posts I like" library)

**ChatGPT Projects** [DATA, "Projects in ChatGPT", updated about 20 Sep 2026]:
- "Add reference material to your project by uploading PDFs, spreadsheets, docs, images, **or by pasting text**."
- "**Save a chat response to your project**: open the message menu… Select **Save to project / Add to project sources** (label may vary)."
- "**Add links from apps**… Supported links: **Google Drive** (files and folders), **Slack** (channels)." Social URLs cannot be added as sources.
- File caps: "**Free: 5 files per project · Go, Plus: 25 · Edu, Pro, Business, Enterprise: 40**"; "only 10 files can be uploaded at the same time".
- Whether pasted-text and saved-response sources count toward these caps and toward Free's 3 uploads/day is not stated [UNVERIFIED]. This was already flagged in wf11.
- Library: Free has 500 MB of Library storage [DATA, Free tier FAQ]. **Add from library** on the web lets you reuse a saved file without uploading it again (7 Aug 2026) [DATA]. Whether attaching from Library counts as an upload is [UNVERIFIED].
- Memory in projects: Plus/Pro can reference earlier chats in the same project [DATA]. Free relies on sources and saved memories.

**Claude Projects** [DATA, support.claude.com 9519177 and 9517075, "updated this week"]:
- "Projects are available to all users, including those with free Claude accounts. Free users can create a maximum of five projects."
- "Click on the '+' button to add content to the project. Upload relevant documents, text files, or code snippets." The exact "add text content" label in Oct 2026 is [UNVERIFIED].
- "Enhanced project knowledge with RAG is only available to users with paid Claude plans… expand capacity by up to 10x."
  - **On Free, every saved swipe sits in the context window**, which also eats into usage.
- Project files: 30 MB each; "Unlimited, but total content must fit within Claude's context window" [DATA, upload page].
- Chats can be moved into a project with "Add to project" [DATA].

**Design-relevant consequence (inference):**
- Swipes should be stored as **one running text source** ("Swipe file") that the machine rewrites or appends to. A source per post doesn't scale.
- The stored entry should be the **pattern** (hook type, structure, angle, why it worked, numbers), not the full copied post. This keeps it small and stays on the right side of originality and copyright.

---

## 8. Platform rules on reposting and "unoriginal content"

| Platform | Rule (date) | What triggers it | Consequence | Label and source |
|---|---|---|---|---|
| **Facebook** | "Cracking down on unoriginal content" (14 Jul 2025) | Reusing others' content without meaningful enhancements; duplicate videos | Duplicates get reduced distribution. Repeat offenders lose monetisation "for a period". Meta was testing links on duplicates pointing to the original | [PRAC, tubefilter / medianama / plagiarismtoday, 15–16 Jul 2025] |
| **Facebook** | "Rewarding Original Creators on Facebook" (**13 Mar 2026**) | "Simply watching along, reacting with facial expressions, stitching multiple clips together, or narrating what's already on screen — without adding anything meaningful"; "duplicative or… minor edits"; "low-value changes" such as borders, captions or speed | Deprioritised in Feed and Reels. Account can become **non-recommendable**. Demonetisation. Allowed: "an on-screen presence from a creator presenting something genuinely new — like fresh information, analysis…" | [DATA, about.fb.com] |
| **Instagram** | Recommendation guidelines (ongoing) | "Less likely to recommend reposts of content already on Instagram, content with noticeable watermarks, or accounts that regularly collect and reshare others' content" | Not recommended to non-followers | [DATA, help.instagram.com 313829416281232 via search snippet] |
| **Instagram** | Originality rule extended to **photos and carousels** (**30 Apr 2026**) | Reposts without significant changes, including "simple screenshots showing original creator attribution". Original means "unique text, creative edits, and voiceover… a relatable take" | Mostly-reposting accounts lose recommendation eligibility (Explore, Reels, suggested). Followers still see them | [PRAC, tubefilter 30 Apr 2026; official post not located → re-check] |
| **Meta (overall)** | "2026: AI Drives Performance" (Jan 2026) | — | 75% of US Instagram recommendations come from original posts (Q4 2025) | [DATA via search snippet, about.fb.com] |
| **TikTok** | Community Guidelines, Integrity & Authenticity (last updated 5 May 2026 per tracker) | "Content is also ineligible for the FYF if it includes **unoriginal or reused material without anything new**." IP-violating content is removed | Not recommended in For You. Reach collapses | [DATA, tiktok.com/community-guidelines/en/integrity-authenticity, read 5 Oct 2026; date from conductatlas] |
| **YouTube** | YPP: "Inauthentic content" (renamed from "repetitious", **15 Jul 2025**) and "Reused content" | Reused: repurposing "without adding significant original commentary, substantive modifications, or educational or entertainment value". Not allowed: "Content downloaded or copied from another online source without any substantive modifications"; "Content that exclusively features readings of other materials" | Channel-level monetisation loss. Reaction, commentary and critical review with clips are allowed | [DATA, support.google.com/youtube/answer/1311392] |
| YouTube "July 2026 update" | Some blogs claim a 15 Jul 2026 revision naming AI content | — | — | [UNVERIFIED; probably a misdated copy of the 2025 change] |
| LinkedIn / X | Not researched in this pass | — | — | — |

**Implications for remixing (inference from the rules above):**
- Borrowing a **format, hook pattern, structure or angle**, then filling it with the coach's own story, proof, numbers and voice, is "something genuinely new". This is the method's authenticity rule anyway.
- Penalised: reposting a screenshot of someone else's post (even with credit), re-uploading clips, reading another creator's caption to camera, near-duplicate captions.
- The machine's output should never be a close paraphrase of the source. Quoting a line needs attribution and should be rare.

---

## 9. What this means for the feature (short, factual)

1. **Default intake = screenshot or paste**, which works on phone and on Free in both apps. Ask for one post at a time.
   - **ChatGPT Free** has a 3/day upload budget, so a carousel should be "send the 2–3 key slides" or "paste the caption".
   - **Claude** can take a whole carousel (≤20) in one message.
2. **A link is a bonus, never the plan.**
   - Newsletters and blogs: yes.
   - YouTube: ask for the transcript text (desktop) or the coach's two-line summary (phone).
   - IG, TikTok, FB, LinkedIn, Threads, X links on Claude: the machine should not even try. It should ask for a screenshot straight away, as the one question in that reply.
   - On ChatGPT: try once, and if nothing useful comes back, ask for a screenshot.
3. **Video:** don't ask for video files.
   - On ChatGPT a short screen recording is allowed but unreliable.
   - On Claude it is impossible.
   - Spoken words arrive as a transcript or the coach's summary.
4. **"Channels I follow" (whole-profile analysis)** is a **paid, desktop, opt-in Browse feature**: Claude Pro + Chrome, or ChatGPT Plus + desktop app + extension. On Free and phone, the fallback is the coach screenshotting the profile grid, which shows counts on TikTok, YouTube and IG Reels, and the machine reading the numbers off it.
5. **Persist patterns, not posts:** one "liked-posts pattern" text source per project, appended through "save this:" / "lưu lại:".

---

## 10. Phase-0 hands-on checks to add

(Each: run on ChatGPT Free and Plus, and on Claude Free and Pro, phone app and desktop or web, with an EN and a VN example. Record exactly what the model received.)

1. Paste a public **Instagram reel** URL, then a **TikTok** video, a **Facebook public Page post**, a **LinkedIn** post, a **Threads** post, an **X** post, a **YouTube** video and a **Substack** post. Log, per app, plan and device: refused / caption only / full text / counts / transcript.
2. **ChatGPT Free upload budget:** how many screenshots before "upload limit reached"? Do images share the 3/day file cap? What is the per-message maximum? Is the rolling 24 h reset as reported?
3. **ChatGPT Free:** does a >10k-character paste (auto-attachment) count toward the 3/day cap? Does "Show in text field" avoid it?
4. **Vietnamese OCR:** five VN caption or carousel screenshots (diacritics, stylised fonts, text over images). Exact-transcription accuracy on ChatGPT (Free/Luna; Plus/Sol) and Claude (Free, Pro).
5. **Carousel:** 10 separate slides in one message (Claude ≤20; ChatGPT ≤10?) versus one stitched tall image. Confirm stitched images lose legibility.
6. **Phone share sheet:** share an IG, TikTok, FB and YouTube post from the social app straight into the ChatGPT and Claude apps. Does a link, preview image or nothing arrive?
7. **Caption copying on phones:** in each social app (IG, TikTok, FB, LinkedIn, Threads, X, YouTube description), can a coach select and copy the caption text? List the apps where screenshot is the only route.
8. **ChatGPT video:** upload a 30–60 s screen recording of a reel (EN and VN speech, plus on-screen text) on Free and Plus, phone and web. Is speech transcribed? Is on-screen text read? Does it count as one upload? Is a 90 s, 100 MB file accepted?
9. **Claude video:** confirm an mp4 is rejected on Free and Pro (web and phone). With code execution on, can an mp4 enter the sandbox and have frames extracted (no audio)?
10. **ChatGPT audio:** upload an m4a voice memo. Is it accepted and transcribed, on Free and on Plus?
11. **YouTube transcript route:** desktop "Show transcript" copy-paste of a 20-minute VN video into ChatGPT Free and Claude Free. Does it fit? Quality? Then try copying the transcript on the YouTube phone app.
12. **ChatGPT extension side chat on a YouTube video:** does it work on Free and Go (Work is "limited"), and on Plus? Does it read VN auto-captions?
13. **Claude in Chrome (Pro):** open a YouTube video with "Show transcript" open. Can it read the transcript panel?
14. **Browse listing:** with Claude in Chrome (Pro) and the ChatGPT extension (Plus), open a TikTok profile, a YouTube Videos tab, an IG Reels tab and a Threads profile. Ask for the last 12–20 posts with date and view count. Measure accuracy against a manual count, time taken, CAPTCHAs or blocks, and approval prompts. Confirm it stays read-only and stores no private names.
15. **Browse on LinkedIn and Facebook Pages:** check which counts are visible, and whether an account warning appears after one low-volume read.
16. **Check the Reddit block** in Claude in Chrome and test whether any other social domain shows "not allowed due to safety restrictions".
17. **ChatGPT Project, Free:** "Save to project" a reply and "paste text" as a source. Do they count toward the 5-file cap? Are they available on the phone app? What is the exact menu label in EN and VN UI?
18. **Claude Project, Free:** add a text swipe as knowledge from web and from the phone app. Exact label? How much context does a 30-entry swipe file consume? Does the coach hit the Free 5-hour cap sooner?
19. **Claude Free budget:** how many "screenshot → pattern → rewrite in my voice" cycles fit in one 5-hour window?
20. **Hidden-count fallbacks:** an IG account with hidden view counts and a LinkedIn creator. Confirm the machine switches to likes or comments, or to a "relative to their other posts" judgement.
21. **Policy re-check before launch:** locate Instagram's own 30 Apr 2026 announcement (only Tubefilter seen), confirm or kill the claimed YouTube "15 Jul 2026" update, and read Meta's Automated Data Collection Terms page directly.

---

## 11. Corrections and conflicts with earlier briefs

- **wf11** said Claude "Code execution and file creation" is on by default for Free/Pro/Max (help page dated 6 Aug 2026). The same page re-read today says "enabled by default for **Pro, Max, Team, and Enterprise**", which does not list Free. Re-check on a Free account.
- **Claude per-file limits conflict:** 500 MB (Upload files, 23 Jul 2026) versus 30 MB (Create and edit files, 6 Aug 2026). Irrelevant for screenshots.
- The ChatGPT File Uploads FAQ wording "Free users are limited to 3 file uploads per day" is confirmed verbatim today (wf11 had it from snippets).
- The ChatGPT Projects page still says "agent mode" exists on paid plans. wf10 found agent mode removed, so the Projects page is stale on this point.

---

## Sources (all read 5 Oct 2026 unless noted)

**OpenAI** (read through r.jina.ai because direct fetch returns 403)
- File Uploads FAQ: https://help.openai.com/en/articles/8555545-file-uploads-faq ("Updated: 24 days ago")
- ChatGPT Image Inputs FAQ, including "Can I upload videos": https://help.openai.com/en/articles/8400551-chatgpt-image-inputs-faq ("Updated: last month")
- ChatGPT Free Tier FAQ: https://help.openai.com/en/articles/9275245-chatgpt-free-tier-faq (2 months ago)
- What is ChatGPT Go: https://help.openai.com/en/articles/11989085-what-is-chatgpt-go (2 months ago)
- Projects in ChatGPT: https://help.openai.com/en/articles/10169521-projects-in-chatgpt (15 days ago)
- Searching the web with ChatGPT: https://help.openai.com/en/articles/9237897-chatgpt-search
- ChatGPT Voice: https://help.openai.com/en/articles/20001274-chatgpt-voice (10 days ago)
- GPT-5.6 and GPT-6 Pro in ChatGPT: https://help.openai.com/en/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt
- ChatGPT release notes (entries 22 Jun, 4 Aug, 7 Aug, 31 Aug, 1 Oct, 2 Oct 2026): https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- OpenAI crawlers (ChatGPT-User): https://platform.openai.com/docs/bots
- Browser extension (YouTube transcript, site permissions): https://learn.chatgpt.com/docs/chrome-extension (published 5 Oct 2026)

**Anthropic**
- Upload files to Claude (23 Jul 2026): https://support.claude.com/en/articles/8241126-upload-files-to-claude
- Enable and use web search: https://support.claude.com/en/articles/10684626-enable-and-use-web-search
- Anthropic crawlers and robots.txt (7 Apr 2026): https://support.claude.com/en/articles/8896518
- Create and edit files (6 Aug 2026): https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude
- Create and manage projects: https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
- What are projects: https://support.claude.com/en/articles/9517075-what-are-projects
- Release notes: https://support.claude.com/en/articles/12138966-release-notes
- Vision (limits, downscaling, limitations): https://platform.claude.com/docs/en/build-with-claude/vision
- Web fetch tool (JavaScript, robots, content types): https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool
- Web search on all plans (27 May 2025): https://claude.com/blog/web-search
- Mobile photo upload and widgets: https://support.claude.com/en/articles/10534883-use-the-claude-widget-on-android , https://support.claude.com/en/articles/10263469-use-claude-app-intents-shortcuts-and-widgets-on-ios

**Platforms**
- robots.txt (downloaded 5 Oct 2026): instagram.com, facebook.com, threads.com, x.com, tiktok.com, linkedin.com, youtube.com, substack.com, reddit.com (blocked)
- YouTube automatic captions languages (includes Vietnamese): https://support.google.com/youtube/answer/6373554
- YouTube channel monetization policies (inauthentic and reused content): https://support.google.com/youtube/answer/1311392
- Meta, Rewarding Original Creators on Facebook (13 Mar 2026): https://about.fb.com/news/2026/03/rewarding-original-creators-on-facebook/
- Meta, 2026: AI Drives Performance (snippet): https://about.fb.com/news/2026/01/2026-ai-drives-performance/
- Instagram, Recommendations (snippet): https://help.instagram.com/313829416281232
- TikTok Community Guidelines, Integrity & Authenticity: https://www.tiktok.com/community-guidelines/en/integrity-authenticity
- TikTok guideline version tracker: https://conductatlas.com/platform/tiktok/tiktok-community-guidelines/for-you-feed-eligibility-exclusion/

**Third-party [PRAC]**
- Tubefilter, Instagram aggregator penalty (30 Apr 2026): https://www.tubefilter.com/2026/04/30/instagram-removes-algorithm-recommendations-repost-content-aggregator/
- Facebook Jul 2025 crackdown: https://www.tubefilter.com/2025/07/15/ai-slop-unoriginal-repetitive-content-monetization-facebook-meta/ , https://www.medianama.com/2025/07/223-meta-cracks-down-on-unoriginal-facebook-content/ , https://www.plagiarismtoday.com/2025/07/16/facebook-to-fight-unoriginal-content/
- ChatGPT and YouTube (9 Jul 2026): https://www.usecarly.com/blog/chatgpt-youtube-integration/
- ChatGPT video analysis (2 Sep 2026): https://vomo.ai/guide/can-chatgpt-analyze-videos ; https://www.cometapi.com/can-chatgpt-watch-videos/
- mp3/mp4 feature request (13 Jul 2026): https://community.openai.com/t/new-chatgpt-mp3-and-mp4-file-support/1386629
- Claude audio and video: https://vomo.ai/guide/can-claude-ai-transcribe-audio , https://sonix.ai/ai/can-claude-transcribe-audio/ , https://claudeissues.com/issue/32130-feature-request-native-video-analysis-support-in-claude
- Image upload caps: https://merlio.app/blog/chatgpt-image-upload-limits (19 Jan 2026) ; https://blog.laozhang.ai/en/posts/chatgpt-plus-image-upload-limit (updated 14 Jul 2026) ; https://claudecodeguides.com/claude-upload-limit-guide/
- YouTube transcript how-tos: https://recast.studio/blog/how-to-get-transcript-of-youtube-video , https://anyspeech.io/blog/how-to-get-a-transcript-of-a-youtube-video , https://zapier.com/blog/youtube-video-transcript
- Instagram view counts: https://lindseygamble.com/blog/instagram-rolls-out-grid-view-counts-to-more-users
- Threads view counts: https://www.socialmediatoday.com/news/threads-adds-view-counts-on-posts/715725/ , https://metricool.com/threads-adds-view-counts/
- Claude and social links: https://marketbetter.ai/blog/can-claude-connect-to-linkedin/
- originality.ai Browse-with-Bing block study (2023, historical): https://originality.ai/blog/what-websites-can-chatgpt-browse-with-bing
- Earlier internal briefs (same day): `wf10-claude-computer-use.md`, `wf10-chatgpt-computer-use.md`, `wf11-ux-facts.md`
