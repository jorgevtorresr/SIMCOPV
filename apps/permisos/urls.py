from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^solicitarpermiso/$', 'apps.permisos.views.permiso', name='permiso'),
    url(r'^verpermisos/$', 'apps.permisos.views.vermispermisos', name='verpermisos'),
    url(r'^validar/$', 'apps.permisos.views.validarpermisos', name='validar'),
    url(r'^validar/permiso/(\d+)/$', 'apps.permisos.views.validarpermiso', name='validarperm'),
    url(r'^Gerencia/validar/$', 'apps.permisos.views.validarpermisosGeren', name='validarGerencia'),
    url(r'^Gerencia/validar/permiso/(\d+)$', 'apps.permisos.views.validarpermisoGeren', name='validarpermGeren'),
    url(r'^RRHH/validar/$', 'apps.permisos.views.validarpermisosRRHH', name='validarRRHH'),
    url(r'^RRHH/validar/permiso/(\d+)/$', 'apps.permisos.views.validarpermisoRRHH', name='validarpermRRHH'),
)