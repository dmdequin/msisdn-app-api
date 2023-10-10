"""
Tests for MSISD API.
"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import MSISD

from msisd.serializers import (
    MSISDSerializer,
    MSISDDetailSerializer,
)

MSISD_URL = reverse('msisd:msisd-list')


def detail_url(msisdn):
    """Create and return a MSISD detail URL."""
    return reverse('msisd:msisd-detail', args=[msisdn])


def create_msisd_entry(**params):  # params is dict
    """Create and return MSISD object."""
    defaults = {
        'id': 17,
        'msisdn': 905519555325,
        'MNO': "Turkcell",
        'country_code': 90,
        'subscriber_number': 5519555325,
        'country_identifier': 'TR',
    }
    defaults.update(params)

    msisd = MSISD.objects.create(**defaults)
    return msisd


def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)


class PublicMSISDAPITests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API."""
        res = self.client.get(MSISD_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateMSISDAPITests(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.client = APIClient()
        self.user = create_user(
            email='user@example.com',
            password='testpass123')
        self.client.force_authenticate(self.user)

    def test_retrieve_msisd_list(self):
        """Test retrieving a list of msisd objects."""
        create_msisd_entry()
        create_msisd_entry(id=13, msisdn=12345678)

        res = self.client.get(MSISD_URL)

        msisd_list = MSISD.objects.all().order_by('-msisdn')
        serializer = MSISDSerializer(msisd_list, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_get_msisd_detail(self):
        """Test get MSISD detail."""
        msisd = create_msisd_entry(msisdn=87654321)

        url = detail_url(msisd.id)  # Was msisd.msisd
        res = self.client.get(url)

        serializer = MSISDDetailSerializer(msisd)
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
        url = detail_url(msisd.id)  # Was msisd.msisd
        res = self.client.patch(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        msisd.refresh_from_db()
        self.assertEqual(msisd.country_code, payload['country_code'])
        self.assertEqual(msisd.country_identifier, an_identifier)

    def test_create_msisd(self):
        """Test creating msisd object."""
        msisd = create_msisd_entry()
        self.assertEqual(str(msisd), str(msisd.msisdn))

    def test_create_msisd_entry(self):
        """Test creating a msisd entry."""
        payload = {
            'msisdn': 221313131415,
            'MNO': "Test Provider",
            'country_code': 22,
            'subscriber_number': 1313131415,
            'country_identifier': 'XX',
        }
        res = self.client.post(MSISD_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        msisd = MSISD.objects.get(msisdn=res.data['msisdn'])
        for k, v in payload.items():
            self.assertEqual(getattr(msisd, k), v)
        self.assertEqual(msisd.msisdn, payload['msisdn'])

    def test_delete_msisd_entry(self):
        """Test deleting a msisd entry successful."""
        msisd = create_msisd_entry()

        url = detail_url(msisd.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(MSISD.objects.filter(id=msisd.id).exists())
