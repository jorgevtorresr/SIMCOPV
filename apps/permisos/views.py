#! python2
# -*- coding: utf-8 -*-
from apps.usuarios.models import Periodo
from apps import group_required
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
	return render(request, "permisos/solicitarpermiso.html",{})

@login_required
@group_required("Jefes Inmediatos","Jefe de Talento Humano y Encargados","Gerente y Encargados")
def validarpermisos(request):
	""" Metodo usado por los jefes de unidad, gerente y encargados
		para validar los permisos ingresados por los usuarios"""
	user = request.user
	permisos = []
	try:
		permisos = Permiso.objects.filter(usuario__persona__unidad=user.persona.unidad,estado=True,ced_jefe_inmed="")
	except:
		pass # If user has no a Group, It don't work
	return render(request,"permisos/validarpermisos.html",{"permisos":permisos})

# Validar permiso para Jefes de Unidad
@login_required
@group_required("Jefes Inmediatos","Jefe de Talento Humano y Encargados","Gerente y Encargados")
def validarpermiso(request,id):
	""" Metodo para validar los permisos usado por el jefe de unidad 
	y encargados """
	permiso = []
	try:
		permiso = Permiso.objects.get(id=id) 
		permiso = [] if permiso.ced_jefe_inmed != "" else permiso
		if request.method == "POST":
			mode = request.POST.get("mode");
			if mode == "rechazar":
				permiso.delete()
			elif mode == "validar":
				permiso.ced_jefe_inmed = request.user.username
				permiso.save()
			else:
				pass
			return HttpResponseRedirect(reverse('validar'))
	except:
		pass # Si el permiso con ese id no existe, se controla desde el template para poner un 404
	return render(request,"permisos/validarpermiso.html",{"permiso":permiso})

@login_required
@group_required("Jefe de Talento Humano y Encargados")
def validarpermisosRRHH(request):
	""" Metodo usado por el jefe de RRHH para ver el listado de 
	permisos para validarlos, previa validación por parte de los jefes inmediatos """
	user = request.user 
	permisos = []
	try: 
		user.groups.get(name="Jefe de Talento Humano y Encargados")
		permisos = Permiso.objects.filter(estado=True,ced_jef_talent="").exclude(ced_jefe_inmed="",ced_gerente="")
	except:
		pass
	return render(request,"permisos/validarpermisos.html",{"permisos":permisos,"RRHH":True,"user":user})

# Validar permiso para Jefe Recursos Humanos y Encargados
@login_required
@group_required("Jefe de Talento Humano y Encargados")
def validarpermisoRRHH(request,id):
	""" Metodo para validar los permisos usado por el jefe de RRHH 
	y encargados, este metodo valida un solo permiso en particular """
	permiso = []
	try:
		permiso = Permiso.objects.get(id=id)
		permiso = [] if permiso.ced_jef_talent != "" else permiso
		if request.method == "POST":
			mode = request.POST.get("mode","")
			if mode == "rechazar":
				permiso.delete();
			elif mode == "validar":
				comprobante = request.POST.get("comprobante","off")
				if comprobante == "on":
					permiso.ced_jef_talent = request.user.username
					permiso.save()
				else:
					permiso.ced_jef_talent = request.user.username
					permiso.estado = False
					permiso.save()
			else:
				pass
			return HttpResponseRedirect(reverse('validarRRHH'))
	except:
		pass # Si el permiso con ese id no existe, se controla desde el template para poner un 404
	return render(request,"permisos/validarpermisoRRHH.html",{"permiso":permiso})


@login_required
@group_required("Gerente y Encargados")
def validarpermisosGeren(request):
	""" Metodo usado por los Gerente y encargados
		para validar los permisos ingresados por los usuarios"""
	user = request.user
	permisos = []
	try:
		# I Dont Know SHOULD WAIT
		permisos = Permiso.objects.filter(estado=True,ced_gerente="").exclude()
	except:
		pass # If user has no a Group, It don't work
	return render(request,"permisos/validarpermisos",{"permisos":"","Geren":True})

# Validar permiso para Gerente y Encargados
@login_required
@group_required("Gerente y Encargados")
def validarpermisoGeren(request,id):
	return render(request,"permisos/validarpermisoGeren.html",{"permiso":permiso})

@login_required
def vermispermisos(request):
	""" Metodo que permite a los peticionarios ver los permisos y el estado de los mismos"""
	permisos = Permiso.objects.filter(usuario=request.user)
	activos = permisos.filter(estado=True)
	historicos = permisos.filter(estado=False)
	return render(request,"permisos/verpermisos.html",{"activos":activos,"historicos":historicos})

# Create your views here.
class PermisoViewSet(viewsets.ModelViewSet):
	queryset = Permiso.objects.all()
	serializer_class = PermisoSerializer 