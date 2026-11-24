from odoo import models,fields

class Reparacion(models.Model):
    _name = 'taller.reparacion'
    _description = 'Reparacion'
    _rec_name = 'description'

    description = fields.Text(string='description',required=True)
    fecha_entrada = fields.Datetime(string='Fecha de entrada',required=True, default=fields.Date.context_today)
    fecha_salida = fields.Datetime(string='Fecha de salida', default=fields.Date.context_today)
    coste = fields.Float(string='Coste',digits=(10, 2),default=0.0)
    activo = fields.Boolean(string='Activo', default=False)

    vehiculo_id = fields.Many2one("taller.vehiculo",string="Vehículo",required=True,ondelete="restrict")
