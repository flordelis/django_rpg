from django.db import models


class EncounterManager(models.Manager):
    def enemy_npcs(self):
        pass

    def friendly_npcs(self):
        pass

    def players(self):
        return super(EncounterManager, self).get_queryset().filter(character__player_owned=True)


class Encounter(models.Model):
    name = models.CharField(max_length=75)
    campaign = models.ForeignKey("Campaign")

    is_running = models.BooleanField(default=False)
    round = models.PositiveIntegerField(default=0)

    objects = EncounterManager()

    class Meta:
        app_label = "rpg_base"

    def __unicode__(self):
        return self.name

    def start(self):
        """
        Sets `is_running` to True, and initiative and NPCs.
        """
        for row in self.charactertemplateinencounter_set.all():
            num = row.num
            template = row.character_template
            encounter = row.encounter

            characters = template.create_characters(encounter.campaign, num=num)

            for character in characters:
                CharacterInEncounter.objects.create(character=character,
                                                    encounter=encounter,
                                                    hp_current=character.hp,
                                                    initiative=0)

        # TODO Roll everyone's initiative.

        self.is_running = True
        self.save()

    def end(self):
        # Sum experience from enemy NPCs
        # Split experience amongst players
        self.is_running = False
        self.save()


class CharacterInEncounter(models.Model):
    """
    Characters have a rolled Initiative specific to an encounter, as well as
    Hit Points.
    """
    character = models.ForeignKey("Character")
    encounter = models.ForeignKey(Encounter)
    hp_current = models.IntegerField()
    initiative = models.PositiveIntegerField