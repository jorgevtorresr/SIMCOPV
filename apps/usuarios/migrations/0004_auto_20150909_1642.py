# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20150731_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificacion',
            old_name='not_descripcion',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='notificacion',
            old_name='not_estado_visto',
            new_name='estado_visto',
        ),
        migrations.RenameField(
            model_name='periodo',
            old_name='peri_anio_fin',
            new_name='anio_fin',
        ),
        migrations.RenameField(
            model_name='periodo',
            old_name='peri_anio_inicio',
            new_name='anio_inicio',
        ),
        migrations.RenameField(
            model_name='periodo',
            old_name='peri_dias_vac',
            new_name='dias_vac',
        ),
        migrations.RenameField(
            model_name='periodo',
            old_name='peri_horas_vac',
            new_name='horas_vac',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='per_puesto',
            new_name='puesto',
        ),
        migrations.RenameField(
            model_name='unidad',
            old_name='uni_nombre',
            new_name='nombre',
        ),
    ]
