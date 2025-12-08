from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from auth_app.models import UsersData, UserPermissions
from base_app.mixins import RoleRequiredMixin
from wallet_app.models import WalletsData


class CreateAdminPageClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['users_list_page', 'write_admins_list_page']

    @staticmethod
    def get(request):
        return render(request, 'admin_panel_app/create_admin_page.html')

    def post(self, request):
        firstname_input = self.request.POST.get('firstname_input')
        lastname_input = self.request.POST.get('lastname_input')
        phone_number_input = self.request.POST.get('phone_number_input')
        national_code_input = self.request.POST.get('national_code_input')
        password_input = self.request.POST.get('password_input')

        orders_list_page_check = self.request.POST.get('orders_list_page_check')
        write_orders_list_page_check = self.request.POST.get('write_orders_list_page_check')

        financial_requests_list_page_check = self.request.POST.get('financial_requests_list_page_check')
        write_financial_requests_list_page_check = self.request.POST.get('write_financial_requests_list_page_check')

        send_message_page_check = self.request.POST.get('send_message_page_check')

        users_list_page_check = self.request.POST.get('users_list_page_check')

        admins_list_page_check = self.request.POST.get('admins_list_page_check')
        write_admins_list_page_check = self.request.POST.get('write_admins_list_page_check')

        data_definition_page_check = self.request.POST.get('data_definition_page_check')
        write_data_definition_page_check = self.request.POST.get('write_data_definition_page_check')

        if len(UsersData.objects.filter(admin_permission=True)) <= 7:
            if UsersData.objects.filter(phone_number=phone_number_input).exists():
                messages.error(request, 'یک کاربر با این شماره موبایل وجود دارد')
                return redirect('CreateAdminPageClass')
            elif UsersData.objects.filter(national_code=national_code_input).exists():
                messages.error(request, 'یک کاربر با این کد ملی وجود دارد')
                return redirect('CreateAdminPageClass')
            else:
                user_data = UsersData.objects.create(user_firstname=firstname_input, user_lastname=lastname_input, phone_number=phone_number_input, national_code=national_code_input, password=password_input, admin_permission=True)

                if orders_list_page_check == 'on':
                    if not UserPermissions.objects.filter(user_data=user_data, permission_name='orders_list_page').exists():
                        UserPermissions.objects.create(user_data=user_data, permission_name='orders_list_page')
                    if write_orders_list_page_check == 'on':
                        if not UserPermissions.objects.filter(user_data=user_data, permission_name='write_orders_list_page').exists():
                            UserPermissions.objects.create(user_data=user_data, permission_name='write_orders_list_page')

                if financial_requests_list_page_check == 'on':
                    if not UserPermissions.objects.filter(user_data=user_data, permission_name='financial_requests_list_page').exists():
                        UserPermissions.objects.create(user_data=user_data, permission_name='financial_requests_list_page')
                    if write_financial_requests_list_page_check == 'on':
                        if not UserPermissions.objects.filter(user_data=user_data, permission_name='write_financial_requests_list_page').exists():
                            UserPermissions.objects.create(user_data=user_data, permission_name='write_financial_requests_list_page')

                if send_message_page_check == 'on':
                    if not UserPermissions.objects.filter(user_data=user_data, permission_name='send_message_page').exists():
                        UserPermissions.objects.create(user_data=user_data, permission_name='send_message_page')

                if users_list_page_check == 'on':
                    if not UserPermissions.objects.filter(user_data=user_data, permission_name='users_list_page').exists():
                        UserPermissions.objects.create(user_data=user_data, permission_name='users_list_page')

                if admins_list_page_check == 'on':
                    if not UserPermissions.objects.filter(user_data=user_data, permission_name='admins_list_page').exists():
                        UserPermissions.objects.create(user_data=user_data, permission_name='admins_list_page')
                    if write_admins_list_page_check == 'on':
                        if not UserPermissions.objects.filter(user_data=user_data, permission_name='write_admins_list_page').exists():
                            UserPermissions.objects.create(user_data=user_data, permission_name='write_admins_list_page')

                if data_definition_page_check == 'on':
                    if not UserPermissions.objects.filter(user_data=user_data, permission_name='data_definition_page').exists():
                        UserPermissions.objects.create(user_data=user_data, permission_name='data_definition_page')
                    if write_data_definition_page_check == 'on':
                        if not UserPermissions.objects.filter(user_data=user_data, permission_name='write_data_definition_page').exists():
                            UserPermissions.objects.create(user_data=user_data, permission_name='write_data_definition_page')

                text = 'مدیر جدید با موفقیت ایجاد شد'
                user_data.save()

                messages.success(request, text)
                return redirect('AdminsListPageClass')
        else:
            return redirect('AdminsListPageClass')
