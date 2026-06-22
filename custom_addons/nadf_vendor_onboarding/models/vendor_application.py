import json
import logging

from odoo import models, fields, api
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

_COMPLIANCE_PROMPT = """You are a procurement compliance officer for NADF (National Agricultural Development Fund), a Nigerian government development agency.

Analyse the attached vendor profile PDF and extract:

1. Company name
2. CAC (Corporate Affairs Commission) registration number
3. Tax Identification Number (TIN)
4. Business areas / services offered
5. Key contact details
6. All compliance documents present (CAC certificate, TIN certificate, PENCOM, ITF, NSITF, BPP registration, etc.)
   For each document: name, issuing authority, issue date, expiry date (if any), and notes
7. Overall compliance assessment
8. Any red flags or concerns

Respond ONLY in this exact JSON format (no preamble, no trailing text):
{
  "company_name": "...",
  "cac_number": "...",
  "tin": "...",
  "business_areas": ["..."],
  "compliance_status": "Compliant|Partially Compliant|Non-Compliant",
  "documents": [
    {
      "document_name": "...",
      "issuing_authority": "...",
      "issue_date": "YYYY-MM-DD",
      "expiry_date": "YYYY-MM-DD",
      "notes": "..."
    }
  ],
  "red_flags": ["..."],
  "summary": "2-3 sentence assessment"
}

Use null (not the string "null") for missing dates. Use an empty array [] for empty lists."""


class NadfVendorApplication(models.Model):
    _name = 'nadf.vendor.application'
    _description = 'NADF Vendor Onboarding Application'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'submission_date desc, id desc'
    _rec_name = 'name'

    name = fields.Char(
        string='Company Name', required=True, tracking=True,
        help='Legal company name as registered with CAC',
    )
    contact_person = fields.Char(string='Contact Person')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')

    profile_pdf = fields.Binary(
        string='Company Profile (PDF)', required=True, attachment=True,
    )
    profile_filename = fields.Char(string='Profile Filename')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft', required=True, tracking=True, copy=False)

    submission_date = fields.Datetime(string='Submission Date', readonly=True, copy=False)
    partner_id = fields.Many2one('res.partner', string='Vendor Partner', readonly=True, copy=False)

    analysis_result = fields.Text(string='AI Analysis (Raw JSON)', readonly=True, copy=False)
    analysis_summary = fields.Html(string='AI Analysis Summary', readonly=True, sanitize=False, copy=False)

    document_ids = fields.One2many(
        'nadf.vendor.document.line', 'application_id', string='Compliance Documents',
    )
    notes = fields.Text(string='Internal Notes')

    # ── State transitions ──────────────────────────────────────────────────────

    def action_submit(self):
        for rec in self:
            if rec.state != 'draft':
                continue
            rec.write({
                'state': 'under_review',
                'submission_date': fields.Datetime.now(),
            })
            rec.message_post(body='Application submitted for review.')
        return True

    def action_approve(self):
        for rec in self:
            if rec.state != 'under_review':
                raise UserError('Only applications under review can be approved.')
            partner = self.env['res.partner'].create({
                'name': rec.name,
                'email': rec.email,
                'phone': rec.phone,
                'supplier_rank': 1,
                'company_type': 'company',
                'comment': f'Approved via NADF Vendor Onboarding. App ID: {rec.id}',
            })
            rec.write({'state': 'approved', 'partner_id': partner.id})
            rec.message_post(
                body=f'Application approved. Vendor record created: <a href="/web#id={partner.id}&model=res.partner">{partner.name}</a>',
            )
        return True

    def action_reject(self):
        for rec in self:
            if rec.state not in ('draft', 'under_review'):
                raise UserError('Only draft or under-review applications can be rejected.')
            rec.write({'state': 'rejected'})
            rec.message_post(body='Application rejected.')
        return True

    def action_reset_draft(self):
        for rec in self:
            if rec.state == 'rejected':
                rec.write({'state': 'draft'})
                rec.message_post(body='Application reset to draft.')
        return True

    # ── AI analysis ───────────────────────────────────────────────────────────

    def action_analyse_with_ai(self):
        self.ensure_one()

        api_key = self.env['ir.config_parameter'].sudo().get_param('nadf.claude.api.key')
        if not api_key:
            raise UserError(
                "Claude API key not configured.\n\n"
                "Go to Settings → Technical → System Parameters and create a parameter:\n"
                "  Key:   nadf.claude.api.key\n"
                "  Value: sk-ant-api03-…"
            )

        if not self.profile_pdf:
            raise UserError('Please attach a company profile PDF before running AI analysis.')

        try:
            import anthropic
        except ImportError:
            raise UserError(
                "The 'anthropic' Python package is not installed.\n\n"
                "Run this command and then restart Odoo:\n"
                "  /Users/mac/odoo17/odoo/venv/bin/pip install anthropic"
            )

        try:
            import base64 as _b64
            client = anthropic.Anthropic(api_key=api_key)

            # Binary field stores base64-encoded data; decode to raw bytes for upload
            pdf_data = self.profile_pdf
            pdf_bytes = _b64.b64decode(pdf_data)
            filename = self.profile_filename or 'vendor_profile.pdf'

            # Upload via Files API — avoids 413 errors on large PDFs
            uploaded = client.beta.files.upload(
                file=(filename, pdf_bytes, 'application/pdf'),
            )
            file_id = uploaded.id
            _logger.info('Uploaded PDF to Anthropic Files API: %s (%d bytes)', file_id, len(pdf_bytes))

            try:
                message = client.beta.messages.create(
                    model='claude-opus-4-8',
                    max_tokens=8192,
                    betas=['files-api-2025-04-14'],
                    messages=[{
                        'role': 'user',
                        'content': [
                            {
                                'type': 'document',
                                'source': {
                                    'type': 'file',
                                    'file_id': file_id,
                                },
                            },
                            {
                                'type': 'text',
                                'text': _COMPLIANCE_PROMPT,
                            },
                        ],
                    }],
                )
            finally:
                # Remove the uploaded file from Anthropic's storage after use
                try:
                    client.beta.files.delete(file_id)
                    _logger.info('Deleted Anthropic file: %s', file_id)
                except Exception as del_err:
                    _logger.warning('Could not delete Anthropic file %s: %s', file_id, del_err)

            result_text = message.content[0].text
            self.analysis_result = result_text

            try:
                # Strip markdown code fences Claude sometimes wraps around JSON
                clean = result_text.strip()
                if clean.startswith('```'):
                    clean = clean.split('\n', 1)[1] if '\n' in clean else clean
                    clean = clean.rsplit('```', 1)[0].strip()
                data = json.loads(clean)
                self._populate_from_ai(data)
            except json.JSONDecodeError:
                self.analysis_summary = f'<pre style="white-space:pre-wrap">{result_text}</pre>'

            self.message_post(body='AI compliance analysis completed successfully.')
            return True

        except anthropic.APIStatusError as e:
            raise UserError(f'Claude API error ({e.status_code}): {e.message}')
        except anthropic.APIConnectionError as e:
            raise UserError(f'Could not reach Claude API. Check internet connection.\n\n{e}')
        except Exception as e:
            _logger.exception('AI analysis failed for vendor application %d', self.id)
            raise UserError(f'Analysis failed: {e}')

    def _populate_from_ai(self, data):
        """Parse AI JSON response and update document lines + HTML summary."""
        status = data.get('compliance_status', 'Unknown')
        status_color = {
            'Compliant': '#d4edda',
            'Partially Compliant': '#fff3cd',
            'Non-Compliant': '#f8d7da',
        }.get(status, '#d1ecf1')
        text_color = {
            'Compliant': '#155724',
            'Partially Compliant': '#856404',
            'Non-Compliant': '#721c24',
        }.get(status, '#0c5460')

        red_flags = [f for f in data.get('red_flags', []) if f]
        red_flags_html = ''
        if red_flags:
            items = ''.join(f'<li>{flag}</li>' for flag in red_flags)
            red_flags_html = f'<div style="margin-top:12px"><strong style="color:#721c24">Red Flags</strong><ul style="margin-top:4px">{items}</ul></div>'

        business_areas = ', '.join(a for a in data.get('business_areas', []) if a)
        summary = data.get('summary', '')
        cac = data.get('cac_number') or ''
        tin = data.get('tin') or ''

        meta_rows = ''
        if cac:
            meta_rows += f'<tr><td style="padding:4px 8px;color:#666">CAC No.</td><td style="padding:4px 8px"><strong>{cac}</strong></td></tr>'
        if tin:
            meta_rows += f'<tr><td style="padding:4px 8px;color:#666">TIN</td><td style="padding:4px 8px"><strong>{tin}</strong></td></tr>'
        if business_areas:
            meta_rows += f'<tr><td style="padding:4px 8px;color:#666">Business Areas</td><td style="padding:4px 8px">{business_areas}</td></tr>'

        meta_table = f'<table style="border-collapse:collapse;margin-top:8px">{meta_rows}</table>' if meta_rows else ''

        self.analysis_summary = f"""
<div style="font-family:sans-serif;padding:16px;background:#fafafa;border-radius:6px;border:1px solid #dee2e6">
    <div style="background:{status_color};color:{text_color};padding:10px 14px;border-radius:4px;font-weight:600;font-size:1.05em">
        Compliance Status: {status}
    </div>
    <p style="margin:12px 0 4px">{summary}</p>
    {meta_table}
    {red_flags_html}
</div>"""

        # Replace document lines with AI-extracted ones
        self.document_ids.unlink()
        for doc in data.get('documents', []):
            issue_date = doc.get('issue_date')
            expiry_date = doc.get('expiry_date')
            self.env['nadf.vendor.document.line'].create({
                'application_id': self.id,
                'document_name': doc.get('document_name') or 'Unknown',
                'issuing_authority': doc.get('issuing_authority') or '',
                'issue_date': issue_date if issue_date and issue_date != 'null' else False,
                'expiry_date': expiry_date if expiry_date and expiry_date != 'null' else False,
                'notes': doc.get('notes') or '',
            })
