from rpg_rest_api.serializers import CampaignSerializer
from rpg_base.models import Campaign
from rest_framework import generics

class CampaignList(generics.ListCreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class CampaignDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
