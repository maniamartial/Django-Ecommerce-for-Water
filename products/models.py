from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


from django.db.models.deletion import CASCADE
from django.db.models.fields import NullBooleanField
# Create your models here.


# Initializing the Water Products Categiories
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brands(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(null=False, blank=False)
    title = models.CharField(max_length=2000, null=False, blank=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=True, null=False)
    brand = models.ForeignKey(Brands, on_delete=CASCADE, default=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    delivery_time = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    digital = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.title


class Order(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderItems = self.orderitem_set.all()
        for i in orderItems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_totals(self):
        orderitems = self.orderitem_set.all()
        total = sum(item.get_total for item in orderitems)
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum(item.quantity for item in orderitems)
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @ property
    def get_total(self):
        total = self.product.price*self.quantity
        return total

    def _str__(self):
        return self.product


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.city)


class Service(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=64, null=False, blank=False)
    location = models.CharField(max_length=64)
    number = models.CharField(max_length=10, blank=True, default=1)
    description = models.TextField(max_length=400, blank=True, default='None')
    time = models.CharField(max_length=64, null=True, default='1')
    specification_service = models.CharField(
        max_length=64, blank=True, default='poool')
    size = models.CharField(max_length=100, blank=True, default='100 by 100')
    fee = models.IntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location
