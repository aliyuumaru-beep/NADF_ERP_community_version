import base64
import logging

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class VendorPortalController(http.Controller):

    @http.route(
        '/vendor/register',
        type='http', auth='public', methods=['GET', 'POST'],
        website=False, csrf=True,
    )
    def vendor_register(self, **kwargs):
        if request.httprequest.method == 'POST':
            return self._handle_submission(**kwargs)
        return request.render('nadf_vendor_onboarding.vendor_registration_form', {
            'error': {},
            'values': {},
        })

    def _handle_submission(self, **post):
        errors = {}
        name = (post.get('company_name') or '').strip()
        email = (post.get('email') or '').strip()
        phone = (post.get('phone') or '').strip()
        contact_person = (post.get('contact_person') or '').strip()
        profile_file = request.httprequest.files.get('profile_pdf')

        if not name:
            errors['company_name'] = 'Company name is required.'
        if not email:
            errors['email'] = 'Email address is required.'
        if not profile_file or not profile_file.filename:
            errors['profile_pdf'] = 'Please upload your company profile PDF.'
        elif not profile_file.filename.lower().endswith('.pdf'):
            errors['profile_pdf'] = 'Only PDF files are accepted.'

        if errors:
            return request.render('nadf_vendor_onboarding.vendor_registration_form', {
                'error': errors,
                'values': post,
            })

        try:
            pdf_data = base64.b64encode(profile_file.read())
            request.env['nadf.vendor.application'].sudo().create({
                'name': name,
                'contact_person': contact_person,
                'email': email,
                'phone': phone,
                'profile_pdf': pdf_data,
                'profile_filename': profile_file.filename,
                'state': 'draft',
            })
            return request.render('nadf_vendor_onboarding.vendor_registration_success', {
                'company_name': name,
            })
        except Exception as e:
            _logger.exception('Vendor registration failed for company: %s', name)
            return request.render('nadf_vendor_onboarding.vendor_registration_form', {
                'error': {'general': f'Submission failed. Please try again or contact NADF IT support. ({e})'},
                'values': post,
            })
