from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	cliente = models.CharField(max_length=255)
	fecha de adopcion = models.CharField(max_length=255)
	numero de telefono = models.DecimalField(max_digits=10,decimal_places=2)
