from odoo import api, fields, models, _
import json

class Requests(models.Model):
    _name = 'requests' # tển bảng
    _description = 'Requests'
    _rec_name = 'title'
    title = fields.Char(string='Title')
    description = fields.Char(string='Description')

    schema_id = fields.Many2many('schemas', string='Schema')

    table_id_domain = fields.Char(
       compute="_compute_table_id_domain",
       readonly=True,
       store=False,
   )



    @api.onchange("schema_id")
    def _compute_table_id_domain(self):
        domain = []
        id = 0
        for i in self.schema_id:
            if id == 0:
                domain = [('full_name','=like',f'{i.name}.%')]
            else:
                domain = ['|']+domain +[('full_name','=like',f'{i.name}.%')]
            id = id + 1
        # ['|',('full_name','=like','bronze.%'),('full_name','=like','silver.%')]
        self.table_id_domain = str(domain)

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

    def action_check(self):
        pass
    # column_id = fields.Many2many('columns', string='Column')
    # image = fields.Binary(string='Image', attachment = True)
    # country = fields.Char(string='Country', required = True)
    # gender = fields.Selection([('male','Male'),('female','Female')], string= 'Gender', default='male')
    # day_of_birth = fields.Datetime(string='Day of birth')
    # position =  fields.Char(string='Position',groups='module_category_player.group_player_manager')
    # height =  fields.Float(string='Height')
    # weight =  fields.Float(string='Weight')