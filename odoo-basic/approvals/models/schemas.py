from odoo import api, fields, models, _


class Schemas(models.Model):
    _name = 'schemas' # tển bảng
    _description = 'schemas'

    name = fields.Char(string='Name', required = True)