from django.contrib import admin
from .models import DeviceCategoryModel, DeviceModel, DeviceHistoryModel


admin.site.register(DeviceCategoryModel)
admin.site.register(DeviceModel)
admin.site.register(DeviceHistoryModel)
