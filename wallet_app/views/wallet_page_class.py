import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from admin_panel_app.models import WithdrawalsData
from auth_app.models import UsersData
from base_app.functions.send_sms import send_sms
from wallet_app.models import WalletsData


class WalletPageClass(LoginRequiredMixin, View):
    login_url = '/login_page/'
    redirect_field_name = 'LoginPageClass'

    def get(self, request):
        error = self.request.GET.get('error')
        wallet_data = WalletsData.objects.get(user_data=UsersData.objects.get(id=self.request.user.id))
        return render(request, 'wallet_app/wallet_page.html', {'wallet_data': wallet_data, 'error': error})

    def post(self, request):
        withdrawal_amount_input = self.request.POST.get('withdrawal_amount_input')
        sheba_number_input = self.request.POST.get('sheba_number_input')

        user_data = UsersData.objects.get(id=self.request.user.id)
        if user_data.user_firstname is None or user_data.user_lastname is None or user_data.national_code is None:
            return redirect('/wallet_page/?error=account_data')
        else:
            wallet_data = WalletsData.objects.get(user_data=UsersData.objects.get(id=self.request.user.id))
            wallet_data.sheba_number = sheba_number_input
            wallet_data.inventory = wallet_data.inventory - int(withdrawal_amount_input)
            wallet_data.save()

            WithdrawalsData.objects.create(wallet_data=wallet_data, withdrawal_amount=withdrawal_amount_input, request_datetime=datetime.datetime.now(datetime.timezone.utc))
            send_sms(phone_number=wallet_data.user_data.phone_number, message=f'با سلام\nدرخواست شما برای برداشت از حساب «آرتازیست پلاس» ( {withdrawal_amount_input} تومان) با موفقیت ثبت شد.\nاین درخواست حداکثر طی 24 ساعت آینده به حسابتان واریز می‌شود.\nدر صورت عدم دریافت وجه با پشتیبانی تماس حاصل فرمایید.')

            messages.success(request, 'درخواست برداشت با موفقیت ثبت شد')
            return redirect('WalletPageClass')
