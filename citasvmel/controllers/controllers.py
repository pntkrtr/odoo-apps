# -*- coding: utf-8 -*-
from odoo import http

# class Citasvmel(http.Controller):
#     @http.route('/citasvmel/citasvmel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/citasvmel/citasvmel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('citasvmel.listing', {
#             'root': '/citasvmel/citasvmel',
#             'objects': http.request.env['citasvmel.citasvmel'].search([]),
#         })

#     @http.route('/citasvmel/citasvmel/objects/<model("citasvmel.citasvmel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('citasvmel.object', {
#             'object': obj
#         })