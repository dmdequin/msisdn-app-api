"""
Serializers for the user API View.
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        """Model and fields used by the serializer"""
        model = get_user_model()
        # Fields available to be changed by API (not by admin).
        fields = ['email', 'password', 'name']
        # Extra metadata regarding the fields.
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    # Override default create method to ensure data validation.
    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user."""
        # This overrides the default update method.
        password = validated_data.pop('password', None)
        # Call update method on ModelSerializer base class.
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            # View will translate this to an HTTP bad request.
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
