from rpg_api.serializers import CampaignSerializer
from rpg_base.models import Campaign
from rest_framework import viewsets

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    filter_fields = ('name',)
