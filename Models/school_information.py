
from odoo import fields , models


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
    # class_list = fields.One2many("class.information", "school_id", string = "Danh sách lớp học")
