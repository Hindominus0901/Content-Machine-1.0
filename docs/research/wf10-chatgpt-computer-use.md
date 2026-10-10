# ChatGPT browser and computer-use options for the Research module's Browse mode (checked 5 Oct 2026)

**Bottom line:** the "Browse" route on ChatGPT is now the **ChatGPT desktop app plus the ChatGPT browser extension**, running in the coach's own Chrome, Edge, Brave or Vivaldi. It is the closest thing to Claude in Chrome. OpenAI's own docs say it can "read or act on sites where you're already signed in, such as LinkedIn". The Work launch post says the desktop app includes Chat, Work and Codex on every plan, Free included, and the pricing table lists Work as "Limited (desktop app)" on Free and Go.

The other options:
- **ChatGPT Work's cloud browser** (Plus and Pro only) runs on OpenAI's computer, not the coach's. It does not use their logged-in sessions.
- **ChatGPT agent, Operator and Atlas are all gone.**

## 1. Checking the earlier brief's two claims

| Claim | Verdict | Evidence (date) |
|---|---|---|
| "ChatGPT agent removed in Aug 2026" | **Removed: true. The August date is unverified and probably earlier.** | The help article now opens with: "ChatGPT agent is no longer available. Use ChatGPT Work for longer, multi-step tasks… For supported browser workflows, see Using cloud browser" (page updated about 15 Sep 2026). The release notes have **no dated retirement notice**. Users reported agent mode missing from 8–18 Jul 2026, and a complaint thread opened 8 Aug 2026. OpenAI Support confirmed the removal in community posts on 7 Sep and 25 Sep 2026. Wikipedia says "early August 2026, without advance deprecation notice". |
| "ChatGPT Work launched July 2026" | **True: 9 Jul 2026** (official release notes and the launch post) | Rolled out to Pro, Pro Lite, Enterprise and Edu first, then Plus and Business "over the coming days". Free and Go get it on web and mobile only through the desktop app (limited). |
| Atlas | **Deprecated 9 Jul 2026; stopped working 9 Aug 2026** (official) | It was only ever on macOS (launched 21 Oct 2025). The Windows, iOS and Android versions were promised but never shipped. |
| Operator | **Gone.** The help article says: "Operator functionality is now integrated into ChatGPT agent mode. The Operator website is no longer accessible." | Wikipedia gives the site shutdown as 31 Aug 2025. |

**Corrections to the source map (`wf7-source-map.md`):**
- **G4** wrongly says Atlas was "replaced by ChatGPT Work + Chrome extension". Officially the replacements are the desktop app (built-in browser), the browser extension, and Work's cloud browser.
- **G5** lists "Plus, Pro, Business" for website sign-in. Officially, sign-in in the cloud browser is **Plus and Pro only**, and it "isn't available for Enterprise or Edu workspaces".
- **G5** also cites "Agent mode 40 msgs/month". That figure belongs to the retired agent, so it no longer applies.

## 2. Options table (5 Oct 2026)

| Option | Status | Plans | Platforms | Uses the coach's own logged-in session? | Social listening: can | Social listening: can't or risky | Quota and speed | Safety confirmations |
|---|---|---|---|---|---|---|---|---|
| **A. Desktop app + browser extension ("@Chrome", side chat)** | Live. Chrome Web Store listing by OpenAI, v1.26.901, updated 4 Sep 2026, 6M users, rated 2.8★. Edge, Brave, Opera and Vivaldi added 31 Aug 2026. | All plans can install the app (launch post, 9 Jul 2026). Work is "Limited (desktop app)" on Free and Go, which get GPT-6 Luna only. **Free use of the extension is not confirmed in-app.** | Desktop app on macOS and Windows (Linux preview since 14 Aug 2026), plus a Chromium browser. No mobile. | **Yes.** It works in the coach's real browser profile, with their cookies and tabs. | Read the open page: Facebook groups the coach is in, YouTube, TikTok, IG, LinkedIn, X, reviews, Ad Library. With @Chrome in a Work chat it can scroll and click. **YouTube videos with captions are officially supported:** it uses the timestamped transcript. | Comments that load lazily need scrolling. Reading comments is **not documented, so test it**. Meta, LinkedIn and X terms forbid automated scraping. Zalo is an app, so the extension doesn't reach it. | Draws on the shared Work/Codex allowance (see option C). Acts live in the coach's own browser. No published speed figures. | Asks before **each new website**: Allow once / Allow for this site / Allow for all sites (marked elevated risk) / Decline. Allow and block lists. History access is asked for every time and has no always-allow. |
| **B. Desktop app built-in browser ("@Browser", Ctrl/Cmd+Shift+B)** | Live (9 Jul 2026) | Pricing table shows it on Free, Go, Plus and Pro | macOS and Windows desktop app | **No.** It has its own profile. The coach signs in by hand inside it, and it runs on their own computer and IP. | Public pages and logged-in pages after a manual sign-in. Tabs and downloads work. | Can't automate file uploads. It doesn't share the coach's Chrome session. | Same shared allowance | Asks before using a new site. Asks before submitting, purchasing, changing permissions or deleting. |
| **C. ChatGPT Work cloud browser** | Live. Website sign-in added 25 Aug 2026. | Plus and Pro. "Excluding Free and Go." | Web and iOS/Android (also cloud Work chats from desktop) | **No.** It is "a separate computer in the cloud" and "doesn't use your personal browser's… cookies… or existing signed-in sessions". | Public pages: Meta Ad Library, competitor sites, some review sites. OpenAI's own example is "Research competitors on social media." It keeps running when the laptop is closed. | Logging into the coach's own Facebook or LinkedIn here hands those sessions to a cloud browser, and data-centre logins may trigger checkpoints (unverified). OpenAI says some sites block automated browsers or require a CAPTCHA, and a MacStories test (26 Aug 2026) hit login failures and freezes. | Plus, local messages per 5 hours: GPT-6 Luna 350–3,000; GPT-6.1 Sol 15–160; GPT-6 Astra 5–45. **Cloud tasks use more.** Weekly caps may apply and credits can be bought. Pro has no 5-hour cap. | Settings > Cloud browser: **Always ask** / Auto approve / Always allow (not recommended). A phishing-check model reviews sign-in requests, and the password form is masked. Confirms "consequential actions". The coach can take over the browser. |
| **D. Computer Use plugin (@Computer, @AppName)** | Live | Work or Codex in the desktop app; "supported regions" (list not published; **Vietnam unverified**) | macOS and Windows. On Windows it takes over the mouse and keyboard. | Yes, any app on the computer, including the real browser and the Zalo PC app. | In principle, any app on the computer. | **Too much power for a coach pack.** Screenshots of whatever is on screen are processed. Using it on Zalo groups breaks the pack's red-rule and VN data-law line. | Shared allowance | Asks per app, with an "Always allow" option. Asks before sensitive actions. |
| **E. Deep research** | Live | Free and Go "Limited"; Plus yes; Pro "Maximum". The help page publishes **no numbers** (usage counter in the product, 30-day reset). | Web, mobile, desktop | No | Public web, uploaded files, connected apps. "Sites > Manage sites" can restrict it to domains such as voz.vn or reddit.com. | No logins, so no Facebook groups, comments or Ad Library. | Minutes per report | Read-only use of apps |
| **F. Plugins / connectors** | The Plugin Directory replaced the App Directory on 9 Jul 2026 | Varies | Varies | Through OAuth | **Meta Ads AI Connectors** (official, open beta since 29 Apr 2026, `mcp.facebook.com/ads`) reach **your own ad accounts only**. They don't cover the Ad Library or competitors' ads. vidIQ and Metricool (third-party) cover your own channels. | **No official Facebook-groups, YouTube-comments, TikTok or IG-comments plugin** was in the directory on 5 Oct 2026. Scraper plugins such as Firecrawl are out under rule 6. | — | — |
| ChatGPT agent / agent mode | **Gone** (see §1) | — | — | — | — | — | It was 40 per month on Plus and 400 on Pro. History only. | — |
| Atlas, including its agent mode, "logged-out mode" and "pauses on sensitive sites such as financial institutions" | **Gone since 9 Aug 2026** | — | Was macOS only | — | — | Logged-out mode and watch-on-sensitive-sites have **no documented equivalent** in A–C. The equivalents are the per-site approvals above. | — | — |

## 3. How a coach starts each one (exact clicks, from the official docs)

**A. Extension (recommended Browse route)**
1. Install the ChatGPT desktop app (Mac or Windows) and sign in.
2. In the app, go to **Settings > Computer Use**. Pick Chrome (or Edge, Brave, Vivaldi; use **More browsers** if it isn't listed) and click **Install**.
3. In the Chrome Web Store, add the extension and accept the permissions.
4. Back in **Computer Use**, check that Chrome shows **Manage**.
5. Two ways to use it:
   - **Side chat:** open the Facebook group, YouTube video or Ad Library page in Chrome. Click the ChatGPT toolbar icon (Mac: Cmd+Shift+.) and paste the Collect prompt.
   - **Agent-style:** in the desktop app, choose **ChatGPT** (top-left), then the **Work** toggle, and type `@Chrome read the open tab …`.
6. When it asks to use a site, choose **Allow once**. Never choose "Allow for all sites", and decline browser-history access.
7. Under **Settings > Computer Use > Manage**, blocklist banking and email domains.

**B. Built-in browser**
1. In the desktop app, choose **ChatGPT**, then **Work**.
2. Press **Cmd/Ctrl+Shift+B**, open a **New tab**, go to the site and sign in yourself.
3. Ask: "use the current page…". Approve the site when asked.

**C. Cloud browser (Plus or Pro)**
1. Open chatgpt.com or the mobile app and select **Work**.
2. Describe the task and include the URL.
3. Approve website access when prompted.
4. If a sign-in is needed, use the secure form or **Sign in on web page instead**, then **I'm done**.
5. Take over the browser if a CAPTCHA appears.
6. Afterwards, go to **Settings > Cloud browser > Browser data > Clear all**.

**E. Deep research**
1. Click **+ > Deep research**, or type `/Deepresearch`.
2. Optionally use **Sites > Manage sites** to list domains.
3. Review the research plan before it starts.

## 4. Terms and privacy cautions for the pack

- **Extension permissions are broad.** They include "Read and change all your data on all websites" and "your browsing history on all your signed-in devices". OpenAI says it "doesn't store a separate complete record of your browser actions", but anything ChatGPT reads becomes chat content, and ChatGPT data controls apply to it. Training is opt-out on Free, Go, Plus and Pro.
- **Prompt injection.** OpenAI's docs say to treat page content, selected text and transcripts as untrusted.
- **Astra pauses (3 Sep 2026).** GPT-6 Astra may pause or stop a conversation when its safety monitor fires.
- **Lockdown Mode (4 Jun 2026).** If a coach turns it on, live browsing and deep research are blocked.
- **The cloud browser keeps cookies** between tasks, so clear them after use.
- **Platform terms:**
  - LinkedIn's User Agreement (effective 3 Nov 2025, re-read 5 Oct 2026) bans "browser plugins and add-ons… to scrape or copy" and "bots or other unauthorized automated methods". Treat LinkedIn as amber/red and low-volume.
  - Meta's terms against automated collection without permission were not re-fetched today; that is from memory and unverified.
- **Vietnam:**
  - Vietnam is on OpenAI's supported-countries list (page updated about Aug 2026).
  - The cloud browser is "available in all regions on paid plans other than Free and Go".
  - The desktop app is global.
  - There is a Vietnamese help centre (help.openai.com/vi-vn).
  - Local prices are third-party figures: Go 132,000đ/month (launched in VN Oct 2025); Plus about 499,000–571,000đ (sources conflict).
- **Reliability:** on 5 Oct 2026 the help centre showed an "Elevated Work Mode errors" incident banner.

## 5. Still unverified (check in a real account before shipping)
- Whether Free and Go accounts can use the extension's browser control, beyond "Limited Work (desktop app)".
- Whether the extension reliably scrolls and captures TikTok, IG, YouTube and Facebook comments.
- Whether the cloud browser can open Meta Ad Library, Shopee or Trustpilot without CAPTCHAs.
- Whether Computer Use is offered in Vietnam.
- Numeric deep-research quotas. The earlier G1 figures are third-party only.
- The exact date ChatGPT agent was removed.

One housekeeping note: an early `curl` test saved a 10 KB Cloudflare 403 page to `/tmp/claude-0/-home-user-Content-Machine-1-0/085f5f0b-5883-504d-aefb-4af9a99859d9/scratchpad/agent.html`. That is the session scratchpad, not the project. Nothing else was written.

## Sources (all accessed 5 Oct 2026)
- ChatGPT release notes (entries 9 Jul, 25 Aug, 31 Aug, 3 Sep, 29 Sep 2026; 4 Jun 2026): https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- ChatGPT agent, "no longer available" (updated about 15 Sep 2026): https://help.openai.com/en/articles/11752874-chatgpt-agent
- Evolving Atlas into ChatGPT: https://help.openai.com/en/articles/20001371-evolving-atlas-into-chatgpt-for-browser-based-agentic-work · VN version: https://help.openai.com/vi-vn/articles/20001371-evolving-atlas-into-chatgpt-for-browser-based-agentic-work
- Atlas release notes: https://help.openai.com/en/articles/12591856-chatgpt-atlas-release-notes · Atlas launch post (21 Oct 2025): https://openai.com/index/introducing-chatgpt-atlas/
- ChatGPT Work and Codex: https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex · Work launch post (9 Jul 2026): https://openai.com/index/chatgpt-for-your-most-ambitious-work/
- Cloud browser: https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt · https://learn.chatgpt.com/docs/browser
- Built-in browser: https://help.openai.com/en/articles/20001277-using-the-built-in-browser-in-the-chatgpt-desktop-app
- Browser extension: https://learn.chatgpt.com/docs/chrome-extension · Chrome Web Store listing: https://chromewebstore.google.com/detail/chatgpt/hehggadaopoacecdllhhajmbjkdcmajg
- Computer Use: https://learn.chatgpt.com/docs/computer-use
- Work/Codex usage limits: https://learn.chatgpt.com/docs/pricing · Plan comparison: https://chatgpt.com/pricing
- Codex plans: https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan
- Deep research: https://help.openai.com/en/articles/10500283-deep-research-in-chatgpt
- Supported countries: https://help.openai.com/en/articles/7947663-chatgpt-supported-countries
- Community threads: https://community.openai.com/t/agent-mode-missing-across-all-platforms-on-pro-account/1387374 · https://community.openai.com/t/agent-mode-was-removed-with-no-real-replacement/1389601 · https://community.openai.com/t/agent-mode-menu-disappeared-after-recent-performance-issues-plus-plan/1386007
- Wikipedia: https://en.wikipedia.org/wiki/OpenAI_Operator · https://en.wikipedia.org/wiki/ChatGPT_Atlas
- Meta Ads AI Connectors: https://www.facebook.com/business/news/meta-ads-ai-connectors · https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-overview
- Plugin directory: https://chatgpt.com/plugins
- LinkedIn User Agreement: https://www.linkedin.com/legal/user-agreement
- Press: MacStories, 26 Aug 2026: https://www.macstories.net/stories/hands-on-with-chatgpt-works-new-cloud-browser-feature/ · Android Authority, 7 Aug 2025 (old agent on Facebook): https://www.androidauthority.com/chatgpt-agent-review-3583538/ · 9to5Mac, 9 Jul 2026: https://9to5mac.com/2026/07/09/openai-is-discontinuing-chatgpt-atlas-its-standalone-desktop-browser/ · Tuổi Trẻ: https://tuoitre.vn/openai-khai-tu-trinh-duyet-atlas-chuyen-cac-tinh-nang-sang-chatgpt-100260717165346252.htm
- VN prices (third-party): https://fptshop.com.vn/tin-tuc/for-gamers/bang-gia-chatgpt-197750 · https://bestapp.vn/blog/chatgpt-go-la-gi