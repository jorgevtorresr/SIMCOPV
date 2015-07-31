from rest_framework import serializers
from .models import Permiso
from django.contrib.auth.models import User

class PermisoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Permiso
		fields = ('url','ced_jefe_inmed','ced_jef_talent',
			'ced_gerente','fecha_inicio','fecha_fin','estado',
			'descripcion', 'comprobante', 'periodo','usuario')