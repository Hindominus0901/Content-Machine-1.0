# Content Machine 1.0: Character Core and Edge Check v2 (design spec)

**How the founder's thesis becomes design rules**
1. **Character attracts people.** Money, freebies and a résumé only borrow attention, because anyone can copy or outbid them. The Edge Check penalises any post where one of these is the whole hook.
2. **There are two attraction modes.** *Admirable* means "who I want to BE". *Likable* means "who I want to be AROUND". Every post is tagged with one of them.
3. **Polarize on ideas. Stay warm with people.**
4. **Be absolute about yourself and calibrated about the world.** State values with no hedge. State outcomes as ranges or conditions.
5. **Proof is what licenses being definitive.** A stance with no anchor in the Character Card is the cheap AI contrarian content the founder warns about.

**Module flow.** Run this once, then refresh every 90 days.
1. Excavation Interview: 45–60 min, or 3 sittings of about 20 min.
2. Buyer Mirror: async, 5–12 clients.
3. Character Card.
4. Stance Bank.
5. Ideation formats.
6. Every script is scored by Edge Check v2 against the Card.

---

## A. CHARACTER CORE

### A1. Excavation Interview (EN + VN)

#### Interviewer rules (system block for the skill)

1. **One question per message.** Never stack questions.
2. **Voice first.**
   - EN: "Tap the mic and ramble for 2–3 minutes. Messy is better. Don't write, talk."
   - VN: "Bấm mic nói thoải mái 2–3 phút. Lộn xộn cũng được. Đừng viết, cứ nói."
3. **Ask for scenes, not adjectives.** If an answer is abstract ("I value honesty"), ask for the scene.
   - EN: "When, where, who was there, what did you say, what did it cost?"
   - VN: "Lúc đó là khi nào, ở đâu, có ai, bạn đã nói gì, mất gì?"
4. **Use at most 2 probes per question, then move on.** Mark missing answers `[GAP]` instead of forcing them.
5. **Ladder to the value.** Ask up to 3 times: "Why does that matter to you?" / "Vì sao điều đó quan trọng với bạn?"
6. **Break hedges with a bet.** If the user hedges ("I guess maybe…"), ask:
   - EN: "If you had to bet $100, what's the answer?"
   - VN: "Nếu phải cược 1 triệu, bạn chọn câu nào?"
7. **Capture voice verbatim.** Copy 1–2 exact phrases per answer into `Voice Samples`. Don't fix the grammar. With VN speech-to-text, only fix obvious diacritic or transcription errors, and confirm any unclear word.
8. **Flag quiet truths.** When the user says "I can't say that publicly" or "Không dám nói công khai", tag it `[QT]`. It becomes a candidate for a "post the one that scares you" piece, subject to safety gate G1.
9. **Stay neutral.** No praise, no coaching, no softening. After each answer, reflect back one line, for example: "So the line you won't cross is X."
10. **Sittings:**
    - S1: Q1–4 (values, refusals, enemy)
    - S2: Q5–8 (stances, trait, taste)
    - S3: Q9–12 (flaws, voice, vision, mirror)

#### The 12 questions

Q1 to Q12 are listed below. For each one: the EN and VN question, two probes in EN and VN, and what it extracts into the Card.

**Q1. Turning point**
- EN: "Take me back to the moment you decided to do this work. Where were you, and what happened?"
- VN: "Kể mình nghe khoảnh khắc bạn quyết định làm nghề này. Lúc đó bạn ở đâu, chuyện gì xảy ra?"
- Probes:
  - "What were you doing before, and what did you hate about it?" / "Trước đó bạn làm gì, và bạn ghét điều gì ở nó?"
  - "What did you tell yourself that day? Exact words." / "Hôm đó bạn tự nói với mình câu gì? Nguyên văn."
- Extracts: origin scene, early signal of the enemy, a voice sample.

**Q2. A principle that cost you**
- EN: "Tell me about a time a principle cost you money, a client or a relationship."
- VN: "Kể một lần bạn giữ nguyên tắc mà mất tiền, mất khách, hoặc mất lòng ai đó."
- Probes:
  - "Roughly how much did it cost?" / "Mất khoảng bao nhiêu?"
  - "Same situation tomorrow: would you do it again? Why does that matter?" (ladder x3) / "Mai gặp lại, bạn có làm y vậy không? Vì sao điều đó quan trọng?"
- Extracts: values in action (§3), principle #1 (§2).

**Q3. Refusals**
- EN: "What do you refuse to do in your work, even though it would pay?"
- VN: "Việc gì trong nghề bạn nhất quyết không làm, dù làm thì ra tiền?"
- Probes:
  - "When were you last tempted?" / "Lần gần nhất bạn bị cám dỗ là khi nào?"
  - "People who do it anyway: what happens to their clients? No names." / "Người vẫn làm thì khách của họ bị gì? Không cần nêu tên."
- Extracts: "I never…" principles (§2).

**Q4. Quiet intolerance**
- EN: "What does your industry complain about privately but never say in public? What are you quietly intolerant of?"
- VN: "Trong ngành bạn, điều gì ai cũng than sau lưng nhưng không ai nói công khai? Điều gì bạn âm thầm không chịu nổi?"
- Probes:
  - "Give me one example from this month." / "Cho mình một ví dụ ngay trong tháng này."
  - "If that old way had a name, what would you call it?" / "Nếu đặt tên cho 'cách cũ' đó, bạn gọi nó là gì?"
- Extracts: the enemy and its old-way name (§4), `[QT]` items.

**Q5. Contrarian truth**
- EN: "What do most people in your field believe that you think is wrong?"
- VN: "Điều gì phần lớn người trong nghề tin là đúng, mà bạn thấy sai?"
- Probes:
  - "How do you know? What did you see with your own clients?" / "Sao bạn biết? Bạn thấy gì ở chính khách của mình?"
  - "Say it out loud: 'Most ___ think ___. The truth is ___.'" / "Nói to: 'Đa số ___ nghĩ ___. Sự thật là ___.'"
- Extracts: contrarian truth (§5), with a link to proof.

**Q6. Ban one piece of advice**
- EN: "If you could ban one piece of advice in your industry forever, which one, and what replaces it?"
- VN: "Nếu được cấm vĩnh viễn một lời khuyên trong ngành, bạn cấm câu nào và thay bằng câu gì?"
- Probes:
  - "What would you argue about at dinner until midnight?" / "Chủ đề nào bạn cãi được tới nửa đêm?"
  - "Which client story proves you right?" / "Câu chuyện khách hàng nào chứng minh bạn đúng?"
- Extracts: hills to die on (§6), the new way (§4).

**Q7. The extreme trait**
- EN: "Which trait of yours do people call 'a bit too much'?"
- VN: "Nét tính cách nào của bạn hay bị bảo là 'hơi quá'?"
- Probes:
  - "When did it annoy someone? When did it win you a client?" / "Có lần nào nó làm ai khó chịu? Có lần nào nó giúp bạn chốt khách?"
  - "Would your biggest fan and your harshest critic both name it?" / "Fan cứng nhất và người ghét bạn nhất có cùng gọi tên nó không?"
- Extracts: the ONE extreme trait (§1), its 10/10 version, and who it repels.

**Q8. Taste, rituals, money**
- EN: "Walk me through your non-negotiables: daily rituals, things you'd never wear, use or say, and where your money goes that a stranger would find odd."
- VN: "Kể mình nghe những thứ 'không bao giờ bỏ': thói quen hằng ngày, thứ bạn không bao giờ mặc, dùng hay nói, và chỗ bạn tiêu tiền mà người lạ thấy hơi lạ."
- Probes:
  - "Why that instead of the normal choice?" / "Vì sao chọn vậy mà không chọn như mọi người?"
  - "Which two things about you 'don't go together'?" / "Hai điểm nào ở bạn tưởng 'không đi chung' với nhau?"
- Extracts: quirks and rituals (§8), material for the flipped-paycheck format, the contradiction pair.

**Q9. Where you look bad**
- EN: "What did you get wrong for years? Where do you still look bad?"
- VN: "Điều gì bạn từng làm sai suốt nhiều năm? Đến giờ bạn vẫn còn 'dở' ở đâu?"
- Probes:
  - "What did it cost you or a client?" / "Cái sai đó làm bạn hoặc khách mất gì?"
  - "Who should NOT hire you?" / "Ai thì KHÔNG nên thuê bạn?"
- Extracts: honest flaws (§9), two-sided proof, the "not for" line.

**Q10. How you talk (voice only)**
- EN: "A client says 'I've tried everything.' Answer them now, out loud, like on a call."
- VN: "Khách nói: 'Em thử đủ cách rồi mà không được.' Trả lời họ ngay, nói như đang gọi điện."
- Probes:
  - "What do you say to clients over and over?" / "Câu nào bạn nói với khách đi nói lại hoài?"
  - "Which industry words make you cringe?" / "Từ nào trong ngành làm bạn nổi da gà?"
- Extracts: voice samples, repeated phrases and banned words (§10). Transcribe raw.

**Q11. Vision**
- EN: "If your work wins, what's different in 10 years for your clients and your industry? What's normal today that will look embarrassing?"
- VN: "Nếu những gì bạn làm thắng, 10 năm nữa khách và cả ngành khác thế nào? Điều gì bình thường hôm nay sẽ thành đáng xấu hổ?"
- Probes:
  - "Who does your client become? How do they describe themselves?" / "Khách của bạn trở thành người thế nào? Họ tự mô tả ra sao?"
  - "What do 'people like us' do that others don't?" / "'Người như chúng ta' làm gì mà người khác không làm?"
- Extracts: vision, the client's future identity, the tribe line (§7).

**Q12. Why they pick you**
- EN: "Why do your best clients pick you over someone cheaper or more famous? Use their words, not yours."
- VN: "Vì sao khách tốt nhất chọn bạn thay vì người rẻ hơn hoặc nổi tiếng hơn? Dùng lời của họ, đừng dùng lời của bạn."
- Probes:
  - "Name one client. What exactly did they say?" / "Kể tên một người. Nguyên văn họ nói gì?"
  - "Who did they almost choose instead?" / "Họ suýt chọn ai khác?"
- Extracts: a working hypothesis for the Buyer Mirror, which the user then checks with the Buyer Mirror script below.

**Closing question**
- EN: "Which answer made you nervous to say out loud? That one goes to the top of your Stance Bank."
- VN: "Câu trả lời nào làm bạn ngại nói ra nhất? Câu đó lên đầu Kho quan điểm."

**After the interview, the AI:**
1. Drafts the Card.
2. Proposes 3 candidate extreme traits, each with its evidence, and asks the user to pick ONE.
3. Marks any value without a cost story as `[UNPROVEN VALUE]`. Content may not use that value until a story exists.
4. Lists the `[GAP]`s.

#### Buyer Mirror mini-script (for clients)

**Setup**
- Ask 5–12 clients: your best ones, plus 1–2 who almost didn't buy.
- Use a voice note, a 10-minute call or a form.
- Never ask inside a sales context.

**Invite**
- **EN:** "Quick favour: I'm rewriting how I describe my work and I want to use your words, not mine. Could you answer 5 questions in a voice note? About 5 minutes, no wrong answers. I'll only quote you anonymously, and only with your OK."
- **VN:** "Nhờ bạn một việc nhỏ nhé: mình đang viết lại cách giới thiệu công việc và muốn dùng chính lời của bạn, không phải lời của mình. Bạn trả lời giúp 5 câu bằng tin nhắn thoại được không? Khoảng 5 phút, không có câu sai. Mình chỉ trích dẫn ẩn danh, và chỉ khi bạn đồng ý."

**Questions**

| # | EN | VN |
|---|---|---|
| 1 | What was going on when you started looking for help? What had you already tried? | Lúc bắt đầu tìm người giúp, bạn đang gặp chuyện gì? Bạn đã thử những cách nào? |
| 2 | What almost stopped you from working with me? | Điều gì suýt làm bạn không chọn mình? |
| 3 | Why me and not someone else? Who else did you look at? (Ladder x2: "Why does that matter to you?") | Vì sao là mình mà không phải người khác? Bạn đã cân nhắc ai? (Hỏi tiếp x2: "Vì sao điều đó quan trọng với bạn?") |
| 4 | Describe me to a friend in one sentence. | Giới thiệu mình cho một người bạn bằng một câu, bạn sẽ nói gì? |
| 5 | What do I do that annoys you a little? Be honest. | Mình có điểm gì làm bạn hơi khó chịu không? Cứ nói thật. |
| Close | Can I quote any of this, without your name? | Mình trích vài câu, không kèm tên, được không? |

**Processing**
- Transcribe verbatim.
- Tally repeated phrases:
  - said by 2 or more clients: candidate signature keyword
  - said by 3 or more: confirmed signature keyword
- Write down the gap between the user's own Q12 answer and what clients actually said. That gap is content.
- Q5 answers usually show the extreme trait in its "too much" form.
- Output: a tally table that feeds Card §11 and format F3.

---

### A2. Character Card (one page, living document)

#### Template

```
CHARACTER CARD — [Name] · v[1.0] · [date] · refresh by [date + 90d]
WHO: [role] for [audience]            NOT FOR: [one line]
XƯNG HÔ (VN): [mình–bạn | tôi–anh chị | chúng ta | anh/chị–em]
DIALS: Expertise [new | established] · Heat default EN [1–3] / VN [1–3]

1  EXTREME TRAIT: [one word or phrase]
   10/10 version: [one scene] · Repels: [who]
2  PRINCIPLES (3–5): I always/never [x] because [y].
3  VALUES IN ACTION (3): [value] | [story] | cost: [number]
4  ENEMY  Old way "[name]": [what it does] → hurts [who]
          New way "[name]": [what we do instead]
5  CONTRARIAN TRUTH: Most [peers] think [X]. The truth is [Y].
6  HILLS (3): [stance] | proof | heat 1–3 | campaign weeks
7  VISION: In [N] years, [picture]. [Today's norm] will look [embarrassing].
   Tribe line: People like us [do X].
8  TASTE · QUIRKS · RITUALS (3–5) + CONTRADICTION: "[trait] but [trait]"
9  WHERE I LOOK BAD (2–3): [mistake] | cost | what I do now
10 VOICE: 5 verbatim phrases · rhythm · words I use · words I ban
11 SIGNATURE KEYWORDS: client words (count) · my coined terms (≤5)
12 PROOF BANK: [link] · top 5 numbers/stories
13 HARD LIMITS: topics I never polarize on
LOG: changes · resonance (phrases the audience repeated back, with count)
```

#### Field rules

| § | Rule | Source |
|---|---|---|
| 1 | Exactly ONE trait. Fans and critics must both name it. Its 10/10 version is a scene, not an adjective. | Q7, Buyer Mirror Q5 |
| 2 | Each principle uses the form "always/never … because …". 3 minimum, 5 maximum. | Q2, Q3 |
| 3 | Each value needs a story with a real cost (money, client, time). Without one it is marked `[UNPROVEN]`. | Q2 |
| 4 | Attack a practice or system, never a person or group. Give the old way a name. | Q4, Q6 |
| 5 | Must pass the 3D test (Disagree, Defend, Demonstrate; see A4). | Q5 |
| 6 | Three hills, each with proof. These are the 3 big ideas for campaign mode (4–6 weeks each). | Q6 |
| 7 | Must name the client's future identity. | Q11 |
| 8 | At least one contradiction pair. Each item states the value behind it. | Q8 |
| 9 | At least 2 entries with their cost, plus a "not for" line. | Q9 |
| 10 | Phrases are verbatim and never AI-polished. | Q10 |
| 11 | Client words outrank coined terms. Coined terms capped at 5. | Buyer Mirror |
| 13 | Defaults come from A4's red list. The user may add to it but not remove from it. | A4 |

#### Keeping the Card alive

Update the Card when any of these happens:
- every 90 days
- after each Buyer Mirror batch
- when a phrase shows up in 3 or more comments or DMs (add it to §11)
- when a stance is retired (record why in the log)
- when a new cost story happens (§3)

Any `[GAP]` or `[UNPROVEN]` field triggers a reminder in the weekly ideation run.

#### Worked example: a speaking coach

```
CHARACTER CARD — Mai Phương · v1.0 · 2026-10-05 · refresh by 2027-01-03
WHO: Speaking & confidence coach for introverted professionals (engineers,
     analysts, doctors) who must present.
NOT FOR: people who need to be stage-ready in 7 days or want to be entertainers.
XƯNG HÔ (VN): mình–bạn (content) · tôi–anh chị (corporate workshops)
DIALS: Expertise established (8 yrs) · Heat EN 2 / VN 1–2

1  EXTREME TRAIT: Over-preparation.
   10/10: rehearsed a 12-min TEDx talk 31 times, out loud, in a parked car.
   Repels: improvisers, "just wing it" people, hype lovers.
2  PRINCIPLES
   - I never teach "fake it till you make it", because faked confidence dies at question one.
   - I always make clients rehearse out loud, because silent practice is daydreaming.
   - I never let a slide carry more than 6 words, because if the slide talks, you don't.
   - I always give clients a range, never a promise: most need 8–12 weeks.
3  VALUES IN ACTION
   Honesty > hype  | turned down a bank's "high-energy keynote" contract, 2024 | ~$5k / 120tr
   Respect quiet   | refused to push a client on stage early; his boss pulled the account | 1 account
   Preparation     | cancelled a workshop I couldn't rehearse; refunded 40 seats | 40 refunds
4  ENEMY  Old way "the Loud School": be louder, power-pose, fake it, wing it
          → hurts introverts who conclude "I'm just not a speaker."
          New way "Quiet Authority / Tự tin trầm": rehearse until boring,
          speak slower, pause on purpose, one idea per slide.
5  CONTRARIAN TRUTH: Most people think confidence comes before preparation.
   The truth: preparation nobody sees IS the confidence.
6  HILLS
   1 "Confidence isn't volume."                     | 140 clients, none trained louder | heat 2 | W1–6
   2 "Boring = ready."                              | 20-Rep Rule; TEDx 31 reps        | heat 2 | W7–12
   3 "Stop cutting 'um'. Start cutting slides."     | [pause-count data]               | heat 3 | W13–18
7  VISION: In 10 years the quietest person in the room is the one everyone
   waits for. "Be more outgoing" will sound as dated as "smoking helps focus."
   Tribe line: People like us prepare in private and speak once, clearly.
8  QUIRKS: rehearses in the "car studio" · warm water only on talk days ·
   refuses headset mics (a handheld lets her lower it and pause) ·
   12-year-old Vios, monthly voice coach.
   CONTRADICTION: "Introvert who teaches public speaking." · "Hates small talk, loves Q&A."
9  WHERE I LOOK BAD
   Froze 40 seconds on a 2019 panel | lost 2 leads, avoided panels for months | now teaches the "40-second rule"
   Taught power poses for 3 years   | ~30% of clients quit by week 4          | banned from curriculum
   Slow: 8–12 weeks, not 2          | loses quick-fix buyers                  | says so on the sales page
10 VOICE: "Say it slower. Slower than that." · "Your pause isn't a mistake.
   It's punctuation." · "Rehearse until it's boring, then twice more." ·
   "Nobody remembers your slides. They remember one sentence." ·
   VN: "Chậm lại. Chậm hơn nữa." · "Khoảng lặng không phải lỗi, nó là dấu chấm câu."
   Rhythm: short imperatives, warm, zero hedges. Uses: rep, car studio.
   Bans: crush it, slay the stage, power pose, unleash · tỏa sáng, bùng nổ năng lượng.
11 SIGNATURE KEYWORDS
   Client words (n=11): "made me feel normal for being quiet" (7) · "calm" (6) ·
   "no hype" (5) · VN: "chị ấy không bắt mình phải diễn" (4/6)
   Coined: Quiet Authority · 20-Rep Rule · Boring = Ready · Car Studio · 40-second rule
12 PROOF BANK: 140 clients since 2018 · TEDx 2023 · [weeks-to-first-calm-talk median]
13 HARD LIMITS: never mock extroverts or name other coaches · no medical
   claims about anxiety (refer out) · no "guaranteed promotion" · no politics
LOG: v1.0 = interview + Buyer Mirror (11 clients)
```

---

### A3. Character content formats

#### Stage model

- **Admirable ("I want to BE them").** Competence, standards, stances and results shown with what they cost. This earns attention and respect.
- **Likable ("I want to be AROUND them").** Warmth, quirks, flaws and shared values. This earns affinity and keeps people around.
- **Overlay tags.** *Trust* means two-sided truth or the buyer mirror. *Convert* means a filter plus an invitation.

**Sequencing.** A flaw makes a person more likable only after their competence is visible (the pratfall effect). So:
- new or small audiences: Admirable to Likable at about 2:1
- established audiences: about 1:1

**Weekly mix (fits 1–2 h):**
1. 1 Stance (Admirable)
2. 1 Value told through a stance (Admirable)
3. 1 Likable post, rotating between quirk, flaw and flipped format
4. 1 Trust post, alternating between a values-in-action story and the buyer mirror

Examples below use Mai's Card. The `[ ]` slots get filled from the user's Card.

**F1. Stance post ("hill")**
- Stage: Admirable. Card: §6, §4, §9.
- Beats: claim (12 words or fewer) → name the old belief → refute it with a reason → proof → "I used to…" → boundary → question CTA.
- EN: "Confidence isn't volume."
- VN: "Tự tin không nằm ở giọng to."

**F2. The day I said no (values-in-action cost story)**
- Stage: Admirable and Likable. Card: §3.
- Beats: the offer (with the number) → why it tempted you → the line it crossed → what you said, verbatim → what it cost → "I'd do it again" → the principle in one line.
- EN: "I turned down $5,000 because they wanted me to make their engineers louder."
- VN: "Mình từ chối hợp đồng 120 triệu vì họ muốn kỹ sư của họ 'nói to lên'."

**F3. Buyer mirror**
- Stage: Trust and Likable. Card: §11.
- Beats: "I asked [N] clients why they chose me" → what you expected → the actual tally, with verbatim quotes → what that says we value → "if that's you…".
- EN: "I asked [11] clients why they hired me. None said 'results'."
- VN: "Mình hỏi [11] học viên vì sao chọn mình. Không ai nói 'vì kết quả'."

**F4. Old way vs new way**
- Stage: Admirable. Card: §4.
- Beats: split screen. The old way does X and leads to its result. The new way does Y and leads to its result. Name both ways. One line on why.
- EN: "The Loud School vs Quiet Authority."
- VN: "Trường phái 'nói to' và Tự tin trầm."

**F5. What I got wrong for [N] years**
- Stage: Likable and Trust. Card: §9.
- Beats: the belief you taught → the evidence it failed, with its cost → the moment you saw it → what you do now → (if established) what you still don't know.
- EN: "For 3 years I taught power poses. I was wrong."
- VN: "3 năm liền mình dạy power pose. Mình đã sai."

**F6. Quiet truth ("the one that scares you")**
- Stage: Admirable. Card: `[QT]` items, §4. Heat 3, and gate G1 is mandatory.
- Beats: say the private complaint in public → why nobody says it → evidence → what to do instead → boundary.
- EN: "Most speaking training teaches you to perform, not to be understood."
- VN: "Phần lớn lớp thuyết trình dạy bạn diễn, không dạy bạn được hiểu."

**F7. Rituals and non-negotiables**
- Stage: Likable. Card: §8.
- Beats: "[N] things I do that look weird" → each ritual plus the value behind it → "people like us…".
- EN: "I rehearse in a parked car. Here's why."
- VN: "Mình tập nói trong xe đang đậu. Đây là lý do."

**F8. Flipped paycheck ("where my money goes")**
- Stage: Likable. Card: §8, §3.
- Beats: income (optional; a range, or leave it out) → what you refuse to spend on → what you overspend on → the value each reveals.
- EN: "I drive a 12-year-old Vios. I pay a voice coach every month."
- VN: "Mình đi con Vios 12 năm tuổi. Nhưng tháng nào cũng trả tiền thầy luyện giọng."

**F9. Not-for-you filter**
- Stage: Convert and Admirable. Card: §9 "not for", §1 "repels".
- Beats: "Don't hire me if…" x3 → "Hire me if…" x2 → invitation.
- EN: "Don't hire me if you need to be stage-ready by Friday."
- VN: "Đừng thuê mình nếu bạn cần lên sân khấu ngay thứ Sáu này."

**F10. Words I banned**
- Stage: Likable and Admirable. Card: §10 bans.
- Beats: the banned phrase → why it hurts → what we say instead (x3).
- EN: "Three phrases banned in my sessions."
- VN: "3 câu bị cấm trong lớp của mình."

**F11. Defend the nuance** (Hormozi)
- Stage: Admirable. Card: §2.
- Beats: "Everyone says Y. I do X." → the reason → the cost you accept → when Y is actually right (calibration).
- EN: "Every coach says cut your ums. I tell clients to keep them."
- VN: "Ai cũng bảo bỏ 'ờ, à'. Mình bảo cứ giữ."

**F12. Vision / people like us**
- Stage: Admirable (tribe). Card: §7.
- Beats: the future picture → what becomes embarrassing → what "people like us" do now → invitation.
- EN: "In 10 years, the quietest person in the room will be the one everyone waits for."
- VN: "10 năm nữa, người trầm nhất phòng họp sẽ là người cả phòng chờ nghe."

**F13. Stance stitch (react to the idea)**
- Stage: Admirable. Card: §6.
- Beats: quote a common piece of advice (anonymised; in VN never show or name the creator) → "here's why I disagree" → proof → what to do instead.
- EN: "'Fake it till you make it.' No. Here's what happens at question one."
- VN: "'Cứ giả vờ tự tin đến khi tự tin thật.' Không. Đây là chuyện xảy ra ở câu hỏi đầu tiên."

**F14. Extreme-trait showcase**
- Stage: Likable and Admirable. Card: §1.
- Beats: show the trait at 10/10 with a receipt → why → who it's not for.
- EN: "A 12-minute talk. 31 rehearsals. Here's rep 1 vs rep 31."
- VN: "Bài nói 12 phút, mình tập 31 lần. Đây là lần 1 và lần 31."

#### Flipped-format remixes

**Rule:** keep the viral format's recognisable shell (framing, pacing, sound). Swap the payload from status to values. Every flip must reveal a choice and the value behind it.

| Viral format | Flip | Hook EN | Hook VN |
|---|---|---|---|
| Day in the life | Day of someone who refuses a norm | "A day as a speaking coach who bans slides over 6 words." | "Một ngày của coach thuyết trình cấm slide quá 6 chữ." |
| What I spend in a week | What my values cost this week | "What my principles cost me this week: [$X] and one client." | "Tuần này nguyên tắc của mình tốn [X triệu] và một khách hàng." |
| Income report | Turned-down report | "Q3 report: money I turned down, and why." | "Báo cáo quý 3: những khoản mình đã từ chối, và lý do." |
| Paycheck breakdown | Flipped paycheck | "Where my money goes says more than what I earn." | "Tiền mình tiêu vào đâu nói về mình rõ hơn mình kiếm bao nhiêu." |
| GRWM | Get ready for a hard "no" | "Get ready with me to turn down a client." | "Chuẩn bị cùng mình trước cuộc gọi từ chối khách." |
| What's in my bag | Objects that hold my standards | "3 things in my bag that keep me honest on stage." | "3 món trong túi giữ mình không 'diễn' trên sân khấu." |
| Red flag / green flag | Clients I say no to | "Red flags I turn down. Green flags I chase." | "Cờ đỏ khiến mình từ chối, cờ xanh khiến mình chủ động mời." |
| Tier list | Industry advice, ranked from useful to harmful | "Ranking popular speaking advice, useful to harmful." | "Xếp hạng lời khuyên thuyết trình: từ hữu ích đến có hại." |
| POV | Your coach tells the truth | "POV: you hired a coach who says 'not ready yet'." | "POV: bạn thuê một coach dám nói 'chưa sẵn sàng đâu'." |
| Things I'd never buy | Things I'll never sell | "5 things I'll never sell, even though they'd pay." | "5 thứ mình không bao giờ bán, dù bán là có tiền." |
| Glow-up before/after | Process, not glow-up | "Rep 1 vs rep 20 of the same talk." | "Lần tập 1 và lần tập 20 của cùng một bài nói." |
| Haul / unboxing | Unboxing my worst month | "Unboxing my worst month: numbers and lesson." | "Mở hộp tháng tệ nhất của mình: số liệu và bài học." |

---

### A4. Polarity guide

**Principle:** polarize on ideas, methods and standards, and stay warm with people. Hostility toward a group is the strongest predictor of shares, and it is toxic (Rathje 2021). Receptive language with people reduces personal attacks (Yeomans 2020).

| Zone | Polarize on / handle | Examples |
|---|---|---|
| **Green: go** | Ideas and beliefs | "Confidence comes first" |
| | Methods and practices | power posing, free discovery calls, 6-week shreds |
| | The old way and industry norms | "đua giá", hustle-as-proof |
| | Systems and big rivals (the underdog effect, Paharia 2014) | mass-market "one-size" programs |
| | Standards, trade-offs and pace | slow over fast, price, homework rules |
| | Fit: who you serve and who you don't | about fit, never about worth |
| | Taste | no-slide talks, no headset mic |
| **Yellow: reframe** | Professional peers as a category | turn "most coaches are frauds" into "most coaching programs skip X" |
| | Client behaviour | a pattern, anonymised, never mocking |
| | Platforms and tools | criticise the mechanic, not the users |
| | Your past self | the safest target there is |
| **Red: hard limits** | Identity groups | gender, ethnicity, religion, age, region (Bắc/Nam), body, disability, sexuality, nationality, personality-as-identity (e.g. "extroverts are shallow") |
| | People and brands | named individuals, competitors, KOLs, brands |
| | Off-limits topics | politics and the state (a hard limit in VN), tragedies, news-jacking |
| | Promises | guaranteed health, financial or legal outcomes |
| | Punching down | at beginners or clients |
| | Claims | anything unprovable (defamation risk) |
| | Outrage | outrage with no teaching underneath |

**Heat dial.** Never go above 3.
1. **Mild:** "I stopped doing X."
2. **Firm:** "Stop X. Do Y."
3. **Spicy:** "X wastes your time, and the industry knows it." It still targets an idea.

Defaults:
- New coaches: 2.
- Established coaches: 2–3.
- VN B2B and older audiences: one notch lower in topic aggression. The wording stays definitive.

**"Scares you" protocol.**
1. Draft the stance at heat 1, 2 and 3.
2. Ask "Which one are you nervous to post?"
3. If it passes gates G1 and G2, recommend that one.

#### Stance generator (skill block)

```
ROLE: Stance Generator. Inputs: Character Card, Proof Bank, optional topic.
Use only Card facts. Never invent numbers; leave [brackets].
Generators (2 stances each):
 S1 Enemy      → "Stop [old way]. Do [new way]. [principle as reason]."
 S2 Principle  → "I will never [violation]. Even when it costs [cost]."
 S3 Contrarian → "Most [audience] think [X]. They're wrong. [mechanism]. [proof]."
 S4 Trait      → "I'm the most [trait] [role] you'll meet. Want [opposite]? Hire someone else."
 S5 Flaw       → "I [old way] for [N] years. It cost [X]. Now I believe [Y]."
 S6 Vision     → "In [N] years, [today's norm] will look like [analogy]."
 S7 Diagnosis  → "You don't have a [X] problem. You have a [Y] problem." (max 1 per post)
 S8 Taste      → "[industry habit] is [noise/lazy]. My standard: [Z]."
 S9 Mirror     → "[N] of [M] clients said '[phrase]'. That's the method."
Filter: drop if it fails 3D — Disagree (a sensible peer could), Defend (in 2 sentences),
Demonstrate (Card proof or story) — or Gate G1.
Score: Card anchor 0–2 + proof ready 0–2 + nervous-to-post +1. Write top 5 at heat 1/2/3.
Output table: stance | generator | Card § | proof | heat | suggested format (F1–F14) | verdict.
Dedupe against the last 30 days. Slot the top 3 into campaign mode (4–6 weeks each).
```

**Worked output for Mai:**

| Stance | Gen | Proof | Heat | Format | Verdict |
|---|---|---|---|---|---|
| "Stop practising in your head. Rehearse out loud, 20 reps." | S1 | 20-Rep Rule | 2 | F1 | PASS |
| "I will never teach you to fake confidence. Even when a bank pays $5k for it." | S2 | §3 | 2 | F2 | PASS |
| "Most people think confidence comes before prep. Backwards." | S3 | 140 clients | 2 | F4 | PASS |
| "I'm the most over-prepared coach you'll meet. Want to wing it? Hire someone else." | S4 | TEDx 31 reps | 3 | F14 | PASS |
| "I taught power poses for 3 years. A third of my clients quit." | S5 | §9 | 1 | F5 | PASS |
| "Extroverts make terrible leaders." | S3 | none | 3 | – | **REJECT** (identity group, no proof). Repair: "Volume isn't leadership." (S8, heat 2) |

#### VN calibration notes

1. **Admit first, then stand firm ("Nhận trước, đứng vững sau").** Open with your own mistake, then state the stance firmly. This protects face (thể diện) and the stance still lands. Example: "Mình từng giảm giá 50% suốt 2 năm. Nên giờ mình nói thẳng: …"
2. **Attack "cách làm" or "lối cũ", never "người" (people).** "Mấy ông coach ngoài kia lừa đảo" ("those coaches out there are scammers") is a group attack, and it fails G1.
3. **Never name a person, brand, KOL or competing spa.** The FLC executive's insult case shows the costs: legal action and a rejected apology.
4. **Face test.** Would you say it in person to an "anh chị đi trước" (a senior you respect)? If not, lower the heat or reframe.
5. **Pick one xưng hô at setup and keep it.**
   - mình–bạn: peer, warm
   - tôi–anh chị: respectful B2B
   - chúng ta: tribe
   - anh/chị–em: warm, but risky across ages
   - "tôi–các bạn" can read as lecturing
6. **Definitive does not mean rude.** Keep relationship particles (nhé, nha, ạ for older or B2B audiences). Cut only the permission-seeking ones (xin phép, đúng không ạ).
7. **Exit-with-dignity lines:**
   - "Nếu bạn thích kiểu…, mình không phải người phù hợp. Không sao cả."
   - "Không hợp thì mình chia tay vui vẻ."
8. **A blunt persona needs a mentor tone to last.** Shark Bình's "phũ" persona shifted to mentoring over time, and VN press reports audiences tiring of repeated drama. Run recurring stances, not one-off hot takes.
9. **Income talk reads as "khoe" (showing off) more easily in VN.** In flipped-paycheck posts, the income figure is optional. Use a range, or leave it out.
10. **Sensitive VN topics:** filial and family duty, regions, gender roles, education as a system (frame it as "cách học cũ", the old way of learning), state and politics (a hard limit).
11. **Compliance.** Under the Advertising Law in force from 1 Jan 2026:
    - disclose ads before and during the promotion
    - only promote what you have used or understand
    - make no false claims

    The 2025 draft cultural code proposes restrictions on cooperation with KOLs who violate it.
12. **Length.** Hooks of about 15–18 syllables. Break long Western-style sentences.
13. **Certainty.** VN scores high on power distance, so definitive phrasing may land at least as well as in EN. This is an inference, not tested in Vietnam.

---

## B. EDGE CHECK v2

### 5. Rubric: five pillars, scored 0–2

#### Run order

1. **Load** the Card and Proof Bank. With no Card, run in **generic mode**: Authenticity and Character are capped at 1, and the verdict reads "PASS-GENERIC: run Character Excavation".
2. **Voice Lint.** Strip using the lists below.
3. **Borrowed-attractor detector** (§6).
4. **Score** the five pillars.
5. **Hard gates.**
6. **Auto-fix loop** (at most 2 passes). Fix Character first, because a new stance rewrites the post. Then Authority, Signature, Value, Authenticity, then re-lint.
7. **Report.**

#### P1. Signature keywords: "Does it sound like *us*?"

| Score | Criteria |
|---|---|
| 0 | Generic category language. None of the client words or coined terms in Card §11. The problem is named in expert jargon the audience doesn't use. |
| 1 | One signature term, but bolted on (only in the CTA or a hashtag), or a coined term used without the audience's own word for the problem. |
| 2 | At least one client verbatim phrase (2 or more mentions) or coined term appears in the hook or punch line, AND the problem is named in the audience's words. No more than 2 coined terms in the post (no jargon soup). |

**Auto-fix:**
- Replace the generic problem noun with the top Buyer Mirror phrase.
- Move the coined term into the hook or the last line.
- Cut coined terms beyond 2.
- If §11 is empty, insert `[SIGNATURE WORD?]` and ask: "What do clients call this problem?"

#### P2. Value: practical or identity

| Score | Criteria |
|---|---|
| 0 | No takeaway, a platitude ("consistency is key"), or 3 or more competing ideas. |
| 1 | A takeaway exists but is generic, can't be acted on, or is buried below line 3. |
| 2 | One big idea that fits in 15 words or fewer, visible by line 2, AND either a concrete step the viewer can do today (**practical**) or a clear "what I stand for / who this is for" that lets the viewer self-identify (**identity**, valid for Likable formats F3, F7, F8, F10, F14). |

**Auto-fix:**
- Apply the one-sentence test.
- Move any secondary ideas to the idea bank.
- Add a "Do this today:" line.
- Swap one abstract noun for a number, name or scene.

#### P3. Authority: proof beside the claim, two-sided

| Score | Criteria |
|---|---|
| 0 | Claims with no proof, invented stats, guarantees, or credibility that rests only on a résumé. |
| 1 | Proof exists but is generic ("helped hundreds") or far from its claim, or it is one-sided (only wins), or outcomes are stated as certainties. |
| 2 | Each main claim has a trust cue (number, client scene or receipt from the Proof Bank) within 2 sentences. Outcomes are stated as ranges or conditions. At least one cost, limit or "who it doesn't work for" line. |

**Auto-fix:**
- Pull the nearest Proof Bank item.
- Rewrite "will" outcomes as ranges, e.g. "most in 8–12 weeks; some longer".
- Add one limitation line.
- With no proof available, insert `[PROOF NEEDED: …]`. **Never fabricate.**

#### P4. Authenticity: the only-you test

| Score | Criteria |
|---|---|
| 0 | Fails the swap test: any coach could post it unchanged. Or 3 or more AI tells. Or the voice is unlike the Card §10 samples. |
| 1 | Some personal detail, but sanitised. Or a story format with no cost or flaw. Or 1–2 AI tells. |
| 2 | Passes the swap test: contains a detail only this person could write (scene, date, quirk, ritual, verbatim phrase). Cadence matches the §10 samples. Story formats include a cost or flaw. Zero AI tells. |

**Auto-fix:**
- Inject one Card scene or quirk.
- Rewrite one line in the rhythm of a voice sample.
- Strip AI fog.
- Replace "serves as" and "plays a role" with "is" and "does".

#### P5. Character & Polarity: would a sensible peer disagree, and would the right person lean in?

| Score | Criteria |
|---|---|
| 0 | No stance (neutral). OR a borrowed-attractor-only hook (§6). OR it attacks people or identity groups. |
| 1 | A stance exists but is generic (no Card anchor, i.e. AI contrarian), hedged, mentions the opposing view without refuting it, or has no boundary. |
| 2 | An **owned** stance that passes the 3D test, anchored to a Card element (trait, principle, enemy or hill), AND **definitive delivery** (zero hedges in the hook, present tense, answer first), AND it **refutes** the old view with a reason, AND it includes a boundary or "for us / not for them" line. |

For Likable formats, a stated choice with its value counts as an implicit stance. "I never use a headset mic, because…" scores 2 if it implies a standard that some people won't share.

**Auto-fix:**
- Run the Stance Generator on the topic and take the closest hill.
- Rewrite the hook from an A4 template.
- Add a refutation line and a boundary line.
- Strip hedges from the claim.

#### Hard gates (pass/fail, outside the score)

- **G1 Polarity safety.**
  - The target is an idea, practice or system.
  - No named people or brands, no identity groups, no punching down.
  - VN face test passed.
- **G2 Truth and claims.**
  - No invented numbers.
  - `[brackets]` block publishing until filled.
  - No guaranteed outcomes.
  - Sponsorship disclosed (VN Advertising Law from 1 Jan 2026).
  - Quoted clients consented.
- **G3 Voice Lint** (auto-fixed; fails only if still failing after fixes).
  - Hook: 12 words or fewer in EN, about 18 syllables or fewer in VN.
  - Hedges: zero in the hook and in claim lines. In the body, at most 1 per 100 words unless odds or a condition follows.
  - Sentences: average 15 words or fewer, none over 25, and at least one punch line of 5 words or fewer.
  - No throat-clearing.
  - AI tells: 1 or fewer.
  - At most one "not X but Y".
  - Questions appear only in the CTA.

#### Verdict rules

| Outcome | Condition |
|---|---|
| **PASS** | 8/10 or more, no pillar at 0, all gates pass |
| **PASS (stance formats)** | Formats F1, F4, F6, F9, F11 and F13 also need Character & Polarity at **2** |
| **EDGE** | 10/10 |
| **FAIL** | Any borrowed-attractor-only post (§6), whatever the total |
| **Auto-fix** | 6–7: run the loop (at most 2 passes), then hand back with "Needs you" questions |
| **Re-ideate** | 5 or below, or a G1 failure: send to the Stance Generator rather than polishing |

**Calibration ladder** (enforced in P3 and P5):

| Claim type | How to state it | Example |
|---|---|---|
| Values and choices | Absolute | "I don't take clients who skip homework." |
| Own patterns | Quantified | "In 140 calls…" |
| Outcomes for others | Range or odds, delivered confidently | "Most see it in 6–8 weeks; some take 12." |
| Banned | – | Certainty about other people's worth, guarantees, humblebrags, "I'm not sure but" |

**Expertise dial:**
- New coaches: no "might be wrong" lines.
- Established coaches: one "here's where I might be wrong" line is allowed.

#### Report format

```
EDGE CHECK v2 — [title] · Format F1 Stance · Stage Admirable · Heat 2
Lint: 9 strips (4 hedges, 2 fillers, 3 AI tells) · avg sentence 10 · hook 4 words
Detector: none
Scores: Signature 2 · Value 2 · Authority 1 · Authenticity 2 · Character 2 = 9/10
Gates: G1 pass · G2 HOLD ([PROOF NEEDED] x1) · G3 pass
Verdict: PASS — publish after 1 data fill
Fixes applied: hook rewritten from Hill #1; "journey", "crucial role" removed; boundary added
Needs you: "What's the median weeks-to-first-calm-talk from your client log?"
```

#### Strip list: EN

| Code | Category | Strip or flag | Replace with |
|---|---|---|---|
| H1 | Low-likelihood hedges | might, may, could, possibly, perhaps, maybe, potentially, arguably, to some extent, somewhat, I guess | Delete. If it's genuinely uncertain: a condition ("works if…"), odds ("7 in 10"), or an owned "I'd bet" / "likely" |
| H2 | Minimizers | a bit, a little, sort of, kind of, rather, quite, pretty much, fairly, more or less, in a sense | Delete |
| H3 | Empty intensifiers | very, really, super, truly, actually, literally, incredibly, extremely | A stronger verb or noun, or a number |
| H4 | Throat-clearing | "So today I want to talk about", "I just wanted to share", "Let me start by saying", "In this video", "Hey guys" | Delete; open with the claim |
| H5 | Self-undercutting | just, only (used as an apology), "I'm no expert but", "hopefully this helps", "if that makes sense", "I could be wrong but", "I'm not sure but", "quick tip" | Delete. For real doubt: "My bet: X. Here's what would change my mind." |
| H6 | Validation tags | right?, you know?, don't you think?, isn't it?, agree? | A period. Questions go in the CTA |
| H7 | Ownerless openers | it seems, it could be argued, some say, many believe, "in my opinion" before facts | State it, or own it ("I'd argue…", "In 140 calls…") |
| H8 | AI fog | "it's important/worth noting", "plays a crucial/pivotal role", serves as, represents, "in today's fast-paced world", navigate, delve, unlock, unleash, elevate, landscape, journey, game-changer, "various factors", "everyone's journey is unique", "results may vary" (as fog), "studies show" (no source), Moreover/Furthermore/Additionally, "In conclusion", a second "not just X but Y", reflexive lists of three | "is" or "does", one concrete fact, a named source, or delete |
| H9 | Spoken fillers | um, uh, like, you know, basically, I mean, so yeah | A pause marked `/` in the script |

**Keep:**
- owned high-likelihood hedges followed by odds ("I'd bet 80%")
- conditions ("If you sell B2B…")
- ranges
- receptive language in replies and DMs ("I hear you. I'd still argue…")
- one "might be wrong" line for established experts

#### Strip list: VN

| Mã | Loại | Cắt hoặc gắn cờ | Thay bằng |
|---|---|---|---|
| V1 | Rào đón | có lẽ, có thể là, chắc là, hình như, dường như, thì phải, hay sao ấy, biết đâu, không chắc lắm nhưng | Bỏ. Nếu thật sự không chắc: điều kiện ("đúng nếu…"), tỉ lệ ("7/10 khách"), "nhiều khả năng", "mình cược là" |
| V2 | Giảm nhẹ | hơi hơi, khá là, tương đối, một chút, phần nào, cũng được, tạm | Bỏ |
| V3 | Ý kiến rỗng | mình nghĩ là, mình thấy là, cá nhân mình thấy, theo quan điểm cá nhân thì, em nghĩ là (đặt trước điều đã chắc) | Nói thẳng. Khi cần sở hữu quan điểm: "Mình tin…", "Mình cược…" |
| V4 | Từ đệm | kiểu như, kiểu là, kiểu kiểu, thực ra thì, thật ra là, nói chung là, về cơ bản thì, đại loại là, thì là mà, ý là, cái việc mà, ờ, ừm | Bỏ. Khi nói thì ngừng một nhịp |
| V5 | Xin phép, tự hạ | em xin phép chia sẻ, chỉ là, vài tips nho nhỏ, hy vọng có ích, không biết có đúng không, nói sai mọi người bỏ qua, góc nhìn nhỏ | Bỏ |
| V6 | Đuôi xin xác nhận | đúng không ạ?, phải không nè?, không biết mọi người thấy sao, có ai giống mình không? | Dấu chấm. Câu hỏi để ở CTA |
| V7 | Mùi AI | không chỉ… mà còn… (từ lần 2), đóng vai trò quan trọng/then chốt, trong bối cảnh/thời đại ngày nay, góp phần, mang lại giá trị, hãy cùng khám phá, hành trình, có thể nói, điều quan trọng cần lưu ý, tóm lại, chìa khóa, bứt phá, tỏa sáng, nâng tầm, chinh phục, vô cùng | Động từ cụ thể, con số, câu chuyện |
| V8 | Câu dài kiểu Tây | Câu trên 25 từ; chuỗi "mà", "trong đó", "nhằm" | Tách câu, mỗi câu một ý |
| V9 | Danh từ hóa | tiến hành thực hiện việc…, công tác…, việc đánh giá… | Động từ: "đánh giá" |

**Giữ lại:**
- tiểu từ tạo quan hệ (nhé, nha, đấy, ạ với khán giả lớn tuổi hoặc B2B)
- xưng hô đã chọn
- "không sao cả" trong câu ranh giới
- "mình cược là" / "nhiều khả năng" khi có tỉ lệ đi kèm

---

### 6. Borrowed-attractor detector (flex-only, freebie-only, résumé-only)

The founder named three borrowed attractors:

| Attractor | Type | What it is |
|---|---|---|
| Money | **Flex** | Income, cars, lifestyle |
| Resources | **Freebie** | Free stuff, giveaways, discounts |
| What you've done | **Résumé** | Years, client counts, logos |

Anyone can copy or outbid them. Visible status signals push would-be friends away (the status-signals paradox, Garcia 2019). Freebies attract freebie-seekers. Rule: **allowed as evidence or as a CTA, never as the reason to follow.**

#### Step 1. Scan the hook and lines 1–3 for triggers

| Type | EN triggers | VN triggers |
|---|---|---|
| Flex | $ / k / "6-/7-figure", "I made", "income report", Stripe/revenue screenshot, Lambo, Rolex, "from Bali", "laptop lifestyle", "quit my 9–5 and now", first class | thu nhập, kiếm được, doanh thu … tỷ, nghìn đô, xe sang, biệt thự, Bali, tự do tài chính, nghỉ việc văn phòng giờ… |
| Freebie / discount | free, FREE, "comment [WORD]", "DM me", "link in bio" as the hook, giveaway, "steal my", template, swipe file, "limited spots", "% off", "first 10" | miễn phí, tặng, free, "comment '…' để nhận", inbox/ib, giảm X%, ưu đãi, khuyến mãi, số lượng có hạn, 10 suất đầu tiên, quà tặng |
| Résumé | "X+ years of experience", "helped 1,000+", Fortune 500, "ex-[company]", "as seen on / featured in", certified, award-winning, #1, "leading expert" | hơn X năm kinh nghiệm, đã giúp / đồng hành cùng hơn X…, chuyên gia hàng đầu, từng làm tại, chứng chỉ quốc tế, được báo chí đưa tin, top 1 |

#### Step 2. Look for a "why" signal in lines 1–3

- **EN:** because, I refuse, I chose, I stopped, I never/always, it cost, I turned down, here's why
- **VN:** vì, mình chọn, mình bỏ, mình không bao giờ, mình luôn, cái giá, mình từ chối, lý do là
- Also counts: any Card §2, §4 or §6 keyword

#### Step 3. Removal test

Delete the money, the freebie or the credential. Does the post still have a reason to exist?

#### Classification

| Class | Condition | Effect |
|---|---|---|
| **X-only** | Trigger present, no why signal, and the removal test fails | Character & Polarity = 0, Authenticity capped at 1, verdict **FAIL** |
| **X-led** | Trigger in the hook, the why only appears at line 4 or later | Character & Polarity capped at 1. Fix: move the why up |
| **X-as-evidence** | The trigger supports a stance | OK |
| **X-as-CTA** | The freebie appears only in the CTA | OK |

#### Repair: "Flip it"

1. **Keep** the asset.
2. **Ask** what choice it reveals (ladder twice: "why does that matter?").
3. **Lead** with that choice or stance.
4. **Demote** the asset to proof (line 3) or to the CTA.

| Type | Before | Character-angle hook EN | VN |
|---|---|---|---|
| Flex | "I made $47k last month from Bali." | "I made [$X] last month. I still drive a 2014 Corolla. Here's why." / "I turned down [$Y] last month. That's the number worth explaining." | "Tháng trước mình kiếm [X]. Mình vẫn đi Corolla 2014. Đây là lý do." / "Tháng trước mình từ chối [Y]. Con số đó mới đáng kể." |
| Freebie | "Comment GUIDE for my free 30-page pricing guide!" | "I don't do free discovery calls. So everything I'd say on one is on this page. Comment GUIDE." / "This template exists because I refuse to [X]." | "Mình không tư vấn miễn phí. Nên mọi điều mình sẽ nói trong buổi đó, mình gom vào một trang. Comment 'GUIDE'." |
| Discount (VN service) | "Giảm 50% tuần này!" | "The last time I ran 50% off, I nearly closed. Here's what I do instead." | "Lần cuối spa mình giảm 50%, mình suýt đóng cửa. Giờ mình làm thế này." |
| Résumé | "15+ years, 200+ companies, Fortune 500." | "[N] clients in, here's what I'd unlearn first." / "6 years at [Big-4] taught me one thing I had to reject." | "Sau [N] khách hàng, đây là điều mình muốn quên đầu tiên." / "6 năm ở [Big-4] dạy mình một điều mình phải bỏ." |

---

### 7. Before and after examples (EN + VN)

Scores are listed as Signature, Value, Authority, Authenticity, Character & Polarity, in that order. `[brackets]` are user data to fill in, enforced by G2.

#### Example 1. Mai Phương, speaking coach (F1 stance, value told through the stance)

**Before (EN):**
> "Public speaking can be a daunting journey for many professionals. In today's fast-paced world, it's important to note that confidence plays a crucial role in delivering impactful presentations. Here are 5 tips that might help: practice regularly, use power poses, know your audience, maintain eye contact, believe in yourself. Remember, everyone's journey is unique! What tips would you add?"

**Before (VN):**
> "Thuyết trình trước đám đông có thể là một hành trình đầy thử thách. Trong thời đại ngày nay, có thể nói sự tự tin đóng vai trò vô cùng quan trọng. Dưới đây là 5 tips nho nhỏ hy vọng có ích: luyện tập thường xuyên, tạo dáng power pose, hiểu khán giả, giao tiếp bằng mắt, tin vào bản thân. Mỗi người một hành trình mà, đúng không ạ?"

**Before score:** 0 / 0 / 0 / 0 / 0 = **0/10**. Lint: 11 hits (EN), 9 hits (VN). Re-ideate.

**After (EN):**
> Confidence isn't volume.
> Most speaking advice tells quiet people to be louder. Power-pose. Fake it.
> It breaks at question one. You can't fake an answer.
> I taught power poses for 3 years. About a third of my clients quit by week four. They felt like frauds.
> Now we do one thing: rehearse out loud until it's boring. Twenty reps. In your car if you have to.
> Boring means ready.
> Want hype? Hire someone else. That's fine.
> Quiet people: what are you rehearsing this week?

**After (VN, mình–bạn):**
> Tự tin không nằm ở giọng to.
> Phần lớn lời khuyên thuyết trình bảo người hướng nội: nói to lên, đứng power pose, cứ giả vờ tự tin.
> Đến câu hỏi đầu tiên là lộ. Câu trả lời thì không giả vờ được.
> Mình từng dạy power pose suốt 3 năm. Gần một phần ba học viên bỏ ngang ở tuần thứ tư. Họ thấy mình đang diễn.
> Giờ lớp mình chỉ làm một việc: tập nói thành tiếng đến khi thấy chán. 20 lần. Không có phòng thì ngồi trong xe mà tập.
> Chán nghĩa là đã sẵn sàng.
> Bạn cần sự sôi động thì mình không phải người phù hợp. Không sao cả.
> Tuần này bạn đang tập cho bài nói nào?

**After score:** 2 / 2 / 2 / 2 / 2 = **10, EDGE**.

**What changed:**
- 5 ideas cut to 1.
- Hill #1 is the hook.
- The old view is refuted.
- The §9 flaw is used as proof.
- Car-studio quirk added.
- "Boring = ready" coined term used.
- A boundary added.

#### Example 2. Ops consultant for 10–50-person agencies (résumé-only plus freebie CTA)

**Card excerpt:**
- Extreme trait: allergic to meetings.
- Enemy: "the status meeting".
- Flaw: 6 years at a Big-4 firm writing decks nobody read.
- Client words: "he fixed it instead of telling us to".

**Before (EN):**
> "With 15+ years of experience and 200+ companies helped, including Fortune 500 clients, I'm a leading operations expert. Today I want to share some insights on operational efficiency. Streamlining processes is crucial in today's competitive landscape. DM me 'OPS' for a free consultation!"

**Before (VN):**
> "Với hơn 15 năm kinh nghiệm và đã đồng hành cùng hơn 200 doanh nghiệp, trong đó có các tập đoàn Fortune 500, tôi xin phép chia sẻ một vài góc nhìn về tối ưu vận hành. Có thể nói, chuẩn hóa quy trình đóng vai trò then chốt trong bối cảnh cạnh tranh hiện nay. Inbox 'OPS' để nhận tư vấn miễn phí ạ!"

**Before score:** Detector **résumé-only**, so **FAIL**. 0 / 0 / 0 / 0 / 0.

**After (EN):**
> Cancel your Monday status meeting. Nobody will miss it.
> I spent 6 years at a Big-4 firm writing 80-page decks. Most were never opened. That's where I learned meetings are where work goes to wait.
> Agencies I work with swap the meeting for a 5-line Friday update. Each person gets back about [X hours] a week. [PROOF NEEDED: client logs]
> If your team needs the meeting to feel managed, keep it. I'm not your guy.
> Want the hours back? The 5 lines are in the comments.

**After (VN, tôi–anh chị; admit first, then stand firm):**
> Tôi từng mất 6 năm viết slide 80 trang. Gần như không ai mở.
> Nên giờ tôi nói thẳng: bỏ cuộc họp giao ban sáng thứ Hai đi.
> Cuộc họp là nơi công việc ngồi chờ.
> Các agency tôi đồng hành thay nó bằng bản cập nhật 5 dòng chiều thứ Sáu. Mỗi người lấy lại khoảng [X giờ] một tuần. [CẦN SỐ LIỆU]
> Nếu đội anh chị cần cuộc họp để yên tâm, cứ giữ. Tôi không phải người phù hợp.
> Còn muốn lấy lại thời gian, mẫu 5 dòng tôi để ở bình luận.

**After score:** 2 / 2 / 2 / 2 / 2 = 10. G2 is on **HOLD** until `[X hours]` is filled.

**What changed:**
- The résumé is flipped into the cost of learning.
- The freebie is demoted to the CTA.
- The enemy is named.
- A boundary added.

#### Example 3. Chị Lan, spa business coach (VN-first; freebie and discount plus a guarantee claim)

**Card excerpt:**
- Extreme trait: obsessed with numbers.
- Enemy: "chạy khuyến mãi để giữ khách" (running discounts to keep clients).
- Flaw: ran 50% off for 2 years and nearly closed.
- Client words: "chị ấy nói thật, không vẽ".

**Before (VN):**
> "TẶNG MIỄN PHÍ bộ 30 kịch bản khuyến mãi giúp spa tăng 300% khách hàng! Comment 'SPA' để nhận ngay. Số lượng có hạn!"

**Before (EN):**
> "FREE: 30 promo scripts that will boost your spa bookings by 300%! Comment SPA now. Limited spots!"

**Before score:** Detector **freebie-only**, and G2 fails (the 300% guarantee). **FAIL**.

**After (VN, mình–các chị):**
> Khuyến mãi không giữ được khách. Nó chỉ giữ được người săn sale.
> Mình biết vì mình từng giảm giá 50% suốt 2 năm. Doanh thu tăng, lợi nhuận về gần 0. Suýt đóng cửa.
> Giờ mình chỉ nhìn một con số: bao nhiêu khách quay lại lần thứ 3 mà không cần giảm giá. Spa mình đang ở [X%].
> Nếu chị đang muốn tăng khách bằng giảm giá, nội dung của mình chắc không hợp. Không sao cả.
> Còn muốn đo con số đó, bảng tính mình dùng để ở bình luận. Comment "LẦN 3".

**After (EN):**
> Discounts don't keep clients. They keep bargain hunters.
> I ran 50% off for two years. Revenue went up. Profit went to almost zero. I nearly closed.
> Now I track one number: clients who come back a third time without a discount. My spa sits at [X%].
> If you want growth through discounts, my content isn't for you. That's fine.
> Want to track it? My spreadsheet is in the comments. Comment THIRD.

**After score:** 2 / 2 / 2 / 2 / 2 = 10. G2 HOLD on `[X%]`.

**What changed:**
- The guarantee is removed.
- The admit-first pattern is used.
- The enemy is named as a practice, not as competitors.
- The freebie becomes the CTA.

#### Example 4. Business coach for freelancers moving to retainers (flex-only, repaired as a flipped paycheck)

**Card excerpt:**
- Extreme trait: radical frugality.
- Enemy: income-screenshot marketing.
- Flaw: year-one Stripe screenshots led to a [22%] refund rate.
- Client words: "the only one who didn't show me his car".

**Before (EN):**
> "I made $47,000 last month working 4 hours a day from Bali. Want my secret? My 6-figure framework is finally open. Link in bio!"

**Before (VN):**
> "Tháng trước mình kiếm được 1,2 tỷ chỉ với 4 tiếng mỗi ngày, làm việc từ Bali. Muốn biết bí mật? Khóa 'Thu nhập 6 con số' đã mở. Link ở bio!"

**Before score:** Detector **flex-only**, so **FAIL**.

**After (EN):**
> I made [$47k] last month. I still drive a 2014 Corolla.
> Where it went: [40%] tax and savings. [20%] my team. A sleep coach. My parents' rent.
> In year one I posted income screenshots. I attracted shortcut-seekers. [22%] asked for refunds.
> So now I show where money goes, not how much comes in. It tells you what I'd do with your business.
> Retainers over launches. Boring over flashy.
> Want the Bali pitch? Follow someone else.

**After (VN; income figure omitted per VN note 9):**
> Tháng trước là tháng doanh thu tốt nhất của mình. Mình vẫn đi con Corolla đời 2014.
> Tiền đi đâu? [40%] thuế và tiết kiệm. [20%] cho đội ngũ. Một chuyên gia giấc ngủ. Tiền nhà cho bố mẹ.
> Năm đầu, mình đăng ảnh chụp doanh thu. Kéo về toàn người muốn đường tắt. [22%] đòi hoàn tiền.
> Nên giờ mình cho bạn xem tiền đi đâu, không phải tiền vào bao nhiêu. Nhìn đó là biết mình sẽ làm gì với việc kinh doanh của bạn.
> Hợp đồng dài hạn hơn là launch rầm rộ. Chắc chắn hơn là hào nhoáng.
> Bạn cần hình ảnh Bali thì có người khác hợp hơn mình.

**After score:** 2 / 2 / 2 / 2 / 2 = 10. G2 HOLD on brackets.

**What changed:**
- Money now shows values, not status.
- The year-one flaw supplies two-sided proof.
- A boundary added.

#### Example 5. Jake, fitness coach for desk-bound founders (AI-fog how-to, rebuilt as a stance)

**Card excerpt:**
- Extreme trait: monk-like discipline.
- Enemy: "fitness as punishment" and 6-week shreds.
- Contrarian truth: fewer decisions beat more motivation.
- Client words: "no guilt".

**Before (EN):**
> "Staying motivated to work out can be challenging, especially for busy entrepreneurs. Here are some strategies that may help: set SMART goals, find an accountability partner, and reward yourself. Remember, consistency is key, and every small step counts on your fitness journey!"

**Before (VN):**
> "Duy trì động lực tập luyện có thể là một thử thách, đặc biệt với các founder bận rộn. Dưới đây là một số chiến lược có thể giúp bạn: đặt mục tiêu SMART, tìm bạn đồng hành, tự thưởng cho bản thân. Hãy nhớ rằng kiên trì là chìa khóa, và mỗi bước nhỏ đều có ý nghĩa trên hành trình của bạn!"

**Before score:** 0 / 1 / 0 / 0 / 0 = **1/10**. Re-ideate with generator S3.

**After (EN):**
> You don't need more motivation. You need fewer decisions.
> By 6 p.m. you're out of decisions. A workout that needs one more gets skipped.
> So my clients decide once, on Sunday: same 3 days, same time, same 40-minute session. Nothing left for Tuesday-you to choose.
> I ran 6-week bootcamps for 3 years. 70% of clients were gone by month two. Motivation was the plan, and it ran out.
> Boring is the program. No guilt, no gaps.
> Want to be yelled at? I'm not your coach.
> What's one decision you can delete this week?

**After (VN, mình–bạn):**
> Bạn không thiếu động lực. Bạn có quá nhiều quyết định.
> 6 giờ chiều, đầu bạn đã cạn quyết định. Buổi tập nào còn cần quyết thêm sẽ bị bỏ.
> Nên học viên của mình chỉ quyết một lần, vào Chủ nhật: cố định 3 ngày, cố định giờ, cố định bài 40 phút. Thứ Ba không còn gì phải chọn.
> Mình từng chạy bootcamp 6 tuần suốt 3 năm. 70% học viên bỏ trước tháng thứ hai. Kế hoạch dựa vào động lực, mà động lực thì cạn.
> Nhàm chán chính là giáo án. Không áy náy, không đứt quãng.
> Bạn thích bị quát cho có lửa thì mình không phải HLV hợp với bạn.
> Tuần này bạn bỏ bớt được quyết định nào?

**After score:** 2 / 2 / 2 / 2 / 2 = 10.

**What changed:**
- Three generic tips replaced by one contrarian mechanism.
- The single allowed "You don't have X, you have Y".
- The 70% loss story gives two-sided proof.
- The signature words "boring is the program" and "no guilt" are used.
- A boundary added.

---

### Implementation notes

**Suggested pack files:**
- `character-core/interview.md` (A1 and the Buyer Mirror)
- `character-core/character-card.md` (A2)
- `ideation/character-formats.md` (A3)
- `ideation/polarity-and-stances.md` (A4 and the generator)
- `quality/edge-check-v2.md` (B5 and B6)
- `quality/examples.md` (B7)

**Time budget for the 1–2 h/week user:**
- The interview is a one-off 45–60 min.
- The Buyer Mirror is async.
- Edge Check runs automatically. The user only answers the "Needs you" prompts.

**Resonance metrics** to log in the Card:
- phrases the audience repeats back
- "this is me" replies
- sales-call answers to "why me"
- unfollows after a stance post, treated as a healthy filter

**Caveats:**
- These founder-supplied frameworks could not be verified on the open web and should be treated as practitioner material: Soo Wei Goh's "one extreme trait", "buyer mirror" and "flipped paycheck"; Nik Setting's quiet-truth lines; Matt Gray's exact "quietly intolerant" wording.
- The VN strip lists, xưng hô guidance and the link between power distance and certainty are editorial inferences, not tested in Vietnam.
- All example numbers are illustrative and must come from the user's own Proof Bank.