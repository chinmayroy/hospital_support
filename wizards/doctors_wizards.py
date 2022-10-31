from odoo import models, fields, api, _

class DoctorsWizards(models.TransientModel):
    _name = "doctors.wizards"
    _description = "Doctors Wizards"
    
    doctors_hospital = fields.Char(string="New Hospital")

    def action_add_hospital(self):
        print('code', self._context.get('active_id'))
        print('Doctors Hospital', self.doctors_hospital)

        doctor = self.env['hospital.support.doctors.informations'].browse(self._context.get('active_id'))
        if doctor:
            doctor.hospital = self.doctors_hospital
            return {'type': 'ir.actions.client', 'tag': 'reload'}
        return {'type': 'ir.actions.act_window_close'}