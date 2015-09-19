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
from apps.usuarios.views import (UserViewSet, PersonaViewSet,
    TipoNotificacionViewSet, PeriodoViewSet, NotificacionViewSet)
from apps.vacaciones.views import VacacionViewSet
from apps.permisos.views import PermisoViewSet

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
    url(r'^$', 'apps.usuarios.views.index', name='index'),
    url(r'^usuarios/', include('apps.usuarios.urls')),
    url(r'^permisos/', include('apps.permisos.urls')),
    url(r'^vacaciones/', include('apps.vacaciones.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
]