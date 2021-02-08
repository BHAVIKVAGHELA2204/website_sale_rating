{
    'name': 'Shop Rating & Review',

    'description': 'A Responsive Bootstrap Theme for Shop Rating',

    'summary': 'A Responsive Bootstrap Theme for Shop Rating',

    'category': 'Website',

    'version': '1.0',

    'depends': ['base', 'website', 'portal', 'website_form', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/review_field.xml',
        'views/assets.xml',
        'views/review_form.xml',
        'views/review_details.xml',
        'views/shop_website.xml',
        'views/product_view.xml',
        'views/template.xml',
        'views/product_review.xml',
    ],

    'images': [
        'static/src/img/Shopping-Cart.jpg',
    ],
    'author': "Test PVT LTD",
    'website': "https://test.io/",

    'application': False,
    'installable': True,
    'auto_install': False,

}
