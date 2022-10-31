# -*- coding: utf-8 -*-

from dataclasses import field
from tkinter import Widget
from odoo import models, fields, api

# Patients Infromations
class PatientsInformations(models.Model):
    _name = 'hospital.support.patients.informations'
    _description = 'hospital.support.patients.informations'

    sl_no = fields.Char(string="SL No")
    name = fields.Char(string="Full Name")
    mobile = fields.Char(string="Mobile")
    address = fields.Char(string="Address")
    diseases = fields.Char(string="Diseases")
    description = fields.Text(string="Details")

    patients_under = fields.Many2many("hospital.support.doctors.informations", "patients_id")

# Doctors Infromations
class DoctorsInformations(models.Model):
    _name = 'hospital.support.doctors.informations'
    _description = 'hospital.support.doctors.informations'

    name = fields.Char(string="Doctor Name")
    code = fields.Integer(string="Code")
    mobile = fields.Char(string="Mobile")
    degree = fields.Char(string="Degrees")
    hospital = fields.Char(string="Hospital Name")

    specialists_id = fields.Many2one("hospital.support.specialists.informations", string="Specialist In")
    patients_id = fields.Many2many("hospital.support.patients.informations", "patients_under", string="Patients List")
    

# Specialists Infromations
class SpecialistsInformations(models.Model):
    _name = 'hospital.support.specialists.informations'
    _description = 'hospital.support.specialists.informations'

    name = fields.Char(string="Specialist Name")
    code = fields.Integer(string="Code")