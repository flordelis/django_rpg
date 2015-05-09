# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpg_base', '0002_auto_20150507_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hitdie',
            name='num',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
