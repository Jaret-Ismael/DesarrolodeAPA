from django.conf.urls import url
from . import views

urlpatterns =[
	url(r'^$',views.principal, name='home'),
	url(r'^admin',views.hello_world, name='hello'),
	url(r'^leo/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail'),
	url(r'^leo/new',views.new_product,name="new_product")

]