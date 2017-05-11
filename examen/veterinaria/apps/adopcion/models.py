from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Persona(models.Model):
	nombre = models.CharField(max_length=255)
	apellidos = models.CharField(max_length=255)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=255)
	email = models.EmailField()
	domicilio = models.TextField()

	def __str__(self):
		return '{}'.format(self.nombre)