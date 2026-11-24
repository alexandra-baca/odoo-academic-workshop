from odoo import models, fields


class Curso(models.Model):
    _name = 'academia.curso'
    _description = 'Curso'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre del curso', required=True)
    descripcion = fields.Text(string='Descripción')
    duracion = fields.Integer(string='Duración en horas')
    precio = fields.Float(string='Precio')
    fecha_inicio = fields.Date(string='Fecha de inicio')
    fecha_fin = fields.Date(string='Fecha de finalización')
    activo = fields.Boolean(string='Activo', default=True)

    alumno_ids = fields.One2many(
        "academia.alumno",  # Modelo que queremos recuperar
        "curso_id",  # Campo Many2one que conecta ambos modelos
        string="Alumnos"  # Nombre que mostrará Odoo
    )

    profesor_id = fields.Many2one(
        "academia.profesor",
        string="Profesor",
        ondelete="restrict"
    )