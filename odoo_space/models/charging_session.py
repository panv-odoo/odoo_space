from datetime import datetime
from odoo import api, fields,models
from odoo.exceptions import ValidationError

class ChargingSession(models.Model):
    _name = "charging.session"
    _description = "Charging Session Model"
    _order = 'status,in_line DESC'

    user_id = fields.Many2one('user.detail',string='User',required=True)
    station_id = fields.Many2one('charging.station',string='Station No.',required=True)
    vehicle_id = fields.Many2one('vehicle.detail',string='Vehicle',required=True)
    initial_charging = fields.Integer('Initial Charging %',required=True)
    final_charging = fields.Integer('Final Charging %',compute='_compute_final_charging',store=True)
    is_fully_charged = fields.Boolean(default=True)
    status = fields.Selection(
        [('waiting','Waiting'),('charging','Charging'),('charged','Charged')],
        default='waiting'
    )
    in_line = fields.Datetime('waiting since',default=datetime.now())
    in_time = fields.Datetime('in-time',)
    out_time = fields.Datetime('out-time')

    @api.depends('is_fully_charged')
    def _compute_final_charging(self):
        for record in self:
            if record.is_fully_charged :
                record.final_charging = 100.00
    
    def action_charge(self):
        for record in self:
            if record.station_id.status == 'occupied':
                raise ValidationError("Can't charge more than one vehicle at a time")
            else:
                record.station_id.status = 'occupied'
                record.status = 'charging'
                record.in_time = datetime.now()

    def action_discharge(self):
        for record in self:
            record.station_id.status = 'available'
            record.status = 'charged'
            record.out_time = datetime.now()
            view_id = self.env.ref('odoo_space.session_view_form').id
            return {
            'name': 'New Charging Session',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'charging.session',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'res_id': record.id,
            'views': [(view_id,'form')],
            }
