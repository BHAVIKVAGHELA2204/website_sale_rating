from odoo import fields, models, api
from datetime import date
from dateutil import relativedelta
import datetime as dt


class ReviewRating(models.Model):
    _name = "review.rating"
    _description = "Review Rating Details"
    _rec_name = 'subject'

    subject = fields.Char(string='Subject')
    review = fields.Text(string='Review')
    rating = fields.Integer(string='Rating')
    product_id = fields.Many2one('product.product', string='Product')
    product_tmpl_id = fields.Many2one('product.template', related='product_id.product_tmpl_id', string='Product',
                                      store=True)
    user_id = fields.Many2one('res.users', string='User')
    reviewed_date = fields.Date(string="Reviewed Date", default=date.today())
    get_reviewed_days = fields.Char(string="Review Day's Ago",
                                    compute='compute_reviewed_days')
    active = fields.Boolean(default=True,
                            help="Set archive to true to hide the maintenance request without deleting it.")

    @api.model
    def create(self, vals):
        if not vals.get('user_id'):
            vals['user_id'] = self.env.user.id
        return super(ReviewRating, self).create(vals)

    def compute_reviewed_days(self):
        for rec in self:
            diff = (relativedelta.relativedelta(dt.date.today(), rec.reviewed_date))
            if diff:
                years = diff.years
                months = diff.months
                days = diff.days
                if years:
                    if months:
                        rec.get_reviewed_days = '%d Year %d months ago' % (years, months)
                    else:
                        rec.get_reviewed_days = '%d years ago' % (years,)
                elif months:
                    rec.get_reviewed_days = '%d months ago' % (months,)
                elif diff.days:
                    rec.get_reviewed_days = '%d days ago' % (days,)
            else:
                rec.get_reviewed_days = 'Today'
