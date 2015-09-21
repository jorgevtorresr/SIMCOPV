from django import forms 
from .models import Persona, Unidad

class PersonaForm(forms.ModelForm):
	def __init__ (self, *args, **kwargs):
		super(PersonaForm, self).__init__(*args, **kwargs)
		self.fields['cedula'].widget.attrs.update({'class':'form-control'})
		self.fields['nombre'].widget.attrs.update({'class':'form-control'})
		self.fields['apellido'].widget.attrs.update({'class':'form-control'})
		self.fields['puesto'].widget.attrs.update({'class':'form-control'})
		self.fields['unidad'].widget.attrs.update({'class':'form-control'})
		self.fields['foto'].widget.attrs.update({'class':'form-control'})
		self.fields['email'].widget.attrs.update({'class':'form-control'})
		self.fields['password'].widget.attrs.update({"class":"form-control"})

	cedula = forms.CharField(max_length=10)
	nombre = forms.CharField(max_length=25)
	apellido = forms.CharField(max_length=25)
	email = forms.EmailField()
	password = forms.CharField(max_length=16)

	class Meta:
		model = Persona
		fields = ("cedula","nombre","apellido","puesto","password","unidad","foto","email")

class UnidadForm(forms.ModelForm):
	def __init__ (self, *args, **kwargs):
		super(UnidadForm, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs.update({'class':'form-control'})

	class Meta:
		model = Unidad
		fields = "__all__"
    
class LoginForm(forms.Form):
	def __init__ (self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.fields['usuario'].widget.attrs.update({'class':'form-control'})
		self.fields['password'].widget.attrs.update({'class':'form-control'})

	usuario = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

class FrontImages(forms.Form):
	def __init__ (self, *args, **kwargs):
		super(FrontImages, self).__init__(*args, **kwargs)
		self.fields['imagen1'].widget.attrs.update({'class':'form-control'})
		self.fields['imagen2'].widget.attrs.update({'class':'form-control'})
		self.fields['imagen3'].widget.attrs.update({'class':'form-control'})
		self.fields['imagen4'].widget.attrs.update({'class':'form-control'})

	imagen1 = forms.ImageField()
	imagen2 = forms.ImageField()
	imagen3 = forms.ImageField()
	imagen4 = forms.ImageField()