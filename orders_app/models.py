import jdatetime
from django.db import models

from auth_app.models import UsersData
from main_app.models import GarbageData


class OrdersData(models.Model):
    user_data = models.ForeignKey(UsersData, null=True, blank=True, on_delete=models.CASCADE)
    order_title = models.CharField(max_length=200, null=True, blank=True)
    order_map_lat_location = models.FloatField(null=True, blank=True)
    order_map_lng_location = models.FloatField(null=True, blank=True)
    access_token = models.CharField(max_length=200, null=True, blank=True)
    order_date = models.DateField(null=True, blank=True)
    order_from_time = models.TimeField(null=True, blank=True)
    order_to_time = models.TimeField(null=True, blank=True)
    created_datetime = models.DateTimeField(null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    order_status = models.BooleanField(blank=True, null=True)
    delete_status = models.BooleanField(blank=True, null=True, default=False)
    delete_text = models.TextField(blank=True, null=True)

    def get_jalali_created_datetime(self):
        jdate = jdatetime.date.fromgregorian(date=self.created_datetime)
        days = ["شنبه", "یک‌شنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه"]
        months = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]

        day_name = days[jdate.weekday()]
        month_name = months[jdate.month - 1]

        return f"{day_name} {jdate.day} {month_name}"

    def get_jalali_order_timeline(self):
        return f'{self.order_from_time.hour} تا {self.order_to_time.hour}'

    def get_str_order_date(self):
        jdate = jdatetime.date.fromgregorian(date=self.order_date)
        days = ["شنبه", "یک‌شنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه"]
        months = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]

        day_name = days[jdate.weekday()]
        month_name = months[jdate.month - 1]

        return f"{day_name} {jdate.day} {month_name}"


class OrderGarbagesData(models.Model):
    order_data = models.ForeignKey(OrdersData, null=True, blank=True, on_delete=models.CASCADE)
    garbage_data = models.ForeignKey(GarbageData, null=True, blank=True, on_delete=models.CASCADE)
    garbage_amount = models.IntegerField(null=True, blank=True)


class SelectedAddressData(models.Model):
    user_data = models.ForeignKey(UsersData, null=True, blank=True, on_delete=models.CASCADE)
    address_title = models.CharField(max_length=200, null=True, blank=True)
    address_text = models.TextField(null=True, blank=True)
    coords_lat = models.CharField(max_length=200, null=True, blank=True)
    coords_lng = models.CharField(max_length=200, null=True, blank=True)
