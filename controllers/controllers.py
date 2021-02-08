from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class RatingPage(http.Controller):
    @http.route('/rating/<model("product.product"):product>', auth='user', type='http', website=True)
    def rating_page(self, product, **kwargs):
        values = {'product_id': product, 'user_id': request.env.user}
        return http.request.render('website_sale_rating.review_rating_page', values)


class WebsiteSaleInherit(WebsiteSale):
    @http.route(['/shop/product/<model("product.template"):product>'], type='http', auth="public", website=True)
    def product(self, product, category='', search='', **kwargs):
        res = super(WebsiteSaleInherit, self).product(product=product, category=category, search=search, **kwargs)
        domain = [('product_tmpl_id', '=', product.id),
                  ('active', '=', True)]
        reviews = request.env['review.rating'].sudo().search(domain)
        res.qcontext.update({'reviews': reviews})
        return res

class individualRatingPage(http.Controller):
    @http.route(['/individual-rating/<int:num>'], type="http", auth='public', website=True)
    def ind_rating(self, num, **kwargs):
        domain = [('rating', '=', num), ('active', '=', True)]
        reviews = request.env['review.rating'].sudo().search(domain)
        return http.request.render('website_sale_rating.selected_product_review', {'reviews': reviews})

class testindividualRatingPage(http.Controller):
    @http.route(['/individual-rating-test/'], type="http", auth='public', website=True)
    def test_ind_rating(self, **kwargs):
        domain = [('active', '=', True)]
        reviews = request.env['review.rating'].sudo().search(domain)
        return http.request.render('website_sale_rating.selected_product_review_test', {'reviews': reviews})
