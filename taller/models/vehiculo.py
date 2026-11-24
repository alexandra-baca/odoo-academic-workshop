from odoo import models,fields

class Vehiculo(models.Model):
    _name = 'taller.vehiculo'
    _description = 'Vehículo'
    _rec_name = 'matricula'

    matricula = fields.Char(string='matricula', index=True, required=True, help="Matricula", copy=False)
    marca = fields.Char(string='Marca', required=True, help='Marca del Vehiculo')
    modelo = fields.Char(string='Modelo', required=True, help='Modelo del Vehiculo')
    anio = fields.Integer(string='Año')

    cliente_id = fields.Many2one("taller.cliente",string='Cliente',required=True,ondelete = "restrict")

    reparacion_ids = fields.One2many("taller.reparacion","vehiculo_id",string="Reparaciones")