from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from decimal import Decimal


class Item(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item_details', kwargs={'pk': self.id})


class Discount(models.Model):
    discount = models.DecimalField(max_digits=5, decimal_places=2)


class Tax(models.Model):
    tax = models.DecimalField(max_digits=5, decimal_places=2)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(Item)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, related_name='item_discount')
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True, related_name='item_tax')

    def __str__(self):
        return self.user.username

    def price_with_tax(self):
        total = sum(Decimal(i.price) for i in self.item.all())
        with_tax = total / Decimal(self.tax.tax)
        discount = (with_tax + total) / 100 * Decimal(self.discount.discount)
        with_discount = (with_tax + total) - discount

        return round(with_discount, 2)

    def get_total_price(self):
        total = sum(Decimal(i.price) for i in self.item.all())

        return total
