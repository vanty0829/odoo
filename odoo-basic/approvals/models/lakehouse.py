from odoo import api, fields, models, _
from . import utils as ms
from sqlalchemy import create_engine
import pandas as pd
import json

class Lakehouse(models.Model):
    _name = 'lakehouse'
    _description = 'lakehouse'

    name = fields.Char(string='Lake name', required = True)
    group_id = fields.Char(string='Group ID', required = True)
    user_id = fields.Many2many('ms_user', string='MS User')


    def group_api(self):
        engine = create_engine('postgresql+psycopg2://odoo:odoo@localhost:5433/odoo')
        user_list = pd.read_sql( 
            f"SELECT ms_user_id id FROM public.lakehouse_ms_user_rel where lakehouse_id = {self.ids[0]}" , 
            con=engine 
        ).to_json(orient='records')
        lista = [self.env['ms_user'].search([('id','=',i['id'])]).object_id for i in json.loads(user_list)]
        listb = [i.object_id for i in self.user_id]
        addlist = list(set(listb) - set(lista))
        rmlist = list(set(lista) - set(listb))

        for i in addlist:
            ms.group_add_member(self.group_id,i)

        for i in rmlist:
            ms.group_remove_member(self.group_id,i)

    @api.model
    def create(self, values):
        res = super(Lakehouse, self).create(values)
        self.group_api()
        return res


    def write(self, values):
        res = super(Lakehouse, self).write(values)
        self.group_api()
        return res