# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from ..settings import *

class GroupLeader(models.Model):
    _name = 'group.leader'

    name = fields.Char(string='Nombre')
    registration_number = fields.Char(string='Número de registro')
    age = fields.Integer(string='Edad')
    phone = fields.Char(string='Telefono')
    email = fields.Char(string='Correo')
    photo = fields.Image(string='Foto')
    