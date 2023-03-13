from django.shortcuts import render, get_list_or_404
from utils.recipes.factory import make_recipe
from recipes.models import Recipe, Category
# Create your views here.


def home(request):
    # buscando apenas receitas que estão marcadas como publicadas
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })
    # return HTTP RESPONSE


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id')
    )  # retorna uma lista e não um queryset ent usamos o indice[] para acessa-la
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category |'
    })


def recipe(request, id):
    recipe = Recipe.objects.filter(
        pk=id,  # buscando pela primary key
        is_published=True
    ).order_by('-id').first()  # buscando apenas por um ID
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        # caso for true lá na view n irá mostrar algum conteudo que configurar da página
        'is_detail_page': True,
    })
