from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from .models import Persona, TipoNotificacion, Periodo, Notificacion
from .serializers import (UserSerializer, PersonaSerializer, TipoNotificacionSerializer, 
	NotificacionSerializer, PeriodoSerializer)
from rest_framework import viewsets
from django.contrib.auth.models import User

# Create your views here.
def hola(request):
	return HttpResponse("Hola")

def hora_actual(request):
	ahora = datetime.now()
	#t = get_template('grid.html')
	#c = Context({'hora':ahora})
	#html = t.render(c)
	return render_to_response('grid.html', {'hora':ahora, 'lista':range(4)})

def bootstrap(request):
	a = 1
	b = 2
	suma = a + b
	return render_to_response('grid.html',{'sumita':suma})

def nuevo(request):
	name = "Jorge"
	return render_to_response('hola.html',{"toto":name})

def post(request, num):
	return HttpResponse("Este es el post %i" % int(num))

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
