from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^permiso/$', 'apps.permisos.views.permiso', name='permiso'),
    url(r'^validar/$', 'apps.permisos.views.validarpermisos', name='validar'),
    url(r'^RRHH/validar/permiso/(\d+)/$', 'apps.permisos.views.validarpermisoRRHH', name='validarpermRRHH'),
    url(r'^validar/permiso/(\d+)/$', 'apps.permisos.views.validarpermiso', name='validarperm'),
)