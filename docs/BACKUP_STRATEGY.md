# NADF ERP — Backup & Recovery Strategy

**Document type:** Mandatory governance artifact (Governance Activation Gate D)
**Standard:** `20_BACKUP_AND_RECOVERY_GOVERNANCE_STANDARD.md` (Autonomous Agent Team)
**Pod:** POD-NADF · **Database:** `NADF` (port 8071) · **Platform:** Odoo 17 Community Edition
**Created:** 2026-06-22 (M-C) · **Maintained by:** A1 Software Factory Orchestrator
**Decision reference:** `DEC-BACKUP-001` (RPO/RTO)

---

## 1. Scope

A complete NADF backup is the **coordinated pair** of:
1. **Database** — full custom-format `pg_dump` of the `NADF` PostgreSQL database (all module data, configuration, master data).
2. **Filestore** — `~/Library/Application Support/Odoo/filestore/NADF` (attachments, images, binary data).

> A database backup without its matching filestore is an **incomplete backup** (per Standard `20`). The two must always be captured together and restored together.

**Custom code** is protected separately via version control: `nadf_erp` is pushed to GitHub (`NADF_ERP_community_version`), which is the offsite copy of all custom modules and governance documents.

## 2. Recovery objectives (DEC-BACKUP-001)

| Objective | Value | Meaning |
|-----------|-------|---------|
| **RPO** (Recovery Point Objective) | ≤ 24 hours | Maximum acceptable data loss — satisfied by daily backups |
| **RTO** (Recovery Time Objective) | ≤ 4 hours | Maximum acceptable downtime to restore service |

## 3. Schedule & retention

| Environment | Cadence | Retention |
|-------------|---------|-----------|
| Production | Daily (automated) | 30 days minimum |
| Staging | Weekly | 14 days minimum |
| Development (current) | On significant change | 7 days minimum |

**Storage location:** `~/odoo_backups/nadf_<timestamp>/` — **outside** the repository and the live data directory. Backups are **never** committed to Git (`backups/`, `*.dump`, `*.tar.gz` are gitignored).

## 4. Tooling

- **`scripts/backup_nadf.sh`** — read-safe; produces `<DB>_<TS>.dump` (pg_dump -F c), `filestore_<DB>_<TS>.tar.gz`, `MANIFEST.txt`, `SHA256SUMS.txt`. Does not modify the live database. Configurable via `NADF_DB`, `NADF_FILESTORE`, `NADF_BACKUP_ROOT`, `PGUSER/PGHOST/PGPASSWORD`.
- **`scripts/restore_nadf.sh`** — restore **drill** tool. **Refuses to target the live `NADF` database** (safety guard); restores into a temporary drill DB and runs verification queries.

## 5. Backup procedure

```
bash scripts/backup_nadf.sh        # → prints the backup directory path
```
Produces the coordinated DB dump + filestore archive + checksums + manifest.

## 6. Restore procedure

```
# Drill / recovery into a NON-production database:
bash scripts/restore_nadf.sh <path-to-.dump> NADF_restore_drill

# Real disaster recovery into production (manual, deliberate):
#   1. Stop the Odoo service on 8071.
#   2. createdb NADF_new && pg_restore --no-owner --no-acl -d NADF_new <dump>
#   3. Restore filestore: tar -xzf filestore_NADF_<TS>.tar.gz into the Odoo data dir.
#   4. Verify (Section 7), then cut over.
```

## 7. Verification criteria

A restore is **verified** when: database restores without fatal errors; `installed_modules` and `res_partner` row counts match the source; the NADF custom modules are present; filestore archive extracts and attachments are accessible.

## 8. Pre-mutation rule

Before any Odoo version upgrade, DB migration, or major module install/removal, a verified backup must exist (a restore drill within 30 days, or a fresh backup+drill immediately before the operation).

## 9. Drill Log (RESTORE_EVENT records)

> Recorded here in M-C; migrates to `IMPLEMENTATION_HISTORY.md` in M-D (per Decision D-2).

| Date | Type | Backup set | Result | Verification |
|------|------|-----------|--------|--------------|
| 2026-06-22 | RESTORE_EVENT (first drill) | `nadf_20260622_114439` (dump 6,215,346 B; filestore 38,265,886 B) | **PASS** — restored to `NADF_restore_drill`, dropped after verify | installed_modules 94 = live 94; res_partner 40 = live 40; nadf modules present (`nadf_facilities_management`, `nadf_vendor_onboarding`); drill DB dropped |

**SHA-256 (backup set `nadf_20260622_114439`):**
- `NADF_20260622_114439.dump` → `48615c6d044fa3626e6c4723f82a8261061b118578b3a2bacd0b947333641622`
- `filestore_NADF_20260622_114439.tar.gz` → `f49c766b174d343d29c598ca447bf207a2544f2ee2102ae1dce2bfdae6c69db1`

## 10. Failure response

On backup failure: investigate immediately (do not wait for the next run), determine root cause, escalate to the SF lead if production data is at risk, and record the failure + resolution in `IMPLEMENTATION_HISTORY.md`.
