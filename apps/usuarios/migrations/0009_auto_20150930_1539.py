# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_auto_20150924_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodo',
            name='dias_vac',
            field=models.IntegerField(default=30),
        ),
    ]
