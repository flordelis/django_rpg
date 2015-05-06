from django.db import models


class Encounter(models.Model):
    name = models.CharField(max_length=75)
    campaign = models.ForeignKey("Campaign")

    is_running = models.BooleanField(default=False)
    round = models.PositiveIntegerField(default=0)

    class Meta:
        app_label = "rpg_base"

    def __unicode__(self):
        return self.name

    def start(self):
        for row in self.charactertemplateinencounter_set.all():
            num = row.num
            template = row.character_template
            encounter = row.encounter

            characters = template.create_characters(num=num, encounter.campaign)

            for character in characters:
                Charact

        self.is_running = True
        self.save()