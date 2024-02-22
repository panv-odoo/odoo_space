from odoo import fields,models

class User(models.Model):
    _name = "user.detail"
    _description = "User Detail Model"
    _inherit = ['mail.thread','mail.activity.mixin']
    name = fields.Char('Name',required=True)
    image = fields.Binary()
    address = fields.Char('Address (Locality)')
    department =  fields.Char("Department",required=True)
    designation = fields.Char("Designation")
    phone =  fields.Char("Phone",required=True)
    email = fields.Char("Email",required=True)
    vehicle_ids = fields.One2many('vehicle.detail','user_id')
    active = fields.Boolean('Active',default=True)
    # postal = fields.Char('Pincode',required=True)
    # designation = fields.Char('Designation',required=True)
    
    # interests = fields.Char("Interests")
    # hobbies = fields.Char('Hobbies')
    # has_vehicle = fields.Boolean('Has Vehicle ?',default=False)
    # fuel_type = fields.Selection(
    #     string= 'Fuel Type',
    #     selection=[('pertrolDiesel','Pertrol / Diesel'),('electric', 'Electric'),('cng','CNG')]
    # )
    # vehicle_type = fields.Selection(
    #     string='Vehicle Type',
    #     selection=[('two_wheeler','Two Wheeler'),('four_wheeler','Four Wheeler')]
    # )
    # licence_plate = fields.Char("Licence Plate")
    # vehiclepool = fields.Boolean('Want to Vehicle Pool',default=False)
    # sitting_cap = fields.Integer('Sitting Capacity (excluding you)')
