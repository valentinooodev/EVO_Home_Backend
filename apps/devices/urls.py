from django.urls import path, include
from .views import (
    RoomDeviceListAPIView
)

app_name = 'devices'

urlpatterns = [
    path('room/<int:pk>', RoomDeviceListAPIView.as_view(), name='device_list'),
]
