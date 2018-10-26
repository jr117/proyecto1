from django import forms
from apps.clientes.models import Cliente

class ClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente
		fields = [
			'nombre',
			'apellido',
			'fechaHBD',
			'numHijos',
		]

		labels = {
			'nombre' : 'Nombre',
			'apellido' : 'Apellidos',
			'fechaHBD' : 'Año de nacimiento',
			'numHijos' : 'Numero de hijos',
		}

		widgets = {
			'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
			'apellido' : forms.TextInput(attrs={'class' : 'form-control'}),
			'fechaHBD' : forms.TextInput(attrs={'class' : 'form-control'}),
			'numHijos' : forms.TextInput(attrs={'class' : 'form-control'}),
		}