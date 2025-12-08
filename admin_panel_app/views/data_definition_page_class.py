from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F, OuterRef, Subquery, Count
from django.shortcuts import render
from django.views import View

from auth_app.models import UsersData, UserPermissions
from base_app.mixins import RoleRequiredMixin
from main_app.models import GarbageData, GarbageCategoriesData, UnitsOfMeasurementData
from wallet_app.models import WalletsData


class DataDefinitionGarbagesDataPageClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['data_definition_page']

    def get(self, request):
        garbages_data = GarbageData.objects.all().order_by('-id')
        garbage_categories_data = GarbageCategoriesData.objects.all().order_by('-id')
        units_of_measurement_data = UnitsOfMeasurementData.objects.all().order_by('-id')
        admin_permissions = list(UserPermissions.objects.filter(user_data=UsersData.objects.get(id=self.request.user.id)).values_list('permission_name', flat=True))
        write_data_definition_page = 'write_data_definition_page' in admin_permissions
        return render(request, 'admin_panel_app/data_definition_garbages_data_page.html', {'garbages_data': garbages_data, 'garbage_categories_data': garbage_categories_data, 'units_of_measurement_data': units_of_measurement_data, 'write_data_definition_page': write_data_definition_page})
