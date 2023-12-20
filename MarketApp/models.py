from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item_details', kwargs={'pk': self.id})
