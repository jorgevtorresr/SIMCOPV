from django.forms import ModelForm, DateTimeInput
from .models import Permiso

class DateTimeInput(DateTimeInput):
	input_type = 'datetime'
	format_key = 'DATE_INPUT_FORMATS'

class PermisoUsuarioForm(ModelForm):
	def __init__(self,*args, **kwargs):
		super(PermisoUsuarioForm, self).__init__(*args, **kwargs)
		self.fields['fecha_inicio'].widget.attrs.update({'class':'form-control'})
		self.fields['fecha_fin'].widget.attrs.update({'class':'form-control'})
		self.fields['descripcion'].widget.attrs.update({'class':'form-control'})

	class Meta:
		model = Permiso
		exclude = ["ced_jefe_inmed","ced_jef_talent","ced_gerente","comprobante","estado","tipo","periodo","usuario"]
		widgets = {'fecha_inicio':DateTimeInput(),
					'fecha_fin':DateTimeInput()}

class PermisoValForm(ModelForm):
	def __init__(self,*args,**kwargs):
		super(PermisoValForm,self).__init__(*args, **kwargs)
		self.fields['fecha_inicio'].widget.attrs.update({'class':'form-control'})
		self.fields['fecha_fin'].widget.attrs.update({'class':'form-control'})
		self.fields['descripcion'].widget.attrs.update({'class':'form-control'})

	class Meta:
		model = Permiso
		exclude = ("ced_jef_talent","ced_gerente","ced_jefe_inmed","comprobante","estado")