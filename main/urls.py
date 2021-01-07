from django.urls import path

from main.views import products_page, RecipesListView, RecipesDetailsView, HomeView, contactView
from orders.views import KitchenView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', products_page, name='products'),
    path('contacts/', contactView, name='contacts'),
    path('kitchen/', KitchenView.as_view(), name='kitchen'),
    path('recipe/', RecipesListView.as_view(), name='view cbv recipes'),
    path('recipe/<int:pk>', RecipesDetailsView.as_view(), name='view recipe'),

]
