# NADF ERP — Next Action

**Last updated:** 2026-06-24 (Phase 1 activated — PEG-6 approved)

## Current Milestone
**M1 — Foundation** (ROADMAP Phase 1). M0 formally closed (PEG-6 approved 2026-06-24, `DEC-PEG6-001`; PR #1 + PR #2 merged to `main`). Phase 1 Product Engineering now active.

## Current State
- **PEG-6 APPROVED** — Phase 1 authorized (CONDITIONAL GO, conditions a–e satisfied/enforced).
- **M0 CLOSED**: Governance Gate 21/21 PASS · governance baseline on `main` (`b8dad2d`) · PEG-6 signed.
- Odoo restarted on corrected `addons_path`; `nadf_vendor_onboarding` and `nadf_facilities_management` confirmed discoverable (exit 0).
- **Single Claude Code session enforced** — only one active session permitted at any time.
- Phase 1 scope **frozen** at Transfer Package v2.1.
- Phase 1 planning documents prepared (`docs/product/`, `docs/work_packages/WP_01_FOUNDATION_HARDENING.md`).
- Legacy build (Phases 0–10) remains **built / unratified** — ratification is Phase 1 work.

## Next Recommended Actions (in order)

**➡️ 1. Activate Governance Layer (G1/G2/G3) before any Delivery Layer work.**
G1 Architecture/Odoo Governance → G2 Quality & Documentation Governance → G3 Security & Change Governance must review and clear WP-01 before D1–D4 agents are activated.

**➡️ 2. WP-01 Go/No-Go checkpoint.** Review `docs/work_packages/WP_01_FOUNDATION_HARDENING.md`. G1/G2/G3 must pass the checkpoint before WP-01 implementation begins.

**➡️ 3. Implement WP-01 — Foundation Hardening** (once G-layer clears): install and version-pin five OCA modules; configure baseline security groups; enforce 2FA; take pre-work backup.

**➡️ 4. Proceed to WP-02 (Finance Core) → WP-03 (Procurement Core) → WP-04 (HR Core) → WP-05 (UAT Preparation)** per `docs/product/PHASE_1_ROADMAP.md`.

## Remaining blockers before WP-01 implementation
- G1/G2/G3 governance layer activation and WP-01 Go/No-Go clearance.
- OCA module Odoo-17-CE compatibility verification (before install).
- Procurement approval chain (WP-PROC-02) remains blocked on B-02/B-03 (client confirmation).
- Pre-work backup must be taken before first schema/data-mutating operation.

## Single-session discipline
⚠️ **Only one Claude Code session may be active at any time.** A concurrent session was detected during M-C stabilization. Before starting any WP implementation, confirm no other session is open against this repository.

## Not yet started (gated)
- Phase 1 foundation ratification + OCA installs (no install without compatibility check + Decision Log entry).
- Custom-module specs (Phase 2) — no spec, no code.
- Department builds — gated on TO-BE delivery.

## Files to read before starting (any session)
1. `docs/NEXT_ACTION.md` (this file)
2. `docs/PRODUCT_STATE_INDEX.md` (session protocol)
3. `PROJECT_STATE.md`
4. `MILESTONE_TRACKER.md`
5. `requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md` (bound authority)
