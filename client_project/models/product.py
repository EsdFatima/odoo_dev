from odoo import models, fields, api

class Product(models.Model):
    _inherit = 'product'

    color = fields.Char(string='Color')


