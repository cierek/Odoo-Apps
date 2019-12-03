# -*- coding: utf-8 -*-

from openerp import api, fields, models, _

class Bukcirra(models.Model):
# where to place new fields
    _inherit = 'stock.picking'
# chenging location_id attributes
    location_id = fields.Many2one(
        'stock.location', "Source Location",
        default=lambda self: self.env['stock.picking.type'].browse(self._context.get('default_picking_type_id')).default_location_src_id,
        readonly=False, required=True,
        states={'draft': [('readonly', False)]})
