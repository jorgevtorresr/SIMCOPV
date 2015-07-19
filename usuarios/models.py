from django.db import models

# Create your models here.
"""class Persona(models.Model):
	pers_cedula = models.CharField(max_length=10, primary_key=True)"""
class Institucion(models.Model):
	inst_nombre = models.CharField(max_length=75)
	inst_direccion = models.CharField(max_length=100)
	inst_telefono = models.CharField(max_length=15)	

class Unidad(models.Model):
	idunidad = models.AutoField(primary_key=True)
	uni_nombre = models.CharField(max_length=75)