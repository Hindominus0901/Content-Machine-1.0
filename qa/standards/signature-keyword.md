# Signature keyword standard (`signature-keyword`)

Build-only rubric (wf12-qa-spec §3.1). Never shipped. It is the G3 judge rubric for the keyword pick and the source of `standard = "signature-keyword"` eval cases.
Sources, in order: wf12-qa-spec §2.8, §3.1, §6 (final, wins) · wf12-qa-standards §4 (draft) · wf7 §4.7 (KW- candidates and lexicon), §7.1 G1–G3 · wf11 §0, §2.1, §3.3 · DECISIONS (edge thesis, comment keywords).

## Purpose

Pick the term that attaches to the coach and that the audience already says: "từ khoá gắn liền với người đó và cũng là 1 từ mà tệp của người đó nói". A signature keyword, not SEO. It is carried once in every piece.

What good means: the term is built from words 3 or more buyers said in 2 or more places; no alternative owns it; the coach can say it 100 times without cringing. The machine picks it and shows why, and the coach can swap it with one word. The registry tracks uses, placements and echo (the audience saying it back).

## Scope

- **Artifact:** the keyword pick: the Map's KEYWORD line, the Brand Card keyword field, the KW- candidate rows in the Research Brief, and the registry fields.
- **When:** the Day-0 pick from the brain-dump; re-scored after the first listening paste, at each monthly re-plan and at a Season change.
- **Output class:** Structured artifact (spec §2.1).
- **Not here:** in-piece use (exactly once, rotated placement, never the same placement twice in a row) is scored by `shared.md` SG6 and SG7.

## Items

| ID | Item | 0 | 1 | 2 | Critical |
|---|---|---|---|---|---|
| SK1 | Audience origin [D] | The origin doesn't recount; the coach's own line, or a quote from fewer than 3 named clients, counted as people; or a provisional term presented as proven | Short of the bar and honestly marked provisional `[guess]`, with the real count shown, the Buyer Mirror set as homework, and pieces meanwhile using the top V-row phrase | Origin V-IDs show ≥3 different people in ≥2 places, or a buyer phrase the coach quotes from ≥3 named clients (founder, 7 Oct 2026). The coach's own clients count; the coach's own lines never do; one client plus "lots of people say it" stays under the bar; duplicates and comments under one post count once per person and place | yes |
| SK2 | Not owned | A named term, product or program of an alternative in the grid | Not owned as far as anyone looked, but the search isn't recorded | Not a named term of any alternative in the grid, and the search is recorded | yes |
| SK3 | Meaning and role | No stated meaning | A meaning, but no role | A one-line meaning; it names a framework, mechanism, enemy, identity or result | no |
| SK4 | Sayable [D] | More than 4 words, or it can't be said aloud naturally | Sayable score 1, or awkward in the coach's voice | ≤4 words, Sayable score ≥2 (of 3), and it reads naturally aloud in the coach's voice | no |
| SK5 | Ownable | Ownable score 1, and it says nothing about this coach | Ownable score 1 with a clear role, or a coined term not built from client words | Ownable score ≥2 (of 3). Coined terms are built from client words; ≤5 coined terms in total (Card rule) | no |
| SK6 | Default shown, swappable | Hidden; presented as the coach's own choice when the machine made it; or no way to swap | Shown, but with no origin or no reason; or the coach must choose from a list before anything is written (an extra decision) | The machine's default is shown in plain words with its origin (who said it, where, by role) and one reason it fits; the alternates are kept; "change" / "đổi" swaps it with no other step | yes |
| SK7 | Registry [D] | No registry fields | Some fields missing, or rotation off | `status`, `uses_30d`, `placements_last_10` and `echo_count` are set; rotation is on. A term with 0 echo after 90 days is offered for retirement at the monthly re-plan; the coach decides | no |
| SK8 | Clean | An identity-group term or a competitor's brand | A generic category word as the whole term ("mindset", "growth", "content") | None of those. VN: no teencode in a term that may run in an ad | no |

**Sayable and Ownable** are the 1–3 scores on the KW- row (wf7 §4.7): Sayable = could the coach say it 100 times; Ownable = would people link it to this coach and no one else.

## Build pass rule

- **Shared rule:** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; hard gates clear; no conditional pass; uncertain = 0.
- **Here:** SK1, SK2 and SK6 score 2; no item scores 0; total ≥13/16.
- **A provisional pick fails the standard** (SK1 = 1). That honest FAIL, named "provisional", is the correct Day-0 result for a dump-only cold start. The term is re-scored after the first listening paste. SK1 = 0 (a provisional term presented as proven) is an honesty fail, recorded in `qa/LEDGER.md`.
- The judge recounts people and places from the cited V-IDs at source, and drops sellers, coaches, bots and seeding accounts first (wf7 G1).
- The shortlist-of-3 decision is removed (spec §6): the machine picks, and "change" swaps.

## Hard gates

- **No names or handles** in the origin record: people appear by role and V-ID only; commenters are never stored.
- **No identity-group term and no competitor's brand** as a keyword (SK8 = 0 fails via "no 0").
- **The coach's own line never counts as a person** (wf7 G3). A phrase the coach quotes from 3+ named clients counts as heard for the keyword; fewer than 3 named clients (one client plus "lots of people say it") stays "(my guess)" / "(mình đoán, Tuần 1 kiểm lại)" (DECISIONS 7 Oct 2026). The research KEEP / WATCH rule is unchanged.
- **Never blocked:** keyword CTAs built on the term, thresholds and "chấm" are written as the coach asks, with one dated note (DECISIONS).

## Runtime check shipped

`core/format-checks.toml`:

```toml
[format.signature-keyword]
checks = [
  "Are the origin V-IDs listed (3+ people, 2+ places), or is the term marked provisional [guess]?",
  "Is it free of every alternative's named terms?",
  "Did the machine pick it and say where it came from and why, in plain words?",
  "Can the coach swap it by saying \"change\", with no other step?",
  "Is it 4 words or fewer and easy to say aloud in the coach's voice?",
]
checks_vn = [
  "Có liệt kê V-ID nguồn (từ 3 người, ở 2 nơi trở lên), hoặc gắn [guess] tạm thời?",
  "Không trùng thuật ngữ riêng của bất kỳ đối thủ nào?",
  "Máy tự chọn và nói rõ nguồn gốc, lý do bằng lời thường?",
  "Coach nhắn \"đổi\" là đổi được ngay, không thêm bước nào?",
  "Tối đa 4 từ, đọc to bằng giọng coach vẫn tự nhiên?",
]
```

## VN note

- A spelling without diacritics is the same keyword (DANG KY = ĐĂNG KÝ); the registry holds both forms.
- English loanwords are fine when the V-rows show buyers using them.
- No teencode as a keyword in anything that might run as an ad (the clear-wording rule); it gets a note, not a block.
- A CTA mechanic ("chấm", "inbox") is never the keyword, and neither is the method name: the keyword, the method name and the old-way name are three separate signature phrases (wf11 §4, rule 7).
- SK4 counts words by whitespace, as the other VN counts do, so the VN cap is 4 tiếng.

## Calibration (fictional coaches)

**PASS.** EN, a bookkeeping coach for solo plumbers. Default: "Friday shoebox". Origin: V-03 (client DM), V-11 and V-14 (two forum posts), V-17 (a comment on her own post) = 4 people, 3 places. The grid search for "shoebox" is recorded: no alternative uses it. Shown as "I picked 'Friday shoebox': four plumbers called their receipts 'the shoebox', in a forum, your DMs and your comments. Say 'change' for 'receipt Fridays'." SK1 2 · SK2 2 · SK3 2 · SK4 2 · SK5 1 · SK6 2 · SK7 2 · SK8 2 = 15/16. **Result: PASS.**

**FAIL.** VN, a coach for small flower-shop owners. Default: "hoa ế", origin listed as "V-02, V-05". V-05 is the coach's own recollection ("nhiều chủ tiệm nói vậy lắm", no named client), so it is coach recall: 1 person in 1 place, presented as proven. SK1 = 0. **Result: FAIL** (SK1: origin "V-02, V-05", with V-05 = coach recall).
