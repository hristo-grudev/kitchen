from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .decorators import group_required
from .forms import RecipesForm
from main.models import Recipes, Products, Main
from random import choice


def list_recipes(request):
    products = Products.objects.filter(name__icontains='гъби').values('id', 'name')
    product_id = products[0]['id']
    recipes = Main.objects.filter(product_id=product_id).values('recipe_id')
    recipes_list = []
    for reci in recipes:
        recipes_list.append(reci['recipe_id'])
    random_recipe = choice(recipes_list)
    recipe_name = Recipes.objects.filter(id=random_recipe).values('id', 'name')
    recipe_id = recipe_name[0]['id']
    recipe_name = recipe_name[0]['name']

    products_for_recipe = Main.objects.filter(recipe_id=recipe_id).values('product_id')
    products_names = Products.objects.filter(id__in=products_for_recipe).values('id', 'name').order_by('name')

    context = {'recipe_name': recipe_name, 'products_names': products_names, 'products_for_recipe': products_for_recipe}
    return render(request, 'index.html', context)


def home_page(request):
    return render(request, 'home.html')


@login_required(login_url="register user")
def products_page(request):
    context = {
        'recipesForm': RecipesForm,
    }
    if context['recipesForm']:
        print(RecipesForm)
    return render(request, 'products.html', context)


@group_required(groups=['God User'])
def contacts_page(request):
    context = {
        'tel': '0883358501',
    }
    return render(request, 'contacts.html', context)
