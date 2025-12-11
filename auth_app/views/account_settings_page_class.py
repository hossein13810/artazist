from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from auth_app.models import UsersData
from wallet_app.models import WalletsData


class AccountSettingsPageClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    def get(self, request):
        user_data = UsersData.objects.get(id=self.request.user.id)
        return render(request, 'auth_app/account_settings_page.html', {'user_data': user_data})

    def post(self, request):
        firstname_input = self.request.POST.get('firstname_input')
        lastname_input = self.request.POST.get('lastname_input')
        national_code_input = self.request.POST.get('national_code_input')
        identification_code_input = self.request.POST.get('identification_code_input')
        home_address_input = self.request.POST.get('home_address_input')

        user_data = UsersData.objects.get(id=self.request.user.id)
        user_data.user_firstname = firstname_input
        user_data.user_lastname = lastname_input
        user_data.national_code = national_code_input
        user_data.home_address = home_address_input
        if identification_code_input != '' and identification_code_input != user_data.my_identification_code:
            friend_data = UsersData.objects.get(my_identification_code=identification_code_input)
            wallet_data = WalletsData.objects.get(user_data=friend_data)
            wallet_data.inventory = wallet_data.inventory + 10000
            wallet_data.save()
            user_data.set_identification_code = identification_code_input
        user_data.save()

        messages.success(request, 'اطلاعات جدید حساب شما با موفقیت ذخیره شد')
        return redirect('AccountSettingsPageClass')
