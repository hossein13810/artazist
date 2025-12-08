from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View

from admin_panel_app.models import WithdrawalsData
from base_app.mixins import RoleRequiredMixin
from orders_app.models import OrdersData


class LoadFinancialRequestsDataClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['financial_requests_list_page']

    @staticmethod
    def post(request):
        data_list = WithdrawalsData.objects.all().order_by('-id').values('id', 'withdrawal_amount', 'status', 'wallet_data__user_data__user_firstname', 'wallet_data__user_data__user_lastname', 'wallet_data__user_data__phone_number', 'wallet_data__sheba_number')

        withdrawals_data = [
            {
                **item,
                'get_jalali_request_datetime': WithdrawalsData.objects.get(id=item['id']).get_jalali_request_datetime(),
            }
            for item in data_list
        ]

        return JsonResponse(list(withdrawals_data), safe=False)
