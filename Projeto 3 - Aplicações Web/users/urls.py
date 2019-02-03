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

    # Página de logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


#       No Django 2.0+, o 'namesapce' do app é definido pela variável 'app_name' e
#       não há necessidade do uso de expressões regulares.
#
#       Como estamos usando uma view padrão de Django, a 'LoginView', a sintaxe
#       fica um pouco diferente. Para usar um template nosso, passamos o argumento
#       'template_name' com o caminho para tal template.
#
#       No URL de logout utilizamos a view 'LogoutView' default. Também não
#       nenhum argumento de template pois não há template de logout.