# Research brief: how Vietnamese coaches launch offers organically, run like a direct-response campaign (2025–2026)

**Labels.** **[DATA]** means a primary or official source: law text, platform policy or docs, or platform-reported numbers. **[DATA-2]** means data or policy reported by a secondary or vendor source; verify before you quote it in the product. **[PRACTITIONER]** means advice or patterns seen in practice, including the founder's examples. **[INFERENCE]** means my own reading of the evidence.

**Limits of this research.** The search tool only returns US results, and it indexes Vietnamese Facebook culture poorly. Searches for the exact slang ("chấm", "q.t", "UP", "hữu duyên", "đủ 100 comment") found almost no documentation. Those points rest on the founder's examples plus observed patterns, so they are marked [PRACTITIONER]. They should be checked against 5–10 live Vietnamese coach accounts before the module ships. Platform rules, laws and tool prices were checked against primary pages where those pages loaded.

---

## 1) Key insights

### A. Platform mechanics that decide how the launch must be built

1. **Meta formally demotes engagement bait.** [DATA] Meta defines it as posts that "explicitly request engagement (such as votes, shares, comments, tags, likes, or other reactions)" for purposes other than a specific call to action. The listed exceptions are finding missing people or property, raising money, petitions, showing support for an issue, and disaster information. Meta's 2017 announcement also exempts posts that ask for "help, advice, or recommendations". Pages that do this "systematically and repeatedly" get stronger, page-level demotion. Meta's Spam policy separately bans "selling, buying, or exchanging for engagement" and engaging "at very high frequencies".
   - [INFERENCE] "Comment 'UP' when we reach 100 comments" and "react ❤️ if…" fall inside the definition.
   - [INFERENCE] "Comment a keyword to get the PDF" is a grey area. It is a lead mechanism, but it still explicitly asks for comments.
   - [INFERENCE] Risk depends on how often you do it and whether the post has value on its own.

2. **Writing "c.m", "q.t" or "chấm" is a workaround, not a fix.** [PRACTITIONER] The founder's examples obfuscate the CTA ("c.m đầu tiên", "Chấm q.t").
   - [DATA-2] For TikTok, a 2026 secondary analysis says classifiers detect coded spellings and that bait is ineligible for the For You feed.
   - [DATA] Vietnam's Advertising Law requires Vietnamese wording in advertising products to be clear and accurate. LuatVietnam reads this as a 5–10M VND fine for individuals when slang or misspelling distorts meaning.
   - [INFERENCE] Obfuscation is a weak and slightly risky crutch. Changing the mechanism is the better fix (see F8).

3. **Comment-to-inbox automation works only on Pages, and only once per comment.** [DATA] Meta's Messenger policy allows "a single message as a reply" to a Page comment, sent within 7 days of the comment. Promotional messages are allowed inside the 24-hour window, which opens only when the person writes back. Outside the window you need message tags, sponsored messages or one-time notifications.
   - [DATA-2] Personal profiles and Groups cannot be automated through the official API.
   - **Design rule:** the first private reply must deliver the lead magnet and ask an easy question, so the person replies and opens the 24-hour window.

4. **You cannot retarget engagement on a personal profile.** [DATA] Meta's Marketing API lists engagement custom-audience sources: Pages (up to 730 days), Instagram business profiles (730 days), lead forms (90 days), Instant Experiences and so on. Personal profiles are not a source.
   - [INFERENCE] Vietnamese coaches who launch only from their personal profile cannot build retargeting audiences from the people who commented. Every launch therefore needs a "mirror" on a Page or Instagram account: the same posts, Reels and lives posted there too, plus a pixel on the landing or form page, so the retargeting phase has audiences to work with.

5. **Link posting on Pages and professional-mode profiles is now paywalled (Sept 2026).** [DATA]
   - Meta tested a limit of 2 organic link posts per month for Pages and professional-mode profiles without Meta Verified (TechCrunch, Dec 2025).
   - Meta One, launched 15 Sep 2026, sells "links in organic posts and reels" in higher tiers (Essential from $14.99, Advanced from $49.99, Expert from $149, Max from $499).
   - [DATA-2] In the Sept 2026 version, links in Page comments also count toward the quota.
   - [INFERENCE] The VN habit of "link ở comment đầu" (link in the first comment) gets expensive on Pages. Sending links in DMs or Zalo, or linking from ads, becomes the default. Plain personal profiles (not professional mode) are outside the reported test.

6. **Text-on-background hook posts.** [DATA-2] Coloured backgrounds only work on text-only posts of 130 characters or less; longer text drops the background.
   - [PRACTITIONER] Vietnamese coaches use them as scroll-stopping "mồi" (bait) hooks.
   - No evidence was found that backgrounds themselves increase reach. Treat any reach effect as a hypothesis to A/B test.

7. **TikTok works differently.** [DATA-2] TikTok Business Messaging supports keyword auto-replies, and each auto-reply is reviewed by TikTok. Pancake/Botcake is described as an official TikTok Business Messaging partner, and comment-to-DM tools on the official API exist for Southeast Asia (e.g., Tuku). TikTok Shop live rules ban showing QR codes or redirecting viewers off-platform. Engagement bait loses For You eligibility.
   - [PRACTITIONER] Vietnamese creators route TikTok viewers through "link/nhóm Zalo ở bio" (link or Zalo group in the bio) or a DM keyword.

8. **Messaging is the Vietnamese checkout.** [DATA] From a Decision Lab × Meta study (June 2024):
   - 83% of businesses in Vietnam say click-to-message ads bring high-quality leads.
   - 45% of consumers message businesses to buy.
   - 43% message businesses on Messenger weekly.
   - 60% prefer Messenger to finalise orders.

   [DATA] Reach, late 2025 (DataReportal 2026): Facebook ad reach 79.0M; TikTok 76.1M adults; Zalo 78.3M MAU; Messenger 57.8M; Instagram only 11.7M. VNG reports Zalo at 79.2M MAU in Q3 2025.
   - [INFERENCE] Facebook plus Zalo is the core launch stack. TikTok is for top of funnel. Instagram is secondary in VN; weight it more in the English edition.

9. **Zalo limits shape the nurture design.** [DATA-2]
   - Normal Zalo groups hold up to 200 members. A verified admin can create or upgrade to a community of up to 1,000 (an upgrade cannot be reversed).
   - Zalo OA paid plans run from 1 Jun 2026. Standard: 1,000,000đ/year, 5 staff accounts. Growth: 2,500,000đ/year, 500 out-of-window consult messages per month, 10 chatbot scripts. Comprehensive: 6,000,000đ/year, 2,000 messages, 50 scripts. Growth and Comprehensive include 4 free broadcasts per month.
   - Consult messages outside the package cost 55đ each. Group-chat maintenance costs 25,000–300,000đ/month.
   - ZNS template messages cost about 200–300đ each, plus CTA-button fees.
   - Personal "Zalo Business" tiers (May 2026): Standard 2,800đ/day (60 messages to strangers per month), Pro 5,500đ/day (120), Elite 55,000đ/day (2,000).
   - [INFERENCE] A "200-person free mini-course" is an honest scarcity number because it matches the Zalo normal-group limit.

### B. Vietnamese practice and trust

10. **The launch grammar.** [PRACTITIONER] This comes from the founder's examples and observed patterns.
    - The bait post promises a freebie ("không bán, chỉ tặng" = not selling, just giving) with a slot cap ("99/50 slot") and a low-effort CTA ("chấm", "c.m", "ib", "UP").
    - A comment threshold ("đủ 100 comment") unlocks a case-study series.
    - The offer post opens with "dành cho ai" (who it's for), gives three punchy promises and a price, and uses campaign hashtags (#makeitlaunch, #comingsoon).
    - Exclusivity and soft scarcity come from "hữu duyên" ("for those fated to see this").
    - Revenue case studies use full VND figures ("571.000.000").
    - Delivery happens in Messenger or a Zalo group, with a free workshop or livestream as the launch event.
    - [DATA-2] "Chấm" also has a functional meaning: leaving "." to follow a post's notifications.

11. **Trust is fragile around "lùa gà" ("herding chickens", i.e. luring the gullible).** [DATA-2] National press keeps exposing course scams:
    - Dân Trí (Dec 2024) lists red flags: guaranteed high returns, flaunting luxury, "free" funnels into expensive courses, unverifiable credentials. It cites the Mr Pips case.
    - CAND (Mar 2024) describes: free or cheap classes on Facebook, TikTok and Zalo; a 500k → full-fee → "premium group" upsell ladder; bought fake engagement; inflated revenue screenshots; "3 tháng đổi xe, 6 tháng đổi nhà" (new car in 3 months, new house in 6).
    - 24h (30 Sep 2026) mocks people who show income and sell courses with "xin vía" ("pass me your luck") comments and "like and share to get free clips".

    [INFERENCE] The founder's own tactics (income figures, slot caps, comment gates) look exactly like what the public now associates with scams. The module has to pair every such tactic with proof, context and honesty signals, or it will hurt the user's brand.

12. **Seeding.** [DATA-2] Vietnamese marketers call clone-account seeding (fake comments and reviews) "con dao hai lưỡi" (a double-edged knife): once detected, trust collapses.
    - [DATA] Decree 147/2024 (effective 25 Dec 2024) requires social accounts to be phone-verified before they can post or comment. Accounts that livestream to sell must verify with a personal ID number.
    - [INFERENCE] Fake seeding is now riskier and traceable. The module should support only real seeding: students, partners, the coach's own explanatory comments.

13. **Typical launch length.**
    - [DATA-2] Jeff Walker's Product Launch Formula (PLF) spreads pre-launch content over about 7–10 days, then opens the cart for a short window with daily emails for 3–7 days.
    - [PRACTITIONER, vendor claim] Learnybox advises pre-launch at least 14 days before cart open and a 5-day cart, and claims about half of sales come on the last day.
    - [PRACTITIONER] VN organic launches commonly run 2–4 weeks of visible campaign. Recommended default: **21 days** (14 days to warm up the audience, a 5–7-day open cart, then close). Also offer a **10-day sprint**.

14. **Workshop and webinar show-up.** [DATA-2] B2B benchmarks put registrant-to-attendee conversion around 40–60% (Hubilo and ON24, secondary). No Vietnamese B2C benchmark was found. [PRACTITIONER] Free VN workshops usually rely on Zalo-group reminders and a 24–48-hour replay. The module should track show-up rather than assume it.

### C. Legal constraints in Vietnam (late 2026)

15. **The amended Advertising Law 75/2025/QH15 has applied since 1 Jan 2026.** [DATA]
    - Article 15a covers "người chuyển tải sản phẩm quảng cáo" (KOLs, KOCs and other people who carry ads). They must verify the advertiser and its documents. If they have not used or do not understand the product, they may not promote it. They must announce that it is an ad "ngay trước và trong khi" (immediately before and during) the promotion.
    - Platforms must remove violating ads within 24 hours.
    - Decree 342/2025 details the law (effective 15 Feb 2026).
    - Decree 87/2026 sets the penalties (effective 15 May 2026). It replaces Decree 38/2021, with a maximum of **100M VND per violation for individuals and 200M VND for organisations**.
    - [DATA-2] Typical ad labels are "Quảng cáo", "Được tài trợ", "#Ad" and "#Sponsored".
    - [INFERENCE] A coach promoting their own course is the advertiser. Affiliates, students or partners who promote it are "người chuyển tải" and must disclose. Self-promotion still has to be truthful and must not mislead.

16. **Superlatives and misleading claims.** [DATA]
    - Using "nhất", "duy nhất", "tốt nhất" or "số một" (best, only, number one) requires legal proof: a market survey by a licensed research organisation, or a certificate from a national, regional or international award. This is defined in Circular 12/2026/TT-BVHTTDL, effective 5 Jul 2026.
    - [DATA-2] The fine for using superlatives without proof is reported at 10–20M VND. Under the old Decree 38/2021, misleading ads about "khả năng kinh doanh" (business capability) cost 60–80M VND for individuals. Re-check both amounts against Decree 87/2026.
    - [INFERENCE] Revenue case studies ("571 triệu sau 1 tuần") and promises like "mở bán trong 21 ngày" (launch in 21 days) need proof, context and a "kết quả cá nhân, không phải cam kết" (personal result, not a guarantee) framing.

17. **Promotion rules for bonuses and discounts.** [DATA]
    - Gift value per unit is capped at 50% of the pre-promotion price. Discounts are capped at 50%, except in government "concentrated" promotion programmes (effective 1 Jul 2025).
    - Decree 239/2026 (effective 26 Jun 2026) removed the 120-day annual cap on discount promotions and eased notification. KPMG says notification is now needed only for prize contests worth 100M VND or more.
    - [INFERENCE] A bonus worth 2,000,000đ on a 4,900,000đ course is about 41%, which is fine. "Tặng kèm" (free bonuses) worth more than the price would break the cap.

18. **Personal data.** [DATA] Personal Data Protection Law 91/2025/QH15 (effective 1 Jan 2026) requires data to be collected for a specific, clear purpose, with consent and notice. Fines for general violations are reported up to 3 billion VND, with higher revenue-based ceilings for some offences (verify).
    - [INFERENCE] Collecting phone numbers or Zalo contacts through comments or DMs needs a one-line purpose and consent statement. Never ask people to post phone numbers publicly.

19. **Ad-platform claims.** [DATA-2] Meta's ad standards ban unrealistic economic or health outcomes and get-rich-quick claims. Secondary 2026 guidance adds: no income screenshots in ads, and no "comment X / type Y" bait inside ads. Retargeting ads must therefore be milder than the organic posts: use the "Send message" button, not "comment 'UP'".

### D. Automation tools: prices and limits

| Tool | What it does in a launch | Price and limits | Label |
|---|---|---|---|
| **Meta Business Suite** (native) | Page comment → private message; custom keywords | Free. Reported limits: up to 5 keywords, sends after about 15 minutes unless you reply first, desktop only. One private reply per comment, within 7 days | DATA-2 |
| **Botcake** (Pancake ecosystem) | Comment auto-reply plus private reply, flows, broadcast; Messenger, IG, WhatsApp, TikTok, Zalo and more | Starter is free for up to **500,000** automated messages/month (auto-replies within 24h). Pro "starting at $30/3m messages"; broadcasts billed per platform | DATA (botcake.io/pricing) |
| **Fchat** | Comment and inbox scripts, sequences, Zalo OA, broadcast | Free: 2 pages, 1,000 contacts. Livechat 99,000đ/month. Chatbot 299,000đ/month (5,000 contacts). Business 999,000đ/month (10,000 contacts). Add-ons: +20k per page or staff member, +100k per 5,000 contacts | DATA (fchat.vn/price) |
| **Pancake** (pages.fm) | Unified inbox; auto-hide comments (e.g., ones containing phone numbers); comment-to-inbox; livestream | Prices conflict across sources (old 2022 tables show a Mini plan around 550k). Verify on pancake.vn | DATA-2 (stale) |
| **HaraSocial** (Haravan) | Facebook, IG, Zalo, Shopee inbox; auto-hide and reply; livestream orders | 14-day trial; price only on request. A third party cites about 300–800k/month (unverified) | DATA-2 |
| **ManyChat** | Better for IG (EN edition) | Pro reportedly from $15/month for 500 contacts, scaling with contacts; AI add-on about $29/month. The site returned 403, so verify | DATA-2 |
| **Zalo OA / ZNS / zBusiness** | Nurture and reminders | See insight 9 | DATA / DATA-2 |

---

## 2) Frameworks and templates

The same example coach is used throughout:

> **Coach Linh** coaches presentation skills for office workers.
> - **Offer:** "Nói Có Lực" ("Speak with Power"), a 6-week cohort.
> - **Price:** 4,900,000đ until two days before close, then 5,900,000đ.
> - **Capacity:** 30 seats, a real limit because she gives weekly 1:1 feedback.
> - **Lead magnet:** "7 câu mở đầu thuyết trình" (7 opening lines for presentations).
> - **Mini-course:** 3 nights in a Zalo group (200 people).
> - **Launch event:** a free Zoom workshop, simulcast to Facebook.

### F1. The organic DR launch arc (8 phases)
- **Source:** founder brief + Jeff Walker's PLF + [PRACTITIONER] Vietnamese patterns.
- **How it works:** each phase has one job and one metric. Every post sends people forward to the next step (DM, Zalo, workshop, cart).

| Phase | Job | Primary metric |
|---|---|---|
| 1. Mồi + lead magnet | Turn readers into conversations or Zalo members | Lead conversations started |
| 2. Belief shift | Break the belief that blocks the purchase | Saves and quality comments |
| 3. Value | Prove competence by giving real value | Saves and shares |
| 4. Educate / case study | Show the mechanism and proof | Series read-through, workshop sign-ups |
| 5. Open cart (DR) | Make the offer | DM enquiries, sales |
| 6. Retarget | Reach warm people again | Cost per conversation, sales |
| 7. Urgency and scarcity | Turn "later" into "now" with real constraints | Last-48h sales |
| 8. Close and post-launch | Keep trust, build the waitlist | Waitlist size, NPS |

**Fill-in template:**
`Offer [name] for [who] → result [specific + conditions] → real constraint [capacity/date/bonus] → lead magnet [x] → event [workshop/live, date] → cart [open–close] → channels [profile/Page/Group/TikTok/Zalo] → proof assets [with consent]`

**Worked example:** "Nói Có Lực" for office workers who freeze in meetings. The result: a clear 3-minute structured talk and chairing one meeting by week 6, if they practise 20 min/day. 30 seats. Lead magnet: "7 câu mở đầu". Workshop: Thursday 20:00. Cart: Friday to the following Thursday, 23:59. Channels: profile plus a Page mirror plus a Zalo group. Proof: 3 students with written consent.

### F2. PLF's sideways sales letter, mapped to Vietnamese Facebook
- **Source:** Jeff Walker via systeme.io [DATA-2].
- **How it works:** four pre-launch content pieces (PLC1 Opportunity, PLC2 Transformation, PLC3 Ownership, then the sales piece) run before a short open cart. In VN, they become posts, a mini-course in Zalo, and a live.
- **Fill-in template:**
  - PLC1 = "Cơ hội: [điều mới có thể] vì [cơ chế]" (Opportunity: what is now possible, and why)
  - PLC2 = "Chuyển hóa: [case study có bối cảnh]" (Transformation: a case study with context)
  - PLC3 = "Làm thử: [bài tập/khung] + vấn đề tiếp theo" (Ownership: try it yourself, then the next problem)
  - Then "Mở đăng ký" (registration opens)
- **Worked example:**
  - PLC1: "Nói hay là kỹ năng có cấu trúc" (speaking well is a structured skill).
  - PLC2: Ms M.'s 6 weeks.
  - PLC3: the 3-2-1 exercise. The new problem it reveals: "tự tập không có ai sửa" (practising alone, nobody corrects you).
  - Sales: the open-cart post plus a live Q&A.

### F3. The three-stage launch (Invitation → Experience → Amplification)
- **Source:** Brandcamp, by Mai Thị Ánh Tuyết, Logitech VN [PRACTITIONER, VN brand-manager view].
- **How it works:**
  - **Invitation:** create curiosity.
  - **Experience:** let people try it (workshop, mini-course).
  - **Amplification:** spread the experience (student posts, recaps, retargeting). Without amplification, only the attendees ever hear about it.
- **Fill-in template:** `Teaser [3 posts] → Experience [event] → Amplify [recap + UGC + ads to viewers]`
- **Worked example:** teaser BG posts, then the Zoom workshop, then a recap carousel, student shares (labelled), and ads to people who watched 75% of the live.

### F4. The Mồi → Inbox → Zalo ladder (moving commenters to inbox)
- **Source:** Meta Messenger policy [DATA] + [PRACTITIONER] Vietnamese flows.
- **How it works:** four routes, depending on the channel.
  - **Route A (Page, automated):**
    1. A keyword comment or DM keyword triggers the bot.
    2. The bot posts a public reply (vary the wording) and sends one private reply. That reply must contain the deliverable plus a quick question or button.
    3. The person replies, which opens the 24-hour window.
    4. Ask for a Zalo or phone number with consent.
    5. They land in the Zalo group or OA.
  - **Route B (personal profile, manual or a VA):**
    - Prefer "nhắn cho mình chữ X" (message me the word X), so the person starts the chat.
    - If you take comments, the VA replies publicly ("Mình nhắn bạn rồi nha, check tin nhắn chờ nhé" = I've messaged you, check your message requests) and sends DMs by hand.
    - Avoid bulk-DM tools, which are a spam risk.
  - **Route C (TikTok):** a keyword DM auto-reply (reviewed by TikTok), an official-API comment-to-DM tool, or a link or Zalo group in the bio.
  - **Route D (Zalo):** form → group of up to 200 (or a community of up to 1,000) → OA for broadcasts and ZNS reminders (template plus phone number plus consent).
- **Fill-in template (first private reply):**
  `Chào [tên], đây là [tài liệu] như đã hứa 👉 [link]. Để mình gửi thêm [bài tập/nhắc lịch workshop] cho đúng, bạn cho mình biết: bạn đang kẹt nhất ở [A] hay [B]? (Mình chỉ dùng thông tin này để gửi tài liệu và nhắc lịch, muốn dừng nhắn "DỪNG".)`
  (Translation: Hi [name], here is [resource] as promised. To send the right extra exercise or workshop reminder, tell me: are you most stuck on A or B? I only use this to send resources and reminders; reply "DỪNG" (STOP) to opt out.)
- **Worked example:** "Chào Lan, đây là file 7 câu mở đầu 👉 [link]. Bạn hay run nhất lúc *mở đầu* hay lúc *bị hỏi bất ngờ*? Mình gửi thêm 1 bài tập đúng chỗ đó." (Are you most nervous at the opening or when asked something unexpected? I'll send an exercise for that.)

### F5. The case-study unlock series (with a Proof–Context–Disclaimer rule)
- **Source:** founder example ("Đủ 100 comment 'UP'… casestudy 571.000.000") + Advertising Law and Meta ad standards [DATA].
- **How it works:**
  - Announce a 5-part series with fixed publish times. Prefer a date over a comment threshold. If you keep a threshold, publish anyway.
  - The five parts: starting point → bottleneck → mechanism → result → lessons and invitation.
  - Every number needs context: list size, years of audience building, ad spend, price, buyer count, refunds, team. Add consent and "kết quả cá nhân" (individual result).
- **Fill-in template:** `[Con số] sau [thời gian] — bối cảnh: [tệp], [chi phí], [giá], [số người mua], [đội ngũ]. Đây là kết quả của [ai], không phải cam kết. Kỳ [n]/5 lúc [giờ].` ([Number] after [time] — context: [audience], [cost], [price], [buyers], [team]. This is [who]'s result, not a promise. Part [n]/5 at [time].)
- **Worked example:** "6 tuần của chị M.: từ run tay đến chủ trì họp quý. Chị tập 20 phút/ngày, 4 buổi sửa 1:1. Kết quả của chị, không phải cam kết cho mọi người. Kỳ 1/5 lúc 20h tối nay." (Ms M.'s 6 weeks, from shaking hands to chairing the quarterly meeting. She practised 20 min/day with 4 1:1 sessions. Her result, not a promise. Part 1/5 tonight at 20:00.)

### F6. Honest scarcity ledger
- **Source:** Vietnamese promotion rules [DATA] + consumer and advertising law [DATA] + [INFERENCE].
- **How it works:** every scarcity claim must map to a real constraint and be updated publicly.
  - Allowed constraints: capacity (with the reason), cohort start date, bonus deadline, price step, Zoom room or Zalo group size.
  - Not allowed: fake counters, "giá chỉ hôm nay" (today-only price) repeated every day, reopening right after close with no change.
  - Gifts must stay within 50% of the price.
- **Fill-in template:** `Ràng buộc: [loại] | Lý do thật: [x] | Con số: [n] | Cập nhật lúc: [giờ] | Sau hạn: [điều gì xảy ra]` (Constraint | real reason | number | updated at | what happens after the deadline)
- **Worked example:**
  - Capacity: 30 seats, because of weekly 1:1 feedback. Updated at 12:00 and 20:00.
  - Bonus: a 30-minute 1:1 (valued at 2,000,000đ, about 41% of the price) until Wednesday 23:59.
  - After close: next cohort expected in [month], with a waitlist.

### F7. The retargeting ladder (via a Page or Instagram mirror)
- **Source:** Meta Marketing API engagement audiences [DATA] + Decision Lab click-to-message data [DATA] + [PRACTITIONER].
- **How it works:** mirror launch content on the Page or IG. Build the audiences, exclude buyers, and run click-to-Messenger or click-to-Zalo ads with mild copy that stays within ad policy.

| Audience | Window | Message |
|---|---|---|
| Watched 75% of workshop or live | 30 days | Recap + offer + deadline |
| Video viewers, 50% | 60–365 days | Belief shift + invitation to the event |
| Page/IG engagers | Up to 730 days | Testimonial |
| Messaged the Page | 30–90 days | FAQ / objection |
| Lead form or pixel (landing page) | 90 days | Bonus deadline |

  Exclude: a buyer list (uploaded only with consent).
- **Fill-in template:** `Audience [x] → Hook nhắc lại điều họ đã xem → 1 lợi ích + 1 bằng chứng → ràng buộc thật → nút "Gửi tin nhắn"` (Audience → hook that recalls what they watched → one benefit + one proof → real constraint → "Send message" button)
- **Worked example:** For the 75% viewers: "Cảm ơn bạn đã ở lại đến cuối workshop. Khóa 'Nói Có Lực' còn [n] suất, đóng thứ Năm 23h59. Bấm Gửi tin nhắn để nhận lịch học." (Thanks for staying to the end of the workshop. "Nói Có Lực" has [n] seats left and closes Thursday 23:59. Tap Send message for the schedule.)

### F8. The bait-safe CTA ladder (working within Meta's engagement-bait rules)
- **Source:** Meta engagement-bait guideline and Spam policy [DATA], TikTok guidance [DATA-2], [PRACTITIONER].
- **How it works:** pick the safest CTA that still converts.

| Level | CTA | Risk |
|---|---|---|
| L1 (safest) | "Nhắn cho mình chữ X" (DM keyword) | Lowest |
| L1 (safest) | A real question asking for advice or experience | Exempt-style |
| L2 | Link or form (mind the Page link limits; DM delivery is better) | Low |
| L3 | Comment a keyword, on a Page with official private replies, at most 1–2 posts/week, and the post must give value on its own | Medium |
| L4 (avoid) | Comment thresholds ("đủ 100 comment"), react bait ("thả tim nếu…"), tag or share bait, coded spellings | High |

- **Fill-in template:** `[Giá trị cốt lõi ngay trong bài]. Muốn bản đầy đủ [x]? Nhắn "[KEYWORD]" cho mình/Page — gửi trong vài phút.` ([Core value inside the post]. Want the full version? Message "[KEYWORD]" to me or the Page and it arrives within minutes.)
- **Worked example:** "Câu mở đầu số 1: … (dùng ngay được). Muốn đủ 7 câu kèm ví dụ? Nhắn 'MỞ' cho Page Linh Nói Có Lực." (Opening line #1: … usable right away. Want all 7 with examples? Message 'MỞ' to the Page.)

### F9. Launch calendars (21-day standard, 10-day sprint)
- **Source:** PLF and Learnybox timing [DATA-2/PRACTITIONER] + founder's "21 ngày".

**21-day standard:**

| Days | What runs |
|---|---|
| D-21 → D-15 | Mồi (3 posts) + belief shift (2) + value (2) + Zalo mini-course invites |
| D-14 → D-8 | 3-night mini-course in Zalo; 5-part case series; workshop registration |
| D-7 | Workshop or live |
| D-6 → D0 | Cart open: offer, FAQ, testimonials, "not for you", live Q&A, retargeting ads; bonus deadline at D-2; close at D0 23:59 |
| D+1 → D+7 | Close, waitlist, onboarding, wins |

**10-day sprint:** D-10 to D-5 is mồi + value + 1 case study. D-4 is the live. D-3 to D0 is cart open, ending in the close.

**Worked example (Linh, 21-day):** BG mồi on Monday, Wednesday and Friday; Zalo class 9–11 [month]; workshop Thursday 20:00; cart from Friday to the following Thursday.

### F10. Voice and xưng hô (forms of address) matrix
- **Source:** [PRACTITIONER] + founder examples.
- **How it works:** pick one pairing per launch and never switch mid-post.

| Pairing | When to use it |
|---|---|
| **mình – bạn** | Default for personal-brand coaches; warm and works across ages |
| **mình – anh chị em / ae** | Community or hustler tone (as in the founder's "anh em hữu duyên"); skews toward entrepreneurs and men |
| **tôi – bạn / quý anh chị** | Consultants and senior experts; authoritative but can feel cold on a personal profile |
| **em – anh chị** | A young coach selling to older professionals (real estate, insurance); humble but lowers authority |
| **cô/chị – các em** | Teacher personas |

- **Style markers** [PRACTITIONER]: a standalone first line; short lines; emoji bullets (👉 ✅ 🔥 👇) used sparingly; "Nói thật nhé" (honestly), "P/s"; full VND figures written with dots; one campaign hashtag.
- **What hurts trust:** "hữu duyên" used in every post, luxury flexing, screenshots of bank transfers, deleting critical comments, mass tagging, unsolicited DMs.
- **Worked example:** Linh uses "mình – bạn" in every post, DM and Zalo message, with one hashtag: #NoiCoLuc.

---

### Template library (Vietnamese): 8 phases × 11 templates

Tags: **[BG]** = text-on-background, 130 characters or less. **[DM]** = DM-keyword CTA (L1). **[CMT]** = comment trigger; use on a Page with automation, at most 1–2 per week (L3). **[LINK]** = form or link; mind the Page link limits. Placeholders are in [brackets].

#### Phase 1: Mồi + lead magnet
1. [BG][DM] Mình vừa soạn xong 7 câu mở đầu thuyết trình dùng được ngay. Không bán, chỉ tặng 50 bạn đầu tiên. Nhắn "MỞ" cho mình 👇
2. [BG][CMT] Nói 5 phút mà sếp chỉ nhớ 1 câu? Mình có checklist 1 trang sửa đúng chỗ đó. Gõ "CHECK" dưới bài, hệ thống gửi liền 👇
3. [DM] 11 giờ đêm qua, sau buổi coaching thứ 4 trong ngày, mình nhận ra gần như ai cũng kẹt ở đúng 1 chỗ: [vấn đề]. Thế là mình viết lại thành [tên tài liệu], [n] trang, đọc 10 phút là dùng được. Miễn phí đến hết [ngày]. Ai cần nhắn "[TỪ KHÓA]", mình gửi tận tay.
4. [LINK] Mình mở lớp mini 3 tối qua nhóm Zalo: mỗi tối 1 video 7 phút + 1 bài tập nhỏ. Miễn phí. Nhóm chỉ nhận 200 bạn vì mình chữa bài từng người. Form đăng ký chỉ hỏi 2 câu, link mình gửi qua tin nhắn khi bạn nhắn "LỚP".
5. [DM] Xong rồi! Bộ prompt "[tên]": dán vào ChatGPT/Claude là ra dàn ý bài nói 5 phút theo đúng khung mình dạy. Mở 99 suất dùng thử để lấy góp ý thật. Muốn thử, nhắn "PROMPT" nha.
6. [DM] Sau 1 tháng mày mò, mình làm xong [công cụ/khung]. Mình cần 30 người dùng thật và góp ý thẳng trước khi hoàn thiện. Không mất phí, chỉ cần dùng thật và nói thật. Ai nhận lời, nhắn "THỬ".
7. [LINK] Bạn thuộc kiểu người nói nào: Kể chuyện, Phân tích, Truyền lửa hay Lắng nghe? Bài test 2 phút, kết quả kèm 1 bài tập riêng cho kiểu của bạn. Nhắn "TEST" để nhận link.
8. [Câu hỏi thật, an toàn] Hỏi thật nè: lần gần nhất phải nói trước nhiều người, điều gì làm bạn run nhất? Mình đọc hết, rồi quay 1 video trả lời 3 nỗi lo được nhắc nhiều nhất.
9. [LINK] Tối thứ Năm, 20h, Zoom 60 phút: "3 lỗi khiến bạn nói mà không ai nghe". Miễn phí. Phòng tối đa [300] người, ai đăng ký trước giữ chỗ trước. Bận vẫn cứ đăng ký, có bản xem lại 48 giờ.
10. [DM] Mình đang quay dở bộ 5 video "[tên]", chưa đăng ở đâu cả. Ai muốn xem bản nháp và góp ý cho mình, nhắn "XEM". Chỉ gửi cho người thật sự muốn học, không spam.
11. [Nhóm FB riêng] Tài liệu này mình chỉ để trong nhóm: [tên], ở mục File. Đọc xong, comment 1 điều bạn sẽ thử tuần này. Thứ Bảy mình chọn 3 bạn để sửa trực tiếp trên live.

#### Phase 2: Belief shift
1. Mình từng tin người nói hay là do bẩm sinh. Cho đến khi [sự kiện]. Hóa ra thứ họ có không phải tài năng mà là [cơ chế]. Và [cơ chế] thì học được.
2. Ngừng luyện giọng đi. Nghe ngược đúng không? Phần lớn học viên mình gặp nói chưa hay không phải vì giọng, mà vì [nguyên nhân thật].
3. Bạn không thiếu tự tin. Bạn thiếu cấu trúc. Tự tin là kết quả của việc biết mình sắp nói gì, không phải điều kiện để bắt đầu.
4. 3 điều mình tin năm [năm] và giờ thấy sai: 1) [niềm tin cũ] 2) [...] 3) [...]. Điều mình tin bây giờ: [niềm tin mới].
5. Sự thật hơi khó nghe: học thêm khóa thứ 5 cũng không giúp bạn nói hay hơn nếu vẫn [hành vi cũ]. Thứ thay đổi bạn là [lặp lại có người sửa].
6. Vì sao người giỏi chuyên môn hay trình bày dở? Vì họ nói theo thứ tự mình nghĩ, còn người nghe cần [thứ tự khác]. Đổi thứ tự là đổi kết quả.
7. "Mình hướng nội nên không hợp nói trước đám đông." Một số người nói cuốn nhất mình biết là người hướng nội. Họ chỉ làm khác đúng 1 điều: [điều đó].
8. [Carousel] 5 lầm tưởng về thuyết trình: mỗi slide là 1 lầm tưởng, 1 sự thật, 1 việc làm ngay.
9. Mình đã dạy sai suốt 2 năm: bắt học viên học thuộc bài. Giờ mình làm ngược lại: [cách mới], và đây là điều thay đổi.
10. Cái giá của "để sau": mỗi buổi họp bạn im lặng là 1 lần ý tưởng của bạn được người khác nói trước. Không phải dọa, chỉ là phép cộng.
11. Thứ tự đúng không phải "giỏi rồi mới nói" mà là: nói, nhận phản hồi, sửa, rồi mới giỏi.

#### Phase 3: Value
1. Khung 3-2-1 cho bài nói 3 phút (lưu lại dùng dần): 3 câu mở, 2 ví dụ, 1 lời kêu gọi. [Giải thích từng phần.]
2. Trước/Sau: câu mở đầu của 1 học viên (đã xin phép). Trước: "…". Sau: "…". Khác nhau ở 2 chỗ: [a], [b].
3. Checklist 5 phút trước buổi họp quan trọng: ☐ [1] ☐ [2] ☐ [3] ☐ [4] ☐ [5].
4. Mổ xẻ 2 phút phát biểu công khai của [diễn giả]: 3 kỹ thuật bạn copy được ngay.
5. Trả lời 5 câu hỏi được hỏi nhiều nhất trong inbox tuần này.
6. Mẫu giới thiệu bản thân 30 giây, thay chữ trong ngoặc là dùng: "Mình là [tên], đang giúp [ai] làm [gì]. Gần đây mình [kết quả nhỏ, cụ thể]. Hôm nay mình mong [mục tiêu]."
7. 7 câu nên bỏ khi thuyết trình, kèm câu thay thế: "Em xin phép trình bày…" → "[câu mới]".
8. Bài tập 60 giây tối nay: ghi âm, nói về ngày hôm nay mà không dùng "thì", "là", "ờ". Nghe lại. Bạn sẽ bất ngờ.
9. [Kịch bản video ngắn] Hook 3 giây: "Đừng mở đầu bằng xin chào." Thân: 2 cách mở thay thế. CTA: "Lưu lại cho buổi họp tới."
10. Live sửa bài tối Chủ nhật: mình sửa trực tiếp 3 bài nói 1 phút các bạn gửi trước 18h thứ Bảy.
11. 4 công cụ miễn phí mình dùng để luyện nói mỗi ngày (không affiliate; nếu có link hoa hồng mình sẽ ghi rõ).

#### Phase 4: Educate / case-study series
1. Series 5 kỳ: 6 tuần của chị M., từ run tay khi phát biểu đến chủ trì họp quý. Kỳ 1 lên lúc 20h tối nay. Bấm Theo dõi để không lỡ.
2. [CMT, phiên bản trung thực của "đủ 100 comment"] Nhiều bạn hỏi nên mình sẽ viết chi tiết case này. Comment "UP" để mình biết bạn muốn đọc phần nào kỹ. Ít hay nhiều mình vẫn đăng nhé 😄
3. Kỳ 1, điểm xuất phát: tháng [x], chị M. nhắn mình: "[trích dẫn]". Bối cảnh: [vai trò], [nỗi sợ], [đã thử gì].
4. Kỳ 2, điểm nghẽn: tuần đầu mình phát hiện chị không thiếu ý, chị thiếu [cơ chế]. Đây là cách mình nhận ra.
5. Kỳ 3, thay đổi: 3 thứ tụi mình đổi: [1], [2], [3]. Cái khó nhất là [x].
6. Kỳ 4, kết quả có bối cảnh: sau 6 tuần, [kết quả đo được]. Chị tập 20 phút/ngày, 4 buổi sửa 1:1. Đây là kết quả của chị M., không phải cam kết cho mọi người.
7. Kỳ 5, bài học cho bạn: [3 bài học]. Muốn thử đúng quy trình này? Workshop tối thứ Năm, nhắn "WORKSHOP" để nhận link.
8. [Case doanh thu] [571.000.000đ] sau [7 ngày] mở bán, và 6 con số phía sau ít ai kể: tệp [x] người xây trong [y] năm, [z] người dự workshop, [a]đ quảng cáo, giá [b]đ, [c] người mua, [d] hoàn tiền. Mình kể để bạn thấy cấu trúc, không phải để hứa hẹn.
9. 3 học viên, 3 kết quả khác nhau: [A] đạt [x], [B] đạt [y], [C] chưa đạt vì [z]. Kết quả phụ thuộc vào [yếu tố].
10. Một học viên không đạt mục tiêu, và điều mình đã sửa trong khóa vì bạn ấy.
11. Bên trong 1 buổi coaching 1:1: 45 phút diễn ra thế nào, từng phút một.

#### Phase 5: Open cart (direct response)
1. **MỞ ĐĂNG KÝ "[Khóa]"**: [lời hứa chính, có điều kiện].
   Dành cho: 👉 [persona 1] 👉 [persona 2] 👉 [persona 3]
   3 việc bạn sẽ làm: **Gỡ ý ra khung** (tuần 1–2) / **Luyện thành lực** (tuần 3–4) / **Ra trận thật** (tuần 5–6).
   Bên trong: [số buổi], [hình thức], [hỗ trợ]. Học phí [giá] (ưu đãi đến [ngày], sau đó [giá]). [n] suất vì [lý do thật].
   Không dành cho bạn nếu: [2 điều]. Đăng ký: nhắn "ĐĂNG KÝ". #[campaign]
2. [BG] Chính thức mở đăng ký [Khóa]. 30 suất, đóng 23h59 ngày [dd/mm]. Chi tiết ở bài ghim trên trang mình 👇
3. Khóa này KHÔNG dành cho bạn nếu: [không có 20 phút/ngày], [muốn kết quả mà không tập], [đã nói tốt và chỉ cần sân khấu].
4. FAQ: học giờ nào? Lỡ buổi thì sao? Có trả góp không? Có hoàn phí không? Khác gì video miễn phí?
5. [Giá]đ nghĩa là gì: [n] buổi nhóm + [m] buổi sửa 1:1 + nhóm hỗ trợ 6 tuần. So sánh thật với [lựa chọn thay thế], không phóng đại.
6. Vì sao mình mở khóa này, và vì sao tới giờ mới mở.
7. Học viên nói gì (đã xin phép): [3 trích dẫn ngắn, tên + vai trò].
8. Cam kết của mình: học hết 2 tuần đầu, làm đủ bài tập mà thấy không phù hợp thì mình hoàn 100% học phí. Mình cam kết quy trình, không cam kết thay bạn kết quả.
9. Tự học, học nhóm hay 1:1, chọn thế nào cho đúng túi tiền và mục tiêu? (Nói thật cả lúc lựa chọn khác hợp với bạn hơn.)
10. Tối nay 21h, live 45 phút trả lời mọi câu hỏi về khóa. Gửi câu hỏi trước qua tin nhắn.
11. [DM, tin nhắn riêng đầu tiên phải đủ thông tin] "Chào [tên], đây là đủ thông tin khóa: lịch [x], học phí [y], ưu đãi đến [z], [n] suất. Bạn muốn mình giữ chỗ hay cần hỏi thêm điều gì trước?"

#### Phase 6: Retargeting (ads + organic follow-up)
1. [Ad, người xem 75% workshop] Cảm ơn bạn đã ở lại đến cuối workshop. Như đã hứa, đây là chi tiết khóa "[Khóa]": còn [n] suất, đóng [ngày]. Bấm Gửi tin nhắn để nhận lịch học.
2. [Ad, người nhận tài liệu] Bạn đã có [tài liệu]. Nếu bước 1 dễ mà bước 2 khó, đó là lúc cần người sửa trực tiếp. [Khóa] giúp đúng phần đó.
3. [Ad, người xem 50% video] Bạn vừa xem "[video]". Muốn có người kèm từng tuần để làm được điều đó? Nhắn cho mình.
4. [Ad, testimonial] "[trích dẫn ngắn]", [tên], [vai trò]. Kết quả cá nhân, mỗi người mỗi khác. Tìm hiểu khóa: Gửi tin nhắn.
5. [Ad, phản bác "không có thời gian"] Khóa thiết kế cho người bận: 20 phút/ngày, buổi tối, có bản xem lại.
6. [Ad, phản bác "hướng nội"] Lớp nhỏ 30 người, tập theo cặp trước khi nói trước nhóm. Không ai bị "đẩy lên sân khấu".
7. [Click-to-Zalo/Messenger] Nhắn cho mình để nhận lịch khai giảng và học phí. Mình trả lời trong ngày.
8. [DM trong 24 giờ, khi người đó đã nhắn] Chào [tên], hôm qua bạn hỏi về [x]. Mình gửi thêm [thông tin], bạn cần mình giải thích phần nào nữa không?
9. [Nhóm Zalo] Nhắc nhẹ cả nhà: tối nay 20h có buổi hỏi đáp về khóa. Ai đã đăng ký mini-class đều vào được.
10. [ZNS hoặc tin OA, có đồng ý trước] [Tên], ưu đãi [x] của khóa [Khóa] kết thúc lúc 23h59 ngày [dd/mm]. Chi tiết: [nút].
11. [Nhắc lại một lần duy nhất] Mình nhắn 1 lần thôi nha: khóa đóng tối thứ Năm. Nếu chưa phải lúc, cứ bỏ qua tin này, mình vẫn gửi tài liệu miễn phí đều đặn.

*Every ad excludes buyers. Ads use the "Gửi tin nhắn" (Send message) button, never "comment X".*

#### Phase 7: Urgency and scarcity (real constraints only)
1. Cập nhật 12h: còn 9/30 suất. Mình cập nhật lại lúc 20h tối nay.
2. Quà 1 buổi 1:1 30 phút chỉ dành cho bạn đăng ký trước 23h59 thứ Tư. Sau đó khóa vẫn mở, chỉ không còn quà.
3. Học phí [4.900.000đ] đến hết [ngày]. Từ [ngày] là [5.900.000đ], giá chính thức cho các khóa sau.
4. Lớp khai giảng [ngày]. Sau ngày đó mình không nhận thêm, vì cả nhóm đã bắt đầu học cùng nhau.
5. Còn 48 giờ. Đây là 3 câu hỏi mình nhận nhiều nhất hôm nay, kèm câu trả lời.
6. Lá thư cuối: nếu bạn vẫn đang phân vân, đây là cách mình sẽ tự quyết nếu là bạn: [3 câu hỏi tự kiểm tra].
7. [BG] Còn 6 tiếng. [Khóa] đóng đăng ký lúc 23h59 tối nay. Khóa sau dự kiến tháng [x]. 👇
8. Vì sao chỉ 30 suất? Vì mỗi tuần mình tự nghe và sửa bài từng bạn. Nhiều hơn thì mình không làm tử tế được.
9. Sau khi đóng thì sao? Mình không mở lại đợt này. Ai bỏ lỡ có thể vào danh sách chờ để được báo trước khi mở lại.
10. [DM cho người đã hỏi] Chào [tên], khóa đóng sau [x] giờ nữa. Bạn muốn mình giữ 1 suất không?
11. Đã đủ 30 suất. Cảm ơn mọi người đã tin tưởng. Danh sách chờ khóa sau ở đây: nhắn "CHỜ".

#### Phase 8: Close and post-launch
1. Đã đóng đăng ký "[Khóa]". Cảm ơn [n] bạn đã chọn học cùng mình. Tuần sau mình bắt đầu.
2. Gửi bạn chưa tham gia: không sao cả. Đây là [tài liệu/video] tặng bạn để tự tập tiếp.
3. Danh sách chờ khóa sau đã mở. Người trong danh sách được báo trước và có ưu đãi riêng. Nhắn "CHỜ".
4. Nhìn lại đợt mở bán: con số thật (đã dự, đã mua, đã hoàn), điều làm tốt và điều chưa tốt.
5. [Nhóm Zalo học viên] Chào mừng cả lớp! Việc đầu tiên: [hướng dẫn tuần 0]. Nội quy nhóm: [3 dòng].
6. Tuần 1 của lớp: [2–3 tiến bộ nhỏ của học viên, đã xin phép].
7. Khảo sát 3 câu: điều gì làm bạn quyết định tham gia, hoặc không tham gia? Mình đọc hết để sửa đợt sau.
8. 5 bài học từ đợt mở bán này, nếu bạn cũng đang chuẩn bị ra mắt sản phẩm.
9. Nếu khóa 6 tuần chưa hợp lúc này: có [lựa chọn nhỏ hơn: workbook/1 buổi workshop có phí] cho bạn bắt đầu.
10. Bộ tài liệu miễn phí vẫn mở cho người mới. Nhắn "MỞ" như cũ.
11. Học viên giới thiệu bạn bè sẽ nhận [quà]. Khi chia sẻ, nhớ ghi rõ "#QuảngCáo / mình nhận quà giới thiệu" theo quy định mới nhé.

---

## 3) Implications for the Content Machine Launch module

1. **Add a "Launch Mode" that runs on top of the domino series.** Map the 8 phases onto the existing chain: Admirable/Likable for mồi and value, Credible for case studies, Trustable for open cart and close.
   - **Inputs:** offer, real constraints, proof assets with consent, channel mix, whether automation is available, calendar length (21 or 10 days), and xưng hô.
   - **Outputs:** a calendar, every post, DM macros, Zalo nurture scripts, retargeting ad sets, and a close/post-launch kit, in both VN and EN.

2. **Platform router (critical).** Ask "Are you launching from a personal profile, a Page, a Group, TikTok or Zalo?" Then automatically:
   - require a Page/IG mirror and a pixel if the user wants retargeting;
   - switch comment CTAs to DM-keyword CTAs for profiles;
   - warn about Page and professional-mode link limits (Meta One);
   - cap BG posts at 130 characters;
   - set Zalo group size to 200 or 1,000.

3. **Bait-risk meter.** Score each post L1–L4 (F8). Cap comment-trigger posts at 1–2 per week. Rewrite threshold posts ("đủ 100 comment") into date-based posts. Flag coded spellings ("c.m", "q.t") with an explanation, not a silent fix.

4. **Compliance linter, VN edition.** Flag:
   - "nhất / số 1 / duy nhất" without proof;
   - guaranteed income, health or result promises;
   - revenue numbers without the context block;
   - testimonials without consent;
   - missing "#QuảngCáo" for affiliates or students who promote;
   - gift value above 50% of price, or discounts above 50%;
   - personal-data asks without a purpose/consent line;
   - slang or abbreviations in ad copy;
   - fake scarcity (a counter that doesn't change, repeated "today only").

   Ship a short note that the user should check with a lawyer. Decree 87/2026 per-violation amounts still need confirming.

5. **First-DM designer.** Because Meta allows exactly one automated private reply, the module should generate first messages that deliver the promised resource, ask a two-option question, and include the consent line (F4).

6. **Proof vault + case-series builder.** Store each case with metrics, context, a consent date and the disclaimer. Generate the 5-part series automatically (F5). The founder's "571.000.000" style becomes a template that forces the context block.

7. **Honest scarcity ledger** (F6), with a slot-counter workflow a VA can update twice a day.

8. **Tool picker.**
   - Page users: Botcake (free tier is enough for most coaches) or Fchat (for Zalo OA in one place).
   - High-volume or livestream sellers: Pancake or HaraSocial.
   - EN/IG users: ManyChat.
   - Profile-only users: manual VA macros.

   Prices change, so version-stamp them.

9. **Trust guardrails as a design principle.** Vietnamese audiences now read "free → upsell → income flex" as lùa gà. Bake in: value-complete posts, failure and variance cases, "who it's not for", refund terms, visible real counters, no luxury or bank-transfer screenshots, and no clone seeding (Decree 147 makes accounts traceable).

10. **Metrics sheet:** reach → conversations (DM/comment) → Zalo joins → workshop show-up → open-cart enquiries → sales → refunds. Vietnamese benchmarks are unknown, so let users log their own numbers and compare launches.

11. **EN edition delta.** Swap Zalo for email and SMS. Give Instagram (ManyChat comment-to-DM) more weight. Swap VN law for FTC/ASA-style earnings-claim rules. The 8-phase structure stays the same.

12. **Validation task before shipping.** Have the founder check the [PRACTITIONER] slang and norms ("chấm", "UP", "slot", "hữu duyên", typical launch length, show-up rates) against 5–10 current Vietnamese coach launches.

---

## 4) Sources

**Meta and TikTok policy and documentation**
- Meta Transparency Center — Engagement Bait: https://transparency.meta.com/features/approach-to-ranking/content-distribution-guidelines/engagement-bait/
- Meta Newsroom — Fighting Engagement Bait on Facebook (2017): https://about.fb.com/news/2017/12/news-feed-fyi-fighting-engagement-bait-on-facebook/
- Meta Community Standards — Spam: https://transparency.meta.com/policies/community-standards/spam/
- Meta for Developers — Messenger Platform & IG Messaging API Policy: https://developers.facebook.com/documentation/business-messaging/messenger-platform/policy
- Meta Marketing API — Engagement Custom Audiences: https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/guides/engagement-custom-audiences
- Meta Newsroom — Introducing Meta One (Sep 2026): https://about.fb.com/news/2026/09/introducing-meta-one-subscription-service-more-features-ai/
- TechCrunch — Facebook tests link posting limit (Dec 2025): https://techcrunch.com/2025/12/17/facebook-is-testing-a-link-posting-limit-for-professional-accounts-and-pages
- Davide Cosmai — Meta One and the Facebook link limit: https://davidecosmai.com/en/notes/meta-one-limite-link-facebook/
- TechCrunch — Meta crackdown on unoriginal content (Jul 2025): https://techcrunch.com/2025/07/14/following-youtube-meta-announces-crackdown-on-unoriginal-facebook-content
- InstantDM — Facebook Comment Automation (2026): https://instantdm.com/blog/facebook-comment-automation
- heyy.to — Meta Business Suite comment auto-reply (2026): https://heyy.to/blog/meta-business-suite-comment-auto-reply/
- Stackmatix — Meta Ads Income Claims Policy (2026): https://www.stackmatix.com/blog/meta-ads-income-claims-policy
- Publer — Facebook background posts (130-character limit): https://publer.com/help/en/article/how-to-create-a-facebook-status-update-with-a-background-14recqj
- AuditSocials — TikTok Engagement Bait Rules 2026: https://www.auditsocials.com/blog/tiktok-engagement-bait-community-guidelines
- Pancake Docs — TikTok Business Messaging: https://docs.pancake.vn/english/pancake-software-user-guide/2.-connect-to-sales-channels/tiktok-business-messaging

**Vietnam market data**
- DataReportal — Digital 2026: Vietnam: https://datareportal.com/reports/digital-2026-vietnam
- Tuổi Trẻ News — Zalo 80M users / VNG: https://news.tuoitre.vn/vietnams-80-million-user-messaging-giant-zalo-puts-spotlight-on-parent-vngs-business-103251229150347905.htm
- Bizhub (Vietnam News) — Meta messaging products / Decision Lab study (Jun 2024): https://bizhub.vietnamnews.vn/meta-launches-new-messaging-products-for-viet-nam-post357433.html

**Tools and pricing**
- Botcake pricing: https://botcake.io/pricing
- Fchat pricing: https://fchat.vn/price
- Nhân Hòa — Pancake là gì (2022 pricing): https://blog.nhanhoa.com/pancake-la-gi/
- Haravan — HaraSocial features: https://www.haravan.com/pages/tinh-nang-phan-mem-harasocial
- Featurebase — ManyChat pricing 2026: https://www.featurebase.app/blog/manychat-pricing
- Zalo Solutions — OA pricing: https://zalo.solutions/oa/pricing
- Nhanh.vn — Bảng giá ZNS: https://zns.nhanh.vn/bang-gia-dich-vu-zalo-zns-nhan-tin-cham-soc-khach-hang-qua-zalo-n97625.html
- Di Động Việt — Zalo Business (2026): https://didongviet.vn/dchannel/tai-khoan-business-zalo/
- Viettel Store — Nhóm Zalo tối đa bao nhiêu người: https://viettelstore.vn/tin-tuc/nhom-zalo-toi-da-bao-nhieu-nguoi-cach-xac-tai-khoan-de-tao-nhom-zalo

**Vietnamese law**
- Huỳnh Nam Law — 5 điểm mới Luật Quảng cáo sửa đổi 2025: https://huynhnamlawfirm.vn/luat-quang-cao-sua-doi-2025-5-diem-moi-doanh-nghiep-va-kols-nhat-dinh-phai-biet/
- The Influencer — Luật Quảng cáo 2025 (Điều 15a): https://theinfluencer.vn/luat-quang-cao-2025-co-hieu-luc-tu-2026-cu-hich-phap-ly-manh-me-cho-thi-truong-influencer-marketing
- Thư Viện Pháp Luật — Quảng cáo trên mạng từ 01/01/2026: https://thuvienphapluat.vn/chinh-sach-phap-luat-moi/vn/ho-tro-phap-luat/chinh-sach-moi/88658/quy-dinh-ve-quang-cao-tren-mang-tu-01-01-2026
- LSVN — Tài liệu chứng minh khi dùng từ "nhất" (Thông tư 12/2026): https://lsvn.vn/quy-dinh-ve-tai-lieu-chung-minh-khi-quang-cao-su-dung-tu-nhat-duy-nhat-tot-nhat-so-mot-a173667.html
- LuatVietnam — Nghị định 342/2025 (chi tiết Luật Quảng cáo): https://luatvietnam.vn/van-hoa/nghi-dinh-342-2025-nd-cp-quy-dinh-chi-tiet-luat-quang-cao-co-hieu-luc-2026-422938-d1.html
- LuatVietnam — Nghị định 87/2026 (xử phạt văn hóa, quảng cáo): https://luatvietnam.vn/vi-pham-hanh-chinh/nghi-dinh-87-2026-nd-cp-xu-phat-vi-pham-hanh-chinh-trong-van-hoa-va-quang-cao-431418-d1.html
- LuatVietnam — Từ lóng, sai chính tả trong quảng cáo: https://luatvietnam.vn/linh-vuc-khac/quy-dinh-moi-cam-su-dung-tu-long-tu-sai-chinh-ta-trong-quang-cao-883-107097-article.html
- Kế toán An Phá — Mức phạt quảng cáo sai sự thật (Nghị định 38/2021, superseded): https://ketoananpha.vn/muc-phat-quang-cao-sai-su-that.html
- LuatVietnam — Khuyến mại không vượt quá 50% từ 01/7/2025: https://luatvietnam.vn/tin-van-ban-moi/khuyen-mai-hang-hoa-dich-vu-khong-vuot-qua-50-gia-tri-tu-01-7-2025-186-102656-article.html
- KPMG Vietnam — Nghị định 239/2026 về khuyến mại: https://kpmg.com/vn/vi/insights/2026/07/decree-239-on-sales-promotion.html
- LuatVietnam — Luật Bảo vệ dữ liệu cá nhân 2025 (91/2025/QH15): https://luatvietnam.vn/tin-van-ban-moi/da-co-luat-bao-ve-du-lieu-ca-nhan-2025-so-91-2025-qh15-186-102925-article.html
- VOV — Xác thực tài khoản MXH từ 25/12 (Nghị định 147/2024): https://vov.vn/xa-hoi/tu-ngay-2512-nguoi-dung-mang-xa-hoi-can-luu-y-gi-ve-xac-thuc-tai-khoan-post1141133.vov

**Trust, culture and seeding in Vietnam**
- Dân Trí — Khóa học làm giàu, tránh bị "lùa gà" (Dec 2024): https://dantri.com.vn/kinh-doanh/nhan-nhan-khoa-hoc-day-lam-giau-nhu-mr-pips-lam-sao-de-tranh-bi-lua-ga-20241211163325451.htm
- CAND — Chốt đơn online hay chiêu thức "lùa gà" (Mar 2024): https://cand.vn/phong-su/chot-don-online-hay-chieu-thuc-lua-ga--i726282/
- 24h — Bi hài trào lưu khởi nghiệp trên MXH (Sep 2026): https://24h.com.vn/kinh-doanh/bi-hai-trao-luu-khoi-nghiep-tren-nen-tang-mang-xa-hoi-c161a1798904.html
- VietnamNet — Thật giả khóa dạy bán hàng TikTok Shop: https://vietnamnet.vn/that-gia-khoa-day-ban-hang-chot-nghin-don-tren-tiktok-shop-i5001996.html
- Brands Vietnam — Seeding Facebook tips: https://www.brandsvietnam.com/congdong/topic/333997-Seeding-Facebook-tips-tang-tuong-tac-va-phat-trien-cong-dong-so-cho-doanh-nghiep
- Sapo — Tool seeding: con dao hai lưỡi: https://www.sapo.vn/blog/tool-seeding-con-dao-hai-luoi-va-cach-seeding-hieu-qua-khi-chay-quang-cao-facebook

**Launch frameworks and benchmarks**
- systeme.io — Jeff Walker's Product Launch Formula: https://systeme.io/blog/jeff-walker-product
- Brandcamp — Mô hình 3 đoạn tung hàng: https://www.brandcamp.asia/blog/144-mo-hinh-3-doan-tung-hang-ra-mat-san-pham-moi
- Learnybox — Email sequence for a course launch (2026): https://learnybox.com/en/blog/email-sequence-for-a-course-launch/
- Hubilo — Webinar statistics and benchmarks 2025: https://www.hubilo.com/blog/webinar-marketing-statistics-benchmarks
- Thiết bị họp — Livestream Zoom Webinar lên Facebook: https://thietbihop.com/huong-dan-livestream-zoom-webinar-len-facebook/