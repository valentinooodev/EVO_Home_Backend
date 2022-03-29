from django.urls import path, include
from .views import RoomListAPIView


app_name = 'rooms'

urlpatterns = [
    path('', RoomListAPIView.as_view(), name='room_list'),
]
