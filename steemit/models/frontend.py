# -*- coding: utf-8 -*-
# this is responsible for creating fields in db in website model
from openerp import api, fields, models

class steemit_website(models.Model):
#model
    _name = 'website'
    _inherit = "website"
    # fields
    social_steemit = fields.Char("Steemit", store="True", copy="True", related="company_id.social_steemit" )
    social_dtube = fields.Char("DTube", store="True", copy="True", related="company_id.social_dtube" )
