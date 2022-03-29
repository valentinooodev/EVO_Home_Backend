from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.rooms.serializers import RoomSerializer
from apps.devices.serializers import DeviceSerializer
from apps.rooms.models import RoomModel
from apps.devices.models import DeviceModel
from commons.response import default_response


class AdminRoomAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        rooms = RoomModel.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(default_response(serializer.data))

    def post(self, request):
        data = request.data
        serializer = RoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(default_response(serializer.data, "Add new room successfully"))
        return Response(default_response(serializer.errors, "Add new room failed, please try again"),
                        status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        room = RoomModel.objects.get(id=pk)
        serializer = RoomSerializer(room, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(default_response(serializer.data, "Change information successfully"))
        return Response(default_response(serializer.errors, "Change information failed, please try again"),
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        room = RoomModel.objects.get(id=pk)
        room.delete()
        return Response(default_response({}, "Delete room successfully"), status=status.HTTP_204_NO_CONTENT)


class AdminDeviceAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        devices = RoomModel.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(default_response(serializer.data))

    def post(self, request):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(default_response(serializer.data, "Add new device successfully"))
        return Response(default_response(serializer.errors, "Add new device failed, please try again"))

    def patch(self, request, pk):
        device = DeviceModel.objects.get(id=pk)
        serializer = DeviceSerializer(device, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(default_response(serializer.data, "Change information successfully"))
        return Response(default_response(serializer.errors, "Change information failed, please try again"),
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        device = DeviceModel.objects.get(id=pk)
        device.delete()
        return Response(default_response({}, "Delete device successfully"), status=status.HTTP_204_NO_CONTENT)
