from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from auth_app.models import UsersData
from orders_app.models import OrdersData
from wallet_app.models import WalletsData


class SaveIdentificationCodeClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    def post(self, request):
        identification_code_input = self.request.POST.get('identification_code_input')
        if UsersData.objects.filter(identification_code=identification_code_input).exists():
            user_data = UsersData.objects.get(my_identification_code=identification_code_input)
            if identification_code_input != user_data.my_identification_code:
                wallet_data = WalletsData.objects.get(user_data=user_data)
                wallet_data.inventory = wallet_data.inventory + 10000
                wallet_data.save()

                my_data = UsersData.objects.get(id=self.request.user.id)
                my_data.set_identification_code = identification_code_input
                my_data.save()
        return redirect('MainPageClass')
