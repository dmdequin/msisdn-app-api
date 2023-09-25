"""
Serializers for MSISD API.
"""
from rest_framework import serializers

from core.models import MSISD


class MsisdSerializer(serializers.ModelSerializer):
    """Serializer for MSISD objects."""

    class Meta:
        model = MSISD
        fields = ['id', 'msisdn', 'country_code',
                  'subscriber_number',
                  ]
        read_only_fields = ['id']  # 'msisdn'

    def create(self, validated_data):
        """Create a MSISD object."""
        msisd = MSISD.objects.create(**validated_data)

        return msisd


class MsisdDetailSerializer(MsisdSerializer):
    """Serializer for MSISD detail view."""

    class Meta(MsisdSerializer.Meta):
        fields = MsisdSerializer.Meta.fields + ['MNO', 'country_identifier']
