from rpg_api.serializers import OrganizationSerializer
from rpg_base.models import Organization
from rest_framework import viewsets

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filter_fields = (
        'name',
    )

