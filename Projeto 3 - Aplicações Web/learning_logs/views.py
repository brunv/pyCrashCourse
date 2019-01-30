from django.shortcuts import render
from .models import Topic

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


def topics(request):
    """Mostra todos os assuntos."""

    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning-Logs/topics.html', context)


#       Inicialmente importamos o modelo associado aos dados de que precisamos.
#       A função 'topics()' exige um parâmetro: o objeto 'request' que Django
#       recebeu do servidor. Em seguida, consultamos o banco de dados pedindo os
#       objetos 'Topic', ordenados de acordo com o atributo 'date_added'.
#
#       Na sequência definimos um contexto que será enviado ao template. Um
#       contexto é um dicionário em que as chaves são os nomes que usaremos no
#       template para acessar os dados e os valores são os dados que devemos
#       enviar ao template.
#
#       Ao construir uma página que use dados, passamos a variável 'context' para
#       'render()', além do objeto 'request' e o path do template.