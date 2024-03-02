{
    'name': 'Products',
    'version': '16.0.0.0',
    'author': 'ESSID Fatima Zahraa',
    'category': 'Custom Modules',
    'license': 'LGPL-3',
    'summary': 'Management of Products',
    'description': """
    This module allows you to manag productaa and calculethe total price.
    """,
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
    ],
    'demo': [

    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
