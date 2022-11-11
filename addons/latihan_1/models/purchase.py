
import datetime
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    down_payment = fields.Float(string="Down Payment")
    total = fields.Float(string="Total", compute="get_total")

    @api.depends('amount_total', 'down_payment')
    def get_total(self):
        totals = self.amount_total - self.down_payment
        self.total = totals
