# -*- coding: utf-8 -*-
##############################################################################
#
# Plastics Extrusion Machinery LLC
# https://www.pemusa.com
#
##############################################################################

{
    "name": "PEMUSA Custom Reports",
    "summary": "PEMUSA Custom Reports",
    "version": "14.0",
    "author": "Plastics Extrusion Machinery LLC",
    "website": "https://www.pemusa.com",
    "category": "Warehouse Management",
    "depends": [
        'base',
        'mrp',
        'project',
        'stock',
    ],
    "data": [
        'report/label_part_tag_zpl_view.xml',
        'report/mrp_work_order_templates.xml',
        'report/report_paper_format.xml',
        'report/product_product.xml',
        'report/pallet_tag_view.xml',
        'report/pull_bin_tag_view.xml',
        'report/report.xml',
    ],
    "installable": True,
    "application": False,
}
