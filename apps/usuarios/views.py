#! python2
# -*- coding: utf-8 -*-
import os
import json
from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import default_storage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.template import Context
from rest_framework import viewsets
from .models import Persona, TipoNotificacion, Periodo, Notificacion, Unidad
from .forms import PersonaForm, LoginForm, UnidadForm, FrontImages
from .serializers import (UserSerializer, PersonaSerializer, TipoNotificacionSerializer, 
	NotificacionSerializer, PeriodoSerializer)

# Create your views here.
def index(request):
	images = []
	with open("{0}/frontimages.json".format(settings.MEDIA_ROOT)) as json_data:
		d = json.load(json_data)
		for image in d.values():
			images.append("{0}frontimages/".format(settings.MEDIA_URL)+image)
	usuario = request.user
	return render_to_response('index.html',{"usuario":usuario,"images":images})

def base(request):
	usuario = request.user
	if usuario.check_password(usuario.username):
		return HttpResponseRedirect("/usuarios/cuenta/change_password/")
	return render(request,'base.html',{})

def agregar_usuario(request):
	if request.method == "POST":
		if request.POST.get("unidad","") == "unidad":
			form = PersonaForm()
			form_unidad = UnidadForm(request.POST)
			if form_unidad.is_valid():
				form_unidad.save()
				men = "Unidad Agregada Correctamente!"
				return render(request, 'usuarios/agregarusuario.html',{"form":form,"form_unidad":form_unidad,"men":men})
		else:
			form = PersonaForm(request.POST, request.FILES)
			form_unidad = UnidadForm()
			if form.is_valid():
				cedula = form.cleaned_data["cedula"]
				nombre = form.cleaned_data["nombre"]
				apellido = form.cleaned_data["apellido"]
				email = form.cleaned_data["email"]
				password = form.cleaned_data["password"]
				unidad = form.cleaned_data["unidad"]
				puesto = form.cleaned_data["puesto"]
				foto = form.cleaned_data["foto"]
				if verificar(cedula):
					existe = True
					try:
						user1 = User.objects.get(username=cedula)	
					except: 
						existe = False
					if existe:
						messages.warning(request, "Cedula ya en uso");
					else:
						usuario = User.objects.create_user(username=cedula, first_name=nombre, last_name=apellido, email=email,password=password)
						if usuario != None:
							persona = Persona(usuario = usuario,puesto = puesto,unidad = unidad, foto=foto)
							persona.save()
							messages.add_message(request, messages.SUCCESS, "Usuario Creado Satisfactoriamente")
						else: 
							messages.error(request, "Error al Insertar Usuario!")
				else:
					messages.error(request, "Cedula Invalida!")
				return HttpResponseRedirect("")
	else:
		form = PersonaForm()
		form_unidad = UnidadForm()
	return render(request, 'usuarios/agregarusuario.html',{"form":form,"form_unidad":form_unidad})

def agregar_periodo(request):	
	return render(request, "usuarios/agregarperiodo.html",{})

def change_password(request):
	return render(request,"usuarios/change-password.html",{})

def images(request):
	if request.method == "POST":
		form = FrontImages(request.POST, request.FILES)
		image1 = request.FILES.get("imagen1","")
		image2 = request.FILES.get("imagen2","")
		image3 = request.FILES.get("imagen3","")
		image4 = request.FILES.get("imagen4","")
		if image1 == "" or image2 == "" or image3 == "" or image4 == "":
			men = "Suba todas las imagenes"
			return render(request, "usuarios/configuracion.html",{"form":form,"men":men})
		else:
			a = existe(image1)
			b = existe(image2)
			c = existe(image3)
			d = existe(image4)
			if a or b or c or d:
				men = "Imagen ya existe"
				return render(request, "usuarios/configuracion.html",{"form":form,"men":men})
			else:
				handle_uploaded_file(image1)
				handle_uploaded_file(image2)
				handle_uploaded_file(image3)
				handle_uploaded_file(image4)
				dic = {"imagen":image1._get_name(), "image2":image2._get_name(), "image3":image3._get_name(),"image4":image4._get_name()}
				jsonob = json.dumps(dic)
				save_json(jsonob)
				success = "Imagenes Actualizadas Correctamente"
				return render(request, "usuarios/configuracion.html",{"form":form,"success":success})
	else:
		form = FrontImages()
	return render(request,"usuarios/configuracion.html",{"form":form})


def handle_uploaded_file(f):
	"""Recibe una imagen(archivo) y la guarda en la carpeta 'media/frontimages' """
	filename = f._get_name()
	ruta = '{0}/{1}'.format(settings.MEDIA_ROOT,'frontimages/{0}'.format(filename))
	with open(ruta,'wb+') as fd:
		for chunk in f.chunks():
			fd.write(chunk)

def save_json(jsonob):
	with open('{0}/frontimages.json'.format(settings.MEDIA_ROOT), 'wb+') as destination:
		destination.write(jsonob)

def existe(f):
	filename = f._get_name()
	ruta = '{0}/{1}'.format(settings.MEDIA_ROOT,'frontimages/{0}'.format(filename))
	return os.path.exists(ruta)

def auth_logout(request):
	logout(request)
	return HttpResponseRedirect("/")

def autenticacion(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['usuario']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					next = request.GET.get("next","")
					if next != "":
						return HttpResponseRedirect(next)
					else:
						return HttpResponseRedirect("/usuarios/simcopv/")
				else:
					mensaje = "El usuario no esta actualmente activo"
					return render(request, "login.html",{"men":mensaje,"form":form})
			else:
				mensaje = "La combinación de Usuario y Contraseña es Incorrecta"
				return render(request, "login.html",{"men":mensaje,"form":form})
	else:
		form = LoginForm()
	return render(request, "login.html",{'form':form})
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class PersonaViewSet(viewsets.ModelViewSet):
	queryset = Persona.objects.all()
	serializer_class = PersonaSerializer

class TipoNotificacionViewSet(viewsets.ModelViewSet):
	queryset = TipoNotificacion.objects.all()
	serializer_class = TipoNotificacionSerializer

class NotificacionViewSet(viewsets.ModelViewSet):
	queryset = Notificacion.objects.all()
	serializer_class = NotificacionSerializer

class PeriodoViewSet(viewsets.ModelViewSet):
	queryset = Periodo.objects.all()
	serializer_class = PeriodoSerializer

def verificar(nro):
    l = len(nro)
    if l == 10 or l == 13: # verificar la longitud correcta
        cp = int(nro[0:2])
        if cp >= 1 and cp <= 22: # verificar codigo de provincia
            tercer_dig = int(nro[2])
            if tercer_dig >= 0 and tercer_dig < 6 : # numeros enter 0 y 6
                if l == 10:
                    return __validar_ced_ruc(nro,0)                       
                elif l == 13:
                    return __validar_ced_ruc(nro,0) and nro[10:13] != '000' # se verifica q los ultimos numeros no sean 000
            elif tercer_dig == 6:
                return __validar_ced_ruc(nro,1) # sociedades publicas
            elif tercer_dig == 9: # si es ruc
                return __validar_ced_ruc(nro,2) # sociedades privadas
            else:
                #raise Exception(u'Tercer digito invalido') 
                return False
        else:
            #raise Exception(u'Codigo de provincia incorrecto') 
            return False
    else:
        #raise Exception(u'Longitud incorrecta del numero ingresado')
        return False

def __validar_ced_ruc(nro,tipo):
    total = 0
    if tipo == 0: # cedula y r.u.c persona natural
        base = 10
        d_ver = int(nro[9])# digito verificador
        multip = (2, 1, 2, 1, 2, 1, 2, 1, 2)
    elif tipo == 1: # r.u.c. publicos
        base = 11
        d_ver = int(nro[8])
        multip = (3, 2, 7, 6, 5, 4, 3, 2 )
    elif tipo == 2: # r.u.c. juridicos y extranjeros sin cedula
        base = 11
        d_ver = int(nro[9])
        multip = (4, 3, 2, 7, 6, 5, 4, 3, 2)
    for i in range(0,len(multip)):
        p = int(nro[i]) * multip[i]
        if tipo == 0:
            total+=p if p < 10 else int(str(p)[0])+int(str(p)[1])
        else:
            total+=p
    mod = total % base
    val = base - mod if mod != 0 else 0
    return val == d_ver
