from odoo import  fields,models

class StudentInformation(models.Model):
    _name = "student.information"
    _description = "Student Information"

    name = fields.Char (string = "Tên học sinh")
    birthday = fields.Date (string = "Ngày sinh")
    class_id = fields.Many2one("class.information",string = "Lớp")