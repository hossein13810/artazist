from django.urls import path
from . import views

urlpatterns = [
    path('wallet_page/', views.WalletPageClass.as_view(), name='WalletPageClass'),
]
