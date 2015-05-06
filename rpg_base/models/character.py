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
    cr = models.PositiveIntegerField(blank=True, null=True, default=None)
    initiative_modifier = models.IntegerField(blank=True, null=True, default=0)
    race = models.ForeignKey("Race")
    user = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        app_label = "rpg_base"

    def create_characters(self, campaign, num=1, name='', player_owned=False):
        """

        :param campaign:
            Required. The campaign that generated characters will belong to
        :param num:
            The number of characters to generate.
        :param name:
            The name applied to all generated characters.
        :param initiative_modifier:
            The initiative modifier that each character will apply to their rolls
        :param player_owned:
            Whether or not this character belongs to a player
        """
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

            new_characters.append(Character.objects.create(campaign=campaign, name=name,
                                                           initiative_modifier=self.initiative_modifier, hp=hp,
                                                           race=self.race, player_owned=player_owned))
        return new_characters

    def __unicode__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=50)
    initiative_modifier = models.IntegerField()
    hp = models.PositiveIntegerField()
    race = models.ForeignKey("Race")
    template = models.ForeignKey("CharacterTemplate", null=True, blank=True)
    player_owned = models.BooleanField(default=False)
    cr = models.PositiveIntegerField(blank=True, null=True, default=None)
    campaign = models.ForeignKey("Campaign")

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
    num = models.IntegerField(default=1)
    die = models.PositiveIntegerField(choices=HIT_DIE_CHOICES)
    mod = models.IntegerField(default=0)
    character_template = models.ForeignKey(CharacterTemplate)

    class Meta:
        app_label = "rpg_base"

    def roll(self):
        roll = 0
        for i in range(self.num):
            roll += randint(1, self.die)

        return roll + self.mod

    def __unicode__(self):
        return "%sd%s + %s" % (self.num, self.die, self.mod)