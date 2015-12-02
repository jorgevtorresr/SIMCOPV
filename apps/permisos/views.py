#! python2
# -*- coding: utf-8 -*-
from datetime import datetime
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
		date_inicio = datetime.strptime(fecha_inicio,'%Y-%m-%d')
		date_fin = datetime.strptime(fecha_fin,'%Y-%m-%d')
		# Take the next year to compare date and control the overflow
		date_after = datetime.strptime("{0}-01-01".format(datetime.now().year),'%Y-%m-%d')
		if date_fin < date_inicio:
			pass
		elif fecha_inicio == fecha_fin:
			pass
		elif date_inicio < datetime.now() || date_inicio < datetime.now():
			pass
		elif date_inicio > date_after || date_fin > date_after:
			pass
		elif fecha_inicio == "" || fecha_fin == "":
			pass
		elif hora_inicio == "" or hora_fin == "" or descripcion == "":
			pass
		else:
			pass # Here comes the truth
		return HttpResponseRedirect(reverse("permiso"))	
	return render(request, "permisos/permiso.html",{})

# Create your views here.
class PermisoViewSet(viewsets.ModelViewSet):
	queryset = Permiso.objects.all()
	serializer_class = PermisoSerializer 