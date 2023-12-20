from django.urls import path
from .views import ItemListView, ItemDetailView

urlpatterns = [
    path('', ItemListView.as_view(), name='items_list'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_details'),
]
