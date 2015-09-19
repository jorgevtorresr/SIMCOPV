# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('permisos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='ced_gerente',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='permiso',
            name='ced_jef_talent',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='permiso',
            name='ced_jefe_inmed',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='permiso',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
