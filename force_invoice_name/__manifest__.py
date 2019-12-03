# -*- coding: utf-8 -*-
# © 2019 Piotr Cierkosz <info@cier.tech>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name' : "Force Invoice Name",
    'version' : "12.0.1.0",
    'images': ['images/thumbnail.png'],
    'author' : "Piotr Cierkosz",
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'depends' : ['account'],
    'installable' : True,
    'description' : "Allows to force the Invoice Name",
    'website': "https://www.cier.tech",
    'summary': 'Allows to force the Invoice Name',
    'data': [
    'views/account_invoice_force_number_customer.xml',
    'views/account_invoice_force_number_vendor.xml',
    ],
    'live_test_url': 'https://youtu.be/_B-V-5Bz4gY',
}
