#! python2
# -*- coding: utf-8 -*-
from apps.usuarios.models import Periodo
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Max
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
		date_inicio = datetime.strptime(fecha_inicio+hora_inicio,'%Y-%m-%d%H:%M')
		date_fin = datetime.strptime(fecha_fin+hora_fin,'%Y-%m-%d%H:%M')
		# Take the next year to compare date and control the overflow
		date_after = datetime.strptime("{0}-01-01".format(datetime.now().year+1),'%Y-%m-%d')
		if date_fin < date_inicio:
			messages.error(request,"Las fechas no son consistentes")
		elif fecha_inicio == fecha_fin and date_inicio.time() > date_fin.time():
			messages.error(request,"Las horas no son consistentes")
		elif date_inicio < datetime.now() or date_fin < datetime.now():
			messages.error(request,"Las fechas no pueden ser menores al día en curso")
		elif date_inicio > date_after or date_fin > date_after:
			messages.error(request,"Las fechas no deben sobrepasar el año en curso")
		elif fecha_inicio == "" or fecha_fin == "":
			messages.error(request,"Ingrese la fecha de inicio y la de fin")
		elif hora_inicio == "" or hora_fin == "" or descripcion == "":
			messages.error(request,"Ingrese los datos completos")
		else:
			# Here comes the truth
			periodos = Periodo.objects.filter(usuario=request.user)
			max = periodos.aggregate(max=Max('anio_periodo'))
			periodomax = []
			if periodos == []:
				messages.error(request,"Usted no tiene permisos asignados.. Por favor contacte con el departamento de RRHH")
			else:
				try:
					periodomax = periodos.get(anio_periodo=max["max"])
				except:
					pass
				if periodomax == []:
					pass
				else:
					# Sending dates without timezone
					permiso = Permiso(fecha_inicio=date_inicio,fecha_fin=date_fin,descripcion=descripcion,usuario=request.user,periodo=periodomax)
					permiso.save()
					messages.success(request,"Permiso ingresado correctamente")
		return HttpResponseRedirect(reverse("permiso"))	
	return render(request, "permisos/permiso.html",{})

@login_required
def validarpermisos(request):
	""" Metodo usado por los jefes de unidad, gerente y encargados
		para validar los permisos ingresados por los usuarios"""
	return render(request,"permisos/validarpermisos.html",{})

# Create your views here.
class PermisoViewSet(viewsets.ModelViewSet):
	queryset = Permiso.objects.all()
	serializer_class = PermisoSerializer 