from rest_framework import serializers
from rpg_base.models import Campaign

class CampaignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campaign
        fields = ('name', 'user', 'description',)

