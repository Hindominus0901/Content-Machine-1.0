# No-pack baselines (Day 0)

## What this is

Each folder holds one Day-0 session between an eval persona and a **plain general assistant with no Content Machine pack**: no instruction block, no method file, no kit, no system prompt. It shows what a coach gets today by opening ChatGPT and asking for help. The pack has to beat it. QA spec §5.1 (G3 Judge) sets the bar: the pack must beat the no-pack baseline by at least 2 Edge points with 0 fabrications, using the median of 3 runs. Baselines only ratchet up.

| File | Contents |
|---|---|
| `transcript.jsonl` | One row per turn: `{"turn", "role": "coach" or "machine", "text", "t_min"}` (the format `graders.py` reads) |
| `meta.json` | `persona`, `edition`, `lane: "baseline"`, `build_sha: "none"`, `suite: "day0"` |
| `notes.md` | The simulator's read of the run: outcome, one message, templates, questions, jargon, invented claims, quit triggers, whether the coach comes back |
| `grades.json` | Output of `python3 evals/graders.py evals/baselines/<folder>` |

## How it was produced

- **One simulator.** A single agent played both sides for each persona. It had the persona folder and the rules below. No API keys were used, and no real ChatGPT account was involved.
- **Coach side.** The coach could only use facts from the persona's `answers.md` and `voice-samples.md`. The three dump chunks are pasted verbatim and in order. The only change: vn/proof-coach's typed correction line appears without its "(chị gõ thêm: …)" stage direction. After the dump, the coach follows `## Behaviour` and uses its pushback lines word for word when the trigger happens. The opening line ("I want to start posting content to get clients…") carries no persona fact.
- **Assistant side.** The assistant plays a typical, competent ChatGPT-style assistant. It may not use a persona fact before the coach has said it in the transcript. Its mistakes are the ones such assistants usually make, such as intake forms, content pillars, word-for-word scripts, praise, hashtags, and unsourced statistics. It also gets credit for what it does well, such as keeping Pam, Trang and Khải out and not writing "certified".
- **Timing.** `t_min` is modelled, not measured. It is built from dictation, typing and reading speeds plus the persona's time away (vn/proof-coach's `notes.md` states its rates).
- **Independent check (this pass).** Every `transcript.jsonl` row parses with the required keys, and every `meta.json` parses. The coach side had no leaks: every dump matches `answers.md`, and every later coach line traces to the answer bank, Behaviour or voice samples. The assistant side had 10 small leaks in 7 replies, where it used a persona fact (or the persona's own wording for it) before the coach had said it. They were rewritten from what the coach had already said:
  - en/coldstart-coach r5: "kids under 10" became "little kids". Dan had only said "little kids".
  - en/coldstart-coach r4: "the January all-or-nothing plan" became "plans built for a 25-year-old with no kids". The first is Dan's answer-bank name for the old way, and he was never asked for it.
  - en/coldstart-coach r4: "Instagram Reels first, then the same video to TikTok" (his answer-bank plan) became a recommendation based on his follower counts.
  - en/proof-coach r3, r4: "how to ask someone for 20 minutes" (her answer-bank free gift) became "how to ask someone for coffee". The bio "for women 45+ leaving long corporate careers" became "for women 45+ who want out of corporate", her own words.
  - vn/proof-coach r3: "nói bằng con số" (the answer-bank reason clients choose her) became a line based on "chị dạy tính lãi". In r4, "Từ nay đến 19/11" (her answer-bank launch date) became "Từ nay đến trước 20/11".
  - vn/hanh r2: "lớp kèm" became "việc kèm". After chunk 1 she had only said "kèm", and the group-class format is an answer-bank fact.

  None of these changed a grade. The assistants read as typical, not strawmen, so no assistant turn was rewritten for plausibility.

## Results

"Templates asked" counts fill-in templates plus form-like numbered intake lists. "Invariants failed" and "Other checks failed" come from `grades.json`. `graders.py` exits 1 on every baseline, which is expected.

| Persona | Coach turns | Minutes | Outcome | One message? | Templates asked | Max questions / reply | Invariants failed | Other checks failed |
|---|---|---|---|---|---|---|---|---|
| en/proof-coach | 7 | 32.4 | film-ready | no | 1 (an "I help [who]…" fill-in) | 3 | I1, I5, I8, I17 | deny_list, quit_triggers, day0_timing |
| en/coldstart-coach | 10 | 35.3 | film-ready | no | 1 (a 4-question intake form) | 4 | I1, I5, I8, I11, I17 | deny_list, quit_triggers, day0_timing |
| vn/proof-coach | 5 | 28.7 | quit | no | 1 (a 5-question intake form) | 5 | I1, I5, I8, I11, I14, I15, I17 | deny_list, quit_triggers, day0_timing |
| vn/hanh-android-free-nocomputer | 8 | 62.8 (about 38 active) | film-ready | no | 1 (a 5-question intake form) | 5 | I1, I5, I6, I8, I9, I11, I15 | deny_list, quit_triggers, day0_timing |

I16 is `not_run` everywhere because `locales/<lang>/examples.md` does not exist yet. The Day-0 target is 24 min. No run reached film-ready inside it, and no run produced one clear message.

### Invented or unsupported claims (all runs)

- **en/proof-coach.** The assistant claimed "up to 75% of resumes are filtered out by software before a human ever sees them" in its reply-3 post idea and again in the reply-5 Reel script. It withdrew the claim only after the coach asked "Is that a real number or did you make that up?"
- **en/coldstart-coach.**
  - It offered the brother's "22 pounds in about 4 months" as proof, unprompted, in replies 3 and 4. These are trap numbers: not weighed, no consent.
  - It approved "I trained a couple hundred people" for the opener in reply 9. Dan never counted.
  - It cited "the sitting-rising test" research from model memory in reply 4.
  - It said "most people scroll with the sound off" in reply 10.
- **vn/proof-coach.**
  - It gave "Khung giờ vàng 11h–13h hoặc 20h–22h" as the best posting times.
  - It said "nội dung đi ngược số đông thường kéo tương tác rất tốt".
  - Its hook 6, "lãi thật tăng hơn gấp đôi", is a multiplier the assistant worked out itself, close to the excluded "lãi gấp đôi".
  - It made up a 25/30/20/15/10% pillar split.
- **vn/hanh-android-free-nocomputer.**
  - It turned Thảo's 2/10 → 5/10 into "20% lên 50%, gấp 2,5 lần", which the persona file forbids.
  - It presented a 40/30/20/10 content ratio as a rule.
  - It said "Facebook đang ưu tiên video ngắn" with no source.
  - It offered a ready caption for cô Hoa's photo ("sau 5 tháng chăm sóc da đều đặn") and said "ảnh vẫn đăng được" once she agrees.
  - It printed "70%" and "gấp đôi" inside advice not to use them.

### Reading the grades

- **Failures that just mean "not the kit's format".** I1 (no NEXT line) and day0_timing (no step tags, so no Map or film-ready step is detected) fail for any plain assistant. They show that the kit's format is missing. They do not measure quality.
- **False positives found in this pass.**
  - en/coldstart-coach I17 "killer" is the coach's own "Zero is the killer". "gold", "perfect" and "love it" are real praise.
  - vn/proof-coach I11 "số 1" is "bài số 1" (post #1).
  - vn/proof-coach I14 cites reply 3, where "chấm" means grading. The real issue is in reply 4: it warns that "chấm" posts get less reach and swaps the CTA to comment "SỔ".
  - vn/proof-coach I15: some of the "mình" hits are public-post hooks, where "mình – các chị em" is correct. The reply-3 inclusive "mình" is a real slip.
  - vn/hanh I9 "insight" is the assistant explaining an English word.
  - vn/hanh I15 hits are "cô" Hoa, "cô" giáo and "tiếng Anh".
  - vn/hanh I8 "15" and "35" are video timestamps.
  - vn/hanh I6 counts three uses of "chọn". Only reply 4's "câu khác chị có thể chọn" is a real extra decision.
- **Known miss.** I2 passes on en/proof-coach, but reply 1 asks for an "I help [who] go from [...] to [...]" fill-in, because the template regex does not match `[who]`.

## Honest limits

- **One simulator wrote both sides, and it had read the persona files.** Independence is only approximate. This check found 10 small assistant-side leaks, which suggests there is still some pull toward the persona's own framing. The real-account runs in G7/G8 are the true test.
- **The assistant is a model imitating a typical assistant, not a real ChatGPT Free or Plus session.** A real free-tier model could do worse, for example with longer walls of text or more fabricated statistics. It could also do better.
- **Quit triggers were read generously, so "film-ready" is a best case.**
  - en/proof-coach: a strict reading quits at reply 1, which had a template, "pillars" and about 380 words before anything usable.
  - en/coldstart-coach: a strict reading quits at reply 1, a 4-question form.
  - vn/proof-coach: reply 1 was a 5-question form. She quit at 28.7 min anyway.
  - vn/hanh: a strict reading of "two questions in one message" and "longer than one phone screen" loses her by reply 4.
- **There is one run per persona, and nothing has been scored for Edge.** The G3 gate needs the median of 3 runs and Edge scores from the validated judge, so these folders cannot yet give the "beat by ≥2 Edge points" comparison.
- **Some behaviour was not simulated.** These runs leave out the voice-mode first tap (counted as about +0.3 min where noted), Hạnh's 9-minute recording loss, and the Free-plan message limits. Timing is modelled, and vn/proof-coach's quit depends on its speed assumptions (see its `notes.md`).
