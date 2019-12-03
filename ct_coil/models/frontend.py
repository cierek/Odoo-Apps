# -*- coding: utf-8 -*-
# Part of CierTech.

from odoo import api, fields, models

class CoilContentCode(models.Model):
    _inherit = "website"

    coil_content = fields.Char("Coil content code")

class res_config_settings(models.TransientModel):
    _inherit="res.config.settings"

    coil_content = fields.Char(string="Coil content code", readonly=False, related="website_id.coil_content")
    has_coil_content = fields.Boolean(string="Coil Monetization")
