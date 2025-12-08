from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from base_app.functions.send_sms import send_sms
from base_app.mixins import RoleRequiredMixin
from orders_app.models import OrdersData


class SaveOrderStatusClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['orders_list_page', 'write_orders_list_page']

    def get(self, request):
        access_token = self.request.GET.get('access_token')

        order_data = OrdersData.objects.get(access_token=access_token)
        order_data.order_status = False

        order_data.save()
        messages.success(request, 'وضعیت درخواست با موفقیت تغییر یافت')
        return redirect('OrdersListPageClass')
