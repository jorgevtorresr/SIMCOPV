#! python2
# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PersonaForm, LoginForm, UnidadForm
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from datetime import datetime
from .models import Persona, TipoNotificacion, Periodo, Notificacion
from .serializers import (UserSerializer, PersonaSerializer, TipoNotificacionSerializer, 
	NotificacionSerializer, PeriodoSerializer)
from rest_framework import viewsets
from django.contrib.auth.models import User
from permisos.forms import PermisoUsuarioForm
from usuarios.forms import PersonaForm
from django.contrib.auth import authenticate, login, logout
import json
from .forms import FrontImages
from django.core.files.storage import default_storage
import os

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
	return render_to_response('base.html', {"usuario":usuario})

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
			form = PersonaForm(request.POST)
			form_unidad = UnidadForm()
			if form.is_valid():
				cedula = form.cleaned_data["cedula"]
				nombre = form.cleaned_data["nombre"]
				apellido = form.cleaned_data["apellido"]
				email = form.cleaned_data["email"]
				usuario = User.objects.create_user(username=cedula, first_name=nombre, last_name=apellido, email=email)
				men  = "Crear esto es horrible!"
				return render(request, 'usuarios/agregarusuario.html',{"form":form,"form_unidad":form_unidad,"men":men})
	else:
		form = PersonaForm()
		form_unidad = UnidadForm()
	return render(request, 'usuarios/agregarusuario.html',{"form":form,"form_unidad":form_unidad})

def agregar_periodo(request):	
	return render(request, "usuarios/agregarperiodo.html",{})

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
						return HttpResponseRedirect("/simcopv/")
				else:
					mensaje = "El usuario no esta actualmente activo"
					return render(request, "login.html",{"men":mensaje,"form":form})
			else:
				mensaje = "La combinación de Usuario y Contraseña es Incorrecta"
				return render(request, "login.html",{"men":mensaje,"form":form})
	else:
		form = LoginForm()
	return render(request, "login.html",{'form':form})

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

def existe(f):
	filename = f._get_name()
	ruta = '{0}/{1}'.format(settings.MEDIA_ROOT,'frontimages/{0}'.format(filename))
	return os.path.exists(ruta)

def save_json(jsonob):
	with open('{0}/frontimages.json'.format(settings.MEDIA_ROOT), 'wb+') as destination:
		destination.write(jsonob)

def auth_logout(request):
	logout(request)
	return HttpResponseRedirect("/")

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
