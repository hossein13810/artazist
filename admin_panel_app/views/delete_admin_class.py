from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from auth_app.models import UsersData, UserPermissions
from base_app.mixins import RoleRequiredMixin
from wallet_app.models import WalletsData


class DeleteAdminClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['admins_list_page', 'write_admins_list_page']

    def get(self, request):
        user_id = self.request.GET.get('user_id')
        UsersData.objects.get(id=user_id).delete()
        messages.success(request, 'حذف مدیر با موفقیت انجام شد')
        return redirect('AdminsListPageClass')
