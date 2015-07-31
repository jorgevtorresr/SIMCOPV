from django.shortcuts import render
from .models import Permiso
from .serializers import PermisoSerializer
from rest_framework import viewsets

# Create your views here.
class PermisoViewSet(viewsets.ModelViewSet):
	queryset = Permiso.objects.all()
	serializer_class = PermisoSerializer