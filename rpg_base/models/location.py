from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    parent_location = models.ForeignKey("Location", null=True, blank=True, default=None)
    campaign = models.ForeignKey("Campaign", null=True, blank=True, default=None)

    class Meta:
        app_label = "rpg_base"

    def __unicode__(self):
        return self.name
