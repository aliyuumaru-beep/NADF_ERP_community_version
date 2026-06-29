# PRODUCT_STATE_INDEX.md — POD-NADF

**Document type:** Product Memory index + session protocol (PEF v1.1 Product Memory System; Gate C7)
**Closes:** `BL-GOV-09` (document session start and end rules in-repo)
**Created:** 2026-06-23 (Migration Sequence M-D) · **Maintained by:** A1 Software Factory Orchestrator

This file is the entry index to POD-NADF state and the **binding session protocol**. It exists so any future session can cold-start from the repository alone, without the transfer package loaded.

---

## 1. State index — where the truth lives

| Concern | Authoritative file |
|---------|--------------------|
| Bound product authority | `requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md` |
| Current status / cockpit | `PROJECT_STATE.md` |
| Next action | `docs/NEXT_ACTION.md` |
| Milestones | `MILESTONE_TRACKER.md` |
| Scope / roadmap / backlog / work packages | `planning/PRODUCT_SCOPE.md`, `planning/ROADMAP.md`, `planning/BACKLOG.md`, `planning/WORK_PACKAGES.md` |
| Decisions | `docs/DECISION_LOG.md` |
| Risks | `RISK_REGISTER.md` |
| Modules | `MODULE_REGISTRY.md` |
| History / changes | `IMPLEMENTATION_HISTORY.md`, `CHANGELOG.md` |
| Backup / recovery | `docs/BACKUP_STRATEGY.md` |
| Gate status | `docs/GOVERNANCE_GATE_REPORT.md` |
| Agent operating rules | `CLAUDE.md` |

## 2. Session START protocol (read in this order)
1. `docs/NEXT_ACTION.md` — what to do next.
2. `PROJECT_STATE.md` — current milestone, blockers, risks, open escalations.
3. `MILESTONE_TRACKER.md` — milestone/gate state.
4. `planning/BACKLOG.md` — current work item and its acceptance criteria.
5. `git status` + current branch — confirm a clean, expected working tree.
6. Confirm platform constraints in `CLAUDE.md` (Odoo 17 CE; no Enterprise; layer boundaries).

## 3. Session END protocol
1. Update every governance doc the work touched (`PROJECT_STATE`, `DECISION_LOG`, `RISK_REGISTER`, `MODULE_REGISTRY`, `IMPLEMENTATION_HISTORY`, `CHANGELOG` as applicable).
2. Refresh `docs/NEXT_ACTION.md` to point at the next action.
3. Commit on a feature branch with a `type(scope): desc` message; open/update a PR into protected `main`. **Never push directly to `main`.**
4. If the live `NADF` DB or schema was changed, confirm a backup exists first and record any `RESTORE_EVENT`/`BACKUP` in `IMPLEMENTATION_HISTORY.md`.
5. Leave the working tree clean.

## 4. Guardrails (always)
- No ERP build of an unspecified department; no custom module without an approved spec.
- No Enterprise modules; no core modification without escalation.
- No cross-pod contamination (NADF assets stay in `nadf_erp`).
- BPOGS/swimlanes are requirements history only.

---

## 5. Programme Checkpoint — Wave A Complete / Wave B Active (2026-06-26)

**Wave A status:** CLOSED  
**Wave B status:** WP-ADM-01 CONDITIONAL PASS (Session 3) · WP-PC-01 NEXT (Session 4)

| Work Package | Wave | Status | PR |
|-------------|------|--------|----|
| WP-01 Foundation Hardening | Pre-wave | CONDITIONAL PASS | #5 (merged `93551ba`) |
| WP-02 Finance Core | Pre-wave | CONDITIONAL PASS | #6 (merged `e58e15c`) |
| WP-03 Procurement Core | Wave A · Session 1 | CONDITIONAL PASS | #8 (merged `be7ed8b`) |
| WP-04 HR Core | Wave A · Session 2 | CONDITIONAL PASS | #10 (open) |
| **WP-ADM-01 Administration Core** | **Wave B · Session 3** | **CONDITIONAL PASS** | **#11 (this branch — pending)** |
| WP-PC-01 Project Coordination | Wave B · Session 4 | NOT STARTED | — |

**M1 — Foundation milestone:** NOT ACHIEVED  
M1 requires WP-ADM-01 + WP-PC-01 PASS + WP-05 UAT prep + DEC-OCA-02 resolution + client CoA sign-off.  
Re-assess at Wave B close.

**Authoritative Wave A completion record:** `docs/governance/WAVE_A_COMPLETION_REPORT.md`  
**Governance register:** `docs/governance/GOVERNANCE_APPROVAL_REGISTER.md` (mandatory — read at session start)  
**Open PRs:** #11 (WP-ADM-01 — this branch)  
**Active branch for next session:** `feat/wp-pc-01-project-coordination`  
**main:** `5e3861e`
