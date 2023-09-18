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
    serializer_class = serializers.MsisdSerializer
    queryset = MSISD.objects.all()

    def get_queryset(self):
        """Retrieve MSISD list."""
        return self.queryset.order_by('-id')
