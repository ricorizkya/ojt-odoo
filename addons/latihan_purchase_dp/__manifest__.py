# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Latihan Purchase DP',
    'category': 'Purchase',
    'author': 'Rico',
    'version': '1.0',
    'website': 'http://www.solvera.id/',
    'description': """
       Latihan menambahkan field DP
    """,
    'data': [
	'views/purchase_order.xml',

    ],
    "depends": [
        "purchase"
    ],
    'installable': True,
    "images":['static/logo.png'],
}
