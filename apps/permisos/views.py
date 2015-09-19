from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .forms import PermisoUsuarioForm
from .models import Permiso
from .serializers import PermisoSerializer

@login_required
def permiso(request):
	if request.method == "POST":
		form = PermisoUsuarioForm(request.POST)
		if form.is_valid():
			fecha_inicio = form.cleaned_data['fecha_inicio']
			fecha_fin = form.cleaned_data['fecha_fin']
			descripcion = form.cleaned_data['descripcion']
			return render(request, "permiso.html",{"form":form})
	else:
		form = PermisoUsuarioForm()
	return render(request, "permisos/permiso.html",{"form":form})

# Create your views here.
class PermisoViewSet(viewsets.ModelViewSet):
	queryset = Permiso.objects.all()
	serializer_class = PermisoSerializer