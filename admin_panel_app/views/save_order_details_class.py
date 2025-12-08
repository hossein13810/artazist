from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from base_app.functions.send_sms import send_sms
from base_app.mixins import RoleRequiredMixin
from main_app.models import GarbageData
from orders_app.models import OrdersData, OrderGarbagesData
from wallet_app.models import WalletsData


class SaveOrderDetailsClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['orders_list_page', 'write_orders_list_page']

    def post(self, request):
        access_token = self.request.POST.get('access_token')
        print(access_token)

        garbages_data = []
        garbage_num = 1
        while True:
            garbage_list_select = self.request.POST.get(f'garbage_list_select_{garbage_num}')
            garbage_amount_input = self.request.POST.get(f'garbage_amount_input_{garbage_num}')
            if garbage_list_select is not None:
                garbages_data.append({
                    'garbage_list_select': garbage_list_select,
                    'garbage_amount_input': garbage_amount_input,
                })
            else:
                break
            garbage_num += 1

        order_data = OrdersData.objects.get(access_token=access_token)
        order_data.order_status = True
        order_data.save()

        all_price = 0
        for garbage in garbages_data:
            garbage_data = GarbageData.objects.get(id=garbage['garbage_list_select'])
            all_price += garbage_data.price_per_unit * int(garbage['garbage_amount_input'])
            OrderGarbagesData.objects.create(order_data=order_data, garbage_data=garbage_data, garbage_amount=garbage['garbage_amount_input'])

        wallet_data = WalletsData.objects.get(user_data=order_data.user_data)
        wallet_data.inventory = wallet_data.inventory + all_price
        wallet_data.save()

        send_sms(phone_number=order_data.user_data.phone_number, message=f'با سلام.\nدرخواست شما در «آرتازیست پلاس» به شماره پیگیری "{order_data.access_token}" توسط اپراتور تایید شد و مبلغ {all_price} تومان به کیف پول شما اضافه شد.\n')

        messages.success(request, 'وضعیت درخواست با موفقیت تغییر یافت')
        return redirect('OrdersListPageClass')
