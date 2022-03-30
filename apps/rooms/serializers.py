from rest_framework import serializers
from .models import RoomModel


class RoomSerializer(serializers.ModelSerializer):
    device_counter = serializers.SerializerMethodField()
    owner_counter = serializers.SerializerMethodField()

    def get_device_counter(self, obj):
        return obj.device_room.count()

    def get_owner_counter(self, obj):
        return obj.owners.count()

    class Meta:
        model = RoomModel
        fields = ('id', 'name', 'owners', 'device_counter', 'owner_counter')
