#! python2
# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PersonaForm, LoginForm
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from .models import Persona, TipoNotificacion, Periodo, Notificacion
from .serializers import (UserSerializer, PersonaSerializer, TipoNotificacionSerializer, 
	NotificacionSerializer, PeriodoSerializer)
from rest_framework import viewsets
from django.contrib.auth.models import User
from permisos.forms import PermisoUsuarioForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
	usuario = request.user
	return render_to_response('index.html',{"usuario":usuario})

def base(request):
	usuario = request.user
	return render_to_response('base.html', {"usuario":usuario})

def config(request):
	if request.method == "POST":
		pass
	else:
		form = PermisoUsuarioForm()
	return render(request, "configuracion.html",{"form":form})

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
