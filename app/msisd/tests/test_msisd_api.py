"""
Tests for MSISD API.
"""
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import MSISD

from msisd.serializers import (
    MsisdSerializer,
    MsisdDetailSerializer,
)

MSISD_URL = reverse('msisd:msisd-list')


def detail_url(msisdn):
    """Create and return a MSISD detail URL."""
    return reverse('msisd:msisd-detail', args=[msisdn])


def create_msisd_entry(**params):
    """Create and return MSISD object."""
    defaults = {
        'msisdn': 905519555325,
        'MNO': "Turkcell",
        'country_code': 90,
        'subscriber_number': 5519555325,
        'country_identifier': 'TR',
    }
    defaults.update(params)

    msisd = MSISD.objects.create(**defaults)
    return msisd


class PublicMsisdAPITests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_msisd_list(self):
        """Test retrieving a list of msisd objects."""
        create_msisd_entry()
        create_msisd_entry()

        res = self.client.get(MSISD_URL)

        msisd_list = MSISD.objects.all().order_by('-id')
        serializer = MsisdSerializer(msisd_list, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_msisd_entry(self):
        """Test creating a msisd entry."""
        payload = {
            'msisdn': 111111111111,
            'MNO': "Phone Provider",
            'country_code': 11,
            'subscriber_number': 1111111111,
            'country_identifier': 'XX',
        }
        res = self.client.post(MSISD_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        msisd = MSISD.objects.get(id=res.data['id'])
        for k, v in payload.items():
            self.assertEqual(getattr(msisd, k), v)
        self.assertEqual(msisd.msisdn, payload['msisdn'])

    def test_get_msisd_detail(self):
        """Test get MSISD detail."""
        msisd = create_msisd_entry()

        url = detail_url(msisd.id)
        res = self.client.get(url)

        serializer = MsisdDetailSerializer(msisd)
        self.assertEqual(res.data, serializer.data)

    def test_partial_update(self):
        """Test partial update of a MSISD object."""
        an_identifier = 'YY'
        msisd = create_msisd_entry(
            msisdn=111111111112,
            MNO='Special Provider',
            country_identifier=an_identifier,
        )

        payload = {'country_code': 22}
        url = detail_url(msisd.id)
        res = self.client.patch(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        msisd.refresh_from_db()
        self.assertEqual(msisd.country_code, payload['country_code'])
        self.assertEqual(msisd.country_identifier, an_identifier)
        # self.assertEqual(msisd.country_code, self.country_code)
