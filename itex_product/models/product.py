from odoo import models, fields, api

class Product(models.Model):
    _name = 'product'

    name = fields.Char(string='Name', required=True)
    description = fields.Char(string='Description')
    unit_price = fields.Float(string='Unit Price', required=True)
    quantity = fields.Float(string='Quantity', default='1.0')
    total_price = fields.Float(string='Total Price', compute='_compute_total_price', store='True')

    @api.depends('quantity', 'unit_price')
    def _compute_total_price(self):
        for record in self:
            record.total_price = record.quantity * record.unit_price

