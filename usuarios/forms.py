from django import forms
from django.forms import ModelForm
from usuarios.models import Persona

class PersonaForm(ModelForm):
	class Meta:
		model = Persona
		fields = '__all__'