from odoo import fields,models

class ChargingSession(models.Model):
    _name = "charging.session"
    _description = "Charging Session Model"

    user_id = fields.Many2one('user.detail',string='User',required=True)
    station_id = fields.Many2one('charging.station',string='Station No.',required=True,readonly=True)
    vehicle_id = fields.Many2one('vehicle.detail',string='Vehicle',required=True)
    current_charging = fields.Integer('Current Charging Percentage',required=True)
    status = fields.Selection(
        [('waiting','Waiting'),('charging','Charging'),('Charged','Charged')],
        default='waiting'
    )
    in_time = fields.Datetime('in-time',default=fields.datetime.now())
    out_time = fields.Datetime('out-time')

    def action_charge(self):
        pass

    def action_discharge(self):
        pass