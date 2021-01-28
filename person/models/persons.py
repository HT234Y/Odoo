# # -*- coding: utf-8 -*-

from odoo import models, fields, api


class Persons(models.Model):
    _name = 'person.person'
    _description = 'person.person'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    full_name = fields.Char(compute='_compute_full_name')
    birthday = fields.Date(string='Dates')
    age = fields.Integer(compute='_compute_age')
    sex = fields.Selection([
        ('male', 'Male'), 
        ('female', 'Female'), 
        ('non-binary', 'Non-binary')])
    company_id = fields.Many2one('res.company', required=True)

    def _compute_age(self):
        if self.birthday:
            d1 = self.birthday
            d2 = date.today()
            self.age = relativedelta(d2, d1).years

    def _compute_full_name(self):
        return "{0} {1}".format(first_name, last_name)