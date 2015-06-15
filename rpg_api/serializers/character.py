from rest_framework import serializers
from rpg_base.models import Character, DndClass, CharacterTemplate, Race, HitDie

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = (
            'name', 'race', 'template', 'cr', 'hp',
            'initiative_modifier', 'type',
            'campaign', 'encounter_only'

        )

class DndClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DndClass
        fields = ('name', 'parent_race')


class CharacterTemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CharacterTemplate
        fields = ('name', 'cr', 'initiative_modifier', 'race', 'user')


class RaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Race
        fields = ('name',)


class HitDieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HitDie
        fields = ('num', 'die', 'mod', 'character_template')