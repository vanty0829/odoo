from odoo import api, fields, models, _


class Player(models.Model):
    _name = 'player' # tển bảng
    _description = 'Player'

    name = fields.Char(string='Name', required = True)
    image = fields.Binary(string='Image', attachment = True)
    country = fields.Char(string='Country', required = True)
    gender = fields.Selection([('male','Male'),('female','Female')], string= 'Gender', default='male')
    day_of_birth = fields.Datetime(string='Day of birth')
<<<<<<< HEAD
    position =  fields.Char(string='Position',groups='player.group_player_manager')
=======
    position =  fields.Char(string='Position',groups='module_category_player.group_player_manager')
>>>>>>> b521d79daac144f916ad8cc00c68f032b5b86f18
    height =  fields.Float(string='Height')
    weight =  fields.Float(string='Weight')