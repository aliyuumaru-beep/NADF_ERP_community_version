# WP-01 — Foundation Hardening
## NADF ERP Programme — Work Package Definition

**Work Package ID:** WP-01
**Title:** Foundation Hardening
**Phase:** 1 — Foundation
**Complexity:** Medium
**Authority:** PEG-6 approval 2026-06-24 · Transfer Package v2.1
**Prepared by:** A1 Master Orchestrator · D1 Functional Architect · G1/G2/G3
**Date:** 2026-06-24
**Status:** PLANNED — awaiting G1/G2/G3 Go/No-Go clearance before implementation

> **DO NOT BEGIN IMPLEMENTATION** until the Go/No-Go checkpoint (§8) is passed by G1, G2, and G3.

---

## 1. Objective

Establish the Phase 1 technical and access foundation:
- Enforce single-session discipline and take a pre-work backup.
- Install, verify, and version-pin all five authorized OCA modules.
- Stand up the baseline security model (user groups for all five Phase 1 departments, TOTP 2FA).
- Verify the Odoo registry loads cleanly with all Phase 1 modules discoverable and exit code 0.

WP-01 is the prerequisite for all other Phase 1 work packages (WP-02, WP-03, WP-04, WP-05). None may begin until WP-01 exit gate passes.

---

## 2. Scope

### In scope
| Item | Detail |
|------|--------|
| Single-session confirmation | Verify no concurrent Claude Code sessions before any mutating operation |
| Pre-work backup | `scripts/backup_nadf.sh` — DB + filestore; record in `IMPLEMENTATION_HISTORY.md` |
| OCA compatibility verification | Confirm each of the 5 OCA modules supports Odoo 17 CE before install |
| OCA installation | Install `mis_builder`, `account_budget_oca`, `purchase_request`, `purchase_requisition`, `helpdesk_mgmt` |
| OCA version pinning | Pin each module version in `requirements.txt` or equivalent |
| Decision Log entries | Log each OCA install as a separate DEC entry (name, version, source URL, rationale) |
| User group creation | Finance (4 groups), Procurement (4), HR (5), Administration (5), Project Coord (4) |
| TOTP 2FA activation | Enable in Odoo General Settings |
| 2FA enforcement | Enforce for Finance Officer, Finance Manager, CFO, Auditor, and CEO groups |
| Registry verification | `odoo-bin --stop-after-init` exit 0 after all installs |

### Out of scope
| Item | Why excluded |
|------|-------------|
| Configuring the OCA modules (Finance, Procurement, etc.) | That is WP-02, WP-03, WP-04 |
| Access rights rules (model-level) | Configured per-department in WP-02..04 |
| Installing unapproved OCA or third-party modules | Not authorized |
| Modifying existing module code | Prohibited — no spec, no code |
| Modifying `nadf_vendor_onboarding` or `nadf_facilities_management` | Unratified; ratification is WP-02+ task |
| Data entry or master data population | Client responsibility |
| Anything Enterprise | Permanently prohibited |

---

## 3. Deliverables

| ID | Deliverable | Verification |
|----|------------|--------------|
| D-WP01-01 | Pre-work backup set recorded (DB + filestore, timestamped) | `~/odoo_backups/` entry + `IMPLEMENTATION_HISTORY.md` log |
| D-WP01-02 | `mis_builder` installed, Odoo-17-CE-compatible, version-pinned | `SELECT state FROM ir_module_module WHERE name='mis_builder' AND state='installed'` |
| D-WP01-03 | `account_budget_oca` installed, version-pinned | As above for `account_budget_oca` |
| D-WP01-04 | `purchase_request` installed, version-pinned | As above |
| D-WP01-05 | `purchase_requisition` installed, version-pinned | As above |
| D-WP01-06 | `helpdesk_mgmt` installed, version-pinned | As above |
| D-WP01-07 | Decision Log entries for all 5 OCA installs | `docs/DECISION_LOG.md` — 5 new DEC entries |
| D-WP01-08 | 22 user groups created (Finance ×4, Proc ×4, HR ×5, Admin ×5, PC ×4) | `SELECT name FROM res_groups WHERE category_id IN (...)` |
| D-WP01-09 | TOTP 2FA active and enforced for Finance Officer, Finance Manager, CFO, Auditor, and CEO | Odoo Settings → Two-factor auth = Required for specific groups |
| D-WP01-10 | Registry load verified exit 0 post-install | `odoo-bin --stop-after-init` terminal output |
| D-WP01-11 | `MODULE_REGISTRY.md` updated with 5 OCA module entries (name, version, source, install date) | Manual review of `MODULE_REGISTRY.md` |

---

## 4. Acceptance Criteria

| ID | Criterion | Test method |
|----|-----------|-------------|
| AC-WP01-01 | All 5 OCA modules return `state='installed'` in `ir_module_module` | DB query |
| AC-WP01-02 | Each of the 5 OCA modules has a Decision Log entry with version and source URL | Manual review of `docs/DECISION_LOG.md` |
| AC-WP01-03 | All 22 Phase 1 user groups exist and are assigned to the correct categories | DB query / Odoo Settings > Users & Groups |
| AC-WP01-04 | TOTP 2FA is set to "Required for specific groups" in Odoo Settings | UI verification |
| AC-WP01-05 | Finance Officer, Finance Manager, CFO, Auditor, and CEO accounts are blocked from login without TOTP | Login test with a Finance user — must prompt for TOTP |
| AC-WP01-06 | `odoo-bin --stop-after-init` exits 0 AND produces no ERROR or CRITICAL log lines attributable to any of the five installed OCA modules or to `nadf_vendor_onboarding` / `nadf_facilities_management` | Command + full log scan |
| AC-WP01-07 | Pre-work backup set recorded and filesize > 0 | `ls -lh ~/odoo_backups/` |
| AC-WP01-08 | Single Claude Code session confirmed active at time of implementation | Manual confirmation in status report |

---

## 5. Risks

| ID | Risk | L | I | Mitigation |
|----|------|---|---|-----------|
| R-WP01-01 | One or more OCA modules incompatible with Odoo 17 CE | Med | High | Compatibility check **before** install; if incompatible, log finding and escalate — do not install incompatible version |
| R-WP01-02 | OCA module install fails / breaks existing modules | Low | High | Take backup (D-WP01-01) before first install; restore to drill DB if recovery needed |
| R-WP01-03 | Concurrent Claude Code session writes conflicting config | Med | Med | Single-session check (AC-WP01-08) is the first action; stop if another session detected |
| R-WP01-04 | User group creation overlaps with existing groups | Low | Low | Query existing groups before creation; update rather than duplicate |
| R-WP01-05 | `requirements.txt` version pinning format not established | Low | Low | Create `requirements.txt` if absent; use `module_name==x.y.z` format |

---

## 6. Governance Reviews Required

| Reviewer | When | Scope |
|----------|------|-------|
| **G1 — Architecture & Odoo Governance** | Go/No-Go checkpoint (before implementation) + Exit gate | OCA module choice and approach order; no core modification; CE-only |
| **G2 — Quality & Documentation Governance** | Exit gate | All deliverables evidenced; Decision Log entries present; doc updates complete before PR |
| **G3 — Security & Change Governance** | Go/No-Go + Exit gate | Single-session confirmed; backup recorded; 2FA active; branch/PR discipline |

All three must pass the **Go/No-Go checkpoint (§8)** before any mutating operation begins, and all three must pass the **Exit gate** before WP-01 is marked Done and WP-02/03/04 can begin.

---

## 7. Dependencies

| Dependency | Status | Notes |
|-----------|--------|-------|
| PEG-6 approval | ✅ 2026-06-24 | Phase 1 authorized |
| G1/G2/G3 Go/No-Go clearance | ⏳ Not yet passed | Required before any implementation |
| Odoo service running on corrected `addons_path` | ✅ PID 51025 | `nadf_vendor_onboarding` + `nadf_facilities_management` discoverable |
| Internet access for OCA repository | Required | Needed for version verification and download |
| OCA module Odoo-17 compatibility confirmation | Required before install | Check OCA repo branch / release notes |

---

## 8. Go/No-Go Checkpoint (required before implementation begins)

**This checkpoint must be passed before D2 Solution Builder executes a single install command.**

G1, G2, and G3 must each confirm:

| Check | G1 | G2 | G3 |
|-------|----|----|-----|
| PEG-6 approval recorded (`DEC-PEG6-001`) | ☐ | ☐ | ☐ |
| Single Claude Code session confirmed | ☐ | ☐ | ☐ |
| Pre-work backup plan confirmed | ☐ | ☐ | ☐ |
| OCA module list matches authorized list (§2 In scope) | ☐ | ☐ | ☐ |
| No Enterprise modules in OCA list | ☐ | ☐ | ☐ |
| Branch created for WP-01 implementation | ☐ | ☐ | ☐ |
| Working tree clean at start | ☐ | ☐ | ☐ |

**Go/No-Go decision:** ☐ GO  ☐ NO-GO (record reason and remediation action)

**Decision recorded by:** ______________________  **Date:** ____________

---

## 9. Implementation Notes (for D2 Solution Builder — not to be actioned before Go/No-Go)

The following notes are provided to inform planning. They do not constitute authorization to implement.

- **OCA source:** OCA modules for Odoo 17 are available at `github.com/OCA/<repo>/tree/17.0`. Preferred install method: clone into a directory on `addons_path` or install via `pip` from OCA PyPI releases.
- **Version pinning:** record the exact commit SHA or release tag, not just the version string.
- **`helpdesk_mgmt` note:** replaces the unratified `project`-based ICT helpdesk workaround from the legacy build. The legacy `project`-based helpdesk configuration should be documented before being superseded.
- **`mis_builder` note:** KPI set must be agreed with the client before dashboard configuration (WP-02-08); WP-01 only installs the module, not configures it.
- **User group naming convention:** follow the naming pattern in `planning/WORK_PACKAGES.md` WP-FIN-03 / WP-HR-01 / WP-ADM-01 sections.
- **2FA enforcement:** Odoo 17 CE uses native TOTP (`auth_totp`); enable in Settings → Technical → Two-factor authentication. Enforce per group via group policy, not per-user.

---

*This work package definition is a planning document only. Implementation does not begin until §8 Go/No-Go passes. Authority: PEG-6 approval 2026-06-24 · Transfer Package v2.1.*
