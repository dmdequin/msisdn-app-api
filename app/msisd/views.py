"""
Views for MSISD APIs.
"""
from rest_framework import viewsets

from core.models import MSISD
from msisd import serializers

from django.shortcuts import render

import phonenumbers
from phonenumbers.phonenumberutil import (
    region_code_for_number,
    NumberParseException,
)


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
    """View for the API homepage."""
    context = {}
    return render(request, "base.html", context=context)


def msisdn_search_view(request, *args, **kwargs):
    """View for searching the MSISD API."""
    query_dict = request.GET  # this is a dictionary
    msisdn = query_dict.get("msisdn")

    msisd_object = None
    if msisdn is not None:

        if MSISD.objects.filter(msisdn=msisdn).exists():
            # If entry exists in database, get object
            msisd_object = MSISD.objects.get(msisdn=msisdn)
            context = {"object": msisd_object}

            return render(request, "search.html", context)


        elif len(msisdn) < 7:
            # If length < minimum valid international number length
            return render(request,
                          "base.html",
                          {"message": "Entry too short, try again."})

        else:
            # If not in db long enough make format compatible with phonenumbers
            number = "+" + str(msisdn)

            try:
                # Check if valid phone number
                x = phonenumbers.parse(number)
                country_code = x.country_code
                country_identifier = region_code_for_number(x)
                subscriber_number = x.national_number

                payload = {
                    'msisdn': msisdn,
                    'MNO': 'unknown',
                    'country_code': country_code,
                    'subscriber_number': subscriber_number,
                    'country_identifier': country_identifier,
                }
                # print(payload)

                if payload['country_identifier'] == None:
                    # If country ID not parsable
                    return render(request,
                              "base.html",
                              {"message": "Entry invalid, try again."})

                else:
                    # If number passes create MSISD object
                    MSISD.objects.create(**payload)

                    # Context to pass to html
                    context = {"object": payload,
                               "message": "New number added to database!"}

                    return render(request, 'search.html', context)

            except NumberParseException:
                # If number is not able to be parsed
                return render(request,
                              "base.html",
                              {"message": "Entry invalid, try again."})
