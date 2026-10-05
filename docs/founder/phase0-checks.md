# Phase-0 checks: test these on real accounts

**Why.** The setup steps in the pack rely on a few app behaviours that no official page confirms. Each check below decides one default in the pack. Please run them once on real accounts (you or a VA) and fill in the results table at the bottom. Then tell me in chat, and I'll update `platform/targets.toml` and set its `verified_on` dates. The release lint fails until every row marked **blocking** has an answer.

**Time.** About 2 hours.

**Accounts you need:**
- ChatGPT Free, plus ChatGPT Plus if you have it
- Claude Free and Claude Pro
- A computer (Windows or Mac) and an Android or iPhone

**Test file.** Use any `.md` file of about 40 KB until the real method file exists. A long article saved as text works.

**When something fails.** Write what you saw, take a screenshot, and move on. Every check has a fallback, so a "no" is a useful answer.

---

## A. ChatGPT

**A1. Save a reply into the project (blocking).**
1. On a computer, open chatgpt.com → Projects → New project → name it "Test" → Create.
2. Start a new chat in the project and type: `Write a 10-line card about my business called BRAND CARD.`
3. Under the reply, open the ⋯ menu. Is there an option such as "Save to project" or "Add to project sources"?
   - Write down the exact label.
   - Click it. Does the card show up under the project's Sources/Files?
4. Repeat steps 2–3 on the phone app.
5. Repeat on a **Free** account.
6. On Free, does the saved reply count as one of the 5 files? Check whether the file count goes up.

**A2. Paste text as a source (blocking).**
- In the project, go to Sources (or Files) → Add. Is there a "Text" option?
- Paste 3 paragraphs and save.
- Check it on Free, and on the phone.

**A3. Create a project on the phone.**
- In the ChatGPT phone app, can you create a new project?
- Can you paste its instructions and add a file?

**A4. Mac app.**
- In the ChatGPT Mac app, can you create a project, edit its instructions and add a file?
- Or can you only view and chat?

**A5. Create tasks from inside a project chat (blocking).**
- In a project chat, type: `Every Monday at 7:07 send me a message that says "Your week". Set it up as a scheduled task.`
  - Does ChatGPT create the task? Check Sidebar → Scheduled (or Tasks).
- Try it on Free and on Plus.

**A6. Weekday scheduling on Free (blocking).**
- On Free, ask for a task "every weekday at 8am", then another for "every Friday".
  - What does it accept?
  - Does it show a time window (morning, afternoon or night) instead of an exact time?

**A7. Longest task text (blocking).**
- Create a task whose instructions are a long text. Start with 3,000 characters, then try 6,000, then 9,000.
- After saving, open the task. Is the whole text still there?
- Write down the longest length that survived intact.

**A8. Free message cap.**
- On Free, send about 40 messages in one hour.
  - Do you hit a limit?
  - Does it switch to another model, and if so, which one?

**A9. Vietnamese dictation length.**
- On the phone, tap the small mic in the message box (not the sound-wave button).
- Speak Vietnamese for 1 minute, then 3 minutes, then 5 minutes.
- Does it cut off? If so, after how long?

## B. Claude

**B1. Paste text into project knowledge (blocking).**
- claude.ai → Projects → New project → in Project knowledge click + . Is there an option to paste text? Write down the exact label.
- Check it on Free and on Pro.

**B2. Save an artifact into the project (blocking).**
- In a project chat, type: `Make a short document called BRAND CARD.`
- Open the artifact's ⋯ menu. Is there "Add to project"? Does it appear in Project knowledge afterwards?
- Check it on Free and on Pro.

**B3. Create a project on the phone.** In the Claude phone app, can you create a project and add instructions and a file?

**B4. Free turns with the kit loaded (blocking).**
- On Free, create a project. Paste a 7,000-character instruction text and add the 40 KB test file.
- Chat normally with short questions and answers.
- How many messages do you get before Claude says you've hit the limit?
- Note the time; the limit resets every 5 hours.

**B5. Instructions length (blocking).**
- Paste a 7,500-character text into Project instructions and save.
- Reopen the instructions. Is all of it still there?

**B6. Skills and Notion on Free.**
- On Free, go to Customize → Skills → + → Upload a skill. Does the upload option exist?
- Connect Notion (Settings → Connectors). Can Claude create a page in Notion when you ask it to?

**B7. Re-uploading a skill.**
- Upload a test skill zip. Then upload a changed zip with the same name.
- Does it replace the first one, or do you now have two?

**B8. Scheduled tasks (Pro).**
- Sidebar → Scheduled → New task. Create one that writes a page in Notion. Click **Run now**.
  - Did it stop to ask for approval?
  - Which approval mode did you pick?

**B9. Mac dictation.** On a Mac, press fn (globe) twice inside the Claude message box and inside ChatGPT's. Does dictation start in both?

## C. Browser agents (for the research module's Browse mode)

**C1. Reading comments (only if you have the tools).**
- **Claude in Chrome (Pro).** Ask it to open one public Facebook group post, one TikTok video and one Instagram post, and copy the first 10 comments word for word. Which ones worked?
- **ChatGPT desktop app + the browser extension (Plus).** Same test.

**Rules for this test:**
- Read only. Never post, react or join a group.
- Don't copy names or handles into your notes.

---

## Results (fill in)

| # | Check | Free | Paid | Exact label / number | Date | Notes |
|---|---|---|---|---|---|---|
| A1 | Save reply to project (computer / phone) | | | | | |
| A1b | Counts toward the 5-file cap? | | — | | | |
| A2 | Paste text as source (computer / phone) | | | | | |
| A3 | Create project on phone | | | | | |
| A4 | Mac app can set up a project | | | | | |
| A5 | Task created from a project chat | | | | | |
| A6 | Free: weekday / weekly-day scheduling, time window | | — | | | |
| A7 | Longest task text kept intact | | | | | |
| A8 | Free message cap / fallback model | | — | | | |
| A9 | VN dictation cut-off | | | | | |
| B1 | Paste text into project knowledge | | | | | |
| B2 | Artifact → Add to project | | | | | |
| B3 | Create project on phone | | | | | |
| B4 | Free turns per 5 h with kit loaded | | — | | | |
| B5 | 7,500-char instructions kept intact | | | | | |
| B6 | Skills upload / Notion write on Free | | — | | | |
| B7 | Skill re-upload replaces | | | | | |
| B8 | Scheduled task Run now: approval stall? | — | | | | |
| B9 | Mac dictation in Claude / ChatGPT | | | | | |
| C1 | Comments readable: FB group / TikTok / IG | | | | | |
