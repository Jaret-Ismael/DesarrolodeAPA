from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.CharField(max_length=255)
	categoria = models.CharField(max_length=255)
	