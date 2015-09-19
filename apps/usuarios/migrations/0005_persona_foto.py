# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20150909_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='foto',
            field=models.ImageField(default=b'profile-pics/image-default.png', null=True, upload_to=b'profile-pics/', blank=True),
        ),
    ]
