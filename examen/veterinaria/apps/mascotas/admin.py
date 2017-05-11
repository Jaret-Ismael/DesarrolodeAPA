from __future__ import absolute_import
from django.contrib import admin
from apps.mascotas.models import Vacuna , Mascota
# Register your models here.
admin.site.register(Vacuna)
admin.site.register(Mascota)