# # -*- coding: utf-8 -*-

from odoo import models, fields, api


class Persons(models.Model):
    _name = 'person.person'
    _description = 'person.person'

    first_name = fields.Char()
    last_name = fields.Char()
    full_name = '{0} {1}'.format(first_name, last_name)
    birthday = fields.Date(string='Dates')
    age = fields.Integer(compute='_compute_age')
    sex = fields.Selection([
        ('male', 'Male'), 
        ('female', 'Female'), 
        ('non-binary', 'Non-binary')])
    company_id = fields.Many2one('res.company')