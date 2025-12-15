from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F, OuterRef, Subquery, Count
from django.shortcuts import render
from django.views import View

from auth_app.models import UsersData
from base_app.mixins import RoleRequiredMixin
from wallet_app.models import WalletsData


class UsersListPageClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['users_list_page']

    def get(self, request):
        wallets_subquery_inventory = WalletsData.objects.filter(user_data=OuterRef('pk')).values('inventory')[:1]
        wallets_subquery_sheba = WalletsData.objects.filter(user_data=OuterRef('pk')).values('sheba_number')[:1]
        users_list = UsersData.objects.filter(master_of_admins=False, is_staff=False, admin_permission=False).exclude(id=self.request.user.id).annotate(wallet_inventory=Subquery(wallets_subquery_inventory), wallet_sheba_number=Subquery(wallets_subquery_sheba), orders_count=Count('ordersdata', distinct=True), withdrawals_count=Count('walletsdata__withdrawalsdata', distinct=True))
        return render(request, 'admin_panel_app/users_list_page.html', {'users_list': users_list})
