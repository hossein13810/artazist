from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from auth_app.models import UsersData, UserPermissions
from base_app.mixins import RoleRequiredMixin
from main_app.models import GarbageCategoriesData, UnitsOfMeasurementData
from wallet_app.models import WalletsData


class EditUnitPageClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['data_definition_page']

    def get(self, request):
        unit_id = self.request.GET.get('unit_id')
        unit_data = UnitsOfMeasurementData.objects.get(id=unit_id)
        return render(request, 'admin_panel_app/edit_unit_page.html', {'unit_data': unit_data})

    def post(self, request):
        unit_id = self.request.POST.get('unit_id')
        unit_name_input = self.request.POST.get('unit_name_input')

        if UnitsOfMeasurementData.objects.filter(unit_name=unit_name_input).exclude(id=unit_id).exists():
            messages.error(request, 'یک واحد با این نام وجود دارد')
            return redirect(f'/edit_unit_page/?unit_id={unit_id}')
        else:
            unit_data = UnitsOfMeasurementData.objects.get(id=unit_id)
            unit_data.unit_name = unit_name_input
            unit_data.save()
            messages.success(request, 'واحد با موفقیت ویرایش شد')
            return redirect('DataDefinitionGarbagesDataPageClass')
