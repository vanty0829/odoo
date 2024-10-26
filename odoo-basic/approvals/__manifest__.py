# -*- coding: utf-8 -*-
{
    'name': "Approvals",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "TyLe",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    #thứ tự khai báo file trong data có dependency
    'data': [
        # 'security/player_security.xml',
        # 'security/ir.model.access.csv',
        'views/root_menu.xml',
        'views/schema_views.xml',
        'views/table_views.xml',
        'views/request_views.xml',
        
    ],
    # any module necessary for this one to work correctly
    'depends': ['base'],
    'license': 'LGPL-3',
}

