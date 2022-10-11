# -*- coding: utf-8 -*-
# from odoo import http


# class UnedlLoanProducts(http.Controller):
#     @http.route('/unedl_loan_products/unedl_loan_products/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unedl_loan_products/unedl_loan_products/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('unedl_loan_products.listing', {
#             'root': '/unedl_loan_products/unedl_loan_products',
#             'objects': http.request.env['unedl_loan_products.unedl_loan_products'].search([]),
#         })

#     @http.route('/unedl_loan_products/unedl_loan_products/objects/<model("unedl_loan_products.unedl_loan_products"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unedl_loan_products.object', {
#             'object': obj
#         })
