<!-- POD-NADF PR template — Software Factory Release & Git Governance Standard (14) -->

## Change description (why, not just what)


## Type
<!-- feat | fix | governance | docs | ops | chore | test | security -->

## Governance Impact Analysis
- [ ] Platform: Odoo 17 **CE only** — no Enterprise module introduced
- [ ] Layer: no cross-pod contamination (NADF assets stay in `nadf_erp`)
- [ ] Spec gating: no custom-module code without an approved spec; no unspecified-department build
- [ ] Security/access: access rights / record rules reviewed if models changed
- [ ] Data/DB: no destructive DB change without a verified backup
- [ ] Backup/recovery impact considered

## Repository memory updated (as applicable)
- [ ] `DECISION_LOG.md`
- [ ] `MODULE_REGISTRY.md`
- [ ] `IMPLEMENTATION_HISTORY.md`
- [ ] `CHANGELOG.md`
- [ ] `RISK_REGISTER.md`
- [ ] `PROJECT_STATE.md`

## Verification / test evidence


## Rollback plan


## Final governance declaration
- [ ] CI (`ci.yml`) passes
- [ ] At least one non-author review (required by branch protection on `main`)
