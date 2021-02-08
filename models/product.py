# -*- coding: utf-8 -*-
# Part of Heliconia Solutions Pvt.ltd.
# See LICENSE file for copyright and licensing details.

from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    review_ids = fields.One2many('review.rating', 'product_tmpl_id', 'Reviews')
    avg_review = fields.Float('Average Reviews', compute='_compute_avg_review', digits=(2, 2))

    @api.depends('review_ids')
    def _compute_avg_review(self):
        total_review = 0.0
        count = 0
        if self.review_ids:
            for review_id in self.review_ids:
                total_review += review_id.rating
                count += 1
            self.avg_review = round((total_review / count), 2)
        else:
            self.avg_review = 0

    def get_ratings(self):
        '''
            @return: dict of rating
        '''
        rating_dict = {1: {'count': 0, 'style': 'width:0%', 'class': 'progress-bar progress-bar-danger'},
                       2: {'count': 0, 'style': 'width:0%', 'class': 'progress-bar progress-bar-warning'},
                       3: {'count': 0, 'style': 'width:0%', 'class': 'progress-bar progress-bar-info'},
                       4: {'count': 0, 'style': 'width:0%', 'class': 'progress-bar progress-bar-primary'},
                       5: {'count': 0, 'style': 'width:0%', 'class': 'progress-bar progress-bar-success'}}
        rating_list = []
        total_count = 0.0
        if self.review_ids:
            for review_id in self.review_ids:
                total_count += 1
                if rating_dict.get(review_id.rating):
                    rating_dict[review_id.rating].update({'count': rating_dict[review_id.rating]['count'] + 1})
                else:
                    rating_dict[review_id.rating].update({'pert': 0})
            for pert in self.review_ids:
                if rating_dict.get(pert.rating):
                    rating_dict[pert.rating].update(
                        {'pert': int((rating_dict[pert.rating]['count'] / total_count) * 100)})
            for r in range(1, 6):
                width_per = int(round((rating_dict[r].get('count') / total_count) * 100))
                width_str = "width:" + str(width_per) + "%"
                rating_dict[r].update({'style': width_str})
                rating_list.append(rating_dict[r])
            rating_list.reverse()

            return rating_list
        else:
            for r in range(1, 6):
                rating_list.append(rating_dict[r])
            rating_list.reverse()

            return rating_list
