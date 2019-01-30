from django.shortcuts import render

# Create your views here.
def index(request):
    """A página inicial de Learning Log."""

    return render(request, 'learning_logs/index.html')


#       Quando uma requisição de URL corresponder ao padrão que definimos em
#       'urls.py' de leraning_logs, o Django procurará uma função chamada 'index()'
#       neste arquivo 'views.py'.
#
#       A função 'render()' utiliza dois argumentos - o objeto 'request' original e
#       um template que pode ser usado para construir a página.