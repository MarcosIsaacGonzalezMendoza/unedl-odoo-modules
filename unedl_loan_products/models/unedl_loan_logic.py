# -*- coding: utf-8 -*-

from odoo import models, fields
from ..settings import *

class UnedlLoan(models.Model):
    _inherit = 'unedl.loan'

    def start_loan_process(self):
        self.discount_inventory_items()
        self.state = PROCESS
        self.name = self.env['ir.sequence'].next_by_code('unedl_loan')


    def end_loan_process(self):
        self.add_inventory_items()
        missing_items_lines = self.line_ids.filtered(lambda x: x.returned_quantity < x.loan_quantity)
        if missing_items_lines:
            message = "Se entregaron objetos incompletos"
            self.state = MISSING
        else:
            message = "Se completó satisfactoriamente el préstamo, vuelve pronto"
            self.state = DELIVERED

        return {
            'effect':{
                'fadeout':'slow',
                'message':message,
                'type':'rainbow_man',
            }
        }
        

    def discount_inventory_items(self):
        for record in self:
            warehouse = self.env['stock.warehouse'].search([('company_id', '=', record.env.user.company_id.id)], limit=1)
            for line in record.line_ids:
                qty_available = (line.available_quantity - line.loan_quantity) * -1
                qty_available_total = (qty_available + line.available_quantity) * -1
                self.env['stock.quant']._update_available_quantity(line.product_id.product_variant_id, warehouse.lot_stock_id, qty_available_total)

    def add_inventory_items(self):
        for record in self:
            warehouse = self.env['stock.warehouse'].search([('company_id', '=', record.env.user.company_id.id)], limit=1)
            for line in record.line_ids:
                qty_available = (line.available_quantity - line.returned_quantity) * -1
                qty_available_total = (qty_available + line.available_quantity)
                self.env['stock.quant']._update_available_quantity(line.product_id.product_variant_id, warehouse.lot_stock_id, qty_available_total)