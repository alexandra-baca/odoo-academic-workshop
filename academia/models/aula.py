
#clase Aula que hereda de models.Model
from odoo import models,fields

class Aula(models.Model):
    _name = 'academia.aula'
    _description = 'Aula'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre',required=True)
    codigo = fields.Char(string='Codigo',required=True)
    activo = fields.Boolean(default=True)
