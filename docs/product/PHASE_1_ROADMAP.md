# Phase 1 — Foundation Roadmap
## NADF ERP Programme

**Document type:** Phase planning — execution roadmap
**Phase:** 1 — Foundation
**Authority:** `requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md` (frozen at PEG-6 approval 2026-06-24)
**Prepared by:** A1 Master Orchestrator · D1 Functional Architect
**Date:** 2026-06-24
**Status:** PLANNING — Governance layer (G1/G2/G3) must activate before any implementation

---

## Activation Sequence (mandatory order)

```
PEG-6 APPROVED ✅ (2026-06-24)
        │
        ▼
GOVERNANCE LAYER activates first
  G1 Architecture & Odoo Governance
  G2 Quality & Documentation Governance
  G3 Security & Change Governance
        │
        ▼
  WP-01 Go/No-Go checkpoint (G1/G2/G3 review)
        │
        ▼
DELIVERY LAYER activates (only after G-layer active)
  D1 Functional Architect
  D2 Solution Builder
  D3 QA & Validation
  D4 Knowledge & Documentation
        │
        ▼
  WP-01 → WP-02 → WP-03 → WP-04 → WP-05
```

---

## Work Package Sequence

| Seq | WP | Title | Complexity | Key dependency | Output |
|-----|----|-------|-----------|----------------|--------|
| 1 | WP-01 | Foundation Hardening | Medium | G-layer Go/No-Go | OCA modules installed; security baseline; Odoo verified |
| 2 | WP-02 | Finance Core | Large | WP-01 complete | CoA, bills, payments, budget, `mis_builder` dashboard |
| 3 | WP-03 | Procurement Core | Large | WP-01 complete | Vendor, requisition, RFQ, goods receipt (approval chain deferred) |
| 4 | WP-04 | HR Core | Large | WP-01 complete | Employees, leave, recruitment, appointment approval |
| 5 | WP-05 | UAT Preparation | Medium | WP-02/03/04 complete | Test plan, defect register, UAT readiness checklist |

WP-02, WP-03, and WP-04 may run concurrently after WP-01 completes. WP-05 requires WP-02/03/04 all complete.

---

## Deliverables per Milestone Gate

### WP-01 Exit Gate (G1/G2/G3 review required)
- [ ] Five OCA modules installed, version-pinned, Decision Log entries present
- [ ] Pre-work backup taken within 24h of first mutating operation
- [ ] Baseline security groups created; TOTP 2FA active for Finance + Senior Mgmt
- [ ] `odoo-bin --stop-after-init` exit 0 after OCA install
- [ ] Single Claude Code session confirmed; working tree clean

### WP-02 Exit Gate (G1/G2/G3 review required)
- [ ] CoA re-validated and exported as reference CSV; client review recorded
- [ ] Vendor-bill workflow: draft → confirmed → posted
- [ ] Payment dual-authorisation tested with two user accounts
- [ ] Trial balance, P&L, balance sheet rendering
- [ ] `mis_builder` dashboard KPIs — client sign-off on KPI set
- [ ] Budget control active against analytic accounts
- [ ] `mail.thread` audit verified on Finance records

### WP-03 Exit Gate (G1/G2/G3 review required)
- [ ] Vendor compliance-status field on `res.partner`
- [ ] `purchase_request` multi-step requisition workflow active
- [ ] RFQ and tender workflow active
- [ ] Goods receipt / stock flow confirmed
- [ ] DEC-CONTRACT-001 logged
- [ ] Audit trail on Procurement records
- [ ] Approval chain status documented (blocked / unblocked)

### WP-04 Exit Gate (G1/G2/G3 review required)
- [ ] 4-level org hierarchy (MD → Director → Manager → Officer)
- [ ] Leave workflow (line manager → HR two-level) verified
- [ ] Recruitment pipeline stages active
- [ ] Appointment/separation approval + CEO notification
- [ ] HR user groups; audit trail on HR records
- [ ] Client review of leave types + org hierarchy recorded

### WP-05 Exit Gate (G2 review required)
- [ ] UAT test plan with one case per Phase 1 AC (AC-01..05, AC-14)
- [ ] Defect register template present
- [ ] UAT readiness checklist agreed
- [ ] Entry/exit criteria documented

### Phase 1 Milestone Gate (M1 closure — all three G-reviews required)
- [ ] All WP-01..05 exit gates passed
- [ ] All Phase 1 acceptance criteria (AC-01..05, AC-14) evidenced
- [ ] All governance documents updated and committed
- [ ] G1 / G2 / G3 milestone review passed
- [ ] Human sponsor milestone acceptance

---

## Phase 1 Blockers (carried in)

| ID | Blocker | Owner | Impact |
|----|---------|-------|--------|
| B-02 | RACI on procurement step 1.19 — awaiting client confirmation | NADF Client | WP-PROC-02 (approval chain) |
| B-03 | PO approval threshold values — awaiting client confirmation | NADF Client | WP-PROC-02 |
| B-04A…G | 7 remaining department TO-BE specs | Claude Desktop | Phase 3 — do not block Phase 1 |
| E-01 | Nigerian payroll legal/HR advisory | Aliyu/Lanasoft | Phase 2/3 only |

---

## Governance Rules (per CLAUDE.md)

- Every change: **feature branch → conventional commit → PR → G-review → merge into protected `main`**.
- No direct push to `main`.
- Update DECISION_LOG / MODULE_REGISTRY / IMPLEMENTATION_HISTORY / CHANGELOG / PROJECT_STATE **before** a PR is marked ready.
- **Never mutate the live `NADF` database for verification** — use `--stop-after-init` for load checks; `restore_nadf.sh` drill DB for restore tests.
- Take a **backup before any schema/data-mutating operation**.
- **Single Claude Code session only** — confirm no concurrent session before starting each WP.

---

*Prepared as planning document only. No implementation has begun. Frozen at PEG-6 approval 2026-06-24.*
