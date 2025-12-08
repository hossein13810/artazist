from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from main_app.models import GarbageData, GarbageCategoriesData


class PricesPageClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    @staticmethod
    def get(request):
        categories_data = GarbageCategoriesData.objects.all()

        prices_data_dict = {}
        for category in categories_data:
            prices_data_dict[category.categories_name] = GarbageData.objects.filter(garbage_categories_data=category)

        return render(request, 'main_app/prices_page.html', {'prices_data_dict': prices_data_dict})
