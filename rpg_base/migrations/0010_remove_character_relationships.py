# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpg_base', '0009_auto_20150524_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='relationships',
        ),
    ]
