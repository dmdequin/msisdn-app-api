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


"""def msisd_result_view(request, msisdn=5492216176161):
    #Get detail using MSISDN.
    msisd_list = MSISD.objects.all()
    msisd_data = msisd_list.filter(msisdn=msisdn)
    return render(request, 'msisd_result.html', {'msisd_data': msisd_data})


def msisdn_search(request):
    #View for searching MSISD API.

    if request.method == 'POST':
        form = GetMSISDNForm(request.POST)
        # Check if form is valid
        if form.is_valid():
            # This doesn't do anything yet
            return reverse('msisd:msisd-detail', args=[form.msisdn])
    else:
        # Get a blank form
        form = GetMSISDNForm()

    return render(request, 'msisd_search.html', {'form': form})"""


def msisdn_base_view(request):
    context = {}
    return render(request, "base.html", context=context)


def msisdn_search_view(request, *args, **kwargs):
    """View for searching the MSISD API."""
    query_dict = request.GET  # this is a dictionary
    msisdn = query_dict.get("msisdn")

    msisd_object = None
    if msisdn is not None:
        msisd_object = MSISD.objects.get(msisdn=msisdn)
        # msisd_object = MSISD.objects.all().filter(msisdn=int(msisdn))
        print(f"MSISD subsc. num.: {msisd_object.subscriber_number}")
        print(f"MSISD MNO: {msisd_object.MNO}")

    print(type(msisd_object))
    context = {"object": msisd_object}
    # print(f"context: {context['object']}")

    return render(request, "search.html", context)
