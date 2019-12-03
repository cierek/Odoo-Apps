# -*- coding: utf-8 -*-
# © 2018 Piotr Cierkosz <piotr.w.cierkosz@gmail.com>
{
    'name': "Remove Google+ from Odoo",
    'version': "11.0.1.0",
    'author': "Piotr Cierkosz",
    'website': "www.cier.tech",
    'category': "Website",
    #comment or remove company_form_googleplus0 below if you are not using mass mailing
    'data': ["views/company_form_googleplus.xml",
    #"views/company_form_googleplus0.xml",
    ],
    'images': ['images/thumbnail.png'],
    'depends' : ['website',
    #comment or remove mass_mailing below if you are not using mass mailing
    #'mass_mailing',
    ],
    'installable' : True,
    'description' : "This module removes Google+ field from Company form",
    'license': 'Other proprietary',
    'summary': 'This module removes Google+ field from Company form',
}
