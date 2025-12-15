from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from auth_app.models import UsersData
from orders_app.models import SelectedAddressData


class SelectedAddressPageClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    def get(self, request):
        selected_adderss = SelectedAddressData.objects.filter(user_data=UsersData.objects.get(id=self.request.user.id)).order_by('-id')
        return render(request, 'main_app/selected_address_page.html', {'selected_adderss': selected_adderss})
