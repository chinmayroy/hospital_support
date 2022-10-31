# -*- coding: utf-8 -*-
{
    'name': "Hospital Support",

    'summary': """Making a connection between doctors and patients""",

    'description': """
        This app is created for supporting to patient by doctor. 
    """,

    'author': "Chinmay Roy",
    'website': "http://www.chinmayroy.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',
    'sequence': 1,

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'web',
        ],

    # always loaded
    'data': [
        'report/patients_report_format.xml',
        'report/patients_report_wizard.xml',
        'wizards/patients_report_wizard_view.xml',
        'wizards/doctors_wizards.xml',
        'views/doctors_informations.xml',
        'report/patients_report.xml',   
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/patients_informations.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 0,
    'currency': 'USD',
    'license': 'LGPL-3',
    'contributors': [
        'Chinmay Roy <https://github.com/chinmayroy>',
    ],
    'icon': '/hospital_support/static/img/hs_icon.png',
    'assets': {
        'web.assets_backend': [
            ('include', 'hospital_support/static/src/css/web_assets_backend.css'),
            ('include', 'hospital_support/static/src/js/web_assets_backend.js'),
        ],
        'web.assets_frontend': [
            ('include', 'hospital_support/static/src/css/web_assets_frontend.css'),
            ('include', 'hospital_support/static/src/js/web_assets_frontend.js'),
        ],
        'web.assets_common': [
            ('include', 'hospital_support/static/src/css/web_assets_common.css'),
            ('include', 'hospital_support/static/src/js/web_assets_common.js'),
        ],
    },
}
