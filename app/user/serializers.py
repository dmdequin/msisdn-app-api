"""
Serializers for the user API View.
"""
from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        """Model and fields used by the serializer"""
        model = get_user_model()
        # Fields available to be changed by API (not by admin)
        fields = ['email', 'password', 'name']
        # extra metadata regarding the fields
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    # Override default create method to ensure data validation
    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)
