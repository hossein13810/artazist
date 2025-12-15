from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.http import JsonResponse
from django.views import View

from main_app.models import GarbageCategoriesData, GarbageData


class LoadGarbageItemsDataClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    def post(self, request):
        category_db_id = self.request.POST.get('category_db_id')
        garbage_items_data = GarbageData.objects.filter(garbage_categories_data_id=category_db_id).annotate(unit_name=F('units_of_measurement_data__unit_name')).values()

        return JsonResponse(list(garbage_items_data), safe=False)
