import datetime
import random

from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View

from auth_app.models import CreateNewUserData, UsersData
from wallet_app.models import WalletsData


class VerifyCodePageClass(View):
    def get(self, request):
        if self.request.session['register_user_data'] and 'phone_number_input' in self.request.session['register_user_data'] and self.request.session['register_user_data']['phone_number_input'] is not None:
            return render(request, 'auth_app/verify_code_page.html')

    def post(self, request):
        random_code_input = self.request.POST.get('random_code_input')
        random_code_db = CreateNewUserData.objects.get(id=self.request.session['register_user_data']['create_new_user_data'])
        if random_code_input != random_code_db.user_random_code:
            create_new_user_data = CreateNewUserData.objects.get(id=self.request.session['register_user_data']['create_new_user_data'])
            if create_new_user_data.try_count >= 3:
                create_new_user_data.try_count = 3
                create_new_user_data.save()
                messages.error(request, 'تلاش بیش از حد! لطفا دوباره تلاش کنید')
                return redirect('LoginPageClass')
            else:
                create_new_user_data.try_count += 1
                create_new_user_data.save()
                messages.error(request, 'کد وارد شده اشتباه است')
                return redirect('VerifyCodePageClass')
        else:
            if UsersData.objects.filter(phone_number=self.request.session['register_user_data']['phone_number_input']).exists():
                user_data = UsersData.objects.get(phone_number=self.request.session['register_user_data']['phone_number_input'])
                identification_code = 'false'
            else:
                while True:
                    my_identification_code = random.randint(12345, 98765)
                    if not UsersData.objects.filter(my_identification_code=my_identification_code).exists():
                        break
                user_data = UsersData.objects.create(phone_number=self.request.session['register_user_data']['phone_number_input'], device_token=self.request.session['device_token'], my_identification_code=my_identification_code)
                if not WalletsData.objects.filter(user_data=user_data).exists():
                    WalletsData.objects.create(user_data=user_data, inventory=0)
                identification_code = 'true'

            login(self.request, user_data)
            user_data.user_last_login = datetime.datetime.now(datetime.timezone.utc)
            user_data.save()
            return redirect(f'/main_page/?identification_code={identification_code}')
