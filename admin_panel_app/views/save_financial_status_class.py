import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from admin_panel_app.models import WithdrawalsData
from base_app.functions.send_sms import send_sms
from base_app.mixins import RoleRequiredMixin


class SaveFinancialStatusClass(LoginRequiredMixin, RoleRequiredMixin, View):
    login_url = '/admin_login_page/'
    redirect_field_name = 'AdminLoginPageClass'
    required_roles = ['financial_requests_list_page', 'write_financial_requests_list_page']

    def get(self, request):
        withdrawal_id = self.request.GET.get('id')
        withdrawal_data = WithdrawalsData.objects.get(id=withdrawal_id)
        withdrawal_data.status = True
        withdrawal_data.pay_datetime = datetime.datetime.now(datetime.timezone.utc)
        send_sms(phone_number=withdrawal_data.wallet_data.user_data.phone_number, message=f'با سلام\nدرخواست برداشت وجه از کیف پول «آرتازیست پلاس» تایید شد و مبلغ {withdrawal_data.withdrawal_amount} تومان به حساب شما با شماره شبا {withdrawal_data.wallet_data.sheba_number} واریز شد.\nدر صورت عدم دریافت وجه با پشتیبانی تماس حاصل فرمایید.')
        withdrawal_data.save()
        messages.success(request, 'وضعیت درخواست با موفقیت تغییر یافت')
        return redirect('FinancialRequestsListPageClass')

    def post(self, request):
        req_id_input = self.request.POST.get('req_id_input')
        text_area_input = self.request.POST.get('text_area_input')
        withdrawal_data = WithdrawalsData.objects.get(id=req_id_input)
        withdrawal_data.status = False
        send_sms(phone_number=withdrawal_data.wallet_data.user_data.phone_number, message=f'با سلام\nدرخواست برداشت وجه از کیف پول «آرتازیست پلاس» به علت بروز مشکل رد شد. علت مشکل:\n {text_area_input}')
        withdrawal_data.save()
        messages.success(request, 'وضعیت درخواست با موفقیت تغییر یافت')
        return redirect('FinancialRequestsListPageClass')
