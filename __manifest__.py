{
    'name': 'School Management',
    'version': '1.0',
    'summary': 'Module to manage School',
    'description': """
        This module helps maintenance School.
    """,
    'author': 'Le Trung Hieu',
    'depends': ['base'],
    'assets': {
        'web.assets_backend': [
            'school/static/src/css/school_style.css',
        ],
    },
    'data': [
        "security/ir.model.access.csv",
        "view/menu_item.xml",
        "view/school_information.xml",
        "view/class_information.xml",
        "view/student_information.xml",
        "view/subject_information.xml",
        "view/teacher_information.xml",
        "view/academic_information.xml",
        "view/score_information.xml"
        # "view/assets_clean.xml"
    ],
    'installable': True,
    'application': True,
}