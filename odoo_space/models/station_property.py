from odoo import fields,models

class Station(models.Model):
    _name = "station.property"
    # never user underscore in name
    _description = "EV Charging Station"

    code = fields.Char('Code',required=True)
    capacity = fields.Integer('Charging Capacity (kWh)')
    availability = fields.Boolean('is Available',required=True)
    remaining_time = fields.Datetime('Remaining Time')
    