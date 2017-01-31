odoo.define('mplus_scanner.Sidebar', function(require) {
"use strict";

var Sidebar = require('web.Sidebar');

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
                alert('in development');
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
