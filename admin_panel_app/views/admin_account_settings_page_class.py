from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from auth_app.models import UsersData, UserPermissions
from base_app.mixins import RoleRequiredMixin
from wallet_app.models import WalletsData


class AdminAccountSettingsPageClass(LoginRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'

    def get(self, request):
        user_data = UsersData.objects.get(id=self.request.user.id)
        return render(request, 'admin_panel_app/admin_account_settings_page.html', {'user_data': user_data})

    def post(self, request):
        firstname_input = self.request.POST.get('firstname_input')
        lastname_input = self.request.POST.get('lastname_input')
        password_input = self.request.POST.get('password_input')
        user_data = UsersData.objects.get(id=self.request.user.id)
        user_data.user_firstname = firstname_input
        user_data.user_lastname = lastname_input

        if password_input != '':
            user_data.password = password_input

        user_data.save()

        messages.success(request, 'ویرایش حساب با موفقیت انجام شد')
        return redirect('AdminAccountSettingsPageClass')
