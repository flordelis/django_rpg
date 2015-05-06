from django.contrib.auth.models import User
from django.db import models


class Campaign(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User)

    class Meta:
        app_label = "rpg_base"

    def __unicode__(self):
        return self.name
