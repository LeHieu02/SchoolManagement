from odoo import  fields,models

class StudentInformation(models.Model):
    _name = "student.information"
    _description = "Student Information"

    name = fields.Char (string = "Tên học sinh")
    birthday = fields.Date (string = "Ngày sinh")
    class_id = fields.Many2one("class.information",string = "Lớp")
    subject_list = fields.Many2many("subject.information","relation_subject_student","student_id","subject_id",string = "Danh sách môn học")


