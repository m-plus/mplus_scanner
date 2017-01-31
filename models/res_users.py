# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class res_users(osv.osv):
    _inherit = 'res.users'

    _columns = {
        'scanner_path': fields.char('Scanner app path'),
        'source_scan_document': fields.char('Scan document source'),
        'dest_scan_document': fields.char('Scan document destination'),
    }
    
    _defaults = {
        'scanner_path': 'C:/Windows/twain_32/Epson/TM-S2000Check/epcsapp.exe'
    }