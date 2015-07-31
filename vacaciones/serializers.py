from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Vacacion

class VacacionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Vacacion
		fields = ('url','ced_jefe_inmed','ced_jef_talent',
			'ced_gerente','fecha_inicio' ,'fecha_fin','estado',
			'periodo','usuario')