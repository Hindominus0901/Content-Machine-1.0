# Claude's computer-use and browser-agent options for social listening (checked 5 Oct 2026)

I checked every fact on 5 Oct 2026 against official pages first: support.claude.com, claude.com, anthropic.com, privacy.claude.com and the Chrome Web Store. Anything I couldn't confirm officially is marked **UNVERIFIED**. This covers the Claude side only. ChatGPT gets a short cross-check at the end. I didn't create or edit any project files.

## What changed since the spec was written (Sep–Oct 2026)

- **26 Aug 2026: Claude in Chrome is generally available** on every paid plan (Pro, Max, Team, Enterprise). The earlier claim is now confirmed by Anthropic's own blog. On the same date Anthropic added a self-checking "Automatically approve" mode, where a separate safety check reviews each action before it runs.
- **26 Aug 2026: Cowork got a built-in browser** inside the Claude Desktop app (macOS, Windows, Linux in beta) for Pro, Max and Team. If the coach already has Claude in Chrome, Chrome stays the default browser. Otherwise the built-in one is used.
- **16 Sep 2026: "Cowork and chat are one Claude"** is rolling out to Pro and Max. In that new experience there is no "Chat"/"Cowork" choice and no web-search toggle. Research is opened with `/deep-research` or **+ → Research**. Actions default to **Manual** approval.
- **6 Oct 2026 (tomorrow):** new Cowork tasks on Pro and Max run in Anthropic's cloud, and the "Only on your computer" option is removed. Browsing, computer use and local files still need the Claude Desktop app to be open.
- **Chrome side panel is now a Cowork session.** That's live on Max and Team and still rolling out to Pro. Sessions are saved to the coach's history and sync to web, desktop and mobile. The old ("classic") panel is still available, and recorded workflows only work there.
- **Reddit is blocked inside Claude in Chrome since 18 Sep 2026.** The message is "This site is not allowed due to safety restrictions." This is **user-reported only** (GitHub issue #95326, still open with no Anthropic reply; dev.to, 28 Sep). Anthropic's docs don't mention it.
- **Extension details:** version 1.0.98, updated 2 Oct 2026. The extension's interface is **English (US) only**.

## Main table: the Claude options

| Option | Plans and price (5 Oct 2026) | Device | How a non-technical coach starts it | Uses the coach's own logins? | Quotas | Safety checks |
|---|---|---|---|---|---|---|
| **A. Claude in Chrome, side panel** (generally available since 26 Aug 2026; the panel itself is still labelled beta) | Pro ($20/month, or $17/month billed yearly), Max (from $100), Team, Enterprise. **Not Free.** | Desktop Google Chrome only. Not other Chromium browsers (Edge, Brave), not phones. | 1) Subscribe at claude.ai/upgrade. 2) In Chrome, open the Chrome Web Store page "Claude" by Anthropic → **Add to Chrome**. 3) Sign in to Claude. 4) Puzzle icon → pin **Claude**. 5) Open the page, e.g. a Facebook group → click the **Claude icon**. 6) Pick **Manually approve** in the drop-down on the message box. 7) Paste the prompt. On each site prompt choose **Allow this time only**, **Allow all for this website** or **Deny**. In the classic panel Claude shows a plan first → **Approve plan**. | **Yes.** Claude reads the tab the coach is already signed in to, and that tab is all it needs. Without the desktop app it can only read the tab the coach is on; having Claude drive Chrome as part of a bigger task needs the desktop app. | No separate quota. Counts against the plan's 5-hour session limit and weekly limit (Settings → Usage). **Auto mode uses more of the limit.** Max gives 5x or 20x Pro. | **Manually approve**: asks before every action. **Automatically approve** is the Cowork-panel default (the action safety check is skipped in "Skip all approvals" mode). **Skip all approvals**: no checks. **Always asks** before downloads, typing sensitive data, granting authorisations and changing permissions. **Never** does purchases, account creation, CAPTCHA bypass, permanent deletes, facial-image scraping, or instructions found in web content. **Blocked** sites: adult and pirated content. **Asks first** on financial sites. |
| **B. Cowork, driving Claude in Chrome** | Paid plans | Claude Desktop (Mac or Windows) plus Chrome. From web or phone it also works if the session is connected to a desktop. | Desktop app → initials (bottom left) → **Settings → Connectors → Claude in Chrome → Configure** → toggle on. Then turn it on per chat from the **Connectors** drop-down, which is off by default. Or set **Settings → Cowork → Preferred browser → Chrome**. | Yes, the coach's own Chrome. | Same plan limits | Same as A. |
| **C. Cowork built-in browser** (26 Aug 2026; was "rolling out" at that time) | Pro, Max, Team. Enterprise if an admin turns it on. | Claude Desktop on macOS 11+, Windows 10+, or Ubuntu 22.04+/Debian 12+ (beta). Desktop must be open and online; can be steered from web or phone. | Install from claude.com/download → sign in → start a task (or pick "Cowork" in the message box) → a browser opens in the side panel when a site is needed. The first time it shows **Import cookies**. | Separate from the coach's own browser. Logins can be imported **site by site from Chrome, Edge or Firefox on macOS, but only from Firefox on Windows and Linux.** No Safari. Otherwise the coach signs in inside the panel, and **those logins are kept for future sessions on that computer.** Banking, email and single-sign-on sites are unticked by default. | Same plan limits | Same safeguards as Chrome: permission before the first action on each site, high-risk sites blocked, every action checked. |
| **D. Computer use (Cowork / Claude Code)** (research preview 23 Mar 2026, still beta) | **Pro and Max only.** Team and Enterprise don't have it. | Claude Desktop on macOS or Windows. The computer must be awake. | Desktop app → **Settings → General (under Desktop app) → Enable computer use** → start a task → approve each app when asked. | Uses whatever apps are on screen. Claude prefers a connector first, then a browser, and only then clicks around the screen. | Same plan limits. Slowest option. | Asks per app. Investment, trading and crypto apps blocked by default. The coach can add apps to a blocklist. **No sandbox:** a link clicked in one app opens even in apps Claude wasn't allowed to use. |
| **E. Research mode, web search and web fetch** | Research needs Pro or above. Web search is on every plan. | Web, desktop, phone | Classic: **+ → Research**. New experience: `/deep-research`, or **+ → Research**. | **No.** Public pages only. Can also read the coach's connected Gmail, Drive and Calendar. | Same limits, used up faster | Follows robots.txt and won't bypass CAPTCHAs. |
| Dispatch (control Cowork from your phone) | Not available to new users (Sep 2026) | — | — | — | — | — |

There is **no standalone Claude web browser product**, unlike OpenAI's Atlas. The browser options are the Chrome extension, the built-in browser inside Claude Desktop, and computer use.

## What each place looks like for social listening

| Place | Claude in Chrome / built-in browser (A–C) | Research / Search (E): robots.txt checked 5 Oct 2026 |
|---|---|---|
| Facebook groups the coach belongs to | Not in any documented block list. Claude reads by screenshot and can scroll and click "See more". **Not live-tested.** Facebook's checkpoint for a new browser login in option C is **UNVERIFIED**. | ✗ facebook.com blocks all bots by default and requires a login. |
| Meta Ads Library | Not documented as blocked, **not tested**. Public pages. | ✗ Same robots.txt as above. |
| Instagram, TikTok, Threads comments | Not documented as blocked, **not tested**. TikTok CAPTCHAs: Claude may not bypass them, so the coach solves them by hand. | ✗ Instagram and Threads block ClaudeBot. TikTok blocks Claude-User and Claude-SearchBot. |
| YouTube comments | Not documented as blocked, **not tested** | ✗ robots.txt blocks `/comment` for all bots, and comments load with scripts. |
| LinkedIn | Not documented as blocked. **Account-restriction risk** from bot-like patterns (GitHub #80986, 24 Jul 2026, user report; account outcome unknown). | ✗ Claude-User is blocked. |
| X | Not documented as blocked, **not tested** | ✗ All bots blocked. |
| Reddit | **✗ Blocked since 18 Sep 2026** (user reports, not in official docs) | ✗ Use ChatGPT or Reddit Answers instead, as the spec already says. |
| Trustpilot and other review sites | Not documented as blocked | ✓ Claude-User allowed apart from a few paths. |
| Shopee VN reviews | Not documented as blocked, **not tested**. Likely CAPTCHAs or login walls (**UNVERIFIED**). | Product pages aren't disallowed, but reviews load with scripts. **UNVERIFIED** whether fetch can read them. |
| Zalo groups | Zalo isn't a website here. Computer use (D) *could* open Zalo PC if the coach approves the app. **Not recommended:** these are other people's private messages, and Vietnam's data-protection law applies. | ✗ |

## Terms and privacy cautions to show the coach

- **Platform terms:**
  - Meta (effective 1 Jan 2025): no automated collection without permission, "regardless of whether… logged-in".
  - LinkedIn User Agreement: bans "crawlers, browser plugins and add-ons" used to scrape.
  - YouTube: no automated access except search engines.
  - Anthropic says the user is responsible for "third-party website terms of service, including any restrictions on automated access". Its agent usage policy bans surveillance and profiling.
  - So: low volume, human pace, Manual approve.
- **Training and retention:**
  - Chrome extension data counts as conversation data. It is used for training **if "Help improve Claude" is on**; the pricing page lists training as opt-out on Free, Pro and Max.
  - If training is on, data is kept up to 5 years de-identified. Deleted chats are purged within 30 days.
  - Screenshots capture whatever is visible, including other members' names and posts.
  - Side-panel sessions are saved and synced, and cloud sessions are processed on Anthropic's servers.
  - Advise the coach: Settings → Privacy → turn training off; turn Memory off for the task (**+ menu**); use a separate Chrome profile; paraphrase rather than store screenshots.
- **Vietnam:**
  - Claude.ai, including Claude in Chrome and Cowork, is listed as available in Vietnam.
  - Billing is by credit card only; the price is in USD and the pricing page says tax isn't included.
  - Claude replies in Vietnamese, but the extension's interface is English.
  - Many VN coaches use Windows with Chrome. There the built-in browser **can't import Chrome logins** (Firefox only), so option A is the simplest route.
  - Vietnam's Personal Data Protection Law 91/2025/QH15 has been in force since 1 Jan 2026.

## Notes for the spec

- The spec line "some domains blocked by a classifier" is only partly right. Officially, adult and piracy sites are blocked and financial sites need permission. Reddit is blocked by user report only. No social site other than Reddit is reported as blocked.
- Before shipping, run one short manual test on Facebook, TikTok, Instagram, YouTube, the Ads Library and Shopee.
- Tell coaches to pick **Manually approve**. It isn't the default in the Chrome side panel.
- Option C is a credible Browse route for coaches who don't use Chrome. Option D is not worth it for social listening.
- Neither Chrome nor the desktop app works on phones, so phone-only coaches stay on Paste.

## ChatGPT cross-check (outside this brief, partial)

help.openai.com refused my requests (HTTP 403), so I couldn't read the official pages directly.
- **Agent mode removed:** I couldn't confirm this on the official help pages. On the OpenAI forum, users reported Agent Mode removed (thread opened 8 Aug 2026). On 7 Sep 2026 an OpenAI_Support reply pointed people to Work's cloud browser (learn.chatgpt.com/docs/browser). That's semi-official support.
- **ChatGPT Work:** search results quoting OpenAI's release notes show Work in the desktop app by 16 and 23 Jul 2026. The exact launch date is **UNVERIFIED**.

## Sources (all accessed 5 Oct 2026)

- [Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)
- [Use Claude in Chrome safely](https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely)
- [Claude in Chrome permissions guide](https://support.claude.com/en/articles/12902446)
- [Claude in Chrome is generally available (26 Aug 2026)](https://claude.com/blog/claude-in-chrome-generally-available)
- [Claude in Chrome product page](https://claude.com/claude-in-chrome)
- [Chrome Web Store listing](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn)
- [Claude gets its own browser in Cowork (26 Aug 2026)](https://claude.com/blog/cowork-built-in-browser)
- [Use the built-in browser in Cowork](https://support.claude.com/en/articles/16607400)
- [Cowork is now Claude (16 Sep 2026)](https://claude.com/blog/cowork-is-now-claude)
- [Claude Cowork and chat are one Claude](https://support.claude.com/en/articles/16761823)
- [Cowork on web, desktop and mobile (6 Oct change)](https://support.claude.com/en/articles/15520349)
- [Get started with Cowork](https://support.claude.com/en/articles/13345190)
- [Use Cowork safely](https://support.claude.com/en/articles/13364135)
- [Let Claude use your computer](https://support.claude.com/en/articles/14128542-computer-use-safety)
- [Claude release notes](https://support.claude.com/en/articles/12138966-release-notes)
- [Use Research](https://support.claude.com/en/articles/11088861)
- [Web search](https://support.claude.com/en/articles/10684626)
- [Anthropic crawlers and robots.txt](https://support.claude.com/en/articles/8896518)
- [Agents and the Usage Policy](https://support.claude.com/en/articles/12005017)
- [Install Claude Desktop](https://support.claude.com/en/articles/10065433)
- [Usage limits](https://support.claude.com/en/articles/9797557)
- [Pricing](https://claude.com/pricing)
- [Supported countries](https://www.anthropic.com/supported-countries)
- [Data retention](https://privacy.claude.com/en/articles/10023548)
- [Model training](https://privacy.claude.com/en/articles/10023580)
- [GitHub #95326: Reddit blocked](https://github.com/anthropics/claude-code/issues/95326)
- [dev.to: Reddit block report](https://dev.to/developerbishwas/this-site-is-not-allowed-due-to-safety-restrictions-so-i-stopped-asking-claude-to-open-sites-for-bej)
- [GitHub #80986: LinkedIn account risk](https://github.com/anthropics/claude-code/issues/80986)
- [Meta Terms](https://www.facebook.com/legal/terms)
- [LinkedIn User Agreement](https://www.linkedin.com/legal/user-agreement)
- [YouTube Terms](https://www.youtube.com/static?template=terms)
- [Vietnam data-protection law (Tilleke)](https://tilleke.com/insights/vietnams-new-personal-data-protection-law-a-closer-look)
- [OpenAI forum: Agent Mode removed](https://community.openai.com/t/agent-mode-was-removed-with-no-real-replacement/1389601)
- robots.txt files for facebook.com, instagram.com, tiktok.com, youtube.com, linkedin.com, x.com, threads.net, trustpilot.com and shopee.vn, fetched directly.