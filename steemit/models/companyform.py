# -*- coding: utf-8 -*-
# this is responsible for creating fields in db in company model
from openerp import api, fields, models

class steemit_view_company_form(models.Model):
    #model
    _name = 'res.company'
    _inherit = 'res.company'
    #fields
    social_steemit = fields.Char("Steemit", store="True", copy="True")
    social_dtube = fields.Char("DTube", store="True", copy="True")
