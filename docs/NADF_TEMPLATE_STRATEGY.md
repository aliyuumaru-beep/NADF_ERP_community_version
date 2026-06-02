# NADF ERP — Public Sector Template Strategy
**Document:** NADF_TEMPLATE_STRATEGY.md
**Version:** 1.0
**Date:** 2026-06-02
**Status:** DRAFT — Awaiting Operator Review
**Layer:** Software Factory → Platform → **Public Sector ERP Template** → NADF Deployment

---

## Purpose

This document positions the NADF ERP MVP within the Software Factory four-layer architecture and defines the strategic boundary between:

1. What is purely NADF-specific (Layer 4 — Client Deployment)
2. What should become a reusable Public Sector ERP Template (Layer 3 — Industry Template)
3. What should be promoted to the Software Factory governance layer (Layer 1)

This document governs template thinking throughout the NADF implementation. Every configuration decision, CSV template, approval pattern, and documentation asset must be evaluated against this strategy.

---

## 1. Software Factory Positioning

### Current Four-Layer State

```
┌──────────────────────────────────────────────────────────┐
│          Layer 1: Software Factory Governance             │
│  software-factory-governance repository (ACTIVE)          │
└───────────────────────────┬──────────────────────────────┘
                            │ inherits
┌───────────────────────────▼──────────────────────────────┐
│          Layer 2: Platform Layer                          │
│  Odoo 17 Community Edition + shared custom addons         │
│  /Users/mac/odoo17/ (FamOil primary — shared platform)   │
└───────────────────────────┬──────────────────────────────┘
                            │ inherits
┌───────────────────────────▼──────────────────────────────┐
│          Layer 3: Industry Template Layer                  │
│                                                           │
│  ┌─────────────────────┐  ┌─────────────────────────┐   │
│  │ Agro-Processing ERP │  │ Public Sector ERP        │   │
│  │ Template (FamOil)   │  │ Template ← NADF creates  │   │
│  │ [ACTIVE]            │  │ this   [NEW]             │   │
│  └─────────────────────┘  └─────────────────────────┘   │
└───────────────────────────┬──────────────────────────────┘
                            │ inherits
┌───────────────────────────▼──────────────────────────────┐
│          Layer 4: Client Deployment Layer                  │
│                                                           │
│  FamOil (deployed)   WamaCare (deployed)   NADF (this)   │
│                                                           │
└──────────────────────────────────────────────────────────┘
```

### NADF's Strategic Role

NADF is simultaneously:
1. A **Layer 4 Client Deployment** — the live MVP environment for NADF
2. The **origin project** for a new **Layer 3 Public Sector ERP Template**

Just as FamOil was both a client deployment and the origin of the Agro-Processing ERP Template, NADF should be both a working client environment and the seed of a reusable Public Sector ERP Template.

This dual role is intentional. The Software Factory grows stronger with each new deployment if implementation decisions are made with template reuse in mind from the start.

---

## 2. What Is NADF-Specific (Layer 4 Only)

These assets belong exclusively to the NADF deployment. They are not reusable by future public sector clients without significant rework.

| Asset | Why NADF-Specific |
|-------|-------------------|
| NADF company name, logo, registration number | Organisational identity |
| NADF staff names and employee records | Personal data |
| NADF email domain (@nadf.gov.ng) | Organisation-specific |
| NADF-specific job titles (e.g., Executive Secretary) | Org-specific nomenclature |
| Specific budget amounts and cost centre codes | NADF-specific financial data |
| NADF-specific vendor names | Client relationships |
| NADF demo scenario narrative details | Org-specific story |
| NADF user credentials | Security — never committed to Git |
| NADF `CLAUDE.md` cockpit state | Live project state |
| NADF `IMPLEMENTATION_HISTORY.md` entries | Project-specific history |
| NADF `DECISION_LOG.md` specific entries | Project-specific decisions |

---

## 3. What Should Become Public Sector ERP Template Assets (Layer 3)

These assets are generalisable to any Nigerian or West African public sector organisation (government agencies, regulatory bodies, development funds, public institutions, administrative organisations).

### 3.1 Organisational Structure Template

| Asset | Template Value |
|-------|---------------|
| Department structure pattern (Finance, Procurement, HR, Executive Office) | Common across all government agencies |
| Job position hierarchy (Officer → Senior Officer → Manager → Head of Unit → Director → Executive Secretary) | Standard Nigerian government grading pattern |
| Executive signature authority structure | Standard public sector governance |

**Template action:** Extract department and job position CSV templates as `public_sector_departments.csv` and `public_sector_job_positions.csv` in the Public Sector Template.

### 3.2 Chart of Accounts — Public Sector Pattern

| Asset | Template Value |
|-------|---------------|
| Income structure: Grants, Recoveries, Other Income | Standard for donor-funded / government-funded organisations |
| Equity: Accumulated Funds (rather than Share Capital) | Non-profit / government equity structure |
| Expense structure: Salaries, Training, Travel, Utilities, Consultancy, Office Expenses | Standard Nigerian government vote head structure |
| Liability: Pension Payables (PENCOM 18% of basic) | Nigeria-specific — applicable to all government employers |
| Liability: Tax Payables (VAT 7.5%, WHT) | Nigerian compliance — applicable to all |

**Template action:** Create `public_sector_coa_nigeria.csv` as a Public Sector Template chart of accounts, clearly separated from the l10n_ng base.

### 3.3 Approval Workflow Pattern — Nigerian Public Sector

| Asset | Template Value |
|-------|---------------|
| Three-tier procurement approval (threshold-based escalation: Officer → Director → Secretary/DG) | Common pattern across Nigerian MDAs |
| Leave approval chain (Supervisor → Head of Unit → Executive) | Standard public sector leave governance |
| Payment approval with finance review gate | Standard public sector payment control |
| Community Edition workaround for multi-level approval | Applicable to all Odoo Community public sector deployments |
| `base_automation` rules for escalation notification | Reusable pattern |

**Template action:** Extract the full approval configuration pattern as a standalone `PUBLIC_SECTOR_APPROVAL_PATTERNS.md` in the Public Sector Template. This is one of the highest-value template contributions.

### 3.4 Procurement Configuration Template

| Asset | Template Value |
|-------|---------------|
| Product categories: Office Supplies, ICT, Operations | Common across government agencies |
| Warehouse structure: Main Store, ICT Store, Consumables Store | Standard for administrative organisations |
| Sample products: Laptop, Printer, Toner, Office Chair, Internet Subscription | Universal office procurement items |
| Vendor classification: Office Supplies, ICT, Training, Logistics | Standard government vendor classification |
| `purchase_requisition` as approval mechanism | Community Edition pattern applicable to any org |

**Template action:** Create `public_sector_procurement_setup.csv` templates in the Public Sector Template.

### 3.5 HR Configuration Template

| Asset | Template Value |
|-------|---------------|
| Leave types: Annual (21 days), Sick (14 days), Casual (5 days), Maternity (12 weeks), Study | Standard Nigerian Leave Act compliance |
| Leave approval chain configuration | Public sector standard |
| Employee import format with Employee ID, Department, Supervisor | Standard HR import |

**Template action:** Create `public_sector_hr_setup.csv` and `PUBLIC_SECTOR_LEAVE_TYPES.md` in the Public Sector Template.

### 3.6 Demo Scenarios Template

| Asset | Template Value |
|-------|---------------|
| Procurement demo scenario (Requisition → Approval → RFQ → PO → Receipt) | Universal — any org with procurement |
| Leave request demo scenario | Universal — any org with HR |
| Invoice payment demo scenario | Universal — any org with finance |
| Approval delegation demo | Universal — approval governance demo |

**Template action:** Create `PUBLIC_SECTOR_DEMO_SCENARIOS.md` as a reusable demonstration guide for public sector ERP demos.

### 3.7 Nigeria Compliance Extension for Public Sector

| Asset | Template Value |
|-------|---------------|
| PENCOM pension at 18% of basic (10% employer + 8% employee) | All Nigerian employers |
| Employee NHF contribution (2.5%) | All Nigerian employees |
| WHT rates for government procurements (10% on professional services, 5% on goods) | All government procurements |
| IPPIS-awareness notes (government payroll integration context) | Applicable to all MDAs |

**Template action:** Add a `public_sector_addendum` section to the existing `NIGERIA_COMPLIANCE.md` (at the FamOil layer) or create a standalone `NIGERIA_PUBLIC_SECTOR_COMPLIANCE.md` in the Public Sector Template.

---

## 4. What Should Be Promoted to Software Factory Layer (Layer 1)

These assets represent implementation methodology improvements that benefit all future projects, not just public sector ones.

| Asset | Promotion Rationale |
|-------|---------------------|
| Community Edition approval workaround methodology | Applicable to any Community Edition client; should be in Software Factory implementation standards |
| NADF PHASE0 foundation checklist | Can become the standard Phase 0 template for all new client deployments |
| NADF inspection report format | Can become the standard Software Factory client inspection template |
| Parametrised backup script pattern (`backup_nadf.sh`) | Already B-level adapted from FamOil; generalise fully for Software Factory |

**Layer 1 promotion process:** After NADF MVP is validated, extract generalised versions of these assets and submit to the `software-factory-governance` repository as new governance artifacts.

---

## 5. Boundary Rules

When implementing NADF, apply these rules to keep boundaries clean:

### Rule 1 — Template-First Thinking
Before implementing any configuration, ask: *"Can this be made generic enough for the Public Sector Template without adding complexity?"* If yes, implement the generic version and document NADF-specific overrides separately.

### Rule 2 — No Client Data in Templates
CSV templates must contain structural headers and example rows only. Real NADF staff names, budget amounts, and vendor names must remain in Layer 4 (NADF deployment data), not in Layer 3 (template).

### Rule 3 — Separation of Template and Deployment
Any asset that goes into `docs/` of the NADF repo and contains NADF-specific content (names, amounts, org details) is Layer 4. Any asset that contains patterns, structures, or configurations applicable to other public sector organisations is Layer 3 and should be flagged for template promotion.

### Rule 4 — No Duplication of Layer 1 Governance
NADF governance files (CLAUDE.md, DECISION_LOG.md, etc.) inherit Layer 1 standards. They do not restate or rewrite them. NADF-specific additions extend; they do not replace.

### Rule 5 — Log Template Promotion Decisions
Any decision to promote an asset from Layer 4 to Layer 3 must be recorded in the NADF DECISION_LOG with type `GOVERNANCE_EXCEPTION` (or a new type `TEMPLATE_PROMOTION`).

---

## 6. Future Public Sector Template Beneficiaries

The Public Sector ERP Template initiated by NADF is designed to serve:

| Organisation Type | Example |
|------------------|---------|
| Government Agencies | MDAs, parastatals |
| Regulatory Bodies | NAFDAC, CBN, SEC, FIRS equivalents |
| Development Funds | Development finance institutions |
| Public Universities and Research Institutions | Universities, polytechnics |
| Public Health Institutions | NHIS, federal hospitals |
| States and Local Government Authorities | State MDAs |
| Regional Development Commissions | NDDC equivalents |

All of these share:
- Nigerian legal/compliance environment
- Government vote-head expense structure
- Approval-by-authority hierarchy
- Non-profit equity structure (Accumulated Funds)
- PENCOM, NHF, WHT obligations

---

## 7. Template Maturity Milestones

| Milestone | Trigger | Action |
|-----------|---------|--------|
| Template seed | NADF MVP complete and validated | Extract generic assets from NADF; create Public Sector Template placeholder repo |
| Template v0.1 | First template extraction committed | Publish `sf-template-public-sector` repo with seed assets |
| Template v1.0 | Second public sector client deployment | Validate template against second deployment; resolve NADF-specific assumptions |

---

*Document produced by: AI Developer (Claude Code) | Date: 2026-06-02*
*Layer model reference: software-factory-governance/docs/PROJECT_LAYERING_MODEL.md*
*Software Factory structure reference: software-factory-governance/docs/SOFTWARE_FACTORY_STRUCTURE.md*
