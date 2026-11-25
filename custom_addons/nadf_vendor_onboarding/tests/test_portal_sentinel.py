"""
Governance sentinel test — WP-GOV-02 / DEC-GOV-02.

Ensures `make test-portal` (--test-tags portal) always finds at least one
test and returns a meaningful exit code. The public /vendor/register route
requires no authentication; a public GET returning HTTP 200 or 302 is enough
to confirm the controller is loaded and routable.
"""
from odoo.tests import HttpCase, tagged


@tagged('portal', '-at_install')
class TestVendorPortalSentinel(HttpCase):
    def test_vendor_register_route_reachable(self):
        """Public GET /vendor/register must not return 404 or 500."""
        response = self.url_open('/vendor/register')
        self.assertIn(
            response.status_code,
            (200, 302),
            f"Expected 200 or 302 from /vendor/register, got {response.status_code}",
        )
