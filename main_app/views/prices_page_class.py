from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from main_app.models import GarbageData, GarbageCategoriesData


class PricesPageClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    @staticmethod
    def get(request):
        garbage_data = GarbageData.objects.all()
        return render(request, 'main_app/prices_page.html', {'garbage_data': garbage_data})
