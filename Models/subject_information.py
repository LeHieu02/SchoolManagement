from odoo import  fields,models

class subjectInformation (models.Model):
    _name = "subject.information"
    _description = "Subject Information"

    name = fields.Char (string = "Tên môn học")
    ID_MH = fields.Char (string = "Mã môn học")
    author = fields.Char (string = "Tác giả")
