from odoo import fields, models,api

class AcademicYear(models.Model):
    _name = "academic.year"
    _description = "Academic Year"

    name = fields.Char(string="Tên năm học")
    start_date = fields.Date(string="Từ ngày")
    end_date = fields.Date(string="Đến ngày")
    semester_ids = fields.One2many("academic.semester", "year_id", string="Danh sách học kỳ")

class AcademicSemester(models.Model):
    _name = "academic.semester"
    _description = "Học kỳ"

    name = fields.Selection([('1', 'Học kỳ 1'), ('2', 'Học kỳ 2')], string="Tên học kỳ")
    year_id = fields.Many2one("academic.year", string="Năm học")
    start_date = fields.Date(string="Từ ngày")
    end_date = fields.Date(string="Đến ngày")
    score_ids = fields.One2many("student.semester.score", "semester_id", string="Bảng điểm")

class StudentSemesterScore(models.Model):
    _name = "student.semester.score"
    _description = "Điểm trung bình học sinh theo học kỳ"

    student_id = fields.Many2one("student.information", string="Học sinh")
    semester_id = fields.Many2one("academic.semester", string="Học kỳ")
    score_list = fields.One2many("score.information", "student_semester_id", string="Bảng điểm")
    average_score = fields.Float(string="Điểm trung bình", compute="_compute_average")
    ranking = fields.Selection([("XS", "Xuất sắc"), ("GI", "Giỏi"), ("KH", "Khá"), ("TB", "Trung bình"), ("YE", "Yếu")],
                               compute="_compute_ranking", string="Xếp loại")

    @api.depends("score_list.score")
    def _compute_average(self):
        for rec in self:
            total = sum(rec.score_list.mapped("score"))
            count = len(rec.score_list)
            rec.average_score = total / count if count else 0

    @api.depends("average_score")
    def _compute_ranking(self):
        for rec in self:
            if rec.average_score >= 9.0:
                rec.ranking = "XS"
            elif rec.average_score >= 8.0:
                rec.ranking = "GI"
            elif rec.average_score >= 6.5:
                rec.ranking = "KH"
            elif rec.average_score >= 5.0:
                rec.ranking = "TB"
            else:
                rec.ranking = "YE"
