# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20150730_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificacion',
            old_name='bot_descripcion',
            new_name='not_descripcion',
        ),
    ]
