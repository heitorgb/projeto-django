from django.urls import path
from recipes.views import home

# HTTP REQUEST <- HTTP RESPONSE - cliente pede servidor responde

# HTTP REQUEST


urlpatterns = [
    # path recebe um rota e uma função que está dentro de um app
    # a função path chamou minha view e passou um argumento "request"
    path('', home),

]
