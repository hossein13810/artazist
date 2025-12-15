from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from auth_app.models import UserPermissions, UsersData
from base_app.mixins import RoleRequiredMixin


class FinancialRequestsListPageClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['financial_requests_list_page']

    def get(self, request):
        admin_permissions = list(UserPermissions.objects.filter(user_data=UsersData.objects.get(id=self.request.user.id)).values_list('permission_name', flat=True))
        write_financial_requests_list_page = 'write_financial_requests_list_page' in admin_permissions
        return render(request, 'admin_panel_app/financial_requests_list_page.html', {'write_financial_requests_list_page': write_financial_requests_list_page})
