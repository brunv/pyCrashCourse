"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('learning_logs.urls'))
]


#       Nesse arquivo 'urls.py', que representa o projeto como um todo, a varável
#       'urlpatterns' inclui os conjuntos de URLs das aplicações do projeto.
#       O código 'admin.site.urls' define todos os URLs que podem ser requisitados
#       a partir do site de administração.
#
#       O segundo path corresponderá a qualquer URL que comece com a palavra
#       'users'. Assim como o terceiro path que corresponde à raiz com '' no URL.
#
#       Os namespaces são criados automaticamente durante o 'include()'. Assim,
#       podemos distinguir os URLs pertencentes à aplicação 'learning_logs' ou
#       'users'.