{
    'name': "Odoo Space",
    'version': '1.0',
    'depends': ['base','mail'],
    'author': "PANV-ODOO",
    'category': 'Services',
    'description': """
        This module is for the technical training Project
    """,
    'application': True,
    'data':[
        'security/ir.model.access.csv',
        
        'views/vehicle_detail_views.xml',
        'views/user_detail_views.xml',
        'views/charging_station_views.xml',
        'views/odoospace_menus.xml',
        
    ],
    'demo':[
        'data/data.xml',
    ],
    'license': 'LGPL-3',
}
