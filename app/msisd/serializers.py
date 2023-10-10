"""
Serializers for MSISD API.
"""
from rest_framework import serializers

from core.models import MSISD


class MSISDSerializer(serializers.ModelSerializer):
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

    def update(self, instance, validated_data):
        """Update MSISD object."""

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class MSISDDetailSerializer(MSISDSerializer):
    """Serializer for MSISD detail view."""

    class Meta(MSISDSerializer.Meta):
        fields = MSISDSerializer.Meta.fields + ['MNO', 'country_identifier']
