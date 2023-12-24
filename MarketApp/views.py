from decimal import Decimal
from random import choice

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, View, TemplateView

import stripe

from .models import Item, Order, Tax, Discount
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
        order = Order.objects.get(user__username=self.request.user.username)
        print(order.id)

        new_price = stripe.Price.create(
            currency="usd",
            unit_amount=round(order.price_with_tax() * 100),
            product_data={'name': ','.join([name.name for name in order.item.all()])}
        )

        session = stripe.checkout.Session.create(
            line_items=[{"price": new_price.get('id'), "quantity": 1}],
            mode='payment',
            success_url='http://127.0.0.1:8000/success/',
            cancel_url='http://127.0.0.1:8000/reject/'
        )
        '''
        Но хочу подметить что такой способ уже устарел 
        и есть более лаконичный и простой способ реализовать редирект
        на checkOut форму. Также хотелось бы подметить что нынешняя реализация
        имеет типовую проблему с не корректным отображением формы оплаты
        а точнее вообще её не отображения, это связано как раз таки с
        устарением метода.
        '''
        return JsonResponse({'sessionId': session['id']})


class CreateOrUpdateOrderItem(View):
    def post(self, request, *args, **kwargs):
        ordered_item = Item.objects.get(id=kwargs.get('pk'))
        discount = choice([dsc.id for dsc in Discount.objects.all()])
        create_order, created = Order.objects.update_or_create(user=request.user,
                                                               tax=Tax.objects.all().first(),
                                                               defaults={'discount': Discount.objects.get(id=discount)}
                                                               )
        create_order.item.add(ordered_item)
        return HttpResponseRedirect(reverse('order_items', kwargs={'slug': create_order.user.username}))


class OrderItems(DetailView):
    model = Order
    context_object_name = 'items'
    template_name = 'MarketApp/order_items.html'
    slug_field = 'user__username'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class SuccessView(TemplateView):
    template_name = 'MarketApp/acceptation/Success.html'


class RejectView(TemplateView):
    template_name = 'MarketApp/acceptation/Rejection.html'
