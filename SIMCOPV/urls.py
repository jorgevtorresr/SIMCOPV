"""SIMCOPV URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from usuarios.views import (UserViewSet, PersonaViewSet,
    TipoNotificacionViewSet, PeriodoViewSet, NotificacionViewSet)
from vacaciones.views import VacacionViewSet
from permisos.views import PermisoViewSet

router = routers.DefaultRouter()
router.register(r'persona', PersonaViewSet)
router.register(r'user', UserViewSet)
router.register(r'tiponotificacion', TipoNotificacionViewSet)
router.register(r'periodo', PeriodoViewSet)
router.register(r'notificacion', NotificacionViewSet)
router.register(r'vacacion', VacacionViewSet)
router.register(r'permiso', PermisoViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'usuarios.views.index', name='index'),
    url(r'^simcopv/$', 'usuarios.views.base', name='base'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    url(r'^config/$', 'usuarios.views.images', name='config'),
    url(r'^permiso/$', 'permisos.views.permiso', name='permiso'),
    url(r'^usuarios/agregarperiodo/$', 'usuarios.views.agregar_periodo', name='agregarperiodo'),
    url(r'^usuarios/agregarusuario/$', 'usuarios.views.agregar_usuario', name='agregarusuario'),
    url(r'^cuenta/login/$', 'usuarios.views.autenticacion', name='auth'),
    url(r'^cuenta/logout/$', 'usuarios.views.auth_logout', name='logout'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
]