from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, View, TemplateView

import stripe

from .models import Item
from MiniMarket import settings


class ItemListView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'MarketApp/items.html'


class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'MarketApp/item_details.html'


class CreateItem(View):
    def post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        item = Item.objects.get(id=kwargs['pk'])

        new_price = stripe.Price.create(
            currency="usd",
            unit_amount=round(item.price * 100),
            product_data={'name': item.name}
        )

        session = stripe.checkout.Session.create(
            line_items=[{"price": new_price.get('id'), "quantity": 1}],
            mode='payment',
            success_url='http://127.0.0.1:8000/success/',
            cancel_url='http://127.0.0.1:8000/reject/'
        )
        return JsonResponse({'sessionId': session['id']})


class SuccessView(TemplateView):
    template_name = 'MarketApp/acceptation/Success.html'


class RejectView(TemplateView):
    template_name = 'MarketApp/acceptation/Rejection.html'
