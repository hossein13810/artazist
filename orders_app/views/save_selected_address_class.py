from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View

from auth_app.models import UsersData
from orders_app.models import SelectedAddressData, OrdersData


class SaveSelectedAddressClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    def post(self, request):
        order_db_id = self.request.POST.get('order_db_id')
        order_db_data = OrdersData.objects.get(id=order_db_id)
        selected_address_title_input = self.request.POST.get('selected_address_title_input')
        SelectedAddressData.objects.create(user_data=UsersData.objects.get(id=self.request.user.id), address_title=selected_address_title_input, coords_lat=order_db_data.order_map_lat_location, coords_lng=order_db_data.order_map_lng_location, address_text=order_db_data.address)

        messages.success(request, 'آدرس منتخب با موفقیت ذخیره شد')
        return redirect('MainPageClass')
