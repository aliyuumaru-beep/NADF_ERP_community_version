from odoo import models, fields, api
from datetime import date, timedelta


class NadfVendorDocumentLine(models.Model):
    _name = 'nadf.vendor.document.line'
    _description = 'Vendor Compliance Document'
    _order = 'document_name'

    application_id = fields.Many2one(
        'nadf.vendor.application', string='Application',
        required=True, ondelete='cascade', index=True,
    )
    document_name = fields.Char(string='Document Name', required=True)
    issuing_authority = fields.Char(string='Issuing Authority')
    issue_date = fields.Date(string='Issue Date')
    expiry_date = fields.Date(string='Expiry Date')
    status = fields.Selection([
        ('valid', 'Valid'),
        ('expiring_soon', 'Expiring Soon (≤30 days)'),
        ('expired', 'Expired'),
        ('no_expiry', 'No Expiry'),
    ], string='Status', compute='_compute_status', store=True)
    notes = fields.Char(string='Notes')

    @api.depends('expiry_date')
    def _compute_status(self):
        today = date.today()
        threshold = today + timedelta(days=30)
        for rec in self:
            if not rec.expiry_date:
                rec.status = 'no_expiry'
            elif rec.expiry_date < today:
                rec.status = 'expired'
            elif rec.expiry_date <= threshold:
                rec.status = 'expiring_soon'
            else:
                rec.status = 'valid'
