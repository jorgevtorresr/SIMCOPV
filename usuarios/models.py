from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Unidad(models.Model):
	idunidad = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=75)

class Persona(models.Model):
	puesto = models.CharField(max_length=25)
	unidad = models.ForeignKey('Unidad')
	usuario = models.OneToOneField(User)

class TipoNotificacion(models.Model):
	tipon_nombre = models.CharField(max_length=55)

class Notificacion(models.Model):
	descripcion = models.CharField(max_length=255)
	estado_visto = models.BooleanField()
	usuario = models.ForeignKey(User)
	tiponotif = models.ForeignKey('TipoNotificacion')

class Periodo(models.Model):
	anio_inicio = models.CharField(max_length=4)
	anio_fin = models.CharField(max_length=4)
	dias_vac = models.IntegerField()
	horas_vac = models.TimeField()
	usuario = models.ForeignKey(User)