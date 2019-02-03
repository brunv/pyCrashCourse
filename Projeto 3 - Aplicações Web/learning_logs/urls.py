"""Define padrões de URL para learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Mostra todos os assuntos
    path('topics/', views.topics, name='topics'),

    # Página de detalhes para um único assunto
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Página para adicionar um novo assunto
    path('new_topic/', views.new_topic, name='new_topic'),

    # Página para adidiconar uma nova entrada
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Página para editar uma entrada
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
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
#
#       Qualquer requisição com um URL que corresponda a esse padrão será então
#       passada para a função 'topics()' em 'views.py'.
#
#       Dentro do colchete angular (<>) devemos descrever o tipo de variável
#       esperada e providenciar um nome para o valor no URL.