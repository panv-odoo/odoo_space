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
        
        'views/res_config_settings_views.xml',
        'views/charging_station_tag_views.xml',
        'views/vehicle_detail_views.xml',
        'views/user_detail_views.xml',
        'views/charging_session_views.xml',
        'views/charging_station_views.xml',
        'views/odoospace_menus.xml',
        
    ],
    'demo':[
        'data/demo_data.xml',
    ],
    'license': 'LGPL-3',
}
