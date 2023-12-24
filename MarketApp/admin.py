from django.contrib import admin
from .models import Item, Order, Tax, Discount


class ModelItem(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.register(Item, ModelItem)
admin.site.register(Order)
admin.site.register(Tax)
admin.site.register(Discount)
