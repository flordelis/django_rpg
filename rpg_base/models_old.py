from django.contrib.auth.models import User
from django.db import models
from random import randint


class DndClass(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Race(models.Model):
    name = models.CharField(max_length=25)
    parent_race = models.ForeignKey("Race", blank=True, null=True, default=None)

    def __unicode__(self):
        return self.name


class CharacterTemplate(models.Model):
    name = models.CharField(max_length=50)
    cr = models.PositiveIntegerField(blank=True, null=True, default=None)
    race = models.ForeignKey(Race)
    user = models.ForeignKey(User, blank=True, null=True)

    def create_characters(self, num=1, name='', initiative_modifier=0, player_owned=False):
        # Create a set of characters.
        new_characters = []
        for i in range(num):
            # Unless a name is given, use the template name.
            name = self.name if name is '' else name

            # If there's more than one we add the index value.
            name += ' %s' % i if num > 1 else ''

            # Roll all Hit Die for this template.
            hp = 0
            for hd in self.hitdie_set.all():
                hp += hd.roll()

            new_characters.append(Character.objects.create(name=name, initiative_modifier=initiative_modifier,
                                                           hp=hp, race=self.race, player_owned=player_owned))
        return new_characters

    def __unicode__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=50)
    initiative_modifier = models.IntegerField()
    hp = models.PositiveIntegerField()
    race = models.ForeignKey(Race)
    template = models.ForeignKey(CharacterTemplate, null=True, blank=True)
    player_owned = models.BooleanField(default=False)
    cr = models.PositiveIntegerField(blank=True, null=True, default=None)
    campaign = models.ForeignKey("Campaign")

    def __unicode__(self):
        return self.name


class CharacterClass(models.Model):
    character = models.ForeignKey(Character)
    dnd_class = models.ForeignKey(DndClass)
    levels = models.PositiveIntegerField()


class Encounter(models.Model):
    name = models.CharField(max_length=75)
    campaign = models.ForeignKey("Campaign")

    is_running = models.BooleanField(default=False)
    round = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.name

    def start(self):
        for template in self.charactertemplateinencounter_set.all():
            template

        self.is_running = True
        self.save()


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


class HitDie(models.Model):
    HIT_DIE_CHOICES = (
        (4, "4"),
        (6, "6"),
        (8, "8"),
        (10, "10"),
        (12, "12"),
    )
    num = models.IntegerField(default=1)
    die = models.PositiveIntegerField(choices=HIT_DIE_CHOICES)
    mod = models.IntegerField(default=0)
    character_template = models.ForeignKey(CharacterTemplate)

    def roll(self):
        roll = 0
        for i in range(self.num):
            roll += randint(1, self.die)

        return roll + self.mod

    def __unicode__(self):
        return "%sd%s + %s" % (self.num, self.die, self.mod)


class Location(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    parent_location = models.ForeignKey("Location", null=True, blank=True, default=None)

    def __unicode__(self):
        return self.name


class CharactersAtLocation(models.Model):
    character = models.ForeignKey(Character)
    location = models.ForeignKey(Location)
    description = models.CharField(max_length=250, null=True, blank=True, default="")


class EncounterLocation(models.Model):
    encounter = models.ForeignKey(Encounter)
    location = models.ForeignKey(Location)
    description = models.CharField(max_length=250, null=True, blank=True, default="")


class Campaign(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name