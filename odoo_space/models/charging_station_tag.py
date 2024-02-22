from odoo import fields,models

class StationTag(models.Model):
    _name = "charging.station.tag"
    _description = "tags for charging stations"

    name = fields.Char('Tags',required=True)
    color = fields.Integer(string='Color')
    # desc = fields.Char('Description',required=True,default="no desc") added for testing purpose

    # sql constraints
    _sql_constraints = [
        ('unique_name','UNIQUE(name)',"Tag with the same name already exists")
    ]
