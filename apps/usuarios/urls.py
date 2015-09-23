from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^simcopv/$', 'apps.usuarios.views.base', name='base'),
    url(r'^config/$', 'apps.usuarios.views.images', name='config'),
    url(r'^registrar/agregarperiodo/$', 'apps.usuarios.views.agregar_periodo', name='agregarperiodo'),
    url(r'^registrar/asignar-roles/$', 'apps.usuarios.views.asignar_roles', name='asignarroles'),
    url(r'^registrar/agregarusuario/$', 'apps.usuarios.views.agregar_usuario', name='agregarusuario'),
    url(r'^cuenta/login/$', 'apps.usuarios.views.autenticacion', name='auth'),
    url(r'^cuenta/logout/$', 'apps.usuarios.views.auth_logout', name='logout'),
    url(r'^cuenta/change_password/$', 'apps.usuarios.views.change_password', name='change_password'),
    url(r'^registrar/asignar-roles/usuario-search/$', 'apps.usuarios.views.ajax_usuario_search', name='usuario_search'),
    url(r'^registrar/asignar-roles/grupo/(\d+)/$', 'apps.usuarios.views.ajax_table_usuarios', name="tabla_grupo"),
)