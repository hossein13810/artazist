from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F, OuterRef, Subquery, Count
from django.shortcuts import render
from django.views import View

from auth_app.models import UsersData, UserPermissions
from base_app.mixins import RoleRequiredMixin
from wallet_app.models import WalletsData


class AdminsListPageClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['admins_list_page']

    def get(self, request):
        admin_permissions = list(UserPermissions.objects.filter(user_data=UsersData.objects.get(id=self.request.user.id)).values_list('permission_name', flat=True))
        print(admin_permissions)
        write_admins_list_page = 'write_admins_list_page' in admin_permissions
        admins_list = UsersData.objects.filter(master_of_admins=False, is_staff=False, admin_permission=True).exclude(id=self.request.user.id)
        return render(request, 'admin_panel_app/admins_list_page.html', {'admins_list': admins_list, 'write_admins_list_page': write_admins_list_page})
