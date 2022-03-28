from django.urls import path, include


app_name = 'api'

urlpatterns = [
    path('devices/', include('apps.devices.urls', namespace='devices')),
    path('rooms/', include('apps.rooms.urls', namespace='rooms')),
    path('users/', include('apps.users.urls', namespace='users')),
]
