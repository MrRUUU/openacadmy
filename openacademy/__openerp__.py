# -*- coding: utf-8 -*-
{
    'name': "Acadèmia Oberta",

    'summary': """Mòdul per la gestió d'una acadèmia""",

    'description': """
         Contingut del mòdul:
            - registrar professors
            - registrar matèries
            - gestionar cursos
    """,

    'author': "Ángel Quintana",
    'website': "http://www.ies-eugeni.cat",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
	'views/openacademy.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],
}