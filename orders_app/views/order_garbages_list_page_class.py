from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from orders_app.models import OrderGarbagesData


class OrderGarbagesListPageClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    def get(self, request):
        access_token = self.request.GET.get('access_token')
        order_garbages_data = OrderGarbagesData.objects.filter(order_data__access_token=access_token).order_by('-id')
        return render(request, 'orders_app/order_garbages_list_page.html', {'access_token': access_token, 'order_garbages_data': order_garbages_data})
