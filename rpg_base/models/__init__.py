from campaign import *
from character import *
from encounter import *
from location import *


class CharacterClass(models.Model):
    character = models.ForeignKey(Character)
    dnd_class = models.ForeignKey(DndClass)
    levels = models.PositiveIntegerField()


class CharacterTemplateInEncounter(models.Model):
    character_template = models.ForeignKey(CharacterTemplate)
    encounter = models.ForeignKey(Encounter)
    num = models.PositiveIntegerField(default=1)


class CharacterInEncounter(models.Model):
    character = models.ForeignKey(Character)
    encounter = models.ForeignKey(Encounter)
    hp_current = models.IntegerField()
    initiative = models.PositiveIntegerField


class CharacterIntroducesEncounter(models.Model):
    """
    This model represents a character who has information that might
    lead the players to this encounter.
    """
    character = models.ForeignKey(Character)
    encounter = models.ForeignKey(Encounter)
    description = models.CharField(max_length=250)


class CharactersAtLocation(models.Model):
    character = models.ForeignKey(Character)
    location = models.ForeignKey(Location)
    description = models.CharField(max_length=250, null=True, blank=True, default="")


class EncounterLocation(models.Model):
    encounter = models.ForeignKey(Encounter)
    location = models.ForeignKey(Location)
    description = models.CharField(max_length=250, null=True, blank=True, default="")
