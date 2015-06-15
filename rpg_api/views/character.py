from rpg_api.serializers import *
from rpg_base.models import *
from rest_framework import viewsets

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class DndClassViewSet(viewsets.ModelViewSet):
    queryset = DndClass.objects.all()
    serializer_class = DndClassSerializer


class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer


class CharacterTemplateViewSet(viewsets.ModelViewSet):
    queryset = CharacterTemplate.objects.all()
    serializer_class = CharacterTemplateSerializer


class HitDieViewSet(viewsets.ModelViewSet):
    queryset = HitDie.objects.all()
    serializer_class = HitDieSerializer




