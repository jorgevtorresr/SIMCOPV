# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('permisos', '0004_permiso_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permiso',
            name='tipo',
            field=models.CharField(default=b'', max_length=12, null=True, blank=True, choices=[(b'', b''), (b'Imputable', b'Imputable'), (b'No Imputable', b'No Imputable')]),
        ),
    ]
