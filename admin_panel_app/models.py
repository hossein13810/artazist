import jdatetime
from django.db import models

from wallet_app.models import WalletsData


class SourcesData(models.Model):
    kavenegar_access_hash = models.CharField(max_length=200, blank=True, null=True)


class WithdrawalsData(models.Model):
    wallet_data = models.ForeignKey(WalletsData, blank=True, null=True, on_delete=models.CASCADE)
    withdrawal_amount = models.IntegerField(blank=True, null=True)
    request_datetime = models.DateTimeField(blank=True, null=True)
    pay_datetime = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)

    def get_jalali_request_datetime(self):
        jdate = jdatetime.date.fromgregorian(date=self.request_datetime)
        months = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]

        month_name = months[jdate.month - 1]

        return f"{jdate.day} {month_name} {jdate.year}"

    def get_jalali_pay_datetime(self):
        jdate = jdatetime.date.fromgregorian(date=self.pay_datetime)
        months = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]

        month_name = months[jdate.month - 1]

        return f"{jdate.day} {month_name} {jdate.year}"


class OperationMessagesData(models.Model):
    message_text = models.CharField(max_length=200, blank=True, null=True)
    message_send = models.BooleanField(blank=True, null=True, default=False)
