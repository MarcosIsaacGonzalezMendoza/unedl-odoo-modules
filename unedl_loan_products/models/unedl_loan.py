# -*- coding: utf-8 -*-

from odoo import models, fields

class UnedlLoan(models.Model):
    _name = 'unedl.loan'

    name = fields.Char(string='Folio')
    partner_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Alumno')
    product_ids = fields.One2many(
        comodel_name='unedl.loan.products', 
        inverse_name='loan_product_id', 
        string='Productos a prestamo')
    comments = fields.Text(string='Comentarios')
    