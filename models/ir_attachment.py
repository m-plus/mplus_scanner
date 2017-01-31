# -*- coding: utf-8 -*-
import base64
import os
import shutil

from openerp.osv import fields, osv
from openerp import tools, _
from openerp.exceptions import UserError

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

    def attach_scan_document(self, cr, uid, model, res_id, context=None):
        user = self.pool.get('res.users').browse(cr, uid, uid)
        if not user.source_scan_document or not user.dest_scan_document:
            raise UserError(_('Please set scan source and destination path!'))
        
        try:
            src_path = user.source_scan_document
            dst_path = user.dest_scan_document
            for fname in os.listdir(src_path):
                file_path = os.path.join(src_path, fname)
                if not os.path.isfile(file_path):
                    continue
                with open(file_path, mode='rb') as fh:
                    file_content = fh.read()
                
                #create attachment and link to object
                attachment_id = self.create(cr, uid, {
                    'name': fname,
                    'datas': base64.encodestring(file_content),
                    'datas_fname': fname,
                    'res_model': model,
                    'res_id': int(res_id)
                }, context)
                
                #move already attached file to destination path
                shutil.move(file_path, os.path.join(dst_path, fname))
            return {}
        except Exception, ex:
            _logger.info('Could not attach scan document: %s', tools.ustr(ex))
        
        return {
            'type': 'ir.actions.client',
            'tag': 'reload'
        }