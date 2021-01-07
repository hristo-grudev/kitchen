from django.contrib import admin

from main.models import Products, Main, Order, Recipes
from orders.models import UserOrders, UserFood, CookFood

admin.site.register(Recipes)
admin.site.register(Products)
admin.site.register(Main)
admin.site.register(UserOrders)
admin.site.register(UserFood)
admin.site.register(CookFood)
