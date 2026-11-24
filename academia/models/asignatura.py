from odoo import models, fields


class Asignatura(models.Model):
    _name = 'academia.asignatura'
    _description = 'Asignatura'
    _rec_name = 'nombre'

    nombre = fields.Char(
        string='Nombre de la asignatura',
        required=True
    )
    codigo = fields.Char(
        string='Código',
        required=True
    )
    descripcion = fields.Text(
        string='Descripción'
    )
    duracion_horas = fields.Integer(
        string='Duración en horas'
    )
    activo = fields.Boolean(
        string='Activo',
        default=True
    )

    alumno_ids = fields.Many2many(
        'academia.alumno',
        'academia_alumno_asignatura_rel',
        'asignatura_id',
        'alumno_id',
        string='Alumnos'
    )