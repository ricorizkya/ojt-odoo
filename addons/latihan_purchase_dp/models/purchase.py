import datetime
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime,timedelta

class SaleOrder(models.Model):
    _inherit = "purchase.order"

    down_payment = fields.Float(string="Down Payment")