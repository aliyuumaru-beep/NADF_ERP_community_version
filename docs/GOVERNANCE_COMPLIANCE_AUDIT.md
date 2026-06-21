# NADF ERP — Software Factory Governance Compliance Audit

**Document:** GOVERNANCE_COMPLIANCE_AUDIT.md
**Audit Date:** 2026-06-13
**Auditor Role:** Independent Software Factory Governance Auditor (non-implementation)
**Scope:** `/Users/mac/nadf_erp/` (NADF ERP, Layer 4 client deployment) against
`/Users/mac/software-factory-governance/` (Layer 1 governance authority), with
`famoil-erp` (`/Users/mac/odoo17/`) used as the maturity comparison baseline.

> This document is an audit only. No remediation has been performed. All findings
> are evidence-based and cite the specific file, command output, or governance
> standard section that supports them.

---

## 1. Executive Summary

NADF ERP has delivered **10 phases of substantive Odoo configuration and two
custom modules** (`nadf_vendor_onboarding`, `nadf_facilities_management`) entirely
**outside the Software Factory governance model**. The project's own Phase 0
planning documents (`NADF_PHASE0_FOUNDATION_PLAN.md`, dated 2026-06-02) correctly
identified the governance scaffolding required before implementation — and that
scaffolding was never built. All four Phase 0 gates (0A–0D) remain unsatisfied,
yet Phases 1–10 proceeded regardless.

**Headline findings:**

1. **The GitHub repository has never been used.** It was created 2026-06-02,
   `isEmpty: true`, `pushedAt == createdAt`, no default branch, branch protection
   API returns `404 Branch not found`. Zero commits, branches, or PRs exist on
   the remote. This is the direct answer to "why haven't I gotten a pull
   request" — PRs require a pushed branch on GitHub, and nothing has ever been
   pushed.
2. **All local work (10 commits + 2 unmerged module trees) sits on `main` with
   no upstream tracking, no feature branches, and no PR history** — a direct
   violation of `GOVERNANCE_STANDARD.md §4.1` (no direct commits to `main` except
   repository initialization).
3. **Mandatory root governance documents are entirely absent**: `CLAUDE.md`,
   `README.md`, `CHANGELOG.md`, `IMPLEMENTATION_HISTORY.md`, `MODULE_REGISTRY.md`,
   `ROADMAP.md` do not exist anywhere in the repository (`GOVERNANCE_STANDARD.md
   §3.1`).
4. **`.github/workflows/` and `.claude/hooks/` directories exist but are empty**
   — the scaffolding was created (likely `mkdir -p`) but never populated, unlike
   `famoil-erp` which has all 4 workflows and 6 hooks operational.
5. **Two completed custom Odoo modules
   (`nadf_vendor_onboarding`, `nadf_facilities_management`) exist only as
   untracked files inside `famoil-erp`'s working tree** (`/Users/mac/odoo17/custom_addons/`)
   — they are not committed to *any* git repository, anywhere. This is a
   data-loss risk independent of all other findings.
6. **No backup, no restore drill, and no offsite copy exists for the `NADF`
   PostgreSQL database**, despite `NADF_PHASE0_FOUNDATION_PLAN.md §6.3` declaring
   a restore drill "a non-negotiable gate" before any user-facing demo.
7. **`famoil-erp` (the maturity baseline) is itself non-compliant with
   `GITHUB_RULESET_BASELINE.md`** — branch protection on its `main` also returns
   `404 Branch not protected`, despite an active feature-branch/PR workflow with
   14+ merged PRs. Only `software-factory-governance` (Layer 1) has an active
   ruleset and CI enforcement.

**Bottom line:** NADF is operating at **Governance Maturity Level 0 (Ad Hoc /
Bootstrap)** against a governance standard that defines Level 4 (Mature) as the
target and explicitly gates Phase 1 on Level 1 being reached first. The project's
own documentation already diagnosed this; the diagnosis was never acted on.

---

## 2. Governance Compliance Matrix

Legend: **PASS** = fully implemented and effective · **PARTIAL** = exists but
incomplete, ineffective, or inconsistent · **FAIL** = required but absent ·
**N/A** = not applicable given current state.

### 2.1 Repository Governance

| Control | Required | Implemented | Effective | Status |
|---|---|---|---|---|
| Git initialized | `GOVERNANCE_STANDARD.md §3` | Yes — local repo, 8–10 commits on `main` | Yes | PASS |
| GitHub remote configured | `GOVERNANCE_STANDARD.md §3` | `origin` → `aliyuumaru-beep/NADF_ERP_community_version` | No — repo `isEmpty: true`, never pushed | PARTIAL |
| Main branch exists remotely | Implicit prerequisite for PR/branch protection | No — `defaultBranchRef.name: ""`, `git ls-remote --heads origin` returns nothing | No | FAIL |
| Upstream tracking configured | Implicit (`git push -u`) | No — `git branch -vv` shows `main` with no tracking ref | No | FAIL |
| Branch protection enabled | `GITHUB_RULESET_BASELINE.md §1.0, §4.1, §7` (activation gate, must precede first AI/contributor write access) | No — `gh api .../branches/main/protection` → `404 Branch not found` (no branch exists to protect) | No | FAIL |
| Feature branch workflow enforced | `GOVERNANCE_STANDARD.md §4.1`; `NADF_PHASE0_FOUNDATION_PLAN.md §7.1` defines `phase/0-foundation` … `phase/6-demo` | No — all 8 original commits + 2 untracked module trees on `main`; no `phase/*` or `feature/*` branches ever created | No | FAIL |
| PR workflow enforced | `PR_GOVERNANCE_STANDARD.md §2.0, §6.0` | No — 0 PRs ever opened (none possible; remote has no branches) | No | FAIL |
| `.github/PULL_REQUEST_TEMPLATE.md` present | `GITHUB_RULESET_BASELINE.md §4.4`, `PR_GOVERNANCE_STANDARD.md §2.0` | No — `.github/workflows/` exists but is empty; no `PULL_REQUEST_TEMPLATE.md` anywhere | No | FAIL |
| Squash merge / merge strategy configured | `GITHUB_RULESET_BASELINE.md §4.3` | N/A — no remote branches exist to merge | N/A | N/A |
| Release tagging policy | `RELEASE_TAGGING_STANDARD.md §2.0` (tag at every phase completion) | No — `git tag -l` returns empty (0 tags across 8–10 completed phases) | No | FAIL |
| Secret scanning / Dependabot | `GITHUB_RULESET_BASELINE.md §4.5` | Unknown/No — cannot configure on empty repo with no default branch | No | FAIL |

### 2.2 Documentation Governance

| Control | Required | Implemented | Effective | Status |
|---|---|---|---|---|
| `CLAUDE.md` (root) | `GOVERNANCE_STANDARD.md §3.1`, `DOCUMENTATION_STANDARD.md §5.0` | No — does not exist; `NADF_PHASE0_FOUNDATION_PLAN.md §1.1` planned it at `/Users/mac/nadf_erp/CLAUDE.md`, never created | No | FAIL |
| `README.md` (root) | `GOVERNANCE_STANDARD.md §3.1`, `DOCUMENTATION_STANDARD.md §4.0` | No | No | FAIL |
| AI onboarding sequence possible | `AI_ONBOARDING_STANDARD.md §2.1–2.6` (7-step mandatory sequence reading governance + project `CLAUDE.md`, `IMPLEMENTATION_HISTORY.md`, `DECISION_LOG.md`, `MODULE_REGISTRY.md`, `ROADMAP.md`) | No — 4 of the 5 project-level documents the sequence requires do not exist | No | FAIL |
| `DECISION_LOG.md` | `GOVERNANCE_STANDARD.md §3.1`, `DECISION_LOG_STANDARD.md §5.0` (root level) | Partial — exists at `docs/DECISION_LOG.md` (not repo root), 8 well-formed entries (DEC-001…DEC-008) following the standard's exact field structure | Partially — content quality is high, location is wrong, and it stops at 2026-06-04 (Phase 5) with no entries for Phases 6–10 | PARTIAL |
| `IMPLEMENTATION_HISTORY.md` | `GOVERNANCE_STANDARD.md §3.1`, `IMPLEMENTATION_HISTORY_STANDARD.md §5.0` | No — does not exist; `NADF_PHASE0_FOUNDATION_PLAN.md §1.3` pre-drafted `IMP-001` for it, never committed | No | FAIL |
| `CHANGELOG.md` | `GOVERNANCE_STANDARD.md §3.1` | No | No | FAIL |
| `ROADMAP.md` / `docs/NADF_ROADMAP.md` | `GOVERNANCE_STANDARD.md §3.1`, `ROADMAP_STANDARD.md §4.0` | No | No | FAIL |
| `MODULE_REGISTRY.md` | `GOVERNANCE_STANDARD.md §3.1`, `REGISTRY_STANDARD.md §5.0` | No | No | FAIL |
| `docs/IMPLEMENTATION_STANDARDS.md` (inherited rules) | `NADF_PHASE0_FOUNDATION_PLAN.md §1.1` (B-level adapt from FamOil) | No | No | FAIL |
| `docs/architecture/ARCHITECTURAL_PRINCIPLES.md` (inherited) | Same | No | No | FAIL |
| `docs/ONBOARDING_GUIDE.md` | `NADF_PHASE0_FOUNDATION_PLAN.md §1.1` | No | No | FAIL |
| NADF-specific planning docs (inspection, asset assessment, template strategy, approval workflows, demo scenarios, Phase 0 plan) | Project-specific, high quality | Yes — 6 documents present in `docs/`, well-structured and self-aware about gaps | Yes, as planning artifacts; not acted on | PASS (as planning), but see §3 |

### 2.3 CI/CD Governance

| Control | Required | Implemented | Effective | Status |
|---|---|---|---|---|
| `doc_lint.yml` (mandatory-docs enforcement) | `NADF_PHASE0_FOUNDATION_PLAN.md §2.1`; modeled on `famoil-erp/.github/workflows/doc_lint.yml` (active) | No — `.github/workflows/` directory exists but contains 0 files | No | FAIL |
| `security_scan.yml` (secret scan) | Same; A-level direct copy planned | No | No | FAIL |
| `ci_review.yml` (Claude governance review on PR) | Same; B-level adapt planned | No | No | FAIL |
| `backup_check.yml` | Same; B-level adapt planned | No | No | FAIL |
| `.claude/settings.json` + 6 hook scripts (`pre_tool_guard.sh`, `post_tool_validator.sh`, `audit_logger.sh`, `file_protection_guard.sh`, `session_start_loader.sh`, `session_end_reporter.sh`) | `NADF_PHASE0_FOUNDATION_PLAN.md §3` | No — `.claude/hooks/` directory exists, contains 0 files; `.claude/settings.json` does not exist | No | FAIL |
| Workflow execution (any workflow has ever run) | Implicit | No — `gh api .../actions/workflows` not queryable (repo empty, no default branch) | No | FAIL |
| Workflow enforcement (required status checks gating merge) | `GITHUB_RULESET_BASELINE.md §4.1` | No | No | FAIL |

### 2.4 Continuity Governance

| Control | Required | Implemented | Effective | Status |
|---|---|---|---|---|
| Repository memory artifact set complete (`DECISION_LOG.md`, `IMPLEMENTATION_HISTORY.md`, `MODULE_REGISTRY.md`, `ROADMAP.md`, `CHANGELOG.md`, `CLAUDE.md`) | `REPOSITORY_MEMORY_PRINCIPLES.md §1.0` | 1 of 6 present (`docs/DECISION_LOG.md`, wrong location) | No — AI agents cannot regain session context per the defined priority hierarchy | FAIL |
| Onboarding completeness (AI can complete `AI_ONBOARDING_STANDARD.md` §2.1–2.7 at session start) | `AI_ONBOARDING_STANDARD.md §5.0` requires: if mandatory docs missing, **stop and report before proceeding** | No — no governance `CLAUDE.md`, no project `CLAUDE.md`; sessions have proceeded through 10 phases without the AI agent halting per §5.0 | No | FAIL |
| Roadmap authority over scope (AI does not implement future-phase work without instruction) | `ROADMAP_STANDARD.md §5.3` | No formal roadmap exists to bound scope; phase sequencing has instead been managed informally via session memory/`MEMORY.md` (an *AI* memory artifact, which `REPOSITORY_MEMORY_PRINCIPLES.md §2.0` ranks **below** repository memory) | Partial — phases have proceeded in a sensible order so far, but with no committed authority | PARTIAL |
| Institutional memory of 10 completed phases | `IMPLEMENTATION_HISTORY_STANDARD.md §6.1` (update at conclusion of every phase) | No — zero `IMPLEMENTATION_HISTORY.md` entries exist for any of the 10 phases | No | FAIL |

### 2.5 Backup Governance

| Control | Required | Implemented | Effective | Status |
|---|---|---|---|---|
| Backup scripts (`scripts/backup_nadf.sh`, `scripts/restore_nadf.sh`) | `NADF_PHASE0_FOUNDATION_PLAN.md §6.1`, modeled on `famoil-erp`'s operational `backup_famoil.sh` | No — neither script exists in `scripts/` (12 phase-runner scripts exist, no backup/restore scripts) | No | FAIL |
| Scheduled backups (launchd `com.nadf.backup.daily.plist`) | `NADF_PHASE0_FOUNDATION_PLAN.md §6.2` | No | No | FAIL |
| Offsite backup (rclone → Google Drive, per FamOil pattern, `famoil-erp` tag `v1.3.0-offsite-backup-operational`) | `BACKUP_RECOVERY_STANDARD.md §2.0` (custom code/data backed up to remote, remote confirmed accessible) | No | No | FAIL |
| `docs/BACKUP_AND_RECOVERY.md` | `NADF_PHASE0_FOUNDATION_PLAN.md §1.1, §6.3` | No | No | FAIL |
| Restore drill evidence (`RESTORE_EVENT` in `IMPLEMENTATION_HISTORY.md`) | `RESTORE_DRILL_STANDARD.md §7.0`; `NADF_PHASE0_FOUNDATION_PLAN.md §6.3` calls this "a non-negotiable gate ... before the MVP is presented to any NADF users" | No — no drill performed, no `IMPLEMENTATION_HISTORY.md` to record it in | No | FAIL |
| RPO/RTO defined | `BACKUP_RECOVERY_STANDARD.md §6.0` | No | No | FAIL |

> **Risk context:** the `NADF` PostgreSQL database alone contains 10 phases of
> configuration — 319-account CoA, 421 maintenance equipment records, 61 fixed
> assets, 5 fleet vehicles, 77 helpdesk tickets, 25 employee records, full
> approval-workflow automation, and live vendor-onboarding/facilities data. None
> of this has a backup of any kind on record.

### 2.6 Odoo / Software Factory Governance

| Control | Required | Implemented | Effective | Status |
|---|---|---|---|---|
| Configuration-first approach (Principle 1 — Platform-Native First) | `ARCHITECTURAL_PRINCIPLES.md §1.0`; `OVERENGINEERING_GUARDRAILS.md §2.2, §2.5` | Yes — Phases 1–8 are pure configuration; DEC-002/DEC-005/DEC-006/DEC-007 explicitly document choosing native config + `base.automation` workarounds over custom code, with rationale and "Revisit Conditions" | Yes | PASS |
| Custom code as last resort, and logged when chosen (Principle 1: "When native capability is rejected in favor of custom code, the reason MUST be logged ... type `CUSTOM_CODE`") | `ARCHITECTURAL_PRINCIPLES.md §1.0` | Partial — Phases 9–10 introduced two full custom modules (`nadf_vendor_onboarding`, `nadf_facilities_management`). No `CUSTOM_CODE`-type entry exists in `docs/DECISION_LOG.md` (which stops at DEC-008, 2026-06-04, before either module was built) | No | FAIL |
| Module registry covers all custom modules / integrations / scripts | `REGISTRY_STANDARD.md §2.0, §3.0` (registration before/at same time as merge — retroactive registration is itself a `GOVERNANCE_EXCEPTION`) | No `MODULE_REGISTRY.md` exists at all. Unregistered artifacts include: 2 custom Odoo modules, 1 external AI integration (`anthropic` SDK / Claude API call from `nadf_vendor_onboarding`), 12 phase-runner scripts, and the shared OCA addons (`om_account_*`, `accounting_pdf_reports`) consumed via DEC-003 | No | FAIL |
| Addon/Layer governance — client-specific code stays in client layer (Layer 4), no cross-project bleed | `PROJECT_LAYERING_MODEL.md §3.4, §4.3` (dependencies flow downward only; Layer 4 projects must not contain each other's code) | No — `nadf_vendor_onboarding/` and `nadf_facilities_management/` (NADF, Layer 4) physically live as **untracked files inside `famoil-erp`'s working tree** (`/Users/mac/odoo17/custom_addons/`, also Layer 4). `nadf_erp/custom_addons/` is empty. DEC-003 logged the *shared addons path* decision but not this consequence | No | FAIL |
| Reusable-asset / Layer 3 classification discipline | `PROJECT_LAYERING_MODEL.md §3.3, §4.1–4.2`; `NADF_TEMPLATE_STRATEGY.md`, `NADF_REUSABLE_ASSET_ASSESSMENT.md` | Yes — both documents exist, classify 67 assets into A/B/C reuse categories, and correctly scope Layer 3 vs Layer 4 candidates | Partial — classification done but no artifact has actually been promoted to Layer 3, and no Layer 3 repos exist yet (consistent with Software Factory's current state per `PROJECT_LAYERING_MODEL.md §5.0`) | PARTIAL |

---

## 3. Governance Violations

### VIOLATION-001 — GitHub repository never activated; all governance scaffolding bypassed
- **Description:** The NADF GitHub repository was created 2026-06-02 and has never received a push. `NADF_PHASE0_FOUNDATION_PLAN.md` — dated the same day — explicitly defines Gate 0B ("Governance Enforcement Active": hooks, CI workflows, `.claude/settings.json`, backup scripts) and states "Only after all Gate 0 checks are satisfied may Phase 1 begin." Phase 1 began anyway, the same day or shortly after.
- **Severity:** Critical
- **Date:** 2026-06-02 (plan written) → ongoing through 2026-06-11+ (Phases 1–10 delivered)
- **Root Cause:** No automated or procedural gate exists to *block* Phase 1 work when Gate 0 checklist items are unchecked. The gate is documentation-only and was not enforced by tooling, by the AI agent's own session discipline, or by operator sign-off recorded in `DECISION_LOG.md`.
- **Impact:** Branch protection, PR review, CI checks (doc-lint, secret-scan, governance review), AI tool-use guardrails (`pre_tool_guard.sh`, `file_protection_guard.sh`), and backup automation were all bypassed for the entire project lifetime to date. No external review has occurred on any of the ~10 phases of work.
- **Prevention:** A **Mandatory Governance Activation Gate** (see §6) that a session cannot proceed past Phase 0 without either (a) all Gate 0A/0B checklist items present as files on disk, verified by a script, or (b) an explicit `GOVERNANCE_EXCEPTION` entry in `DECISION_LOG.md` naming the Software Factory lead who approved deferral and a remediation deadline.

### VIOLATION-002 — Direct commits to `main` with no feature-branch/PR workflow
- **Description:** All 8 original commits (Phase 0 through Phase 8) plus subsequent Phase 9/10 work were committed directly to `main`. `NADF_PHASE0_FOUNDATION_PLAN.md §7.1` defines a `phase/0-foundation` … `phase/6-demo` branch model; none of these branches were ever created (`git branch -a` shows only `main`).
- **Severity:** High
- **Date:** 2026-06-02 through present (ongoing)
- **Root Cause:** `GOVERNANCE_STANDARD.md §4.1`'s "repository initialization (first commit only)" exception was treated as covering *all* commits, not just the first.
- **Impact:** No PR-based review checkpoint exists anywhere in the project history. `PR_GOVERNANCE_STANDARD.md`'s entire apparatus (Governance Impact Analysis, Repository Memory Review, rollback plans, final governance declaration) has never been exercised on this project.
- **Prevention:** Branch protection (once the remote `main` exists) with "require PR before merging" + "block force pushes" + "require linear history" per `GITHUB_RULESET_BASELINE.md §4.1`, applied **before** any further commits are pushed.

### VIOLATION-003 — Two completed custom modules exist in zero version-controlled locations
- **Description:** `nadf_vendor_onboarding` (Phase 9, complete with smoke tests per project memory) and `nadf_facilities_management` (Phase 10, in progress) are physically located at `/Users/mac/odoo17/custom_addons/`, which is the working tree of the **`famoil-erp`** repository. `git ls-files` in `famoil-erp` confirms these directories are untracked. `nadf_erp/custom_addons/` is empty. Neither repository has these modules committed.
- **Severity:** Critical
- **Date:** Discovered 2026-06-13 (modules built progressively from ~2026-06-09 onward per project memory)
- **Root Cause:** DEC-003 ("Shared Addons Path Strategy") justified *reading* shared OCA addons from `famoil-erp`'s `custom_addons/` for dependency reasons, but NADF's own new modules were also written into that same shared directory rather than `nadf_erp/custom_addons/` (which the Phase 0 plan and `nadf.conf`'s `addons_path` both reserve for NADF-specific code). No decision log entry covers writing NADF-original code into FamOil's tree.
- **Impact:** Two phases of completed Odoo development have **no backup, no remote copy, and no recovery path** if `/Users/mac/odoo17/custom_addons/` is lost, cleaned, or `famoil-erp`'s working tree is reset. This also pollutes `famoil-erp`'s working tree with another client's code, violating `PROJECT_LAYERING_MODEL.md §4.3` (Layer 4 projects must not contain each other's artifacts).
- **Prevention:** Move both module directories into `nadf_erp/custom_addons/`, update `nadf.conf`'s `addons_path` accordingly, commit them to `nadf_erp` with `MODULE_REGISTRY.md` entries (`MOD-001`, `MOD-002`), and log a `DECISION_LOG.md` entry (type `ARCHITECTURE`, referencing/superseding DEC-003's scope).

### VIOLATION-004 — Zero backups of the `NADF` database; restore drill never performed
- **Description:** `NADF_PHASE0_FOUNDATION_PLAN.md §6.3` declares a restore drill "non-negotiable" before MVP presentation to users. No `scripts/backup_nadf.sh`/`restore_nadf.sh` exist, no `docs/BACKUP_AND_RECOVERY.md` exists, and no `IMPLEMENTATION_HISTORY.md` (which doesn't exist) records any `RESTORE_EVENT`.
- **Severity:** Critical
- **Date:** Ongoing since Phase 1 (database created 2026-06-02)
- **Root Cause:** Backup tooling was scoped in Phase 0 planning as B-level adaptations from FamOil's operational `backup_famoil.sh`, but Phase 0 was never completed (see VIOLATION-001), so the adaptation never happened.
- **Impact:** 10 phases of configuration data (CoA, assets, fleet, HR, helpdesk, vendor/facilities application data) exist only in a single local PostgreSQL instance with no redundancy.
- **Prevention:** Adapt `famoil-erp`'s `backup_famoil.sh`/offsite-rclone pattern (already proven at `v1.3.0-offsite-backup-operational`) for NADF before any further configuration work; perform and record one restore drill per `RESTORE_DRILL_STANDARD.md §3.0`.

### VIOLATION-005 — Repository memory artifacts not maintained past Phase 5
- **Description:** `docs/DECISION_LOG.md` contains DEC-001 through DEC-008, all dated 2026-06-02 to 2026-06-04 (Phases 0–5). Phases 6 through 10 — including the introduction of two custom modules and an external AI/API integration (`nadf_vendor_onboarding`'s Claude API call) — have **no corresponding decision log entries**, despite `DECISION_LOG_STANDARD.md §2.0` requiring entries for "technology or dependency choice" (the `anthropic` SDK) and "integration pattern decision" (the AI analysis pipeline).
- **Severity:** Medium
- **Date:** Gap begins 2026-06-04
- **Root Cause:** No `IMPLEMENTATION_HISTORY.md` or `MODULE_REGISTRY.md` exists to prompt entries at phase boundaries (`IMPLEMENTATION_HISTORY_STANDARD.md §6.1`: update "at conclusion of each project phase").
- **Impact:** Future sessions/auditors cannot determine why the AI integration was chosen, what alternatives were considered, or what its data-handling implications are (`SECURITY_STANDARD.md §5.0` — personal/financial data handling should be identified).
- **Prevention:** Backfill `DEC-009` (AI vendor-application analysis via Claude API — type `INTEGRATION`/`TECHNOLOGY`) and `DEC-010` (facilities management module — type `ARCHITECTURE`/`CUSTOM_CODE`) as part of the same remediation pass that creates `MODULE_REGISTRY.md`.

### VIOLATION-006 — Operator approval gate (Gate 0D) has no recorded evidence
- **Description:** `NADF_PHASE0_FOUNDATION_PLAN.md §9, Gate 0D` requires recorded operator approval of the Phase 0 plan and an explicit confirmation to proceed to Phase 1. `DEC-004` confirms the fiscal-year question (one of the three Gate 0D items) was answered, but no entry confirms "Operator has reviewed and approved this Phase 0 Foundation Plan" or "Operator has confirmed: proceed to Phase 1."
- **Severity:** Medium
- **Date:** 2026-06-02
- **Root Cause:** The Phase 0 document was marked `Status: DRAFT — Awaiting Operator Review` and never updated to `APPROVED`.
- **Impact:** No audit trail demonstrates the operator consciously accepted the risk of proceeding without Gate 0A/0B/0C being satisfied — it appears to have happened by default/momentum rather than decision.
- **Prevention:** Any future "skip a gate" decision must be an explicit, dated `GOVERNANCE_EXCEPTION` entry in `DECISION_LOG.md`, not a status field left in `DRAFT`.

### VIOLATION-007 (baseline comparison, not NADF-specific) — `famoil-erp` main branch lacks branch protection despite mature PR workflow
- **Description:** `famoil-erp` has 4 active CI workflows, 6 active Claude hooks, and a real feature-branch/PR history (PRs #6, #7, #11–#14 visible in commit messages). However `gh api repos/aliyuumaru-beep/famoil-erp/branches/main/protection` returns `404 Branch not protected`.
- **Severity:** Medium (affects Layer 4 baseline quality, not NADF directly, but is the template NADF is meant to inherit)
- **Date:** Ongoing
- **Root Cause:** `GITHUB_RULESET_BASELINE.md §8.0`'s own non-compliance note anticipated this: "The Software Factory lead should apply these settings ... before Phase 2 adoption of any project repository begins, so FamOil and WamaCare are set up correctly from the start." This was never done for FamOil either.
- **Impact:** Even the project NADF is meant to copy governance from does not fully meet the GitHub-side baseline — meaning NADF cannot "inherit" a correctly configured remote even if it copies FamOil's `.github/` and `.claude/` directories verbatim.
- **Prevention:** Apply `GITHUB_RULESET_BASELINE.md §4.2` ruleset to `famoil-erp/main` (only `software-factory-governance` currently has this), then replicate to NADF once its remote `main` exists.

---

## 4. Governance Maturity Assessment

Maturity levels per `GOVERNANCE_STANDARD.md §13.0`:
Level 0 Ad Hoc · Level 1 Documented · Level 2 Repeatable · Level 3 Governed ·
Level 4 Automated · Level 5 Software Factory.

| Project | Level | Justification |
|---|---|---|
| **Software Factory overall** (`software-factory-governance`) | **Level 4 (Automated)**, trending toward 5 | 20 governance standard documents, all templates present, active GitHub ruleset (`software-factory-governance-v1`), 3 active CI workflows (doc-lint, governance-validate, secret-scan) on its own repo. Gap to Level 5: the standards are not yet *enforced* on the Layer 4 projects they govern (FamOil, NADF) — enforcement stops at the governance repo's own boundary. |
| **FamOil** (`famoil-erp`) | **Level 2–3 (Repeatable / partially Governed)** | Strong repeatable practice: feature branches, PR merges (#6–#14), conventional commits, release tags (`v1.2.0`…`v1.5.0`), full `.github/workflows/` and `.claude/hooks/` populated and presumably running, restore drill performed (`v1.5.0-restore-validated`, `feature/restore-drill-report` — "partial pass, ir_attachment gap found"). Falls short of Level 3 "Enforced": no branch protection/ruleset on `main` (VIOLATION-007), and current working tree has uncommitted changes plus foreign (NADF) untracked directories. |
| **NADF** (`nadf_erp`) | **Level 0 (Ad Hoc / Bootstrap)** | Per `GOVERNANCE_STANDARD.md §13.0`, Level 0 = "repository initialized, root files created." NADF has the repository initialized but **none** of the mandatory root files exist. Excellent *planning* documents exist (Phase 0 plan, inspection report, asset assessment, template strategy) — these represent Level 1-quality thinking — but none of the planned artifacts were instantiated, so the project cannot be credited above Level 0 on the implemented state. |

---

## 5. Gap Analysis

Synthesizing §2–4, NADF's gap to its own stated Phase 0 target breaks down as:

| Area | Target (per NADF's own Phase 0 plan) | Actual | Gap |
|---|---|---|---|
| Root governance docs | 7 files (`CLAUDE.md`, `README.md`, `CHANGELOG.md`, `PROJECT_FACTORY_MANUAL.md`, + `docs/{DECISION_LOG,IMPLEMENTATION_HISTORY,IMPLEMENTATION_STANDARDS,MODULE_REGISTRY,NADF_ROADMAP,BACKUP_AND_RECOVERY,ONBOARDING_GUIDE}.md`) | 1 of 12 (`docs/DECISION_LOG.md`, partial) | 11 missing |
| CI/CD workflows | 4 (`doc_lint`, `security_scan`, `ci_review`, `backup_check`) | 0 (empty directory) | 4 missing |
| Claude governance hooks | 6 hooks + `settings.json` | 0 (empty directory) | 7 missing |
| Backup/restore tooling | `backup_nadf.sh`, `restore_nadf.sh`, daily launchd job, offsite rclone | 0 | 4 missing |
| Git/GitHub setup | Pushed `main`, branch protection, PR-only merges, release tags | Empty remote, no protection, 0 PRs, 0 tags | Full gap |
| Module registry | All custom modules + scripts registered | Not started | Full gap |
| Custom module location | `nadf_erp/custom_addons/` | `famoil-erp`'s `custom_addons/`, untracked | Misplaced + unrecoverable |

**Net assessment:** roughly **2 of ~30 planned governance artifacts exist**
(the planning docs themselves, and a partial decision log). The estimated "~4
hours" of Phase 0 effort in the plan was never spent, while an estimated
several hundred hours of Phase 1–10 implementation work proceeded on top of
that missing foundation.

---

## 6. Recommended Improvements

### Critical (implement immediately)

1. **Recover the orphaned custom modules.** Move `nadf_vendor_onboarding/` and
   `nadf_facilities_management/` from `famoil-erp`'s working tree into
   `nadf_erp/custom_addons/`, update `nadf.conf`'s `addons_path`, and commit
   them to `nadf_erp`.
   - *Benefit:* eliminates the single largest data-loss risk in the project.
   - *Risk mitigated:* total loss of ~2 phases of Odoo development with no backup.
   - *Effort:* Low (file move + config edit + commit).
   - *Priority:* P0.

2. **Stand up backup + restore drill for the `NADF` database**, adapting
   `famoil-erp`'s proven `backup_famoil.sh` / offsite-rclone pattern, and record
   one passing drill.
   - *Benefit:* satisfies the "non-negotiable" Phase 0 §6.3 gate; protects 10
     phases of configuration data.
   - *Risk mitigated:* unrecoverable loss of the entire NADF database.
   - *Effort:* Medium (script adaptation ~1–2 hrs, drill ~1 hr).
   - *Priority:* P0.

3. **Push `main` to GitHub and apply the `GITHUB_RULESET_BASELINE.md §4.2`
   ruleset** (require PR + 1 approval, dismiss stale reviews, block force-push,
   restrict deletions, linear history).
   - *Benefit:* this is the literal fix for the original question — PRs cannot
     exist until a branch exists on GitHub to open them against.
   - *Risk mitigated:* unreviewed changes to `main`; unrecoverable force-pushes.
   - *Effort:* Low (one push + GitHub ruleset configuration).
   - *Priority:* P0.

### High Priority

4. **Create the 7 mandatory root documents** (`CLAUDE.md`, `README.md`,
   `CHANGELOG.md`, `IMPLEMENTATION_HISTORY.md`, `MODULE_REGISTRY.md`,
   `ROADMAP.md`, plus relocate/duplicate `DECISION_LOG.md` to root per
   `GOVERNANCE_STANDARD.md §3.1`), seeding `IMPLEMENTATION_HISTORY.md` with
   retroactive `PHASE_COMPLETE` entries for Phases 0–10.
   - *Benefit:* restores AI-agent onboarding capability (`AI_ONBOARDING_STANDARD.md`);
     restores institutional memory.
   - *Risk mitigated:* future sessions re-doing or contradicting completed work.
   - *Effort:* Medium (mostly retroactive documentation, ~3–4 hrs).
   - *Priority:* P1.

5. **Populate `.github/workflows/` and `.claude/` from the `famoil-erp`
   pattern**, adapted per `NADF_PHASE0_FOUNDATION_PLAN.md §2–3` (project name,
   port 8071, DB `NADF`, mandatory-docs list).
   - *Benefit:* automated doc-lint/secret-scan/governance-review enforcement;
     AI tool-use guardrails active for future sessions.
   - *Risk mitigated:* repeat of the current "no enforcement" state for all
     future work.
   - *Effort:* Medium (mostly copy + find/replace, ~1–2 hrs).
   - *Priority:* P1.

6. **Create `MODULE_REGISTRY.md`** and register: `nadf_vendor_onboarding`,
   `nadf_facilities_management`, the `anthropic`/Claude API integration, the 12
   phase-runner scripts, and the shared OCA addons consumed via DEC-003.
   - *Benefit:* prevents duplicate-effort and undocumented dependencies.
   - *Risk mitigated:* invisible technical debt; unregistered integrations
     (especially the external AI API call, which has security/data implications).
   - *Effort:* Medium.
   - *Priority:* P1.

7. **Backfill decision log entries DEC-009/DEC-010** for the Phase 9/10 custom
   modules and AI integration, per `DECISION_LOG_STANDARD.md §2.0`.
   - *Benefit:* closes the institutional-memory gap since 2026-06-04.
   - *Risk mitigated:* future contradiction/reversal of undocumented decisions.
   - *Effort:* Low.
   - *Priority:* P1.

### Medium Priority

8. **Apply `GITHUB_RULESET_BASELINE.md §4.2` to `famoil-erp/main`** (currently
   unprotected despite active PR workflow) so the project NADF is meant to
   inherit from is itself compliant (VIOLATION-007).
   - *Benefit:* fixes the inheritance source, not just the copy.
   - *Risk mitigated:* force-push/unreviewed-merge risk on the more mature,
     more valuable FamOil repo.
   - *Effort:* Low.
   - *Priority:* P2.

9. **Retroactive release tags** for NADF Phases 1–10 (`v0.x.0-phaseN` per
   `RELEASE_TAGGING_STANDARD.md §3.0`), once `main` is pushed.
   - *Benefit:* gives the project a navigable history of deployed states.
   - *Risk mitigated:* inability to identify/rollback to a known-good phase
     boundary.
   - *Effort:* Low.
   - *Priority:* P2.

### Optional

10. **Define RPO/RTO for NADF** in `DECISION_LOG.md` per
    `BACKUP_RECOVERY_STANDARD.md §6.0` once backups exist — likely generous
    given MVP/demo status, but should be stated rather than implicit.
    - *Benefit:* makes implicit risk tolerance explicit and reviewable.
    - *Risk mitigated:* mismatched expectations if NADF moves toward production.
    - *Effort:* Low.
    - *Priority:* P3.

---

## 7. Revised Governance Activation Gate

### Question: Should NADF have been allowed to start implementation (Phase 1)?

**Answer: FAIL**

**The exact gate that should have blocked implementation:**
`NADF_PHASE0_FOUNDATION_PLAN.md §9, Gate 0B — "Governance Enforcement Active"`,
combined with the document's own closing line: *"Only after all Gate 0 checks
are satisfied may Phase 1 begin."* At the time Phase 1 began (2026-06-02), Gate
0A was at best 2/12 (17%) and Gate 0B was 0/6 (0%) — both far below the
all-or-nothing bar the document itself sets.

**Why this gate failed to block anything:** the gate existed only as
checkboxes in a markdown file with `Status: DRAFT`. Nothing — no script, no
hook, no CI check, no session-start ritual — actually *read* that file and
*compared it against the filesystem* before allowing Phase 1 work to begin.
The gate was advisory, and advisory gates do not gate.

### Recommended modification to Software Factory governance so future projects cannot bypass this gate

Add to `software-factory-governance/onboarding/AI_ONBOARDING_STANDARD.md` (or
a new `governance/ACTIVATION_GATE_STANDARD.md`) a **machine-checkable Phase 0
Activation Gate**:

1. Every new Layer-4 client repository must contain a
   `scripts/check_governance_gate.sh` (copied unmodified from
   `software-factory-governance`, Layer 1) that checks for the presence and
   non-emptiness of: the 7 mandatory root documents, `.github/workflows/*.yml`
   (4 files), `.claude/hooks/*.sh` (6 files) + `.claude/settings.json`,
   `scripts/backup_*.sh` + `scripts/restore_*.sh`, and a remote `main` branch
   with branch protection/ruleset active (checked via `gh api`).
2. **`AI_ONBOARDING_STANDARD.md §2` (the mandatory AI session-start sequence)
   must run this script before Step 1**, for any repository whose
   `IMPLEMENTATION_HISTORY.md` does not yet contain a `PHASE_COMPLETE` entry for
   "Phase 0" / "Foundation". If the script reports any FAIL, the AI agent's
   onboarding completion statement (`AI_ONBOARDING_STANDARD.md §6.0`) must be
   replaced with an explicit halt: *"Governance Activation Gate FAILED — N of M
   checks missing. I will not proceed to implementation work until these are
   resolved or a GOVERNANCE_EXCEPTION is logged in DECISION_LOG.md by the
   Software Factory lead."*
3. This converts Gate 0B from a markdown checklist (read, in practice, never)
   into a command (`./scripts/check_governance_gate.sh`) that any session — AI
   or human — runs automatically and cannot talk itself past, mirroring how
   `software-factory-governance` already enforces its *own* standards via CI
   (`governance-validate.yml`) but extending that enforcement down to Layer 4
   at session-start time rather than push-time, since Layer 4 projects currently
   demonstrate they can accumulate 10 phases of work without ever pushing.

---

## 8. Overall Audit Verdict

**NON-COMPLIANT.**

NADF ERP has produced substantial, technically competent Odoo configuration
and two functioning custom modules, built on top of *zero* of the governance
infrastructure its own Phase 0 planning correctly specified as prerequisite.
The project's planning documents (`NADF_MVP_INSPECTION_REPORT.md`,
`NADF_REUSABLE_ASSET_ASSESSMENT.md`, `NADF_PHASE0_FOUNDATION_PLAN.md`,
`docs/DECISION_LOG.md`) demonstrate the governance model was understood — the
failure is one of **activation and enforcement, not comprehension**.

The original question — "why haven't I gotten a pull request from GitHub" — has
a precise answer: **a PR is a property of a pushed branch on GitHub, and no
branch of this repository has ever been pushed.** This is symptom, not root
cause; the root cause is documented above as VIOLATION-001 through
VIOLATION-006, and the remediation path is the Critical/High items in §6,
sequenced as: recover orphaned modules → secure backups → push `main` and apply
branch protection → restore documentation/registry → re-establish CI/hooks →
resume phase work under the now-active gate.

No changes have been made to the repository, GitHub configuration, or any
file as part of this audit.
