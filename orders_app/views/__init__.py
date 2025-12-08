from orders_app.views.cancel_order_class import CancelOrderClass
from orders_app.views.load_garbage_categories_data_class import LoadGarbageCategoriesDataClass
from orders_app.views.load_garbage_items_data_class import LoadGarbageItemsDataClass
from orders_app.views.my_orders_history_page_class import MyOrdersHistoryPageClass
from orders_app.views.order_add_garbage_page_class import OrderAddGarbagePageClass
from orders_app.views.order_datetime_page_class import OrderDatetimePageClass
from orders_app.views.order_delete_garbage_class import OrderDeleteGarbageClass
from orders_app.views.order_details_page_class import OrderDetailsPageClass
from orders_app.views.order_edit_garbage_page_class import OrderEditGarbagePageClass
from orders_app.views.order_garbages_list_page_class import OrderGarbagesListPageClass
from orders_app.views.order_map_page_class import OrderMapPageClass
from orders_app.views.save_selected_address_class import SaveSelectedAddressClass

__all__ = [
    'OrderMapPageClass',
    'OrderGarbagesListPageClass',
    'OrderAddGarbagePageClass',
    'MyOrdersHistoryPageClass',
    'LoadGarbageCategoriesDataClass',
    'LoadGarbageItemsDataClass',
    'OrderDatetimePageClass',
    'OrderEditGarbagePageClass',
    'OrderDeleteGarbageClass',
    'CancelOrderClass',
    'OrderDetailsPageClass',
    'SaveSelectedAddressClass',
]
