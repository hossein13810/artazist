from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from base_app.mixins import RoleRequiredMixin
from orders_app.models import OrdersData, OrderGarbagesData


class OrdersDetailsPageClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['orders_list_page']

    def get(self, request):
        access_token = self.request.GET.get('access_token')
        order_data = OrdersData.objects.get(access_token=access_token)
        order_garbages_list = OrderGarbagesData.objects.filter(order_data=order_data)
        return render(request, 'admin_panel_app/orders_details_page.html', {'order_data': order_data, 'order_garbages_list': order_garbages_list})
