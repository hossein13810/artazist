from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from auth_app.models import UsersData
from orders_app.models import OrdersData


class MyOrdersHistoryPageClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    def get(self, request):
        user_orders_list = OrdersData.objects.filter(user_data=UsersData.objects.get(id=self.request.user.id)).order_by('-id')
        return render(request, 'orders_app/my_orders_history_page.html', {'user_orders_list': user_orders_list})
