from django.db import models
from usuarios.models import Periodo
from django.contrib.auth.models import User

# Create your models here.
class Permiso(models.Model):
	ced_jefe_inmed = models.CharField(max_length=10, null=True, blank=True)
	ced_jef_talent = models.CharField(max_length=10, null=True, blank=True)
	ced_gerente = models.CharField(max_length=10, null=True, blank=True)
	fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
	fecha_fin = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
	descripcion = models.TextField()
	comprobante = models.ImageField(upload_to='comprobantes/%Y/%m/%d')
	estado = models.BooleanField(default=True)
	periodo = models.ForeignKey(Periodo)
	usuario = models.ForeignKey(User)