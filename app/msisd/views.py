"""
Views for MSISD APIs.
"""
from rest_framework import viewsets

from core.models import MSISD
from msisd import serializers
from msisd.forms import GetMSISDNForm

from django.shortcuts import render
# from django.http import HttpResponseRedirect
from django.urls import reverse


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


# This is hard coded for now...
def get_msisd(request, msisdn=5492216176161):
    """Get detail using MSISDN."""
    msisd_list = MSISD.objects.all()
    msisd_data = msisd_list.filter(msisdn=msisdn)
    return render(request, 'msisd_result.html', {'msisd_data': msisd_data})


def search_msisdn(request):
    """View for searching MSISD API."""

    if request.method == 'POST':
        form = GetMSISDNForm(request.POST)
        # Check if form is valid
        if form.is_valid():
            # This doesn't do anything yet
            return reverse('msisd:msisd-detail', args=[form.msisdn])
    else:
        # Get a blank form
        form = GetMSISDNForm()

    return render(request, 'msisd_search.html', {'form': form})
