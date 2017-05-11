from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Alumno
from .forms import AlumnoForm


def principal(request):
	admin = Admin.objects.order_by('id')
	template = loader.get_template('home.html')
	context = {
		'admin': admin	
	}
	return HttpResponse(template.render(context, request))

def hello_world(request):
	admin = Admin.objects.order_by('id')
	template = loader.get_template('index.html')
	context = {
		'admin': admin	
	}
	if request.user.is_authenticated():
		return HttpResponse(template.render(context, request))
	else:
		return HttpResponseRedirect('/')

def product_detail(request,pk):
	admin = get_object_or_404(admin, pk=pk)
	template = loader.get_template('product_detail.html')
	context = {
	'admin': admin
	}
	if request.user.is_authenticated():
		return HttpResponse(template.render(context, request))
	else:
		return HttpResponseRedirect('/')

def new_product(request):
	if request.method == 'POST':
		form = AdminForm(request.POST, request.FILES)
		if form.is_valid():
			admin = form.save()
			admin.save()
			return HttpResponseRedirect('/')
	else:
		form = AdminForm()
	template = loader.get_template('new_product.html')
	context = {
		'form': form
	}
	if request.user.is_authenticated():
		return HttpResponse(template.render(context, request))
	else:
		return HttpResponseRedirect('/')