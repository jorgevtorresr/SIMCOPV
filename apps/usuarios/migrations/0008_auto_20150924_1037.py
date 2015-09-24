# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_persona_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='periodo',
            old_name='anio_fin',
            new_name='anio_periodo',
        ),
        migrations.RemoveField(
            model_name='periodo',
            name='anio_inicio',
        ),
        migrations.AddField(
            model_name='periodo',
            name='dias_fijo',
            field=models.IntegerField(default=30),
        ),
    ]
