# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_globalpermission'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='tipo',
            field=models.CharField(default=b'LOSEP', max_length=50, choices=[(b'LOSEP', b'LOSEP'), (b'Codigo de Trabajo', b'Codigo de Trabajo')]),
        ),
    ]
