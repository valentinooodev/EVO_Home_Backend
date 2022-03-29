from django.urls import path
from .views import (
    AdminRoomAPIView,
    AdminDeviceAPIView
)


app_name = 'admins'

urlpatterns = [
    path('rooms/', AdminRoomAPIView.as_view(), name='admin_rooms'),
    path('rooms/<int:pk>/', AdminRoomAPIView.as_view(), name='admin_rooms'),
    path('devices/', AdminDeviceAPIView.as_view(), name='admin_devices'),
    path('devices/<int:pk>', AdminDeviceAPIView.as_view(), name='admin_devices'),
]
