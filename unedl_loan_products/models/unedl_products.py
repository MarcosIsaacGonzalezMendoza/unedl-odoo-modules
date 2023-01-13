# -*- coding: utf-8 -*-

from odoo import models, fields

class UnedlProducts(models.Model):
    _name = 'unedl.products'

    name = fields.Char(string='Nombre')
    code = fields.Char(string='Código')
    quantity_available = fields.Float(string='Cantidad disponible')
    description = fields.Text(string='Descripción')
    photo = fields.Image(string='Foto')