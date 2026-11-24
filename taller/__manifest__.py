# -*- coding: utf-8 -*-
{
    'name': "gestion taller",

    'summary': "modulo para gestion ation taller",

    'description': """
Este va a ser un modulo para la gestion taller
    """,

    'author': "Alexandra",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': '',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/cliente_views.xml',
        'views/mecanico_views.xml',
        'views/vehiculo_views.xml',
        'views/reparacion_views.xml',
        #'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode

    'application': True,
    'installable': True,
    'license':'LGPL-3',
}
