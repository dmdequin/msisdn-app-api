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


def in_database(msisdn):
    """Check if msisd object exists in database."""
    exists = False
    if MSISD.objects.filter(msisdn=msisdn).exists():
        exists = True

    return exists


def get_msisd_object(request, msisdn):
    """Get msisdn object from db and render the page."""
    msisd_object = MSISD.objects.get(msisdn=msisdn)
    context = {"object": msisd_object}

    return render(request, "search.html", context)


def create_msisd_object(request, **payload):
    """Create msisd object and render page."""
    MSISD.objects.create(**payload)

    context = {"object": payload,
               "message": "New number added to database!"}

    return render(request, 'search.html', context)


def render_page_invalid_number(request, short=False):
    """Render page for invalid numbers."""
    context = {"message": "Entry invalid, try again."}

    if short:
        context = {"message": "Entry too short, try again."}

    return render(request, "base.html", context)


def parse_number_information(msisdn, valid_number):
    """Parse various information from given valid number."""
    payload = {
        'msisdn': msisdn,
        'MNO': 'unknown',
        'country_code': valid_number.country_code,
        'subscriber_number': valid_number.national_number,
        'country_identifier': region_code_for_number(valid_number),
    }

    return payload


def number_is_too_short(number):
    """Return True if number is too short."""
    return (len(number) < 7)


def msisdn_search_view(request, *args, **kwargs):
    """View for searching the MSISD API."""
    query_dict = request.GET  # This is a dictionary
    msisdn = query_dict.get("msisdn")

    if msisdn is not None:

        if in_database(msisdn):
            # If entry in database get object and render page
            return get_msisd_object(request, msisdn)

        if number_is_too_short(msisdn):
            # If length < minimum valid international number length
            return render_page_invalid_number(request, 'short')

        # Make format compatible with phonenumbers
        number = "+" + str(msisdn)

        try:
            # Check if valid phone number
            valid_number = phonenumbers.parse(number)

            payload = parse_number_information(msisdn, valid_number)

            if payload['country_identifier'] is None:
                # If country ID not parsable
                return render_page_invalid_number(request)

            # If number passes create MSISD object and render
            return create_msisd_object(request, **payload)

        except NumberParseException:
            # If number is not able to be parsed
            return render_page_invalid_number(request)
