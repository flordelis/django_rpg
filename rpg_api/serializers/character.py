from rest_framework import serializers
from rpg_base.models import Character

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            'name', 'race', 'template', 'cr', 'hp',
            'initiative_modifier', 'type',
            'campaign', 'encounter_only'

        )

