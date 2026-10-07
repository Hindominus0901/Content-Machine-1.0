# Research corpus

This folder holds everything researched and designed before the build started, all dated 5 Oct 2026. Modules, evals and QA rubrics are written from these files.

## Which file wins

When files disagree, the higher item wins:

1. [`../DECISIONS.md`](../DECISIONS.md): the founder's decisions.
2. `wf11-ux-spec.md`: the final UX. It replaces the install and first session in the architecture spec.
3. `wf12-qa-spec.md`: the final QA system.
4. `arch-final-spec.md`: the final architecture.
5. Everything else: the research briefs and design drafts behind those specs.

Conflicts already resolved are listed under "Reconciliations" in [`../PLAN.md`](../PLAN.md).

**Founder sources.** [`founder-sources.md`](founder-sources.md) digests the transcripts and screenshots the founder shared. It outranks web research where they conflict.

## Final specs

| File | What it settles |
|---|---|
| `wf11-ux-spec.md` | Install (Project kit, Door B, helper path), Day 0 minute by minute, Weekly Talk, level-ups L0.5–L5, the 5 phrases, what the coach never sees, persona acceptance criteria |
| `wf11-message-focus.md` | The Message Focus Engine: one message, ≤3 big ideas, NOT NOW, the 6 message tests |
| `wf12-qa-spec.md` | QA in four layers: the runtime Ship Check card and verdict lines, the standards, the coach checklists, build gates G0–G9 and invariants I1–I18 |
| `arch-final-spec.md` | Source tree, modules, schemas (Brand Brain/Bank/hub), automations, the quality system, bilingual strategy, phases, risks |
| `wf7-research-module-spec.md` | The research module R0–R8, ported from the founder's agency protocol |
| `wf10-access-modes-design.md` | Research access modes: Search, Browse-Claude, Browse-ChatGPT, Deep research, Paste. Includes the batch prompts |
| `wf6-character-design.md` | Character Core interview, Character Card, character formats, Edge Check v2 |
| `wf5-launch-design.md` | Launch types A–D, phases P0–P9, launch math, Scarcity Ledger, calendars, launch mode |
| `wf9-entertainment-catalog.md` | 24 entertainment/POV formats (E01–E24), EN + VN |
| `wf8-mattgray-playbook.md` | Packaging and hook library. Ship it renamed; never use his framework names |
| `wf2-synthesis.md` | Reference-creator synthesis, the Domino Series unit, VN edition requirements |
| `wf3-recommendation.md` | Hub (Notion + Sheets Lite) and the 3 automations |

## Supporting files

| Group | Files |
|---|---|
| UX drafts, facts and persona walkthroughs | `wf11-ux-design-concierge.md`, `wf11-ux-design-zero-setup.md`, `wf11-ux-design-guided-project.md`, `wf11-ux-facts.md`, `wf11-walkthrough-1.md` (chị Hạnh), `wf11-walkthrough-2.md` (anh Tuấn), `wf11-walkthrough-3.md` (Linda) |
| QA drafts | `wf12-qa-runtime.md`, `wf12-qa-standards.md`, `wf12-qa-build.md`, `wf12-qa-critique.md` |
| Architecture panel | `arch-proposal-robustness.md` (the base), `arch-proposal-coach-ux.md`, `arch-proposal-outcomes.md`, `arch-judgments.json` |
| Research module | `wf7-research-port.md`, `wf7-source-map.md`, `wf10-chatgpt-computer-use.md`, `wf10-claude-computer-use.md` |
| Character | `wf6-character-polarity.md`, `wf6-definitive-concise.md` |
| Launch | `wf5-launch-frameworks.md`, `wf5-vietnam-launch.md` |
| Matt Gray sweep | `wf8-mattgray-youtube.md`, `wf8-mattgray-linkedin-x.md`, `wf8-mattgray-newsletter-leadmagnets.md`, `wf8-mattgray-instagram.md` |
| Strategy references | `strategy-coverage.md`: every Soo Wei Goh and Matt Gray idea and where it lives in the machine (7 Oct 2026) |
| Entertainment scouts | `wf9-pov-global.md`, `wf9-pov-vietnam.md` |
| Reference creators + VN market | `wf2-gadzhi-morgan.md`, `wf2-robthebank-niksetting.md`, `wf2-sooweigoh-luebben.md`, `wf2-suby-hormozi.md`, `wf2-houseofag-gentlerainman.md`, `wf2-vietnam-market.md` |
| Hub + automations | `wf3-content-hub.md`, `wf3-scheduled-tasks.md` |
| First-round briefs | `wf1-packaging.md`, `wf1-gaps.md`, `wf1-educational.md`, `wf1-entertainment.md`, `wf1-converting.md`, `wf1-series-trust.md`, `wf1-research-ideation.md` |

## Rules for using this corpus

- **Platform facts go stale.** Any limit or behaviour quoted here is copied into `platform/targets.toml` with a `verified_on` date. Shipped text never cites it from here.
- **Personas in walkthroughs and examples are fictional.**
- **Never ship Matt Gray's framework names** (Content Waterfall, Content GPS, 4-3-2-1, Authenticity Machine, Founder OS). Never copy his inflated value math or his fake scarcity.
