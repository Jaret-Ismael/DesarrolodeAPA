from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	raza = models.CharField(max_length=255)
	edad = models.CharField(max_length=255)
	vacunas = models.CharField(max_length=255)
	fecha de adopcion = models.DecimalField(max_digits=24,decimal_places=2)