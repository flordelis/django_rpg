# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpg_base', '0011_auto_20150524_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characterrelationship',
            name='from_character',
        ),
        migrations.RemoveField(
            model_name='characterrelationship',
            name='to_character',
        ),
        migrations.RemoveField(
            model_name='character',
            name='relationships',
        ),
        migrations.DeleteModel(
            name='CharacterRelationship',
        ),
    ]
