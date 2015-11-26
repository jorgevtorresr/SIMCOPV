# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('permisos', '0005_auto_20150921_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='fecha_fin',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='permiso',
            name='fecha_inicio',
            field=models.DateTimeField(),
        ),
    ]
