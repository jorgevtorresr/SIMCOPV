# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('usuarios', '0005_persona_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalPermission',
            fields=[
            ],
            options={
                'verbose_name': 'global_permission',
                'proxy': True,
            },
            bases=('auth.permission',),
        ),
    ]
