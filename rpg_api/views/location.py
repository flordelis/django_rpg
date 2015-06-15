from rpg_api.serializers import LocationSerializer
from rpg_base.models import Location
from rest_framework import viewsets

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_fields = (
        'name', 'parent_location__name', 'parent_location',
    )

