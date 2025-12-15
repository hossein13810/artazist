import datetime

from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View

from auth_app.models import UsersData
from wallet_app.models import WalletsData


class FillUserDataPageClass(View):
    def get(self, request):
        if self.request.session['register_user_data'] and 'code_verify' in self.request.session['register_user_data'] and self.request.session['register_user_data']['code_verify']:
            return render(request, 'auth_app/fill_user_data_page.html')
        else:
            return redirect('LoginPageClass')

    def post(self, request):
        firstname_input = self.request.POST.get('firstname_input')
        lastname_input = self.request.POST.get('lastname_input')
        national_code_input = self.request.POST.get('national_code_input')

        if UsersData.objects.filter(phone_number=self.request.session['register_user_data']['phone_number_input']).exists():
            messages.error(request, 'این شماره قبلا استفاده شده است')
            return redirect('LoginPageClass')
        elif UsersData.objects.filter(national_code=national_code_input).exists():
            messages.error(request, 'این کد ملی قبلا استفاده شده است')
            return redirect('FillUserDataPageClass')
        else:
            user_data = UsersData.objects.create(user_firstname=firstname_input, user_lastname=lastname_input, phone_number=self.request.session['register_user_data']['phone_number_input'], national_code=national_code_input, device_token=self.request.session['device_token'])
            login(self.request, user_data)
            user_data.user_last_login = datetime.datetime.now(datetime.timezone.utc)
            user_data.save()
            if not WalletsData.objects.filter(user_data=user_data).exists():
                WalletsData.objects.create(user_data=user_data, inventory=0)
            messages.success(request, 'حساب شما با موفقیت ایجاد شد')
            return redirect('MainPageClass')
