"""
URL mappings for the MSISD app.
"""
from django.urls import (
    path,
    include
)

from rest_framework.routers import DefaultRouter

from msisd import views


router = DefaultRouter()
router.register('msisd', views.MsisdViewset)

app_name = 'msisd'

urlpatterns = [
    path('', include(router.urls)),
]
