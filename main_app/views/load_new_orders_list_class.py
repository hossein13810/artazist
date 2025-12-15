from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from auth_app.models import UsersData
from orders_app.models import OrdersData


class LoadNewOrdersListClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    def post(self, request):
        user_orders_list = OrdersData.objects.filter(user_data=UsersData.objects.get(id=self.request.user.id), order_status=None, delete_status=False).exclude(order_title=None).order_by('-id')
        data_list = []
        for order in user_orders_list:
            data_list.append({
                'id': order.id,
                'access_token': order.access_token,
                'order_date': order.get_str_order_date(),
                'timeline': order.get_jalali_order_timeline(),
                'order_status': order.order_status,
                'address': order.address,
            })
        return JsonResponse(data_list, safe=False)
