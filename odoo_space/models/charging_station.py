from odoo import fields,models
from dateutil.relativedelta import relativedelta

class ChargingStation(models.Model):
    _name = "charging.station"
    # never user underscore in name
    _description = "Charging Station Model"
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char('Code',required=True,default='Charging Station',copy=False)
    location = fields.Selection(
        string = 'Location',
        selection=[('lln1','LLN1'),('lln2','LLN2')]
    )
    status = fields.Selection(
        string = 'Status',
        selection=[('available','Available'),('occupied','Occupied')],
        default='available'
    )
    voltage_capacity = fields.Float('Voltage Capacity (KWh)',default=11.0)
    active = fields.Boolean('Active',default=True)
    session_ids = fields.One2many('charging.session','station_id')
    # capacity = fields.Float('Charging Capacity (kWh)',copy=False)
    # availability = fields.Boolean('is Available',required=True,default=True)
    # remaining_time = fields.Datetime('Remaining Time',copy=False,default=lambda self: fields.datetime.now()+relativedelta(minutes=30))
    # active = fields.Boolean(default=True)
