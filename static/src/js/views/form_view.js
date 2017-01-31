odoo.define('mplus_scanner.FormView', function (require) {
"use strict";

var core = require('web.core');
var Model = require('web.DataModel');
var FormView = require('web.FormView');

var _t = core._t;

FormView.include({
    render_sidebar: function($node) {
        this._super.apply(this, arguments);
        if (this.sidebar && this.options.sidebar) {
            this.sidebar.add_items('other', [
                { label: _t('Scan document'), callback: this.on_button_scan_document },
            ]);
        }
    },
    on_button_scan_document: function() {
        var self = this;
        return new Model("ir.attachment").call('open_scan_app');
    },
});

return FormView;

});
