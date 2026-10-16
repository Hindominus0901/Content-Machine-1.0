# Message Focus Engine: design (EN + VN)

## 0. What it is, where it lives, what it changes

The engine turns "I know a lot" into ONE message. After that, the machine checks every piece against that message without asking the coach anything.

**Changes to arch-final-spec §2.2 and §5.1:**
- **Day-0 intake.** The 10-question intake and the Edge card go away. In their place: a brain-dump (talk, don't answer) → at most 6 questions, mostly pre-filled from the dump → a one-screen **Message Map** → **one decision ("OK")**.
- **The day's real decision.** It is no longer "pick 1 of 3 keywords". The machine pre-picks the keyword built from buyer words and shows the other two as alternates. Approving a sentence that sounds like you is easy; choosing between invented terms is not.
- **Character Core Q1–Q5.** These are covered by the dump: origin, what annoys them, stories and voice. The extreme trait is inferred. The deep Excavation stays optional homework.
- **Voice sample question.** The old "paste 2 things you wrote" is gone, because the dictated dump is the voice sample.

**Where it lives:**
- **`modules/message.md`** (new, ≤150 lines). It holds the dump sort, Focus Score, the 6 questions, the Map, NOT NOW, drift handling, and the re-plan and retire rules. The named method, Big Domino and B1–B7 move here, and the chain is now generated from the pillars. `signature.md` keeps only keyword mining and the registry.
- **`core/ship-check.md`** gets step 0, FOCUS (≤420 chars), and a WHY line in every footer.
- **Brand Brain.** The MESSAGE MAP becomes block 1 of the Brief and of the ChatGPT Task Brief.
- **Bank.** New row type **X (Parked)**.
- **Content database.** New properties **Pillar** (P1 | P2 | P3 | Off-map) and **Why**.
- **Install.** It needs nothing beyond a chat: no hub, connector, skill or automation in session 1. That supports the founder's "simplest possible setup". The hub and automations come in Session 2.

**How the founder's references map onto the engine:**

| Founder reference | Becomes |
|---|---|
| One core problem · Hormozi "narrow" · Nik "write for one person" | WHO = one person per Season; THEIR WORDS = one problem, quoted word for word |
| Signal framework (5 years ahead / what people come to you for unasked / what you're quietly intolerant of) | Q1 probe / Q2 / Q3 |
| Named method | METHOD (Q5); the machine names it |
| Enemy / old way | OLD WAY (Q3), given a name |
| 3 big ideas / hills (Matt Gray's authority pillars) | 3 PILLARS, each one a hill plus the belief it installs |
| Belief-shift chain | Generated from the pillars: P1 = B1–B2, P2 = B3–B4 (Big Domino), P3 = B5–B7 |
| Signature keywords + 4-3-2-1 "3 signature phrases" | Exactly 3 phrases: keyword (an audience word) · method name · old-way name |
| One extreme trait | The SAID WITH line |
| Buyer Mirror | Q1 and Q2 ask what the client actually said; Week-1 homework validates the keyword and P3 proof |
| Why-loop research | One "why" probe in Q2 + Quick Listen → the root cause becomes Pillar 1's belief |
| Nik: one idea / change one belief per post | FOCUS checks 2–3 |
| Domino series | Each Season week runs one pillar's dominoes; every piece links forward |
| Matt Gray 4-3-2-1 | 4 rungs · 3 phrases · 2 formats (weekly recording + native short) · 1 platform (+ email or Zalo) |

---

## 1. The conversation: brain-dump → ≤6 questions → ONE message

### 1.1 Conversation rules (in message.md)
1. **Talk first, choose second.** The machine proposes options taken from the dump (A/B/C plus a stated default). The coach picks or corrects.
2. **One question per message** in guided mode. At most 1 probe per question and 3 per session. A hedge gets a bet: "If you had to bet $100…" / "Nếu phải cược 1 triệu…".
3. **Never pre-fill words you didn't hear.** Q2 (their exact words) and Q4 (a result with a number) are always asked live, unless the dump already holds a verbatim quote and a number.
4. **"skip" always works.** The machine fills in a default and marks it "(my guess)" / "(mình đoán)" on the Map.
5. **VN xưng hô** is inferred from how the coach refers to themselves in the dump, then confirmed in the one-line defaults step.
6. **Speech-to-text.** Fix only obvious errors; confirm any unclear word.

### 1.2 Step 0: brain-dump (1–11 min)

**EN**
> Before any questions, empty your head. Tap the mic in the message box and talk for 5–10 minutes, in 2–3 chunks. Messy is perfect. Don't organize; that's my job. Talk about any of these:
> • what you teach or fix for people • what clients ask you again and again • 2–3 clients who changed (before → after) • what annoys you about how your industry does it • what you learned the hard way • what you sell today (or "nothing yet")
> Say "done" when you're empty.

**VN**
> Trước khi hỏi gì, bạn cứ "xả" hết những gì mình biết ra đã nhé. Bấm biểu tượng micro trong ô chat rồi nói 5–10 phút, chia 2–3 lần cũng được. Lộn xộn càng tốt, đừng sắp xếp, phần đó để mình lo. Gợi ý vài thứ để nói:
> • bạn đang dạy hoặc giúp người ta giải quyết chuyện gì • câu khách hỏi đi hỏi lại hoài • 2–3 người khách đã thay đổi: lúc đầu thế nào, giờ ra sao • điều bạn thấy ngứa mắt trong cách ngành mình đang làm • bài học bạn phải trả giá mới có • bạn đang bán gì (hoặc "chưa bán gì")
> Nói xong thì gõ "xong".

**Other ways to dump:**
- paste a transcript of any live, webinar or podcast (common for VN coaches);
- paste the last 10 posts;
- type 10 bullets.

**After each chunk:** "Got it. Keep going or say 'done'. You haven't mentioned {jogger}. Anything there?" / "Mình nhận rồi. Nói tiếp, hoặc gõ 'xong'. Bạn chưa kể về {gợi ý}, có gì kể thêm không?"

**What the machine extracts without showing it:**

| From the dump | Becomes |
|---|---|
| Topics | Knowledge Inventory, sorted into piles |
| Client groups | WHO candidates |
| Clients quoted second-hand | V-rows tagged `second-hand`, until the Buyer Mirror confirms them |
| Stories and results | S-rows and P-rows (Consent N, Substantiated N) |
| "Annoys me", "I'd never" | Enemy candidates and B-stances |
| How they talk | Voice Card: 5 verbatim phrases, register, dialect, VN xưng hô |
| Length, repetition and emotion per topic | ENERGY score |
| The transcript itself | **Pillar #0**: Week 1 is cut from it (≥70% the coach's own words) |

### 1.3 Inventory reply (addresses "afraid of diluting")

**EN:** "You know a lot. I counted {19} things you could teach, {6} client stories and {4} strong opinions. That isn't too much. It's about 6 months of content, if we say it in the right order. Now let's pick the ONE thing you'll be known for. Nothing gets thrown away; the rest gets parked on purpose."

**VN:** "Bạn biết nhiều thật. Mình đếm được {19} điều bạn dạy được, {6} câu chuyện khách hàng và {4} quan điểm rất rõ. Vậy không phải là nhiều quá đâu, đó là khoảng 6 tháng content, miễn mình nói đúng thứ tự. Giờ mình chọn ra MỘT điều bạn muốn người ta nhớ tới. Không bỏ gì cả, phần còn lại được cất để sau, có chủ đích."

### 1.4 Default flow: the pre-filled check (one screen)

> **EN:** "Here's what I heard. Say 'yes', or fix any line by its number. I'll only ask about the '?' lines.
> 1 Who: {A} · 2 Their words: ? · 3 Old way: {…} · 4 Best result: ? · 5 Your way: {3 steps} · 6 Offer: {…}"
>
> **VN:** "Đây là những gì mình nghe được. Đúng thì gõ 'ok', sai dòng nào thì sửa theo số. Mình chỉ hỏi thêm mấy dòng có dấu '?'.
> 1 Ai: {A} · 2 Lời của họ: ? · 3 Cách cũ: {…} · 4 Kết quả tốt nhất: ? · 5 Cách của bạn: {3 bước} · 6 Offer: {…}"

The usual pattern is 1 confirmation plus 2–3 questions asked live. Saying "one by one" / "từng câu" switches to guided mode.

### 1.5 The 6 questions (guided mode, and for every "?" line)

**Q1 · WHO (one person)**
- **EN:** "From what you said, you could help A) {…} B) {…} C) {…}. Which group already pays you, and would you happily work with 50 more of them? Pick one, then describe one real person from it: their job, roughly how old, and what was happening when they found you."
- **VN:** "Theo những gì bạn kể, bạn giúp được A) {…} B) {…} C) {…}. Nhóm nào đang trả tiền cho bạn, và bạn sẵn sàng làm với thêm 50 người như vậy nữa? Chọn một nhóm, rồi tả một người thật trong đó: làm nghề gì, khoảng bao nhiêu tuổi, lúc tìm tới bạn thì đang gặp chuyện gì."
- **Probe (Signal framework):** "Is that who you were 5 years ago?" / "Bạn của 5 năm trước có giống họ không?"
- **If skipped, or "all of them":** the group with the most evidence of paying.

**Q2 · THEIR #1 PROBLEM, IN THEIR WORDS**
- **EN:** "When that person first reached out, what did they say? Their exact words; messy is fine. I heard '{phrase}' in your story. Is that how they put it?"
- **VN:** "Lúc người đó nhắn bạn lần đầu, họ nói gì? Nguyên văn lời họ, lộn xộn cũng được. Mình nghe bạn kể có câu '{…}', họ nói đúng vậy không?"
- **Probe (the why-loop):** "Why do you think they stayed stuck with it so long?" / "Theo bạn, vì sao họ loay hoay với chuyện này lâu vậy?"
- **If skipped:** Quick Listen phrases tagged `[to confirm]`.

**Q3 · OLD WAY / ENEMY**
- **EN:** "What had they already tried that didn't work? And what does your industry keep telling them that you'd ban forever?"
- **VN:** "Trước khi gặp bạn, họ đã thử những cách nào mà không ăn thua? Và ngành mình hay khuyên họ điều gì mà bạn muốn cấm luôn?"
- **Probe:** "If that old way had a name, what would you call it?" / "Nếu đặt tên cho 'cách cũ' đó, bạn gọi nó là gì?"
- **If skipped:** the enemy candidate the coach spent longest on in the dump.

**Q4 · PROMISE + PROOF**
- **EN:** "Tell me your best result: where they started, what changed, where they are now, with a number or a timeframe. Then: what do most clients get, and how long does it usually take?"
- **VN:** "Kể ca bạn tự hào nhất: lúc đầu họ thế nào, điều gì thay đổi, giờ ra sao, có con số hay mốc thời gian càng tốt. Rồi: đa số khách đạt được gì, thường mất bao lâu?"
- **Probe:** "What exactly did they say when it worked?" / "Lúc thấy kết quả, họ nói nguyên văn câu gì?"
- **If skipped, or no clients yet:** the coach's own before → after, a promise framed as process, and the founding pilot.

**Q5 · YOUR WAY (named method)**
- **EN:** "Explain how you actually fix it, like you're telling a friend over coffee: first, then, then? I'll give it a name. (Already have one? Tell me.)"
- **VN:** "Kể cách bạn thật sự xử lý chuyện này, như đang nói với bạn thân ở quán cà phê: bước đầu làm gì, rồi gì, rồi gì? Mình sẽ đặt tên cho cách làm đó. (Có tên rồi thì nói luôn.)"
- **Probe:** "Which step does everyone else skip?" / "Bước nào người khác hay bỏ qua nhất?"
- **If skipped:** 3 steps drawn from the dump; the machine names them.

**Q6 · THE OFFER IT LEADS TO**
- **EN:** "What do you sell today: name, price, and how people buy (call, DM, link)? If nothing yet, say 'nothing yet' and I'll set up a simple first offer with you."
- **VN:** "Hiện bạn đang bán gì: tên, giá, và khách mua bằng cách nào (gọi, nhắn tin, link)? Nếu chưa có thì cứ nói 'chưa có', mình cùng bạn dựng một offer đầu tiên thật gọn."
- **Probe:** "What do people actually buy it for?" / "Khách mua thật ra là vì phần nào?"
- **If skipped, or nothing to sell:** Offer v0 (Dunford, about 5 minutes) → a "Founding 5" pilot.

**Fallback if the coach refuses to narrow** ("but I'll lose people"):
- **EN:** "You won't lose them. Everyone can still watch. We're choosing who it's FOR."
- **VN:** "Bạn không mất ai đâu. Ai cũng xem được. Mình chỉ chọn nội dung này viết CHO ai."

### 1.6 How the machine picks the ONE message (hidden)

**Candidates** are the 2–5 who × problem pairs found in the dump. Each is scored 0–2 on six criteria:

| Criterion | 2 | 1 | 0 |
|---|---|---|---|
| PAID | Already paid for this | Would plausibly pay | Free only |
| WORDS | Can quote them | Paraphrase only | None |
| PROOF | A result story with a number | A process story or own story | None |
| EDGE | Intolerant of the usual fix and has a different way | An opinion only | Generic |
| NARROW | Role + stage + moment | Role only | "Anyone" |
| ENERGY | Talked longest or most emotionally about it | Some | None |

**Picking rules:**
- The highest total wins. Ties go to PAID first, then NARROW.
- PAID = 0 for every candidate → run Offer v0.
- **Narrowing pass:** if NARROW < 2, the machine adds a stage and a moment from the dump ("niche until it scares you").
- **Root cause:** after Q2, Quick Listen runs (≤5 searches). A pattern counts only if it is seen in at least 2 places. The machine builds the why-chain pattern → why → why → root, and the root becomes Pillar 1's new belief. Without browsing, it uses the dump and tags the result `[verify in Week 1]`.
- **The coach sees one line only.** "Why this one: {4} people paid you for it, you can quote them, you have {Maria}'s story, and you lit up about {the Bali Fix}." The runner-up goes to NOT NOW as a Season-2 candidate.

---

## 2. The Message Map (one screen, about 20 lines)

### 2.1 Template (EN, with VN labels in brackets)
```
MY MESSAGE MAP · Season 1 · {dates} · v1                      [BẢN ĐỒ THÔNG ĐIỆP · Mùa 1]
ONE MESSAGE (one breath)                                       [MỘT THÔNG ĐIỆP (nói trong một hơi)]
 I help {one person} who "{their words}" {promise} with {Method}, instead of {old way}.
BIO LINE  {≤12 words} · DM "{KEYWORD}"                          [DÒNG BIO]
WHO        {role · stage · the moment they find you}            [AI]
THEIR WORDS "{V-1}" · "{V-2}"                                   [LỜI CỦA HỌ]
PROMISE    {X → Y in Z, as a range}                             [LỜI HỨA]
METHOD     {Name}: 1 … · 2 … · 3 …                              [PHƯƠNG PHÁP]
OLD WAY    "{name}": {what it does, why it fails}               [CÁCH CŨ]
OFFER      {name · price · how to buy} ← every piece walks here [OFFER]
KEYWORD    "{K-1}" (once in every piece) · SAID WITH: {extreme trait} [TỪ KHOÁ · CHẤT RIÊNG]
3 PILLARS = what they must believe before they buy             [3 TRỤ = điều họ phải tin trước khi mua]
 1 {hill}  "{old belief}" → "{new belief}"   proof {S-/P-ID | NEEDS}
 2 {hill}  "…" → "…"                          proof …
 3 {hill}  "…" → "…"                          proof …
NOT NOW (parked on purpose, not lost)                          [ĐỂ SAU (cất có chủ đích, không mất)]
 · {topic}: {reason} · back when {trigger}   (≤7 shown)
EVERY PIECE: 1 pillar · 1 idea · 1 belief · keyword · 1 next step [MỖI BÀI: 1 trụ · 1 ý · 1 niềm tin · từ khoá · 1 bước tiếp]
```

**Pocket version** (3 lines the coach can screenshot): the core message, the 3 pillar names, the keyword.

**Hidden from the coach** (stored in the Brain): the Big Domino sentence ("If they believe {P2 new belief}, every other objection goes away"), B1–B7, the Focus Scores and the root-cause chain.

### 2.2 Tests the core message must pass (the machine rewrites before showing)
1. **One breath:** ≤35 words EN, ≤50 âm tiết VN.
2. **Their words:** the problem part is a quoted V-phrase.
3. **Narrow:** it names a stage or moment, not only a role.
4. **Swap test:** it contains the method name or the old-way name, so a competitor couldn't post it unchanged.
5. **Money:** it ends at something sold, or at the founding pilot.
6. **Claims-safe:** the promise is a range or a condition. No guarantee. In VN, no nhất / duy nhất / cam kết.

### 2.3 Pillars are beliefs, not topics
There are exactly 3. A cold start may show 2, plus "proof pillar coming".

Each pillar is a **hill**: a stance of 6 words or fewer that passes the 3D test (a sensible peer could Disagree, you can Defend it, you can Demonstrate it). Each also carries old belief → new belief (their words where possible), its B-IDs and a proof ID or NEEDS.

| Pillar | Job | Chain beliefs | Main rungs |
|---|---|---|---|
| **P1 · The real problem** | "It's not my fault; the real cause is {root}" | B1, B2 | Admirable, Likable, Credible (reach) |
| **P2 · The better way** | "{Old way} fails because …; {Method} works". This is where the Big Domino lives | B3, B4 | Credible |
| **P3 · You can, now, with me** | Proof; "I can, even though {objection}"; "now beats someday" | B5, B6, B7 | Trustable (proof-gated) |

Character pieces are not a 4th pillar. They are how a pillar gets said: through the trait, a value or the enemy. Each still carries a P1–P3 tag.

### 2.4 NOT NOW parking (Bank type X)

**Reason codes:**

| Code | EN | VN |
|---|---|---|
| DIFF-BUYER | different buyer | khác người mua |
| DIFF-PROBLEM | different problem | khác vấn đề |
| NO-OFFER | nothing to sell for it yet | chưa có gì để bán cho nó |
| TOOL | a tool, not a message → "seasoning" | công cụ, không phải thông điệp → "gia vị" |
| GENERIC | anyone could say it | ai cũng nói được |
| RISKY | claims or credential risk | dễ dính claim sai, ngoài chuyên môn |
| TOO-EARLY | right person, later stage | đúng người, giai đoạn sau |

**Ways a parked topic can come back:**
- 3 or more buyer mentions in 30 days;
- the offer changes;
- a launch needs it;
- Season N;
- never (RISKY).

**Reassurance line, shown with the list:**
- **EN:** "Nothing you know is wasted. 'Parked' means later, on purpose. People remember you for what you say 50 times."
- **VN:** "Không có gì bạn biết bị bỏ phí. 'Để sau' là để sau có chủ đích. Người ta nhớ bạn vì điều bạn nói đi nói lại 50 lần."

### 2.5 How every future piece is checked: FOCUS = Ship Check step 0
```
0 FOCUS (before drafting): PILLAR P1/P2/P3 (character-led only if it carries the enemy, trait or a pillar belief)
· ONE-LINE idea ≤15 words (VN ≤20 âm tiết), else split → 2nd idea becomes an Idea row · ONE belief B-n "you think X → actually Y"
· their words (V) or keyword in hook / caption L1 · ONE next step from the ladder · topic not on NOT NOW
(else bridge to nearest pillar, or park as X-n) → print WHY line
```

**Drift handling** (coach asks for a topic that is off the Map). There are three outcomes, and the coach is never lectured:
1. **On-map:** proceed without comment.
2. **Bridgeable (the default):**
   - EN: "That fits your map if I angle it to Pillar 2: '{angle}'. Writing that version. Say 'as is' for the original."
   - VN: "Ý này vào được bản đồ nếu mình xoay về Trụ 2: '{góc}'. Mình viết bản đó nhé. Muốn giữ nguyên thì nói 'giữ nguyên'."
3. **Not bridgeable:**
   - EN: "Parked as X-9: {reason}. It comes back {trigger}. Want it anyway? It'll be your 1 off-map piece in these 10."
   - VN: "Mình cất ý này vào Để sau (X-9): {lý do}. Nó quay lại khi {điều kiện}. Bạn vẫn muốn đăng? Đây sẽ là bài ngoài bản đồ duy nhất trong 10 bài."
   - If the coach insists, the machine writes it, tags it **Off-map**, and counts it against the budget.

---

## 3. The "say it to get clients" bridge

### 3.1 The WHY line (top of every script, one line, plain words)
- **EN:** `WHY THIS GETS CLIENTS: shifts "{old belief, their words}" → "{new belief}" (Pillar 2) · next: comment {KEYWORD} → {asset} → DM: "{qualifying question}" → {offer}`
- **VN:** `VÌ SAO RA KHÁCH: đổi "{niềm tin cũ}" → "{niềm tin mới}" (Trụ 2) · bước tiếp: comment {TỪ KHOÁ} → {quà} → inbox hỏi: "{câu hỏi lọc}" → {offer}`

### 3.2 The four specifics (Ship Check auto-fix; this is how the coach says it specifically)
Every piece includes:
1. **One person** at stage level.
2. **One moment** they have lived (an R-row).
3. **One number or timeframe**, from a P-row or `[NEEDS]`. Never invented.
4. **Their words** (a V-row) or the keyword.

**Before and after:**
- **EN:** "Many women struggle with burnout and want more balance." → "It's 9:40pm. You're answering one more email and thinking: I can't do this for 15 more years."
- **VN:** "Nhiều chủ spa gặp khó khăn trong việc giữ chân khách hàng." → "Khách làm xong buổi 99k, cười rất tươi, rồi không bao giờ quay lại."

### 3.3 Minimal CTA ladder (3 steps for the coach; maps onto the 4-rung spec)

| Step | Used on | EN | VN |
|---|---|---|---|
| 0 Follow / send | P1 reach pieces (Admirable, Likable) | "Follow. Part 2 tomorrow: {next}." / "Send this to the friend who…" | "Follow để xem Phần 2: {…}" / "Gửi cho đứa bạn đang…" |
| 1 Comment KEYWORD → asset (**default**) | Credible (P1, P2) | "Comment EXIT and I'll send you {asset}." | "Comment 'QUAY LẠI', mình gửi {quà} qua inbox nha." |
| 2 DM / book | Trustable (P3, from Week 2, proof-gated; ≤1 a week on Lean, ≤2 on Standard) | "DM me EXIT if you want help building yours." | "Ai muốn mình xem giúp trường hợp của mình, inbox 'QUAY LẠI' nha." |

**Season rules:**
- **One keyword and one asset per Season.** The machine writes the asset itself from Q5: the method as a 1-page checklist or script. The coach builds nothing.
- **DM bridge:**
  - **M1** delivers the asset and asks ONE qualifying question built from the WHO stages, which sorts buyers from browsers.
  - **M2:** buyer stage → invite to a 15-minute call or the offer. Otherwise → "Part 2 is here", and the person stays in nurture.
  - VN path: inbox → Zalo.
- **Mix.** About 3 step-0, 3 step-1 and 1 step-2 per Lean week. A comment-keyword piece counts as a "give", so give-to-ask stays at 3:1 or more.

---

## 4. Anti-dilution rules (enforced automatically)

| # | Rule | Threshold | Enforced in |
|---|---|---|---|
| 1 | One person per Season | 2nd buyer only after 8 consistent weeks AND ≥3 clients from the first | Map lock; drift → park DIFF-BUYER |
| 2 | One idea per piece | One-line idea ≤15 words, written before drafting; two ideas → split | FOCUS |
| 3 | One belief per piece | B-ID required; "you think X → actually Y" | FOCUS, Edge V |
| 4 | Same 3 pillars all Season | Core message locked 90 days; pillars locked per Season; at re-plan a pillar's **angle** may change, its **belief** may not | `locks` in the Brain |
| 5 | Everything on-pillar | 100% of planned pieces carry P1–P3; ≤20% character-led; off-map only when the coach asks, ≤1 in 10 | BATCH, drift handler, REVIEW |
| 6 | Weekly focus | ≥60% of the week's pieces on that week's pillar (chain order W1 P1 → W2 P2 → W3 P3 → W4 all + offer); every pillar gets ≥3 exposures per 30 days in ≥2 formats | plan.md, BATCH |
| 7 | Three signature phrases only | Keyword once per piece in a rotating placement; method name in every Credible/Trustable piece and pillar recording; old-way name ≥1×/week; no new coined term mid-Season (new names → park) | Ship Check K, variation guard |
| 8 | One keyword CTA + one asset per Season | A 2nd asset only at re-plan | CTA kit |
| 9 | Parked topics are seasoning | May appear as ONE line inside an on-map piece, never as the hook or the main idea | FOCUS |
| 10 | Promotion (park → map) | Only at re-plan, and only if ≥3 buyer mentions in 30 days, the offer changed, or a launch needs it. It replaces a pillar's angle or becomes the next Season's candidate, **never a 4th pillar** | Monthly check |
| 11 | Retire | **Angle:** buyer signals <0.5× the other pillars for 4 weeks (belief kept, new angle). **Keyword:** ≥60 days with echo 0 while an alternative has ≥2 echoes. **Core message:** changes only at the quarterly re-map or an offer change. **Format:** existing 4-week rule | review.md, plan.md |
| 12 | New ≤20% | Weekly bets follow More/Better/New; "New" ideas must be on-map | REVIEW |
| 13 | One pillar per recording | The recording guide stays within one pillar; "park that" / "để sau" said mid-recording → an X-row | fmt-long.md, CUT |
| 14 | "Sick of saying it" counter | REVIEW shows times said vs estimated times heard, to stop premature changes | REVIEW |

The visible NOT NOW list is capped at 7 items; the rest are archived as X-rows.

---

## 5. How it plugs in, with zero added coach steps

### 5.1 First session, minute by minute (works on the lightest install: a Project with pasted instructions, any plan)

| Min | Coach | Machine |
|---|---|---|
| 0 | "Set up my Content Machine" / "Cài đặt Content Machine" | 3-line promise. EN: "1) Empty your head: talk 5–10 min. 2) I find the ONE thing you'll be known for and park the rest. 3) You film your first video today." VN: "1) Xả hết ra: nói 5–10 phút. 2) Mình tìm MỘT điều bạn nên được nhớ tới, phần còn lại cất để sau. 3) Bạn có ngay một video để quay hôm nay." |
| 1–11 | Brain-dump in 2–3 dictated chunks, or a pasted transcript | "Keep going" plus one jogger not yet covered |
| 11–12 | — | Inventory (3 lines) + pre-filled check (6 lines) |
| 12–18 | "yes / fix 3" + 2–3 live "?" questions | Quick Listen after Q2 (≤5 searches) → why-chain → P1 root |
| 18–20 | — | **Message Map** + pocket version |
| 20–21 | **The one decision: "OK", or change one line** | Saves the Map (Notion if connected; otherwise the top block of `MY-BRAND-BRAIN.md`, saved later) |
| 21–24 | **First win** | FILM TODAY: a P1 "Belief Bomb" short, Ship-Checked, with its WHY line |
| 24–27 | Confirms one defaults line: platform, hours, record day, delivery mode, xưng hô | — |
| 27–35 | Skims | Season 1 = 4 weeks on the 3 pillars; CTA kit (keyword, asset, M1/M2); **Week 1 cut from the dump** (pillar #0) |
| 35–40 | "later" or go | Hub + automations offered as **Session 2**. Exactly one NEXT line |

**Turn count.** About 9–11 coach turns, which fits free-tier caps. The film-ready piece still arrives by minute 25 or earlier.

### 5.2 Weekly loop: what the engine adds automatically

| Job | What the engine adds | Coach |
|---|---|---|
| **BATCH** (Mon) | Picks the week's pillar from the chain; ≥60% of slots on it; FOCUS + WHY on each piece; the recording guide covers one pillar in 4–6 segments and includes "say 'park that' if a new idea pops up" | 0 new steps |
| **CUT** | Scores transcript segments for pillar fit; off-map segments → X-rows or character slots; "park that" markers → X-rows (this tames rambling pillars) | 0 |
| **DROP** (weekdays) | The idea always comes from the Map. 1 in 5 capture questions asks "what did a client say this week?" → V-rows → keyword echo. "Add to my brain: idea X" gets a one-line verdict: on-map (Pillar n) or parked (reason) | 0 (answering is optional) |
| **REVIEW** (Fri) | Adds a FOCUS block to the scoreboard (example below) | 0 |

```
FOCUS  on-map 9/10 · P1 4 · P2 3 · P3 2 · "Quiet Exit" said 9× · heard back 2× (EXIT comments 14)
       new buyer words: "scared of the gap on my CV" (V-21) → P3 idea · parked +1: LinkedIn tips (DIFF-PROBLEM)
```

**ChatGPT (stateless).** The Map sits inside the Task Brief, and the week's pillar comes from date arithmetic (chain week → pillar).

### 5.3 Monthly re-plan, quarterly re-map, launches
- **"Plan next month", step 1: Message check (2 min, one decision).**
  - Per pillar: pieces, buyer signals (keyword comments + DMs + attributed calls) and the best piece.
  - Keyword echo; the top 3 new buyer phrases; parked items that hit the promotion trigger.
  - The recommendation defaults to **KEEP**. The alternatives are SHARPEN one line (suggested from new buyer phrases) or PROMOTE X-n into a pillar angle.
  - The new Season reruns B1–B7 on the same pillars with new angles and new proof.
  - On ChatGPT, the new `MY-BRAND-BRAIN.md` carries the Map at the top. This is the replacement already counted in the "≤2 upkeep actions a month".
- **Quarterly re-map.** The last 90 days of the Bank (captures, DMs, transcripts) are treated as a fresh brain-dump and re-scored. If the current message still wins, which is the usual case, it stays. If not, the machine proposes a new Map and asks only the questions whose answers changed.
- **Launches.** The launch's Big Domino is the P2 belief, and the launch's phase-2 belief posts are pillars 1–3. A launch never adds a pillar.

### 5.4 Schema and budget changes
- **`schemas/brand-brain.toml` → `[message]`:**
  - core, bio_line, pocket, who, their_words[V], promise;
  - method{name, steps[3]}, old_way{name, line}, offer_ref;
  - keyword (K-1), phrases[3], trait;
  - pillars[3]{name, old_belief, new_belief, b_ids, proof_ids, angle};
  - big_domino, not_now[X];
  - locks{message_until, pillars_until, keyword_until};
  - focus_scores (internal).
- **`schemas/banks.toml` → X (Parked):** topic · reason code · return trigger · mentions_30d · source (dump, drop, cut, request) · status (parked, seasoning, promoted, dropped).
- **`schemas/hub.toml`:** Content gets `Pillar` (select) and `Why` (text); the Sheets Lite tab gets the same two columns.
- **Budgets:**
  - Map block ≤1,200 characters EN / ≤1,400 VN.
  - Task Brief copy ≤900 / ≤1,050 (the parked list is reduced to names only).
  - The FOCUS line is about 420 characters and is added to the ChatGPT pasted instructions, which stay within 6,000.
  - ChatGPT anchor: `§CM-MESSAGE` in `CM-A-PLAN.md`.

### 5.5 Eval gates (add "knows-too-much" personas, EN + VN)
- ≤8 coach turns to reach the Map, and the Map passes all 6 tests.
- Over 4 simulated weeks of batches:
  - ≥90% of pieces on-map;
  - 0 NOT NOW items used as a hook or main idea;
  - WHY line in 100% of pieces;
  - the keyword exactly once in 100% of pieces;
  - the one-line idea ≤15 words in 100% of pieces.
- Human test: at least 2 of 3 non-technical testers (including at least 1 VN tester) can repeat their core message from memory the next day.

---

## 6. Worked examples

### 6.1 EN: Dana, a life coach who knows "too much"
Dana is 46, an ICF-certified coach and ex-HR director (18 years). She posts daily on Instagram and LinkedIn about everything. She has 2,300 followers and got 4 clients last year, all by referral.

**Brain-dump (excerpt, dictated):**
> "…I do life coaching but honestly it's everything: I'm certified in breathwork, I did Enneagram training, boundaries, confidence, relationships, career change, morning routines, I've been reading about perimenopause energy, I also fix people's LinkedIn profiles… my last four clients were all women in corporate, an HR manager, a finance director, 40-something, they're just done. One said 'I'm so tired of being tired', another said 'I can't just quit, I have a mortgage and two kids'… what drives me nuts is the self-care industry: take a bath, go to Bali, come back to the same 200 emails… I left HR in 2019 but I didn't just quit, I tested coaching for 9 months of weekends, I had a spreadsheet, people laugh, I make every client build one… Maria, a finance director, started weekend bookkeeping for small businesses, made $1,200 in 6 weeks, left in month 7… I sell 3-month 1:1 for $1,800, all referrals."

**Inventory:** 19 teachable things in 4 piles (career exit 7 · wellbeing tools 6 · relationships 4 · confidence 2), 6 stories, 4 strong opinions.

**Focus Score:**

| Candidate | PAID | WORDS | PROOF | EDGE | NARROW | ENERGY | Total |
|---|---|---|---|---|---|---|---|
| A · Corporate women in their 40s who want out | 2 | 2 | 2 | 2 | 2* | 2 | **12** |
| B · Women wanting confidence | 1 | 0 | 1 | 1 | 0 | 1 | 4 |
| C · Breathwork / nervous-system reset | 0 | 0 | 1 | 1 | 0 | 2 | 4 |

\*After the narrowing pass.

**Pre-filled check:** Dana answers "yes, fix 4" and supplies Maria's numbers and the typical range: a tested side offer in 8–12 weeks, an exit in 6–12 months, and some clients choose to stay with new boundaries.

**Message Map**
```
ONE MESSAGE  I help corporate women in their 40s who are "tired of being tired" but "can't just quit"
             build a Quiet Exit: test the next thing first, then leave with a runway. Not the Bali Fix.
BIO LINE     Helping corporate women in their 40s plan a Quiet Exit. DM "EXIT".
WHO          Finance/HR managers, 40–50, 15+ yrs in, kids + mortgage; finds me after a bad week ("cried in the parking garage")
THEIR WORDS  "I'm so tired of being tired" (V-1) · "I can't just quit, I have a mortgage" (V-2)
PROMISE      A tested next step in 8–12 weeks; most exit in 6–12 months (some stay, with boundaries)
METHOD       The Quiet Exit: 1 Stop the leak (contract hours, 2 wks) · 2 Test small (sell 1 thing to 3 people) · 3 Build the runway (number + date)
OLD WAY      "The Bali Fix": rest, retreat, return to the same inbox
OFFER        3-month 1:1, $1,800 ("The Quiet Exit in 90 days") · DM → 15-min call
KEYWORD      "Quiet Exit" (comment EXIT) · SAID WITH: spreadsheet-level practical (built her own exit sheet over 9 months)
PILLARS
 1 Not burnout, a dead end   "I need rest" → "I'm tired because there's no next step"          S-1 (her 2019 exit)
 2 Test before you jump      "I must quit to find out" → "I can test while I'm still paid"      P-1 Maria [NEEDS consent]
 3 A runway, not a leap      "I can't with a mortgage" → "With a number and a date, I can"      NEEDS (Buyer Mirror W1)
NOT NOW
 · Breathwork: TOOL → one line inside P1 pieces only   · Enneagram: DIFF-PROBLEM → back at 3+ buyer asks
 · Relationships: DIFF-BUYER → second offer, not before Season 3   · Perimenopause energy: RISKY → stays parked, refer out
 · Morning routines: GENERIC → only as a "my 6am spreadsheet" character piece
 · Confidence for 20-somethings: DIFF-BUYER → Season 3 candidate   · LinkedIn job tips: DIFF-PROBLEM (they want out, not a new corporate job)
```
**Hidden Big Domino:** "If they believe they can test their next thing while still paid, the fear of quitting stops being the objection."

**First 3 pieces:**
1. **FILM TODAY · native short · P1 · Admirable.** Title hook "Not burnout. A dead end." Verbal hook: "You're not tired because you work too hard. You're tired because there's no next step."
   `WHY: shifts "I need rest" → "I need a next step" · next: Follow, Part 2 "test your next job before you quit"`
2. **Carousel / LinkedIn post · P2 · Credible.** "The Quiet Exit: how I tested coaching for 9 months of weekends before leaving HR (3 steps)"
   `WHY: shifts "I must quit to find out" → "I can test while paid" · next: comment EXIT → 1-page Runway Sheet → DM "Still in the job, or already out?" → 3-month 1:1`
3. **Case story · P3 · Trustable (Week 2, proof-gated).** "Maria made $1,200 on weekends before she ever quit" [NEEDS: Maria's OK]
   `WHY: shifts "people like me can't" → "a finance director with 2 kids did" · next: DM EXIT → 15-min call`

### 6.2 VN: Chị Hạnh, a spa-business coach
Chị Hạnh is 38 and lives in Đà Nẵng. She owned 2 spas for 9 years and has coached spa owners for 2. She has 4,800 Facebook friends and 1,200 TikTok followers, and posts about everything.

**Brain-dump (excerpt, dictated):**
> "…chị làm spa 9 năm rồi, giờ coach cho chủ spa, mà nói thật chị biết nhiều thứ lắm: chạy quảng cáo Facebook, TikTok, máy móc công nghệ cao, kỹ thuật chăm sóc da, tuyển nhân viên, làm SOP, giấy phép, thiết kế phòng, thuê KOL… Học viên của chị đa số là chủ spa nhỏ, 1–2 cơ sở, 3–5 kỹ thuật viên, doanh thu cứ lẹt đẹt 150–200 triệu, bạn nào cũng than 'chạy khuyến mãi thì đông, ngưng là vắng', có bạn nói 'khách đến một lần rồi mất hút luôn'… Chị ghét nhất kiểu đồng giá 99k, cả con đường spa nào cũng 99k, đua nhau tới chết… Hồi 2018 chị giảm 50% gần 2 năm, suýt đóng cửa… Sau đó chị ghi sổ từng khách, phát hiện khách quay lại đủ 3 lần trong 2 tháng là gần như thành khách quen… Bạn Ngọc ở Huế học chị, bỏ 99k, làm theo, 8 tuần sau khách quen tăng gần gấp đôi… Chị đang bán khoá 6 tuần, nhóm 10 người, 6,9 triệu."

**Inventory** (the machine addresses her as "chị", inferred from the dump): "Chị biết nhiều thật: mình đếm được 21 điều chị dạy được, 5 câu chuyện học viên, 3 quan điểm rất rõ. Đó là khoảng 6 tháng content nếu nói đúng thứ tự."

**Focus Score:**

| Ứng viên | PAID | WORDS | PROOF | EDGE | NARROW | ENERGY | Tổng |
|---|---|---|---|---|---|---|---|
| A · Chủ spa nhỏ, khách không quay lại | 2 | 2 | 2 | 2 | 2 | 2 | **12** |
| B · Chủ spa muốn chạy quảng cáo FB/TikTok | 1 | 1 | 1 | 0 | 1 | 1 | 5 |
| C · Kỹ thuật chăm sóc da, máy móc | 0 | 0 | 1 | 1 | 1 | 1 | 4 |

C is also a different buyer: technicians, not spa owners.

**Pre-filled check:** chị Hạnh answers "ok, sửa 4" and adds the real numbers from Ngọc's spa (consent still pending). Defaults line: xưng hô "mình – chị em chủ spa", Facebook + TikTok + Zalo.

**Bản đồ thông điệp**
```
MỘT THÔNG ĐIỆP  Mình giúp chủ spa nhỏ đang "chạy khuyến mãi thì đông, ngưng là vắng" giữ khách quay lại
                mà không cần giảm giá, bằng Công thức 3 Lần Quay Lại, thay vì đua giá 99k.
DÒNG BIO        Giúp chủ spa nhỏ giữ khách quay lại, không giảm giá. Inbox "QUAY LẠI".
AI              Chủ spa 30–45 tuổi, 1–2 cơ sở, 3–5 kỹ thuật viên, doanh thu đứng ở 150–200 triệu/tháng, vừa chạy xong một đợt 99k thì vắng
LỜI CỦA HỌ      "Chạy khuyến mãi thì đông, ngưng là vắng" (V-1) · "Khách đến một lần rồi mất hút" (V-2)
LỜI HỨA         Khách quen tăng rõ sau 6–10 tuần, không giảm giá (kết quả tùy mỗi spa)
PHƯƠNG PHÁP     Công thức 3 Lần Quay Lại: 1 Nhắn Zalo trong 24 giờ kèm ảnh soi da · 2 Hẹn lịch ngay tại quầy · 3 Mời thẻ liệu trình đúng giá, tặng thêm buổi chứ không giảm
CÁCH CŨ         "Đua giá 99k": kéo được người săn sale, không giữ được khách
OFFER           Khoá "Spa Khách Quay Lại" · 6 tuần · nhóm 10 chủ spa · 6.900.000đ · inbox → Zalo → chuyển khoản
TỪ KHOÁ         "khách quay lại" (comment QUAY LẠI / QUAY LAI) · CHẤT RIÊNG: ám ảnh con số (ghi sổ từng khách suốt 9 năm)
3 TRỤ
 1 Khuyến mãi không giữ được khách  "Vắng là do thiếu quảng cáo" → "Vắng là do khách không có lý do quay lại"   S-1 (giảm 50% gần 2 năm, suýt đóng cửa)
 2 Ba lần là thành khách quen        "Muốn giữ khách phải giảm giá" → "Quay đủ 3 lần trong 60 ngày là thành khách quen"   P-1 spa của Ngọc [CẦN: số liệu + đồng ý]
 3 Spa nhỏ làm được, làm ngay        "Spa nhỏ phải có phần mềm, ngân sách" → "3 kỹ thuật viên, Zalo và cuốn sổ là đủ"   CẦN thêm 1 ca (Buyer Mirror tuần 1)
ĐỂ SAU
 · Chạy quảng cáo FB/TikTok: khác vấn đề (kéo khách mới) → sớm nhất Mùa 3, khi học viên đã giữ được khách
 · Kỹ thuật da, máy móc: khác người mua + dễ dính claim sai → để sau
 · Tuyển & giữ nhân viên: vấn đề kề bên ("nhân viên nghỉ là khách đi theo") → ứng viên Mùa 2 nếu ≥3 học viên hỏi
 · Giấy phép, pháp lý: chưa gắn offer → 1 bài hỏi-đáp khi mở bán
 · Thiết kế phòng: ai cũng nói được → chỉ làm "gia vị" trong bài Trụ 3
 · Thuê KOL: là một kiểu "cách cũ" → chỉ xuất hiện làm ví dụ trong Trụ 1
MỖI BÀI: 1 trụ · 1 ý · 1 niềm tin · từ khoá · 1 bước tiếp
```

**First 3 pieces:**
1. **QUAY HÔM NAY · TikTok/Reels "góc nhìn" · Trụ 1.** On-screen hook "Đông nhờ 99k, vắng cũng vì 99k". Verbal hook: "Chạy khuyến mãi thì đông, ngưng là vắng? Vì khách chưa có lý do quay lại."
   `VÌ SAO RA KHÁCH: đổi "vắng là do thiếu quảng cáo" → "vắng là do khách không có lý do quay lại" · bước tiếp: follow xem Phần 2 "3 lần là thành khách quen"`
2. **Bài FB "chia sẻ thật" · Trụ 2 · Credible.** "Mình ghi sổ từng khách suốt 9 năm. Khách quay lại đủ 3 lần trong 60 ngày gần như thành khách quen."
   `VÌ SAO RA KHÁCH: đổi "muốn giữ khách phải giảm giá" → "giữ khách bằng quy trình 3 lần" · bước tiếp: comment QUAY LẠI → kịch bản Zalo 7 ngày chăm khách sau buổi đầu → inbox hỏi "Spa chị đang có mấy kỹ thuật viên, khách quen chiếm khoảng bao nhiêu ạ?" → khoá 6 tuần`
3. **Case · Trụ 3 · Trustable (tuần 2, cần proof).** "Spa 4 kỹ thuật viên ở Huế bỏ đồng giá 99k: 8 tuần sau chuyện gì xảy ra" [CẦN: số liệu thật + chị Ngọc đồng ý; kèm "kết quả tùy mỗi spa"]
   `VÌ SAO RA KHÁCH: đổi "spa mình nhỏ, không làm được" → "spa 4 người đã làm được" · bước tiếp: inbox QUAY LẠI → workshop trên Zalo → khoá 6 tuần (giá công khai)`

---

### Critical Files for Implementation
None of these files exist yet; the repo only holds the placeholder `yeah`.
- /home/user/Content-Machine-1.0/modules/message.md (new): brain-dump prompt and sort, Focus Score, the 6 questions, Message Map, NOT NOW codes, drift handling, lock/promote/retire rules, and B1–B7 generated from the pillars.
- /home/user/Content-Machine-1.0/modules/setup.md, with /home/user/Content-Machine-1.0/strings/en.toml and /home/user/Content-Machine-1.0/strings/vn.toml: the new first-session order (dump → pre-filled check → Map → one decision → film today) and every EN/VN line above as keyed strings.
- /home/user/Content-Machine-1.0/core/ship-check.md: the step-0 FOCUS card, the WHY line in the footer, and the four-specifics auto-fix.
- /home/user/Content-Machine-1.0/schemas/brand-brain.toml, with /home/user/Content-Machine-1.0/schemas/banks.toml and /home/user/Content-Machine-1.0/schemas/hub.toml: the `[message]` block and its locks, Bank type X, and the Content `Pillar` and `Why` properties.
- /home/user/Content-Machine-1.0/modules/plan.md, with /home/user/Content-Machine-1.0/modules/review.md and /home/user/Content-Machine-1.0/modules/fmt-long.md: the pillar-per-week rhythm, the FOCUS scoreboard block, the monthly Message check, the quarterly re-map, and single-pillar recording guides with "park that" capture.