from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View

from base_app.mixins import RoleRequiredMixin
from main_app.models import GarbageData


class LoadGarbagesDataClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['orders_list_page']

    @staticmethod
    def post(request):
        garbages_data = GarbageData.objects.all().order_by('-id').values()
        return JsonResponse(list(garbages_data), safe=False)
