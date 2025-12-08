from django.shortcuts import render, redirect
from django.views import View


class FirstMessagePageClass(View):

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('LoginPageClass')
        else:
            device_token = self.request.GET.get('device_token')
            self.request.session['device_token'] = device_token
            return render(request, 'auth_app/first_message_page.html')
