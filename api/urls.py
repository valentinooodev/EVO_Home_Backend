from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = 'api'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('actions/', include('apps.actions.urls'), name='token_verify'),
    path('devices/', include('apps.devices.urls', namespace='devices')),
    path('rooms/', include('apps.rooms.urls', namespace='rooms')),
    path('users/', include('apps.users.urls', namespace='users')),
]
