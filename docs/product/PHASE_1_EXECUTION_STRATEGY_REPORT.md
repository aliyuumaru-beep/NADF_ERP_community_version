# Phase 1 — Execution Strategy Report
## NADF ERP Programme — Post-WP-02 Planning

**Document ID:** PHASE1-ESR-001
**Phase:** 1 — Foundation
**Prepared by:** A1 Master Orchestrator
**Date:** 2026-06-25
**Status:** FINAL — for Business Sponsor review and A1 adoption

> **Purpose:** Define the optimal execution sequence, parallelisation model, and governance concurrency level for the remaining Phase 1 work packages: WP-03 (Procurement Core), WP-04 (HR Core), WP-ADM-01 (Administration), and WP-PC-01 (Project Coordination). No implementation is authorised by this document — it is a planning artefact only.

---

## 1. Phase 1 Remaining Work Summary

| WP | Title | Items (MH/SH/CH) | Blocked items | Est. complexity | Dependencies cleared? |
|----|-------|-----------------|--------------|----------------|----------------------|
| WP-03 | Procurement Core | 6 MH + 1 blocked | WP03-07 (B-02/B-03) | Medium | ✅ WP-01 complete |
| WP-04 | HR Core | 7 MH + 2 SH/CH | None | Low-Medium | ✅ WP-01 complete |
| WP-ADM-01 | Administration Core | 4 MH | None | Medium | ✅ WP-01 complete; helpdesk_mgmt installed |
| WP-PC-01 | Project Coordination | 3 MH + 1 SH | None | Low-Medium | ✅ WP-01 complete (soft dep on WP-ADM-01) |

**Also in scope (concurrent):**
- DEC-OCA-02 investigation (Option A) — parallel to WP-03/04 execution; minimal session overhead
- WP02-08 amendment — gated on client KPI sign-off; no action until client confirms

---

## 2. Dependency Map

### Hard dependencies (must be satisfied before starting)
```
WP-01 [DONE] ──┬──► WP-03 (purchase_request, purchase_requisition installed)
               ├──► WP-04 (hr, hr_holidays, hr_recruitment CE native)
               ├──► WP-ADM-01 (helpdesk_mgmt installed; fleet, account_asset CE)
               └──► WP-PC-01 (project CE native; user groups in place)
```

### Soft dependencies (preferred ordering, not strictly blocking)
```
WP-ADM-01 ──► WP-PC-01
```
Rationale: WP-PC-01 §9 implementation note requires legacy `project`-module ICT helpdesk tasks from Phase 8 to be reviewed/migrated after `helpdesk_mgmt` (WP-ADM-01) is configured. If WP-PC-01 runs before WP-ADM-01, the ICT helpdesk tasks remain in `project` and would clutter the PCU project view. This is low-risk but creates rework.

### Cross-WP interactions (no ordering dependency, but awareness needed)
| Interaction | Detail | Risk |
|------------|--------|------|
| WP-03 ↔ WP-02 | Procurement requisition → purchase order → vendor bill chain; analytic accounts from WP-02 must be applied to PO lines | Low — analytic accounts are in place; no WP-02 re-execution needed |
| WP-04 ↔ WP-03 | HR leave approval flow references `hr.employee` hierarchy; Procurement staff also appear in HR records | Low — parallel configuration; HR records already exist from Phase 8 |
| WP-ADM-01 ↔ WP-02 | Asset register depreciation entries post to `account.asset.asset` → `account.move`; CoA must be valid | Low — CoA validated in WP-02; depreciation account assignments must use NADF 8-digit codes |
| WP-ADM-01 ↔ WP-03 | Vehicle procurement and asset acquisition by PO are explicitly OUT OF SCOPE for WP-ADM-01 | No risk — scope boundary is clear |

### Blocked items (do not block WP execution but must be tracked)
| Item | WP | Blocker | Status |
|------|----|---------|--------|
| WP03-07 — Multi-level approval chain | WP-03 | Client confirmation B-02 (RACI step 1.19) and B-03 (approval thresholds) | BLOCKED — client action required before this item can be configured |
| WP02-07 — Budget control | WP-02 | DEC-OCA-02 | BLOCKED — under governance resolution |
| WP02-08 — mis_builder dashboard | WP-02 | Client KPI sign-off | DEFERRED — client action |

---

## 3. Options Analysis

### Option 1 — Sequential Execution

**Sequence:** WP-03 → WP-04 → WP-ADM-01 → WP-PC-01

**Description:** Execute each work package fully (implementation → PR → review → merge) before starting the next. Only one branch is active at any time. Each WP's PR is merged to `main` before the next WP branch is created.

| Factor | Assessment |
|--------|-----------|
| Branch management | Minimal — 1 branch at a time; no merge conflicts |
| Governance overhead | Minimal — 1 exit gate at a time; G1/G2/G3 can give full attention to each review |
| Session discipline | Simplest — no context switching between WPs mid-session |
| Velocity | Slowest — time spent waiting for PR review is idle time |
| Risk | Lowest — no cross-contamination between WPs |
| Total PR count | 4 additional PRs (PR #7, #8, #9, #10) |

**Estimated time-to-WP-05:** 4 complete execution cycles. If each cycle takes 1–2 sessions (execution + review), total elapsed time = 4–8 sessions.

**When to choose:** If governance review capacity is constrained, if configuration complexity is high, or if a WP failure must be fully diagnosed before continuing.

---

### Option 2 — Parallel Execution (Maximum Concurrency)

**Sequence:** WP-03 + WP-04 + WP-ADM-01 simultaneously; WP-PC-01 after WP-ADM-01 merges.

**Description:** Create three feature branches simultaneously. Execute all three WPs in the same session or across overlapping sessions. Raise three PRs simultaneously.

| Factor | Assessment |
|--------|-----------|
| Branch management | High complexity — 3 concurrent branches; merge conflicts possible if any WP touches shared config (user groups, analytic accounts, ir.config_parameter) |
| Governance overhead | Very high — G1/G2/G3 must review 3 exit gates simultaneously; risk of incomplete reviews |
| Session discipline | **Violates single-session constraint** — CLAUDE.md prohibits more than one Claude Code session at a time; true parallel execution requires a second session |
| Velocity | Theoretically fastest; in practice, session constraint means sequential execution with rapid switching |
| Risk | Medium-High — cross-WP configuration conflicts are possible; harder to diagnose which WP caused a regression |
| Governance compliance | **NOT RECOMMENDED** under current single-session governance |

**Why Option 2 is not viable:** The single-session constraint in CLAUDE.md (`Only one Claude Code session may be active at any time`) means that true parallel execution — two or more WPs being actively implemented simultaneously — is prohibited. Raising three PRs simultaneously is permissible, but executing three WPs in parallel is not.

---

### Option 3 — Hybrid Execution (Recommended)

**Description:** Execute WPs in two waves, exploiting the PR review window as an overlap buffer.

**Wave A:** WP-03 (execute) → PR #7 open → *while PR #7 awaits reviewer* → WP-04 (execute) → PR #8 open → *wait for both PRs to merge* → Wave B.

**Wave B:** WP-ADM-01 (execute on merged main) → PR #9 open → *while PR #9 awaits reviewer* → WP-PC-01 (execute) → PR #10 open → *wait for both PRs to merge*.

**After Wave B:** WP-05 UAT preparation.

```
Timeline (schematic):

Session 1:    [WP-03 execute] → PR #7 open
Session 2:    [WP-04 execute] → PR #8 open  (PR #7 in review simultaneously)
              |
              [PR #7 merged] [PR #8 merged]  (independent reviewer merges)
              |
Session 3:    [WP-ADM-01 execute] → PR #9 open
Session 4:    [WP-PC-01 execute] → PR #10 open  (PR #9 in review simultaneously)
              |
              [PR #9 merged] [PR #10 merged]
              |
Session 5:    [WP-05 UAT preparation]
```

| Factor | Assessment |
|--------|-----------|
| Branch management | Low-Medium — maximum 2 concurrent branches per wave; reviewer merges one while the other is being prepared |
| Governance overhead | Manageable — G1/G2/G3 review 1 exit gate at a time; second gate enters review while first is being processed |
| Session discipline | Compliant — single active session at all times; PR review happens out-of-session (independent reviewer) |
| Velocity | Near-optimal — PR review latency is recaptured by executing the next WP |
| Risk | Low — two branches per wave are unlikely to conflict; WP-03 and WP-04 touch different Odoo domains |
| WP ordering rationale | WP-03 first (higher complexity, client-blocked item WP03-07 needs early flagging); WP-04 second; WP-ADM-01 third (medium complexity); WP-PC-01 last (has soft dependency on WP-ADM-01) |

**Option 3 is recommended.**

---

## 4. WP-03 / WP-04 Ordering within Wave A

Within Wave A, WP-03 is executed before WP-04. Rationale:

1. **Complexity:** WP-03 (Procurement) is more technically involved than WP-04 (HR). Executing it first while the session is freshest reduces the risk of decisions being made under fatigue.

2. **Client-blocked item:** WP03-07 (multi-level approval chain) is blocked on client confirmation of B-02 and B-03. Beginning WP-03 first surfaces this blocker early and allows time for client response before WP-04 completes.

3. **OCA module involvement:** WP-03 exercises `purchase_request` (OCA) and `purchase_requisition` (CE). Both were installed under WP-01 but have not yet been configured. Confirming they are functional in a configured state before WP-04 (which uses only CE modules) is the prudent order.

4. **Procurement audit trail:** WP-03 also verifies `mail.thread` on `purchase.request` and `purchase.order` — an AC-14 requirement. Clearing this in WP-03 gives confidence that the audit trail pattern is consistent before WP-04 verifies it on HR models.

---

## 5. Governance Concurrency Assessment

**Question:** How many concurrent WPs can the Agent OS governance model safely support?

### Governance capacity factors

| Factor | Constraint |
|--------|-----------|
| Single-session rule | 1 active implementation session at a time |
| G1/G2/G3 review capacity | G1/G2/G3 are consolidated in A1 Orchestrator; each exit gate review takes ~30–45 min of session time |
| Branch protection | 1 independent reviewer approval required per PR; reviewer is out-of-session (human sponsor or designated reviewer) |
| PR review latency | Variable — dependent on human reviewer availability |
| Configuration conflict risk | Increases linearly with number of concurrent branches touching overlapping config |

### Concurrency levels assessed

| Level | Description | Assessment |
|-------|-------------|-----------|
| Level 1 — 1 active WP | Sequential: 1 WP executing, 0 in PR review | **Safe but slow** — recovers 0% of PR latency |
| Level 2 — 1 active + 1 in review | Hybrid Wave: 1 WP executing, 1 WP in PR review | **Safe and efficient** — recommended maximum |
| Level 3 — 1 active + 2 in review | 1 executing, 2 PRs open simultaneously | **Marginal** — review bottleneck; human reviewer overload risk; accept only if reviewer confirms capacity |
| Level 4 — 4 concurrent | All WPs simultaneously | **Not compliant** — single-session rule violated; configuration conflict risk unacceptable |

**Recommendation: Level 2 — maximum safe concurrency is 1 WP executing + 1 WP in independent PR review.**

This is the concurrency model embedded in Option 3 (Hybrid). It recovers the PR review latency window without violating single-session discipline or overwhelming G1/G2/G3 review capacity.

### Rationale for rejecting Level 3+

- The independent reviewer (human sponsor) should not be asked to review two PRs simultaneously. Rushed review increases the risk of accepting a regression.
- Two concurrent branches increase the probability of a merge conflict on `DECISION_LOG.md`, `CHANGELOG.md`, `MODULE_REGISTRY.md`, or `IMPLEMENTATION_HISTORY.md` — all of which every WP must update before PR.
- G1/G2/G3 exit gate consolidation (A1 is the consolidating agent) works cleanly for one review at a time; two concurrent exit gates risk cross-contamination of findings.

---

## 6. Recommended Execution Plan

### Wave A — Procurement + HR (Sessions 1–2 after PR #6 confirmed merged)

**Session 1:** Execute WP-03 Procurement Core
- Branch: `feat/wp-03-procurement-core`
- Go/No-Go: G1/G2/G3 confirm WP-01 exit gate PASS, `purchase_request` and `purchase_requisition` state='installed', branch clean
- Execute WP03-01..06 (WP03-07 remains blocked — document as BLOCKED in PR)
- Commit and open PR #7
- G1/G2/G3 exit gate review within same session

**Session 2:** Execute WP-04 HR Core (PR #7 in review)
- Branch: `feat/wp-04-hr-core`
- Go/No-Go: G1/G2/G3 confirm WP-01 exit gate PASS, branch clean (does NOT require PR #7 to be merged first — HR domain is independent of procurement config)
- Execute WP04-01..09
- Commit and open PR #8
- G1/G2/G3 exit gate review within same session
- *Note:* WP04-02 (department reassignment for 11 Administration staff) requires coordination with HR department — flag for client confirmation if needed

**After both PRs merged:** Verify `main` is clean before Wave B.

### Wave B — Administration + Project Coordination (Sessions 3–4)

**Session 3:** Execute WP-ADM-01 Administration Core
- Branch: `feat/wp-adm-01-administration-core`
- Go/No-Go: G1/G2/G3 confirm WP-01 exit gate PASS, `helpdesk_mgmt` state='installed', branch clean
- Execute BL-ADM-01..04 (note: Administration user groups already created in WP-01; BL-ADM-04 is a verification step)
- Document legacy `project`-based helpdesk workaround supersession (D-ADM01-07)
- Commit and open PR #9

**Session 4:** Execute WP-PC-01 Project Coordination (PR #9 in review)
- **Note:** WP-PC-01 branch should be based on the WP-ADM-01 branch HEAD (not `main`) if PR #9 has not merged yet, OR wait for PR #9 to merge before starting WP-PC-01.
  - Preferred: wait for PR #9 to merge, then branch from `main`. This avoids compound branches.
  - If PR #9 review is delayed, WP-PC-01 can begin after documenting the dependency in the PR description.
- Branch: `feat/wp-pc-01-project-coordination`
- Go/No-Go: G1/G2/G3 confirm `helpdesk_mgmt` configured (WP-ADM-01 done), WP-PC-01 user groups from WP-01 verified
- Execute BL-PC-01..04 (note: Project Coordination user groups already created in WP-01; BL-PC-04 is a verification step)
- Commit and open PR #10

### After Wave B — DEC-OCA-02 + WP-05

**Session 5 (or concurrent with Wave B PRs):**
- DEC-OCA-02 Option A investigation: check OCA/account-budgeting@17.0 for patch
- Begin WP-05 UAT preparation (test plan skeleton, UAT entry/exit criteria, defect register)
- WP02-08 amendment (if client KPI sign-off received)

---

## 7. Pre-execution Checklist (per WP)

Before each WP session begins, the following state must be confirmed:

| Check | WP-03 | WP-04 | WP-ADM-01 | WP-PC-01 |
|-------|-------|-------|-----------|---------|
| WP-01 exit gate PASS confirmed | ✅ (CONDITIONAL PASS accepted) | ✅ | ✅ | ✅ |
| WP-02 exit gate PASS confirmed | ✅ (CONDITIONAL PASS accepted) | ✅ | ✅ | ✅ |
| Relevant modules state='installed' | `purchase_request`, `purchase_requisition` | `hr`, `hr_holidays`, `hr_recruitment` (CE) | `helpdesk_mgmt`, `fleet`, `account_asset` (CE) | `project` (CE) |
| Single Claude Code session confirmed | Required | Required | Required | Required |
| Pre-WP backup taken | Required | Required | Required | Required |
| Working tree clean | Required | Required | Required | Required |
| Feature branch created | Required | Required | Required | Required |
| Go/No-Go: G1/G2/G3 confirmed | Required | Required | Required | Required |
| Client blockers noted in WP plan | WP03-07 (B-02/B-03) | WP04-02 (dept assignments), WP04-07 (leave types) | BL-ADM-01 (vehicle data) | BL-PC-01 (phase names) |

---

## 8. Risk Register (Execution Phase)

| Risk ID | Risk | L | I | WP affected | Mitigation |
|---------|------|---|---|------------|-----------|
| R-ESR-01 | WP-03 `purchase_request` multi-step workflow conflicts with existing CE `purchase` settings from Phase 3 legacy build | Med | Med | WP-03 | Review existing Purchase settings before configuration; document any overrides in DECISION_LOG.md |
| R-ESR-02 | WP-04 department reassignment (11 Administration staff) may require client HR data confirmation | Med | Low | WP-04 | Flag WP04-02 as client-action item; proceed with org hierarchy validation; do not force-reassign without client input |
| R-ESR-03 | WP-ADM-01 `account_asset` depreciation accounts must use NADF 8-digit CoA codes — wrong account assignment creates P&L errors | Low | High | WP-ADM-01 | Cross-reference `csv_templates/nadf_coa_revalidated_20260625.csv` before configuring depreciation accounts |
| R-ESR-04 | WP-PC-01 milestone `is_reached` restriction via `ir.rule` may not be possible without a write rule on `project.milestone` — CE limitation | Med | Med | WP-PC-01 | Test `ir.rule` approach on drill DB first; if not viable, document limitation and propose Phase 2 custom approach (no core modification) |
| R-ESR-05 | PR merge conflict on `DECISION_LOG.md` or `CHANGELOG.md` if two WP PRs are open simultaneously | Low | Low | All WPs | Use Wave A/B structure; PR #7 merged before PR #8 raised (if practical); resolve conflicts manually before merge |
| R-ESR-06 | Client blockers (B-02/B-03 for WP03-07; department data for WP04-02) delay Phase 1 UAT readiness | Med | Med | WP-03, WP-04 | Flag blockers at WP start; document as BLOCKED in PR; do not hold WP completion on client items if all other ACs pass |

---

## 9. A1 Master Orchestrator Recommendation

**Recommended execution model: Option 3 — Hybrid, two-wave, Level 2 concurrency.**

**Rationale:**
1. WP-03 and WP-04 are fully independent and have no shared Odoo domain. Wave A parallel execution (1 active + 1 in PR review) is safe and efficient.
2. WP-ADM-01 and WP-PC-01 have a soft dependency (helpdesk_mgmt migration of legacy project tasks). Wave B sequential execution (WP-ADM-01 → WP-PC-01) with the PR overlap buffer is the optimal balance.
3. Single-session discipline is maintained throughout. No concurrent Claude Code sessions are required or permitted.
4. Maximum safe concurrency: **Level 2** (1 executing + 1 in PR review). Level 3+ introduces reviewer overload and merge-conflict risk without meaningful velocity gain given the session constraint.
5. DEC-OCA-02 Option A investigation should run in the same session as WP-05 authoring (Wave B / Session 5), not as a blocking gate on Wave A.

**Execution sequence summary:**
```
[Now]         WP-02 exit gate report + DEC-OCA-02 review authored ✅
[Session 1]   WP-03 Procurement Core execute → PR #7
[Session 2]   WP-04 HR Core execute → PR #8  (while PR #7 reviewed)
              [PRs #7 + #8 merged]
[Session 3]   WP-ADM-01 Administration execute → PR #9
[Session 4]   WP-PC-01 Project Coordination execute → PR #10  (after/while PR #9 reviewed)
              [PRs #9 + #10 merged]
[Session 5]   DEC-OCA-02 Option A investigation + WP-05 UAT preparation
```

**Next immediate action:** User confirms PR #6 (`feat/wp-02-finance-core`) has merged. A1 will then begin WP-03 Procurement Core execution (Session 1, Wave A).

---

*Prepared by A1 Master Orchestrator. No implementation authorised by this document. Authority: PEG-6 approval 2026-06-24 · Transfer Package v2.1.*
