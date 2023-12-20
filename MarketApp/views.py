from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Item


class ItemListView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'MarketApp/items.html'


class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'MarketApp/item_details.html'





