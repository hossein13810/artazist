from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from auth_app.models import UsersData, UserPermissions
from base_app.mixins import RoleRequiredMixin
from main_app.models import GarbageCategoriesData, UnitsOfMeasurementData
from wallet_app.models import WalletsData


class CreateUnitPageClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['data_definition_page']

    @staticmethod
    def get(request):
        return render(request, 'admin_panel_app/create_unit_page.html')

    def post(self, request):
        unit_name_input = self.request.POST.get('unit_name_input')

        if UnitsOfMeasurementData.objects.filter(unit_name=unit_name_input).exists():
            messages.error(request, 'یک واحد با این نام وجود دارد')
            return redirect('CreateUnitPageClass')
        else:
            UnitsOfMeasurementData.objects.create(unit_name=unit_name_input)
            messages.success(request, 'واحد جدید با موفقیت ایجاد شد')
            return redirect('DataDefinitionGarbagesDataPageClass')
