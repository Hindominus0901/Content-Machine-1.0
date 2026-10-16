# Brief: Loading a markdown "drop-in pack" into AI chat products (status on 5 Oct 2026)

Labels: **[DATA]** means vendor documentation or a published study. **[PRAC]** means a third-party guide, a community report or a practitioner's opinion. Where the vendors' own pages disagree, the conflict is flagged.

---

## 1) Key insights

1. **All three big chat products now use the same file format: an Agent Skills folder with a `SKILL.md` file.** Claude (Skills and Plugins), ChatGPT (Skills and Plugins, which replace Custom GPTs) and Gemini (Skills, which replace Gems) all accept a folder that holds a `SKILL.md` with YAML `name` + `description` and optional reference files. [DATA: agentskills.io spec; claude.com/docs; learn.chatgpt.com; Gemini Apps Help]

2. **Do not build Content Machine as a Custom GPT.** OpenAI's help center says Custom GPTs retire on **Dec 11, 2026** (Feb 11, 2027 for Enterprise workspaces with an approved deferral). It also says: *"New GPT creation and publishing are not available on personal ChatGPT accounts, including Free, Go, Plus, and Pro."* [DATA, via search snippet; help.openai.com blocks direct fetch]
   - The migration turns GPT instructions into a skill and knowledge files into reference material inside a plugin. Custom actions do not carry over. [DATA: learn.chatgpt.com migrate guide]
   - Migrated plugins "start private". Support told a creator that link access for people outside the workspace "does not exist today". So the old model of selling a GPT by sharing its link is broken. [PRAC: OpenAI community, Sep 23, 2026]

3. **Gems are going away too.** Personal Google accounts move in **Nov 2026**, and their Gems are converted to skills automatically. Workspace business accounts move in Mar 2027 and education accounts in Jun 2027. [DATA]

4. **Skills hold the methods; Projects hold the person's own facts.** Anthropic describes Skills as "task-specific procedures that Claude loads when a request matches". It describes Projects as "background knowledge that's always loaded in that project's chats". [DATA] So a skill cannot remember a coach's offer, audience and voice. The pack needs both parts: skills for **how** (research, ideas, scripts, series), and a per-user **Brand Brain** file stored in a Project.

5. **Long knowledge files get ignored because of how they are read.**
   - Retrieval-based knowledge only reads matching chunks of a file, not the whole file. ChatGPT GPT knowledge is "pulled in depending on relevance". Paid Claude Projects switch to RAG when knowledge nears the context limit, using a "project knowledge search tool". [DATA]
   - Even models that read the full context get less reliable as the input grows. Chroma's "Context Rot" study (Jul 14, 2025) tested 18 models, and "Lost in the Middle" (Liu et al., 2023) found the same pattern. [DATA]
   - The fixes: route the model to the right file, keep files small and focused, and put the non-negotiable rules in the always-loaded instruction layer.

6. **Availability changes month to month and the vendor docs contradict each other.** Design for the lowest common denominator, which is "Project + pasted instructions". Treat Skills and Plugins as the premium install path.

### Platform facts (verified Oct 2026)

| Surface | Who can use it | Format and limits | How to install or share |
|---|---|---|---|
| **Claude Skills** | Help center: Free, Pro, Max, Team, Enterprise. Free was added in a Feb 11, 2026 announcement. **Conflict:** claude.com/docs still says Pro and up. **"Code execution and file creation" must be on** (Settings > Capabilities). [DATA] | **One skill per zip.** The zip must contain the folder as its top level: `my-skill.zip/my-skill/SKILL.md`. A SKILL.md at the zip root "isn't recognized as a skill". `name`: up to 64 characters, lowercase, digits and hyphens, must match the folder, and must not contain "claude" or "anthropic". `description`: **200 characters on claude.ai** (help center, Jul 22, 2026) vs 1,024 in the docs and spec, so **use ≤200**. Optional fields: `license`, `compatibility` (≤500), `metadata`. No official zip size is published; third parties say 50 MB [PRAC]. SKILL.md should stay under 500 lines (about 5k tokens). [DATA] | Customize > Skills > + > Create skill > Upload a skill, then toggle it on. It triggers automatically from the description, or the user types `/`. Team and Enterprise can share skills (view-only, updates flow to recipients) or Owners can provision them org-wide. [DATA] |
| **Claude Plugins** (many skills in one file) | **Paid plans only** (Pro, Max, Team, Enterprise). [DATA] | Needs `.claude-plugin/plugin.json` plus `skills/<name>/SKILL.md`. Up to 5,000 files and 200 MB. Chat loads skills, and loads commands as skills. Chat ignores agents and hooks. A top-level `bin/` folder blocks the install entirely. [DATA] | Customize > Plugins > Add > **Upload plugin** (.zip or .plugin). Or **Add marketplace** with a GitHub `owner/repo`, which can sync automatically so updates arrive by themselves. Installs also reach Cowork and Claude Code. People on personal plans get it by being sent the zip. [DATA] |
| **Claude Projects** | Free users get up to 5 projects. RAG (about 10x capacity) is paid-only. Sharing is Team and Enterprise only. [DATA] | Knowledge: 30 MB per file, unlimited count, but the total must fit the context window. Chat attachments: 500 MB per file, 20 files per chat. No instruction-length limit is published (third-party claims range from about 8k characters to "200 KB") [PRAC]. | Paste the instructions and upload the knowledge files. |
| **ChatGPT Custom GPTs** | No new creation on personal accounts. Retiring Dec 11, 2026. [DATA] | Instructions: 8,000 characters. Knowledge: 20 files per GPT lifetime, 512 MB per file, 2M tokens per text file. Conversation starters are supported. [DATA via snippets] | Not recommended. |
| **ChatGPT Projects** | Available to Free users since Sep 3, 2025. [DATA] | Files per project: Free 5, Go and Plus 25, Pro, Business, Enterprise and Edu 40. Uploads go in batches of 10. 512 MB per file. [DATA] Project instructions about 8,000 characters [PRAC]. Global custom instructions: 1,500 characters on Free and Go, 5,000 on paid plans (Jul 15, 2026) [PRAC]. Free users get about 3 file uploads per day [PRAC]. | Paste the instructions and upload the files. |
| **ChatGPT Skills and Plugins** | The help center says Skills are "generally available" for Business, Enterprise, Healthcare and Edu. The learn.chatgpt.com pricing page lists Skills and Plugins on Plus and Pro too. A Plus user reported personal Skills vanished from Chat on **Sep 18, 2026** but still worked in Work. For Plugins, Free and Go users can browse the directory, but "plugin extensions are not available" to them. [DATA + PRAC] | Upload with Skills > Create > Upload from your computer, as a folder or a zip. ChatGPT scans the upload and may mark it **"Needs Review"**. A built-in `skill-creator` is included. API bundle rules: a single top-level folder, exactly one SKILL.md, ≤50 MB zip, ≤500 files. [DATA] | Plugins can be made by mentioning **@Plugin Creator** in a chat. Sharing is workspace-only. **For Plus users, "maybe"; Projects work for everyone.** |
| **Gemini** | Gems: up to 10 knowledge files [PRAC/Google]. **Skills are free** for personal accounts aged 18+ with Keep Activity on, on web, mobile and Mac. [DATA] | Upload a SKILL.md, a folder, or a zip "that contains a SKILL.md file in its main folder". Total ≤100 MB. .md, .txt and .pdf work; **.docx and .xlsx are not supported**. Hidden files such as `.DS_Store` can make the upload fail. [DATA] | The zip-root rule is the **opposite of Claude's** (or at least ambiguous). Tell Gemini users to upload the **unzipped folder**. |

---

## 2) Frameworks & templates

### F1. Three-layer progressive disclosure [DATA: Agent Skills spec; Anthropic best practices]

**How it works:**
- **Layer 1:** `name` + `description` (about 100 tokens) are always loaded.
- **Layer 2:** the SKILL.md body (<500 lines, <5k tokens) loads when the skill is triggered.
- **Layer 3:** files in `references/` and `assets/` load only when a step names them.

**Rules:**
- Keep references **one level deep**. Claude may only preview (`head -100`) files that are linked from other linked files.
- Put a table of contents at the top of any file longer than 100 lines.
- Write descriptions in **third person**, saying both what the skill does and when to use it.
- Use the same terms everywhere.

**Template (worked for a career coach):**
```markdown
---
name: cm-scripts
description: Writes short-form video and post scripts (educational, relatable, converting) in the user's voice. Use when the user asks for a script, hook, caption, reel, TikTok, or ad.
---
# Content Machine: Scripts
Before writing: find MY-BRAND-BRAIN in this chat/project. If missing, ask the 5 questions in references/quick-intake.md, then continue.

Copy this checklist and tick it off:
- [ ] 1. Content type? Educational / Relatable / Converting
- [ ] 2. Pick a format: Educational → references/edu-formats.md | Relatable → references/relatable-formats.md | Converting → references/converting-formats.md
- [ ] 3. Write 3 hooks with references/hooks.md; choose the strongest and say why
- [ ] 4. Fill assets/script-template.md
- [ ] 5. Run references/qa-checklist.md; fix every fail; re-run
- [ ] 6. Close with the series link: which piece comes next and why
```
The description above is about 170 characters, under the 200-character claude.ai limit.

### F2. Methods-vs-memory split [DATA: Anthropic skills vs projects comparison; design inference]

**How it works:** skills are stateless and shared by every user. Facts about one user live in a single persistent file in that user's Project.

**Template (`MY-BRAND-BRAIN.md`):**
```
WHO I HELP: [role, stage, situation]
THEIR #1 PROBLEM (their words): "[...]"
WHAT THEY'VE TRIED THAT FAILED: [...]
MY RESULT/PROMISE: [from X to Y in Z]
MY OFFER: [name, price, format, CTA link/keyword]
MY PROOF: [3 client wins with numbers]
MY BELIEFS/CONTRARIAN TAKES: [3]
MY VOICE: [5 words I use / 5 I never use] + 2 sample posts I wrote
```
**Example:** Maya is a career coach for first-time managers. Her offer is the "New Manager Bootcamp", 8 weeks for $1,500, and her CTA is "DM 'LEAD'". Every skill reads this file first, so a script for Maya automatically uses her audience's words, for instance "I got promoted and now my friends report to me".

### F3. Router (file-map) instructions [DATA: Anthropic "domain-specific organization" pattern; PRAC: GPT builders naming files explicitly]

**How it works:** the always-loaded instructions do not try to hold the knowledge. They say *which file to open for which request* and *what output shape to return*. This beats retrieval misses because the model searches or opens a named file instead of guessing.

**Template (keep it ≤7,500 characters so it fits ChatGPT's 8,000-character limit):**
```
ROLE: You are Content Machine, strategist + copywriter for the person in MY-BRAND-BRAIN.md.
ALWAYS FIRST: read MY-BRAND-BRAIN.md. If a field is blank, ask (max 3 questions at once).
ROUTER: open the named file BEFORE answering:
| User wants                         | Open                                 | Return                          |
| audience pains, words, objections  | 02-research-and-ideas.md → RESEARCH  | Pain-map table                  |
| ideas, topics, what to post        | 02-research-and-ideas.md → IDEAS     | 10 ideas tagged EDU/REL/CONV    |
| a script, hook, caption, ad        | 03-scripts.md                        | Filled script template + QA     |
| a series, launch, weekly plan      | 04-series-and-system.md              | Domino series plan              |
NON-NEGOTIABLES: [3–5 rules]
(Repeat NON-NEGOTIABLES as the last lines of this box.)
```

### F4. Instruction sandwich [DATA: vendor testing]

**How it works:**
- OpenAI's GPT-4.1 guide says that with long context, putting instructions **at both the beginning and the end** performed better than putting them only above or only below.
- Anthropic says to put long documents at the top and the query at the end, which "can improve response quality by up to 30%".

**Template:** each knowledge file starts with a 5-line "WHEN TO USE THIS FILE / RULES" header and ends with a 3-line "BEFORE YOU ANSWER, CHECK" footer.

### F5. Checklist plus feedback loop [DATA: Anthropic skill best practices]

**How it works:** the model copies a checklist and ticks it off. A reference file acts as the "validator": draft, check against the list, fix, re-check.

**Template (`qa-checklist.md`, excerpt):**
```
FAIL if any:
□ Hook > 12 words or doesn't name the viewer or their problem
□ Any sentence the audience wouldn't say out loud
□ No specific number, name, or moment
□ CTA doesn't match the content type (EDU = save/follow; CONV = DM/keyword)
□ No "next piece" link
```

### F6. Evaluation-first [DATA: Anthropic]

**How it works:**
1. Run 3 realistic prompts *without* the pack and write down what goes wrong.
2. Write just enough instructions to fix those failures.
3. Re-run and compare.

Test on every model the pack targets. Claude's `skill-creator` does this in chat.

**Example evals for Maya:**
- "Give me 10 ideas for this week."
- "Script a POV reel about my first 1:1 as a new manager."
- "Write a 45-second ad for the Bootcamp."

### F7. Free-tier one-paste starter [PRAC/design]

```
I've attached CONTENT-MACHINE-ALL-IN-ONE.md. Read ALL of it before replying.
Act as the Content Machine it describes.
Step 1: Run the Brand Brain interview, one question at a time.
Step 2: Output my finished MY-BRAND-BRAIN.md in one code block so I can save it.
Step 3: Ask what I want first: Research, Ideas, Scripts, or a Series.
For this whole chat: [3 non-negotiables]. Batch outputs (e.g., 5 scripts per reply).
```

---

## 3) What this means for the Content Machine design

1. **Write the pack once, as skill folders that follow the Agent Skills spec, and generate every other format from them.** Concatenate them into Project files and an all-in-one file. This avoids keeping four versions in sync by hand.

2. **Ship one download with four install paths, chosen by the user's plan:**
```
content-machine-1.0/
├── START-HERE.md                 ← 1 page: "Which plan are you on?" → Path A/B/C/D
├── A-claude-paid/content-machine-plugin.zip    (Pro/Max/Team/Ent: Customize > Plugins > Upload)
├── B-claude-free-or-gemini/      (one zip per skill; Gemini: upload the unzipped folder)
│   ├── cm-brand-brain.zip  ├── cm-research.zip  ├── cm-ideas.zip
│   ├── cm-scripts.zip      └── cm-series.zip
├── C-any-project/                (Claude Projects, ChatGPT Projects incl. Free: ≤5 files)
│   ├── 00-PASTE-INTO-INSTRUCTIONS.txt   (≤7,500 chars; F3 router)
│   ├── 01-research-and-ideas.md  ├── 02-scripts.md  └── 03-series-and-system.md
│   (leaves slots for the user's MY-BRAND-BRAIN.md + CONTENT-LOG.md)
└── D-one-file/CONTENT-MACHINE-ALL-IN-ONE.md  (+ F7 starter prompt at the top)
```
   - Path C is three uploaded files plus pasted instructions. That fits ChatGPT Free's limits of 5 files per project and about 3 uploads per day.
   - Inside the plugin, use `skills/cm-*/SKILL.md`, a `plugin.json`, and **no `bin/` folder**.

3. **Use five instruction-only skills (no scripts):**
   - `cm-brand-brain`: onboarding interview that outputs MY-BRAND-BRAIN.md.
   - `cm-research`: audience research.
   - `cm-ideas`: ideation.
   - `cm-scripts`: scripting.
   - `cm-series`: domino series plus cadence.

   Instruction-only skills avoid depending on code execution and work the same on ChatGPT and Gemini. Keep descriptions ≤200 characters, in third person, with trigger words first, because Codex shortens descriptions when many skills are installed. Never put "claude" in a skill name.

4. **Brand Brain is the one file the user must save into their Project.** Every skill checks for it and runs a 5-question mini-intake if it is missing. The best Claude setup is **Plugin (methods) + Project (Brand Brain + content log)**.

5. **For ChatGPT in Oct 2026, use Projects (Path C) as the main route.** Offer the skills zip only as "if you see Skills in your account". Do not build or sell a GPT.

6. **Use Markdown only, never PDF or DOCX.** Gemini skills reject .docx and Projects only extract text anyway. Use small focused files with a TOC for anything over 100 lines, a header and footer on each file (F4), and the same terms everywhere (always "Educational / Relatable / Converting").

7. **Keep time-sensitive material out of skill bodies.** Platform and algorithm notes go in one dated `references/platform-notes.md`, following Anthropic's "avoid time-sensitive information" rule.

8. **Plan around free-tier caps.** Claude Free allows roughly 15–40 messages per 5 hours [PRAC]. Instruct the model to batch: 10 ideas or 5 scripts per reply, plus a whole series plan in one go.

9. **Distribute through a GitHub marketplace repo for paid Claude users,** so updates reach them automatically. Put a version number in `plugin.json` and in skill `metadata`.

10. **Build trust and QA into the pack.** Claude tells users to read uploaded skills before turning them on, and ChatGPT may flag uploads as "Needs Review". So each skill folder gets a plain-English README. Each release also runs the three F6 evals on Claude Free/Pro, ChatGPT Free/Plus and Gemini.

---

## 4) Sources

- Agent Skills specification — https://agentskills.io/specification
- Claude: Create custom skills — https://claude.com/docs/skills/how-to
- Claude: Skills overview — https://claude.com/docs/skills/overview
- Claude Help: Use skills in Claude — https://support.claude.com/en/articles/12512180-use-skills-in-claude
- Claude Help: How to create custom skills (Jul 22, 2026) — https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
- Claude: Plugins overview — https://claude.com/docs/plugins/overview
- Claude: Plugin structure and testing — https://claude.com/docs/plugins/build
- Claude: Plugin feature support across platforms — https://claude.com/docs/plugins/platform-support
- Claude: Share a plugin — https://claude.com/docs/plugins/share
- Claude Help: Use plugins in Claude — https://support.claude.com/en/articles/13837440-use-plugins-in-claude
- Claude Help: What are projects — https://support.claude.com/en/articles/9517075-what-are-projects
- Claude Help: RAG for projects — https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects
- Claude Help: Uploading files (Jul 23, 2026) — https://support.claude.com/en/articles/8241126-uploading-files-to-claude
- Anthropic: Skill authoring best practices — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Anthropic: Long context tips — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/long-context-tips
- Claude on X, free plan gets skills (Feb 11, 2026) — https://x.com/claudeai/status/2021630343372259759
- OpenAI Help: Custom GPT retirement and migration FAQ — https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq
- OpenAI Help: Skills in ChatGPT — https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- OpenAI Help: Plugins in ChatGPT — https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex
- OpenAI Help: Projects in ChatGPT — https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- OpenAI Help: Knowledge in GPTs — https://help.openai.com/en/articles/8843948-knowledge-in-gpts
- learn.chatgpt.com: Build skills / Build plugins / Migrate GPTs / Pricing — https://learn.chatgpt.com/docs/build-skills , https://learn.chatgpt.com/docs/build-plugins.md , https://learn.chatgpt.com/docs/migrate-custom-gpts.md , https://learn.chatgpt.com/docs/pricing.md
- OpenAI API Skills guide (bundle limits) — https://developers.openai.com/api/docs/guides/tools-skills
- OpenAI Community: GPT→plugin migration access concerns (Sep 23, 2026) — https://community.openai.com/t/openai-s-custom-gpt-plugin-migration-raises-access-concerns/1399984
- OpenAI Community: Bring Skills to Plus/Pro (Sep 28–30, 2026) — https://community.openai.com/t/bring-native-chatgpt-skills-to-plus-and-pro/1401449
- OpenAI Community: GPT knowledge file limits — https://community.openai.com/t/what-is-the-knowledge-file-limit-that-can-be-uploaded-to-train-custom-gpts/653244
- ChatGPT Projects free for all users (Sep 2025) — https://www.folio3.ai/ai-pulse/openai-extends-chatgpt-projects-free-users
- ChatGPT free upload cap (PRAC) — https://www.fileuploadgpt.com/blog/chatgpt-file-upload-limit-free-plan
- Custom instructions 5,000 characters (PRAC) — https://www.mindstudio.ai/blog/chatgpt-custom-instructions-character-limit
- Project instructions 8,000 characters (PRAC) — https://x.com/csswizardry/status/2086093470867845287
- ChatGPT Skills availability analysis (PRAC, Aug 5, 2026) — https://www.aiagentslibrary.com/blog/chatgpt-skills-availability/
- Gemini: Transition from Gems to skills — https://support.google.com/gemini/answer/18560919?hl=en
- Gemini: Create & manage skills — https://support.google.com/gemini/answer/17094296?hl=en
- Gemini: Use Gems — https://support.google.com/gemini/answer/15146780?hl=en
- Chroma, Context Rot (Jul 14, 2025) — https://research.trychroma.com/context-rot
- Liu et al., Lost in the Middle (2023) — https://arxiv.org/abs/2307.03172
- OpenAI GPT-4.1 Prompting Guide — https://cookbook.openai.com/examples/gpt4-1_prompting_guide
- Claude free-tier message limits (PRAC) — https://ai.zenken.co.jp/en/post/claude-usage/