from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import ListView, DetailView

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


@group_required(groups=['God User'])
def products_page(request):
    recipes_list = Recipes.objects.all()
    paginator = Paginator(recipes_list, 25)
    page = request.GET.get('page')
    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        recipes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        recipes = paginator.page(paginator.num_pages)
    context = {
        'recipesForm': RecipesForm,
        'recipes': recipes,
    }
    if context['recipesForm']:
        print(RecipesForm)
    return render(request, 'products.html', context)


@login_required(login_url="register user")
def contacts_page(request):
    context = {
        'tel': '0883358501',
    }
    return render(request, 'contacts.html', context)


def view_recipe(request):
    context = {
        'tel': '0883358501',
    }
    return render(request, 'recipe.html', context)


class RecipesListView(ListView):
    template_name = 'products.html'
    model = Recipes
    context_object_name = 'recipes'
    paginate_by = 25


class RecipesDetailsView(DetailView):
    model = Recipes
    template_name = 'recipe.html'
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        recipe = context['recipes']
        products_list = Main.objects.filter(recipe__exact=recipe.id).select_related('product')

        context['heading_text'] = f'{recipe.name} details'
        context['products_list'] = products_list
        return context
