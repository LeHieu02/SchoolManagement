from odoo import fields, models
from odoo.addons.test_impex.models import field


class ClassInformation(models.Model):
    _name = "class.information"
    _description = "Class Management"

    name = fields.Char (string = "Tên lớp")
    grade = fields.Char(string = "Khối")
    # mainTeacher = fields.Char(string = "GVCN")
    mainTeacher = fields.Many2one("teacher.information",string="GVCN")
    school_id = fields.Many2one ("school.information" , string = "Trường")
    student_list = fields.One2many("student.information","class_id",string = "Danh sách học sinh")
    address = fields.Text(related = "school_id.address", string = "Địa chỉ")

class SchoolInformation(models.Model):
    _inherit = "school.information"

    class_list = fields.One2many("class.information","school_id",string = "Danh sách lớp")