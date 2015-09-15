from django import forms 
from usuarios.models import Persona

class PersonaForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields = '__all__'

class LoginForm(forms.Form):
	def __init__ (self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.fields['usuario'].widget.attrs.update({'class':'form-control'})
		self.fields['password'].widget.attrs.update({'class':'form-control'})

	usuario = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())