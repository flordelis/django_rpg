# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpg_base', '0008_auto_20150524_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characterrelationship',
            name='character',
        ),
        migrations.RemoveField(
            model_name='character',
            name='characters',
        ),
        migrations.AddField(
            model_name='character',
            name='relationships',
            field=models.ManyToManyField(related_name='related_to', to='rpg_base.Character'),
        ),
        migrations.DeleteModel(
            name='CharacterRelationship',
        ),
    ]
