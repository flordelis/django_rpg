# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('cr', models.FloatField(default=None, null=True, blank=True)),
                ('hp', models.PositiveIntegerField()),
                ('initiative_modifier', models.IntegerField()),
                ('type', models.CharField(default=False, max_length=2, choices=[(b'PL', b'Player'), (b'EN', b'Enemy'), (b'AL', b'Ally'), (b'NT', b'Neutral'), (b'EO', b'Encounter Only')])),
                ('campaign', models.ForeignKey(to='rpg_base.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('levels', models.PositiveIntegerField()),
                ('character', models.ForeignKey(to='rpg_base.Character')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterInEncounter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hp_current', models.IntegerField()),
                ('character', models.ForeignKey(to='rpg_base.Character')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterIntroducesEncounter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=250)),
                ('character', models.ForeignKey(to='rpg_base.Character')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterLocationRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(default=b'', max_length=250, null=True, blank=True)),
                ('character', models.ForeignKey(to='rpg_base.Character')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('cr', models.PositiveIntegerField(default=None, null=True, blank=True)),
                ('initiative_modifier', models.IntegerField(default=0, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterTemplateInEncounter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.PositiveIntegerField(default=1)),
                ('character_template', models.ForeignKey(to='rpg_base.CharacterTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='DndClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75)),
                ('is_running', models.BooleanField(default=False)),
                ('round', models.PositiveIntegerField(default=0)),
                ('campaign', models.ForeignKey(to='rpg_base.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='EncounterLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(default=b'', max_length=250, null=True, blank=True)),
                ('encounter', models.ForeignKey(to='rpg_base.Encounter')),
            ],
        ),
        migrations.CreateModel(
            name='HitDie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField(default=1)),
                ('die', models.PositiveIntegerField(choices=[(4, b'4'), (6, b'6'), (8, b'8'), (10, b'10'), (12, b'12')])),
                ('mod', models.IntegerField(default=0)),
                ('character_template', models.ForeignKey(to='rpg_base.CharacterTemplate')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=250)),
                ('parent_location', models.ForeignKey(default=None, blank=True, to='rpg_base.Location', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('parent_race', models.ForeignKey(default=None, blank=True, to='rpg_base.Race', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='encounterlocation',
            name='location',
            field=models.ForeignKey(to='rpg_base.Location'),
        ),
        migrations.AddField(
            model_name='charactertemplateinencounter',
            name='encounter',
            field=models.ForeignKey(to='rpg_base.Encounter'),
        ),
        migrations.AddField(
            model_name='charactertemplate',
            name='race',
            field=models.ForeignKey(to='rpg_base.Race'),
        ),
        migrations.AddField(
            model_name='charactertemplate',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='characterlocationrelationship',
            name='location',
            field=models.ForeignKey(to='rpg_base.Location'),
        ),
        migrations.AddField(
            model_name='characterintroducesencounter',
            name='encounter',
            field=models.ForeignKey(to='rpg_base.Encounter'),
        ),
        migrations.AddField(
            model_name='characterinencounter',
            name='encounter',
            field=models.ForeignKey(to='rpg_base.Encounter'),
        ),
        migrations.AddField(
            model_name='characterclass',
            name='dnd_class',
            field=models.ForeignKey(to='rpg_base.DndClass'),
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.ForeignKey(to='rpg_base.Race'),
        ),
        migrations.AddField(
            model_name='character',
            name='template',
            field=models.ForeignKey(default=None, blank=True, to='rpg_base.CharacterTemplate', null=True),
        ),
    ]
