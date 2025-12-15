from django.contrib import admin

from main_app.models import GarbageCategoriesData, UnitsOfMeasurementData, GarbageData

admin.site.register(GarbageCategoriesData)
admin.site.register(UnitsOfMeasurementData)
admin.site.register(GarbageData)
