from __future__ import absolute_import
from django.core.urlresolvers import reverse
from django.conf.urls import url, include
from apps.mascotas.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo/$', mascota_view, name='crear'),
    url(r'^list/$', mascota_list, name='listar'),
    url(r'^edit/(?P<pk>\d+)/$', mascota_edit, name='editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', mascota_delete, name='eliminar'),
    ]