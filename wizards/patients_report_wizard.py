from datetime import date
from odoo import models, fields, api, _

class PatientsReportWizard(models.TransientModel):
    _name = "patients.report.wizard"
    _description = "Patients Report Wizard"
    
    patient_name = fields.Many2one("hospital.support.patients.informations", string="Patient Name:")
    date_from = fields.Date(string="Date From:")
    date_to = fields.Date(string="Date To:")
    

    def action_print_patients_report(self):
        datalist = []
        patients_report_w = self.env['hospital.support.patients.informations'].sudo().search([('create_date', '>=', self.date_from), ('create_date', '<=', self.date_to)])
        # patients_report_w = self.env['hospital.support.patients.informations'].search_read()
        print("==================================================================================")
        print(patients_report_w)
        print("==================================================================================")
        for line in patients_report_w:
            values = {
                'sl_no': line.sl_no,
                'name': line.name,
                'mobile': line.mobile,
                'address': line.address,
                'diseases': line.diseases,
                'description': line.description,
            }
            datalist.append(values)
        data = {
            'form_data': self.read()[0],
            'patients_report_w': datalist
        }
        return self.env.ref('hospital_support.action_patients_report_wizard').report_action(self, data=data)