# -*- coding: utf-8 -*-
{
    'name': "module-model",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "tyle",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'data': [
        'wizards/transient_model_views.xml',
        'views/base_model_views.xml',
    ],
    # any module necessary for this one to work correctly
    'depends': ['base'],
}