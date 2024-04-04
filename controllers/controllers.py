# -*- coding: utf-8 -*-
# from odoo import http


# class KedaMaterialReg(http.Controller):
#     @http.route('/keda_material_reg/keda_material_reg/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/keda_material_reg/keda_material_reg/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('keda_material_reg.listing', {
#             'root': '/keda_material_reg/keda_material_reg',
#             'objects': http.request.env['keda_material_reg.keda_material_reg'].search([]),
#         })

#     @http.route('/keda_material_reg/keda_material_reg/objects/<model("keda_material_reg.keda_material_reg"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('keda_material_reg.object', {
#             'object': obj
#         })
