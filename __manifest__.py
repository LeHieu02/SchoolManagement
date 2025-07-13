{
    'name': 'School Management',
    'version': '1.0',
    'summary': 'Module to manage School',
    'description': """
        This module helps maintenance School.
    """,
    'author': 'Le Trung Hieu',
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        "view/menu_item.xml",
        "view/school_information.xml",
        "view/class_information.xml",
        "view/student_information.xml"
    ],
    'installable': True,
    'application': True,
}