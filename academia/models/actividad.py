from odoo import models, fields

class Actividad(models.Model):
    _name = 'academia.actividad'
    _description = 'Actividad'

    nombre = fields.Char(string='Nombre de la actividad', required=True)
    descripcion = fields.Text(string='Descripción')
    fecha = fields.Date(string='Fecha')
    hora = fields.Float(string='Hora')
    lugar = fields.Char(string='Lugar')
    tipo = fields.Selection([
        ('academica', 'Académica'),
        ('deportiva', 'Deportiva'),
        ('cultural', 'Cultural'),
    ], string='Tipo de actividad', default='academica')
    activo = fields.Boolean(string='Activo', default=True)