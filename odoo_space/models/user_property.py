from odoo import fields,models

class User(models.Model):
    _name = "user.property"
    # never user underscore in name
    _description = "Users"

    name = fields.Char('Name',required=True)
    address = fields.Char('Address (only Locality)',required=True)
    postal = fields.Char('Pincode',required=True)
    designation = fields.Char('Designation',required=True)
    email = fields.Char("Email",required=True)
    phone =  fields.Char("Phone",required=True)
    department =  fields.Char("Department",required=True)
    interests = fields.Char("Interests")
    hobbies = fields.Char('Hobbies')
    has_vehicle = fields.Boolean('Has Vehicle ?',default=False)
    fuel_type = fields.Selection(
        string= 'Fuel Type',
        selection=[('pertrolDiesel','Pertrol / Diesel'),('electric', 'Electric'),('cng','CNG')]
    )
    vehicle_type = fields.Selection(
        string='Vehicle Type',
        selection=[('two_wheeler','Two Wheeler'),('four_wheeler','Four Wheeler')]
    )
    licence_plate = fields.Char("Licence Plate")
    vehiclepool = fields.Boolean('Want to Vehicle Pool',default=False)
    sitting_cap = fields.Integer('Sitting Capacity (excluding you)')
    active = fields.Boolean('Active',default=True)
