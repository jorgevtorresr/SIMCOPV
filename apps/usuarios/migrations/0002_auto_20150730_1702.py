# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bot_descripcion', models.CharField(max_length=255)),
                ('not_estado_visto', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('peri_anio_inicio', models.CharField(max_length=4)),
                ('peri_anio_fin', models.CharField(max_length=4)),
                ('peri_dias_vac', models.IntegerField()),
                ('peri_horas_vac', models.TimeField()),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('per_puesto', models.CharField(max_length=25)),
                ('unidad', models.ForeignKey(to='usuarios.Unidad')),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TipoNotificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipon_nombre', models.CharField(max_length=55)),
            ],
        ),
        migrations.DeleteModel(
            name='Institucion',
        ),
        migrations.AddField(
            model_name='notificacion',
            name='tiponotif',
            field=models.ForeignKey(to='usuarios.TipoNotificacion'),
        ),
        migrations.AddField(
            model_name='notificacion',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
