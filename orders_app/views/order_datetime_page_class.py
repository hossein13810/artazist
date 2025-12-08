import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from persiantools.jdatetime import JalaliDate
from orders_app.models import OrderGarbagesData, OrdersData


class OrderDatetimePageClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    def get(self, request):
        access_token = self.request.GET.get('access_token')
        return render(request, 'orders_app/order_datetime_page.html', {'access_token': access_token})

    def post(self, request):
        access_token_input = self.request.POST.get('access_token_input')
        order_title_input = self.request.POST.get('order_title_input')
        order_description_input = self.request.POST.get('order_description_input')
        datepicker_from_input = fa_to_en_digits(self.request.POST.get('datepicker_from_input'))
        datepicker_to_input = fa_to_en_digits(self.request.POST.get('datepicker_to_input'))

        year_from, month_from, day_from = map(int, datepicker_from_input.split("/"))
        year_to, month_to, day_to = map(int, datepicker_to_input.split("/"))
        gregorian_date_from = JalaliDate(year_from, month_from, day_from).to_gregorian()
        gregorian_date_to = JalaliDate(year_to, month_to, day_to).to_gregorian()

        datetime_from = datetime.datetime(gregorian_date_from.year, gregorian_date_from.month, gregorian_date_from.day).date()
        datetime_to = datetime.datetime(gregorian_date_to.year, gregorian_date_to.month, gregorian_date_to.day).date()
        order_data = OrdersData.objects.get(access_token=access_token_input)
        order_data.order_title = order_title_input
        order_data.order_from_date = datetime_from
        order_data.order_to_date = datetime_to
        order_data.description = order_description_input
        order_data.save()

        messages.success(request, 'درخواست شما با موفقیت ثبت شد')
        return redirect('MainPageClass')


def fa_to_en_digits(s):
    fa_digits = "۰۱۲۳۴۵۶۷۸۹"
    en_digits = "0123456789"
    trans_table = str.maketrans(''.join(fa_digits), ''.join(en_digits))
    return s.translate(trans_table)
