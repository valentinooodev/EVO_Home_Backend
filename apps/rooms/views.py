from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.response import Response
from .models import RoomModel
from .serializers import RoomSerializer
from commons.response import default_response


class RoomListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RoomSerializer

    def get(self, request):
        rooms = request.user.room_permission.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(default_response(serializer.data))