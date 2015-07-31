# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0002_auto_20150730_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ced_jefe_inmed', models.CharField(max_length=10, blank=True)),
                ('ced_jef_talent', models.CharField(max_length=10, blank=True)),
                ('ced_gerente', models.CharField(max_length=10, blank=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(null=True)),
                ('descripcion', models.TextField()),
                ('comprobante', models.ImageField(upload_to=b'comprobantes/%Y/%m/%d')),
                ('estado', models.BooleanField()),
                ('periodo', models.ForeignKey(to='usuarios.Periodo')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
