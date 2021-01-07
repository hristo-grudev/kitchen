from django.urls import path

from orders.views import ShoppingCartView

urlpatterns = [
    path('', ShoppingCartView.as_view(), name='shopping cart'),
    # path('recipe/<int:pk>', RecipesDetailsView.as_view(), name='view recipe'),

]
