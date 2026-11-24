
{
    'name': 'Academia',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Gestión de una academia',
    'description': 'Módulo para gestionar alumnos, profesores, cursos y actividades.',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/alumno_views.xml',
        'views/profesor_views.xml',
        'views/curso_views.xml',
        'views/actividad_views.xml',
        'views/aula_views.xml',
        'views/asignatura_views.xml',

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
