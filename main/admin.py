from django.contrib import admin

from main.models import Products, Main, Order, Recipes

admin.site.register(Recipes)
admin.site.register(Products)
admin.site.register(Main)
admin.site.register(Order)
