from odoo import api, fields, models, _


class ms_user(models.Model):
    _name = 'ms_user'
    _description = 'MS User'

    name = fields.Char(string='Username', required = True)