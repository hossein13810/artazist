import time

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from admin_panel_app.views import OperationMessagesDataManagerClass
from admin_panel_app.views.functions.send_notification import send_notification
from auth_app.models import UsersData
from base_app.mixins import RoleRequiredMixin


class SendMessagePageClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['send_message_page']

    @staticmethod
    def get(request):
        users_list = UsersData.objects.filter(admin_permission=False, is_staff=False)
        return render(request, 'admin_panel_app/send_message_page.html', {'users_list': users_list})

    def post(self, request):
        users_list_select = self.request.POST.get('users_list_select')
        message_text_input = self.request.POST.get('message_text_input')
        send_mode_notif_input = self.request.POST.get('send_mode_notif_input')

        users_list = []
        if users_list_select != 'all':
            for user in users_list_select.split(','):
                users_list.append(user.split(' - ')[1][1:])
        else:
            users_list = list(UsersData.objects.filter(admin_permission=False, is_staff=False).values_list('phone_number', flat=True))

        if send_mode_notif_input == 'true':
            for user in users_list:
                status = send_notification(device_token=UsersData.objects.get(phone_number=user).device_token, message_text=message_text_input)
                OperationMessagesDataManagerClass.update_message(message_text=f'0{user} --- {status} --- اعلان')

        time.sleep(2)
        return HttpResponse('done')
