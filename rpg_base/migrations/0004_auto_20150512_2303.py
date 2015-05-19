# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpg_base', '0003_auto_20150507_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='encounter_only',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='type',
            field=models.CharField(default=False, max_length=2, choices=[(b'PL', b'Player'), (b'EN', b'Enemy'), (b'AL', b'Ally'), (b'NT', b'Neutral')]),
        ),
    ]
