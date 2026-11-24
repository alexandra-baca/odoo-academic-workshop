
from odoo import models, fields


class Alumno(models.Model):
    _name = "academia.alumno"
    _description = "Gestión de alumnos"
    _rec_name = "nombre"

    nombre = fields.Char(
        required=True,
        index=True,
        help="Nombre del alumno"
    )

    apellidos = fields.Char(
        required=True,
        index=True,
        help="Apellidos del alumno"
    )

    dni = fields.Char(
        required=True,
        copy=False,
        index=True,
        help="Documento Nacional de Identidad"
    )

    fecha_nacimiento = fields.Date()
    direccion = fields.Char()
    codigo_postal = fields.Char()
    ciudad = fields.Char()
    provincia = fields.Char()
    telefono = fields.Char()
    email = fields.Char()

    fecha_alta = fields.Date(
        default=fields.Date.today,
        readonly=True
    )

    activo = fields.Boolean(
        default=True
    )

    observaciones = fields.Text()

    curso_id = fields.Many2one(
        "academia.curso",
        string="Curso",
        required=True,
        ondelete="restrict"
    )

    asignatura_ids = fields.Many2many(
        'academia.asignatura',
        'academia_alumno_asignatura_rel',
        'alumno_id',
        'asignatura_id',
        string='Asignaturas'
    )