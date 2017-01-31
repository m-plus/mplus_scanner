# -*- coding: utf-8 -*-
{
    'name': "Mplus Scanner",
    'summary': """
        Attached scanned document to object
    """,
    'description': """
        Attached scanned document to object
    """,
    'author': "Mplus Software",
    'website': "http://mplus.software",
    'category': 'CRM',
    'version': '1.0',
    'depends': ['document'],
    'data': [
        'views/mplus_scanner.xml',
        'views/res_users_view.xml',
    ],
    'qweb' : [
        "static/src/xml/*.xml",
    ],
}