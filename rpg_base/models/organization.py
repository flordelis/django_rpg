from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    campaign = models.ForeignKey("Campaign", null=True, blank=True, default=None)

    class Meta:
        app_label = "rpg_base"

    def __unicode__(self):
        return self.name


class OrganizationMember(models.Model):
    organization = models.ForeignKey(Organization)
    character = models.ForeignKey("Character")
    description = models.CharField(max_length=250, blank=True, null=True)


class OrganizationLocation(models.Model):
    organization = models.ForeignKey(Organization)
    location = models.ForeignKey("Location")
    description = models.CharField(max_length=250, blank=True, null=True)
