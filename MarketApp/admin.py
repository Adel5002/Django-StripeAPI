from django.contrib import admin
from .models import Item


class ModelItem(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.register(Item, ModelItem)
