"""
Views for MSISD APIs.
"""
from rest_framework import viewsets

from core.models import MSISD
from msisd import serializers
# from msisd.forms import GetMSISDNForm

from django.shortcuts import render
# from django.urls import reverse


class MsisdViewset(viewsets.ModelViewSet):
    """View for manage MSISD APIs."""
    serializer_class = serializers.MsisdDetailSerializer
    queryset = MSISD.objects.all()

    def get_queryset(self):
        """Retrieve MSISD list."""
        return self.queryset.order_by('-msisdn')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            # Return standard serializer if action is list.
            return serializers.MsisdSerializer

        # Else, return detailed serializer.
        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new MSISD entry."""
        serializer.save()


def msisdn_base_view(request):
    context = {}
    return render(request, "base.html", context=context)


def msisdn_search_view(request, *args, **kwargs):
    """View for searching the MSISD API."""
    query_dict = request.GET  # this is a dictionary
    msisdn = query_dict.get("msisdn")

    msisd_object = None
    if msisdn is not None:
        if MSISD.objects.filter(msisdn=msisdn).exists():
            # If entry exists in database
            msisd_object = MSISD.objects.get(msisdn=msisdn)
        else:
            return render(request, "base.html",
                          {"message": "The number does not exist in database"})

    context = {"object": msisd_object}

    return render(request, "search.html", context)
