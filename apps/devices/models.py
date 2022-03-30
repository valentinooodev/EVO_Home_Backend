from django.db import models
from commons.models import BaseModel
from apps.rooms.models import RoomModel


class DeviceCategoryModel(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'device_categories'
        verbose_name_plural = 'Device Categories'
        ordering = ('-created_at',)


class DeviceModel(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    status = models.BooleanField(default=False)
    data = models.TextField(null=True, blank=True)
    category = models.ForeignKey(DeviceCategoryModel, on_delete=models.CASCADE, related_name='device_category')
    is_sensor = models.BooleanField(default=False)
    room = models.ForeignKey(RoomModel, on_delete=models.CASCADE, related_name='device_room')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'devices'
        verbose_name_plural = 'Devices'
        ordering = ('-created_at',)


class DeviceHistoryModel(BaseModel):
    device = models.ForeignKey(DeviceModel, on_delete=models.CASCADE, related_name='device_history')
    data = models.TextField()

    def __str__(self):
        return f'{self.device} - {self.updated_at} - {self.data}'

    class Meta:
        db_table = 'device_histories'
        verbose_name_plural = 'Device Histories'
        ordering = ('-created_at',)
