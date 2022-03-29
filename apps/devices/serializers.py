from rest_framework import serializers
from .models import DeviceCategoryModel, DeviceModel, DeviceHistoryModel


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceModel
        fields = ('id', 'name', 'status', 'data', 'category', 'room')


class DeviceHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceHistoryModel
        fields = ('device', 'data')
        