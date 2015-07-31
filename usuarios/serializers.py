from rest_framework import serializers
from .models import (Unidad, Persona, 
TipoNotificacion, Notificacion, Periodo)
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model =  User
		fields = ('url','username','email','first_name','last_name',)

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Persona
		fields = ('per_puesto', 'unidad', 'usuario',)

class TipoNotificacionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = TipoNotificacion
		fields = ('tipon_nombre',)

class NotificacionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Notificacion
		fields = ('not_descripcion','not_estado_visto','usuario','tiponotif',)

class PeriodoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Periodo
		fields = ('peri_anio_inicio','peri_anio_fin','peri_dias_vac','peri_horas_vac','usuario',)