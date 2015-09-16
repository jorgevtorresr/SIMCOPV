# -*- coding: utf-8 -*-
def user(request):
	usuario = request.user
	return dict(
		usuario = usuario
	)