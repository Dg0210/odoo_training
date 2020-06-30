from odoo import models, fields, _


class SaleOrderTags(models.Model):
    _name = 'sale.order.tags'
    _rec_name = 'name'

    name = fields.Char(string='Tags')
    name_count = fields.Integer(string='Delivery Count', compute='count_tag_id')

    def check_order_tags(self):
        view_id_tree = self.env.ref('sale.view_order_tree').id
        view_id_form = self.env.ref('sale.view_order_form').id
        return {
            'name': _('Order List'),
            'domain': [('tag_ids', 'in', self.ids)],
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'sale.order',
            'views': [(view_id_tree, 'tree'), (view_id_form, 'form')],
            'view_id ref="sale.view_order_tree"': '',
        }

    def count_tag_id(self):
        count = self.env['sale.order'].search_count(
            [('tag_ids', '=', self.id)])
        self.name_count = count

