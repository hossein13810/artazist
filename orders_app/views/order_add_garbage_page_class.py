from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from orders_app.models import OrderGarbagesData, OrdersData


class OrderAddGarbagePageClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    def get(self, request):
        access_token = self.request.GET.get('access_token')
        return render(request, 'orders_app/order_add_garbage_page.html', {'access_token': access_token})

    def post(self, request):
        access_token = self.request.POST.get('access_token')
        garbage_categories_select = self.request.POST.get('garbage_categories_select')
        garbage_item_select = self.request.POST.get('garbage_item_select')
        garbage_amount_input = self.request.POST.get('garbage_amount_input')
        description_input = self.request.POST.get('description_input')

        OrderGarbagesData.objects.create(order_data=OrdersData.objects.get(access_token=access_token), garbage_data_id=garbage_item_select, garbage_amount=garbage_amount_input, description=description_input)

        messages.success(request, 'زباله جدید با موفقیت به لیست اضافه شد')
        return redirect(f'/order_garbages_list_page/?access_token={access_token}')
