# NADF ERP — Next Action

**Last updated:** 2026-06-19

## Current Phase
Phase 1 — Business Process Documentation (in progress) + Phase 2 — Odoo CE Configuration (re-scoping)

## Current Department
Legal Services Unit (LSU) — P5 AS-IS in production

## Current Milestone
M-LSU-05: Complete Legal P5 AS-IS swimlane (dual START triggers, HLSU as accountability note, not a separate lane); then produce Legal P4 Detailed TO-BE; then P5 and P6 Detailed TO-BE.

## Current Blocker
None blocking swimlane work. Platform correction (Odoo 17 CE) requires Claude Code to audit installed modules before ERP work resumes.

## Next Recommended Action
**For Claude Desktop:** Complete Legal P5 AS-IS swimlane. Upload workbook if not yet available. Once P5 AS-IS is approved, produce P4 Detailed TO-BE, then P5 and P6.

**For Claude Code (first session):** Run full discovery sequence (Section 17 of transfer package v2). Produce Discovery Report. Run Governance Activation Gate (Section 14). Priority: identify any Enterprise-only modules currently installed in Odoo and document them in `docs/DECISION_LOG.md` under M-PLATFORM-CORRECTION. Do not begin any ERP configuration work until this audit is complete and reported.

## Files to read before starting (Claude Code)
1. `docs/NEXT_ACTION.md` (this file)
2. `docs/PRODUCT_STATE_INDEX.md`
3. `docs/CONTROL_TOWER.md`
4. `NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.md` (if loaded into session)
