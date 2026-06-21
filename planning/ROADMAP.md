# ROADMAP.md
## NADF ERP Programme — Implementation Sequence

**Document type:** Operational — derived from NADF Full Product Transfer Package v2.1  
**Last updated:** 2026-06-20  
**Authority:** NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md

---

## PHASE 0 — GOVERNANCE REMEDIATION
**Status:** ⏳ Not started — URGENT  
**Sequence position:** Must complete before any Phase 1 work begins

### Objectives
- Confirm the repository is properly initialised and governed
- Confirm the Odoo instance contains zero Enterprise modules
- Activate all five Governance Gates
- Establish the programme memory system in the repository

### Deliverables
| ID | Deliverable |
|----|------------|
| D-0.1 | Discovery Report — full repository and Odoo instance audit |
| D-0.2 | `docs/GOVERNANCE_GATE_REPORT.md` — all five gates PASS |
| D-0.3 | `docs/BACKUP_STRATEGY.md` — daily backup schedule and restore procedure documented |
| D-0.4 | Repository scaffold committed to `main` — all control documents present and current |
| D-0.5 | `docs/DECISION_LOG.md` entry DEC-PLATFORM-001 — Odoo 17 CE platform confirmed |
| D-0.6 | GitHub branch protection and CI workflow active |
| D-0.7 | `docs/NEXT_ACTION.md` current and pointing to Phase 1 |

### Dependencies
- Repository access (`/Users/mac/nadf_erp`)
- Odoo instance access (`/Users/mac/odoo17`)
- Transfer Package v2.1 loaded into session

### Exit Criteria
- All five Governance Gates: PASS
- Zero Enterprise modules in Odoo instance (or removal plan documented)
- Repository scaffold committed and pushed
- Backup strategy documented and last backup confirmed within 24 hours

---

## PHASE 1 — FOUNDATION
**Status:** 🔄 In progress (partial — requires governance activation first)  
**Sequence position:** After Phase 0 exit criteria met

### Objectives
- Configure Odoo 17 CE core modules for Finance, Procurement, HR, Administration, and Project Coordination
- Install and configure all required OCA modules
- Establish user groups and access rights for all Phase 1 departments
- Implement approval workflows for Phase 1 departments

### Deliverables
| ID | Deliverable |
|----|------------|
| D-1.1 | Finance: chart of accounts, vendor bills, payment workflow, budget control, 2FA, user groups |
| D-1.2 | Finance: `mis_builder` dashboard with NADF financial KPIs |
| D-1.3 | Procurement: `purchase_request` multi-step requisition and approval chain |
| D-1.4 | Procurement: RFQ and purchase order workflow with threshold-based approval |
| D-1.5 | Procurement: vendor record structure with compliance status field |
| D-1.6 | HR: employee records, 4-level org hierarchy, leave workflow, recruitment pipeline |
| D-1.7 | Administration: fleet register, asset register, `helpdesk_mgmt` ICT ticketing |
| D-1.8 | Project Coordination: project structure, task/milestone model, phase gate config |
| D-1.9 | OCA modules installed, version-pinned, and logged: `mis_builder`, `helpdesk_mgmt`, `purchase_request`, `purchase_requisition`, `account_budget_oca` |
| D-1.10 | Access rights matrix: all Phase 1 user groups configured and tested |

### Dependencies
- Phase 0 exit criteria met
- Procurement blockers B-02 and B-03 resolved by client (approval chain cannot be completed until then)
- OCA Odoo 17 compatibility confirmed for each module before installation

### Exit Criteria
- All Phase 1 acceptance criteria (AC-01 through AC-05, AC-14) met
- All D-1.x deliverables committed to repository
- Governance documents updated
- No open critical defects from Phase 1 self-review

---

## PHASE 2 — CORE ERP (CUSTOM MODULES — SPECIFICATIONS)
**Status:** ⏳ Not started  
**Sequence position:** Runs in parallel with Phase 1 from mid-Phase 1 onwards

### Objectives
- Produce approved design specifications for all six custom modules
- Client sign-off obtained on each spec before development begins
- No custom module development in this phase — specification only

### Deliverables
| ID | Deliverable |
|----|------------|
| D-2.1 | `docs/modules/nadf_payroll_ng_spec.md` — approved |
| D-2.2 | `docs/modules/nadf_vendor_compliance_spec.md` — approved |
| D-2.3 | `docs/modules/nadf_facility_spec.md` — approved |
| D-2.4 | `docs/modules/nadf_legal_contract_spec.md` — approved (after Legal TO-BE complete) |
| D-2.5 | `docs/modules/nadf_investment_spec.md` — approved (after Investment TO-BE + client requirements session) |
| D-2.6 | `docs/modules/nadf_me_indicators_spec.md` — approved (after M&E TO-BE complete) |

### Dependencies
- `nadf_payroll_ng_spec`: Nigerian statutory payroll legal/HR input required
- `nadf_legal_contract_spec`: Legal Services Unit TO-BE P4–P6 complete
- `nadf_investment_spec`: Investment TO-BE complete + client business requirements session
- `nadf_me_indicators_spec`: M&E TO-BE complete
- `nadf_vendor_compliance_spec`, `nadf_facility_spec`: Phase 1 department TO-BEs already complete — can start

### Exit Criteria
- All six specs approved and committed
- Each spec contains: purpose, capability map reference, data model, business rules, UI description, test cases, acceptance criteria

---

## PHASE 3 — EXTENDED CAPABILITIES (CUSTOM MODULE DEVELOPMENT + REMAINING DEPARTMENTS)
**Status:** ⏳ Not started  
**Sequence position:** After Phase 2 specs approved; runs alongside TO-BE delivery from Claude Desktop

### Objectives
- Build and test all six custom Odoo modules against their approved specs
- Configure Odoo for Legal, Strategy, Communications, Sustainable Agriculture, Investment, M&E, and Executive Management — each triggered when its TO-BE specification arrives
- Complete access rights matrix for all 12 departments

### Deliverables
| ID | Deliverable |
|----|------------|
| D-3.1 | `nadf_payroll_ng` — developed, tested, deployed to staging |
| D-3.2 | `nadf_vendor_compliance` — developed, tested, deployed to staging |
| D-3.3 | `nadf_facility` — developed, tested, deployed to staging |
| D-3.4 | `nadf_legal_contract` — developed, tested, deployed to staging |
| D-3.5 | `nadf_investment` — developed, tested, deployed to staging |
| D-3.6 | `nadf_me_indicators` — developed, tested, deployed to staging |
| D-3.7 | Legal Services Unit: Odoo build complete against TO-BE spec |
| D-3.8 | Strategy & Planning: Odoo build complete against TO-BE spec |
| D-3.9 | Communications: Odoo build complete against TO-BE spec |
| D-3.10 | Sustainable Agriculture: Odoo build complete against TO-BE spec |
| D-3.11 | Investment: Odoo build complete (`nadf_investment`) |
| D-3.12 | Monitoring & Evaluation: Odoo build complete (`nadf_me_indicators` + `mis_builder`) |
| D-3.13 | Executive Management: Odoo build complete (`mis_builder` dashboard) |
| D-3.14 | Full access rights matrix — all 12 departments, all user groups, all roles |

### Dependencies
- Each department build: corresponding TO-BE specification delivered
- Each custom module development: corresponding spec approved (Phase 2)
- `nadf_investment` development: after `nadf_investment_spec` approved AND Investment TO-BE delivered

### Exit Criteria
- All six custom modules tested against their acceptance criteria
- All 12 department Odoo builds complete
- All acceptance criteria AC-01 through AC-14 met
- All governance documents updated and committed

---

## PHASE 4 — INTEGRATIONS
**Status:** ⏳ Not started  
**Sequence position:** After Phase 3 exit criteria met

### Objectives
- Implement and test cross-functional workflows that span multiple departments
- Verify end-to-end process chains function correctly across module boundaries
- Confirm audit trail coverage across all integrated workflows

### Deliverables
| ID | Deliverable |
|----|------------|
| D-4.1 | Budget → Procurement → Finance end-to-end approval chain tested and verified |
| D-4.2 | HR appointment → CEO approval → payroll integration tested |
| D-4.3 | Project → Finance budget consumption linkage tested |
| D-4.4 | Investment disbursement → Finance payment chain tested |
| D-4.5 | Cross-department notification and escalation matrix configured and tested |
| D-4.6 | Executive dashboard: cross-department KPI roll-up verified against source data |
| D-4.7 | Integration test report committed to repository |

### Dependencies
- Phase 3 exit criteria met (all department builds complete)

### Exit Criteria
- All cross-functional acceptance criteria (AC-13) met
- Integration test report produced and committed
- No open critical defects

---

## PHASE 5 — TESTING & STABILISATION
**Status:** ⏳ Not started  
**Sequence position:** After Phase 4 exit criteria met

### Objectives
- Execute full User Acceptance Testing cycle
- Resolve all defects raised during UAT
- Stabilise the system for production deployment
- Produce training documentation

### Deliverables
| ID | Deliverable |
|----|------------|
| D-5.1 | UAT test plan and test cases (one per acceptance criterion) |
| D-5.2 | UAT execution — all AC-01 through AC-14 tested with NADF users |
| D-5.3 | UAT defect register — all defects logged, triaged, resolved |
| D-5.4 | UAT sign-off document — signed by NADF |
| D-5.5 | Super user training documentation per department |
| D-5.6 | System administrator guide |
| D-5.7 | Final governance document review — all control documents current |

### Dependencies
- Phase 4 exit criteria met
- NADF UAT team available and briefed
- Staging environment stable

### Exit Criteria
- UAT sign-off obtained from NADF
- Zero open critical defects
- Zero open high defects (or formally deferred with client agreement)
- Training documentation complete

---

## PHASE 6 — DEPLOYMENT
**Status:** ⏳ Not started  
**Sequence position:** After Phase 5 exit criteria (UAT sign-off) met

### Objectives
- Deploy the complete Odoo system to production
- Execute data migration
- Confirm system health post-cutover
- Hand over to NADF operations

### Deliverables
| ID | Deliverable |
|----|------------|
| D-6.1 | Cutover plan — documented and approved |
| D-6.2 | Data migration: master data loaded (employees, vendors, chart of accounts values, asset register) |
| D-6.3 | Production deployment executed |
| D-6.4 | Post-deployment smoke test — all critical workflows verified on production |
| D-6.5 | Go-live confirmation — signed by NADF and Lanasoft |
| D-6.6 | Hypercare plan — support model for first 30 days post-go-live |
| D-6.7 | Final repository state committed and tagged: `v1.0-go-live` |

### Dependencies
- Phase 5 exit criteria (UAT sign-off) met
- Production server confirmed and accessible
- NADF IT team briefed on production environment

### Exit Criteria
- Production system live and stable
- Go-live confirmation signed
- All governance documents final and committed
- Hypercare period begun

---

## PHASE 7 — TEMPLATE EXTRACTION
**Status:** ⏳ Not started  
**Sequence position:** After Phase 6 go-live confirmed; may begin during hypercare period

### Objectives
- Extract all "Generic Reusable" and "Government ERP" assets from the NADF deployment
- Strip NADF-specific data and configuration
- Package as the Lanasoft Public Sector ERP Template
- Document the template for future use

### Deliverables
| ID | Deliverable |
|----|------------|
| D-7.1 | Template extraction report — all assets identified against PRODUCT_SCOPE.md Section 7 |
| D-7.2 | Anonymised repository scaffold — NADF references stripped |
| D-7.3 | Parameterised custom modules — NADF data stripped; structure retained (`nadf_` prefix replaced with `public_sector_`) |
| D-7.4 | Government chart of accounts template — structure retained; NADF-specific codes removed |
| D-7.5 | OCA module integration patterns — documented as reusable configuration guides |
| D-7.6 | Public Sector ERP Template repository — new repository created and published |
| D-7.7 | Template README and deployment guide |

### Dependencies
- Phase 6 exit criteria met
- Legal clearance from Lanasoft for template publication

### Exit Criteria
- Public Sector ERP Template repository created and documented
- All extracted assets verified free of NADF-specific data
- Template README sufficient for a future deployment team to cold-start
