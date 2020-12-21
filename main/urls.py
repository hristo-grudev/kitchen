from django.urls import path

from main.views import list_recipes, products_page, contacts_page, home_page

urlpatterns = [
    path('', home_page, name='home'),
    path('products/', products_page, name='products'),
    path('contacts/', contacts_page, name='contacts'),

]
