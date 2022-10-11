# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class unedl_loan_products(models.Model):
#     _name = 'unedl_loan_products.unedl_loan_products'
#     _description = 'unedl_loan_products.unedl_loan_products'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
