from __future__ import unicode_literals
from __future__ import absolute_import
from django.db import models
from apps.adopcion.models import Persona


# Create your models here.
class Vacuna(models.Model):
	"""docstring for Vacuna"""
	nombre = models.CharField(max_length=50)
	def __init__(self):

		return '{}'.format(self.nombre)
		
		

class Mascota(models.Model):
	nombre = models.CharField(max_length=255)
	raza = models.CharField(max_length=255)
	sexo = models.CharField(max_length=255)
	persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	vacuna = models.ManyToManyField(Vacuna, blank=True)

	def __init__(self):

		return '{}'.format(self.nombre)
		