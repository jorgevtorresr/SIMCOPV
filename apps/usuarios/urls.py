from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^simcopv/$', 'apps.usuarios.views.base', name='base'),
    url(r'^config/$', 'apps.usuarios.views.images', name='config'),
    url(r'^periodos/agregarperiodo/$', 'apps.usuarios.views.agregar_periodo', name='agregarperiodo'),
    url(r'^periodos/agregarperiodoporusuario/$', 'apps.usuarios.views.agregar_periodoporusuario', name='agregarperiodoporusuario'),
    url(r'^usuarios/agregarusuario/$', 'apps.usuarios.views.agregar_usuario', name='agregarusuario'),
    url(r'^usuarios/verusuarios/$', 'apps.usuarios.views.ver_usuarios', name='verusuarios'),
    url(r'^roles/asignar-roles/$', 'apps.usuarios.views.asignar_roles', name='asignarroles'),
    url(r'^cuenta/login/$', 'apps.usuarios.views.autenticacion', name='auth'),
    url(r'^cuenta/logout/$', 'apps.usuarios.views.auth_logout', name='logout'),
    url(r'^cuenta/change_password/$', 'apps.usuarios.views.change_password', name='change_password'),
    url(r'^ajax/asignar-roles/usuario-search/$', 'apps.usuarios.views.ajax_usuario_search', name='usuario_search'),
    url(r'^ajax/asignar-roles/grupo/(\d+)/$', 'apps.usuarios.views.ajax_table_usuarios', name="tabla_grupo"),
    url(r'^ajax/asignar-roles/usuarios-por-tipo/$', 'apps.usuarios.views.ajax_tabla_agregarperiodo', name="tabla_tipo"),
    url(r'^ajax/asignar-roles/usuarios-por-periodo/$','apps.usuarios.views.ajax_usuarios_periodo', name="tabla_usuarios_periodo"),
)