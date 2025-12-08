import base64
import datetime
import random
import string

import jdatetime
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.views import View

from auth_app.models import UsersData
from base_app.functions.send_sms import send_sms
from orders_app.models import OrdersData, SelectedAddressData


class OrderMapPageClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    def get(self, request):
        selected_address_data = SelectedAddressData.objects.filter(user_data=UsersData.objects.get(id=self.request.user.id))
        return render(request, 'orders_app/order_map_page.html', {'selected_address_data': selected_address_data})

    def post(self, request):
        coords_lat_input = self.request.POST.get('coords_lat_input')
        coords_lng_input = self.request.POST.get('coords_lng_input')
        loc_address_input = self.request.POST.get('loc_address_input')
        date_input = self.request.POST.get('date_input')
        timeline_input = self.request.POST.get('timeline_input')
        from_time = f'{timeline_input.split("_")[0]}:00'
        to_time = f'{timeline_input.split("_")[1]}:00'

        year, month, day = map(int, date_input.split('/'))
        jalali_date = jdatetime.date(year, month, day)
        gregorian_date = jalali_date.togregorian()

        while True:
            random_str = generate_random_string()
            if OrdersData.objects.filter(access_token=random_str).exists():
                continue
            else:
                break

        order_title = f'درخواست {len(OrdersData.objects.filter(user_data=UsersData.objects.get(id=self.request.user.id))) + 1}'
        order_db_id = OrdersData.objects.create(user_data=UsersData.objects.get(id=self.request.user.id), order_map_lat_location=coords_lat_input, order_map_lng_location=coords_lng_input, access_token=random_str, order_title=order_title, address=loc_address_input, order_date=gregorian_date, order_from_time=from_time, order_to_time=to_time, created_datetime=datetime.datetime.now(datetime.timezone.utc))

        send_sms(phone_number=order_db_id.user_data.phone_number, message=f'با سلام.\nدرخواست شما در «آرتازیست پلاس» به شماره پیگیری "{order_db_id.access_token}" با موفقیت ثبت شد.\n')

        return redirect(f'/main_page/?audio_play=play&order_db_id={order_db_id.id}')


def generate_random_string(length=6):
    characters = string.digits
    return ''.join(random.choices(characters, k=length))
