from datetime import datetime
from odoo import fields,models
from dateutil.relativedelta import relativedelta

class Station(models.Model):
    _name = "station.property"
    # never user underscore in name
    _description = "EV Charging Station"

    name = fields.Char('Code',default='CS-',required=True,copy=False)
    capacity = fields.Float('Charging Capacity (kWh)',copy=False)
    availability = fields.Boolean('is Available',required=True,default=True)
    remaining_time = fields.Datetime('Remaining Time',copy=False,default=lambda self: fields.datetime.now()+relativedelta(minutes=30))
    active = fields.Boolean(default=True)
    