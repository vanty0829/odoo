from odoo import api, fields, models, _


class Tables(models.Model):
    _name = 'tables' # tển bảng
    _description = 'tables'

    name = fields.Char(string='Name', required = True)
    schema_id = fields.Many2one('schemas', string='Schema')