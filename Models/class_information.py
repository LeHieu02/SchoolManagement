from odoo import fields, models
from odoo.addons.test_impex.models import field


class ClassInformation(models.Model):
    _name = "class.information"
    _description = "Class Management"

    name = fields.Char (string = "Tên lớp")
    grade = fields.Char(string = "Khối")
    mainTeacher = fields.Char(string = "GVCN")
    school_id = fields.Many2one ("school.information" , string = "Trường")
    student_list = fields.One2many("student.information","class_id",string = "Danh sách học sinh")

class SchoolInformation(models.Model):
    _inherit = "school.information"

    class_list = fields.One2many("class.information","school_id",string = "Danh sách lớp")