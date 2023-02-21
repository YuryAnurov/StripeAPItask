from django.contrib import admin
from .models import Item, Order

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'fprice', 'fdescription')

admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
