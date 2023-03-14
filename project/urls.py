"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# HTTP REQUEST <- HTTP RESPONSE - cliente pede servidor responde

# HTTP REQUEST


urlpatterns = [
    path('admin/', admin.site.urls),
    # include precisa ser passado uma string que contem o seu app e o seu arquivo
    path('', include('recipes.urls'))
    # path recebe um rota e uma função que está dentro de um app
    # a função path chamou minha view e passou um argumento "request"
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# usamos esse comando para acessar as imagens que fizemos o upload
