{
    'name': 'NADF Vendor Onboarding',
    'version': '17.0.1.0.0',
    'category': 'Procurement',
    'summary': 'AI-powered vendor registration portal with Claude PDF compliance analysis',
    'author': 'NADF ERP Project',
    'depends': ['base', 'mail', 'purchase'],
    'data': [
        'security/nadf_vendor_security.xml',
        'security/ir.model.access.csv',
        'views/vendor_application_views.xml',
        'views/menus.xml',
        'templates/vendor_portal.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
