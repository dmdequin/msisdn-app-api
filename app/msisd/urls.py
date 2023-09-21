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
    # path('api-search/', views.msisdn_base_view),
    path('api-search/', views.msisdn_search_view),
    # api/msisd/search/
    # path('search/', views.msisdn_search),
    # api/msisd/result/
    # path('result/', views.msisd_result_view, name='msisd_result_view'),
]
