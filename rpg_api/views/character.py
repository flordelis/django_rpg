from rpg_api.serializers import *
from rpg_base.models import *
from rest_framework import viewsets

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_fields = (
        'name', 'race', 'race__name',
        'campaign', 'campaign__name',
        'template__name', 'template',
        'type',
    )


class DndClassViewSet(viewsets.ModelViewSet):
    queryset = DndClass.objects.all()
    serializer_class = DndClassSerializer
    filter_fields = ('name',)


class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    filter_fields = ('name',)


class CharacterTemplateViewSet(viewsets.ModelViewSet):
    queryset = CharacterTemplate.objects.all()
    serializer_class = CharacterTemplateSerializer
    filter_fields = (
        'name', 'race__name', 'cr',
    )


class HitDieViewSet(viewsets.ModelViewSet):
    queryset = HitDie.objects.all()
    serializer_class = HitDieSerializer




