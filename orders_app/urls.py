from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('order_map_page/', views.OrderMapPageClass.as_view(), name='OrderMapPageClass'),
    path('order_garbages_list_page/', views.OrderGarbagesListPageClass.as_view(), name='OrderGarbagesListPageClass'),
    path('order_add_garbage_page/', views.OrderAddGarbagePageClass.as_view(), name='OrderAddGarbagePageClass'),
    path('order_add_garbage_page/', views.OrderAddGarbagePageClass.as_view()),
    path('my_orders_history_page/', views.MyOrdersHistoryPageClass.as_view(), name='MyOrdersHistoryPageClass'),
    path('load_garbage_categories_data/', csrf_exempt(views.LoadGarbageCategoriesDataClass.as_view()), name='LoadGarbageCategoriesDataClass'),
    path('load_garbage_items_data/', csrf_exempt(views.LoadGarbageItemsDataClass.as_view()), name='LoadGarbageItemsDataClass'),
    path('order_datetime_page/', views.OrderDatetimePageClass.as_view(), name='OrderDatetimePageClass'),
    path('order_edit_garbage_page/', views.OrderEditGarbagePageClass.as_view(), name='OrderEditGarbagePageClass'),
    path('order_delete_garbage/', views.OrderDeleteGarbageClass.as_view(), name='OrderDeleteGarbageClass'),
    path('cancel_order/', views.CancelOrderClass.as_view(), name='CancelOrderClass'),
    path('order_details_page/', views.OrderDetailsPageClass.as_view(), name='OrderDetailsPageClass'),
    path('save_selected_address/', csrf_exempt(views.SaveSelectedAddressClass.as_view()), name='SaveSelectedAddressClass'),
]