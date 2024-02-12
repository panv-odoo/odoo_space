{
    'name': "Odoo Space",
    'version': '1.0',
    'depends': ['base'],
    'author': "PANV-ODOO",
    'category': 'Services',
    'description': """
    This module is for the technical training Project
    """,
    'application': True,
    'depends':['mail'],
    'data':[
        'security/ir.model.access.csv',

        'views/user_property_views.xml',
        'views/station_property_view.xml',
        'views/odoospace_menus.xml',
        
    ],
    'license': 'LGPL-3',
}
