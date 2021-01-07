import random

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from main.models import Recipes


class KitchenView(PermissionRequiredMixin, ListView):
    template_name = 'home.html'
    context_object_name = 'random'
    model = Recipes

    random_number = random.randint(1, 6700)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        max_id = Recipes.objects.all().values('id').order_by("-id")[0]
        recipe_id1, recipe_id2, recipe_id3 = random.sample(range(1, max_id['id'] + 1), 3)
        random_recipe = Recipes.objects.filter(id__in=[recipe_id1, recipe_id2, recipe_id3]).values('id', 'name', 'url')
        context['random_recipe'] = random_recipe

        return context


class ShoppingCartView(ListView):
    template_name = 'shopping_cart.html'
    context_object_name = 'random'
    model = Recipes

    random_number = random.randint(1, 6700)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        max_id = Recipes.objects.all().values('id').order_by("-id")[0]
        recipe_id1, recipe_id2, recipe_id3 = random.sample(range(1, max_id['id'] + 1), 3)
        random_recipe = Recipes.objects.filter(id__in=[recipe_id1, recipe_id2, recipe_id3]).values('id', 'name', 'url')
        context['random_recipe'] = random_recipe
        print(context['random_recipe'][0])

        return context
