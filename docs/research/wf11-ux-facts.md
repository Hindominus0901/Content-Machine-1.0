The simplest setup that still gives great results is a **"Project kit" that is identical on both apps**: on a computer, create one Project, paste one instruction block, and add at most 2 method files. That takes about 3 minutes. After that the coach just talks: the AI interviews them, writes their Brand Card, and the coach saves it into the Project with the app's own button. The Notion hub, the skill zip, the connector and the automations should all move out of Day 0 and be added later, with the machine guiding the coach. The fallback is a "paste one starter prompt" chat backed by the app's memory. It works on a phone in 30 seconds, but it is the weaker option.

For the VN edition, default to **ChatGPT**. Claude's own voice input does not support Vietnamese.

Labels: [DATA] means an official help page or release note. [PRAC] means a third-party or community source. [UNVERIFIED] means it needs a hands-on test. All facts were checked on or before 5 Oct 2026. help.openai.com blocked direct reads, so the OpenAI facts come from search snippets and mirrors.

## 1. Key facts, dated

**ChatGPT**
- **Projects on every plan, including Free.**
  - Files per project: Free 5, Go/Plus 25, Pro 40 [DATA via snippets, May 2026].
  - Free also allows only about 3 file uploads a day [PRAC].
  - Project instructions hold about 8,000 characters [PRAC].
  - Free has unlimited text chat on GPT-5.6 Luna since 7 Aug 2026, but only about 27K of instant context [PRAC]. Large files will only be partly read.
- **Two features that remove the download/upload loop** (from 25 Feb 2026, [DATA-ish via release-note mirrors]):
  - **Save a ChatGPT reply into the Project's sources** from the message menu. The menu label varies, something like "Save to project" or "Add to project sources".
  - **Paste text directly as a source** (Sources → Add → Text).
  - Whether this works on Free, on mobile, and whether it counts toward the 5-file cap is [UNVERIFIED].
- **Project memory.** A project can use Default memory (reads saved memories) or Project-only memory. Since Aug 2026 an unshared project can switch between the two without being recreated [PRAC].
- **Mobile.** The help docs say projects can be created and edited only on the web and the Windows app; phones and Mac can only view and chat in them [DATA quote, older]. I found no proof that phone creation exists now [UNVERIFIED]. Using a project from the phone works, including uploads and voice. Voice mode inside Projects and with uploaded files arrived 3–7 Aug 2026 [DATA].
- **Sharing a ready-made project with buyers does not work as a delivery method.**
  - Link sharing does exist on Free/Go/Plus/Pro, with "Anyone with a link" as an option.
  - But it is a shared workspace: every member sees every chat, the files and the instructions.
  - Member caps: Free 5, Go/Plus 10, Pro 100.
  - Personal memory is switched off in shared projects, and the project is locked to project-only memory.
  - The link was broken on 10 Sep and 24 Sep 2026 [PRAC].
  - There is no "duplicate project" or template feature as of Sep 2026 [PRAC].
- **Shared chat links.** A recipient can continue a shared chat as their own private copy. Uploaded files probably do not come with it in a usable form, and project instructions are not included [PRAC]. Treat this route as experimental.
- **Memory.**
  - Saved memories plus chat-history reference. A rebuilt memory system (OpenAI calls it "Dreaming") reached Plus/Pro in the US on 4 Jun 2026; Free and Go were promised "over the coming weeks" [DATA via 9to5Mac].
  - Memories are condensed, not stored word for word, and the capacity is not published [PRAC]. Memory can hold a short brand essence, not a 600-word brief.
  - Global custom instructions: 1,500 characters on Free/Go [PRAC].
- **Skills and plugins: not a path for personal plans.**
  - Skills are rolled out to Business, Enterprise, Healthcare and Edu.
  - A Plus user reported personal Skills disappeared from Chat on 18 Sep 2026 (they still worked in "Work").
  - Free and Go users can browse plugins but cannot use them.
  - "ChatGPT Work" requires Plus and is a more technical, desktop-style workspace.
  - Custom GPTs retire on 11 Dec 2026, and personal accounts can no longer create new ones.
- **Scheduled-task share links** work for Free, Go, Plus and Pro. They carry the instructions, the schedule and the creator's time zone, but no files or memory.

**Claude**
- **Projects on Free.** Free accounts get up to 5 projects [DATA]. Paid plans switch to search-based reading (RAG) when knowledge gets large; on Free, everything loads into the conversation. Project sharing is Team/Enterprise only [DATA].
- **Mobile.** Some sources say the app cannot create projects [PRAC, older; UNVERIFIED for Oct 2026].
- **Memory is on by default for Free, Pro and Max** on web, desktop and mobile (Free since 2 Mar 2026) [DATA].
  - Each project has its own separate memory space.
  - Since 10 Jul 2026, memory is a list of separate entries you can view and edit in Settings → Memory.
  - The user can say "remember this" [DATA].
  - Whether global memory also appears inside projects is not documented.
  - Searching past chats is paid only [DATA].
- **Importing memory.** There is a "Memory Import" in Settings → Capabilities (also claude.com/import-memory), labelled experimental. It works on Free/Pro/Max on web and desktop [PRAC].
- **Skills on Free, Pro, Max, Team and Enterprise** [DATA].
  - Install: Customize → Skills → + → Create skill → Upload a skill → choose the .zip.
  - "Code execution and file creation" is **ON by default** for Free/Pro/Max (help page dated 6 Aug 2026). The toggle step can be removed from the guide.
  - Installing a skill from the phone: [UNVERIFIED]. One source says skills are not on mobile; Cowork mobile (paid) can use them.
  - Sharing a skill with people outside an organization is not documented. One third-party claim that Pro/Max users can share skills by email is [UNVERIFIED].
- **Shared chats** (all plans, web only) are **view only**: the recipient cannot continue or copy them [DATA, 4 Sep 2026].
- **Published artifacts.**
  - Free, Pro and Max users can publish an artifact; anyone with the link can open it.
  - Any AI feature in it asks the visitor to sign in to Claude, and that use counts against **the visitor's** own plan limits [DATA].
  - Saving data per visitor requires the creator to be on a paid plan, is capped at 20 MB of text, works on web and desktop only, and is deleted for good if the artifact is unpublished [PRAC].
  - It cannot use the visitor's skills or memory.
  - It is good as a zero-install setup wizard or demo, but not as the machine itself. The link can also leak to non-buyers.
- **Free plan limits.** Roughly 15–40 messages per 5 hours, varying with load, on Sonnet 4.6 [PRAC]. The onboarding interview needs to be split into sittings.

**Voice and mobile**
- **ChatGPT** dictation got a new speech model on 26 Jun 2026 for all plans, with better Vietnamese named explicitly [PRAC mirror of the release note]. Voice mode lists Vietnamese.
- **Claude** mobile dictation supports 12 languages, and **Vietnamese is not one of them** (help page dated 23 Jul 2026, [DATA]). Voice mode does not list Vietnamese either. Vietnamese Claude users must use the phone keyboard microphone instead (Gboard or iOS dictation, both support Vietnamese).
- Uploading files and photos from a phone works in both apps.
- Claude is officially available in Vietnam, but Pro needs an international card; MoMo and ZaloPay are not accepted [PRAC].

## 2. Minimal paths by app and plan

Times are my own estimates for a non-technical user and do not include the interview.

| # | App / plan | Exact steps | Install time | Where the brand profile lives | Result quality |
|---|---|---|---|---|---|
| C0 | ChatGPT, any plan, phone OK | Copy the "Start" prompt from the setup page → paste it into a new chat → answer by voice → at the end say "Remember my Brand Card: [3 lines]" | about 30 s | Saved memory (condensed, may be dropped). The method does not persist, so the prompt is re-pasted each session | Medium |
| **C1** | **ChatGPT Free and up, set up on web or Windows** | Sidebar → Projects → New project → name it "Content Machine" → keep Default memory → Create → Instructions → paste the block → Save → Add files: 1–2 method files, or paste them as text sources → New chat in the project → "Bắt đầu" → interview → on the Brand Card reply: ••• → Save to project | **2–3 min** | A project source (exact text) plus project memory | **High** |
| C2 | ChatGPT shared project link | — | — | — | **Do not use** (everyone sees everyone's chats, member caps, memory off, link bugs) |
| K0 | Claude, any plan, phone OK | Paste the starter prompt → interview → "Remember this: [Brand Card]" | about 30 s | Memory entries (can be viewed and edited) | Medium |
| K1 | Claude Free and up, web or desktop | Download the zip **in Chrome** → Customize → Skills → + → Create skill → Upload a skill → turn it on → new chat: "Start Content Machine" (or type "/") | 1–2 min | Memory entries | Medium-high (skill triggering depends on the description) |
| **K2** | **Claude Free and up, web or desktop** | Projects → + New Project → name it → Set project instructions → paste the block → Save → + → add 1–2 method files (or K1's skill instead) → chat inside the project → at the end save the Brand Card via the artifact's ••• → Add to project [UNVERIFIED on Free/Pro], or via + → paste as text [UI label UNVERIFIED] | **about 3 min** | Project knowledge plus project memory | **High** |
| K3 | Claude published-artifact wizard | Click link → sign in → do the interview → copy the result | 0 | The visitor copies it out (saved data only on web/desktop) | Good front door, weak engine |
| K4 | Claude Pro + Notion + scheduled tasks | The existing architecture | 13–15 min | Notion | Highest, but a "later" upgrade |

## 3. Ranked recommendation

1. **The Project kit (C1 or K2): same steps and same texts in both apps.** It is one paste block plus at most 2 small method files, which fits Free's 5 files and roughly 3 uploads a day. The Brand Card is saved **with the app's own button**, so the coach never downloads or re-uploads anything. Setup happens once on a computer; after that everything runs from the phone by voice. This is the best balance of few steps and lasting, high-quality results. VN edition: default to ChatGPT (Vietnamese voice, Free unlimited text, no international card needed).
2. **Fallback, for no computer or when the coach gets stuck:** the C0/K0 one-paste starter plus memory. The coach gets a first script inside the first session. At the end the machine tells them: "When you're at a computer, take 3 minutes to make it permanent," and then walks them through C1 or K2.
3. **Optional power-ups, added later and guided by the machine:**
   - The Claude skill (K1, now with no toggle step).
   - Notion and scheduled tasks (K4) for Claude Pro.
   - A published artifact as a zero-install setup or interview front door, Claude edition only.

What this means for the architecture:
- Drop the skill, Notion and connector steps from Day 0.
- Make the instructions self-checking: if no Brand Card is found in the sources, run a 5-question quick intake.
- Start every reply with a short "running" tag, so a chat opened outside the project is noticed immediately.
- Keep the method files lean, because of the 27K context on ChatGPT Free and the usage caps on Claude Free.
- Split the interview into roughly 20-minute sittings.

## 4. Most common beginner setup failures and how to guard against them

1. **Chatting outside the Project**, so the instructions don't apply. Guard: the "running" tag at the top of each reply, and a big "always open the project first" line in the guide.
2. **Trying to create the Project on a phone.** Creation is web/Windows only for ChatGPT, and unverified for Claude. Guard: the guide says "do this once on a computer."
3. **Safari on Mac auto-unzips the download**, leaving a folder instead of a zip, and the skill upload fails. Guard: tell users to download in Chrome, or ship pasteable text instead of files.
4. **Too many files.** ChatGPT Free allows 5 files per project and about 3 uploads a day. Guard: at most 2 files, or paste them as text sources.
5. **Memory switched off**, or using Temporary/Incognito chat. Guard: keep the brand profile in Project sources, not only in memory.
6. **Vietnamese voice in Claude comes out wrong**, because Claude's dictation doesn't support Vietnamese. Guard: tell users to use the keyboard microphone.
7. **Claude Free usage cap hit in the middle of the interview.** Guard: run the interview in sittings, with a "continue tomorrow" save point.
8. **Long chats drift away from the instructions** [PRAC]. Guard: one chat per job, which the "What's next?" flow already does.

## 5. Test by hand before launch
- ChatGPT "Save to project" and "paste text as source": do they work on Free, on mobile, and do they count toward the 5-file cap?
- Can ChatGPT and Claude projects now be created on a phone?
- Claude: does the artifact "Add to project" option exist on Free/Pro, and what is the exact label for pasting text into project knowledge?
- Claude: can a skill be uploaded or used on mobile, and can Pro/Max users share a skill outside an org?
- Do global Claude memories show up inside projects?
- How well does the model in a published Claude artifact handle the interview?

## Sources
- OpenAI Projects help: https://help.openai.com/en/articles/10169521-projects-in-chatgpt (snippets only)
- OpenAI shared links and tasks FAQ: https://help.openai.com/en/articles/7925741-chatgpt-shared-links-faq (snippets only)
- Shared-project link bug, 24 Sep 2026: https://community.openai.com/t/shared-project-link-redirects-recipient-to-chatgpt-home-page-instead-of-opening-the-project/1400306
- Shared-project collaborator limits, chat visibility and memory: https://kowalah.com/insights/how-to-use-chatgpt-shared-projects-from-shadow-ai-to-shared-intelligence , https://www.ai-toolbox.co/chatgpt-management-and-productivity/how-to-use-chatgpt-projects-guide-2026
- Project memory modes: https://www.memorylake.ai/en/blogs/chatgpt-project-memory-modes , https://learn.chatgpt.com/docs/whats-new
- Projects "sources from anywhere", Feb 2026: https://devicebase.net/en/openai-chatgpt/updates/add-sources-to-your-projects-from-anywhere/8uh , https://www.generalpurpose.com/the-distillation/chatgpt-projects-knowledge-base
- No duplicate-project feature: https://community.openai.com/t/feature-request-selectively-move-or-copy-projects-between-completely-separate-chatgpt-accounts/1398050
- Mobile project creation thread: https://community.openai.com/t/adding-projects-in-ios-on-iphone-andipad/1077111
- Memory update, 4 Jun 2026: https://9to5mac.com/2026/06/04/openai-says-chatgpts-memory-feature-is-getting-smarter-and-coming-to-free-users/
- Memory limits: https://dessence.ai/blog/chatgpt-memory-limit-workaround
- Skills on Plus/Pro: https://community.openai.com/t/bring-native-chatgpt-skills-to-plus-and-pro/1401449 , https://theaicareerlab.com/blog/chatgpt-skills-what-they-are-how-to-enable-2026
- ChatGPT update log: https://releasebot.io/updates/openai/chatgpt
- Free plan, GPT-5.6 Luna and context: https://businesstoday.in/technology/news/story/openai-rolls-out-gpt-5-6-luna-as-default-chatgpt-model-removes-text-chat-limits-for-free-tier-users-547871-2026-08-07 , https://www.datastudios.org/post/chatgpt-free-plan-limits-and-access-what-you-can-do-without-paying
- Upload caps: https://blog.laozhang.ai/en/posts/chatgpt-file-upload-limits-free-plus-pro
- Dictation update, 26 Jun 2026: https://releases.sh/release/rel_yW0Fo9ZQmkMJxmMAxOPoi-chatgpt-improves-dictation-with-new-speech-to-text-model
- Claude memory: https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context , https://www.memorylake.ai/en/blogs/claude-new-memory-entries
- Claude memory import: https://www.macrumors.com/2026/03/02/anthropic-memory-import-tool/
- Claude Projects: https://support.claude.com/en/articles/9517075-what-are-projects , https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
- Claude skills: https://support.claude.com/en/articles/12512180-use-skills-in-claude , https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
- Code execution default: https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude
- Claude shared chats: https://support.claude.com/en/articles/16762496-share-a-chat-with-specific-people
- Claude artifacts: https://support.claude.com/en/articles/9547008-share-artifacts , https://caipi.ai/blog/can-claude-artifacts-save-data , https://www.ai-toolbox.co/claude-management-and-productivity/how-to-use-claude-artifacts-guide-2026
- Claude dictation and voice mode: https://support.claude.com/en/articles/10065434-use-dictation-on-claude-mobile , https://support.claude.com/en/articles/11101966-use-voice-mode
- Claude Free limits: https://ai.zenken.co.jp/en/post/claude-usage/
- Claude in Vietnam: https://gptprompts.ai/vi/gia-claude
- Safari auto-unzip: https://kb.yoast.com/kb/safari-automatically-unzips-archive/