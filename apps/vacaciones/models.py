from django.db import models
from django.contrib.auth.models import User
from apps.usuarios.models import Periodo

# Create your models here.
class Vacacion(models.Model):
	ced_jefe_inmed = models.CharField(max_length=10, blank=True)
	ced_jef_talent = models.CharField(max_length=10, blank=True)
	ced_gerente = models.CharField(max_length=10, blank=True)
	fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
	fecha_fin = models.DateField(auto_now=False, auto_now_add=False)
	estado = models.BooleanField()
	periodo = models.ForeignKey(Periodo)
	usuario = models.ForeignKey(User)