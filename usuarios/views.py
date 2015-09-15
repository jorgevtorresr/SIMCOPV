from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PersonaForm
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from .models import Persona, TipoNotificacion, Periodo, Notificacion
from .serializers import (UserSerializer, PersonaSerializer, TipoNotificacionSerializer, 
	NotificacionSerializer, PeriodoSerializer)
from rest_framework import viewsets
from django.contrib.auth.models import User
from permisos.forms import PermisoUsuarioForm

# Create your views here.
def index(request):
	return render_to_response('index.html',{})

def base(request):
	return render_to_response('base.html', {})

def config(request):
	if request.method == "POST":
		pass
	else:
		form = PermisoUsuarioForm()
	return render(request, "configuracion.html",{"form":form})

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
