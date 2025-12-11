from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from base_app.mixins import RoleRequiredMixin
from main_app.models import GarbageCategoriesData, UnitsOfMeasurementData, GarbageData


class EditGarbagePageClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['data_definition_page']

    def get(self, request):
        garbage_id = self.request.GET.get('garbage_id')
        garbage_data = GarbageData.objects.get(id=garbage_id)
        categories_data = GarbageCategoriesData.objects.all().order_by('-id')
        units_data = UnitsOfMeasurementData.objects.all().order_by('-id')
        return render(request, 'admin_panel_app/edit_garbage_page.html', {'categories_data': categories_data, 'units_data': units_data, 'garbage_data': garbage_data})

    def post(self, request):
        garbage_id = self.request.POST.get('garbage_id')
        garbage_item_name_input = self.request.POST.get('garbage_item_name_input')
        unit_input = self.request.POST.get('unit_input')
        price_input = self.request.POST.get('price_input')
        icon_input = self.request.FILES.get('icon_input')
        image_input = self.request.FILES.get('image_input')
        description_input = self.request.POST.get('description_input')

        if GarbageData.objects.filter(garbage_item_name=garbage_item_name_input).exclude(id=garbage_id).exists():
            messages.error(request, 'یک زباله با این نام وجود دارد')
            return redirect(f'/edit_garbage_page/?garbage_id={garbage_id}')
        else:
            garbage_data = GarbageData.objects.get(id=garbage_id)
            garbage_data.garbage_item_name = garbage_item_name_input
            garbage_data.units_of_measurement_data = unit_input
            garbage_data.price_per_unit = price_input
            garbage_data.description = description_input
            if icon_input:
                garbage_data.garbage_icon = icon_input
            if image_input:
                garbage_data.garbage_image = image_input
            garbage_data.save()
            messages.success(request, 'ویرایش زباله با موفقیت انجام شد')
            return redirect('DataDefinitionGarbagesDataPageClass')
