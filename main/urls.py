from django.urls import path

from main.views import list_recipes, products_page, contacts_page, home_page, view_recipe, RecipesListView, RecipesDetailsView

urlpatterns = [
    path('', home_page, name='home'),
    path('products/', products_page, name='products'),
    path('contacts/', contacts_page, name='contacts'),
    path('recipe/', RecipesListView.as_view(), name='view cbv recipes'),
    path('recipe/<int:pk>', RecipesDetailsView.as_view(), name='view recipe'),

]
