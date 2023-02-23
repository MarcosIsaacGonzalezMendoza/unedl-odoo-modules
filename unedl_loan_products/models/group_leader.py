# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from ..settings import *
from .check_data import *
class GroupLeader(models.Model):
    _name = 'group.leader'
    _sql_constraints = [
        ("registration_number_unique", "unique(registration_number)", "El número de registro ya existe, favor de verificar la información"),
    ]

    name = fields.Char(string='Nombre')
    registration_number = fields.Char(string='Número de registro')
    age = fields.Integer(string='Edad')
    phone = fields.Char(string='Telefono')
    email = fields.Char(string='Correo')
    photo = fields.Image(string='Foto')

    @api.constrains('age')
    def _constrains_age(self):
        for record in self:
            if record.age < 18:
                raise UserError("La edad miníma permitida es 18 años, verifica tu información")
    
    @api.constrains('name')
    def _constrains_name(self):
        for record in self:
            if not is_valid_name(record.name):
                raise UserError("La sintaxis del nombre no es adecuada, verifica tu información")

    @api.constrains('email')
    def _constrains_email(self):
        for record in self:
            if not is_valid_email(record.email):
                raise UserError("La sintaxis del correo no es adecuada, verifica tu información")
    
    @api.constrains('phone')
    def _constrains_phone(self):
        for record in self:
            if not is_valid_phone(record.phone):
                raise UserError("La sintaxis del Teléfono no es adecuada, verifica que sean 10 digitos sin espacios")


    @api.constrains('registration_number')
    def _constrains_registration_number(self):
        for record in self:
            if len(record.registration_number) != 11:
                raise UserError("La sintaxis del número de registro es incorrecta, verifica que sean 11 digitos")