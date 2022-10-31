# -*- coding: utf-8 -*-
from odoo import http


class HospitalSupport(http.Controller):
    @http.route('/hospital_support/hospital_support', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/hospital_support/hospital_support/objects', auth='public')
    def list(self, **kw):
        return http.request.render('hospital_support.listing', {
            'root': '/hospital_support/hospital_support',
            'objects': http.request.env['hospital_support'].search([]),
        })

    @http.route('/hospital_support/hospital_support/objects/<model("hospital.support.patients.informations"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('hospital_support.object', {
            'object': obj
        })
