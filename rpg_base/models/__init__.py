from campaign import *
from character import *
from encounter import *
from organization import *
from location import *


class CharacterClass(models.Model):
    """
    A character has a levels in a class, and may have multiple classes.
    """
    character = models.ForeignKey(Character)
    dnd_class = models.ForeignKey(DndClass)
    levels = models.PositiveIntegerField()


class CharacterTemplateInEncounter(models.Model):
    """
    A GM may select a Template with which to generate enemy, or friendly, NPCs.

    Multiple instances of these NPCs may be generated for an Encounter.
    """
    character_template = models.ForeignKey(CharacterTemplate)
    encounter = models.ForeignKey(Encounter)
    num = models.PositiveIntegerField(default=1)


class CharacterIntroducesEncounter(models.Model):
    """
    This model represents a character who has information that might
    lead the players to an encounter.
    """
    character = models.ForeignKey(Character)
    encounter = models.ForeignKey(Encounter)
    description = models.CharField(max_length=250)


class CharacterLocationRelationship(models.Model):
    """
    A generic model representing a characters relationship to some location.
    """
    character = models.ForeignKey(Character)
    location = models.ForeignKey(Location)
    description = models.CharField(max_length=250, null=True, blank=True, default="")

class CharacterRelationship(models.Model):
    from_character = models.ForeignKey("Character", related_name="from_characters")
    to_character = models.ForeignKey("Character", related_name="to_characters")
    description = models.CharField(max_length=250, null=True, blank=True, default="")


class EncounterLocation(models.Model):
    """
    Ties an encounter to a location.
    """
    encounter = models.ForeignKey(Encounter)
    location = models.ForeignKey(Location)
    description = models.CharField(max_length=250, null=True, blank=True, default="")
