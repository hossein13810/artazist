import datetime

from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View

from auth_app.models import UsersData, UserPermissions


class AdminLoginPageClass(View):

    def get(self, request):
        if self.request.user.is_authenticated:
            user_data = UsersData.objects.get(id=self.request.user.id)
            permissions_page = finde_permission(user_data=user_data)
            return redirect(permissions_page)
        else:
            return render(request, 'admin_panel_app/admin_login_page.html')

    def post(self, request):
        username_input = self.request.POST.get('username_input')
        password_input = self.request.POST.get('password_input')

        if not UsersData.objects.filter(phone_number=username_input, password=password_input, admin_permission=True).exists():
            messages.error(request, 'اطلاعات وارد شده صحیح نیست')
            return redirect('AdminLoginPageClass')
        else:
            user_data = UsersData.objects.get(phone_number=username_input)
            login(self.request, user_data)
            user_data.user_last_login = datetime.datetime.now(datetime.timezone.utc)
            user_data.save()
            permissions_page = finde_permission(user_data=user_data)
            return redirect(permissions_page)


def finde_permission(user_data):
    permissions_page = None
    admin_permissions = list(UserPermissions.objects.filter(user_data=user_data).values_list('permission_name', flat=True))
    if 'orders_list_page' in admin_permissions:
        permissions_page = 'OrdersListPageClass'
    elif 'financial_requests_list_page' in admin_permissions:
        permissions_page = 'FinancialRequestsListPageClass'
    elif 'send_message_page' in admin_permissions:
        permissions_page = 'SendMessagePageClass'
    elif 'users_list_page' in admin_permissions:
        permissions_page = 'UsersListPageClass'

    return permissions_page
