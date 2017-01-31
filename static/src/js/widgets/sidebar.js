odoo.define('mplus_scanner.Sidebar', function(require) {
"use strict";

var Sidebar = require('web.Sidebar');
var framework = require('web.framework');
var Model = require('web.DataModel');

Sidebar.include({
    init : function(){
        this._super.apply(this, arguments);
    },
    start: function() {
        var self = this;
        this._super(this);
        this.$el.off('click','.dropdown-menu li a');
        this.$el.on('click','.dropdown-menu li a', function(event) {
            if($(this).hasClass('file_scan')) {
                new Model("ir.attachment").call('attach_scan_document', [self.dataset.model, self.model_id]).then(function(result) {
                    if(result.type) {
                        self.do_action(result);
                    }
                    else {
                        self.do_attachement_update(self.dataset, self.model_id);
                        framework.unblockUI();
                    }
                });
            }
            else {
                var section = $(this).data('section');
                var index = $(this).data('index');
                var item = self.items[section][index];
                if (item.callback) {
                    item.callback.apply(self, [item]);
                } else if (item.action) {
                    self.on_item_action_clicked(item);
                } else if (item.url) {
                    return true;
                }
            }
            event.preventDefault();
        });
    },
});

return Sidebar;

});
