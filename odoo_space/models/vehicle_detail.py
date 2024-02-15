from odoo import models,fields
class Vehicle(models.Model):
    _name = "vehicle.detail"
    _description = "Vehicle Detail Model"

    license_plate = fields.Char('License Plate',required=True)
    model = fields.Char('Model',required=True,help="car model - colour")
    manufacturer = fields.Selection(
        string='Manufacturer',
        selection=[('tesla', 'Tesla'),
                    ('nissan', 'Nissan'),
                    ('chevrolet', 'Chevrolet'),
                    ('bmw', 'BMW'),
                    ('audi', 'Audi'),
                    ('hyundai', 'Hyundai'),
                    ('ford', 'Ford')]
    )
    user_id = fields.Many2one('user.detail',required=True)
    battery_capacity = fields.Float('Battery Capacity',default=114.0)
