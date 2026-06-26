# IMPLEMENTATION_HISTORY.md
## NADF ERP Programme — Implementation History (POD-NADF)

**Document type:** Mandatory repository artifact (`18_IMPLEMENTATION_HISTORY_STANDARD.md`, Repository Standard `10`)
**Created:** 2026-06-23 (Migration Sequence M-D) · **Maintained by:** A1 Software Factory Orchestrator
**Scope:** Milestones, phases, recoveries, backups/restore events, and significant operational changes. Append-only.

---

## 1. Legacy MVP build (out of governance sequence) — author `MAC`

| Date | Phase | Summary | Commit |
|------|-------|---------|--------|
| 2026-06-02 | Phase 0 | Inspection & foundation documents | `48f1738` |
| 2026-06-02 | Phase 1 | Company, fiscal year, users | `4479b0e` |
| 2026-06-03 | Phase 2 | Finance configuration | `44d3d33` |
| 2026-06-03 | Phase 3–4 | Procurement & HR configuration | `0c22549` |
| 2026-06-04 | Phase 5 | Approval workflows (base.automation) + decisions | `ec2fc32` |
| 2026-06-04 | Phase 6 | Demo scenarios live in `NADF` DB | `038ed67` |
| 2026-06-05 | Phase 7 | NADF government chart of accounts (319 accts) | `59feda0` |
| 2026-06-08 | Phase 8 | Assets, fleet, ICT helpdesk, staff roster | `05568b4` |
| 2026-06-09 | Phase 9 | `nadf_vendor_onboarding` built (then untracked in FamOil tree) | — |
| 2026-06-13 | Phase 10 | `nadf_facilities_management` built (then committed in famoil-erp `55c1787`) | — |

> All legacy work is **built / unratified** — delivered before M0 governance completed (see `docs/GOVERNANCE_COMPLIANCE_AUDIT.md`, Maturity Level 0). No milestone is closed.

## 2. Agent OS migration — author `A1 Software Factory Orchestrator`

### M-B — Bootstrap-enable (2026-06-21)
- Stood up `PROJECT_STATE.md`, `MILESTONE_TRACKER.md`, reconciled `planning/`; quarantined the stale Control-Tower scaffold zip. Commits `16c8cf7`, `d15b30d`.

### M-C — Governance Certification & Recovery (2026-06-22)
| Item | Evidence |
|------|----------|
| Recovered `nadf_vendor_onboarding` (MR-01, integrity 12/12) | `a9738b4` |
| Relocated `nadf_facilities_management` from `famoil-erp@55c1787` (MR-02, integrity 33/33) | `4ccb306` |
| FamOil contamination removed + `nadf_*` guard (local-only) | famoil `9a16f74` |
| RISK_REGISTER + DEC-PLATFORM-001/RECOVERY-001/002/BACKUP-001 | `c21cfd8` |
| Backup strategy + first restore drill | `ad43fa4` |
| Governance gate baseline (16/21) | `b52d15d` |
| PROJECT_STATE/MILESTONE_TRACKER reconcile | `a63cf99` |

### M-C incident stabilization (2026-06-22)
- **Configuration drift:** relocation left `nadf.conf` `addons_path` pointing only at the old `odoo17/custom_addons`; relocated modules undiscoverable. Corrected `addons_path` (added `nadf_erp/custom_addons`). Verified: `odoo-bin --stop-after-init` loaded 94 modules, exit 0. Commit `f53304c`. Second concurrent writer session later self-terminated; `f53304c` pushed.

### M-D — Closure-tier docs, CI, main fold (2026-06-23)
- Authored mandatory root docs (`README`, `CLAUDE.md`, `CHANGELOG`, `IMPLEMENTATION_HISTORY`, `MODULE_REGISTRY`, root `ROADMAP`), `docs/PRODUCT_STATE_INDEX.md` (session rules, BL-GOV-09), and CI (`.github/workflows/ci.yml`). Governance Gate re-run to full 21/21. PR opened to fold `phase/0-governance` → `main`.

### WP-04 — HR Core executed (2026-06-26) — M1 Foundation active

| Item | Result |
|------|--------|
| WP04-00: Pre-work backup | `nadf_20260625_142500` — dump 6.3 MB + filestore 37 MB — PASS |
| WP04-00: `hr_recruitment` install | 17.0.0.1 CE native installed; 105 modules (was 100); exit 0 — DEC-WP04-001 |
| WP04-01: Manager hierarchy | 8 `parent_id` corrections committed; 4-level org: ES → CS Head → HR/Comms/ICT Heads → Officers — DEC-WP04-004 |
| WP04-02: Admin dept employees | 6 employees (IDs 12,13,14,18,20,23) flagged; dept/mgr pending client — B-WP04-01 |
| WP04-03: Leave approval workflows | 4 types corrected to `both` (Annual, Casual, Sick, Compensatory); statutory retained at `hr` — DEC-WP04-003 |
| WP04-04: Recruitment pipeline | 5-stage NADF pipeline: Vacancy Posted → Shortlisted → Interview → Offer → Appointment (hired_stage=True). Odoo defaults folded — DEC-WP04-001 |
| WP04-05: x_employment_state | Selection field id=11644 on `hr.employee`; 24 employees = `employed`; 2 CEO automations active (auto ids 7,8) — DEC-WP04-002 |
| WP04-06: mail.thread audit | `hr.employee` ✅ `hr.leave` ✅ `hr.applicant` ✅ — AC-14 PASS |
| WP04-07: HR group assignments | Employee (8), Line Manager (5), HR Officer (1), HR Manager (1), CEO (1); Time Off Officer + Responsible wired |
| WP04-08: Company RC/TIN | DEFERRED — client must supply NADF RC number and TIN (B-WP04-02) |
| WP04-09: Claude API key | Pre-confirmed SET (108 chars) — PASS |

**WP-04 exit gate status:** CONDITIONAL PASS — 25/26 criteria PASS; WP04-08 DEFERRED (client action); WP04-02 DEFERRED (client action). 0 FAIL. All blocking items are client-data dependencies, not technical blockers.

**Key findings:**
- `hr_recruitment` ships with 6 default stages; stages have no `active` field — use `fold=True` + high sequence to suppress defaults.
- `base.automation` activity action state is `next_activity` (not `activity` — that is Enterprise-only). Confirmed in CE Odoo 17.
- Suleiman Yusuf (Finance Officer) was incorrectly mapped to Strategy Head in legacy build — corrected to Finance Head.
- x_employment_state is DB-resident (same pattern as x_compliance_status, DEC-WP03-001). Risk of loss on DB rebuild — document in Phase 2 `nadf_vendor_compliance` or `nadf_hr_custom` spec.

### WP-03 — Procurement Core executed (2026-06-25) — M1 Foundation active

| Item | Result |
|------|--------|
| WP03-00: Pre-work backup | `nadf_20260625_133009` — dump 6.3 MB + filestore 37 MB — PASS |
| WP03-01: Vendor compliance field | `x_compliance_status` created (ir.model.fields id=11353) on `res.partner`; 3 compliant, 1 pending — DEC-WP03-001 |
| WP03-02: `purchase_request` workflow | `procurement.officer` → PR User; `head.procurement` → PR Manager; WP03-TEST-PR-001 draft→to_approve→approved — PASS |
| WP03-03: `purchase_requisition` Call for Tender | Type id=2 created; T/REQ/001 → P00010 (Abuja, ₦250K) + P00011 (ProLearn, ₦242.5K); ProLearn awarded; Abuja cancelled; requisition closed — PASS |
| WP03-04: Goods receipt | NADF/IN/00004 validated (5× HP Toner from P00011); stock.move state=done, qty=5.0 — PASS |
| WP03-05: OCA `contract` evaluation | OCA `contract` not in addons_path; fit-gap: RACI requirement unmet; recommendation = DEFER Phase 2/3; DEC-CONTRACT-001 logged |
| WP03-06: mail.thread audit | purchase.request: 2 messages ✅; purchase.order: 5 messages ✅ — AC-14 PASS |
| WP03-07: Multi-level approval | BLOCKED — B-02 (RACI 1.19) + B-03 (thresholds) client confirmation outstanding. ₦500,000 threshold UNCHANGED |

**WP-03 exit gate status:** CONDITIONAL PASS — 6/7 items done; WP03-07 blocked (B-02/B-03). Compliance field is DB-only (R-WP03-01, creation command documented).

**Key findings:**
- OCA `purchase_request` uses its own group hierarchy; NADF procurement users mapped via direct group assignment (DEC-WP03-002).
- `purchase.requisition` CE native flow: confirm → manual RFQ creation per vendor → award (confirm winner, cancel losers) → close.
- Odoo 17 `stock.move.line` uses `quantity` field (not `qty_done` — removed); `stock.move` uses `quantity` computed from move_line_ids.
- `ir.model.fields` creation via shell works for simple selection fields; field is DB-resident (not version-controlled).

### WP-02 — Finance Core re-validated (2026-06-25) — M1 Foundation active

| Item | Result |
|------|--------|
| WP02-01: CoA re-validated | 319 NADF 8-digit accounts active; 71 CE legacy deprecated — PASS |
| WP02-02: CoA exported | `csv_templates/nadf_coa_revalidated_20260625.csv` (319 rows); client review pending |
| WP02-03: Vendor bill workflow | draft → posted cycle validated; BILL/2026/06/0002 created + reversed — PASS |
| WP02-04: Payment workflow | Bank (BNK1) + Cash (CSH1) journals verified; dual-auth advisory via base.automation (4 rules active) — DEC-WP02-001 |
| WP02-05: Finance user assignments | finance.officer → Finance Officer; head.finance → Finance Manager + CFO — PASS |
| WP02-06: Analytic accounts | 5 dept cost centres confirmed: CC-ADM, CC-EXE, CC-FIN, CC-HR, CC-PRO — DEC-WP02-002 |
| WP02-07: Budget control | BLOCKED — DEC-OCA-02 (account_budget_oca incompatible) |
| WP02-08: mis_builder dashboard | Deferred — client KPI sign-off required (SH priority) |
| WP02-09: Financial reports | 5 account.report records confirmed (CE native) — PASS |
| WP02-10: mail.thread audit | Confirmed on account.move — PASS |
| WP02-11: Tax accounts | WHT 41030102 (14 tax lines), VAT 41030103 (8 tax lines) — no changes needed |

**WP-02 exit gate status:** CONDITIONAL PASS — 9/11 items done; WP02-07 blocked (DEC-OCA-02); WP02-08 deferred (client action required).

### WP-01 — Foundation Hardening executed (2026-06-25) — M1 Foundation active

| Item | Evidence / Decision |
|------|---------------------|
| Single-session confirmed (WP01-01) | One Claude Code process (PID 44319) at execution start |
| Pre-work backup taken (WP01-02) | `nadf_20260624_160329`: dump 5.9 MB + filestore 36 MB — verified |
| OCA compatibility verified (WP01-03..07) | 4 of 5 OCA modules compatible; `account_budget_oca` blocked (DEC-OCA-02) |
| `mis_builder` 17.0.1.5.0 installed (WP01-08) | `state='installed'`; deps: `report_xlsx` (OCA/reporting-engine), `date_range` (OCA/server-ux), `board` (CE) — DEC-OCA-01 |
| `account_budget_oca` NOT installed (WP01-09) | Compatibility failure — field `theoritical_amount` missing; escalated — DEC-OCA-02 |
| `purchase_request` 17.0.2.3.4 installed (WP01-10) | `state='installed'` — DEC-OCA-03 |
| `purchase_requisition` 17.0.0.1 CE native (WP01-11) | Already installed; confirmed CE native; DEC-OCA-05 |
| `helpdesk_mgmt` 17.0.1.10.4 installed (WP01-12) | `state='installed'` — DEC-OCA-04 |
| 22 Phase 1 user groups created (WP01-13..17) | Finance×4, Procurement×4, HR×5, Administration×5, Project Coordination×4 — committed to DB |
| TOTP 2FA policy set to `required` (WP01-18..19) | `auth_totp.policy = required` in `ir.config_parameter`; global enforcement; DEC-2FA-002 |
| Registry exit 0 post-install (WP01-20) | 100 modules, 1.78s, no ERROR/CRITICAL lines for any Phase 1 module — AC-WP01-06 PASS |
| OCA addons path added (D-WP01-11) | `nadf.conf` updated: `/Users/mac/oca_addons` added to `addons_path`; `MODULE_REGISTRY.md` updated |
| Odoo restarted PID 54258 | Running on updated `nadf.conf` with full OCA addons path |

**WP-01 exit gate status:** CONDITIONAL PASS — 4/5 OCA modules installed; `account_budget_oca` blocked (DEC-OCA-02). WP-02 Finance re-validation can proceed; WP02-07 (budget) blocked pending DEC-OCA-02 resolution.

### Phase 1 activation — PEG-6 approved (2026-06-24) — governance-only

- **PEG-6 APPROVED** by Business Sponsor (Aliyu / Lanasoft Technologies); recorded as `DEC-PEG6-001`. M0 formally closed.
- **Odoo restart:** live service was already stopped at restart attempt; started fresh as PID 51025 on corrected `nadf.conf`. Both custom modules confirmed discoverable (`get_modules()` check) and `--stop-after-init` exit 0.
- **Phase 1 planning documents authored** (planning only — no coding): `docs/product/PHASE_1_PRODUCT_CAPABILITY_MAP.md`, `docs/product/PHASE_1_ROADMAP.md`, `docs/product/PHASE_1_BACKLOG.md`, `docs/work_packages/WP_01_FOUNDATION_HARDENING.md`.
- **PEG-6 package updated:** §15 approval record added; §Readiness Summary business authorization updated to APPROVED.
- **Governance docs updated:** `NEXT_ACTION.md` (M1 active, G-layer next), `CHANGELOG.md`, `IMPLEMENTATION_HISTORY.md`, `docs/DECISION_LOG.md` (`DEC-PEG6-001`).
- **No module code changed. No Odoo functional configuration changed.** Committed on branch `docs/phase-1-activation` → PR to `main`.
- Single-session discipline enforced in state docs. Phase 1 scope frozen at Transfer Package v2.1. Governance layer (G1/G2/G3) must activate before delivery layer (D1–D4) and before any WP implementation.

### PEG-6 — Product Authorization package prepared (2026-06-24) — governance-only
- Confirmed `main` @ `989b65f` carries the merged governance baseline; working tree clean; all 11 required governance docs present; CI script present. All stop-checks passed.
- Authored `docs/governance/PEG_6_PRODUCT_AUTHORIZATION_PACKAGE.md` (14 sections; WP-01..05; G1/G2/G3-then-D1..D4 activation plan; **CONDITIONAL GO** recommendation with conditions a–e).
- Updated `docs/NEXT_ACTION.md` (next action = PEG-6 review/approval) and `CHANGELOG.md`.
- **No module code and no Odoo functional configuration changed.** Prepared on branch `docs/peg-6-product-authorization` → PR (branch protection: no direct `main` push).
- Carried warnings into the package: concurrent session detected during M-C stabilization (R-11); live Odoo not yet restarted after `addons_path` correction (R-12, §4 pending operational note). Development remains **blocked** pending PEG-6 approval.

## 3. RESTORE_EVENT log
*(Migrated from `docs/BACKUP_STRATEGY.md` §9 per Backup & Recovery Standard `20`.)*

| Date | Type | Backup set | Result | Verification |
|------|------|-----------|--------|--------------|
| 2026-06-22 | RESTORE_EVENT (first drill) | `nadf_20260622_114439` (dump 6,215,346 B; filestore 38,265,886 B) | **PASS** | Restored to `NADF_restore_drill`; installed_modules 94 = live 94; res_partner 40 = live 40; both NADF modules present; drill DB dropped |

**Backup-set SHA-256:** dump `48615c6d…641622` · filestore `f49c766b…6c69db1`.

## 4. Pending operational note
- Live Odoo instance (PID observed 7732) was running on the pre-fix in-memory `addons_path`; a graceful restart is advised so it adopts the corrected `nadf.conf`. The next restart is verified clean (§2 M-C incident).
