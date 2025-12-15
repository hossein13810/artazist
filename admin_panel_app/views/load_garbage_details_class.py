from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View

from base_app.mixins import RoleRequiredMixin
from main_app.models import GarbageData


class LoadGarbageDetailsClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['orders_list_page']

    def post(self, request):
        garbage_db_id = self.request.POST.get('garbage_db_id')
        garbage_details_data = GarbageData.objects.get(id=garbage_db_id)
        return JsonResponse(garbage_details_data, safe=False)
