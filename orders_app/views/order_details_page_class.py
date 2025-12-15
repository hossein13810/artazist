from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from orders_app.models import OrderGarbagesData, OrdersData


class OrderDetailsPageClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    def get(self, request):
        access_token = self.request.GET.get('access_token')
        order_data = OrdersData.objects.get(access_token=access_token)
        order_garbages_data = OrderGarbagesData.objects.filter(order_data=order_data)
        return render(request, 'orders_app/order_details_page.html', {'order_data': order_data, 'order_garbages_data': order_garbages_data})
