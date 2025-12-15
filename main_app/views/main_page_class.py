from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from auth_app.models import UsersData
from orders_app.models import OrdersData


class MainPageClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    def get(self, request):
        audio_play = self.request.GET.get('audio_play')
        order_db_id = self.request.GET.get('order_db_id')
        identification_code = self.request.GET.get('identification_code')
        user_orders_list = OrdersData.objects.filter(user_data=UsersData.objects.get(id=self.request.user.id), order_status=None, delete_status=False).exclude(order_title=None).order_by('-id')
        my_identification_code = UsersData.objects.get(id=self.request.user.id).my_identification_code
        return render(request, 'main_app/main_page.html', {'user_orders_list': user_orders_list, 'audio_play': audio_play, 'order_db_id': order_db_id, 'identification_code': identification_code, 'my_identification_code': my_identification_code})
