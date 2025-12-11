from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('main_page/', views.MainPageClass.as_view(), name='MainPageClass'),
    path('prices_page/', views.PricesPageClass.as_view(), name='PricesPageClass'),
    path('about_us_page/', views.AboutUsPageClass.as_view(), name='AboutUsPageClass'),
    path('selected_address_page/', views.SelectedAddressPageClass.as_view(), name='SelectedAddressPageClass'),
    path('load_new_orders_list/', csrf_exempt(views.LoadNewOrdersListClass.as_view()), name='LoadNewOrdersListClass'),
    path('delete_selected_address/', views.DeleteSelectedAddressClass.as_view(), name='DeleteSelectedAddressClass'),
    path('save_identification_code/', csrf_exempt(views.SaveIdentificationCodeClass.as_view()), name='SaveIdentificationCodeClass'),
    path('prices_details_page/', views.PricesDetailsPageClass.as_view(), name='PricesDetailsPageClass'),
]
