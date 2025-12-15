from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from base_app.mixins import RoleRequiredMixin
from main_app.models import GarbageCategoriesData, UnitsOfMeasurementData, GarbageData


class CreateGarbagePageClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['data_definition_page']

    @staticmethod
    def get(request):
        categories_data = GarbageCategoriesData.objects.all().order_by('-id')
        units_data = UnitsOfMeasurementData.objects.all().order_by('-id')
        return render(request, 'admin_panel_app/create_garbage_page.html', {'categories_data': categories_data, 'units_data': units_data})

    def post(self, request):
        garbage_item_name_input = self.request.POST.get('garbage_item_name_input')
        unit_input = self.request.POST.get('unit_input')
        price_input = self.request.POST.get('price_input')
        icon_input = self.request.FILES.get('icon_input')
        image_input = self.request.FILES.get('image_input')
        description_input = self.request.POST.get('description_input')

        if GarbageData.objects.filter(garbage_item_name=garbage_item_name_input).exists():
            messages.error(request, 'یک زباله با این نام وجود دارد')
            return redirect('CreateGarbagePageClass')
        else:
            GarbageData.objects.create(garbage_item_name=garbage_item_name_input, units_of_measurement_data=unit_input, price_per_unit=price_input, garbage_icon=icon_input, garbage_image=image_input, description=description_input)
            messages.success(request, 'زباله جدید با موفقیت ایجاد شد')
            return redirect('DataDefinitionGarbagesDataPageClass')
