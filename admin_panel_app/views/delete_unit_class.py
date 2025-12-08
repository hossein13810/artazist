from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from auth_app.models import UsersData, UserPermissions
from base_app.mixins import RoleRequiredMixin
from main_app.models import UnitsOfMeasurementData
from wallet_app.models import WalletsData


class DeleteUnitClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['data_definition_page']

    def get(self, request):
        unit_id = self.request.GET.get('unit_id')
        UnitsOfMeasurementData.objects.get(id=unit_id).delete()
        messages.success(request, 'حذف واحد با موفقیت انجام شد')
        return redirect('DataDefinitionGarbagesDataPageClass')
