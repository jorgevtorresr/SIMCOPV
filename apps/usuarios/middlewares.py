
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

class change_password(object):
	def process_request(self,request):
		idusuario = request.GET.get("username","")
		try:
			if idusuario != "":
				func = User.objects.get(username=idusuario)
				return HttpResponseRedirect(reverse("cambiarpassword",args=(func.id,)))
		except:
			print "io paso"
		return None