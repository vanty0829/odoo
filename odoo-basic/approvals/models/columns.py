from odoo import api, fields, models, _


class Columns(models.Model):
    _name = 'columns' # tển bảng
    _description = 'columns'

    name = fields.Char(string='Name', required = True)
    table_id = fields.Many2many('tables', string='Table')