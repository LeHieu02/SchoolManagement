from odoo import  fields,models,api
from odoo.fields import Many2one


class teacherInformation(models.Model):
    _name = "teacher.information"
    _description = "Teacher Information"

    name = fields.Char(string = "Ten giao vien")
    phone = fields.Char (string = "So dien thoai")
    email = fields.Char(string = "Email")
    subject_id = fields.Many2many ("subject.information","relation_teacher_subject","teacher_id","subject_id", string = "Danh sach mon hoc")
    class_list = fields.Many2many("class.information","relation_class_teacher","teacher_id", "class_id",string="Lớp đang dạy")
