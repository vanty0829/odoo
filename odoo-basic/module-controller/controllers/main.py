from odoo import http

class TyController(http.Controller):
    @http.route('/ty',auth='public',type='http')
    def ty_check(self):
        return "Check check"