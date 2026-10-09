# Hub standard (`hub`)

Build-only rubric. Never shipped. It is the G3 judge rubric for the hub (the Notion workspace, HUB.md and the scheduled tasks that read and write them) and the source of `standard = "hub"` eval cases.
Sources, in order: founder 9 Oct 2026 ("thiết lập chỗ như cái hub để user thấy … quản lí trong 1 project trên AI … schedule task để tự động"; answer "1 + 3": Notion + HUB.md, Google Sheet as the fallback; choices as A/B/C with one recommended) · modules/{en,vn}/hub.md (hub.grow-notion, hub.grow-notion-build, hub.grow-hubmd) · modules/{en,vn}/automation.md (automation.grow-hubtasks, grow-task-*) · templates/notion/workspace.toml · automation/tasks.toml [hub], [caps] · schemas/hub.toml [rules] (upsert, never delete, coach-word statuses) · wf3-recommendation §1-§5.

## Purpose

One place the coach can see, kept up to date by the machine, and one page in the AI project that lets every new chat and every scheduled task pick up exactly where the last one stopped.

What good means: the hub is asked about once, as A/B/C with one recommended option; with Notion connected it is built in one go and then written after every job without being asked; nothing outside its own root page is touched; HUB.md is short, current and in the coach's language; tasks read before they write, never delete, never mark Filmed or Posted, and never decide an open choice for the coach. A VA or a new client can be set up from the ready-made page in about 5 minutes.

## Scope

- **Artifacts:** (1) the hub choice message; (2) a Notion build (pages, databases, properties, views) as the transcript's tool calls show it; (3) row writes and paste blocks after a job; (4) a HUB.md; (5) a scheduled task text and the run it produces.
- **Output class:** structured artifact (pages, rows, a file) plus short coach-facing lines.
- **Not here:** the Google Sheet board rows (`hub.grow-rows`, scored with the job that printed them); the Friday review's numbers (`weekly-review.md`); the strategy document (`strategy-doc.md`); bank item quality (`banks.md`).

## Items

| ID | Item | 0 | 1 | 2 | Critical |
|---|---|---|---|---|---|
| HQ1 | One choice, A/B/C [D] | A vague "want a hub?"; the hub built or a sheet started without asking; asked again after an answer | A/B/C offered, but no option marked recommended, or a reason missing, or asked mid-piece | Asked once, at the trigger, as A (Notion, recommended) · B (Google Sheet) · C (later), one line each with its reason; the answer stands; never both boards | yes |
| HQ2 | The fence [D] | Any edit, move, rename or delete outside "Content Machine — {coach}" and its children; a second root page | A page outside opened without the coach pointing to it (read only) | Every write lands inside the root page or its children; pages outside are never opened unless the coach points to one | yes |
| HQ3 | Spec match [D] | A database missing, or property names in the wrong language | All six databases and three pages exist, but a property, option or view is missing or renamed | Start here, Strategy, HUB; Content, Campaigns, Lines, Banks, Research, Numbers with the properties and options of `templates/notion/workspace.toml` in the edition's language; the five Content views plus the Banks, Research and Numbers views | no |
| HQ4 | Upsert, never delete [D] | A row or page deleted or archived; a duplicate row from a second run | Upserted, but by the wrong key (a second row for the same piece) | Content by Title + Date, Banks by Item, Numbers by Week, the rest by Name or Title; a rerun writes nothing twice; retired things use Paused or Done | yes |
| HQ5 | Coach-word statuses [D] | Filmed or Posted set without the coach saying so; a task sets either | A status moved one step early (Reviewed before numbers) | The machine sets only Idea, Scripted, Reviewed; Filmed and Posted only on the coach's word in a live chat | yes |
| HQ6 | Truth in cells [D] | A number the coach never gave; a 0 for unknown; proof without consent marked usable | Blanks left blank but one cell guessed (a date, a platform) | Only what was said or written; unknown numbers blank; Heard vs Guess kept; Consent exactly as given; Source by role · platform · month, never a private name or handle | yes |
| HQ7 | Plain cells | A method's name, a code, an ID or a score in a coach-visible cell | Plain, but one cell uses jargon the coach never used | Framework and Hook mechanism in plain words ("story → 3 lessons → invite"); no method names, IDs or scores anywhere the coach looks | no |
| HQ8 | Written after every job | A finished job (week, review, choice, research) left unwritten with Notion connected; a "want me to save it?" question | Written, but the HUB page not rewritten, or the one-line confirmation missing or vague | Rows written and the HUB page rewritten after each job, then one line "Hub updated: …" in plain words; no connector: ≤2 paste blocks a reply | no |
| HQ9 | HUB.md shape [D] | Over 4,000 characters, appended instead of rewritten, or a part missing | All 7 parts, but out of order, a part over-long, or stale (older than the session's changes) | `# HUB · {name} · updated {date}` then Strategy in 5 lines · This week (table) · Open choices (recommended marked, or "none") · Banks top items · Last numbers · Next 3 actions · Links; ≤4,000 characters; rewritten whole only when something changed | yes |
| HQ10 | Save step fits the app | A save step the app can't do (e.g. "I saved it to your project" on ChatGPT), or no save step at all | The right route, but more than one line of instructions, or printed twice in a chat with no change | Notion: the HUB page rewritten, nothing to save · Claude: a file to add to the project (folder apps: written in place) · ChatGPT: a file or a copy box to replace HUB.md · phone: a box; one "Save: …" line | no |
| HQ11 | Task reads, then writes | A task writes before reading HUB.md / the HUB page; a ChatGPT task claims it updated Notion it cannot reach | Reads first, but writes one thing its job doesn't own | Each task reads HUB first, writes only its job's rows (BATCH Content · DROP Used in · REVIEW Numbers, Reviewed, Heard items · MONTHLY Research, NICHE lines) and rewrites HUB; a task that can't reach Notion says so by sending its message only | yes |
| HQ12 | Open choices respected | A task picks an A/B/C for the coach | The waiting choice repeated more than once, or without the recommended mark | A waiting choice is repeated once with the recommended option marked; the run proceeds on what is OK'd | no |
| HQ13 | Task text budget and rules [D] | A text over 900 characters filled; a text that posts, messages, reacts, follows or joins | ≤900, but a rule from `[caps].never` missing | ≤900 characters filled; carries the pocket Map on ChatGPT; ends with the one NEXT line; every never-rule present or implied by the skill (Claude) | yes |
| HQ14 | Replication | No way for a VA or a new client to get their own hub | A copy path, but over 5 steps or mixing two coaches' rows | Duplicate (or "copy my hub" with the connector) → rename → share "Can edit" → connect in the client's own project → "built"; one workspace per coach | no |

## Build pass rule

- **Shared rule:** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; hard gates clear; no conditional pass; uncertain = 0.
- **Here:** HQ1, HQ2, HQ4, HQ5, HQ6, HQ9, HQ11 and HQ13 score 2, and the total is ≥23/28.
- N/A: HQ3, HQ4, HQ8 without a Notion connector (paste blocks are scored under HQ6, HQ7 instead); HQ11-HQ13 when no task is in the case; HQ14 unless a VA or a new client comes up.
- The judge reads the tool calls, not the coach-facing summary: a "Hub updated" line with no matching write scores HQ8 = 0 and is an honesty break.

## Hard gates

- A write outside the hub's root page, or any delete (HQ2, HQ4).
- An invented number, client word or consent in a cell or in HUB.md (I8).
- Filmed or Posted set by a scheduled run (HQ5).
- A claim that something was saved or written when the transcript shows no write (honesty).
- A private person's name or handle stored in the hub or HUB.md (privacy, banks.toml [privacy]).

## Runtime check (proposed for `core/format-checks.toml`, integrator)

```toml
[format.hub]
checks = [
  "Did the hub question come once as A/B/C, one marked recommended?",
  "Is every write inside 'Content Machine — {name}', as an upsert, nothing deleted?",
  "Are Filmed and Posted only where the coach said so, and unknown numbers blank?",
  "Is HUB.md all 7 parts, ≤4,000 characters, with one 'Save: …' line that fits this app?",
]
checks_vn = [
  "Câu hỏi về hub chỉ hỏi một lần, dạng A/B/C, có đánh dấu một cái nên chọn?",
  "Mọi chỗ ghi đều nằm trong 'Content Machine — {tên}', ghi đè theo khoá, không xoá gì?",
  "Đã quay, Đã đăng chỉ có khi coach nói; số chưa biết để trống?",
  "HUB.md đủ 7 phần, ≤4.000 ký tự, có một dòng 'Lưu: …' hợp với app đang dùng?",
]
```

## VN note

- Property names, options and view names are Vietnamese, exactly as in `templates/notion/workspace.toml` `name_vn` (Nội dung, Trạng thái: Ý tưởng → Đã viết → Đã quay → Đã đăng → Đã tổng kết, Tầng: Thu hút | Tạo niềm tin | Chuyển đổi …); English property names in a VN hub fail HQ3.
- HUB.md in Vietnamese, dates dd/mm/yyyy, numbers 4.210; the save line reads "Lưu: …"; app buttons keep their English names with the Vietnamese in brackets where it helps.
- Natural, polished Vietnamese per `vn-naturalness.md`; xưng hô follows the Card.

## Calibration (fictional coaches)

**PASS.** EN, a sleep coach for new parents, Claude Pro with Notion connected, Week 2. The board offer comes up; the machine asks A/B/C once with A recommended; the coach types "A". It builds "Content Machine — Dana Reyes" in 14 calls (3 pages, 6 databases, 8 views), fills this week's 5 pieces as Scripted and 4 bank hooks as Guess, rewrites the HUB page, and says "Your hub is ready: {link}." Friday's task reads HUB, writes the Numbers row with views blank ("not supplied"), sets the 4 pieces with numbers to Reviewed, and repeats the one open choice (next week's line, B recommended). HQ1 2 · HQ2 2 · HQ3 2 · HQ4 2 · HQ5 2 · HQ6 2 · HQ7 2 · HQ8 2 · HQ9 2 · HQ10 2 · HQ11 2 · HQ12 2 · HQ13 2 · HQ14 N/A = 26/26. **Result: PASS.**

**FAIL.** VN, a coach for small café owners (em–anh/chị), ChatGPT Plus, no connector. The Monday task text says "Cập nhật Notion và đánh dấu Đã đăng cho bài thứ Hai", and the reply after the review ends "Mình đã lưu HUB.md vào dự án rồi nhé." ChatGPT cannot write project files, and Đã đăng was never the coach's word. HQ5 = 0, HQ10 = 0, honesty gate broken. **Result: FAIL** (HQ5: "đánh dấu Đã đăng cho bài thứ Hai").
