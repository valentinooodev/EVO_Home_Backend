from django.urls import path, include
from .views import (
    DevicePowerSwitchAPIView
)


app_name = 'actions'

urlpatterns = [
    path('switch/<int:pk>/', DevicePowerSwitchAPIView.as_view(), name='power_switch'),
]
