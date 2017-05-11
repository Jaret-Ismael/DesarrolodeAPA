from __future__ import absolute_import
from django import forms
from apps.mascotas.models import Mascota
from apps.mascotas.models import Persona

class MascotaForm(forms.ModelForm):
	class Meta:
		model = Mascota

		fields = [
			'nombre',
			'sexo',
			'raza',
			#'',
			'persona',
			'vacuna',
		]
		label = {
			'nombre': 'Nombre',
			'sexo' : 'Sexo',
			#'edad_aprox': 'Edad',
			#'fecha_rescate': 'Fecha de rescate',
			'persona': 'Adoptante',
			'vacuna': 'Vacunas',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'sexo': forms.TextInput(attrs={'class':'form-control'}),
			#'edad_aprox': forms.TextInput(attrs={'class':'form-control'}),
			#'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
			'persona': forms.Select(attrs={'class':'form-control'}),
			'vacuna': forms.CheckboxSelectMultiple(),
		}