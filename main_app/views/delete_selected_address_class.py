from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from auth_app.models import UsersData
from orders_app.models import SelectedAddressData


class DeleteSelectedAddressClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    def get(self, request):
        selected_adderss_id = self.request.GET.get('selected_adderss_id')
        SelectedAddressData.objects.get(id=selected_adderss_id).delete()
        messages.success(request, 'آدرس منتخب با موفقیت حذف شد')
        return redirect('SelectedAddressPageClass')
