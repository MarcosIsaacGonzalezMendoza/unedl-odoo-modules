# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UnedlLoanProducts(models.Model):
    _name = 'unedl.loan.products'

    product_id = fields.Many2one(
        comodel_name='unedl.products', 
        string='Producto')
    loan_product_id = fields.Many2one(
        comodel_name='unedl.loan', 
        string='Folio de prestamo')
    loan_quantity = fields.Float(
        string='Cantidad prestada')
    returned_quantity = fields.Float(
        string='Cantidad devuelta')
    
    # related
    available_quantity = fields.Float(
        string='Cantidad disponible',
        related='product_id.quantity_available')
    
    
    
    