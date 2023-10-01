from odoo import models, fields, api


class Voyage(models.Model):
    _name = 'travel.travel'
    _description = 'Modèle Voyage'
    # Define fields for the travel record
    name = fields.Char(string="Nom du voyage", required=True)
    depart = fields.Char(string="Lieux de Depart", required=True)
    destination = fields.Char(string="Destination", required=True)
    time_depart = fields.Datetime(string= "temp de départ", required=True)
    nb_place = fields.Integer(string="Nombre de place", required=True)
    montant = fields.Float(string="Montant", required=True)

    # Define a many2one relationship to the res.partner model
    contact_id = fields.Many2one('res.partner', string="Contact")

    # Define an onchange function for the montant field
    @api.onchange('montant')
    def _onchange_montant(self):
        if self.contact_id:
            # Call the _compute_reward_level function of the associated res.partner record
            self.contact_id._compute_reward_level()




