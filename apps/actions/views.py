from django.shortcuts import render
from rest_framework.views import APIView
from apps.devices.models import DeviceModel
from rest_framework.response import Response
from rest_framework import permissions
from commons.response import default_response


class DevicePowerSwitchAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        device = DeviceModel.objects.get(id=pk)
        action = request.data.get('status')
        device.status = action
        device.save()
        return Response(default_response(request.data))
