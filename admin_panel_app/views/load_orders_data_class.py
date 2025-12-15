from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View

from base_app.mixins import RoleRequiredMixin
from orders_app.models import OrdersData


class LoadOrdersDataClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['orders_list_page']

    @staticmethod
    def post(request):
        orders_data = OrdersData.objects.filter(delete_status=False).exclude(order_title=None).order_by('-id').values('id', 'order_title', 'user_data__user_firstname', 'user_data__user_lastname', 'user_data__phone_number', 'created_datetime', 'order_date', 'order_from_time', 'order_to_time', 'order_status', 'access_token', 'order_map_lat_location', 'order_map_lng_location')

        orders_data = [
            {
                **item,
                'get_jalali_created_datetime': OrdersData.objects.get(id=item['id']).get_jalali_created_datetime(),
                'get_str_order_date': OrdersData.objects.get(id=item['id']).get_str_order_date(),
                'order_timeline': OrdersData.objects.get(id=item['id']).get_jalali_order_timeline()
            }
            for item in orders_data
        ]

        return JsonResponse(list(orders_data), safe=False)
