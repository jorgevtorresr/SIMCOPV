# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inst_nombre', models.CharField(max_length=75)),
                ('inst_direccion', models.CharField(max_length=100)),
                ('inst_telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('idunidad', models.AutoField(serialize=False, primary_key=True)),
                ('uni_nombre', models.CharField(max_length=75)),
            ],
        ),
    ]
