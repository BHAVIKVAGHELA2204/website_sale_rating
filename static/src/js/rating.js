odoo.define('website_sale_rating.product_rating', function(require) {
"use strict";

    var ajax = require('web.ajax');
    require('web.dom_ready');

    $('#add_product_rating').click(function (event) {
        var product_id = $('input.product_id').val()
        var url = '/rating/' + product_id
        window.location.replace(url);
    });

});
