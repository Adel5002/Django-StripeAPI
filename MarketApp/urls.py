from django.urls import path
from .views import ItemListView, ItemDetailView, CreateItem, SuccessView, RejectView, CreateOrUpdateOrderItem, \
    OrderItems

urlpatterns = [
    path('', ItemListView.as_view(), name='items_list'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_details'),
    path('buy/<int:pk>/', CreateItem.as_view(), name='create_item'),
    path('success/', SuccessView.as_view(), name='success'),
    path('reject/', RejectView.as_view(), name='reject'),

    path('add-item-order/<int:pk>/', CreateOrUpdateOrderItem.as_view(), name='create_order_item'),
    path('ordered-items/<slug:slug>/', OrderItems.as_view(), name='order_items'),
]
