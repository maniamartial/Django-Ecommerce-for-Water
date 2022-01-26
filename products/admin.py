

from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.
from .models import Brands, Category, Order, OrderItem, Product, Service, ShippingAddress


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'is_published', 'created_at')
    list_display_links = ('id', 'title')
    list_filter = ('price', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('title', 'price')
    ordering = ('price',)
    #exclude = ('description',)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'location', 'number', 'fee')


# Registering the water Products
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brands)


admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Service, ServiceAdmin)
