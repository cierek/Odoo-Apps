# -*- coding: utf-8 -*-
# © 2019 Piotr Cierkosz <info@cier.tech>

{
    'name': 'Odoo - Coil Integration',
    'author': 'Piotr Cierkosz',
    'website': 'http://www.cier.tech',
    'version': '12.0.1.0',
    'category': 'Website',
    'images': ['images/thumbnail.png'],
    'depends' : ['website'],
    'installable' : True,
    'license': 'Other proprietary',
    'summary': 'Add Coil Monetization to your website',
    'data': [
        'views/res_config_settings_view.xml',
        'views/frontend.xml',
    ],
    'description': """
    Add Coil code to your website - compatible with multi-websites
    """,
}
