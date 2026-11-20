# NADF ERP — developer convenience targets
# Requires: Odoo 17 venv at ~/OdooFolder/odoo17/odoo/venv/bin/python

PYTHON   = $(HOME)/OdooFolder/odoo17/odoo/venv/bin/python
ODOO_BIN = $(HOME)/OdooFolder/odoo17/odoo/odoo-bin
ADDONS   = $(HOME)/OdooFolder/odoo17/odoo/odoo/addons,$(HOME)/OdooFolder/nadf_erp/custom_addons

.PHONY: help pre-review test-portal

help:
	@echo "Available targets:"
	@echo "  make pre-review    Run static pre-review checks (Odoo 17 compat, manifests, XML)"
	@echo "  make test-portal   Run portal HttpCase smoke tests (--test-tags portal)"

pre-review:
	@echo "Running pre-review static checks …"
	$(PYTHON) scripts/pre_review_check.py
	@echo "Pre-review complete."

test-portal:
	@echo "Running portal HttpCase smoke tests …"
	@echo "NOTE: Requires NADF DB and modules installed. No portal HttpCase tests exist yet —"
	@echo "      this target is ready for future WPs that add portal code."
	$(PYTHON) $(ODOO_BIN) \
		-d NADF \
		--addons-path=$(ADDONS) \
		--test-enable --stop-after-init \
		--test-tags portal \
		--without-demo all
	@echo "Portal tests done."
