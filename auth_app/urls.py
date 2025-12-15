from django.urls import path
from . import views

urlpatterns = [
    path('first_message_page/', views.FirstMessagePageClass.as_view(), name='FirstMessagePageClass'),
    path('login_page/', views.LoginPageClass.as_view(), name='LoginPageClass'),
    path('register/', views.LoginPageClass.as_view()),
    path('account_settings_page/', views.AccountSettingsPageClass.as_view(), name='AccountSettingsPageClass'),
    path('verify_code_page/', views.VerifyCodePageClass.as_view(), name='VerifyCodePageClass'),
    path('fill_user_data_page/', views.FillUserDataPageClass.as_view(), name='FillUserDataPageClass'),
    path('logout/', views.LogoutClass.as_view(), name='LogoutClass'),
]