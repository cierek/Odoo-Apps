# -*- coding: utf-8 -*-
# © 2019 Piotr Cierkosz <info@cier.tech>
# Module was produced in a good faith, it was tested with clean Odoo 11 version and no errors were detectedself.
# Can't guarantee proper work of the module and I don't take responsibility for errors caused by itself.
# E-mail me with any questions.
{
    'name': 'Implemented by visible for all users',
    'author': 'Piotr Cierkosz',
    'website': 'http://www.cier.tech',
    'version': '12.0.1.0',
    'category': 'Extra Tools',
    'images': ['images/thumbnail.png'],
    'depends' : ['website', 'website_crm_partner_assign', 'crm'],
    'installable' : True,
    'license': 'Other proprietary',
    'summary': 'Makes implemented by field visible for all users',
    'auto_install': False,
    'data': [
        'views/implemented_visible.xml',
    ],
    'description': """
    Makes implemented by field visible for all users
    """,
}
