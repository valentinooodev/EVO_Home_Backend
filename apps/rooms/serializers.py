from rest_framework import serializers
from .models import RoomModel


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomModel
        fields = ('id', 'name', 'owners')
