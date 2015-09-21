from django.db import models
from django.contrib.auth.models import User
from apps.usuarios.models import Periodo

# Create your models here.
class Permiso(models.Model):
	TIPOS = (
		("",""),
		("Imputable","Imputable"),
		("No Imputable","No Imputable"),
		)
	ced_jefe_inmed = models.CharField(max_length=10, null=True, blank=True)
	ced_jef_talent = models.CharField(max_length=10, null=True, blank=True)
	ced_gerente = models.CharField(max_length=10, null=True, blank=True)
	fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
	fecha_fin = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
	descripcion = models.TextField()
	comprobante = models.ImageField(upload_to='comprobantes/%Y/%m/%d')
	estado = models.BooleanField(default=True)
	tipo = models.CharField(choices=TIPOS, max_length=12,default="",null=True,blank=True)
	periodo = models.ForeignKey(Periodo)
	usuario = models.ForeignKey(User)