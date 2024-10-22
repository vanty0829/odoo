from odoo import api, fields, models, _


class Requests(models.Model):
    _name = 'requests' # tển bảng
    _description = 'Requests'

    title = fields.Char(string='Title')
    description = fields.Char(string='Title')
    schema_id = fields.Many2many('schemas', string='Schema')
    table_id = fields.Many2many('tables', string='Table')
    column_id = fields.Many2many('columns', string='Column')
    # image = fields.Binary(string='Image', attachment = True)
    # country = fields.Char(string='Country', required = True)
    # gender = fields.Selection([('male','Male'),('female','Female')], string= 'Gender', default='male')
    # day_of_birth = fields.Datetime(string='Day of birth')
    # position =  fields.Char(string='Position',groups='module_category_player.group_player_manager')
    # height =  fields.Float(string='Height')
    # weight =  fields.Float(string='Weight')