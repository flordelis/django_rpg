# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpg_base', '0013_auto_20150524_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=250)),
                ('campaign', models.ForeignKey(default=None, blank=True, to='rpg_base.Campaign', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=250, null=True, blank=True)),
                ('location', models.ForeignKey(to='rpg_base.Location')),
                ('organization', models.ForeignKey(to='rpg_base.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=250, null=True, blank=True)),
                ('character', models.ForeignKey(to='rpg_base.Character')),
                ('organization', models.ForeignKey(to='rpg_base.Organization')),
            ],
        ),
    ]
