# NADF ERP — developer convenience targets
# Requires: Odoo 17 venv at ~/OdooFolder/odoo17/odoo/venv/bin/python
#
# NOTE: ADDONS points to the main checkout (~/OdooFolder/nadf_erp/custom_addons).
# When running from a worktree, ensure your changes are present in that path or
# override: make test-portal ADDONS=<odoo_addons>,<your_worktree>/custom_addons

PYTHON   = $(HOME)/OdooFolder/odoo17/odoo/venv/bin/python
ODOO_BIN = $(HOME)/OdooFolder/odoo17/odoo/odoo-bin
ADDONS   = $(HOME)/OdooFolder/odoo17/odoo/odoo/addons,$(HOME)/OdooFolder/nadf_erp/custom_addons
# NB: in a git worktree, override: make test-portal ADDONS=$(HOME)/OdooFolder/odoo17/odoo/odoo/addons,$(PWD)/custom_addons
# NEVER use the live DB for tests. Default to a drill copy; override with DB=nadf_drill.
# To create a drill copy: pg_dump -F c NADF | pg_restore -d nadf_drill (or use restore_nadf.sh)
DB       ?= nadf_drill

.PHONY: help pre-review test-portal

help:
	@echo "Available targets:"
	@echo "  make pre-review            Run static pre-review checks (Odoo 17 compat, manifests, XML)"
	@echo "  make test-portal [DB=...]  Run portal HttpCase smoke tests (--test-tags portal) on drill DB"

pre-review:
	@echo "Running pre-review static checks …"
	$(PYTHON) scripts/pre_review_check.py
	@echo "Pre-review complete."

test-portal:
	@if [ "$(DB)" = "NADF" ]; then echo "ERROR: Do not run test-portal against the live NADF database. Use DB=nadf_drill or another drill copy." >&2; exit 1; fi
	@echo "Running portal HttpCase smoke tests on DB=$(DB) …"
	@echo "NOTE: No portal HttpCase tests registered yet — target is ready for future portal WPs."
	@echo "      When the first portal HttpCase test is added, verify this target exits 0 on pass"
	@echo "      and non-zero on failure. If Odoo exits non-zero when no tests match --test-tags,"
	@echo "      add an explicit empty-test sentinel rather than using '|| true'"
	$(PYTHON) $(ODOO_BIN) \
		-d $(DB) \
		--addons-path=$(ADDONS) \
		--test-enable --stop-after-init \
		--test-tags portal \
		--without-demo all
	@echo "Portal tests done."
