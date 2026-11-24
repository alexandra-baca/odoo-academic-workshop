from odoo import models, fields

class Profesor(models.Model):
    _name = 'academia.profesor'
    _description = 'Profesor'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos')
    especialidad = fields.Char(string='Especialidad')
    email = fields.Char(string='Correo electrónico')
    telefono = fields.Char(string='Teléfono')
    fecha_contratacion = fields.Date(string='Fecha de contratación')
    activo = fields.Boolean(string='Activo', default=True)

    curso_ids = fields.One2many(
        "academia.curso",
        "profesor_id",
        string="Cursos"
    )