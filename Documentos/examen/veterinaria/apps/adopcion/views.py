from __future__ import absolute_import
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.adopcion.forms import PersonaForm, SolicitudForm
from apps.adopcion.models import Persona, Solicitud
# Create your views here.

def index(request):
	return render(request, 'adopcion/index.html')


def adopcion_view(request):
	if request.method == 'POST':
		form = PersonaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('mascota:index')
	else:
		form = PersonaForm()
	return render(request, 'adopcion/adopcion_form.html',{'form':form})

def adopcion_list(request):
	persona = Persona.objects.all()
	contexto = {'persona':persona}
	return render(request, 'adopcion/adopcion_list.html',contexto)
