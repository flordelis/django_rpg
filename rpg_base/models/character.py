from django.contrib.auth.models import User
from django.db import models
from random import randint


class DndClass(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        app_label = "rpg_base"

    def __unicode__(self):
        return self.name


class Race(models.Model):
    name = models.CharField(max_length=25)
    parent_race = models.ForeignKey("Race", blank=True, null=True, default=None)

    class Meta:
        app_label = "rpg_base"

    def __unicode__(self):
        return self.name


class CharacterTemplate(models.Model):
    name = models.CharField(max_length=50)
    cr = models.FloatField(blank=True, null=True, default=0)
    initiative_modifier = models.IntegerField(blank=True, null=True, default=0)
    race = models.ForeignKey("Race")
    user = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        app_label = "rpg_base"

    def create_characters(self, campaign, num=1, name='', type='EN', encounter_only=True):
        """

        :param campaign:
            Required. The campaign that generated characters will belong to
        :param num:
            The number of characters to generate.
        :param name:
            The name applied to all generated characters.
        :param type:
            The type of character.
        """
        # TODO Check that the Character type is valid.

        name = self.name if name is '' else name

        # Create a set of characters.
        new_characters = []
        for i in range(num):
            iname  = name + (' %s' % (i + 1) if num > 1 else '')

            # Roll all Hit Die for this template.
            hp = 0
            for hd in self.hitdie_set.all():
                hp += hd.roll()

            new_characters.append(Character.objects.create(campaign=campaign, name=iname,
                                                           initiative_modifier=self.initiative_modifier, hp=hp,
                                                           race=self.race, type=type, encounter_only=encounter_only))
        return new_characters

    def __unicode__(self):
        return self.name


class Character(models.Model):
    CHARACTER_TYPE = (
        ('PL', 'Player'),
        ('EN', 'Enemy'),
        ('AL', 'Ally'),
        ('NT', 'Neutral'),
    )

    name = models.CharField(max_length=50)

    race = models.ForeignKey("Race")
    template = models.ForeignKey("CharacterTemplate", null=True, blank=True, default=None)

    cr = models.FloatField(blank=True, null=True, default=0)
    hp = models.PositiveIntegerField()
    initiative_modifier = models.IntegerField()
    type = models.CharField(choices=CHARACTER_TYPE, default=False, max_length=2)
    campaign = models.ForeignKey("Campaign")

    encounter_only = models.BooleanField(default=False)

    class Meta:
        app_label = "rpg_base"

    def __unicode__(self):
        return self.name


class HitDie(models.Model):
    HIT_DIE_CHOICES = (
        (4, "4"),
        (6, "6"),
        (8, "8"),
        (10, "10"),
        (12, "12"),
    )
    num = models.PositiveIntegerField(default=1)
    die = models.PositiveIntegerField(choices=HIT_DIE_CHOICES)
    mod = models.IntegerField(default=0)
    character_template = models.ForeignKey(CharacterTemplate)

    class Meta:
        app_label = "rpg_base"

    def roll(self):
        roll = 0
        for i in range(self.num):
            roll += randint(1, self.die)

        roll += self.mod

        return roll if roll > 0 else 1

    def __unicode__(self):
        return "%sd%s + %s" % (self.num, self.die, self.mod)