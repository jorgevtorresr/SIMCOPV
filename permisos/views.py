from django.shortcuts import render
from .models import Permiso
from .serializers import PermisoSerializer
from rest_framework import viewsets
from permisos.forms import PermisoUsuarioForm
from django.contrib.auth.decorators import login_required

@login_required
def permiso(request):
	if request.method == "POST":
		pass
	else:
		form = PermisoUsuarioForm()
	return render(request, "permiso.html",{"form":form})

# Create your views here.
class PermisoViewSet(viewsets.ModelViewSet):
	queryset = Permiso.objects.all()
	serializer_class = PermisoSerializer