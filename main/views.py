import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from main.forms import ContactForm
from orders.models import UserFood, UserOrders
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


@login_required(login_url="login user")
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


class HomeView(ListView):
    template_name = 'home.html'
    context_object_name = 'random'
    model = Recipes

    random_number = random.randint(1, 6700)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        max_id = Recipes.objects.all().values('id').order_by("-id")[0]
        recipe_id1, recipe_id2, recipe_id3 = random.sample(range(1, max_id['id']+1), 3)
        random_recipe = Recipes.objects.filter(id__in=[recipe_id1, recipe_id2, recipe_id3]).values('id', 'name', 'url')
        context['random_recipe'] = random_recipe

        return context


class RecipesListView(LoginRequiredMixin, ListView):
    login_url = 'login user'
    redirect_field_name = 'view cbv recipes'

    template_name = 'products.html'
    model = Recipes
    context_object_name = 'recipes'
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Recipes.objects.filter(name__icontains=query)
        else:
            return Recipes.objects.all()


class RecipesDetailsView(DetailView):
    model = Recipes
    template_name = 'recipe.html'
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = context['recipes']
        products_list = Main.objects.filter(recipe__exact=recipe.id).select_related('product')

        context['heading_text'] = f'{recipe.name} details'
        context['products_list'] = products_list

        order = UserFood.objects.filter(user__exact=self.request.user.id).filter(status=False).select_related('order').values('order')
        if order:
            ordered_recipes = UserOrders.objects.filter(order_id__exact=order[0]['order']).filter(order_start__isnull=False).select_related('recipe').values('recipe')

            for item in ordered_recipes:
                if recipe.id in list(item.values()):
                    context['this_is_ordered'] = 'You already ordered this'

        return context


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, from_email, ['hr.grudev@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contacts.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')
