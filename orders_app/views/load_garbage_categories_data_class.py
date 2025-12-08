from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View

from main_app.models import GarbageCategoriesData


class LoadGarbageCategoriesDataClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    @staticmethod
    def post(request):
        garbage_categories_data = GarbageCategoriesData.objects.all().values()

        return JsonResponse(list(garbage_categories_data), safe=False)
