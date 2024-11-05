# -*- coding: utf-8 -*-
{
    'name': "OWL Todo",

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
    'data':[
        'security/ir.model.access.csv',
        'views/todo_task_views.xml'
    ],
    # any module necessary for this one to work correctly
    'depends': ['base'],
    'license': 'LGPL-3',
}

