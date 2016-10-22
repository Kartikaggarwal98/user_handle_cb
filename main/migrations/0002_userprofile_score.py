# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='score',
            field=models.IntegerField(default=1, blank=True),
            preserve_default=False,
        ),
    ]
