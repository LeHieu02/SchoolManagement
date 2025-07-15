from odoo import  fields,models,api

class StudentInformation(models.Model):
    _name = "student.information"
    _description = "Student Information"

    name = fields.Char (string = "Tên học sinh")
    birthday = fields.Date (string = "Ngày sinh")
    class_id = fields.Many2one("class.information",string = "Lớp")
    subject_list = fields.Many2many("subject.information","relation_subject_student","student_id","subject_id",string = "Danh sách môn học")
    student_fee = fields.Monetary(string = "Tổng học phí", currency_field="currency_id",compute = "_compute_student_fee")
    currency_id = fields.Many2one("res.currency",default=lambda self: self.env.ref("base.VND"),string = "Đơn vị")

    @api.depends("subject_list", "class_id.school_id.school_fee")
    def _compute_student_fee(self):
        vnd_currency = self.env['res.currency'].search([('name', '=', 'VND')], limit=1)
        for rec in self:
            rec.student_fee = len(rec.subject_list) * (rec.class_id.school_id.school_fee)
            rec.currency_id = vnd_currency

class ScoreInformation(models.Model):
    _name = "score.information"
    _description = "Score Information"

    student_id = fields.Many2one("student.information", string = "Học sinh")
    subject_id = fields.Many2one("subject.information", string = "Môn học")
    score = fields.Float(string = "Điểm số")
    # semester = fields.Selection([("HK1","Học kỳ 1"),("HK2","Học kỳ 2")],string = "Học Kỳ")
    semester_id = fields.Many2one("academic.semester", string="Học kỳ", required=True)
    student_semester_id = fields.Many2one("student.semester.score", string="Bảng điểm học kỳ")


