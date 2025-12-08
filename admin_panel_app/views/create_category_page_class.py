from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from auth_app.models import UsersData, UserPermissions
from base_app.mixins import RoleRequiredMixin
from main_app.models import GarbageCategoriesData
from wallet_app.models import WalletsData


class CreateCategoryPageClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['data_definition_page']

    @staticmethod
    def get(request):
        return render(request, 'admin_panel_app/create_category_page.html')

    def post(self, request):
        category_name_input = self.request.POST.get('category_name_input')
        description_input = self.request.POST.get('description_input')

        if GarbageCategoriesData.objects.filter(categories_name=category_name_input).exists():
            messages.error(request, 'یک دسته بندی با این نام وجود دارد')
            return redirect('CreateCategoryPageClass')
        else:
            GarbageCategoriesData.objects.create(categories_name=category_name_input, description=description_input)
            messages.success(request, 'دسته بندی جدید با موفقیت ایجاد شد')
            return redirect('DataDefinitionGarbagesDataPageClass')
