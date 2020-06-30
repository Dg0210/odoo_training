{
    'name': 'Sales Orders',
    'category': 'Sales',
    'author': 'Dg210',
    'depends': [
        'base', 'sale'
    ],
    'data': ['views/customer_view.xml',
             'wizards/sale_order_tag_wizard.xml',
             'views/sale_order_tag.xml',
             'views/sale_order_sub_view.xml',
             'security/ir.model.access.csv',
             'reports/orders_reports.xml'
             ],
    'installable': True,
    'application': True,

}
