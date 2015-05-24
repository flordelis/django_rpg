# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpg_base', '0007_characterrelationship'),
    ]

    operations = [
        migrations.RenameField(
            model_name='characterrelationship',
            old_name='target',
            new_name='character',
        ),
        migrations.RemoveField(
            model_name='characterrelationship',
            name='subject',
        ),
        migrations.AddField(
            model_name='character',
            name='characters',
            field=models.ManyToManyField(to='rpg_base.Character', through='rpg_base.CharacterRelationship', blank=True),
        ),
    ]
