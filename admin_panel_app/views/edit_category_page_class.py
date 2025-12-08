from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from auth_app.models import UsersData, UserPermissions
from base_app.mixins import RoleRequiredMixin
from main_app.models import GarbageCategoriesData
from wallet_app.models import WalletsData


class EditCategoryPageClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['data_definition_page']

    def get(self, request):
        category_id = self.request.GET.get('category_id')
        category_data = GarbageCategoriesData.objects.get(id=category_id)
        return render(request, 'admin_panel_app/edit_category_page.html', {'category_data': category_data})

    def post(self, request):
        category_id = self.request.POST.get('category_id')
        category_name_input = self.request.POST.get('category_name_input')
        description_input = self.request.POST.get('description_input')

        if GarbageCategoriesData.objects.filter(categories_name=category_name_input).exclude(id=category_id).exists():
            messages.error(request, 'یک دسته بندی با این نام وجود دارد')
            return redirect(f'/edit_category_page/?category_id={category_id}')
        else:
            category_data = GarbageCategoriesData.objects.get(id=category_id)
            category_data.categories_name = category_name_input
            category_data.description = description_input
            category_data.save()
            messages.success(request, 'دسته بندی با موفقیت ویرایش شد')
            return redirect('DataDefinitionGarbagesDataPageClass')
