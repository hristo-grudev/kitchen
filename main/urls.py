from django.urls import path

from main.views import list_recipes

urlpatterns = [
    path('', list_recipes, name='list recipes'),

]
