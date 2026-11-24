from odoo import fields,models

class mecanico(models.Model):
    _name = 'taller.mecanico'
    _description = 'Mecanico'
    _rec_name = 'nombre'

    nombre = fields.Char(string='nombre', required=True, help='Nombre del mecanico')
    especialidad = fields.Char(string='Especialidad', help='Especialidad')
    telefono = fields.Char(string='Telefono')
    activo = fields.Boolean(string='Activo', default=True)

    reparacion_ids = fields.Many2many("taller.reparacion", string='Reparacion')
