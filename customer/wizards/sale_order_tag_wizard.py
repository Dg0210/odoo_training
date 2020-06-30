from odoo import models, fields, api


class SelectOrder(models.TransientModel):
    _name = "select.order"

    tag_id = fields.Many2one('sale.order.tag', string='tag')
    order_ids = fields.Many2many('sale.order', string='Đơn hàng', domain="[('tag_ids', 'not in', tag_id)]")

    @api.model
    def default_get(self, fields):
        res = super(SelectOrder, self).default_get(fields)
        active_id = self._context.get('active_id')
        res['tag_id'] = active_id
        return res

    def button_save_order(self):
        for order in self.order_ids:
            partner_id = self.env.context.get('active_id', False)
            partner = self.env['sale.order.tags'].browse(partner_id)
            order.tag_ids += partner

