# -*- coding: utf-8 -*-
# Part of CierTech.


from odoo import api, fields, models

class website(models.Model):
    _inherit = 'website'

    ct_searchbar_in_shop=fields.Boolean(string="Searchbar in shop")


class res_config_settings(models.TransientModel):
    _inherit="res.config.settings"

    ct_searchbar_in_shop = fields.Boolean(
        related="website_id.ct_searchbar_in_shop", string="Searchbar in shop", readonly=False)
