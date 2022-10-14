# -*- coding: utf-8 -*-

from odoo import models, fields
from ..settings import *

class UnedlLoan(models.Model):
    _inherit = 'unedl.loan'

    def start_loan_process(self):
        self.state = PROCESS
        self.name = self.env['ir.sequence'].next_by_code('unedl_loan')

    def end_loan_process(self):
        self.state = DELIVERED

    def declare_missing_loan(self):
        self.state = MISSING