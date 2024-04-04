from odoo import http
from odoo.http import request
import json
import logging
_logger = logging.getLogger(__name__)

class MaterialControllers(http.Controller):
    @http.route('/registered-material', auth='public', type='http', website=True)
    def display_registered_material(self, **kw):
        material_register = request.env['material.reg']
        
        material_id = kw.get('_id')
        if material_id:
            material = material_register.sudo().browse(int(material_id))
            if material:
                partner_name = material.partner_id.name if material.partner_id else ""
                material_data = {
                    'id': material.id,
                    'name': material.name,
                    'mat_code': material.mat_code,
                    'mat_type': material.mat_type,
                    'buy_price': material.buy_price,
                    'partner_name': partner_name
                }
                return json.dumps(material_data)
            else:
                return 'Material not found', 404
        else:
            mat_type = kw.get('mat_type')
            if mat_type:
                materials = material_register.search([('mat_type', '=', mat_type)])
            else:
                materials = material_register.search([])
            
            material_data = []
            for material in materials:
                partner_name = material.partner_id.name if material.partner_id else ""
                material_data.append({
                    'id': material.id,
                    'name': material.name,
                    'mat_code': material.mat_code,
                    'mat_type': material.mat_type,
                    'buy_price': material.buy_price,
                    'partner_name': partner_name
                })
            return json.dumps(material_data)

    @http.route('/update-material/<int:material_id>', type='json', auth='public', website=True, methods=['PATCH'])
    def update_material(self, material_id, **kwargs):
        req_dict = request.jsonrequest
        buy_price = req_dict.get('buy_price')
        if buy_price:
            material_register = request.env['material.reg']
            material = material_register.browse(material_id)
            if material:
                material.write({'buy_price': float(buy_price)})
                return 'Material with ID {} updated successfully with buy_price: {}'.format(material_id, buy_price)
            else:
                return 'Material not found'
        else:
            return 'Missing buy_price parameter'
        
    @http.route('/delete-material/<int:material_id>', type='json', auth='public', website=True, methods=['DELETE'], csrf=False)
    def delete_material(self, material_id):
        req_dict = request.jsonrequest
        if req_dict.get('delete') == True:
            material_register = request.env['material.reg']
            material = material_register.sudo().browse(material_id)
            if material:
                material.unlink()
                return 'Material with ID {} deleted successfully'.format(material_id), 200
            else:
                return 'Material not found', 404
        else:
            return "You're not allowed to delete this record", 404