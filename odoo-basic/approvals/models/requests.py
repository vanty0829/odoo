from odoo import api, fields, models, _


class Requests(models.Model):
    _name = 'requests' # tển bảng
    _description = 'Requests'
    _rec_name = 'title'
    title = fields.Char(string='Title')
    description = fields.Char(string='Description')
    schema_id = fields.Many2many('schemas', string='Schema')
    table_id = fields.Many2many('tables', string='Table')
    users = fields.Text(string='Users')
    
    from_date = fields.Datetime(string='From Date')
    to_date = fields.Datetime(string='To Date')
    active = fields.Boolean(default=True)

    request_state = [
        ('draft', "Draft"),
        ('submitted', "Submitted"),
        ('approved', "Approved"),
    ]


    state = fields.Selection(
        selection=request_state,
        string="Status",
        readonly=True, copy=False, index=True,
        tracking=3,
        default='draft')
    
    def action_submit(self):
        self.state = 'submitted'
    # column_id = fields.Many2many('columns', string='Column')
    # image = fields.Binary(string='Image', attachment = True)
    # country = fields.Char(string='Country', required = True)
    # gender = fields.Selection([('male','Male'),('female','Female')], string= 'Gender', default='male')
    # day_of_birth = fields.Datetime(string='Day of birth')
    # position =  fields.Char(string='Position',groups='module_category_player.group_player_manager')
    # height =  fields.Float(string='Height')
    # weight =  fields.Float(string='Weight')