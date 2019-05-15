# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Professor(models.Model):
    _name = 'openacademy.professor'

    professor_nom = fields.Char('nom', size=20, required=True)
    professor_cognoms = fields.Char('cognoms', size=30, required=True)
    phone = fields.Char('telèfon', size=9, required=True)
    email = fields.Char('correuElectrònic')    
    professor_id = fields.One2many('openacademy.curs', 'professor')


class Materia(models.Model):
    _name = 'openacademy.materia'

    materia_nom = fields.Char('nom', size=20, required=True)
    descripcio = fields.Text()
    materia_id = fields.One2many('openacademy.curs', 'materia')


class Curs(models.Model):
    _name = 'openacademy.curs'

    curs_nom = fields.Char(string="nom", size=20, required=True)
    nivell = fields.Char(string="nivell", size=20)
    professor = fields.Many2one('openacademy.professor', 'professor_id')
    materia = fields.Many2one('openacademy.materia', 'materia_id')
    alumne = fields.Many2one('openacademy.alumne','alumne_id')
	
class Alumne(models.Model):
    _name = 'openacademy.alumne'

    alumne_nom = fields.Char(string="nom", size=20)
    alumne_cognoms = fields.Char(string="cognoms", size=20)
    alumne_id = fields.One2many('openacademy.curs', 'alumne')
	
    
	
	
	


