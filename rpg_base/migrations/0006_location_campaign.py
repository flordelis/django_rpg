# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpg_base', '0005_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='campaign',
            field=models.ForeignKey(default=None, blank=True, to='rpg_base.Campaign', null=True),
        ),
    ]
