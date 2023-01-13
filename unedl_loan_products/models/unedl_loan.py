# -*- coding: utf-8 -*-

from odoo import models, fields
from ..settings import LOAN_STATE

class UnedlLoan(models.Model):
    _name = 'unedl.loan'
    _order = 'name DESC'
    _inherit = ['mail.thread', 'portal.mixin']
    _description = 'Folio de prestamo'

    name = fields.Char(string='Folio')
    state = fields.Selection(
        string='Estado', 
        selection=LOAN_STATE,
        tracking=True)
    partner_id = fields.Many2one(
        comodel_name='group.leader', 
        string='Jefe de grupo')
    line_ids = fields.One2many(
        comodel_name='unedl.loan.products', 
        inverse_name='loan_product_id', 
        string='Líneas a prestamo',
        tracking=True)
    comments = fields.Text(string='Comentarios',
    tracking=True)

    # related_fields
    partner_image = fields.Binary(
        string='Jefe de grupo',
        related='partner_id.photo')
    