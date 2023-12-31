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
router.register('msisd', views.MSISDViewset)  # api/msisd/msisd/

app_name = 'msisd'

urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.msisdn_base_view, name='home'),
    path('api-search/', views.msisdn_search_view),
]
