from django.contrib import admin

from orders_app.models import OrderGarbagesData, OrdersData, SelectedAddressData

admin.site.register(OrderGarbagesData)
admin.site.register(OrdersData)
admin.site.register(SelectedAddressData)
