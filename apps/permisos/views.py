#! python2
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets
from .forms import PermisoUsuarioForm
from .models import Permiso
from .serializers import PermisoSerializer

@login_required
def permiso(request):
	if request.method == "POST":
		fecha_inicio = request.POST.get('fecha_inicio','')
		hora_inicio = request.POST.get('hora_inicio','')
		fecha_fin = request.POST.get('fecha_fin','')
		hora_fin = request.POST.get('hora_fin','')
		descripcion = request.POST.get('descripcion','')
		# I have to obligatorily make server validation		
		return HttpResponseRedirect(reverse("permiso"))
	return render(request, "permisos/permiso.html",{})

# Create your views here.
class PermisoViewSet(viewsets.ModelViewSet):
	queryset = Permiso.objects.all()
	serializer_class = PermisoSerializer