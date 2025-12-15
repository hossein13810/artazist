import datetime
import random

import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from admin_panel_app.models import SourcesData
from auth_app.models import UsersData, CreateNewUserData
from base_app.functions.send_sms import send_sms


class LoginPageClass(View):
    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('MainPageClass')
        else:
            return render(request, 'auth_app/login_page.html')

    def post(self, request):
        phone_number_input = self.request.POST.get('phone_number_input')

        time_send_access = True
        if CreateNewUserData.objects.filter(user_phone_number=phone_number_input).exists():
            create_new_user_data = CreateNewUserData.objects.filter(user_phone_number=phone_number_input).last()
            if (datetime.datetime.now(datetime.timezone.utc) - create_new_user_data.send_time).seconds <= 120:
                time_send_access = False

        if not time_send_access:
            messages.error(request, 'لطفا پس از گذشت 2 دقیقه دوباره تلاش کنید')
            return redirect('LoginPageClass')
        else:
            random_code = random.randint(12345, 98765)
            create_new_user_data = CreateNewUserData.objects.create(user_phone_number=phone_number_input, user_random_code=random_code, send_time=datetime.datetime.now(datetime.timezone.utc), try_count=0)

            self.request.session['register_user_data'] = {
                'phone_number_input': phone_number_input,
                'create_new_user_data': create_new_user_data.id,
                'code_verify': False
            }

            send_sms(phone_number=phone_number_input, message=f'با سلام\n به «آرتازیست پلاس» خوش آمدید؛\n لطفا این کد را در اختیار دیگران قرار ندهید: {random_code}')
            return render(request, 'auth_app/verify_code_page.html', {'phone_number_input': phone_number_input})
