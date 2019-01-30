"""Define padrões de URL para learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index')
]

#       No Django 2.0, o 'namesapce' do app é definido pela variável 'app_name' e
#       não há necessidade do uso de expressões regulares.
#
#       Para deixar claro com qual 'urls.py' estamos trabalhando, adicionamos uma
#       docstring no início do arquivo.
#       Também importamos o os módulos path e views. O ponto diz a Python para
#       importar views do mesmo diretório em que está este módulo 'urls.py'.
#
#       A variável 'urlpatterns' nesse módulo é uma lista de páginas individuais
#       que podem ser solicitadas a partir de uma aplicação 'learning_logs'.
#
#       O primeiro argumento de 'path', a string vazia '', corresponde ao URL-base.
#       Qualquer outro URL que não existir fará Django devolver uma página de erro.
#       O segundo argumento espcifica qual função da view deve ser chamada.
#       O terceiro argumento fornece o nome 'index' para esse padrão URL para que
#       possamos referenciá-lo em outras seções do código.