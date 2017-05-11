from __future__ import absolute_import
from django.conf.urls import url, include
from apps.adopcion.views import adopcion_view, adopcion_list, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete
urlpatterns = [
    #url(r'^index$', index_adopcion),
    url(r'^list$', SolicitudList.as_view(), name='listar'),
    url(r'^nuevo$', SolicitudCreate.as_view(), name='crear'),
 	url(r'^editar/(?P<pk>\d+)$', SolicitudUpdate.as_view(), name='editar'),
	url(r'^eliminar/(?P<pk>\d+)$', SolicitudDelete.as_view(), name='eliminar'),
       
]