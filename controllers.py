# -*- coding: utf-8 -*-
from openerp import http

# class Mythem(http.Controller):
#     @http.route('/mythem.js/mythem.js/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mythem.js/mythem.js/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mythem.js.listing', {
#             'root': '/mythem.js/mythem.js',
#             'objects': http.request.env['mythem.js.mythem.js'].search([]),
#         })

#     @http.route('/mythem.js/mythem.js/objects/<model("mythem.js.mythem.js"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mythem.js.object', {
#             'object': obj
#         })