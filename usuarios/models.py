from django.db import models

# Create your models here.
class Unidad(models.Model):
	idunidad = models.AutoField(primary_key=True)
	uni_nombre = models.CharField(max_length=75)
"""
class Persona(models.Model):
	pers_cedula = models.CharField(max_length=10, primary_key=True)
	pers_nombre = models.CharField(max_length=35)
	pers_apellido = models.CharField(max_length=35)
	pers_puesto = models.CharField(max_length=25)
	unidad = models.ForeignKey('Unidad')

class Usuario(models.Model): # settings.AUTH_USER_MODEL
	pers_cedula = models.OneToOneField('Persona', primary_key=True)
	usu_password = models.CharField(max_length=16)
	usu_estado = models.BooleanField()
	rol = models.ManyToManyField('Rol')

class Rol(models.Model):
	idrol = models.AutoField(primary_key=True)
	rol_nombre = models.CharField(max_length=25)

class PermisoRol(models.Model):
	idpermiso = models.AutoField(primary_key=True)
	prol_nombre = models.CharField(max_length=35)
	rol = models.ForeignKey('Rol')

"""