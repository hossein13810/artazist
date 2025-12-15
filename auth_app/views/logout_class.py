from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


class LogoutClass(View):
    def get(self, request):
        self.request.session['register_user_data'] = None
        self.request.session.modified = True
        logout(self.request)
        return redirect('LoginPageClass')