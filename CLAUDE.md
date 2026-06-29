# CLAUDE.md — POD-NADF Agent Operating Rules

Project-specific instructions for any Claude Code / Software Factory agent working in `nadf_erp`. Inherits the Software Factory Governance and Product Engineering Framework v1.1; the rules below extend them for this deployment.

## Identity & layer
- **Pod:** POD-NADF · **Layer:** Layer 4 — Client Deployment. This repo owns NADF-specific config, custom modules, master data, and its own governance docs. It must **never** contain logic belonging to Platform (Layer 2) or Template (Layer 3), and **never** another client's assets (the M-C incident was a NADF module mis-located in `famoil-erp` — do not reintroduce cross-contamination).
- **Do not modify the FamOil (`/Users/mac/odoo17` → famoil-erp) or WamaCare repositories** except where an explicit, logged cross-pod remediation is authorised.

## Platform (hard constraints)
- **Odoo 17 Community Edition only.** Enterprise modules are **prohibited**: `web_studio`, `sign`, `documents`, `documents_spreadsheet`, `knowledge`, `hr_payroll` (EE), `helpdesk` (EE), `industry_fsm`, `account_accountant`.
- Approach order: **Native CE → Configuration → OCA (vetted, version-pinned) → existing SF modules → Custom module.** Core modification is prohibited unless escalated and logged.
- DB `NADF`, port `8071`. Interpreter with Odoo deps: `/Users/mac/odoo17/odoo/venv/bin/python`. Module source of truth: `nadf_erp/custom_addons/` (on `addons_path` in `nadf.conf`).

## Authority
1. `requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md` (bound — load at session start)
2. `planning/PRODUCT_SCOPE.md` → `planning/ROADMAP.md` → `planning/BACKLOG.md` → `planning/WORK_PACKAGES.md`
- The quarantined scaffold zip in `docs/imports/` is **non-authoritative** — never extract or cite it.

## Working rules
- **No spec, no code.** Custom modules require an approved design spec (Phase 2) before development.
- **No build of an unspecified department** — department Odoo builds are gated on TO-BE delivery.
- BPOGS/swimlanes are **requirements-source history only**, not implementation work.
- Every change: feature branch → commit (`type(scope): desc`) → PR → review → merge into protected `main`. Do not push directly to `main`.
- Update the governance docs that a change touches **before** the PR is complete: `DECISION_LOG.md`, `MODULE_REGISTRY.md`, `IMPLEMENTATION_HISTORY.md`, `CHANGELOG.md`, `RISK_REGISTER.md`, `PROJECT_STATE.md`.
- **Never** mutate the live `NADF` database for verification — use `--stop-after-init` for load checks and `restore_nadf.sh` (drill DB) for restore tests. Take a backup before any schema/data-mutating operation.

## Session protocol
Follow `docs/PRODUCT_STATE_INDEX.md`: read `docs/NEXT_ACTION.md` → `PROJECT_STATE.md` → `MILESTONE_TRACKER.md` → `planning/BACKLOG.md` → `docs/governance/GOVERNANCE_APPROVAL_REGISTER.md` (open escalations + deferred decisions) → `git status` at start; update state docs and commit at end.

## Governance Approval Register (AOP-015)
`docs/governance/GOVERNANCE_APPROVAL_REGISTER.md` (GAR-NADF-001) is a **mandatory governance artifact**. Read it at session start to understand open escalations, deferred decisions, and active exceptions. Update it as a mandatory acceptance criterion on every Work Package Exit Gate before closing the gate. Never close a Work Package without confirming the register is current.

## Milestone closure
A milestone closes only when its Work Packages are closed, G1/G2/G3 governance reviews pass, docs are complete, and (for production) a human sponsor approves. Until then, work is tracked **built / unratified**, never "closed."
