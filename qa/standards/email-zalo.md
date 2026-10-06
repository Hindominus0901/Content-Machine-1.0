# Email / Zalo message standard (`email-zalo`)

Build-only rubric (wf12-qa-spec §3.1). Never shipped. It is the G3 judge rubric for email and Zalo messages and the source of `standard = "email-zalo"` eval cases.
Sources, in order: wf12-qa-spec §3.1 and its dedupe rules (final, wins) · wf12-qa-standards §12 (draft) and House Rules §4 · wf5 §4.8–§4.9 (reply kit, nurture and open-cart sequences) · DECISIONS (formats; privacy).

## Purpose

One message with one job that earns the next open. This is the owned-channel half of every domino.

What good means: one job and one CTA; 3 personal subject lines, each paid off in the first two sentences; a preview or first line that opens a loop; story → one lesson → link to the pillar → P.S. CTA, in 250 words or fewer. It reads as the coach writing to one person and is worth reading even if they never buy. It goes only to opted-in readers, and every capture message or Zalo sequence has an easy way out.

## Scope

- **Format:** email (nurture, value, launch open-cart, last call) and Zalo messages (1:1, group, Zalo OA where consented), including capture messages (M1, M2) when they go by email or Zalo. Single messages and sequences (the 5-message nurture; the open-cart order, wf5 §4.9).
- **Output class:** Script, normal; a sales email or a message with a price, seats or a deadline is Script, claims.
- **Scored on top of `shared.md`,** which must pass first. This file never restates SG items: truth, claims, polarity, quotes, urgency-from-the-Ledger and the keyword live there.
- **Not here:** a subject line or DM line on its own (`micro.md`); sending, list hygiene and the email tool's settings (the machine can't test a send).

## Items

| ID | Item | 0 | 1 | 2 | Critical |
|---|---|---|---|---|---|
| EM1 | One job, one CTA [D] | Two asks, or links to two different places | One ask, but a second link or a buried second action | One link or one ask. A value email carries the offer only in the P.S. | yes |
| EM2 | Subject and preview | A fake "Re:" or "Fwd:", or a subject the body never pays off | Subjects that read commercial, or a preview that summarises | 3 subject lines, personal not commercial, each a claim or a question, paid off within the first 2 sentences; the preview or first line opens a loop | no |
| EM3 | House voice | A corporate or form-letter register, stacked fragments, or padding | One of the three rules slips | The three rules hold: simple words with rhythm (no stacked fragments); nothing unnecessary; one person, "you" (VN: the coach's xưng hô, to one reader) | yes |
| EM4 | Earns the next open | A pure pitch with nothing to keep | Some value, but a loop left open | Valuable on its own; every loop opened is closed in the same message; a sequence is about 80% value | no |
| EM5 | Length [D] | Over the limit | — | Email ≤250 words; Zalo within its dated default in `platform/targets.toml` | no |
| EM6 | Consent and exit | Sent to contacts who did not opt in; a capture message with no purpose or consent line; a Zalo sequence with no stop word; or deliverability or a stop rule claimed as tested | Email whose unsubscribe link and postal address (via the coach's email tool) are "not confirmed" | Opted-in contacts only. Capture messages state the purpose and ask for consent. Zalo sequences carry a stop word. Email relies on the coach's email tool for the unsubscribe link and postal address, confirmed once at setup | yes |
| EM7 | Truth in the inbox | Fake familiarity ("I saw you opened this", a fake personal recap, "as promised" when nothing was promised); guilt or shame lines | Manufactured intimacy on a list send ("I'm writing this just to you") | None of those: the message treats the reader as an adult on a list they chose, and pushes only with the reasons the post or offer already gives | yes |
| EM8 | Continuity | Price, guarantee or deadline differs from the offer or the Ledger | Same terms, but a different argument from the post or pillar it follows | Makes the same argument as the post or pillar it links to; price, guarantee and deadline are exactly as the offer and the Ledger state them | no |
| EM9 | Sequence fit | Out of order (e.g. the offer before the nurture's epiphany message) | The right place, but the buyer-exclusion or stop rule isn't stated | Matches its role (nurture: deliver + set the stage → backstory and the wall → the epiphany → hidden benefits + invite → waitlist and early access; then the open-cart order). States the buyer-exclusion and stop rule as one line for the coach | no |

**The three inline rules (EM3)** replace "Part A 6/6" (spec §3.1 dedupe): simple words with rhythm, no stacked fragments · nothing unnecessary · one person, "you".

## Build pass rule

- **Shared rule:** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; hard gates clear; no conditional pass; uncertain = 0.
- **Here:** `shared.md` passes; EM1, EM3, EM6 and EM7 score 2; total ≥15/18.
- **Deliverability is recorded "not run",** never "clean". The machine can't test a send, so it never claims a stop rule works.
- EM6 at 1 ("not confirmed") fails the build; the persona's setup answers must confirm the email tool once.
- EM9 is N/A for a one-off message that belongs to no sequence.

## Hard gates

- Every gate in `shared.md` (SG1, SG2, SG3, SG-copy, SG4, SG7) is scored there and must be clear.
- **Honesty:** a message or record that says deliverability, unsubscribe or the stop word was tested scores EM6 = 0 ("never claim a check that didn't run").
- **Capture in private only:** a phone or Zalo number is never asked for in public comments (a House Rules hard stop); capture runs in a DM, a form or the message itself.

## Runtime check shipped

`core/format-checks.toml`:

```toml
[format.email-zalo]
checks = [
  "Does it have one job and one CTA?",
  "Does the preview (or first line) open a loop?",
  "Are price, guarantee and deadline the same as in the post or offer it follows?",
  "Does it go only to people who opted in, with a stop line on Zalo?",
  "Is every deadline real, with deliverability recorded \"not run\"?",
]
checks_vn = [
  "Một việc, một lời kêu gọi?",
  "Dòng xem trước (hoặc câu đầu) mở ra một điều khiến người đọc muốn đọc tiếp?",
  "Giá, điều kiện hoàn tiền và hạn chót giống hệt bài đăng hoặc offer trước đó?",
  "Chỉ gửi người đã đồng ý nhận, và tin Zalo có dòng \"Muốn dừng nhận tin, nhắn DỪNG\"?",
  "Mọi hạn chót đều thật, và việc gửi vào hộp thư được ghi \"chưa kiểm\"?",
]
```

## VN note

- Zalo replaces email in the private track. With no subject line, line 1 does the subject's job (EM2 scores line 1).
- Use [anh/chị] or the chosen pronoun pair, the same one through a whole sequence.
- The stop line is "Muốn dừng nhận tin, nhắn DỪNG".
- Each capture message carries the purpose and consent line required by PDP Law 91/2025.
- Zalo OA and ZNS promotional templates have their own approval rules [VERIFY]; this is a note only, never a check.
- Prices with dots (9.900.000đ), public; never "giá ib".

## Calibration (fictional coaches)

**PASS.** EN, a bookkeeping coach for solo plumbers. Nurture #2, 180 words, to the list that opted in through the FRIDAY SHOEBOX sheet. Subject: "The envelope that cost me a client". Preview: "It was the fuel receipt." Body: the van-dashboard story (S-06), one lesson, a link to the pillar. One ask: "Reply with the day you'd do yours." The email tool's unsubscribe line was confirmed at setup. EM1 2 · EM2 2 · EM3 2 · EM4 2 · EM5 2 · EM6 2 · EM7 2 · EM8 2 · EM9 1 (no stop-rule line for the coach) = 17/18, with `shared.md` passed. **Result: PASS.**

**FAIL.** VN, a coach for small flower-shop owners. Zalo, open-cart day. It opens: "Mình thấy bạn đã xem tin hôm qua rồi nè, sao chưa đăng ký?" and ends with no stop word. EM7 = 0 (fake familiarity) and EM6 = 0 (no stop word). **Result: FAIL** (EM7: "Mình thấy bạn đã xem tin hôm qua rồi nè"; EM6: no "Muốn dừng nhận tin, nhắn DỪNG").
