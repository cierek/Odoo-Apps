# -*- coding: utf-8 -*-
# © 2019 Piotr Cierkosz <piotr.w.cierkosz@gmail.com>
{
    'name': "Remove Google+ from Odoo Blog",
    'version': "10.0.1.0.1",
    'author': "Piotr Cierkosz",
    'website': "www.cier.tech",
    'category': "Website",
    'data': [
    "views/company_form_googleplus_blog.xml",
    "views/company_form_googleplus_blog0.xml",
    ],
    'images': ['images/thumbnail.png'],
    'depends' : ['website','website_blog',
    ],
    'installable' : True,
    'description' : "This module removes Google+ from Odoo Blog",
    'license': 'Other proprietary',
    'summary': 'This module removes Google+ from Odoo Blog',
}
