from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    DeviceCategoryModel,
    DeviceModel,
    DeviceHistoryModel
)
from .serializers import (
    DeviceSerializer
)
from config.settings.base import AUTH_USER_MODEL
from commons.response import default_response


class RoomDeviceListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        devices = DeviceModel.objects.filter(room=pk, is_sensor=False)
        serializer = DeviceSerializer(devices, many=True)
        return Response(default_response(serializer.data, "ok"))
