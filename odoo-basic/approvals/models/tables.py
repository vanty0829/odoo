from odoo import api, fields, models, _


class Tables(models.Model):
    _name = 'tables' # tển bảng
    _description = 'tables'
    _rec_name = 'full_name'
    name = fields.Char(string='Name', required = True)
    schema_id = fields.Many2one('schemas', string='Schema')
    full_name = fields.Char(string='Full Name', compute='_compute_name',store=True)
    schema_name = fields.Char(related='schema_id.name')

    @api.depends('schema_name', 'name')
    def _compute_name(self):
        for r in self:
            r.full_name = str(r.schema_name) + '.' + str(r.name)