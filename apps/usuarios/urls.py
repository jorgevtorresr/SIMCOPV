from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^simcopv/$', 'apps.usuarios.views.base', name='base'),
    url(r'^config/$', 'apps.usuarios.views.images', name='config'),
    url(r'^registrar/agregarperiodo/$', 'apps.usuarios.views.agregar_periodo', name='agregarperiodo'),
    url(r'^registrar/agregarusuario/$', 'apps.usuarios.views.agregar_usuario', name='agregarusuario'),
    url(r'^cuenta/login/$', 'apps.usuarios.views.autenticacion', name='auth'),
    url(r'^cuenta/logout/$', 'apps.usuarios.views.auth_logout', name='logout'),
)
