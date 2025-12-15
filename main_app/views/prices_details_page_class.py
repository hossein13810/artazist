from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from main_app.models import GarbageData, GarbageCategoriesData


class PricesDetailsPageClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    def get(self, request):
        garbage_db_id = self.request.GET.get('id')
        garbage_data = GarbageData.objects.get(id=garbage_db_id)
        return render(request, 'main_app/prices_details_page.html', {'garbage_data': garbage_data})
