from datetime import datetime

from odoo import api, fields,models,Command
from odoo.exceptions import ValidationError
from odoo.tools.float_utils import float_compare

class ChargingSession(models.Model):
    _name = "charging.session"
    _description = "Charging Session Model"
    _order = 'status,in_line DESC'

    user_id = fields.Many2one('user.detail',string='User',required=True)
    station_id = fields.Many2one('charging.station',string='Station No.',required=True)
    vehicle_id = fields.Many2one('vehicle.detail',string='Vehicle',required=True)
    initial_charging = fields.Integer('Initial Charging %',required=True)
    final_charging = fields.Integer('Final Charging %',compute='_compute_final_charging',store=True,readonly=False)
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
                
    @api.constrains('initial_charging', 'final_charging')
    def _check_percentage(self):
        for record in self:
            if record.initial_charging < 0 or record.final_charging < 0 \
                    or record.initial_charging > 100 or record.final_charging > 100:
                raise ValidationError("Charging percentages must be between 0 and 100")

            result = float_compare(record.final_charging,record.initial_charging,2)
            if(result < 0 ):
                raise ValidationError("Final Percentage can't be less than Initial Percentage")
    
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
            
            generate_invoice = self.env['ir.module.module'].sudo().search([('name', '=', 'account'), ('state', '=', 'installed')], limit=1)
            
            if generate_invoice:
                # to generate partner_id for the user of the odoo_space
                if not record.user_id.partner_id:
                    partner_id = self.env['res.partner'].sudo().create({
                        'name': record.user_id.name,
                        'is_company': False,
                        'street':record.user_id.address,
                        'phone': record.user_id.phone,
                        'email': record.user_id.email,
                        'function': record.user_id.designation
                    })
                    record.user_id.partner_id = partner_id.id
                
                #  to generate invoice
                invoice_val = {
                'partner_id': record.user_id.partner_id.id,
                'move_type': 'out_invoice',  
                'invoice_line_ids': [
                    Command.create({
                        'name':'Charging Service',
                        'quantity':1,
                        'price_unit':12000
                    })
                ]}
                # print(" reached ".center(100, '='))
                self.env['account.move'].sudo().create(invoice_val)
            
            # to open session form view to enter final_charging percentage
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
