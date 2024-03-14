
from odoo import api, models,fields


class ResConfigSettings(models.TransientModel):
  _inherit = 'res.config.settings'
  
  module_account = fields.Boolean("Create Invoice after Disconnect")
  
  # for future requirements  
  # def set_values(self):
  #   res = super(ResConfigSettings, self).set_values()
  #   self.env['ir.config_parameter'].sudo().set_param('odoo_space.generate_invoice', self.generate_invoice)
  #   return res

  # @api.model
  # def get_values(self):
  #     res = super(ResConfigSettings, self).get_values()
  #     generate_invoice = self.env['ir.config_parameter'].sudo().get_param('odoo_space.generate_invoice')
  #     res.update(generate_invoice=generate_invoice)
  #     return res