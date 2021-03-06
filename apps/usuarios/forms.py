from django import forms 
from django.contrib.auth.models import User
from django.forms.models import model_to_dict, fields_for_model
from .models import Persona, Unidad, Periodo

class PersonaForm(forms.ModelForm):
	def __init__ (self, *args, **kwargs):
		super(PersonaForm, self).__init__(*args, **kwargs)
		self.fields['cedula'].widget.attrs.update({'class':'form-control'})
		self.fields['nombre'].widget.attrs.update({'class':'form-control'})
		self.fields['apellido'].widget.attrs.update({'class':'form-control'})
		self.fields['puesto'].widget.attrs.update({'class':'form-control'})
		self.fields['tipo'].widget.attrs.update({'class':'form-control'})
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
		fields = ("cedula","nombre","apellido","puesto","password","tipo","unidad","foto","email")

class PersonaModificarForm(forms.ModelForm):
	def __init__(self,instance=None, *args, **kwargs):
		_fields = ('username','first_name','last_name','email')
		_initial = model_to_dict(instance.usuario, _fields) if instance is not None else {}
		super(PersonaModificarForm, self).__init__(initial=_initial,instance=instance,*args,**kwargs)
		self.fields.update(fields_for_model(User,_fields))
		self.fields['username'].widget.attrs.update({'class':'form-control'})
		self.fields['first_name'].widget.attrs.update({'class':'form-control'})
		self.fields['last_name'].widget.attrs.update({'class':'form-control'})
		self.fields['puesto'].widget.attrs.update({'class':'form-control'})
		self.fields['tipo'].widget.attrs.update({'class':'form-control'})
		self.fields['unidad'].widget.attrs.update({'class':'form-control'})
		self.fields['foto'].widget.attrs.update({'class':'form-control'})
		self.fields['email'].widget.attrs.update({'class':'form-control'})
	
	class Meta:
		model = Persona
		exclude = ("usuario",)

	def save(self, *args, **kwargs):
		u = self.instance.usuario
		u.first_name = self.cleaned_data['first_name']
		u.last_name = self.cleaned_data['last_name']
		u.email = self.cleaned_data['email']
		u.save()
		profile = super(PersonaModificarForm, self).save(*args, **kwargs)
		return profile

class PeriodoForm(forms.ModelForm):
	def __init__ (self, *args, **kwargs):
		super(PeriodoForm, self).__init__(*args, **kwargs)
		self.fields['anio_periodo'].widget.attrs.update({'class':'form-control'})
		self.fields['dias_fijo'].widget.attrs.update({'class':'form-control'})
		self.fields['dias_vac'].widget.attrs.update({'class':'form-control'})
		self.fields['horas_vac'].widget.attrs.update({'class':'form-control'})
		
	class Meta:
		model = Periodo
		fields = ("anio_periodo","dias_fijo","dias_vac","horas_vac","usuario")
    
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