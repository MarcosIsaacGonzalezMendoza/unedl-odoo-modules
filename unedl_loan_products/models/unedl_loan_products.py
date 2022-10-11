# -*- coding: utf-8 -*-

from odoo import models, fields

class UnedlLoanProducts(models.Model):
    _name = 'unedl.loan.products'

    product_id = fields.Many2one(
        comodel_name='product.template', 
        string='Producto')
    loan_product_id = fields.Many2one(
        comodel_name='unedl.loan', 
        string='Folio de prestamo')
    
    
    