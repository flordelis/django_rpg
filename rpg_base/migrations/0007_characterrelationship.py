# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpg_base', '0006_location_campaign'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(default=b'', max_length=250, null=True, blank=True)),
                ('subject', models.ForeignKey(related_name='subject', to='rpg_base.Character')),
                ('target', models.ForeignKey(related_name='target', to='rpg_base.Character')),
            ],
        ),
    ]
