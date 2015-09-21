# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('permisos', '0003_auto_20150917_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='permiso',
            name='tipo',
            field=models.CharField(default=b'Imputable', max_length=12, choices=[(b'', b''), (b'Imputable', b'Imputable'), (b'No Imputable', b'No Imputable')]),
        ),
    ]
