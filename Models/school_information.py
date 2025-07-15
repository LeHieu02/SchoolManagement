from re import search

from odoo import fields , models , api
from odoo.tools.populate import compute


class SchoolInformation (models.Model):
    _name = "school.information"
    _description = "school information"

    name = fields.Char(string = "Tên trường")
    type = fields.Selection([('private','Dân lập'), ('public','Công lập')],default = 'public', string = "Loại trường")
    email = fields.Text (string = "Email")
    address = fields.Text (string = " Địa chỉ")
    phoneNu = fields.Char (string = "Số điện thoại")
    hasOnlineClass = fields.Boolean(string = "Có lớp online không?")
    rank = fields.Integer(string = "Xếp hạng")
    establishDay = fields.Date(string = "Ngày thành lập")
    document = fields.Binary(string = "Tài liệu về trường")
    document_name = fields.Char(string = "Tên tài liệu")
    school_fee = fields.Monetary(string = "Học phí/môn học" ,compute = "_auto_count_fee", currency_field= "currency_school_id")
    currency_school_id = fields.Many2one ("res.currency",default=lambda self: self.env.ref("base.VND"), string = "Đơn vị")

    @api.depends("type")
    def _auto_count_fee(self):
        vnd_currency = self.env['res.currency'].search([("name","=","VND")], limit = 1)
        for rec in self:
            if rec.type == "private":
                rec.school_fee = 2000000
                rec.currency_school_id=vnd_currency
            else:
                rec.school_fee = 1000000
                rec.currency_school_id = vnd_currency

