# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpg_base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='cr',
            field=models.FloatField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='charactertemplate',
            name='cr',
            field=models.FloatField(default=0, null=True, blank=True),
        ),
    ]
