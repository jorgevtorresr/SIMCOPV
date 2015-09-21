from django.forms import ModelForm, DateInput
from .models import Permiso

class DateInput(DateInput):
	input_type = 'date'

class PermisoUsuarioForm(ModelForm):
	def __init__(self,*args, **kwargs):
		super(PermisoUsuarioForm, self).__init__(*args, **kwargs)
		self.fields['fecha_inicio'].widget.attrs.update({'class':'form-control'})
		self.fields['fecha_fin'].widget.attrs.update({'class':'form-control'})
		self.fields['descripcion'].widget.attrs.update({'class':'form-control'})

	class Meta:
		model = Permiso
		exclude = ["ced_jefe_inmed","ced_jef_talent","ced_gerente","comprobante","estado","tipo","periodo","usuario"]
		widgets = {'fecha_inicio':DateInput(),
					'fecha_fin':DateInput()}