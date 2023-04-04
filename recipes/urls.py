from django.urls import path

from . import views

# HTTP REQUEST <- HTTP RESPONSE - cliente pede servidor responde

# HTTP REQUEST

# recipes:recipe namespace
app_name = 'recipes'

urlpatterns = [
    # path recebe um rota e uma função que está dentro de um app
    # a função path chamou minha view e passou um argumento "request"
    path('', views.home, name="home"),
    path('recipes/search/', views.search, name="search"),
    path('recipes/category/<int:category_id>/',
         views.category, name="category"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),

]
