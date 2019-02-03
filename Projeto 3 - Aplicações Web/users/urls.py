"""Define padrões de URL para users."""

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'
urlpatterns = [
    # Página de login
    path('login/',
        auth_views.LoginView.as_view(template_name='users/login.html'),
        name='login'),
]


#       No Django 2.0+, o 'namesapce' do app é definido pela variável 'app_name' e
#       não há necessidade do uso de expressões regulares.
#
#       Como estamos usando uma view padrão de Django, a 'LoginView', a sintaxe
#       fica um pouco diferente. Para usar um template nosso, passamos o argumento
#       'template_name' com o caminho para tal template.