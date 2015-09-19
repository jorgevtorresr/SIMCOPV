# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('permisos', '0002_auto_20150914_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='fecha_fin',
            field=models.DateField(null=True, blank=True),
        ),
    ]
