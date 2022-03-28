from django.db import models
from commons.models import BaseModel
from config.settings.base import AUTH_USER_MODEL


class RoomModel(BaseModel):
    name = models.CharField(max_length=255)
    owners = models.ManyToManyField(AUTH_USER_MODEL, related_name='room_permission')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'rooms'
        verbose_name_plural = 'Rooms'
