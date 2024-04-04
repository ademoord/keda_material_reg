from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class MaterialRegister(models.Model):
    _name = 'material.reg'
    _description = 'Material Registration'

    name = fields.Char(string='Material No', required=True)
    mat_code = fields.Char(string='Code', required=True)
    mat_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], string='Type', required=True)
    buy_price = fields.Float(string='Sale Price', required=True)
    partner_id = fields.Many2one('res.partner', string='Related Supplier', required=True)

    @api.constrains('buy_price')
    def _check_buy_price(self):
        for record in self:
            if record.buy_price < 100:
                raise ValidationError(_("The sale price must be equal to or greater than 100."))
    