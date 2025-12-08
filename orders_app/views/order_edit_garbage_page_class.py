from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from main_app.models import GarbageData
from orders_app.models import OrderGarbagesData, OrdersData


class OrderEditGarbagePageClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    def get(self, request):
        access_token = self.request.GET.get('access_token')
        garbage_db_id = self.request.GET.get('garbage_db_id')
        garbage_db_data = OrderGarbagesData.objects.get(id=garbage_db_id)
        return render(request, 'orders_app/order_edit_garbage_page.html', {'access_token': access_token, 'garbage_db_data': garbage_db_data})

    def post(self, request):
        access_token = self.request.POST.get('access_token')
        order_garbage_db_id = self.request.POST.get('order_garbage_db_id_input')
        garbage_item_select = self.request.POST.get('garbage_item_select')
        garbage_amount_input = self.request.POST.get('garbage_amount_input')
        description_input = self.request.POST.get('description_input')

        order_garbage_db_data = OrderGarbagesData.objects.get(id=order_garbage_db_id)
        order_garbage_db_data.garbage_data = GarbageData.objects.get(id=garbage_item_select)
        order_garbage_db_data.garbage_amount = garbage_amount_input
        order_garbage_db_data.description = description_input
        order_garbage_db_data.save()

        messages.success(request, 'زباله انتخاب شده با موفقیت ویرایش شد')
        return redirect(f'/order_garbages_list_page/?access_token={access_token}')
