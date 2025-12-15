import json
from collections import OrderedDict
from datetime import datetime, timedelta

import jdatetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from admin_panel_app.models import WithdrawalsData
from base_app.mixins import RoleRequiredMixin


class FinancialChartShowPageClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['financial_requests_list_page']

    @staticmethod
    def get(request):
        return render(request, 'admin_panel_app/financial_chart_show_page.html')

    def post(self, request):
        order_date_filter = self.request.POST.get('order_date_filter')
        order_date_filter = json.loads(order_date_filter)
        withdrawals_data = WithdrawalsData.objects.all()
        pay_error = 0
        pay_false = 0
        pay_true = 0
        for withdrawal in withdrawals_data:
            if withdrawal.status is None:
                pay_false += 1
            elif withdrawal.status:
                pay_true += 1
            elif not withdrawal.status:
                pay_error += 1

        # -------------------------------------------------------------------------------------------
        start_jalali = order_date_filter[0]
        end_jalali = order_date_filter[1]

        start_date = self.jalali_to_gregorian(start_jalali)
        end_date = self.jalali_to_gregorian(end_jalali)

        delta_days = (end_date - start_date).days
        days = [start_date + timedelta(days=i) for i in range(delta_days + 1)]

        result = OrderedDict()

        for day in days:
            day_start = datetime.combine(day, datetime.min.time())
            day_end = datetime.combine(day, datetime.max.time())

            withdrawals = WithdrawalsData.objects.filter(
                request_datetime__range=(day_start, day_end)
            )

            count_true = withdrawals.filter(status=True).count()
            count_false = withdrawals.filter(status=False).count()
            count_none = withdrawals.filter(status__isnull=True).count()

            jdate = jdatetime.date.fromgregorian(date=day)
            formatted_date = f"{jdate.year}/{jdate.month:02}/{jdate.day:02}"

            result[formatted_date] = [count_none, count_true, count_false]

        charts_data_dict = {
            'circle_chart_data': [pay_false, pay_true, pay_error],
            'bar_chart_data': dict(result)
        }

        return JsonResponse(charts_data_dict)

    @staticmethod
    def jalali_to_gregorian(jdate_str):
        y, m, d = map(int, jdate_str.split('/'))
        return jdatetime.date(y, m, d).togregorian()
