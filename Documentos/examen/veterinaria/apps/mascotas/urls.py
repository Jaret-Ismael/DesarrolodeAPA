urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', MascotaCreate.as_view(), name='crear'),
    url(r'^list$', MascotaList.as_view(), name='listar'),
    url(r'^edit/(?P<pk>\d+)/$', MascotaUpdate.as_view(), name='editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', MascotaDelete.as_view(), name='eliminar'),
]