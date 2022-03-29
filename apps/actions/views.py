from django.shortcuts import render
from rest_framework.views import APIView
from apps.devices.models import DeviceModel
from rest_framework.response import Response
from rest_framework import permissions
from commons.response import default_response
from apps.devices.serializers import DeviceHistorySerializer


class DevicePowerSwitchAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        device = DeviceModel.objects.get(id=pk)
        action = request.data.get('status')
        if device.status == action:
            return Response(default_response(request.data))
        device.status = action
        device.save()
        device_history = dict()
        device_history['device'] = pk
        if action:
            device_history['data'] = 'Turn ON'
        else:
            device_history['data'] = 'Turn OFF'
        device_history_serializer = DeviceHistorySerializer(data=device_history)
        if device_history_serializer.is_valid():
            device_history_serializer.save()
        return Response(default_response(request.data))
