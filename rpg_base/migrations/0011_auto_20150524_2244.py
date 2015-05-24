# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpg_base', '0010_remove_character_relationships'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(default=b'', max_length=250, null=True, blank=True)),
                ('from_character', models.ForeignKey(related_name='from_characters', to='rpg_base.Character')),
                ('to_character', models.ForeignKey(related_name='to_characters', to='rpg_base.Character')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='relationships',
            field=models.ManyToManyField(related_name='related_to', through='rpg_base.CharacterRelationship', to='rpg_base.Character'),
        ),
    ]
