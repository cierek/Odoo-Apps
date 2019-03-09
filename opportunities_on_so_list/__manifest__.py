# -*- coding: utf-8 -*-

{
    'name' : "Opportunity on Sales Orders list",
    'version' : "1.1",
    'images': ['images/thumbnail.png'],
    'author' : "Piotr Cierkosz",
    'category': 'Sales',
    'license': 'Other proprietary',
    'depends' : ['sale', 'crm'],
    'installable' : True,
    'description' : "This module adds opportunities to the tree view (Sales Orders and Quotations)",
    'website': "www.cier.tech",
    'summary': 'This module allows users to see the connected opportunity on the sales orders and quotations tree views',

    'data': ['views/so_tree_views.xml',],

}
