from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from orders_app.models import OrderGarbagesData, OrdersData


class CancelOrderClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    def get(self, request):
        text = self.request.GET.get('text')
        order_db_id = self.request.GET.get('order_db_id')
        order_data = OrdersData.objects.get(id=order_db_id)
        order_data.delete_status = True
        order_data.delete_text = text
        order_data.save()

        messages.success(request, 'درخواست، با موفقیت لغو شد')
        return redirect('MainPageClass')

