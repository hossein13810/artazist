from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from orders_app.models import OrderGarbagesData, OrdersData


class OrderDeleteGarbageClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    def get(self, request):
        access_token = self.request.GET.get('access_token')
        order_garbage_db_id = self.request.GET.get('order_garbage_db_id')
        OrderGarbagesData.objects.get(id=order_garbage_db_id).delete()

        messages.success(request, 'زباله، با موفقیت از لیست حذف شد')
        return redirect(f'/order_garbages_list_page/?access_token={access_token}')

