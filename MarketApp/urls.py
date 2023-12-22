from django.urls import path
from .views import ItemListView, ItemDetailView, CreateItem, SuccessView, RejectView

urlpatterns = [
    path('', ItemListView.as_view(), name='items_list'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_details'),
    path('buy/<int:pk>/', CreateItem.as_view(), name='create_item'),
    path('success/', SuccessView.as_view(), name='success'),
    path('reject/', RejectView.as_view(), name='reject'),
]
