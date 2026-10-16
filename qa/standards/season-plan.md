# Season plan standard (`season-plan`)

Build-only rubric (wf12-qa-spec §3.1). Never shipped. It is the G3 judge rubric for the Season (domino) plan and the source of `standard = "season-plan"` eval cases.
Sources, in order: wf12-qa-spec §2.1, §3.1 (final, wins) · wf12-qa-critique #48 (correct by construction) · wf12-qa-standards §5 (draft) · arch-final-spec §5.5 (grid, ladder, phase mixes) · wf11 §2.3, §3.3, §4 rules 4–8 (pillars, CTA ladder, anti-dilution) · wf11-ux-spec §3.2 (Weekly Talk, never a zero week) · wf13 §3 (saved shapes per week) · DECISIONS (Weekly Talk is the default pillar).

## Purpose

Four Domino Weeks that move the belief chain forward each month and sweep all 4 rungs every week, so reach and trust are built before the ask.

What good means: every week has one belief step, one pillar format, the phase mix, ≥1 character piece, and ≥1 Trustable piece from Week 2. Every slot has one rung, one belief, a CTA matched to its rung and a link to the next domino. Each pillar belief gets ≥3 exposures per 30 days in ≥2 formats. Give:ask stays ≥3:1 over any 8 weeks. The plan fits the coach's volume tier, never has a zero week, and names every proof it needs.

## Scope

- **Artifact:** the Season plan: the header (phase, offer, keyword, Big Domino), the chain table, Weeks 1–4 and their slots (rung, B-ID, pillar P1–P3, format, CTA, link-forward, proof), and the monthly re-plan of the same.
- **Output class:** Structured artifact (spec §2.1), correct by construction. The build ships slot grids per volume tier (Lean, Standard, VA) and phase that satisfy SP1–SP5, SP7 and SP9; lint proves each grid at G1, and a grid that fails is a build blocker. At runtime the model only fills slots.
- **What the judge scores:** the filled plan: what went into each slot, and anything moved, dropped or added. A slot changed against the shipped grid with no logged coach request scores the affected [D] item 0.
- **Not here:** each slot's script (`shared.md` plus its format standard); launch calendars (`launch-assets.md`).

## Items

| ID | Item | 0 | 1 | 2 | Critical |
|---|---|---|---|---|---|
| SP1 | Chain moves forward [D] | No chain; beliefs invented; or the order reversed | One week out of chain order or under 60% on its pillar, or one belief untraced | B1–B7 run vehicle → internal → external across Weeks 1–4 (W1 B1–B2, W2 B3, W3 B4–B5, W4 B6–B7 + offer). Each week names its B-IDs and its pillar in order (W1 P1 → W2 P2 → W3 P3 → W4 all + offer), with ≥60% of its pieces on that pillar. Each false belief traces to a V or O row through the Map | yes |
| SP2 | All four rungs [D] | A week missing a rung (Trustable from Week 2), or slots with no rung or belief | One slot missing its link-forward, or one CTA one rung off | Every week has Admirable, Likable, Credible and Trustable pieces (Trustable from Week 2). Every slot has one rung, one B-ID, the ladder CTA for its rung and a link-forward | yes |
| SP3 | Funnel balance [D] | A bucket more than 20 points off the phase target; an Entertain piece that fails the Buyer Filter; a week from Week 2 with no bottom-of-funnel proof | One bucket 11–20 points off | Entertain/Educate/Convert within 10 points of the grid's phase target. Every Entertain piece passes the Buyer Filter at ≥2/3. From Week 2, every week carries bottom-of-funnel proof | yes |
| SP4 | Give:ask [D] | Below 3:1 in any rolling 8-week window | 3:1 holds, but one CTA bucket is more than 10 points off | ≥3:1 over any rolling 8 weeks. Monthly CTA mix about 60% contextual lead magnet / 20% direct offer / 20% DM trigger, each within 10 points | yes |
| SP5 | Repetition [D] | A pillar belief with fewer than 2 exposures in 30 days, or slots with no keyword | A belief at 3 exposures but in one format, or a week with no character piece | Each pillar belief gets ≥3 spaced exposures per 30 days in ≥2 formats (name it → make it personal → remind at the decision point). The keyword is in every slot. ≥1 character piece a week; character-led ≤20% | no |
| SP6 | Proof gate [D] | A hard direct-response ask while proof_gate is locked; a Trustable slot naming a P-ID whose consent doesn't cover that use; proof that doesn't exist | A NEEDS PROOF slot with no homework that unlocks it | Hard asks only when proof_gate is open. Each Trustable slot names a consented P-ID (consent covers the slot's use), process or founding proof, or NEEDS PROOF plus the homework that unlocks it (default: "ask 3 past clients one question") | yes |
| SP7 | Fits capacity [D] | More slots than the tier holds, or a zero week | Two homework items, one over 10 minutes, or no talk day set | Slots match the volume tier. One pillar a week: the Weekly Talk by default, the filmed pillar opt-in, with the mini-talk for a busy week, so no week is zero. ≤1 homework item of ≤10 minutes. Talk or record day set | no |
| SP8 | Series links | No series, markers or link-forward | Series named, but markers or next-domino pointers missing; or two keywords or assets in one Season | 2 named recurring shows. Series markers ("Part N"). Each piece points to the next domino or the pillar. One keyword and one real A-row per Season (a second asset only at re-plan) | no |
| SP9 | Variation [D] | One format all week, or a format three times in a row | Two formats a week, or two planned hook stems repeat | ≥3 formats a week; no format more than twice in a row; planned hook stems distinct. Saved liked-post shapes: ≤1 a week on Lean, ≤2 on Standard/VA, native slots only | no |
| SP10 | Traceable | An invented source, or a NOT NOW topic as a slot's main idea | One slot untraced and unlabelled, or an off-map slot not tagged | Every slot cites its source IDs (B-ID, pillar, S/V/P/R) or is marked [guess]. 100% of planned slots carry P1–P3. Off-map only on the coach's request, ≤1 in 10, tagged Off-map | no |

**Phase targets (Ent/Edu/Conv, arch §5.5):** audience-building 40/45/15 · steady 30/50/20 · launch runway 20/30/50. PLAN caps entertainment at 20–30%; that conflict is the founder's to settle. The shipped grid holds the number in force, and the judge scores against the grid.

**CTA ladder:** Admirable = follow · Likable = send to a friend · Credible = save, or comment the keyword (the default) · Trustable = DM the keyword, or book. A give is a follow, send, save or keyword-for-an-asset CTA; an ask is buy, book, offer or a launch direct-response CTA.

## Build pass rule

- **Shared rule:** every critical item scores 2; total ≥ ceil(0.8 × max), N/A removed from the max; hard gates clear; no conditional pass; uncertain = 0.
- **Here:** SP1, SP2, SP3, SP4 and SP6 score 2, and the total is ≥16/20.
- Rolling ratios and mixes are counted in code (G1 on the grid, `graders.py` on the fill), never by the judge's estimate.
- The monthly re-plan is re-scored the same way. A pillar's angle may change at re-plan; its belief may not (wf11 rule 4).
- An honest shortfall passes: a Trustable slot written as NEEDS PROOF with its homework is a 2 on SP6. A slot filled with proof that doesn't exist is a 0.

## Hard gates

- A slot that plans a hard stop: invented proof, a testimonial or result with no consented P-row, an urgency slot with no 4-yes Ledger row.
- A 4th pillar. Character pieces are how a pillar gets said, not a pillar.
- Codes in coach text: the plan the coach sees is in plain words, with no B-IDs, rung names or rubric codes outside paste blocks (I4).
- **Never blocked:** the coach's comment-keyword CTA in any slot; an off-map piece the coach insists on (written, tagged Off-map, counted against the ≤1 in 10).

## Runtime check shipped

`core/format-checks.toml`:

```toml
[format.season-plan]
checks = [
  "Did I fill the shipped grid for this tier and phase without moving, dropping or adding slots?",
  "Does each Trustable slot name a consented P-ID, process or founding proof, or NEEDS PROOF?",
  "Does each slot carry one pillar, one belief, the keyword and its rung's CTA, with nothing from NOT NOW as its main idea?",
  "Does every slot cite its source, or carry [guess]?",
]
checks_vn = [
  "Mình điền đúng khung dựng sẵn cho gói và giai đoạn này, không dời, bỏ hay thêm ô nào?",
  "Mỗi ô Trustable có ghi dòng P đã được đồng ý, bằng chứng quy trình hoặc founding, hoặc [CẦN BẠN]?",
  "Mỗi ô có 1 trụ, 1 niềm tin, từ khoá và CTA đúng nấc, không lấy chủ đề ĐỂ SAU làm ý chính?",
  "Mỗi ô đều dẫn nguồn, hoặc gắn [guess]?",
]
```

## VN note

- Default platforms: Facebook profile (professional mode) and Groups, TikTok for reach, Zalo to close, YouTube for long-form. The private track runs on Zalo.
- CTA wording uses "nhắn / inbox / comment từ khoá". The series marker is "Phần N".
- The seasonal overlay (Tết; tháng cô hồn = no launches; 8/3, 20/10, 20/11) applies only once the `seasonal_overlay` key is filled. While it is PENDING, there is no overlay.
- Xưng hô in slot text follows the Card.

## Calibration (fictional coaches)

**PASS.** EN, a bookkeeping coach for solo plumbers. Lean, Season 1, audience-building, Weekly Talk on Mondays. W1 P1 "Receipts aren't the problem; April is" (B1–B2), W2 P2 the Friday Shoebox method (B3), W3 P3 "I can, even with a van full of paper" (B4–B5), W4 all + the founding offer. W2's Trustable slot names "founding proof: cohort 1, first 5 plumbers"; W3's names P-02 (consent: posts). Give:ask 4:1. SP1 2 · SP2 2 · SP3 2 · SP4 2 · SP5 2 · SP6 2 · SP7 2 · SP8 1 (one named show) · SP9 2 · SP10 2 = 19/20. **Result: PASS.**

**FAIL.** VN, a coach for small flower-shop owners (mình–bạn), Standard. W2's Trustable slot reads "Mở đăng ký gói Tiệm Hoa Có Khách Quen 2.990.000đ, inbox HOA Ế để giữ chỗ" while proof_gate is locked: no consented P-row, no founding framing. SP6 = 0. The 17/20 total does not matter. **Result: FAIL** (SP6: "Mở đăng ký gói Tiệm Hoa Có Khách Quen 2.990.000đ, inbox HOA Ế để giữ chỗ").
