"""
Views for MSISD APIs.
"""

from rest_framework import viewsets
# from rest_framework.authentication import TokenAuthentication
# from reset_framework.permissions import IsAuthenticated

from core.models import MSISD
from msisd import serializers


class MsisdViewset(viewsets.ModelViewSet):
    """View for manage MSISD APIs."""
    serializer_class = serializers.MsisdDetailSerializer
    queryset = MSISD.objects.all()

    def get_queryset(self):
        """Retrieve MSISD list."""
        return self.queryset.order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.MsisdSerializer

        return self.serializer_class
