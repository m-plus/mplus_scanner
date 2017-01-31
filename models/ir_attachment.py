# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from openerp import tools

import logging
_logger = logging.getLogger(__name__)

class ir_attachment(osv.osv):
    _inherit = 'ir.attachment'
    
    def open_scan_app(self, cr, uid, context=None):
        try:
            user = self.pool.get('res.users').browse(cr, uid, uid)
            if user.scanner_path:
                import subprocess
                subprocess.Popen(user.scanner_path)
        except Exception, ex:
            _logger.info('Could not open app: %s', tools.ustr(ex))
        return True
