from odoo import models, fields


class Customer(models.Model):
    _inherit = "res.partner"
    id_num = fields.Char("Identity Number")
    _sql_constraints = [('id_num','UNIQUE (cmt)','This Identity Number was exist!!!'), ]
