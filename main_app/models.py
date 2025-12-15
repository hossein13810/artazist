from django.db import models


class GarbageCategoriesData(models.Model):
    categories_name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.categories_name


class UnitsOfMeasurementData(models.Model):
    unit_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.unit_name


class GarbageData(models.Model):
    garbage_item_name = models.CharField(max_length=200, blank=True, null=True)
    units_of_measurement_data = models.CharField(max_length=200, blank=True, null=True)
    price_per_unit = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    garbage_icon = models.ImageField(blank=True, null=True, upload_to='garbage_icons')
    garbage_image = models.ImageField(blank=True, null=True, upload_to='garbage_images')
