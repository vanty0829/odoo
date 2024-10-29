from odoo import api, fields, models, _
import json
from . import utils as ms
from . import asutils as asms
from sqlalchemy import create_engine
from sqlalchemy.sql import text

class Requests(models.Model):
    _name = 'requests' # tển bảng
    _description = 'Requests'
    _rec_name = 'title'
    title = fields.Char(string='Title')
    description = fields.Char(string='Description')
    lake_id = fields.Many2one('lakehouse', string='Lakehouse')
    user_id = fields.Many2many('ms_user', string='Users')
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
        list1 = [i.id for i in self.env['tables'].search(domain)]
        list2 = [i.ids[0] for i in self.table_id]
        
        self.write({"table_id":[(6,0,list(set(list1) & set(list2)))]}) 

    table_id = fields.Many2many('tables', string='Table')
    # users = fields.Text(string='Users')
    
    from_date = fields.Datetime(string='From Date')
    to_date = fields.Datetime(string='To Date')
    active = fields.Boolean(default=True)

    request_state = [
        ('draft', "Draft"),
        ('submitted', "Submitted"),
        ('approved', "Approved"),
        ('revoked', "Revoked"),
    ]


    state = fields.Selection(
        selection=request_state,
        string="Status",
        readonly=True, copy=False, index=True,
        tracking=3,
        default='draft')
    
    state_a = fields.Selection(related='state')
    state_b = fields.Selection(related='state')
    
    def action_submit(self):
        self.state = 'submitted'

    def action_revoke(self):
        self.state = 'revoked'
        rmlist = []
        engine = create_engine('postgresql+psycopg2://odoo:odoo@localhost:5433/odoo')
        with engine.connect() as con:
            for i in self.user_id.ids:
                if ms.check_user_exist(self.ids[0],i) == 0:
                    rmlist.append(self.env['ms_user'].search([('id','=',i)])['name'])

                    con.execute(text(f"""
                                merge into public.lakehouse_ms_user_rel a
                                using (select {self.lake_id.id} lakehouse_id, {i} ms_user_id) b
                                on a.lakehouse_id = b.lakehouse_id
                                and a.ms_user_id = b.ms_user_id
                                when matched then delete;
                                COMMIT
                                """))
        asms.as_group_remove_list(self.lake_id.name,rmlist)
    
    def action_approve(self):
        self.state = 'approved'
        engine = create_engine('postgresql+psycopg2://odoo:odoo@localhost:5433/odoo')
        with engine.connect() as con:
            for line in self.user_id.ids:
                con.execute(text(f"""
                            merge into public.lakehouse_ms_user_rel a
                            using (select {self.lake_id.ids[0]} lakehouse_id, {line} ms_user_id) b
                            on a.lakehouse_id = b.lakehouse_id
                            and a.ms_user_id = b.ms_user_id
                            when not matched then
                            insert (lakehouse_id, ms_user_id)
                            values (b.lakehouse_id, b.ms_user_id);
                            COMMIT
                            """))
                try:
                    asms.as_group_add_list(self.lake_id.name,[self.env['ms_user'].search([('id','=',line)]).name])
                except:
                    pass


    # def group_api(self,values):
    #     engine = create_engine('postgresql+psycopg2://odoo:odoo@localhost:5433/odoo')
    #     lake_name = self.name if self.name else values['name']
    #     if self.ids:
    #         user_list = pd.read_sql( 
    #             f"SELECT ms_user_id id FROM public.lakehouse_ms_user_rel where lakehouse_id = {self.ids[0]}" , 
    #             con=engine 
    #         ).to_json(orient='records')
        
    #         lista = [self.env['ms_user'].search([('id','=',i['id'])]).name for i in json.loads(user_list)]
    #         listb = [i.name for i in self.user_id]
    #     else:
    #         lista = []
    #         listb = [self.env['ms_user'].search([('id','=',i[-1])])['name'] for i in values['user_id']]

    #     addlist = list(set(listb) - set(lista))
    #     rmlist = list(set(lista) - set(listb))

    #     asms.as_group_add_list(lake_name,addlist)
    #     asms.as_group_remove_list(lake_name,rmlist)
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