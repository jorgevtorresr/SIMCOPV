# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType


class GlobalPermissionManager(models.Manager):
    def get_query_set(self):
        return super(GlobalPermissionManager, self).\
            get_query_set().filter(content_type__name='global_permission')

# Creation of Permission Model without a Model Object (content_type)
class GlobalPermission(Permission):
    """A global permission, not attached to a model"""

    objects = GlobalPermissionManager()

    class Meta:
        proxy = True
        verbose_name = "global_permission"


    def save(self, *args, **kwargs):
        ct, created = ContentType.objects.get_or_create(
            model=self._meta.verbose_name, app_label=self._meta.app_label,
        )
        self.content_type = ct
        super(GlobalPermission, self).save(*args)

class Unidad(models.Model):
	idunidad = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=75)

	def __unicode__(self):
		return self.nombre

class Persona(models.Model):
	puesto = models.CharField(max_length=25)
	unidad = models.ForeignKey('Unidad')
	TIPOS_DE_USUARIOS = (
		("LOSEP","LOSEP"),
		("Codigo de Trabajo","Codigo de Trabajo"),
	)
	tipo = models.CharField(default="LOSEP",choices=TIPOS_DE_USUARIOS, max_length=50)
	foto = models.ImageField(upload_to="profile-pics/", default='profile-pics/image-default.png',blank=True, null=True)
	usuario = models.OneToOneField(User)
	
	def __unicode__(self):
		return self.usuario.username

class TipoNotificacion(models.Model):
	tipon_nombre = models.CharField(max_length=55)

class Notificacion(models.Model):
	descripcion = models.CharField(max_length=255)
	estado_visto = models.BooleanField()
	usuario = models.ForeignKey(User)
	tiponotif = models.ForeignKey('TipoNotificacion')

class Periodo(models.Model):
	anio_periodo = models.CharField(max_length=4)
	dias_fijo = models.IntegerField(default=30)
	dias_vac = models.IntegerField()
	horas_vac = models.TimeField()
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return "{0}-{1}".format(self.anio_periodo,self.usuario.username)