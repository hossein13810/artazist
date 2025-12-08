from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View

from admin_panel_app.models import OperationMessagesData
from base_app.mixins import RoleRequiredMixin


class OperationMessagesDataManagerClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['send_message_page']

    @staticmethod
    def get(request):
        message_text = None
        last_message = OperationMessagesData.objects.filter(message_send=False).last()
        if last_message:
            message_text = last_message.message_text
            last_message.message_send = True
            last_message.save()

        return HttpResponse(message_text)

    @staticmethod
    def update_message(message_text):
        OperationMessagesData.objects.create(message_text=message_text)
