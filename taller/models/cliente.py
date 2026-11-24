from odoo import models, fields

class Cliente(models.Model):
    _name = 'taller.cliente'
    _description = 'Cliente'
    _rec_name = 'nombre'

    nombre = fields.Char(string='nombre', required=True, help='Nombre del cliente')
    telefono = fields.Char(string='Telefono')
    email = fields.Char(string='Email', index=True)
    activo = fields.Boolean(string='Activo', default=True)

    #un cliente puede tener varios vehiculos
    vehiculo_ids = fields.One2many("taller.vehiculo", "cliente_id", string='Vehiculo')