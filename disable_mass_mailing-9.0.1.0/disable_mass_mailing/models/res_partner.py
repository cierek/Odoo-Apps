# -*- coding: utf-8 -*-
# Copyright 2018 CierTech - Piotr Cierkosz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    opt_out = fields.Boolean(
        string='Opt-Out',
        default=True,
        store=True,
        copy=True,
        help='If opt-out is checked, this contact has refused to receive emails for mass mailing and marketing campaign. Filter Available for Mass Mailing allows users to filter the partners when performing mass mailing.'
    )
