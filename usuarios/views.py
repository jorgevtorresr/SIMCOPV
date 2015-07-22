from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from datetime import datetime

# Create your views here.
def hola(request):
	return HttpResponse("Hola")

def hora_actual(request):
	ahora = datetime.now()
	#t = get_template('grid.html')
	#c = Context({'hora':ahora})
	#html = t.render(c)
	return render_to_response('grid.html', {'hora':ahora, 'lista':range(4)})

def post(request, num):
	return HttpResponse("Este es el post %i" % int(num))