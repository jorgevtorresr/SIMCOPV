#! python manage.py shell < script.py
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from apps.usuarios.models import Persona
user1 = User.objects.get(username="0705674216")
per = Persona.objects.get(usuario=user1)
per.delete()
user1.delete()
