from django.shortcuts import render
from .models import Vacacion
from .serializers import VacacionSerializer
from rest_framework import viewsets

# Create your views here.
class VacacionViewSet(viewsets.ModelViewSet):
	queryset = Vacacion.objects.all()
	serializer_class = VacacionSerializer