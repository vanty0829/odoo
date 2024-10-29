from odoo import api, fields, models, _
from . import utils as ms
from . import asutils as asms
from sqlalchemy import create_engine
import pandas as pd
import json
import asyncio
class Lakehouse(models.Model):
    _name = 'lakehouse'
    _description = 'lakehouse'

    name = fields.Char(string='Lake Name', required = True)
    user_id = fields.Many2many('ms_user', string='MS User')


    def group_api(self,values):
        engine = create_engine('postgresql+psycopg2://odoo:odoo@localhost:5433/odoo')
        lake_name = self.name if self.name else values['name']
        if self.ids:
            user_list = pd.read_sql( 
                f"SELECT ms_user_id id FROM public.lakehouse_ms_user_rel where lakehouse_id = {self.ids[0]}" , 
                con=engine 
            ).to_json(orient='records')
        
            lista = [self.env['ms_user'].search([('id','=',i['id'])]).name for i in json.loads(user_list)]
            listb = [i.name for i in self.user_id]
        else:
            lista = []
            listb = [self.env['ms_user'].search([('id','=',i[-1])])['name'] for i in values['user_id']]

        addlist = list(set(listb) - set(lista))
        rmlist = list(set(lista) - set(listb))

        asms.as_group_add_list(lake_name,addlist)
        asms.as_group_remove_list(lake_name,rmlist)
        

    @api.model
    def create(self, values):
        self.group_api(values)
        res = super(Lakehouse, self).create(values)
        return res


    def write(self, values):
        res = super(Lakehouse, self).write(values)
        self.group_api(values)
        return res