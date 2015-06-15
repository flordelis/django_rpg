from rest_framework import serializers
from rpg_base.models import Organization

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'pk', 'name', 'description', 'campaign',
        )

